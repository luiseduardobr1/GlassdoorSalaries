import os, re, requests, time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.keys import Keys

# Get number of pages
numero_paginas=int(input('How many pages? '))

# Initialize browser
chromedriver = "./chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

tic = time.time()

# Open Glassdoor website
thing_url = "https://www.glassdoor.com.br/index.htm"
driver.get(thing_url)

# Login - Google
pagina=driver.find_element_by_css_selector('#InlineLoginModule > div > div > div > div > div > div.mt-xsm.social > div > div.col-sm-6.pl-sm-xsm.mt-xsm.mt-sm-0.p-0 > button').click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
pagina2=driver.find_element_by_css_selector('#identifierId').send_keys('GMAIL EMAIL')
driver.find_element_by_css_selector('#identifierNext > span > span').click()
time.sleep(2)
driver.find_element_by_xpath(r'//*[@id="password"]/div[1]/div/div[1]/input').send_keys('GMAIL PASSWORD')
driver.find_element_by_css_selector('#passwordNext > span > span').click()

# Glassdoor access - salaries
driver.implicitly_wait(10) # seconds
tipo_de_vaga = 'analista'
onde_vaga='Fortaleza, Ceará (Brasil)'
driver.switch_to.window(driver.window_handles[0])
pagina3=driver.find_element_by_css_selector('#sc\.keyword').send_keys(tipo_de_vaga)
driver.find_element_by_css_selector('#SiteSrchTop > form > div > ul > li.jobs.active-context').click()
driver.find_element_by_css_selector('#SiteSrchTop > form > div > ul > li.salaries > span').click()
driver.find_element_by_css_selector('#sc\.location').clear()
driver.find_element_by_css_selector('#sc\.location').send_keys(onde_vaga)
pagina4 = driver.find_element_by_css_selector('#sc\.keyword')
pagina4.send_keys(Keys.ENTER)


# Start Web-Scraping
cargo=[]
empresa=[]
salario=[]
medias=[]

for contador in range(0,numero_paginas):
    time.sleep(3)
    html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    soup = BeautifulSoup(html, "html.parser")

    #soup = BeautifulSoup(open(r'C:\Users\luisedu\Desktop\glass.html', encoding='utf-8'), "html.parser")
    for line in soup.findAll('div', attrs={'class': 'row align-items-center m-0 salaryRow__SalaryRowStyle__row'}):
        # Cargo
        cargo.append(line.find(class_='salaryRow__JobInfoStyle__jobTitle strong').text.strip())
        print(line.find(class_='salaryRow__JobInfoStyle__jobTitle strong').text)
        # Empresa
        empresa.append(line.find(class_='salaryRow__JobInfoStyle__employerName').text.strip())
        print(line.find(class_='salaryRow__JobInfoStyle__employerName').text)
        # Salário
        ssalario=str(line.find(class_='col-2 d-none d-md-block px-0 py salaryRow__SalaryRowStyle__amt').text)
        ssalario=ssalario.replace('/mês','')
        ssalario=ssalario.replace('por hora','')
        ssalario=ssalario.replace(',','')
        ssalario=ssalario.replace('Cerca de','')
        ssalario=ssalario.replace(' mil','000')
        print(ssalario)
        salario.append(ssalario)
        if ssalario.find('-')>0:
            try:
                menor=int(re.findall('R\$\s*(\w*) - R\$\s*\w*', ssalario)[0])
                maior=int(re.findall('R\$\s*\w* - R\$\s*(\w*)', ssalario)[0])
                print('Media ' + str((maior+menor)/2))
                medias.append(str((maior+menor)/2))
            except:
                medias.append('-')
        else:
            medias.append('-')
        
    driver.find_element_by_css_selector('#SalariesByCompany > div.module > div.salariesByCompanyModule__SalariesByCompanyStyle__pagination > ul > li.pagination__PaginationStyle__next > a').click()
    
for i in range(0,len(empresa)):
    combinacao_nacional=[cargo[i],empresa[i],salario[i],medias[i]]
    df=pd.DataFrame(combinacao_nacional)
    with open('salariosGlassdoor.csv', 'a', encoding='utf-16', newline='') as f:
        df.transpose().to_csv(f, encoding='utf-16', header=False, sep = "\t", index=False)