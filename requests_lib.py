import requests
'''
Relative libraries requests and urllib.requests
to parse the response:
json, lxml, BeautifulSoup, Slenium for html
'''
response=requests.get('https://en.wikipedia.org/wiki/main_page')
response.encoding='ISO-8859-1' # this will clean up the html code 

html_text= str(response.text)
#print(html_text.find('Did you know'))

# to decode into unicode
#print(response.content.decode('utf-8')) # to decode from byte to html txt

'''using json library'''
import json
data_string='[{"a":"A", "b":"B", "c":3.0, "d":[1,2]}]'

data_list=json.loads(data_string)
print(data_list[0]['a'])