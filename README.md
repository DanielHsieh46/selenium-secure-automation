# selenium-secure-automation
A lightweight Python library that extends Selenium with secure and resilient element interactions, featuring built-in retries, timeouts, and safe fallbacks to reduce flaky test failures.

---

## Features
- 🔒 **Secure wrappers** around common Selenium actions (click, send_keys, select, get text/attributes).
- ⏱ **Automatic retries and timeouts** for more reliable automation in unstable environments.
- 🧩 **Consistent API design** – every helper follows the same pattern, making it predictable and easy to use.
- 🛠 **Supports both `WebDriver` and `WebElement`** as entry points via a shared context resolver.
- 🧾 **Debug utilities** to quickly inspect element texts.
---
## Installation
1. This library is just a helper script. Copy `secure_operate.py` into your project and import it:
   
```python
from secure_operate import (
    secure_click,
    secure_send_keys,
    secure_get_text,
    secure_get_attribute,
    secure_find_all_elements,
)
```

2. Install the required dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
```

This will install Selenium 4.28.1, the version this library was tested with.
      
---

## Usage Examples

### Clicking safely

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from secure_operate import secure_click

driver = webdriver.Chrome()
driver.get("https://example.com")

secure_click(driver, By.ID, "submit-button")
```

### Sending keys with retries

```python
secure_send_keys(driver, By.NAME, "username", "my_user")
secure_send_keys(driver, By.NAME, "password", "secret")
```

### Selecting from dropdowns

```python
secure_select_by_visible_text(driver, By.ID, "country", "Taiwan")
```

### Extracting values or text

```python
text = secure_get_text(driver, By.CSS_SELECTOR, ".title")
value = secure_get_value(driver, By.NAME, "email")
outer_html = secure_get_attribute(driver, By.XPATH, "//table", "outerHTML")
```

### Waiting for presence

```python
element = secure_presence_wait(driver, By.CLASS_NAME, "dynamic-item")
```

### Finding multiple elements

```python
items = secure_find_all_elements(driver, By.CSS_SELECTOR, ".list-item")
for item in items:
    print(item.text)
```

### Debugging element texts

```python
debug_element_texts(driver, By.CSS_SELECTOR, ".product-title")
```

### Output

```text
Found 3 element(s) for .product-title:
[0] .text = 'PlayStation 5', innerText = 'PlayStation 5'
[1] .text = 'Xbox Series X', innerText = 'Xbox Series X'
[2] .text = 'Nintendo Switch', innerText = 'Nintendo Switch'
```

---

## API Reference

All secure functions share the same consistent pattern:

```python
secure_action(driver_or_element, by, locator_value, ..., timeout=10, retries=3)
```

* **driver\_or\_element**: a `WebDriver` or `WebElement` instance
* **by**: Selenium locator strategy (`By.ID`, `By.XPATH`, etc.)
* **locator\_value**: string locator value
* **timeout**: maximum wait time in seconds (default: 10)
* **retries**: how many times to retry before raising (default: 3)

### Provided functions

* `secure_click` – waits until clickable, then clicks
* `secure_js_click` – clicks via JavaScript
* `secure_send_keys` – clears then sends keys
* `secure_send_keyboard` – sends keys (without clear)
* `secure_select_by_visible_text` – selects from a `<select>` dropdown
* `secure_get_text` – returns `.text`
* `secure_js_get_text` – returns `textContent` or `innerText` via JS
* `secure_get_value` – returns `.get_attribute("value")`
* `secure_get_attribute` – returns a given attribute
* `secure_presence_wait` – waits for element presence and returns it
* `secure_find_all_elements` – waits for all elements and returns list
* `debug_element_texts` – prints `.text` and `innerText` for debugging

---

## Philosophy

This library enforces **strict consistency**:

* Same function signatures across all helpers.
* Identical retry logic (`print("retrying...")` + `time.sleep(2)`).
* Minimal surprises – every function follows the same pattern.

This makes the helpers easy to remember, predictable to use, and reduces flaky Selenium scripts in real-world automation.









