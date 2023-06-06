from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests

link_1 = "https://www.ebay.com/itm/325629485391?hash=item4bd107a14f:g:5wAAAOSwvapkRY8T&amdata=enc%3AAQAIAAAAwMbbeV9DJSZsbNxez48F16bFhioZp7ylwZIYP29bZVYpzPN1hxepXvsae5i49hmyXQkItJK9JSHtcu%2Fy%2B4tOQbsSZn43wpgIA%2F%2BgZV020kZJzjSLdSSWInEc82dbVj2kSyYbCy2jUkF09sMZz%2FcF7sw74u3IWBaiNKdcjCQJjL0xusPcl680WrazvY7Wjn2M2cVlKp46vFhR7PkQmqWjrOnNCXW15zQDHfPWql0r3YlxiwGI3NUs8iPdECmM80rHlg%3D%3D%7Ctkp%3ABk9SR4L1yMv2YQ"
link_2 = "https://www.amazon.de/-/en/GeForce-Gaming-Graphics-DisplayPort-DUAL-RTX3060-O12G-V2/dp/B096658ZWP/ref=sr_1_2?crid=3CFC68BIQBBWX&keywords=gpu&qid=1682364085&sprefix=gpu%2Caps%2C91&sr=8-2&th=1"


link_5 = "https://www.amazon.com/ASUS-Graphics-DisplayPort-Military-Grade-Certification/dp/B0985VND1G/ref=sr_1_3?crid=3QUMNYPLCHZGZ&keywords=gpu&qid=1682360533&sprefix=gpu%2Caps%2C150&sr=8-3&th=1"


link = [link_1]
for i in link:
    req = Request(i, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    
    with requests.Session() as c:
        soup = BeautifulSoup(webpage, 'html5lib')
        price = soup.find('span',attrs={'itemprop':'price'})['content']
        print(price)

#update the fucking website links if you want this to run
