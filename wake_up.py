import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        # Launch a headless browser
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        print("Visiting the app...")
        await page.goto("https://voudmovieup.streamlit.app/")
        
        # Wait for 10 seconds to let the JS load
        await page.wait_for_timeout(10000)
        
        # Check if the "Wake Up" button exists and click it
        wake_button = page.get_by_role("button", name="Yes, get this app back up!")
        if await wake_button.is_visible():
            print("App was sleeping. Clicking wake button...")
            await wake_button.click()
            await page.wait_for_timeout(5000)
        else:
            print("App was already awake!")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
  
