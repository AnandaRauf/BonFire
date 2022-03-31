from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import os
import pyfiglet
from capmonster_python import RecaptchaV2Task #Must top up balance
#from Recap import RecaptchaV2Selenium #Library maintenance by Ananda Rauf Maududi
#import requests
#import time
print("---------------------------------------------------------------------\n")
text= "BonFire"
art_text = pyfiglet.figlet_format(text)
version= "Version 1.0.0\n"
print(art_text)
print(version)
devby= "Developed by Ananda Rauf Maududi"
devdate= "Developed date 25 March 2022"
print(devby)
print(devdate)
print("---------------------------------------------------------------------\n")



class MenuBonFire():
    def menu():
        print("Menu BonFire:")
        print
        print("1.Bot Auto Claim ClaimSol.xyz")
        print("2.Bot Auto Claim FaucetCrypto.com")
        print("3.Bot Auto Claim AutoFaucet.org")
        print("4.Exit")

class AutoClaimSolana():
    def autoclaimsolana(self):
        
        
        
        opendriver = webdriver.Chrome(executable_path=r'webdriver/chromedriver.exe')
        openbrowser = opendriver
        print("You're choose bot Auto Claim ClaimSol")

        target = "https://claimsol.xyz/login"
        openbrowser.get(target)
        
        user_account= open("AccountClaimSol.txt")
        check_user = user_account.readlines()
        login_user_username = check_user[0]
        login_user_pw = check_user[1]
        elementID = openbrowser.find_element_by_id('password')
        elementID.send_keys(login_user_pw)
        elementID = openbrowser.find_element_by_id('email')
        elementID.send_keys(login_user_username)
        elementID = openbrowser.find_element_by_id('password')
        elementID.send_keys(login_user_pw)
        elementID = openbrowser.find_element_by_id('email')
        elementID.send_keys(login_user_username)
        
        

        #Bug Library Recap TypeError: __init__() missing 2 required positional arguments: '_client_key' and 'executable_path'

        #BotRecap = RecaptchaV2Selenium()
        #BotRecap._get_site_key()

        #BotRecap._solve_recaptcha()
        #BotRecap.submit_form()

        
        #Sitekey Recaptcha from website ClaimSol
        
        sitekey_recaptchaV2= "6LfyhQofAAAAAPM-CHSPHupt-TB8kP9Ztuajwt2_"

        #with open(r"apikey2Captcha.txt", "r") as f:
            #api_key_two_captcha = f.read()

        #form = {"method": "userrecaptcha",
                # "googlekey": sitekey_recaptchaV2,
                 #"key": api_key_two_captcha, 
                 #"pageurl": target, 
                 #"json": 1}

        #response_bot_bypass_recaptchaV2 = requests.post('http://2captcha.com/in.php', data=form)
        #request_id = response_bot_bypass_recaptchaV2.json()['request']

        #url_bot_bypass_recaptchaV2 = f"http://2captcha.com/res.php?key={api_key_two_captcha}&action=get&id={request_id}&json=1"
        #status = 0
        #while not status:
            #res = requests.get(target)

            #if res.json()['status']==0:
                #time.sleep(3)

            #else:
                #requ = res.json()['request']
                #js = f'document.getElementById("g-recaptcha-response").innerHTML="{requ}";'
                #openbrowser.execute_script(js)
                #elementID.find_element_by_class('btn btn-pill text-white btn-block btn-primary').click()
                #openbrowser.find_element_by_tag('p')
                #openbrowser.get_attribute('innerHTML')
                #status = 1

        
        apikey_CapMonsta= "6972cc6613c49aa71b391100dc801ee0"
        captcha = RecaptchaV2Task(apikey_CapMonsta) #apikey_CapMosnta 
        task_start = captcha.create_task(target,sitekey_recaptchaV2,no_cache=True)
        captcha.join_task_result(task_starts=task_start, maximum_time=180)
        
        
        elementID.submit()
        #elementID.find_element_by_class('btn btn-pill text-white btn-block btn-primary').click()
        sleep(10)
        elementID.find_element_by_tag('p')
        element.get_attribute('innerHTML')

class FaucetCryptoClaim():
    def faucetcryptoclaim(self):
        s= Service("webdriver/chromedriver.exe")
        opendriver = webdriver.Chrome('service=s')
        openbrowser = opendriver
        print("You're choose bot Auto Claim FaucetCrypto.com\n")
        openbrowser.get("https://faucetcrypto.com/login")
        user_account= open("AccountFaucetCrypto.txt")
        check_user = user_account.readlines()
        login_user = check_user[0]
        login = openbrowser.get(login_user)

        print(login,"(FaucetCrypto):","[INFO][USERNAME]","anandarauf02\n")
        print("(FaucetCrypto):","HAS BEEN LOGIN\n")
        print("(FaucetCrypto):[USERINFO]","Test\n")

class AutoFaucetClaim():
    def autofaucetclaim(self):
        s= Service("webdriver/chromedriver.exe")
        opendriver = webdriver.Chrome('service=s')
        openbrowser = opendriver
        print("You're choose bot Auto Claim AutoFaucet.org\n")
        openbrowser.get("https://www.autofaucet.org/login")
        user_account= open("AccountFaucetCrypto.txt")
        check_user = user_account.readlines()
        login_user = check_user[0]
        login = openbrowser.get(login_user)

        print(login,"(AutoFaucet):","[INFO][USERNAME]","anandarauf02\n")
        print("(AutoFaucet):","HAS BEEN LOGIN\n")
        print("(AutoFaucet):[USERINFO]","Test\n")


MenuBonFire.menu()

choose= int(input("Choose menu:"))

ACSolana = AutoClaimSolana()
FC = FaucetCryptoClaim()
AF = AutoFaucetClaim()

if choose==1:
    ACSolana.autoclaimsolana()

elif choose==2:
    FC.faucetcryptoclaim()

elif choose==3:
    AF.autofaucetclaim()

elif choose==4:
    print("Thank you for using BonFire")
    exit

else:
    print("Sorry,not found")
    print("Please try again")
    MenuBonFire.menu()
    choose= int(input("Choose menu:"))


    

    
        
