#Grabs all variants that fall within a specific region & returns the chromosomal coordinates
#Limited to a region of 5Mb per query
import json
import requests

#Query entrez ID with Ensembl's API 'overlap/region/:species/:region'
region = input('Enter genomic region, e.g. 1:1-1000:')
url = f'https://rest.ensembl.org/overlap/region/human/{region}?feature=gene;feature=variation;content-type=application/json'
rurl = requests.get(url); outurl = rurl.json()

final = open('variants.txt', 'w')
for x in outurl:
      if x['id'].startswith('rs'):
        chrom = x['seq_region_name']; start = x['start']; locat = ('chr' + chrom)
        print(locat, start, sep='\t', file=final)
print('Run complete! Check variants.txt')