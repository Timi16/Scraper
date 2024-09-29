import requests
from bs4 import BeautifulSoup

def scrape_warning_notice():
    url = "https://www.belizefsc.org.bz/warning-notice/"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.content, 'html.parser')
    warning_sections = soup.find_all('article')
    companies = []

    for section in warning_sections:
        headings = section.find_all('h3')
        for heading in headings:
            company = heading.get_text(strip=True)
            companies.append(company)
    
    if companies:
        with open("warning_notices.txt", "w", encoding="utf-8") as file:
            file.write("Companies with warning notices:\n\n")
            for idx, company in enumerate(companies, 1):
                file.write(f"{idx}. {company}\n")
        print("Scraped data has been successfully written to warning_notices.txt'")
    else:
        print("No companies found under warning notices.")

scrape_warning_notice()
