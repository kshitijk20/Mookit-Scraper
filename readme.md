# Mookit Scraping

This script takes an argument ```n``` from the user where ```n``` is the number of lectures of a course ```MTH102AA```. The details of the lecture is stored in the CSV File. The ```mookit.csv``` stores:

* Week Number
* Lecture Name
* Link to the Video Lecture

## Getting Started

Implementation of web scraping in Python with Beautiful Soup Library

### Installation

Libraries that need to be installed via pip inorder to run the script:

* bs4
* lxml
* codecs
* pandas

### Installing the libraries

```
pip install bs4
```
```
pip install beautifulsoup4
```
```
pip install pandas
```
```
pip install lxml
```

### Importing the Librarires

```
from bs4 import BeautifulSoup
from lxml import html
import codecs
import pandas as pd
```

## Execution

* Use inspect option of the browser's developer tools to extract the HTML code of the required webpage on Mookit.
* Use Beautiful Soup library for scraping and parsing data from the HTML code.
* Build a script that fetches the data from the HTML code according to the User Input and displays relevant information.
* Use Pandas library to save the extracted data in the .csv file.