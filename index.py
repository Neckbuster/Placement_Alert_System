import requests
from bs4 import BeautifulSoup

from mailsender import sendMail

cookies = { 
# Add Cookies
}

headers = { 
#Add Headers
}

data = { 
# Add Data
}
s = requests.Session()
s.post('https://collegeplacements.com/wp-login.php', headers=headers, cookies=cookies, data=data)

import threading
head = 'ram ji ki sena'
###CAll this with Interval
def myFunc():
  global head
  threading.Timer(5.0, myFunc).start()
  response = s.get('https://collegeplacements.com/news/')
  if(response.status_code==200):
    soup = BeautifulSoup(response.content, features="lxml")
    elm = soup.select_one('#post-8445 > header > h1 > a')
    if(elm.get_text()==head):
      pass
    else:
      head = elm.get_text()
      print(type(head))
      sendMail(head.encode('ascii','ignore').decode('ascii'))
  else:
    print('Not working Properly')
    

myFunc()