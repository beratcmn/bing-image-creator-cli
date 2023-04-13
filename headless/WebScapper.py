"""
### Selenium Wrapper and Helper Functions
"""


from dataclasses import dataclass

from selenium import webdriver
from selenium.webdriver.common.by import By

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

    def open_browser(self):
        self.driver.get(self.PAGE_URL)

        self.browserWindowHWND = AppView.current().hwnd

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

    def generate_image(self):
        self.driver.get(self.PAGE_URL)
        time.sleep(5)
        prompt_input_element = self.get_prompt_input_element()

        os.system("cls")

        prompt = input("Enter prompt: ")

        prompt_input_element.send_keys(prompt)
        prompt_input_element.submit()

        print("Generating image...")
        time.sleep(10)

    def start(self):
        # self.open_browser()
        while True:
            self.generate_image()

            if input("Generate another image? (y/n): ") == "n":
                break
