#Based on "Learning the Python 3 Standard Library" by Learning the Python 3 Standard Library
#I was watching this course on Lynda.com to refresh my Python3 knowledge and this was the most interesting part. It's mind-blowingly simple to use a Google API to get books' data based on the ISBN

import urllib.request
import json
import textwrap

ISBN=input("Give me an ISBN number (example: 9780007477159): ")

with urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q=isbn:"+str(ISBN)) as f:
    text = f.read()
    decodedtext = text.decode('utf-8')

obj = json.loads(decodedtext)

print(obj['items'][0]['volumeInfo']['title'])
