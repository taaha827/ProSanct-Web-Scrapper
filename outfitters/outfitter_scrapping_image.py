#This Code is used to scrap images from different websites depending on their structure
#Developed by Prosanct
#Develped Date: 7/5/2018
#Modified Date: 7/5/2018

from bs4 import BeautifulSoup
from selenium import webdriver
import re
import requests

class scraping:
    url = None
    browser= None
    html = None
    soup = None
    img = None
    imgs =None
    def __init__(self):
        self.url="http://pixabay.com"
        print(self.url+"Default Constructor is called")
    def __init__(self,data):
        #This is where the link of the website goes which we want to scrap
        self.url=data
        print(self.url)

    def getresponse(self):
        #We use PhantomJS because we want the fully loaded page, not the response that is given by the browser in which the scripts have not run
        self.browser = webdriver.PhantomJS() 
        self.browser.get(self.url) 
        

    #this is to get that specific webpage
    def extractresponse(self):
        #extracting the elements of the returned web page
        self.html = self.browser.page_source  
        self.soup = BeautifulSoup(self.html, 'html.parser') 
    def specificextraction(self):        
        slider_div = self.soup.find_all("section",{"class":"container-fluid box-baners"})  
        stri = str(slider_div)
        soup1 = BeautifulSoup(stri,'html.parser')
        self.imgs = soup1.find_all('img')
    def saving_image(self):
        u = "https://"
        urls = [img['src'] for img in self.imgs]
        a=1
        for url in urls:
            filename = re.search(r'/([\w_-]+[.](jpg|gif|png))', url)
            print(filename)
            if filename is None:
                print("Data is none in outfitters")
            else:    
                with open(filename.group(1), 'wb') as f:
                #if 'http' not in url:
                # sometimes an image source can be relative 
                # if it is provide the base url which also happens 
                # to be the site variable atm. 
                # url = '{}{}'.format(site, url)
                #getting the image at the mentioned source
                    u='http:'
                    u =u+url
                    print(u)
                    response = requests.get(u)
                    #Saving it in the directory where the script is running
                    f.write(response.content)


