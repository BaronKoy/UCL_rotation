#Grabs all RS IDs for a gene and pushes out a VEP input file
import json
import requests
#pyVEP is a potential module for python VEP but local install does not seem to be working at the moment
#from pyVEP import VEP

#Query entrez ID with Ensembl's API 'GET overlap/id/:id'
entrez = input('Enter entrez gene id:')
url = f'https://rest.ensembl.org/overlap/id/{entrez}?content-type=application/json;feature=gene;feature=variation'
rurl = requests.get(url)
outurl = rurl.json()
#Only use the line below should you wish to printout the gene name to the top of the VEP output file (though this then cannot be used as an input)
#print('Gene:', outurl[0]['external_name']) 
genename = outurl[0]['external_name']

# Parse API output for VEP input entries (chromsome, start, end, allele, strand, identifier) and create file for VEP input
with open('out.txt', 'w') as f:
    for x in outurl:
        if x['strand'] == 1:
            x['strand'] = '+'
        elif x['strand'] == -1:
            x['strand'] = '-'
        if x['id'].startswith('rs'):
            alle1 = (x['alleles'][0])
            alle2 = (x['alleles'][1])
            final_allele = alle1 + '/' + alle2
            print(x['seq_region_name'], x['start'], x['end'], final_allele, x['strand'], x['id'], sep='\t', file=f)
print(genename, 'vep output file created')
print('please run ./vep -i out.txt -o vep_output')

#VEP can also use variant identifier as an input (though this method is not recommended due to processing speed)
#The option below can be used if you want to use the identifier but keep in the mind the note from the line above
#print(x['id'])