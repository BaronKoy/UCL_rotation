#Grabs all RS IDs that fall within a specific region
#Limited to a region of 5Mb per query
import json
import requests
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

with open('RSID_phenotypes.json', 'w') as f:
   for y in gouturl:
      if 'external_name' in y:
         gene = y['external_name']
         start = y['start']
         end = y['end']
         print('Overlapping gene(s):', gene, start,'-', end, file=f)
#Use the line below for whole output
#print(outurl)

#For all associated RS IDs
with open('RSID_phenotypes.json', 'a') as f:
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
               print('RS_ID:', rsid, '/', 'Phenotype:', phenor, '/', 'Source:', source, file=f)

#For all associated COSMIC IDs
with open('COSMIC_phenotypes.json', 'w')as d:
   for cos in outurl:
      if cos['id'].startswith('COS'):
         cosid = cos['id']
         for a in cos['phenotype_associations']:
            cospheno = a['description']
            print('COSMIC_ID:', cosid, '/', 'Phenotype:', cospheno, file=d)
