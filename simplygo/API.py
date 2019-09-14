import requests
import json
import logging
from enum import Enum
from simplygo.CryptLib import CryptLib
from simplygo import Constants, Utility, JsonFields

logger = logging.getLogger(__name__)


class API:
    SESSION_FILE = '/tmp/simplygo.session'

    class HttpMethod(Enum):
        GET = 'GET'
        POST = 'POST'
        PUT = 'PUT'
        DELETE = 'DELETE'

    def __init__(self, user_name, user_pass, session_location=None):
        if session_location:
            self.SESSION_FILE = session_location

        # Store session information here
        self.session_info = None

        # Crypt lib reverse engineered from SimplyGo app.
        simply_crypt = CryptLib()

        # Try to decrypt user_name and make sure it's encrypted.
        try:
            user_name = simply_crypt.decrypt(user_name)
        except ValueError:
            logger.debug("User name was not entered encrypted.")
        finally:
            self.user_name = simply_crypt.encrypt(user_name)

        # Try to decrypt user_password and make sure it's encrypted.
        try:
            user_pass = simply_crypt.decrypt(user_pass)
        except ValueError:
            logger.debug("User password was not entered encrypted.")
        finally:
            self.user_pass = simply_crypt.encrypt(user_pass)

        if not self._resume_session():
            self._authenticate()

    def _test_session(self):
        try:
            self.query_api(Constants.API_ABT_NOTIFICATION)
            logger.debug("Session successfully tested.")
            return True
        except SimplyGoError as e:
            logger.debug("Session test fail: %r", e)
            return False

    def _authenticate(self):
        # We can probably make this more dynamic.
        login_data = {
            'user_email': self.user_name,
            'user_password': self.user_pass,
            'SystemIp': '127.0.0.1',
            'Device': {
                'DeviceId': 1337,
                'AppVersionName': str(Constants.API_APP_VERSION),
                'AppVersionCode': str(Constants.API_APP_VERSION),
                'DeviceType': 1,
                'DeviceBrand': 'Python SimplyGoAPI'
            }
        }
        try:
            self.session_info = self._query_api(Constants.API_ABT_SIGN_IN, login_data, self.HttpMethod.POST)
            logger.debug("Authenticated.")
            with open(self.SESSION_FILE, 'w') as f:
                json.dump(self.session_info, f)
        except OSError as e:
            logger.warn("Unable to write session information: %r", e)

    def _resume_session(self):
        logger.debug("Trying to resume session.")

        try:
            with open(self.SESSION_FILE, 'rb') as f:
                self.session_info = json.load(f)
                self._test_session()
                logger.debug("Session resumed.")
                return True
        except (Exception, FileNotFoundError, SimplyGoError) as e:
            logger.debug("Session cannot be resumed: %r", e)
            return False

    def _query_api(self, endpoint: str, data: json, method: HttpMethod):
        headers = {'Authorization': Utility.encodeHmacSHA256(endpoint, method.value), 'Accept': 'application/json'}
        logger.debug("Signature: %r", headers.get('Authorization'))
        logging.debug("Payload: %r", data)
        try:
            r = requests.request(method.value, Constants.ABT_API_URL + endpoint, headers=headers, json=data)
            resp = r.json()
            logger.debug("API response: %r", resp)
            if resp.get('status_code') == 0:
                raise SimplyGoApiError(resp.get('status_text'))
            return resp.get('data')
        except (ValueError, json.decoder.JSONDecodeError):
            logger.exception("Unable to decode SimplyGO API data.")
        return False

    def query_api(self, endpoint: str, data=None, method=HttpMethod.POST):
        pre_data = {JsonFields.JSON_FIELD_USER_SESS_KEY: self.session_info.get(JsonFields.JSON_FIELD_USER_SESS_KEY)}
        if data:
            pre_data.update(data)
        return self._query_api(endpoint, pre_data, method)


class SimplyGoError(Exception):
    pass


class SimplyGoApiError(SimplyGoError):
    pass
