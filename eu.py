import requests
from bs4 import BeautifulSoup
import os

# Function to download images from URLs
def download_image(url, directory):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(directory, os.path.basename(url)), 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {url}")
        else:
            print(f"Failed to download: {url}, Status code: {response.status_code}")
    except Exception as e:
        print(f"Exception while downloading {url}: {str(e)}")

# Function to scrape images from a webpage
def scrape_images(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            img_tags = soup.find_all('img')
            for img in img_tags:
                img_url = img.get('src')
                if img_url:
                    download_image(img_url, 'downloads')
                else:
                    print("Image URL not found in tag:", img)
        else:
            print(f"Failed to fetch page: {url}, Status code: {response.status_code}")
    except Exception as e:
        print(f"Exception while scraping {url}: {str(e)}")

# Example usage:
if __name__ == "__main__":
    url = 'https://example.com'
    scrape_images(url)
