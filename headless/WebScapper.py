"""
### Selenium Wrapper and Helper Functions
"""


from dataclasses import dataclass

from selenium import webdriver
from selenium.webdriver.common.by import By

import requests

from pyvda import AppView

import time
import os


@dataclass
class Scrapper:
    """
    ### Scrapper is a wrapper for Selenium that provides helper functions for scraping the Bing.


    #### Args:
        * defaultBrowser (str, default = edge): Default browser. "chrome" | "firefox" | "edge"
        * webdriverPath (str, default = /msedgedriver.exe): Path to the webdriver executable.
    """

    defaultBrowser: str = "edge"
    webdriverPath: str = "/msedgedriver.exe"
    PAGE_URL = "https://www.bing.com/create"
    edgeAutoLogin: bool = True

    browserWindowHWND = 0

    def __post_init__(self):
        if self.defaultBrowser == "chrome":
            self.driver = webdriver.Chrome(executable_path=self.webdriverPath)
        elif self.defaultBrowser == "firefox":
            self.driver = webdriver.Firefox(executable_path=self.webdriverPath)
        elif self.defaultBrowser == "edge":
            self.driver = webdriver.Edge(executable_path=self.webdriverPath)
        else:
            raise Exception("Invalid browser!")

    def open_browser(self, move_callback):
        self.driver.get(self.PAGE_URL)

        self.browserWindowHWND = AppView.current().hwnd
        move_callback()

        self.driver.maximize_window()

        time.sleep(5)

        # ? Cookie prompt
        self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div[2]/button[1]"
        ).click()

        time.sleep(5)

        if self.defaultBrowser == "edge" and self.edgeAutoLogin:
            self.get_prompt_input_element()
            print("Auto login successful!")

        # TODO Uncomment this line to pause the program after the browser is opened.
        # input("Press enter to continue...")

    def get_prompt_input_element(self):
        while True:
            try:
                print("Prompt element found!")
                return self.driver.find_element(
                    By.XPATH, "/html/body/div[2]/div[2]/div[2]/form/div/input[1]"
                )
            except:
                print("Prompt element not found, refreshing...")
                self.driver.get(self.PAGE_URL)
                time.sleep(5)

    # TODO Create a function to save images to local disk.
    def save_image(self, url: str):
        image_name = url.split("/")[-1]
        with open("image.png", "wb") as f:
            f.write(requests.get(url).content)

    def save_images(self):
        print("Saving images...")

        # ? Image xPaths
        # /html/body/div[2]/div/div[5]/div[1]/div/div/div/ul[1]/li[1]/div/div/a/div/img
        # /html/body/div[2]/div/div[5]/div[1]/div/div/div/ul[1]/li[2]/div/div/a/div/img
        # /html/body/div[2]/div/div[5]/div[1]/div/div/div/ul[1]/li[3]/div/div/a/div/img
        # /html/body/div[2]/div/div[5]/div[1]/div/div/div/ul[1]/li[4]/div/div/a/div/img

        print("Getting image 1...")
        image_1 = self.driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div[5]/div[1]/div/div/div/ul[1]/li[1]/div/div/a/div/img",
        ).get_attribute("src")

        print("Getting image 2...")
        image_2 = self.driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div[5]/div[1]/div/div/div/ul[1]/li[2]/div/div/a/div/img",
        ).get_attribute("src")

        print("Getting image 3...")
        image_3 = self.driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div[5]/div[1]/div/div/div/ul[1]/li[3]/div/div/a/div/img",
        ).get_attribute("src")

        print("Getting image 4...")
        image_4 = self.driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div[5]/div[1]/div/div/div/ul[1]/li[4]/div/div/a/div/img",
        ).get_attribute("src")

        print("Saving images...")
        self.save_image(image_1)
        self.save_image(image_2)
        self.save_image(image_3)
        self.save_image(image_4)

    def save_image_urls(self):
        print("Saving image URLs...")

        # ? Image xPaths
        # /html/body/div[2]/div/div[5]/div[1]/div/div/div/ul[1]/li[1]/div/div/a
        # /html/body/div[2]/div/div[5]/div[1]/div/div/div/ul[1]/li[2]/div/div/a
        # /html/body/div[2]/div/div[5]/div[1]/div/div/div/ul[2]/li[1]/div/div/a
        # /html/body/div[2]/div/div[5]/div[1]/div/div/div/ul[2]/li[2]/div/div/a

        # ? This has to be a try block because Bing doesn't always produce 4 images.
        images_total, image_1, image_2, image_3, image_4 = (
            self.driver.current_url,
            "",
            "",
            "",
            "",
        )
        try:
            print("Getting image 1...")
            image_1 = self.driver.find_element(
                By.XPATH,
                "/html/body/div[2]/div/div[5]/div[1]/div/div/div/ul[1]/li[1]/div/div/a",
            ).get_attribute("href")
            time.sleep(0.5)

            print("Getting image 2...")
            image_2 = self.driver.find_element(
                By.XPATH,
                "/html/body/div[2]/div/div[5]/div[1]/div/div/div/ul[1]/li[2]/div/div/a",
            ).get_attribute("href")
            time.sleep(0.5)

            print("Getting image 3...")
            image_3 = self.driver.find_element(
                By.XPATH,
                "/html/body/div[2]/div/div[5]/div[1]/div/div/div/ul[2]/li[1]/div/div/a",
            ).get_attribute("href")
            time.sleep(0.5)

            print("Getting image 4...")
            image_4 = self.driver.find_element(
                By.XPATH,
                "/html/body/div[2]/div/div[5]/div[1]/div/div/div/ul[2]/li[2]/div/div/a",
            ).get_attribute("href")
            time.sleep(0.5)
        except:
            print("An error occurred while getting image URLs.")
        finally:
            print("Saving URLs...")
            with open("image_urls.txt", "w") as f:
                f.write(
                    images_total + "\n",
                    image_1 + "\n" + image_2 + "\n" + image_3 + "\n" + image_4,
                )

    def generate_image(self):
        self.driver.get(self.PAGE_URL)
        time.sleep(5)
        prompt_input_element = self.get_prompt_input_element()

        os.system("cls")

        prompt = input("Enter prompt: ")

        prompt_input_element.send_keys(prompt)
        prompt_input_element.submit()

        print("Generating image...")
        time.sleep(15)

    def start(self):
        # self.open_browser()
        while True:
            self.generate_image()
            # self.save_images()
            self.save_image_urls()

            if input("Generate another image? (y/n): ") == "n":
                break
