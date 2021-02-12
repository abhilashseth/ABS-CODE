from selenium import webdriver
import config

class Driver:
    def __init__(self):
        self.DRIVER_OBJ = webdriver.Chrome('/home/abhilash/Documents/Project/personal-project/Selenium project/chromedriver_linux64/chromedriver')