from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create WebDriverWait object (max wait 10 seconds)



driver = webdriver.Firefox()


# driver.get('https://www.udemy.com/?utm_source=adwords-brand&utm_medium=udemyads&utm_campaign=Brand-Udemy_la.EN_cc.India_dev.&campaigntype=Search&portfolio=BrandDirect&language=EN&product=Course&test=&audience=Keyword&topic=&priority=&utm_content=deal4584&utm_term=_._ag_133043842301_._ad_595460368494_._kw_udemy_._de_c_._dm__._pl__._ti_kwd-296956216253_._li_9062008_._pd__._&matchtype=b&gad_source=1&gad_campaignid=17099057432&gclid=EAIaIQobChMI0_n2gJ2UjwMV3KlmAh0dWxyNEAAYASAAEgKcEfD_BwE')
# driver.find_element(By.CLASS_NAME ,'ud-btn-label').click()


driver.get('https://testautomationpractice.blogspot.com/')
wait = WebDriverWait(driver, 10)

element = wait.until(
    EC.visibility_of_element_located((By.ID, "name"))
)
driver.find_element(By.ID,'name').send_keys('Tester')
driver.find_element(By.CSS_SELECTOR,'#email').send_keys('Tester@gmail.com')
driver.find_element(By.CSS_SELECTOR,'input[placeholder="Enter Phone"]').send_keys('12345678')
ad = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//textarea[@id = 'textarea']"))
)
ad.send_keys('''
text123
    hn
             pin= 300''')

ad1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#male")))
ad1.click()
target_days = ["Sunday", "Tuesday"]

# Get all labels
day_labels = driver.find_elements(By.CSS_SELECTOR, "label.form-check-label")

for label in day_labels:
    print(label)
    print('-----------------')
    day_text = label.text.strip()
    print(day_text)
    print('-----------------')
    if day_text in target_days:
        label.click()  # clicking label will toggle the checkbox linked with 'for'
        print(f"Selected: {day_text}")
