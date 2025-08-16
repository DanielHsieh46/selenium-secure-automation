#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
import time

def _resolve_context(driver_or_element):
    if isinstance(driver_or_element, WebDriver):
        return driver_or_element, driver_or_element
    elif isinstance(driver_or_element, WebElement):
        return driver_or_element.parent, driver_or_element
    else:
        raise TypeError("Must pass WebDriver or WebElement")

def debug_element_texts(driver, by, locator_value):
    elements = driver.find_elements(by, locator_value)
    print(f"Found {len(elements)} element(s) for {locator_value}:")
    for i, el in enumerate(elements):
        print(f"[{i}] .text = '{el.text.strip()}', innerText = '{el.get_attribute('innerText').strip()}'")

def secure_select_by_visible_text(driver_or_element, by, locator_value, visible_text, timeout=10, retries=3):
    executor, context = _resolve_context(driver_or_element)
    for attempt in range(retries):
        try:
            element = WebDriverWait(context, timeout).until(EC.presence_of_element_located((by, locator_value)))
            dropdown = Select(element)
            dropdown.select_by_visible_text(visible_text)
            return
        except Exception as e:
            if attempt < retries - 1:
                print("retrying...")
                time.sleep(2)
            else:
                raise e

def secure_click(driver_or_element, by, locator_value, timeout=10, retries=3):
    executor, context = _resolve_context(driver_or_element)
    for attempt in range(retries):
        try:
            element = WebDriverWait(context, timeout).until(EC.element_to_be_clickable((by, locator_value)))
            element.click()
            return
        except Exception as e:
            if attempt < retries - 1:
                print("retrying...")
                time.sleep(2)
            else:
                raise e

def secure_send_keys(driver_or_element, by, locator_value, keys, timeout=10, retries=3):
    executor, context = _resolve_context(driver_or_element)
    for attempt in range(retries):
        try:
            element = WebDriverWait(context, timeout).until(EC.element_to_be_clickable((by, locator_value)))
            element.clear()
            element.send_keys(keys)
            return
        except Exception as e:
            if attempt < retries - 1:
                print("retrying...")
                time.sleep(2)
            else:
                raise e

def secure_js_click(driver_or_element, by, locator_value, timeout=10, retries=3):
    executor, context = _resolve_context(driver_or_element)
    for attempt in range(retries):
        try:
            element = WebDriverWait(context, timeout).until(EC.presence_of_element_located((by, locator_value)))
            executor.execute_script("arguments[0].click();", element)
            return
        except Exception as e:
            if attempt < retries - 1:
                print("retrying...")
                time.sleep(2)
            else:
                raise e

def secure_get_value(driver_or_element, by, locator_value, timeout=10, retries=3):
    executor, context = _resolve_context(driver_or_element)
    for attempt in range(retries):
        try:
            element = WebDriverWait(context, timeout).until(EC.presence_of_element_located((by, locator_value)))
            return element.get_attribute("value")
        except Exception as e:
            if attempt < retries - 1:
                print("retrying...")
                time.sleep(2)
            else:
                raise e

def secure_send_keyboard(driver_or_element, by, locator_value, keys, timeout=10, retries=3):
    executor, context = _resolve_context(driver_or_element)
    for attempt in range(retries):
        try:
            element = WebDriverWait(context, timeout).until(EC.presence_of_element_located((by, locator_value)))
            element.send_keys(keys)
            return
        except Exception as e:
            if attempt < retries - 1:
                print("retrying...")
                time.sleep(2)
            else:
                raise e

def secure_get_text(driver_or_element, by, locator_value, timeout=10, retries=3):
    executor, context = _resolve_context(driver_or_element)
    for attempt in range(retries):
        try:
            element = WebDriverWait(context, timeout).until(EC.presence_of_element_located((by, locator_value)))
            return element.text
        except Exception as e:
            if attempt < retries - 1:
                print("retrying...")
                time.sleep(2)
            else:
                raise e

def secure_presence_wait(driver_or_element, by, locator_value, timeout=10, retries=3):
    executor, context = _resolve_context(driver_or_element)
    for attempt in range(retries):
        try:
            element = WebDriverWait(context, timeout).until(EC.presence_of_element_located((by, locator_value)))
            return element
        except Exception as e:
            if attempt < retries - 1:
                print("retrying...")
                time.sleep(2)
            else:
                raise e

def secure_js_get_text(driver_or_element, by, locator_value, timeout=10, retries=3):
    executor, context = _resolve_context(driver_or_element)
    for attempt in range(retries):
        try:
            element = WebDriverWait(context, timeout).until(EC.presence_of_element_located((by, locator_value)))
            text = executor.execute_script("return arguments[0].textContent;", element).strip()
            if not text:
                text = executor.execute_script("return arguments[0].innerText;", element).strip()
            return text
        except Exception as e:
            if attempt < retries - 1:
                print("retrying...")
                time.sleep(2)
            else:
                raise e

def secure_find_all_elements(driver_or_element, by, locator_value, timeout=10, retries=3):
    executor, context = _resolve_context(driver_or_element)

    for attempt in range(retries):
        try:
            WebDriverWait(context, timeout).until(
                EC.presence_of_all_elements_located((by, locator_value))
            )
            elements = context.find_elements(by, locator_value)
            if elements:
                return elements
            else:
                raise Exception("Elements found but list is empty")

        except Exception as e:
            if attempt < retries - 1:
                print("retrying...")
                time.sleep(2)
            else:
                raise e

def secure_get_attribute(driver_or_element, by, locator_value, attribute, timeout=10, retries=3):
    executor, context = _resolve_context(driver_or_element)    
    for attempt in range(retries):
        try:
            element = WebDriverWait(context, timeout).until(
                EC.presence_of_element_located((by, locator_value))
            )
            return element.get_attribute(attribute)
        except Exception as e:
            if attempt < retries - 1:
                print("retrying...")
                time.sleep(2)
            else:
                raise e


# In[ ]:




