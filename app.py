from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

navegador.get("https://login.infojobs.com.br/Account/Login?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3DInfoJobs.Web%26redirect_uri%3Dhttps%253A%252F%252Fwww.infojobs.com.br%252Fsignin-oidc%26response_type%3Dcode%2520id_token%26scope%3Dopenid%2520profile%2520email%26state%3DOpenIdConnect.AuthenticationProperties%253DijBefzdFHTLoWc1qZT4bkISyJqLwivIrFAyEAnNwOsCHTKIMi8DOB9TqEIgekQXYV8kqSkikOR8PFQa-p3ryprZ7MAp4AHxHIL8Gq0E-etPv2A8rmqfHjyAoxzgsOk1Tsw5k3ExejqSN9wfz9yrHTwooGVtp_3-7_7VzvuWm02d1iaMOWz6Gs6SqG35g-2-lTjgn-A%26response_mode%3Dform_post%26nonce%3D638315910488074405.ODEyNmQ1OGQtZDRkMi00MjBkLWI2MmQtZTM3NGM1NTdmYjkwNzg1MTQ0MTgtNTcxNC00MTAxLThlZWYtNDhlNmZmNjZjNDkz%26x-client-SKU%3DID_NET472%26x-client-ver%3D6.31.0.0")
sleep(5)

#login
email = "luscals2003@gmail.com"
senha = "159963Ls"
cargo = "operador"

#preenchendo login
navegador.find_element('xpath', '//*[@id="didomi-notice-agree-button"]').click()
navegador.find_element('xpath', '//*[@id="Username"]').send_keys(email)
navegador.find_element('xpath', '//*[@id="Password"]').send_keys(senha)
navegador.find_element('xpath', '//*[@id="loginForm"]/button').click()

#fazendo a pesquisa
navegador.find_element('xpath', '/html/body/nav/div/div/ul/li[1]/a').click()
navegador.find_element('xpath', '//*[@id="keywordsCombo"]').send_keys(cargo)
navegador.find_element('xpath', '/html/body/main/div[1]/section/div[1]/div[4]/a').click()

#filtrando pesquisa
navegador.find_element('xpath', '//*[@id="facetRenovationDateRange"]/div[1]/a').click()
navegador.find_element('xpath', '//*[@id="facetRenovationDateRange"]/div[2]/div/a[1]').click()
navegador.find_element('xpath', '//*[@id="sortOptions"]/a[1]').click()

#pegando links da pag
td_vagas = navegador.find_element(By.ID, 'filterSideBar')
vagas = td_vagas.find_elements(By.TAG_NAME, "a")
links = []

#filtrando os links que sao msm vagas
for vaga in vagas:
    link = vaga.get_attribute('href')
    
    if link.endswith(".aspx"):
        links.append(link)

#candidatura
for link in links:
    navegador.get(link)
    navegador.find_element('xpath', '//*[@id="VacancyHeader"]/div[3]/div[1]/a').click()
    sleep(10)
