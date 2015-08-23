# pubmed_abstract_counter
Script to count number of abtracts for given query

Example:
<code bash>
python pubmed_abstract_counter.py infile.txt > outfile.txt
</code>

Out file consists of the original query followed by a tab and than the count of abstracts matching that query.

Note: In 

<code bash>
def main():
</code>

you can add your email to: 

<code bash>
Entrez.email = ""
</code>

Requirements:

python 2.7
Biopython
