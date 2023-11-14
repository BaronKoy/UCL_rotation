#Grabs all RS IDs that fall within a specific region & provides phenotype & source
#Limited to a region of 5Mb per query
import json
import requests
import re
#pyVEP is a potential module for python VEP but local install does not seem to be working at the moment
#from pyVEP import VEP

#Query entrez ID with Ensembl's API 'overlap/region/:species/:region'
region = input('Enter genomic region, e.g. 1:1-1000:')
url = f'https://rest.ensembl.org/phenotype/region/homo_sapiens/{region}?feature_type=Variation;content-type=application/json'
rurl = requests.get(url)
outurl = rurl.json()
gurl = f'https://rest.ensembl.org/overlap/region/human/{region}?feature=gene;content-type=application/json'
rgurl = requests.get(gurl)
gouturl = rgurl.json()

#Append overlapping genes to the beginning of the output file
print('Overlapping gene(s):')
for y in gouturl:
   if 'external_name' in y:
      gene = y['external_name']
      start = y['start']
      end = y['end']
      print('Gene:', gene, start, '-', end)
#Use the line below for whole output
#print(outurl)

#Output phenotype associated RS_IDs, phenotype, & source
with open('all_rsid.txt', 'w') as f:
   for x in outurl:
      if x['id'].startswith('rs'):
         rsid = x['id']
         for z in x['phenotype_associations']:
            pheno = z['description']
            if pheno == 'ClinVar: phenotype not specified':
               phenow = pheno
            else:
               phenor = pheno
               source = z['source']
               print(rsid, phenor, source, sep='\t', file=f)
               print(rsid, phenor, source, sep='\t')

#Initial API query output check
print('Filtering by GWAS & non-GWAS hits.....')

#Below can be used to gather data on all COSMIC IDs
"""#For all associated COSMIC IDs
with open('COSMIC_phenotypes.txt', 'w')as d:
   for cos in outurl:
      if cos['id'].startswith('COS'):
         cosid = cos['id']
         for a in cos['phenotype_associations']:
            cospheno = a['description']
            print('COSMIC_ID:', cosid, '/', 'Phenotype:', cospheno, file=d)"""


#Separate GWAS & non-GWAS IDs into different files
#GWAS hits will be used with the GWAS catalog API, while non-GWAS hits continue with Ensembl API
with open('all_rsid.txt') as output:
   final = open('AF_output.json', 'w')
   for clin_id in output:
      if 'NHGRI-EBI GWAS catalog' in clin_id:
         GWAS = clin_id
         GWAS_clean = GWAS.strip('\n')
         #print(GWAS_clean)
      if 'NHGRI-EBI GWAS catalog' not in clin_id:
         non_GWAS = clin_id
         clean = clin_id.split()
         rsentry = clean[0]
         popurl = f'https://rest.ensembl.org/variation/human/{rsentry}?content-type=application/json;pops=1'
         outpopurl = requests.get(popurl)
         routpopurl = outpopurl.json()
         json_object = json.dumps(routpopurl, indent=4)
         print(json_object, file=final)
         
print('Popluation stats retrived - file: AF_output.json')
print('Parsing JSON AF data.....')