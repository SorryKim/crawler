from selenium import webdriver

browser = webdriver.Chrome() #"./chromedriver.exe"

# 네이버 이동
browser.get("http://www.naver.com")

# 로그인 버튼 클릭
elem = browser.find_element(by="class_name", value="link_login")
elem.click()

# id입력 pw입력
browser.find_element(by="id", value="id").send_keys("123")
browser.find_element(by="id", value="pw").send_keys("123")

# 로그인버튼 클릭
browser.find_element(by="id", value="log.login").click()


