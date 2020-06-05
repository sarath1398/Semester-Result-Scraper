from selenium import webdriver
from bs4 import BeautifulSoup
from requests import get
#from PIL import Image
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import TimeoutException
options=webdriver.ChromeOptions()
options.binary_location=r'C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe'
options.headless(True)
path=r'C:\Program Files\Python38\Scripts\chromedriver.exe'
driver=webdriver.Chrome(executable_path=path,options=options)
#driver.minimize_window()
url='http://karpagam.edu.in/'
driver.get(url)
response=get(url)
#print(response.text)
soup=BeautifulSoup(response.text,'html.parser')
#print(soup.prettify())
#print(list(soup.descendants))
link=soup.find_all('a',text='Karpagam College of Engineering')
link=link[0]['href']
link1=url+link
driver.get(link1)
response=get(link1)
#print(response.text)
name=driver.find_element_by_id('studentrollno')
name.send_keys('{}'.format(input('Enter Rollno: ')))
password=driver.find_element_by_id('studentpassword')
password.send_keys('{}'.format(input('Enter Password: ')))
button=driver.find_elements_by_xpath("//input[@type='submit' and @value='Login']")[0]
button.click()
#print(soup.find_all('input',id='studentrollno'))
#soup.find_all('input',id='')
response=get(driver.current_url)
soup=BeautifulSoup(response.text,'html.parser')
semester=input()
link=soup.find_all('a',text='Semester {}'.format(semester))[1]['href']
link2=url+'Automation/'+link
driver.get(link2)
driver.maximize_window()
#driver.get(link2)
#print(driver.current_url)
month,year=input(),input()
month=month[:3].capitalize()
option=driver.find_element_by_xpath("//select/option[@value='{} {}']".format(month,year))
option.click()
try:
    btn=driver.find_element_by_xpath("//input[@type='button' and @value='Load Semester Marksheet']")
    btn.click()
    driver.execute_script('window.scrollTo(0,{})'.format(int(0.4*1080)))
    driver.get_screenshot_as_file('result.png')
except Exception:
    driver.refresh()

'''
while True:
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME,"div")))
        break
    except TimeoutException:
        print("Loading took too much time!")
        driver.refresh()
'''
