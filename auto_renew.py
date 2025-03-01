from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    url = "https://stream4lit-l89x9uaknyuyndksxqvatx.streamlit.app/"
    button_text = "Yes, get this app back up!"
    
    options = Options()
    options.add_argument("--headless=new")  # 更好的无头模式
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    logging.info("启动浏览器...")
    driver = None  # 初始化driver为None
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        
        logging.info(f"访问 {url} ...")
        driver.get(url)

        # 等待按钮出现
        try:
            button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//button[contains(text(), '{button_text}')]"))
            )
            logging.info("按钮已找到，点击中...")
            button.click()
            logging.info("按钮已点击。")
        except NoSuchElementException:
            logging.info("未找到按钮，可能已经在线。")

    except Exception as e:
        logging.error(f"发生错误: {str(e)}")

    finally:
        if driver:  # 只有在driver初始化后才调用quit
            driver.quit()
        logging.info("浏览器已关闭。")

if __name__ == "__main__":
    main()
