import requests
from bs4 import BeautifulSoup

def fetch_display_text(wkp_page):
    try:
        response = requests.get(f"https://en.wikipedia.org/wiki/{wkp_page}")
        
        if response.status_code == 200:
            content = response.text
            soup = BeautifulSoup(content, "html.parser")
            text = soup.get_text()
            print(text)
 
        else:
            print(f"There is no information on {wkp_page}.")
    except ValueError:
        print("Error")

if __name__ == "__main__":
    wkp_page = input("Enter name that will display text from Wikipedia pages: ")
    fetch_display_text(wkp_page)