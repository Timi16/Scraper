import requests
from bs4 import BeautifulSoup

def scrape_names():
    url = "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2001-360/FullText.html"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    
    names = []
    section = soup.find('h2', string="Coming into Force")
    
    if section:
        next_element = section.find_next('ul')
        if next_element:
            list_items = next_element.find_all('li')
            for li in list_items:
                name = li.get_text(strip=True)
                if name:
                    names.append(name)
    
    if names:
        with open("names.txt", "w", encoding="utf-8") as file:
            for name in names:
                file.write(name + "\n")
        print("Names have been successfully written into names.txt'.")
    else:
        print("No names found .")

scrape_names()
