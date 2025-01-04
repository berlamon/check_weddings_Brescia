import requests
from bs4 import BeautifulSoup

def check_website():
    url = "https://example.com"  # <-- Change this to your target URL
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Example: Find the first <h1> element on the page
        target_element = soup.select_one("h1")
        
        if target_element:
            target_text = target_element.get_text().strip()
            print(f"[INFO] The <h1> says: {target_text}")
        else:
            print("[ERROR] Could not find any <h1> element on the page.")
    else:
        print(f"[ERROR] Failed to load the page. Status code: {response.status_code}")

if __name__ == "__main__":
    check_website()
