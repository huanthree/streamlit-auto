from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# 配置浏览器选项
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 无头模式（可选）
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# 初始化WebDriver（注意：需要下载对应版本的ChromeDriver）
driver = webdriver.Chrome(options=options)

try:
    # 访问目标网页
    driver.get("https://stream4lit-l89x9uaknyuyndksxqvatx.streamlit.app/")

    # 设置显式等待（最多等待10秒）
    wait = WebDriverWait(driver, 10)
    
    # 尝试查找按钮
    button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(., 'Yes, get this app back up!')]")
    ))
    
    # 如果找到按钮则点击
    button.click()
    print("成功点击重启按钮")

except TimeoutException:
    # 如果未找到按钮
    print("成功：未找到需要点击的按钮")

finally:
    # 关闭浏览器
    driver.quit()
