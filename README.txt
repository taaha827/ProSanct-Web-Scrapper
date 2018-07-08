# ProSanct-Web-Scrapper
This is a repository which contains the project, that will be used to scrape different website and then finding which brands are having sales which then we can tell the customers\users of our app about.
If you are looking to set up on your own device then you need to follow some steps which are:
Step 1:first you need to install the following packages: image, BeautifulSoup4,tesseract, request selenium, pymsql, glob, pytesseract
Step 1.1:To  install them go to the folder where you have installed python go to the Scripts folder run cmd there and write 
pip install *insert package_name_here*
Step 2:First in each of the folder ther will be a file *insert folder_name*_scrapper.py file open\edit it and change 
after that change the path in variables  "jpgs" and "pngs" to where ever you are running your script\project
Step 3:You also need to install PhanotmJS in your Machine, just copy PhantomJS.exe from the current repository in every folder.
       You can read more about phantomJS here:http://phantomjs.org
Step 4:You need to create a database named daraz on your local host wamp server and then add a table daraz_data to it with the schema id(primary), FilePath(varchar),TextRead(varchar) with collation of TextRead to utf8_general_ci, in the last build this step will be automated but for now this has to be done manually 
Step 5: The last step is to change the file path in sys.append() to wherever you have stored the project in ever folder_name_scrapper.py
