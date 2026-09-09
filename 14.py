import time
import os
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define your target website configuration
URL = "https://example.com"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
EXCEL_FILE = "automated_web_data.xlsx"

def scrape_and_export():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Starting scrape job...")
    
    try:
        # 1. Fetch website HTML
        response = requests.get(URL, headers=HEADERS, timeout=10)
        response.raise_for_status()
        
        # 2. Parse HTML content (Adjust tags/classes based on your target site)
        soup = BeautifulSoup(response.text, "html.parser")
        scraped_data = []
        
        # Example: Scraping rows from a specific data container
        for item in soup.find_all("div", class_="data-row"):
            scraped_data.append({
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Title": item.find("h3", class_="title").text.strip() if item.find("h3") else "N/A",
                "Value": item.find("span", class_="value").text.strip() if item.find("span") else "N/A"
            })
            
        if not scraped_data:
            print("⚠️ No data items found matching the selectors.")
            return

        # 3. Convert to DataFrame
        new_df = pd.DataFrame(scraped_data)
        
        # 4. Append to Excel instead of overwriting historical data
        if os.path.exists(EXCEL_FILE):
            existing_df = pd.read_excel(EXCEL_FILE)
            final_df = pd.concat([existing_df, new_df], ignore_index=True)
        else:
            final_df = new_df
            
        final_df.to_excel(EXCEL_FILE, index=False)
        print(f"✅ Successfully saved {len(new_df)} rows to {EXCEL_FILE}!")

    except Exception as e:
        print(f"❌ Error occurred during execution: {e}")

# --- AUTOMATION LOOP ---
# Run the job immediately, then repeat at an interval (e.g., every 24 hours)
INTERVAL_SECONDS = 24 * 60 * 60  # Adjust as needed (e.g., 3600 for every hour)

if __name__ == "__main__":
    print("🚀 Automation engine initialized. Press Ctrl+C to stop.")
    while True:
        scrape_and_export()
        print(f"😴 Sleeping for {INTERVAL_SECONDS / 3600:.1f} hours...")
        time.sleep(INTERVAL_SECONDS)