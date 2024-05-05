from selenium import webdriver
from _logger import logger
browser = webdriver.Edge(r"C:\Users\th056\Documents\Google-Image-Scraper\webdriver\msedgedriver.exe")

browser.set_window_size(1400, 1050)
search_key = "Lamborghini Car photography"
url=f"""
https://www.
google.com/search?q={search_key}+images&newwindow=1&sca_esv=2c6693827cfe3781&sca_upv=1&udm=2&biw=1498&bih=872&tbs=sur%3acl&sxsrf=adlywijfafqzxnn9mcg6kb4cjq83bzdxvq%3a1714946890255&ei=sgm4zr-td8q6i-gpxoouka8&ved=0ahukewi_4m6bw_efaxvk3qihhcsxc_iq4dudcba&uact=5&oq=car+images&gs_lp=egxnd3mtd2l6lxnlcnaicmnhcibpbwfnzxmydraagiaegledgemyiguychaagiaegemyiguychaagiaegemyiguychaagiaegemyiguychaagiaegemyiguychaagiaegemyiguychaagiaegemyiguychaagiaegemyiguybraagiaemguqabiabejdcvaawjaicab4ajabajgbsakgabcqqgefmi04ljg4aqpiaqd4aqgyagmgaskqwgieecmyj8icebaagiaegledgemygweyigwyawcsbwuyltgumaahtdm&sclient=gws-wiz-serp
"""
# url = "https://www.google.com/search?q=%s&source=lnms&tbm=isch&sa=X&ved=2ahUKEwie44_AnqLpAhUhBWMBHUFGD90Q_AUoAXoECBUQAw&biw=1920&bih=947" % (
#             search_key)
browser.get(url)
from bs4 import BeautifulSoup

# Get the HTML content of the webpage
html = browser.page_source

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all <img> elements
img_elements = soup.find_all('img')

logger.info(f"Found {len(img_elements)} images for search key: {search_key}")
# get the src value
_base64 = []
for idx, k in enumerate(img_elements):
    if k.has_attr('src'):
        logger.info(f"iterating {idx} ")
        # _base64.append(k['src'])

        if k['src'].startswith('data:image'):
            browser.get(k['src'])
            _base64.append(browser.get_screenshot_as_base64())



with open(f"images.txt", "w") as f:
    for item in _base64:
        f.write("%s\n\n\n" % item)


import base64
from PIL import Image
import io
from pathlib import Path
from _logger import logger
Path("images").mkdir(exist_ok=True, parents=True)


def process_base64_image():
    with open("images.txt", 'r') as f:
        _data = f.read()
    base64_str = _data.split("\n\n\n")
    for idx, k in enumerate(base64_str):
        if k:

            # Decode the base64 string to an image
            img_data = base64.b64decode(k)
            img = Image.open(io.BytesIO(img_data))

            # Check if the resolution is greater than 256x256
            width, height = img.size
            if width > 256 or height > 256:
                logger.info("Image resolution is greater than 256x256")
                # Write the image to a file
                img.save(f'images/{idx}'
                         f'.png', 'PNG')
            else:
                logger.info("Image resolution is not greater than 256x256")

process_base64_image()