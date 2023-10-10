# Mobile Phone Information Scraper

This Python script allows you to fetch detailed information about a mobile phone from the 91mobiles website based on its name. The script uses web scraping techniques to extract specifications and saves them in an Excel file for easy reference.

### Prerequisites

Before using this script, make sure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

Additionally, you need to install the following Python libraries:

```bash
pip install requests
pip install beautifulsoup4
pip install pandas
```
## Usage
To use the code, simply run the following command in the terminal:
```
python mobile_phone_specification.py
```
You will be prompted to enter the name of the mobile phone. Once you enter the name, the code will get the specifications of the phone and save them in an Excel file with the name of the phone.

## Example
```
[+] Enter mobile name: iphone 13 pro max

Screen Size: 6.7 inches
Resolution: 1284 x 2778 pixels
Processor: Apple A15 Bionic
RAM: 6GB
Storage: 128GB, 256GB, 512GB, 1TB
Rear Camera: 12MP + 12MP + 12MP
Front Camera: 12MP
Battery: 4352mAh
Operating System: iOS 15
```
### Output
The code will generate an Excel file with the name of the mobile phone, containing the following columns:

Key
Value
The Key column will contain the names of the specifications, and the Value column will contain the values of the specifications.

## Disclaimer
Please be aware that web scraping may be subject to the terms of service of websites. Ensure you have the necessary permissions to scrape data from the 91mobiles website, and respect their policies.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
