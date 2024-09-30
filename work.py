import requests
from bs4 import BeautifulSoup

def scrape_warning_notice(url):
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return []
    
    soup = BeautifulSoup(response.content, 'html.parser')
    warning_sections = soup.find_all('article')
    companies = []

    for section in warning_sections:
        headings = section.find_all('h3')
        for heading in headings:
            company = heading.get_text(strip=True)
            companies.append(company)
    
    return companies

# Example usage
url = "https://www.belizefsc.org.bz/warning-notice/"
company_list = scrape_warning_notice(url)

if company_list:
    print("Companies with warning notices:", company_list)
else:
    print("No companies found.")
