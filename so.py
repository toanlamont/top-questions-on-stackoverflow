import sys
import requests
from bs4 import BeautifulSoup

N = int(sys.argv[1])
label = sys.argv[2]
r = requests.get(
    "https://stackoverflow.com/questions/tagged/"
    "{}?sort=MostVotes&edited=true".format(label)
)
tree = BeautifulSoup(markup=r.text, features="html.parser")
nodes = tree.find_all(name="a", attrs={"class": "s-link"})
for node in nodes:
    if N == 0:
        break
    if (node.text).isspace() is False:
        print(node.text, "https://stackoverflow.com" + node.attrs["href"])
        N -= 1