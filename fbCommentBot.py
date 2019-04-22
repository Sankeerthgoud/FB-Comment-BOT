#Credits https://github.com/parane
import selenium
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import argparse
import time

# Uncomment this for invisible browser
# display = Display(visible=0)
# display.start() credit Chirag Rathod (Srce Cde) Email: chiragr83@gmail.com

class FbBot():

    def __init__(self, driver, username, password):

        self.driver = driver
        driver.implicitly_wait(3)
        login = self.driver.find_element_by_id("email")
        login.send_keys(username)
        login = self.driver.find_element_by_id("pass")
        login.send_keys(password)
        login.send_keys(Keys.RETURN)

        if driver.current_url != "https://www.facebook.com/":
            exit("Invalid Credentials")
            self.driver.quit()
        else:
            print("Login Successful")

        self.automate_comment()
        time.sleep(2)

    def automate_comment(self):
        self.driver.get("https://m.facebook.com/groups/373347030059013/permalink/378354062891643/")

        try:
            with open("quote.txt", errors='ignore') as ins:
                for line in ins:
                    print(line.rstrip('\n'));
                    wish = self.driver.find_element_by_id('composerInput')
                    wish.send_keys(line.rstrip('\n'))
                    time.sleep(5)
                    wish = self.driver.find_element_by_name('submit')
                    wish.click()
                    time.sleep(2)
        except Exception as e:
            print(e)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--u', help="Username")
    parser.add_argument('--p', help="Password")

    args = parser.parse_args()

    if not args.u:
        exit("Please specify FB username using --u=parameter")
    if not args.p:
        exit("Please specify FB password using --p=parameter")

    try:
        print("started");
		
        driver = webdriver.Chrome(executable_path=r'C:\python3\chromedriver\chromedriver.exe')
        driver.get("https://www.facebook.com/")
       
        f = FbBot(driver, args.u, args.p)
        driver.implicitly_wait(5)

        print("Thanks for using!!!")

    except KeyboardInterrupt:
        exit("User Aborted")

    except BaseException as e:
        exit("Invalid parameter\n"+str(e))

if __name__ == "__main__":
    main()
