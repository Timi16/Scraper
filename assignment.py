
import requests
from bs4 import BeautifulSoup

def scrape_names(url):
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return []

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
    else:
        print("No 'Coming into Force' section found.")
    
    return names

# Example usage
url = "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2001-360/FullText.html"
names_list = scrape_names(url)

if names_list:
    print("Names found:", names_list)
else:
    print("No names found.")
