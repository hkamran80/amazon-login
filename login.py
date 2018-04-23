from getpass import getpass
import webbrowser
import requests
import os


amazon_username = raw_input("Amazon email: ")
amazon_password = getpass()

headers = {
	"User-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
	"action": "sign-in",
	"email": amazon_username,
	"password": amazon_password
	}

r = requests.get("https://www.amazon.com/gp/sign-in.html", headers=headers)
print(r.status_code)

r = requests.get("https://www.amazon.com/gp/flex/sign-in/select.html", headers=headers)
print(r.status_code)

r = requests.get("https://www.amazon.com/", headers=headers)
print(r.status_code)
