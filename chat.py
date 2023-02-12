
from typing import KeysView
from selenium import webdriver
from time import sleep
import time

driver = webdriver.Chrome()

driver.get('https://login.microsoftonline.com/common/oauth2/v2.0/authorize?response_type=id_token&scope=openid%20profile&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=eyJpZCI6IjE2ODExYTFlLTAxYzAtNGYyOS1hYjc4LWYzOTRlZmUwOTQ2NiIsInRzIjoxNjMzNTE2OTMwLCJtZXRob2QiOiJyZWRpcmVjdEludGVyYWN0aW9uIn0%3D&nonce=74ed1ad1-6f2b-4f78-a4a4-50f78f3b8d8b&client_info=1&x-client-SKU=MSAL.JS&x-client-Ver=1.3.4&client-request-id=d738128f-18ce-42e4-b29c-d6d4e3dcd75e&response_mode=fragment')

time.sleep(2)

driver.find_element_by_id("i0116").send_keys("vikash.chand2020@vitstudent.ac.in")
time.sleep(2)
driver.find_element_by_id("idSIButton9").click()

time.sleep(2)









driver.find_element_by_id("i0118").send_keys("")
time.sleep(2)
driver.find_element_by_id("idSIButton9").click()


driver.find_element_by_id("idSIButton9").click()#yes button always remember

time.sleep(2)

driver.find_element_by_class_name("table-row").click()

time.sleep(12)
driver.find_element_by_id("searchInputField").send_keys("20mis0206")
'''driver.find_element_by_id("433a6dd3-e96a-4512-ac20-ce7f1041daac").click()'''


