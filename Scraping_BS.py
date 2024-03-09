import requests
from bs4 import BeautifulSoup
import pandas as pd

def scraped_in_txt_file(df):
  with open('scraped_data.txt', 'w') as file:
    for index, row in df.iterrows():
      file.write("Price: {}\n".format(row['Price']))
      file.write("Name: {}\n".format(row['Name']))
      file.write("Description: {}\n".format(row['Description']))
      file.write("Number of Reviews: {}\n\n".format(row['Number of Reviews']))
    

def scraping_BS():
  try:
    response = requests.get('https://webscraper.io/test-sites/e-commerce/allinone')
    if response.status_code == 200:
      content = response.text
      soup = BeautifulSoup(content, "html.parser")
      items = soup.find_all('div', class_=['caption','ratings'])
      text = '\n'.join(item.get_text() for item in items)
      lines = text.split('\n')
      filtered_lines = [item for item in lines if item != '']
      
      data = []

      for i in range(0,len(filtered_lines),4):
        item_data = {
                'Price': filtered_lines[i],
                'Name': filtered_lines[i+1],
                'Description': filtered_lines[i+2],
                'Number of Reviews': filtered_lines[i+3]
            }
        data.append(item_data)
      df = pd.DataFrame(data)
      return df

  except NameError:
    print("ee")
if __name__ == "__main__":
    df = scraping_BS()
    print(df)
    scraped_in_txt_file(df)
