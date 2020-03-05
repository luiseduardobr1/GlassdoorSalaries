# GlassdoorSalaries
Extract salaries available on Glassdoor from any job and save them on a CSV file

# Requirements
* [Selenium](https://selenium-python.readthedocs.io/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Pandas](https://pandas.pydata.org/)
* [Chromedriver](https://chromedriver.chromium.org/downloads)
* [Requests](https://requests.readthedocs.io/en/master/)

# How to use
1) Put your google login and password in the code:
```Python
# Login - Google
pagina=driver.find_element_by_css_selector('#InlineLoginModule > div > div > div > div > div > div.mt-xsm.social > div > div.col-sm-6.pl-sm-xsm.mt-xsm.mt-sm-0.p-0 > button').click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
pagina2=driver.find_element_by_css_selector('#identifierId').send_keys('GMAIL EMAIL')
driver.find_element_by_css_selector('#identifierNext > span > span').click()
time.sleep(2)
driver.find_element_by_xpath(r'//*[@id="password"]/div[1]/div/div[1]/input').send_keys('GMAIL PASSWORD')
driver.find_element_by_css_selector('#passwordNext > span > span').click()
```
