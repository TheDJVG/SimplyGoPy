import base64
from builtins import bytearray, len, str
from simplygo import Constants
from enum import Enum, auto
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES

# p014sg.com.transitlink.utility.CryptLib;
class CryptLib:
    _iv = bytearray(16)
    _key = bytearray(32)

    class EncryptMode(Enum):
        ENCRYPT = auto()
        DECRYPT = auto()

    def _encryptDecrypt(self, string: str, mode: EncryptMode):
        key = Constants.ABT_ENCRYPTION_KEY.encode('UTF-8')
        iv = Constants.ABT_ENCRYPTION_IV.encode('UTF-8')

        key_length = len(key)
        iv_length = len(iv)

        if key_length > len(self._key):
            key_length = len(self._key)

        if iv_length > len(self._iv):
            iv_length = len(self._iv)

        self._key = key[:key_length]
        self._iv = iv[:iv_length]

        cipher = AES.new(self._key, AES.MODE_CBC, self._iv)

        if mode is self.EncryptMode.ENCRYPT:
            return base64.b64encode(cipher.encrypt(pad(string.encode('UTF-8'), 16))).decode()

        if mode is self.EncryptMode.DECRYPT:
            return unpad(cipher.decrypt(base64.b64decode(string)), 16).decode()

    def encrypt(self, string: str):
        return self._encryptDecrypt(string, self.EncryptMode.ENCRYPT)

    def decrypt(self, string: str):
        return self._encryptDecrypt(string, self.EncryptMode.DECRYPT)
