# Auto Purchase Bot

![Cover Image](cover-image-url.jpg)

This repository contains a Selenium-based bot that automatically logs in to the Online Shop website(takes Momoshop as example) and attempts to purchase a specified product. The bot continuously checks for the availability of the product and clicks the "Buy" button when it becomes available.

## Features

- Automated login to Momoshop website
- Continuous checking for product availability
- Automated clicking of "Buy" and "Checkout" buttons
- User prompt to exit the script

## Prerequisites

- Python 3.x
- Chrome browser
- ChromeDriver compatible with your Chrome version

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/auto-purchase-bot.git
    cd auto-purchase-bot
    ```

2. Install the required Python packages:

    ```bash
    pip install selenium
    ```

3. Download the ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in your system's PATH.

## Usage

1. Open the `auto_purchase_bot.py` file and update the following lines with your Momoshop account credentials:

    ```python
    driver.find_element(By.ID, 'memId').send_keys('YOUR_USERNAME')
    driver.find_element(By.ID, 'passwd').send_keys('YOUR_PASSWORD')
    ```

2. Optionally, you can change the product URL to the one you want to purchase:

    ```python
    driver.get("https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=YOUR_PRODUCT_CODE")
    ```

3. Run the script:

    ```bash
    python auto_purchase_bot.py
    ```

4. After logging in, the script will wait for you to press Enter to start the auto-purchase process.

5. The bot will continuously check for the availability of the product and attempt to purchase it when available. You can exit the script by typing "QUIT" when prompted.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or bug fixes.
