import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

mb = input("[+] Enter mobile name: ").split()

def MobileInfo():
    
    fulNm = "-".join(mb)

    # Page url
    url = f'https://www.91mobiles.com/{fulNm}-price-in-india'

    # get url in python
    page = requests.get(url)

    # Getting the webpage's content in pure html
    soup = bs(page.content,'html.parser')

    # Getting all the div contaner which has spec_box class where table is present
    table_contanir = soup.find_all(class_ = 'spec_box')

    # Getting extrack result as a table
    tble_key = []
    tble_value = []


    def extracr_tcontant():

        for tcontant in table_contanir:
            rows = tcontant.find_all('tr')

            for row in rows:
                try:
                    table_key1 = row.find('td', class_ = 'spec_ttle').get_text(strip=True)
                    table_value = row.find('td', class_ = 'spec_des').get_text(strip=True)
                    tble_key.append(table_key1) 
                    tble_value.append(table_value)
                    print(f"{table_key1}{' -->> '}{table_value}")

                except AttributeError:
                    continue

        return 1

    extracr_tcontant()

    dic = {
        "key" : tble_key,
        "value" : tble_value

    }
    df = pd.DataFrame(dic)

    if len(df)==0:
        print(f"You entrer a unvalid phone:")
    else:
        df.to_excel(f"{fulNm}.xlsx")

MobileInfo()

