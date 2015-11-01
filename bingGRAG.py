
from py_bing_search import PyBingSearch
import sys
import os

linkfile = sys.argv[-1]
linkfile = linkfile.replace("^", "|");
bing=PyBingSearch('MsYC/eW39AiaY9EYFIC8mlX8C7HPRRooagMKRwVZx7Q')
result_list, next_uri = bing.search(linkfile, limit=5, format='json')
#result_list, next_uri = bing.search("Python Software Foundation", limit=50, format='json')
result_list[0].description

file = open( 'bingResults.txt', 'w')
for res in result_list:
	file.write('"' + res.url + '" ')
	break
