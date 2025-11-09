import requests
import selectorlib
from datetime import datetime
import sqlite3

URL = "http://programmer100.pythonanywhere.com"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url):
    response = requests.get(url, HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("temp.yaml")
    value = extractor.extract(source)["temp"]
    return value

connect = sqlite3.connect (r"C:\Users\ADMIN\PycharmProjects\PythonProject10\Temperature.db")
cursor = connect.cursor()



scraped = scrape(URL)
extracted = extract(scraped)
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
cursor.execute ("INSERT INTO Temperatures VALUES (?,?)" , (timestamp, extracted))
connect.commit()
#with open("temp.txt", "a") as f:
    #f.write(f"{timestamp} - {extracted}\n")

print (extracted)