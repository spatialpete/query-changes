#! python3
# queries a term, returns result as text file
# if file exists, compares to previous results
# if there is a new result, send an email

import requests, sys, webbrowser, bs4, os.path

queryTerm = 'AMD Ryzen'

res = requests.get('http://google.com/search?q=' + queryTerm)
res.raise_for_status()

# return results as text
soup = bs4.BeautifulSoup(res.text, "html.parser")

# select results
linkElems = soup.select('.r a')
print(linkElems[1])
print(len(linkElems))

# write results to text file
#outFile = open('E:/Python/SearchResults.txt', 'w')
#for i in linkElems:
    #outFile.write(str(i) + '\n')
#outFile.close()

# todo: if outFile already exists, compare new file to old file
# this will need to be moved above the write results to text file part
compareList = []
if os.path.exists('E:/Python/SearchResults.txt'):
    oldFile = open('E:/Python/SearchResults.txt', 'r')
    oldFileList = oldFile.readlines()
    print(oldFileList[1])
    for newItem in linkElems:
        #for oldItem in oldFileList:
        if newItem in oldFileList:
            compareList.append(newItem)
            print('new search result found')
            print("1: " + str(oldItem) + '\n 2: ' + str(newItem))
else:
    outFile = open('E:/Python/SearchResults.txt', 'w')
    for i in linkElems:
        outFile.write(str(i) + '\n')
    outFile.close()

# todo: email any changes
