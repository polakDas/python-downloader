from multiprocessing import Pool
import time
import os

def download(link):
    os.system(f"aria2c '{link}'")

links = []
n = int(input(">"))
for i in range(1, n+1):
    links.append(f'.....{i}..') # add link in fstring
                    
with Pool(n) as pool:
    print(pool.map(download, links))