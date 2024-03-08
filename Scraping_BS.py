import requests
from bs4 import BeautifulSoup
import re

def scraped_in_txt_file(text):
      file = open("test_sites.txt", "w") 
      file.write(str(text))
      file.close()
      #see file content 
      #file = open("test_sites.txt","r")
      #print(file.read())
    

def scraping_BS():
  try:
    response = requests.get('https://webscraper.io/test-sites/e-commerce/allinone')
    if response.status_code == 200:
      content = response.text
      soup = BeautifulSoup(content, "html.parser")
      text = soup.get_text()
      # Remove excess whitespace
      text = re.sub(r'\n\s*\n', '\n\n', text)  # Replace multiple newlines with two newlines
      print(text)
      scraped_in_txt_file(text)  
  
  except NameError:
    print("ee")
if __name__ == "__main__":
    scraping_BS()
