from simplygo import Constants
import uuid
import urllib.parse
import time
import hmac
import hashlib
import base64


def encodeHmacSHA256(endpoint: str, http_method: str):
    stringList1 = []
    stringList2 = []
    stringList3 = []

    uuid_local = str(uuid.uuid4())
    time_now = str(round(time.time()))

    stringList1.append('https://abtapp.transitlink.com.sg/')
    stringList1.append(endpoint)
    lowercase_url = urllib.parse.quote(''.join(stringList1)).lower()

    stringList2.append(Constants.ABT_APP_ID)
    stringList2.append(http_method)
    stringList2.append(lowercase_url)
    stringList2.append(time_now)
    stringList2.append(uuid_local)
    string = ''.join(stringList2)

    signature = hmac.new(base64.b64decode(Constants.ABT_APP_KEY), msg=string.encode('UTF-8'),
                         digestmod=hashlib.sha256)
    sig_string = base64.b64encode(signature.digest()).decode('UTF-8')

    stringList3.append("amx e62e7c778eed4b5ba220a8d3c512a555:")
    stringList3.append(sig_string)
    stringList3.append(":")
    stringList3.append(uuid_local)
    stringList3.append(":")
    stringList3.append(time_now)
    return ''.join(stringList3)
