from selenium import webdriver
import os , time
import re
from selenium.webdriver.common.keys import Keys


def chat():
    search_key = input("Who do you want me to chat with? : ")
    your_name = input("Enter you name (as provided on whatsapp): ")
    your_number = input("Enter you number on whatsapp (Format- : +xx xxxxx xxxxx")
    try:
        url = "https://web.whatsapp.com/"
        url2=  "https://www.cleverbot.com/"

        options = webdriver.ChromeOptions()
        chromedriver = "D://chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        options.add_argument(r'--user-data-dir=C:\Users\xxx\AppData\Local\Google\Chrome\User Data')
        browser = webdriver.Chrome(chromedriver,chrome_options=options)
        type(browser)

        browser.get(url)
        time.sleep(3)
        while True:
            try:
                logged_in = browser.find_element_by_css_selector('#side')
                if logged_in:
                    break
                else:
                    pass
            except:
                pass
            time.sleep(0.5)
        search_bar = browser.find_element_by_css_selector('#side > div.search-container > div > label > input')
        search_bar.click()
        search_bar.send_keys(search_key)
        if (browser.current_url == url):
            pass
        else:
            browser.close()
            chat()
        time.sleep(3)
        found = browser.find_element_by_xpath('//*[@title="'+ search_key +'"]')
        found.click()
        time.sleep(1)
        browser.find_element_by_css_selector('body').send_keys(Keys.CONTROL + "t")
        browser.switch_to.window(browser.window_handles[-1])
        browser.get(url2)
        if (browser.current_url == url2):
            pass
        else:
            browser.close()
            chat()
        browser.find_element_by_css_selector('body').send_keys(Keys.CONTROL + "\t")
        browser.switch_to.window(browser.window_handles[0])
        if (browser.current_url == url):
            pass
        else:
            browser.close()
            chat()
        while True:
            if (browser.current_url == url):
                pass
            else:
                browser.close()
                chat()
            messages = browser.find_elements_by_class_name('bubble-text')
            for message in messages:
                id = ""
                code = message.get_attribute('innerHTML')
                try:
                    emoji = re.findall(r'<span class="emojitext selectable-text"><img alt="(.*?)".*?</span>',code)[0]
                except:
                    pass
                my_data_list = re.findall(r'<span class="message-pre-text">(.*?)</span>', code)
                my_data = my_data_list[0]
                elements = re.findall(r'<!-- react-text:.*?-->(.*?)<!-- /react-text -->', my_data)
                try_id = re.findall(
                    r'<span class="screen-name-text" dir="auto"><!-- react-text:.*?-->(.*?)<!-- /react-text -->', code)
                if len(try_id) < 1:
                    id = elements[3]
                else:
                    id = try_id[0]
                his_reply = message.find_element_by_class_name('selectable-text')
                his_reply = his_reply.text
            if his_reply=="":
                his_reply == emoji
            if (browser.current_url == url):
                pass
            else:
                browser.close()
                chat()
            if id == your_number or id == your_name:
                continue
            else:
                pass
            browser.find_element_by_css_selector('body').send_keys(Keys.CONTROL + "\t")
            browser.switch_to.window(browser.window_handles[-1])
            if (browser.current_url == url2):
                pass
            else:
                browser.close()
                chat()
            bot_chat = browser.find_element_by_css_selector('#avatarform > input.stimulus')
            bot_chat.send_keys(his_reply)
            bot_chat.send_keys(Keys.ENTER)
            while True:
                try:
                    snip_icon = browser.find_element_by_css_selector('#snipTextIcon')
                    break
                except:
                    pass
            bot_reply =  browser.find_element_by_css_selector('#line1 > span.bot').text
            print(bot_reply)
            browser.find_element_by_css_selector('body').send_keys(Keys.CONTROL + "\t")
            browser.switch_to.window(browser.window_handles[0])
            if (browser.current_url == url):
                pass
            else:
                browser.close()
                chat()
            his_chat = browser.find_element_by_css_selector('#main > footer > div.block-compose > div.input-container > div > div.input')
            his_chat.send_keys(bot_reply)
            his_chat.send_keys(Keys.ENTER)
            if his_reply.lower() == "bye":
                break
        browser.close()
    except:
        browser.close()
        chat()
chat()
