# ProSanct-Web-Scrapper
This is a repository which contains the project, that will be used to scrape different website and then finding which brands are having sales which then we can tell the customers\users of our app about.
If you are looking to set up on your own device then you need to follow some steps which are:
first you need to install the following packages: image, BeautifulSoup4, request selenium, pymsql, glob, pytesseract
To  install them go to the folder where you have installed python go to the Scripts folder run cmd there and write pip install *package_name_here*
First in each of the folder ther will be a file folder_name_scrapper.py file open\edit it and change 
after that change the path in "jpgs" and "pngs" to where ever you are running your script\project
other then that you are good to go.
You also need to install PhanotmJS in your Machine just copy PhantomJS.exe in every folder.
You can read more about phantomJS here:http://phantomjs.org
You need to create a database named daraz on your local host wamp server and then add a table daraz_data to it with the schema id(primary), FilePath(varchar),TextRead(varchar) with collation of TextRead to utf8_general_ci 
The last step is to change the file path in sys.append() to wherever you have stored the project in ever folder_name_scrapper.py
