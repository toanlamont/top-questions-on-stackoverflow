import requests
from bs4 import BeautifulSoup
import sys

results = []
r = requests.get("http://ketqua1.net")
tree = BeautifulSoup(markup=r.text, features="html.parser")
nodes = tree.find_all(name="td", attrs={"class": "chu17"})

for node in nodes:
    results.append(node.text)
if len(sys.argv) == 1:
    for result in results:
        print(result)
else:
    for number in sys.argv[1:]:

        if number in results:
            print("{} trung lo".format(number))
        else:
            print("{} KHONG trung lo".format(number))