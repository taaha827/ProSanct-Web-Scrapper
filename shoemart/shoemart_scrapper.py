#This Code is used to read the file names of the images and is then used to read those images and extracting text from those images and then storing all this data in the database that we have created
#Developed by Prosanct
#Develped Date: 7/5/2018
#Modified Date: 7/5/2018

import sys
sys.path.append('C:\\wamp64\\www\\daraz_scrapper')
import shoemart_scrapping_image
#importing the necessary libraries
from PIL import Image
#This library will help us read the addresses of the files 
import glob
#this is the external database class that we have created our selves
import database
#this library will process the images and will extract data from them
import pytesseract
#this is a neccessaty as it is used to set the run time enviroment variable in windows this address should be where you have downloaded and extracted the tesseract.exe file you can find that by a single google search
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\tesseract-ocr\\tesseract.exe'

#this check is used to check if the code run is running in the main class or not
if __name__ == "__main__":
    db = database.Database()
    obj = shoemart_scrapping_image.scraping("https://www.shoemartstores.com/ae/en/")
    obj.getresponse()   
    obj.extractresponse()
    obj.specificextraction()
    obj.saving_image()
#readding all the addresses of the images that we have stored in .jpg format
jpgs = glob.glob("C://wamp64/www/daraz_scrapper/shoemart\\*.jpg")

#readding all the addresses of the images that we have stored in .png format
pngs = glob.glob("C:/wamp64/www/daraz_scrapper/shoemart\\*.png")

#merging the list of addresses that we have stored
mergedList = jpgs + pngs

#now by using that list we extract the file names of the images and then using pytesseract to extract text from the images and then storing it in our database.

for path in mergedList:
    print(path)
    splitArr = path.split('\\')
    # Data Insert into the table
    query ="INSERT INTO daraz_data(`FilePath`,`TextRead`) VALUES(" + "'"+splitArr[1]+"','"+db.connection.escape_string(pytesseract.image_to_string(Image.open(str(path))))+"')"
    db.insert(query)

