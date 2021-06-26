import requests


header = {
   "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)",
   "Cookie": "roleid=1; ASP.NET_SessionId=r0jh1bzlh3nv1ofmllgdxknb", # 可以后续通过selemium重新得到，或者requests
}
url = "http://223.3.95.75/simtrade/Common/ShowPopUp.aspx?p1=0&p2=02&p3=E2&p4=14"
r = requests.get(url, headers= header)
print(r.text)