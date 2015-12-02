# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException

def driver():
    url = os.getenv('SELENIUM_HUB')
    if None == url:
        return webdriver.Chrome()
    else:
        return webdriver.Remote(url, desired_capabilities=DesiredCapabilities.CHROME)

wait_seconds = 30
driver = webdriver.Chrome();
wait = WebDriverWait(driver, wait_seconds)

default_engine = By.CSS_SELECTOR

def useXpath():
    global default_engine
    default_engine = By.XPATH

def goto(url):
    driver.get(url)

def waitPage(title):
    wait.until(EC.title_is(title))

def switchToWindow(title):
    handles = driver.window_handles
    while len(handles) == 1:
        handles = driver.window_handles
    driver.switch_to_window(handles[len(handles) - 1])
    try:
        waitPage(title)
    except TimeoutException:
        driver.switch_to_window(handles[len(handles) - 2])

def switchToLightbox(path):
    wait.until(EC.visibility_of_element_located((default_engine, path)))

def switchToFrame(name):
    wait.until(EC.visibility_of_element_located((By.ID, name)))
    driver.switch_to_frame(name)

def getXPathByDynamicId(tag, value):
    return '//' + tag + '[contains(@id, "' + value +'")]'

def getXPathByText(tag, value):
    return '//' + tag + '[contains(., "' + value +'")]'

def click(path):
    if wait_seconds > 0:
        element = wait.until(EC.element_to_be_clickable((default_engine, path)))
    else:
        element = driver.find_element(default_engine, path)
    try:
        element.click()
    except Exception, e:
        driver.execute_script('arguments[0].scrollIntoView(true)', element)
        element.click();

def rightClick(path):
    ActionChains(driver).context_click(driver.find_element(default_engine, path)).perform()

def doubleClick(path):
    ActionChains(driver).double_click(driver.find_element(default_engine, path)).perform()

def drag(sourcePath, targetPath):
    source = driver.find_element(default_engine, sourcePath)
    target = driver.find_element(default_engine, targetPath)
    ActionChains(driver).drag_and_drop(source, target).perform()

def select(path, index):
    if wait_seconds > 30:
        click(path)
        Select(driver.find_element(default_engine, path)).select_by_index(index)
    elif wait_seconds > 20:
        Select(wait.until(EC.visibility_of_element_located((default_engine, path)))).select_by_index(index)
    else:
        Select(driver.find_element(default_engine, path)).select_by_index(index)

def selectByText(path, text):
    if wait_seconds > 30:
        click(path)
        Select(driver.find_element(default_engine, path)).select_by_visible_text(text)
    elif wait_seconds > 20:
        Select(wait.until(EC.visibility_of_element_located((default_engine, path)))).select_by_visible_text(text)
    else:
        Select(driver.find_element(default_engine, path)).select_by_visible_text(text)

def inputText(path, text):
    if wait_seconds > 0:
        wait.until(EC.visibility_of_element_located((default_engine, path))).send_keys(text)
    else:
        driver.find_element(default_engine, path).send_keys(text)

def getText(path):
    if wait_seconds > 0:
        return wait.until(EC.presence_of_element_located((default_engine, path))).text
    else:
        return driver.find_element(default_engine, path).text

def pressCtrlX(key):
    ActionChains(driver).key_down(Keys.CONTROL).send_keys(key).key_up(Keys.CONTROL).perform()

def selectAll():
    pressCtrlX('a')

def copy():
    pressCtrlX('c')

def paste():
    pressCtrlX('v')
