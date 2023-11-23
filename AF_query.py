#Query a region within the human genome (GRCh38) to return variant IDs, phenotypes, source, & allele frequencies across 1KG populations
#Limited to a region of 5Mb per query
import json
import requests
import re

#Endpoint for /phenotype/region/:species/:region - Return phenotype annotations that overlap a given genomic region.
region = input('Enter genomic region, e.g. 1:1-1000:')
url = f'https://rest.ensembl.org/phenotype/region/homo_sapiens/{region}?feature_type=Variation;content-type=application/json'
rurl = requests.get(url)
outurl = rurl.json()
#Endpoint for overlap/region/:species/:region - Retrieves features (e.g. genes, transcripts, variants and more) that overlap a given region.
gurl = f'https://rest.ensembl.org/overlap/region/human/{region}?feature=gene;content-type=application/json'
rgurl = requests.get(gurl)
gouturl = rgurl.json()

#Generate README file for details of output
info = open('README.txt', 'w')
print('Populations:', 'AFR = African', 'AMR = American', 'EAS = East Asian', 
      'EUR = European', 'SAS = South Asian', sep='\n', file=info)
print('', file=info)
print('Sub-populations:', 'ACB = African Caribbean in Barbados', 
      'ASW = African ancestry in Southwest US', 'ESN = Esan in Nigeria', 'GWD = Gambian in Western Division, The Gambia', 
      'LWK = Luhya in Webuye, Kenya', 'MSL = Mende in Sierra Leone', 'YRI = Yoruba in Ibadan, Nigeria', 
      'CLM = Colombian in Medellin, Colombia', 'MXL = Mexican Ancestry in Los Angeles, California',
      'PEL = Peruvian in Lima, Peru', 'PUR = Puerto Rican in Puerto Rico', 
      'CDX = Chinese Dai in Xishuangbanna, China', 'CHB = Han Chinese in Bejing, China', 
      'CHS = Southern Han Chinese, China', 'JPT = Japanese in Tokyo, Japan', 
      'KHV = Kinh in Ho Chi Minh City, Vietnam', 
      'CEU = Utah residents with Northern and Western European ancestry', 'FIN = Finnish in Finland', 
      'GBR = British in England and Scotland', 'IBS = Iberian populations in Spain', 
      'TSI = Toscani in Italy', 'BEB = Bengali in Bangladesh', 'GIH = Gujarati Indian in Houston, TX', 
      'ITU = Indian Telugu in the UK', 'PJL = Punjabi in Lahore,Pakistan', 
      'STU = Sri Lankan Tamil in the UK', sep='\n', file=info)

#Below can be used to gather data on all COSMIC IDs
"""#For all associated COSMIC IDs
with open('COSMIC_phenotypes.txt', 'w')as d:
   for cos in outurl:
      if cos['id'].startswith('COS'):
         cosid = cos['id']
         for a in cos['phenotype_associations']:
            cospheno = a['description']
            print('COSMIC_ID:', cosid, '/', 'Phenotype:', cospheno, file=d)"""

#Generate text file containing all variants found with phenotype association & source
phenofile = open('all_ids.txt', 'w')
print('Overlapping genes:', file=phenofile)
for y in gouturl:
   if 'external_name' in y:
      gene = y['external_name']
      start = y['start']
      end = y['end']
      print('Gene:', gene, start, '-', end, file=phenofile)
print('', file=phenofile)
#Use the line below for whole output
#print(outurl)

final = open('AF_output.txt', 'w')
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
            #Append all IDs found, phenotype, & source to the all IDs output file
            print(rsid, '/', phenor, '/', source, file=phenofile)
            #Below lines begin query for retriving populations AFs using RS IDs found in the above steps
            popurl = f'https://rest.ensembl.org/variation/human/{rsid}?content-type=application/json;pops=1'
            outpopurl = requests.get(popurl)
            routpopurl = outpopurl.json()
            json_object = json.dumps(routpopurl, indent=4)
            json1 = json.loads(json_object)
            for m in json1['mappings']:
               pos = str(m['start'])
               seq_region = m['seq_region_name']
               pos_done = ('Chr' + seq_region + ':' + pos)
               print('Position:', pos_done, '/', rsid, '/', phenor, file=final)
            popcheck = json1['populations']
            for p in popcheck:
                if p['population'].startswith('1000G'):
                  popul = p
                  popname = popul['population'].replace('1000GENOMES:phase_3:', '')
                  popfreq = popul['frequency']
                  popallele = popul['allele']
                  print(popname, popfreq, popallele, sep='\t', file=final)
print('Pipeline complete! Check file AF_output.txt')