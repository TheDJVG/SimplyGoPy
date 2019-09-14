import logging
from builtins import str, isinstance, Exception

from simplygo.CryptLib import CryptLib
from simplygo.API import API, SimplyGoError, SimplyGoApiError
from simplygo import Constants, Utility, JsonFields
from datetime import date, datetime
from calendar import monthrange

logger = logging.getLogger(__name__)


class Ride:

    def __init__(self, user_name, user_pass):
        self.simplygo_api = API(user_name, user_pass)

        self.user_info = None
        self.card_info = None

    def _set_user_info(self):
        data = self.simplygo_api.query_api(Constants.API_ABT_USER_DETAIL)
        for key, value in data.items():
            # Try decrypting data but not password.
            if isinstance(key, str) and key not in ['Password']:
                try:
                    data[key] = CryptLib().decrypt(value)
                except Exception:
                    continue
        self.user_info = data

    def _set_card_info(self):
        self.card_info = self.simplygo_api.query_api(Constants.API_ABT_GET_CARD_LIST)

    def _get_user_info(self, cache=True):
        if not self.user_info or not cache:
            self._set_user_info()
        return self.user_info

    def _get_card_info(self, cache=True):
        if not self.card_info or not cache:
            self._set_card_info()
        return self.card_info

    def get_card_info(self):
        return self._get_card_info()

    def get_user_info(self):
        return self._get_user_info()

    def _get_transactions(self, card_id: str, start_date: date, end_date: date):
        date_info = {JsonFields.JSON_FIELD_CARD_ID: card_id,
                     JsonFields.JSON_FIELD_START_DATE: start_date.strftime(Constants.MYSQL_DATE_FORMAT),
                     JsonFields.JSON_FIELD_END_DATE: end_date.strftime(Constants.MYSQL_DATE_FORMAT)}
        return self.simplygo_api.query_api(Constants.API_ABT_GET_TRANSACTION, date_info)

    def get_transactions(self, card_id: str, start_date=date.today(), end_date=date.today()):
        if not isinstance(start_date, date):
            start_date = datetime.strptime(start_date, Constants.MYSQL_DATE_FORMAT)
        if not isinstance(end_date, date):
            end_date = datetime.strptime(end_date, Constants.MYSQL_DATE_FORMAT)

        return self._get_transactions(card_id, start_date, end_date)

    def get_transactions_this_month(self, card_ids=None):
        start_date = date.today().replace(day=1)
        end_date = start_date.replace(day=monthrange(start_date.year, start_date.month)[1])
        if not card_ids:
            card_ids = [x[JsonFields.JSON_FIELD_UNIQUE_CODE] for x in self.get_card_info() if
                        JsonFields.JSON_FIELD_UNIQUE_CODE in x]
        if isinstance(card_ids, str):
            card_ids = [card_ids]
        return {card_id: self.get_transactions(card_id, start_date, end_date) for card_id in card_ids}

    def get_notifications(self):
        return self.simplygo_api.query_api(Constants.API_ABT_NOTIFICATION)
