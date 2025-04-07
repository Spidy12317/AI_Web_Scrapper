import fastapi
from fastapi import Form
import os
import gc
import asyncio
import logging
import nest_asyncio
from dotenv import load_dotenv
from playwright.async_api import async_playwright
import asyncio
import tempfile
from PIL import Image
import io 


nest_asyncio.apply()
load_dotenv()

app = fastapi.FastAPI()


@app.get("/")
async def root():
    return {"message": "This is a test endpoint"}

@app.get("/test")
async def test(num_of_test: int = Form(default=1), num_of_concurrent: int = Form(default=1), url: str = Form(default="https://www.example.com")):
    print(num_of_test, num_of_concurrent)
    print("Starting Test")

    try:
                
        async def get_screenshot(semaphore=None):
            if semaphore:
                async with semaphore:
                    return await get_screenshot()

            with tempfile.TemporaryDirectory() as temp_dir: 
                async with async_playwright() as p:
                    browser = await p.chromium.launch(headless=True)
                    page = await browser.new_page()
                    await page.goto(url)
                    img_bytes = await page.screenshot(timeout=0,full_page=True)    
                    await browser.close()
                    del img_bytes,browser,page
            return


        task = []
        semaphore = asyncio.Semaphore(num_of_concurrent)
        
        for _ in range(num_of_test):
            task.append(asyncio.shield(get_screenshot(semaphore)))  # Shield to prevent coroutine leaks

        await asyncio.gather(*task)

        gc.collect()  


        logging.info("Test Successful")
        return {"message": "Test Successful"}

    except Exception as e:
        logging.error(f"An error occurred during the test: {e}", exc_info=True)
        return {"Error": f"An error occurred: {str(e)}"}

