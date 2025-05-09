## Project Setup

1. **Clone the repository**

2. **Create a virtual environment**

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the test**
   ```bash
   pytest tests/test_payment_flow.py
   ```

---

## Project Structure & File Summary

### `configs/config.yaml`
Stores runtime values like `base_url` and custom amount. Avoids hardcoding test data.

### `configs/locators.yaml`
Centralized location for all XPath selectors used in the project. Makes maintenance easier.

---

### `pages/base_page.py`
Base class with reusable utility methods for waiting, clicking, sending keys, and checking visibility. All pages extend this to ensure DRY code.

### `pages/payment_page.py`
Page Object Model for the payment screen. Handles:
- Button clicks
- Bill splitting
- Tip selection
- Entering card details inside iframes
- Final payment submission and success verification

---

### `tests/test_payment_flow.py`
Main automation test:
- Navigates to the payment page
- Performs full payment flow using custom split
- Asserts key checkpoints
- Prints progress to the console for easier debug

---

### `utils/config_loader.py`
Loads values from `config.yaml`.

### `utils/reader.py`
Fetches element locators from `locators.yaml` using a `LocatorReader` class.

---

### `conftest.py`
Pytest fixture for initializing and closing a Chrome browser using `webdriver-manager`.

---

### `requirements.txt`
All required Python packages:
- selenium
- pytest
- webdriver-manager
- pyyaml
