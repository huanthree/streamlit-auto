from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import shutil
import time

def main():
    url = "https://stream4lit-l89x9uaknyuyndksxqvatx.streamlit.app/"
    button_text = "Yes, get this app back up!"
    
    options = Options()
    options.add_argument("--headless")  # 无头模式，后台运行
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # 检查 chromedriver 是否安装
    chromedriver_path = shutil.which("chromedriver")
    if not chromedriver_path:
        print("chromedriver 未安装或未在 PATH 中")
    else:
        print(f"chromedriver 路径: {chromedriver_path}")
    
    # 启动浏览器
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        
        print("访问网页...")
        driver.get(url)
        time.sleep(5)  # 等待页面加载
        
        try:
            button = driver.find_element(By.XPATH, f"//button[contains(text(), '{button_text}')]")
            print("按钮已找到，点击中...")
            button.click()
            print("按钮已点击。")
        except Exception:
            print("未找到按钮，任务成功。")
    
    except Exception as e:
        print(f"发生错误: {str(e)}")
    
    finally:
        driver.quit()
        print("浏览器已关闭。")

if __name__ == "__main__":
    main()
