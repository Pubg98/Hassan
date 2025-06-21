import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

TARGET_GROUP_NAME = "اخبار يوم العاشر الحديث"

def load_last_message():
    try:
        with open("last_message.txt", "r", encoding="utf-8") as f:
            return f.read().strip()
    except:
        return None

def send_to_whatsapp():
    msg = load_last_message()
    if not msg:
        print("⚠️ لا توجد رسالة لإرسالها.")
        return

    options = uc.ChromeOptions()
    options.add_argument("--no-first-run --no-service-autorun --password-store=basic")

    driver = uc.Chrome(options=options)
    driver.get("https://web.whatsapp.com/")

    print("📷 امسح كود QR لتسجيل الدخول في واتساب...")

    input("✅ بعد تسجيل الدخول، اضغط Enter هنا في Replit...")

    time.sleep(3)
    search_box = driver.find_element(By.XPATH, '//div[@title="Search input textbox"]')
    search_box.click()
    time.sleep(1)
    search_box.send_keys(TARGET_GROUP_NAME)
    time.sleep(3)

    group = driver.find_element(By.XPATH, f'//span[@title="{TARGET_GROUP_NAME}"]')
    group.click()
    time.sleep(2)

    input_box = driver.find_element(By.XPATH, '//div[@title="Type a message"]')
    input_box.send_keys(msg)
    input_box.send_keys("\n")

    print("✅ تم إرسال الرسالة إلى واتساب.")
    time.sleep(5)
    driver.quit()