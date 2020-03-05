# Glassdoor - Salaries
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
...
pagina2=driver.find_element_by_css_selector('#identifierId').send_keys('GMAIL EMAIL')
driver.find_element_by_css_selector('#identifierNext > span > span').click()
time.sleep(2)
driver.find_element_by_xpath(r'//*[@id="password"]/div[1]/div/div[1]/input').send_keys('GMAIL PASSWORD')
...
```

2) Change the **job** (*tipo_de_vaga* variable) and **city** (*onde_vaga* variable):
```Python
# Glassdoor access - salaries
driver.implicitly_wait(10) # seconds
tipo_de_vaga = 'analista'
onde_vaga='Fortaleza, Ceará (Brasil)'
...
```

3) It will be created a CSV file, named *salariosGlassdoor.csv*, with four columns: job type, company name, salary, average salary. 

# Screenshot

![image](https://user-images.githubusercontent.com/56649205/75986264-87a07280-5ecc-11ea-8748-c6a8a0ed7c72.png)
