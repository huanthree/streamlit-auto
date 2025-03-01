import sys
import io
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

# 修复编码问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 需要访问的URL列表
TARGET_URLS = [
    "https://stream4lit-l89x9uaknyuyndksxqvatx.streamlit.app/",
    "https://fool4stream-xr8trzmsvvm9yfbecdqtuz.streamlit.app/"
]

def process_url(url):
    """处理单个URL的访问逻辑"""
    print(f"\n正在处理URL: {url}")
    
    # 浏览器配置（每次创建新实例保证会话独立）
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    try:
        driver = webdriver.Chrome(options=options)
        driver.set_page_load_timeout(30)  # 页面加载超时设置
        
        # 访问页面
        driver.get(url)
        print("页面加载成功")

        # 查找按钮
        wait = WebDriverWait(driver, 15)
        button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(., 'Yes, get this app back up!')]")
        ))
        
        # 点击按钮
        button.click()
        print("成功点击重启按钮")
        return True

    except TimeoutException:
        print("状态正常：未找到需要点击的按钮")
        return True
    except WebDriverException as e:
        print(f"访问异常：{str(e)}")
        return False
    finally:
        if 'driver' in locals():
            driver.quit()

# 主程序
if __name__ == "__main__":
    success_count = 0
    
    for index, url in enumerate(TARGET_URLS, 1):
        print(f"\n{'='*30}")
        print(f"正在处理第 {index}/{len(TARGET_URLS)} 个应用")
        if process_url(url):
            success_count += 1
    
    print(f"\n处理完成，成功处理 {success_count}/{len(TARGET_URLS)} 个应用")
