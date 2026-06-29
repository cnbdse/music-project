from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

keyword = "周杰倫"

driver.get("https://www.youtube.com")

time.sleep(3)

search = driver.find_element(By.NAME, "search_query")
search.send_keys(keyword)
search.send_keys(Keys.ENTER)

time.sleep(5)

videos = driver.find_elements(By.ID, "video-title")

data = []

for video in videos[:20]:

    title = video.get_attribute("title")
    url = video.get_attribute("href")

    if title and url:
        data.append({
            "歌曲名稱": title,
            "影片網址": url
        })

df = pd.DataFrame(data)

df.to_csv(
    "youtube_music.csv",
    index=False,
    encoding="utf-8-sig"
)

print(df)

driver.quit()

print("完成！CSV 已儲存")