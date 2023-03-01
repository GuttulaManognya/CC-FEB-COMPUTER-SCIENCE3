import pyshorteners
link=input("enter url\t")
short=pyshorteners.Shortener()
tiny=short.tinyurl.short(link)
print(tiny)
