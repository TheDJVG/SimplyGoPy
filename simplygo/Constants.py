# From p014sg.transitlink.base.Constants

# Used for HMAC
ABT_APP_ID = "e62e7c778eed4b5ba220a8d3c512a555"
ABT_APP_KEY = "hbssWNf65LyAuYomc4HQTzopBw0MPOY/llZ54mTeKNM="

# Used to encrypt / decrypt username/password send to SimplyGo API. These values seem static.. (secure..).
ABT_ENCRYPTION_IV = "1ZZea_ai9_ceU9iM"
ABT_ENCRYPTION_KEY = "27f0563f0bdc91a37457ea21436766e8c865dc8cd8d42140048820cc48ccddf5"

# Used for Device object
API_APP_VERSION = "5.4.1";

# Fields used for API communication
ABT_API_URL = 'https://abtapp.transitlink.com.sg/'
API_ABT_GET_CARD_LIST = 'api/card/get'
API_ABT_GET_MONTHLY_USAGES = 'api/card/GetUsages'
API_ABT_GET_RECIPIENT = 'api/account/GetRecipient'
API_ABT_GET_TRAIN_STATIONS = 'api/claims/GetTrainStations'
API_ABT_GET_TRANSACTION = 'api/card/Transactions'
API_ABT_NOTIFICATION = 'api/Notification/Get'
API_ABT_SIGN_IN = 'api/account/SignIn'
API_ABT_USER_DETAIL = 'api/account/Get'

# Constants not from the transitlink app
MYSQL_DATE_FORMAT = "%d-%m-%Y"