# FB-Comment-BOT
FB Comment BOT

A basic python facebook-bot that can automate your comments in group. All you need to feed the group address and feed data into Input.txt(every line is posted as comment) 

# Requirements
It requires 
- Python 3.x (https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe)
- Selenium - After installing python open command prompt and run "pip install Selenium" command. ( set the path for python - https://geek-university.com/python/add-python-to-the-windows-path/)
- pyvirtualdisplay pakage - "pip install pyvirtualdisplay"
- Chrome Driver (http://chromedriver.chromium.org/downloads) Download appropriate driver based on your chrome version. and unizip it to 
"C:\python3\chromedriver\"
- Download the files "fbCommentBot.py" and "Input.txt" into a folder


# Usage:
From the above folder open command prompt(SHIFT+Right click) and run the command - "python fbCommentBot.py --u=username --p=password" to start the script. Sit back and watch it do the work.
 
*Change the group link at line 36

*Be aware scipt may abruptly stop if the page dosent load properly, just restart the script and trim the Input.txt file appropriately

Credits: https://github.com/parane
