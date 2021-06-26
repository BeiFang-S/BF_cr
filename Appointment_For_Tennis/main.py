import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--window-size=1366,768') #设置浏览器分辨率

driver = webdriver.Chrome(options = options)

username = "213183668"
password = "1999swn.."
driver.get("https://newids.seu.edu.cn/authserver/login?goto=http://my.seu.edu.cn/index.portal")
driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div[4]/div/form/p[1]/input").send_keys(username)
time.sleep(1.6)
driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div[4]/div/form/p[2]/input[1]").send_keys(password)


driver.quit()


url = "http://yuyue.seu.edu.cn/eduplus/order/initOrderIndex.do?sclId=1&t_s=1622179265340&amp_sec_version_=1&gid_=NGJzMDFHVVJlOTZRTFBpU1VveXBDQStHQUoxckJjbVIzci9GTWlLOG9zWFJENW1JSnJPQUVDMFZuR0xiRFczKy95ZTBMNDlKQTJ5ZzV3aEVQT1RwREE9PQ&EMAP_LANG=zh&THEME=indigo"
header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Cookie" : "JSESSIONID=C1BBACA65EB1B7D897938C2C2E749817; gr_user_id=517330ad-3f57-4a43-8e5d-e1b39c5f66bc; zg_8da79c30992d48dfaf63d538e31b0b27=%7B%22sid%22%3A%201617497975963%2C%22updated%22%3A%201617497975963%2C%22info%22%3A%201617497975968%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22firstScreen%22%3A%201617497975963%7D; zg_did=%7B%22did%22%3A%20%221758868fc0324d-0d6ee77e6a92a8-333376b-144000-1758868fc047c3%22%7D; zg_=%7B%22sid%22%3A%201617497989386%2C%22updated%22%3A%201617497989393%2C%22info%22%3A%201617413474483%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22ehall.seu.edu.cn%22%2C%22cuid%22%3A%20%22213183668%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22firstScreen%22%3A%201617497989386%7D; JSESSIONID=8E5B782EED39CF51AA8166436467BB13; amlbcookie=01; iPlanetDirectoryPro=AQIC5wM2LY4SfcyJSabmlkJj%2BTMxH1CGMqFcQi3hOLHorcA%3D%40AAJTSQACMDE%3D%23",
}
r = requests.get(url = url, headers = header)

