#! python3
# queries a term, returns result as text file
# if file exists, compares to previous results
# if there is a new result, send an email

import requests, sys, webbrowser, bs4, os.path

queryTerm = 'AMD Ryzen'

res = requests.get('http://google.com/search?q=' + queryTerm)
res.raise_for_status()

# return results as text
soup = bs4.BeautifulSoup(res.text)

# select results
linkElems = soup.select('.r a')
print(linkElems[1])
print(len(linkElems))

# write results to text file
outFile = open('E:/Python/SearchResults.txt', 'w')
for i in linkElems:
    outFile.write(str(i) + '\n')
outFile.close()

# todo: if outFile already exists, compare new file to old file
# this will need to be moved above the write results to text file part
if os.path.exists('E:/Python/SearchResults.txt'):
    oldFileList = outFile.readlines()
    print oldFileList

# todo: email any changes
