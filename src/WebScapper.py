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

is_first_image = True


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

        try:
            # ? Cookie prompt
            self.driver.find_element(
                By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div[2]/button[1]"
            ).click()

            time.sleep(5)
        except Exception:
            pass

        if self.defaultBrowser == "edge" and self.edgeAutoLogin:
            self.get_prompt_input_element()
            print("Auto login successful!")

    def get_prompt_input_element(self):
        while True:
            try:
                if is_first_image:
                    element = self.driver.find_element(
                        By.XPATH,
                        "/html/body/div[2]/div[4]/div[1]/div/div/div[1]/form/textarea",
                    )
                else:
                    element = self.driver.find_element(
                        By.XPATH, "/html/body/div[2]/div[2]/div[2]/form/div/input[1]"
                    )
                print("Prompt element found!")
                return element
            except Exception:
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

        while True:
            try:
                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            # "/html/body/div[2]/div/div[5]/div[1]/div/div/div/ul[1]/li[1]/div/div/a",
                            "/html/body/div[3]/div[1]/div[5]/div[1]/div[2]/div/div[1]/ul[1]/li[1]/div/div/a",
                        )
                    )
                )
                print("Images generated.")
                break
            except Exception as e:
                print("An error occurred while generating images:", str(e).strip()[:50])
                print("Refreshing page...")
                self.driver.get(self.driver.current_url)

    def save_image_urls(self) -> list[str]:
        print("Saving image URLs...")

        # ? Image xPaths
        image_path_1 = (
            "/html/body/div[3]/div/div[5]/div[1]/div/div/div[1]/ul[1]/li[1]/div/div/a"
        )
        image_path_2 = (
            "/html/body/div[3]/div/div[5]/div[1]/div/div/div[1]/ul[1]/li[2]/div/div/a"
        )
        image_path_3 = (
            "/html/body/div[3]/div/div[5]/div[1]/div/div/div[1]/ul[2]/li[1]/div/div/a"
        )
        image_path_4 = (
            "/html/body/div[3]/div/div[5]/div[1]/div/div/div[1]/ul[2]/li[2]/div/div/a"
        )

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
                image_path_1,
            ).get_attribute("href")
            time.sleep(0.5)

            print("Getting image 2...")
            image_2 = self.driver.find_element(
                By.XPATH,
                image_path_2,
            ).get_attribute("href")
            time.sleep(0.5)

            print("Getting image 3...")
            image_3 = self.driver.find_element(
                By.XPATH,
                image_path_3,
            ).get_attribute("href")
            time.sleep(0.5)

            print("Getting image 4...")
            image_4 = self.driver.find_element(By.XPATH, image_path_4).get_attribute(
                "href"
            )
            time.sleep(0.5)
        except Exception as e:
            print("An error occurred while getting image URLs:", str(e))
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
            print("Saving image from URL: ", url)
            name = self.save_image(url, urls.index(url))
            image_names.append(name)

        h.create_image_grid(h.to_kebab_case(self.imagePrompt), image_names)

    def save_image(self, url: str, index: int = 0):
        time.sleep(3)

        self.driver.get(url)
        image_name = ""
        try:
            print("Waiting for image to load...")
            if index == 0:
                image = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            # "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[2]/div/div/div/img",
                            "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div/div/img",
                        )
                    )
                )
            else:
                image = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[2]/div/div/div/img",
                            # "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div/div/img",
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
        except Exception as e:
            print("An error occurred while saving image:", str(e))
        finally:
            return image_name

    def start(self):
        global is_first_image

        while True:
            self.generate_image()
            urls = self.save_image_urls()
            self.save_images(urls=urls[1:])

            if input("Generate another image? (y/n): ") == "n":
                break

            is_first_image = False
