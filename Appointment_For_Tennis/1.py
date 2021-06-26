from urllib.parse import urlencode
import requests
ReqHeader = {
    "Host": "newids.seu.edu.cn",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
}
url = "https://newids.seu.edu.cn/authserver/needCaptcha.html?"
querydata = {
    "username" : "213183668",
    "pwdEncrypt2" : "pwdEncryptSalt",
    "_" : "1622184779563",
}
url = url + urlencode(querydata)
print(url)