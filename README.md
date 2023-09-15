# Automated Ticket Booking with Selenium (Acropolis museum)

This Python script automates the process of booking tickets on a website using the Selenium library. It is specifically designed for booking tickets on the website [https://etickets.theacropolismuseum.gr](https://etickets.theacropolismuseum.gr), using Firefox browser.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Important](#importantnotes)

## Prerequisites
Before running the script, make sure you have the following installed:
- [Python](https://www.python.org/downloads/)
- [Selenium](https://selenium-python.readthedocs.io/installation.html)
- [Geckodriver](https://github.com/mozilla/geckodriver/releases) (for Firefox)

## Installation
1. Clone this repository or download the script file.
   ```shell
   git clone https://github.com/GeorgeStampou/acropolis-bot.git
2. Change into the project directory.
   ```shell
   cd acropolis-bot-main
3. Install the required libraries if you haven't already:
   ```bash
   pip install selenium
4. Download and place the appropriate driver (e.g., Geckodriver) in the same directory as the script.
5. Update the script with your personal information.
   - Customize the form-filling process in the fill_out_form function. You can change the field names and values according to your needs.

## Usage

1. Run the script:
   ```shell
   python formbot.py
2. The script will automate the following steps:
- Language selection
- Date selection (3 days from the current date)
- Selection of ticket quantity (you can change the persons to the number you like. First person calculated already)
- Form filling with personal information
- Acceptance of terms and conditions
3. After running the script, it will proceed to the payment page. You can manually complete the payment process.

## Important Notes
- This script is provided for educational purposes only. Please use it responsibly and in compliance with the terms of use of the website you are automating.
- Website structures and elements may change over time, so the script may require updates to work with the latest version of the website.
