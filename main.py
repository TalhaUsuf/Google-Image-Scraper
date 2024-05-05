# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:02:06 2020

@author: OHyic

"""
# Import libraries
import os
import concurrent.futures
from GoogleImageScraper import GoogleImageScraper
from patch import webdriver_executable
from _logger import logger

# Test the logger


def worker_thread(search_key):
    image_scraper = GoogleImageScraper(
        webdriver_path,
        image_path,
        search_key,
        number_of_images,
        headless,
        min_resolution,
        max_resolution,
        max_missed)
    image_urls = image_scraper.find_image_urls()
    logger.info(f"Found {len(image_urls)} images for search key: {search_key}")
    image_scraper.save_images(image_urls, keep_filenames)

    # Release resources
    del image_scraper


if __name__ == "__main__":
    # Define file path
    webdriver_path = os.path.normpath(os.path.join(os.getcwd(), 'webdriver', webdriver_executable()))
    image_path = os.path.normpath(os.path.join(os.getcwd(), 'photos'))

    # Add new search key into array ["cat","t-shirt","apple","orange","pear","fish"]
    search_keys = list(set(["cat", "t-shirt"]))

    # Parameters
    number_of_images = 5  # Desired number of images
    headless = False  # True = No Chrome GUI
    min_resolution = (0, 0)  # Minimum desired image resolution
    max_resolution = (9999, 9999)  # Maximum desired image resolution
    max_missed = 10  # Max number of failed images before exit
    number_of_workers = 1  # Number of "workers" used
    keep_filenames = False  # Keep original URL image filenames

    logger.info(f"Webdriver path: {webdriver_path}")
    logger.info(f"number of images: {number_of_images}")
    logger.info(f"headless: {headless}")
    logger.info(f"min_resolution: {min_resolution}")
    logger.info(f"max_resolution: {max_resolution}")
    logger.info(f"max_missed: {max_missed}")
    logger.info(f"number_of_workers: {number_of_workers}")
    logger.info(f"keep_filenames: {keep_filenames}")

    # Run each search_key in a separate thread
    # Automatically waits for all threads to finish
    # Removes duplicate strings from search_keys
    with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_workers) as executor:
        executor.map(worker_thread, search_keys)
