import pyshorteners

url = input("Enter the url: ")

def shorternur(url):
    s = pyshorteners.Shortener()
    print(f"Your short URL is: {s.tinyurl.short(url)}")


shorternur(url)

