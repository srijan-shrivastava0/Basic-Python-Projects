import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://realpython.com"  # You can replace this with any real URL

# Send a GET request
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# ----- Extract and print text content -----
print("📄 All Text Content:\n")
print(soup.get_text(strip=True, separator='\n'))

# ----- Extract and print all paragraph tags -----
print("\n📝 Paragraphs:\n")
for para in soup.find_all('p'):
    print(para.get_text(strip=True))

# ----- Extract and print all image URLs -----
print("\n🖼️ Image Sources:\n")
for img in soup.find_all('img'):
    src = img.get('src')
    if src:
        print(src)

# ----- Extract and print all hyperlinks -----
print("\n🔗 All Links:\n")
for link in soup.find_all('a'):
    href = link.get('href')
    if href:
        print(href)
