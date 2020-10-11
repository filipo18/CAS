from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

titles=[] 
submitters=[] 
audiences=[] 
texts=[]

driver.get("https://matrix.uwcisak.jp/bearly")
driver.implicitly_wait(6)
driver.find_element_by_xpath("""//*[@id="email"]""").send_keys("2021.alexander.nygaard@uwcisak.jp")
driver.find_element_by_xpath("""//*[@id="password"]""").send_keys("1ZTY8gIWxHsk")
driver.find_element_by_xpath("""//*[@id="submit"]""").click()

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

driver.implicitly_wait(6)

for a in soup.findAll('div', attrs={'class':'bearly-container'}):


    title = a.find("div", attrs={'class': 'bearly-title'})
    submitter_audience_text = title.find_next_sibling()

    text = a.find("div", attrs={"class": "bearly-body"})

    title = title.getText().strip()
    submitter_audience_text = submitter_audience_text.getText()
    text = text.getText().strip()

    submitter, audience = [part.strip() for part in submitter_audience_text[0:-1*len(text)-3].split("|")]

    # Append to lists
    titles.append(title)
    submitters.append(submitter)
    audiences.append(audience)
    texts.append(text)

df = pd.DataFrame({'Titles':titles,'Submitters':submitters,"Audiences":audiences,"Texts":texts})
df.to_csv('inputs.csv', index=False, encoding='utf-8')


driver.close()
