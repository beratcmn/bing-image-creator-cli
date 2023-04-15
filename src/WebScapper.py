"""
### Selenium Wrapper and Helper Functions
"""


from dataclasses import dataclass

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests

from pyvda import AppView

import helpers as h

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

    imagePrompt = ""
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

    def get_prompt_input_element(self):
        while True:
            try:
                element = self.driver.find_element(
                    By.XPATH, "/html/body/div[2]/div[2]/div[2]/form/div/input[1]"
                )
                print("Prompt element found!")
                return element
            except:
                print("Prompt element not found, refreshing...")
                self.driver.get(self.PAGE_URL)
                time.sleep(5)

    def generate_image(self):
        self.driver.get(self.PAGE_URL)
        time.sleep(5)
        prompt_input_element = self.get_prompt_input_element()

        os.system("cls")

        self.imagePrompt = input("Enter prompt: ")

        prompt_input_element.send_keys(self.imagePrompt)
        prompt_input_element.submit()

        print("Generating images...")

        try:
            first_image = WebDriverWait(self.driver, 45).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "/html/body/div[2]/div/div[5]/div[1]/div/div/div/ul[1]/li[1]/div/div/a",
                    )
                )
            )
        finally:
            print("Images generated.")

    def save_image_urls(self) -> list[str]:
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
            filename = h.to_kebab_case(self.imagePrompt) + ".txt"
            print(filename)
            with open("outputs/" + filename, "w") as f:
                f.write(
                    self.imagePrompt
                    + "\n"
                    + images_total
                    + "\n"
                    + image_1
                    + "\n"
                    + image_2
                    + "\n"
                    + image_3
                    + "\n"
                    + image_4,
                )

            return [images_total, image_1, image_2, image_3, image_4]

    def save_images(self, urls: list[str]):
        print("Saving images...")

        image_names = []

        for url in urls:
            name = self.save_image(url, urls.index(url))
            image_names.append(name)

        h.create_image_grid(h.to_kebab_case(self.imagePrompt), image_names)

    def save_image(self, url: str, index: int = 0):
        time.sleep(2)

        self.driver.get(url)
        try:
            print("Waiting for image to load...")
            image = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "/html/body/div[2]/div/div/div[1]/div/div[2]/div/div/div[2]/div/div/img",
                    )
                )
            )
            print("Image found.")
            image_url = image.get_attribute("src")
            image_data = requests.get(image_url).content
            image_name = (
                "outputs/"
                + h.to_kebab_case(self.imagePrompt)
                + "-"
                + str(index)
                + ".png"
            )
            with open(
                image_name,
                "wb",
            ) as handler:
                handler.write(image_data)
        finally:
            return image_name

    def start(self):
        while True:
            self.generate_image()
            urls = self.save_image_urls()
            self.save_images(urls=urls[1:])

            if input("Generate another image? (y/n): ") == "n":
                break
