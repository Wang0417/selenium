from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
#設定 chrome drive執行路徑
options=Options()
options.chrome_executable_path=(r'C:\Users\user\Desktop\seleium\chromedriver.exe')
#建立drive來操作瀏覽器
driver=webdriver.Chrome(options=options)
#連線網址(連到104)    
driver.get('https://www.104.com.tw/jobs/search/?area=6001001000,6001002000&jobsource=2018indexpoc&ro=0')
login=driver.find_element(By.XPATH,'//*[@id="global_bk"]/ul/li[2]/ul/li[6]/a').click()
username=driver.find_element(By.ID ,'username')
password=driver.find_element(By.ID ,'password')
username.send_keys('zxc5352@gmail.com')
password.send_keys('************')
btn=driver.find_element(By.ID ,'submitBtn')
btn.send_keys(Keys.ENTER)
time.sleep(5)

#捲動視窗顯示更多內容
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
titletags=driver.find_elements(By.CLASS_NAME,"js-job-link")
for tags in titletags:
    if 'python' in tags:
        print(tags.text)
driver.close()