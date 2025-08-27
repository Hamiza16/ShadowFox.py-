# INTERMIDIATE LEVEL - WEB SCRAPER
#Extract data from websites using libaries like Beautiful Soup or Scrapy.

import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.apple.com/in/") #Sample website for web scrapping

soup = BeautifulSoup(req.content, "html.parser")

#--------------------------------------------------SOME BASIC OPERATIONS DONE FOR WEB SCRAPPING-------------------------------------------------------------------#
#Display content of website
print(soup.prettify())

#extracting all texts information
print(soup.get_text())

#extracting titles
print(soup.title)

#extracting all the URLs found within a page’s <a> tags
for link in soup.find_all('a'):
    print(link.get('href'))
    
#extracting all headings
headings = soup.find_all(['h1', 'h2', 'h3'])

# Find all <p> tags
paragraphs = soup.find_all('p')
# Print each paragraph's text
for idx, paragraph in enumerate(paragraphs):
    print(f"Paragraph {idx + 1}: {paragraph.text}")
#-------------------------------------------------------------------------------------------------------------------------------------------------#

file_path = 'web_scrapper_extracted_data.txt'
# Save the data to a text file
with open(file_path, 'w', encoding='utf-8') as file:
    for heading in headings:
        file.write(f"{heading.name}: {heading.text.strip()}\n")
print(f"Data saved to {file_path}")
#------------------------------------------------------------------------------------------------------------------------------------------------#