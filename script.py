from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}
options.add_experimental_option('prefs', prefs) 
options.add_argument("disable-infobars") 
driver = webdriver.Chrome(options=options)
driver.maximize_window() 

driver.get("https://m.momoshop.com.tw/mymomo/login.momo") # Login Page

driver.find_element(By.ID, 'memId').send_keys('YOUR ACCOUNT NAME')
driver.find_element(By.ID, 'passwd').send_keys('YOUR PASSWORD')
driver.find_element(By.CLASS_NAME, 'login').click()

# Stop after login. Press Enter to continue.
input("Press Enter to continue...")

# GRIIIx
driver.get("https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=10669315&str_category_code=1911700049&sourcePageType=4&openid=1")	
# Test Product
# driver.get("https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=7419911&cid=recitri&oid=BfM&ctype=B&recomd_id=rgc-rl2t_normal_1718559946_364247367")

while 1:
	try:
		insure = WebDriverWait(driver, 0.5, 0.2).until(EC.presence_of_element_located((By.ID, 'insureChkBox2'))) # Insure Checkbox
		insure.click()
		buy = WebDriverWait(driver, 1, 0.5).until(EC.presence_of_element_located((By.ID, 'buy_yes'))) # Purchase Button
		buy.click() # Click when it's available
		print ('Can Buy now!')
		driver.find_element(By.CLASS_NAME, 'checkoutButton').click() # Click on Checkout button
		
		if input("Input QUIT to exit...") == "QUIT": # Input QUIT to exit
			break
	
	except:
		print("Can't buy yet! Reloading!")
		driver.refresh() # Reload
