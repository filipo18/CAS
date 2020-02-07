from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

titles=[] 
submitters=[] 
audiences=[] 
texts=[]

driver.get("https://matrix.uwcisak.jp/posts")
driver.implicitly_wait(6)
driver.find_element_by_xpath("""//*[@id="email"]""").send_keys("2021.alexander.nygaard@uwcisak.jp")
driver.find_element_by_xpath("""//*[@id="password"]""").send_keys("PASSWORD")
driver.find_element_by_xpath("""/html/body/div/div/div/div/div/form/div[4]/div/button""").click()

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

for a in soup.findAll('div', attrs={'class':'card'}):
    title = a.find("h5", attrs={'class':'card-title'})
    submitter = a.find('span', attrs={'class':'font-italic'})
    audience = a.find("span", attrs={"class":"font-weight-bold"})
    text = a.find("p", attrs={"class": "card-text"})

    titles.append(title.getText())
    submitters.append(submitter.getText())
    audiences.append(audience.getText())
    texts.append(text.getText())


print("Titles:\n", titles)
print("Submitters:\n", submitters)
print("Audiences:\n", audiences)
print("Texts:\n", texts)

df = pd.DataFrame({'Titles':titles,'Submitters':submitters,"Audiences":audiences,"Texts":texts})
df.to_csv('inputs.csv', index=False, encoding='utf-8')


