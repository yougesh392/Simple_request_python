import requests
from bs4 import BeautifulSoup

def price_check(p):
    if p<6000:
        print("Good Buy it")
    else: 
        print("Naaah")



request = requests.get("https://w11stop.com/stock-clearance/raspberry-pi-3-model-b")
#returns a html page
content = request.content

soup = BeautifulSoup(content,"html.parser")

elemet = soup.find("div",{"class":"product-price"})
#<div class="product-price">Rs6,800/-</div>

#strip to return only string
price = elemet.text.strip()#Rs6,800/

#parsing so only numbers get extracted
numbers = ""
for word in price:
   if word.isdigit():
      numbers = numbers + word

print_int = int(numbers)

price_check(print_int)
