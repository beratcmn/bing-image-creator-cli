from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import os

driver = webdriver.Edge(executable_path="/msedgedriver.exe")

PAGE_URL = "https://www.bing.com/create"

driver.get(PAGE_URL)

time.sleep(5)

# ? Cookie prompt
driver.find_element(
    By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div[2]/button[1]"
).click()

time.sleep(5)


def get_prompt_input_element():
    while True:
        try:
            print("Prompt element found!")
            return driver.find_element(
                By.XPATH, "/html/body/div[2]/div[2]/div[2]/form/div/input[1]"
            )
        except:
            print("Prompt element not found, refreshing...")
            driver.get(PAGE_URL)
            time.sleep(5)


def generate_image():
    driver.get(PAGE_URL)
    time.sleep(5)
    prompt_input_element = get_prompt_input_element()

    os.system("cls")

    prompt = input("Enter prompt: ")

    prompt_input_element.send_keys(prompt)
    prompt_input_element.submit()

    print("Generating image...")
    time.sleep(10)

    # input("Press enter to continue...")


if __name__ == "__main__":
    while True:
        generate_image()

        if input("Generate another image? (y/n): ") == "n":
            break
