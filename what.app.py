from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
# open fire fox new tab , you should set the executable_path for geckodriver.exe by the local path at your machine 
# for example the local path for me C:\Users\NoteBook\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.7\geckodriver.exe
web =webdriver.Firefox(executable_path=r'C:\Users\NoteBook\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.7\geckodriver.exe')
# set the URL for the website you need to open 
web.get('https://web.whatsapp.com')
# wait till web site opened 
time.sleep(50)
# then select what you need by using find_element_by_css_selector
# you can get CSS address by right click on cell you want and copy css select address 
#here "search cell to write the name for the person or his phone number "
s=web.find_element_by_css_selector('._1awRl')
# to write any thing into the selected cell "search cell"
s.send_keys('0122450')
time.sleep(3)
# simulate enter button 
s.send_keys(Keys.ENTER)
# select message cell 
w=web.find_element_by_css_selector('._1hRBM > div:nth-child(2)')
# send your message 
w.send_keys('you are haced')
w.send_keys(Keys.ENTER)
time.sleep(3)
