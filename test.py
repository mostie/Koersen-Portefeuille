import sys

print (sys.version)

a=3
b=3
print(a+b)
for i in range(5):
    print(i)
    i=i+1
browser.get("https://www.evernote.com/Login.action")
time.sleep(10)
username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")
username.send_keys("peter.mostmans@telenet.be")
password.send_keys("T5p4gnAjFYN#ykW")
login_attempt = browser.find_element_by_xpath("//*[@type='Continue']")
login_attempt.submit()
