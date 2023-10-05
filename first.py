from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
#設定 chrome drive執行路徑
options=Options()
options.chrome_executable_path=(r'C:\Users\user\Desktop\seleium\chromedriver.exe')
#建立drive來操作瀏覽器
driver=webdriver.Chrome(options=options)
#連線網址(連到104)
driver.get('https://www.104.com.tw/jobs/search/?area=6001001000,6001002000&jobsource=2018indexpoc&ro=0')
#捲動視窗顯示更多內容
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(3)
titletags=driver.find_elements(By.CLASS_NAME,"js-job-link")
for tags in titletags:
    print(tags.text)
driver.close()