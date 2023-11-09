#Grabs all RS IDs that fall within a specific region
#Limited to a region of 5Mb per query
import json
import requests
#pyVEP is a potential module for python VEP but local install does not seem to be working at the moment
#from pyVEP import VEP

#Query entrez ID with Ensembl's API 'overlap/region/:species/:region'
region = input('Enter genomic region, e.g. 1:1-1000:')
url = f'https://rest.ensembl.org/overlap/region/human/{region}?feature=gene;feature=variation;content-type=application/json'
rurl = requests.get(url)
outurl = rurl.json()

with open('rsID_input_out.txt', 'w') as z:
    for y in outurl:
        if y['id'].startswith('rs'):
            rsid = y['id']
            print(rsid, file=z)
print('vep rs_ID identifier input file successfully created')
print('Run: vep -i rsID_input_out.txt -o vep_output.txt --cache ~/.vep/homo_sapiens')