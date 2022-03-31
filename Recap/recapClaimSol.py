from selenium import webdriver
from capmonster_python import RecaptchaV2Task
from time import sleep
import os

class RecaptchaV2Selenium:
    def __init__(self, _client_key, executable_path):
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
        self.captcha = RecaptchaV2Task(_client_key)
        self.browser = webdriver.Firefox(executable_path=executable_pathss)
        print("You're choose bot Auto Claim ClaimSol")
        self.website_url = "https://claimsol.xyz/login"

        
    def _get_site_key(self):
        self.browser.get("https://claimsol.xyz/login")
        return self.browser.find_element_by_class("g-recaptcha").get_attribute("data-sitekey")

    def _solve_recaptcha(self):
        self.captcha.set_user_agent(self.user_agent)
        task_id = self.captcha.create_task(website_url=self.website_url,
                                           website_key=self._get_site_key(),
                                           no_cache=True)
        return self.captcha.join_task_result(task_id=task_id, maximum_time=180).get("gRecaptchaResponse")

    def submit_form(self):
        #user_account= open("AccountClaimSol.txt")
        #check_user = user_account.readlines()
        #login_user_username = check_user[0]
        #self.login_user_pw = check_user[1]
        #self.browser.find_element_by_id('email')
        #self.browser.send_keys(login_user_username)
        #self.browser.find_element_by_id('password')
        #self.browser.send_keys(login_user_pw)
        
        self.browser.execute_script("document.getElementsByClassName('g-recaptcha-response')[0].innerHTML = "
                                    f"'{self._solve_recaptcha()}';")
        
        self.browser.find_element_by_class("btn btn-pill text-white btn-block btn-primary").click()
        sleep(10)
        self.browser.close()
        return self.browser.find_element_by_class_name("recaptcha-success")
        #self.browser.open()
        #self.browser.find_element_by_tag('p')
        #self.browser.get_attribute('innerHTML')

if __name__ == "__main__":
    #Client Key Cap Monster get from https://capmonster.cloud/en/:
    client_key = "6972cc6613c49aa71b391100dc801ee0"
    executable_pathss = "webdriver/chromedriver.exe"
    recaptcha_selenium = RecaptchaV2Selenium(client_key, executable_pathss)
