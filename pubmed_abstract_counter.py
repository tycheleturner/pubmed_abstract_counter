#! /usr/bin/env python

import re #regular expression tool
import sys
from Bio import Entrez
from Bio import Medline

try:
       fname = sys.argv[1]
except:
       sys.stderr.write("Usage: pubmedAbstractCount.py <infile> > <outfile>\n")
       sys.exit(1)

class QueryReader(object):
    def __init__(self, filename):
        self.fh = file(filename, 'r')
    def __iter__(self):
        return self
    def next(self):
        while True:
            line = self.fh.readline()
            if line == "":
                self.fh.close()
                raise StopIteration
            line = line[:-1]
            return line
    
def main():

    Entrez.email = ""

    for query in QueryReader(fname):
        query = query.strip()
                #Get all the pubmed entries matching my query
        handle = Entrez.egquery(term=query)
        record = Entrez.read(handle)
        for row in record["eGQueryResult"]:
            if row["DbName"]=="pubmed":
                count = row["Count"]
                print '\t'.join([query, count])


if __name__ == "__main__":
    main()
