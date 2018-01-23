import urllib.request

url = #Write the URL here
imagefile = "test.jpg"

urllib.request.urlretrieve(url, imagefile)

print("File saved")
