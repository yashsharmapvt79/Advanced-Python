import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from playwright.sync_api import sync_playwright
import asyncio
from pyppeteer import launch

# URL to scrape
url = 'https://chatgpt.com'

# Check if the page can be scraped with static requests
def scrape_static(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        print("Static content:")
        for heading in soup.find_all('h1'):
            print(heading.get_text())
    except Exception as e:
        print(f"Static scraping failed: {e}")

# Check if the page requires JavaScript rendering with Selenium
def scrape_selenium(url):
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(url)
        
        print("Selenium content:")
        elements = driver.find_elements_by_tag_name('h1')
        for element in elements:
            print(element.text)
        
        driver.quit()
    except Exception as e:
        print(f"Selenium scraping failed: {e}")

# Check if the page requires JavaScript rendering with Playwright
def scrape_playwright(url):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url)
            
            print("Playwright content:")
            h1_elements = page.locator('h1').all_text_contents()
            for text in h1_elements:
                print(text)
            
            browser.close()
    except Exception as e:
        print(f"Playwright scraping failed: {e}")

# Check if the page requires JavaScript rendering with Pyppeteer
async def scrape_pyppeteer(url):
    try:
        browser = await launch(headless=True)
        page = await browser.newPage()
        await page.goto(url)
        
        print("Pyppeteer content:")
        h1_elements = await page.querySelectorAllEval('h1', 'elements => elements.map(e => e.textContent)')
        for text in h1_elements:
            print(text)
        
        await browser.close()
    except Exception as e:
        print(f"Pyppeteer scraping failed: {e}")

# Main function to determine the scraping method
def main(url):
    print("Attempting static scraping...")
    scrape_static(url)
    
    # Fallback to Selenium if static scraping fails
    print("\nAttempting Selenium scraping...")
    scrape_selenium(url)
    
    # Fallback to Playwright if Selenium fails
    print("\nAttempting Playwright scraping...")
    scrape_playwright(url)
    
    # Fallback to Pyppeteer if Playwright fails
    print("\nAttempting Pyppeteer scraping...")
    asyncio.run(scrape_pyppeteer(url))

# Run the main function
if __name__ == "__main__":
    main(url)
