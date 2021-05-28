import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

#UTILIZAR CHROME DRIVER GLOBAL
#CREADO: Luis Felipe Guevara Andrade
#FECHA:  2021-05-27

class TestSelectSelenium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.close()



    def test_ingle_input_filed(self):
        driver = self.driver
        driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
        text_message = driver.find_element_by_xpath("//input[@id='user-message']")
        button_show_message = driver.find_element_by_xpath("//button[contains(text(),'Show Message')]")

        text_message.send_keys('Hola Mundo')
        button_show_message.click()
        time.sleep(5)
        text_your_message = driver.find_element_by_xpath("//span[@id='display']")

        self.assertEqual('Hola Mundo', text_your_message.text)


    def test_single_checkbox(self):
        driver = self.driver
        driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")

        time.sleep(2)

        options_list = [
            "//input[@id='isAgeSelected']"
        ]

        for s in options_list:
            check_button = driver.find_element_by_xpath(s)
            check_button.click()

        text_message = driver.find_element_by_xpath("//div[@id='txtAge']")

        time.sleep(5)
        self.assertEqual("Success - Check box is checked", text_message.text)


    def test_radio_button_select(self):
        driver = self.driver
        driver.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")

        radio_button_male = driver.find_element_by_xpath(
            "//body/div[@id='easycont']/div[1]/div[2]/div[1]/div[2]/label[1]/input[1]"
        )

        button_show_message = driver.find_element_by_xpath("//button[@id='buttoncheck']")

        text_output = driver.find_element_by_xpath(
            "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[2]/p[3]"
        )
        time.sleep(3)
        radio_button_male.click()
        button_show_message.click()
        time.sleep(5)
        self.assertRegex(text_output.text, "Male")

    def test_radio_button_no_select(self):
        driver = self.driver
        driver.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")

        button_show_message = driver.find_element_by_xpath("//button[@id='buttoncheck']")

        text_output = driver.find_element_by_xpath(
            "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[2]/p[3]"
        )
        time.sleep(3)
        button_show_message.click()
        time.sleep(5)
        self.assertRegex(text_output.text, "is Not checked")


if __name__ == '__main__':
    unittest.main()
