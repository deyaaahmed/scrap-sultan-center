#!/usr/bin/env python3
# /* All Code As Below Was Written By 7azabet */

# This very simple script, basically is used to
# scrap any data from 'sultan-center.com' website *_^


import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from csv import writer
import pandas as pd
from os import getcwd, chdir
import os


# Using Class ( Object Oriented Programming >>> OOP )
class Scrapper:
    # Scrapping Function To Scrap 'sultan-center.com' website.
    def __init__(self):
        self._captions = 0
        self._imagesLinks = 0
        self._imagesLinksList = []
        self._measurementUnits = 0
        self._totalPrice = 0

    def scrap(self, url):
        # captions = 0
        # imagesLinks = 0
        # imagesLinksList = []
        # measurementUnits = 0
        # url = "https://www.sultan-center.com/food/snack-beverage/biscuits.html"

        response = requests.get(url)

        pageSource = response.text

        soup = BeautifulSoup(pageSource, "html.parser")

        products = soup.findAll(class_="item product product-item")
        # CSV File Name
        csvFileName = url.split('/')[-1].replace('.html', '').strip() + ".csv"
        # Inserting Data Into CSV File
        with open(f"{csvFileName}", "w") as csvFile:
            csvWriter = writer(csvFile)
            for product in products:
                # ------------------------------------ SCRAPPED DATA ------------------------------------ #
                # Caption Of The Image Product
                caption = product.find(class_="product-item-link").get_text().strip()
                self._captions += 1
                # Link Of The Image Product
                imageLink = product.find(class_="product-image-photo")['src']
                self._imagesLinks += 1
                self._imagesLinksList.append(imageLink)
                # Measurement Unit Of Product
                measurement = product.find(class_="product_measurement").find("span").get_text().strip()
                self._measurementUnits += 1
                price = product.find(class_="price").find('span').get_text().strip()
                self._totalPrice += float(price)
                ''' of course you can store this data inside any file with any format '''
                # ------------------------------------ WRITING INFO ------------------------------------ #
                csvWriter.writerow([caption, imageLink, price, measurement])

            # ------------------------------------ PRINTING INFO ------------------------------------ #
            # print(caption)
            # print(imageLink)
            # print(measurement)
        # ------------------------------------ SETTING HEADERS ------------------------------------ #
        csvFile2 = pd.read_csv(csvFileName)
        csvFile2.to_csv(csvFileName, header=["Product Caption", "Product Image Link", "Product Price", "Product "
                                                                                                       "Measurement "
                                                                                                       "Unit"],
                        index=False)
        print(f"""\n
    ####################################
    $           Products Info          $
    ####################################
    1) Number Of Capions = {self._captions} 
    2) Number Of Image Links = {self._imagesLinks} 
    3) Number Of Total Price = {self._totalPrice} KWD 
    4) Number Of Measuerments Units = {self._measurementUnits} 
    ####################################
        \n""")

    current_path = getcwd()

    def donwloadImages(self, path=current_path):
        """Invoking This Method Will download all images that scrapped\nThe default path is current working directory""".title()
        if not os.path.exists(path):
            os.mkdir(path)
        chdir(path)
        for imageLink in self._imagesLinksList:
            imageName = imageLink.split("/")[-1].strip()
            try:
                urlretrieve(imageLink, imageName)
                print(f"{imageName} has been downloaded successfully!".title())
            except:
                pass


# Creating An Object From Our Class.
scrapper = Scrapper()

# Scrap Link For Only Testing.
# In This Example, We'll Scrap Biscuits :)
scrapper.scrap("https://www.sultan-center.com/food/snack-beverage/biscuits.html")

# Let's Try Our Download Images Method.
scrapper.donwloadImages("biscuitsImages")

# Creating A New Object From Our Class.
# scrapper2 = Scrapper()
# scrapper2.scrap("https://www.sultan-center.com/food/snack-beverage/biscuits/cookies-biscuits.html")
# scrapper2.donwloadImages()

# Using A Function
# """# Scrapping Function To Scrap 'sultan-center.com' website.
# def scrap(url):
#     captions = 0
#     imagesLinks = 0
#     measurementUnits = 0
#     # url = "https://www.sultan-center.com/food/snack-beverage/biscuits.html"
#
#     response = requests.get(url)
#
#     pageSource = response.text
#
#     soup = BeautifulSoup(pageSource, "html.parser")
#
#     products = soup.findAll(class_="item product product-item")
#
#     for product in products:
#         # ------------------------------------ SCRAPPED DATA ------------------------------------ #
#         # Caption Of The Image Product
#         caption = product.find(class_="product-item-link").get_text().strip()
#         captions += 1
#         # Link Of The Image Product
#         imageLink = product.find(class_="product-image-photo")['src']
#         imagesLinks += 1
#         # Measurement Unit Of Product
#         measurement = product.find(class_="product_measurement").find("span").get_text().strip()
#         measurementUnits += 1
#         # ------------------------------------ PRINTING INFO ------------------------------------ #
#         print(caption)
#         print(imageLink)
#         print(measurement)
#     print(f"""\n
#     ####################################
#     Number Of Capions = {captions}
#     Number Of Image Links = {imagesLinks}
#     Number Of Measuerments Units = {measurementUnits}
#     ####################################
#     \n""")
#
#
# # Scrapping Fruits
# scrap("https://www.sultan-center.com/catalogsearch/result/?q=fruits")
#
# # Scrapping Chocolates
# scrap("https://www.sultan-center.com/food/snack-beverage/chocolate-snacks.html")
# """

"""Best Wishes!
7azabet."""
