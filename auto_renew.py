from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():
    url = "https://stream4lit-l89x9uaknyuyndksxqvatx.streamlit.app/"
    button_text = "Yes, get this app back up!"
    
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        print("访问网页...")
        driver.get(url)
        time.sleep(5)
        
        buttons = driver.find_elements(By.XPATH, f"//button[contains(text(), '{button_text}')]")
        if buttons:
            print("按钮已找到，点击中...")
            buttons[0].click()
            print("按钮已点击。")
        else:
            print("未找到按钮，任务成功。")
    
    except Exception as e:
        print(f"发生错误: {str(e)}")
    
    finally:
        driver.quit()
        print("浏览器已关闭。")

if __name__ == "__main__":
    main()
