#Extract all rs IDs within a given region and find matches in the HGDP dataset
#Output a final VCF with only matching SNPs
#This script assumes the chromosomal HGDP vcf file is within the curret working directory
#HGDP chromosome file can be changed on line 32
import requests
import json
import gzip

firstfile = open('all_ids.txt', 'w')
#output = open('output.json', 'w')
#Retrive all rs IDs within the provided genomic region
query = input('Enter genomic region, e.g. 1:1-1000:')
url = f'https://rest.ensembl.org/overlap/region/human/{query}?feature=gene;feature=variation;content-type=application/json'
rurl = requests.get(url)
ourl = rurl.json()
json1 = json.dumps(ourl, indent=4)
#Use line 7 & this line below to print out the default JSON output to an external file
#print(json1, file=output)
for object in json1:
    object = json.loads(json1)
for x in object:
    if x['id'].startswith('rs'):
        rsid1 = x['id']
        print(rsid1, file=firstfile)
        
finalfile = open('rsid_match.vcf', 'w')
print('##fileformat=VCFv4.2', file=finalfile)
print('HGDP01201', 'HGDP00479', 'HGDP01408', 'HGDP00471', 'HGDP01411', 'HGDP00937', 'HGDP01189', 'HGDP01094', 'HGDP00469', 'HGDP00475', 'HGDP01368', 'HGDP00473', 'HGDP01405', 'HGDP00470', 'HGDP00458', 'HGDP00904', 'HGDP01200', 'HGDP00452', 'HGDP00459', 'HGDP00914', 'HGDP00942', 'HGDP01031', 'HGDP00944', 'HGDP01406', 'HGDP01216', 'HGDP00907', 'HGDP01202', 'HGDP00908', 'HGDP00940', 'HGDP00911', 'HGDP00464', 'HGDP00929', 'HGDP00986', 'HGDP01244', 'HGDP00941', 'HGDP00934', 'HGDP00462', 'HGDP00453', 'HGDP00935', 'HGDP00943', 'HGDP01412', 'HGDP01243', 'HGDP01299', 'HGDP00845', 'HGDP00994', 'HGDP01283', 'HGDP00993', 'HGDP00918', 'HGDP00985', 'HGDP00910', 'HGDP00135', 'HGDP00214', 'HGDP00655', 'HGDP01096', 'HGDP00472', 'HGDP00450', 'HGDP00905', 'HGDP01298', 'HGDP00715', 'HGDP00711', 'HGDP00103', 'HGDP00359', 'HGDP00788', 'HGDP00136', 'HGDP00541', 'HGDP01285', 'HGDP00491', 'HGDP00105', 'HGDP00127', 'HGDP00547', 'HGDP00463', 'HGDP00703', 'HGDP00580', 'HGDP00130', 'HGDP00167', 'HGDP00576', 'HGDP01385', 'HGDP00662', 'HGDP00948', 'HGDP00005', 'HGDP00163', 'HGDP00346', 'HGDP00609', 'HGDP01257', 'HGDP00608', 'HGDP00544', 'HGDP00714', 'HGDP00057', 'HGDP00213', 'HGDP00165', 'HGDP01300', 'HGDP00931', 'HGDP00466', 'HGDP00279', 'HGDP00945', 'HGDP00056', 'HGDP01050', 'HGDP00288', 'HGDP00562', 'HGDP01396', 'HGDP01009', 'HGDP01383', 'HGDP00341', 'HGDP01013', 'HGDP00543', 'HGDP00947', 'HGDP00723', 'HGDP00467', 'HGDP00545', 'HGDP00610', 'HGDP00001', 'HGDP00218', 'HGDP00933', 'HGDP00856', 'HGDP00062', 'HGDP01086', 'HGDP00710', 'HGDP01192', 'HGDP00009', 'HGDP00924', 'HGDP00550', 'HGDP00920', 'HGDP01225', 'HGDP00925', 'HGDP00938', 'HGDP00478', 'HGDP00939', 'HGDP01256', 'HGDP00724', 'HGDP00726', 'HGDP00837', 'HGDP01190', 'HGDP00555', 'HGDP01029', 'HGDP00118', 'HGDP01081', 'HGDP01415', 'HGDP01418', 'HGDP01043', 'HGDP00843', 'HGDP01419', 'HGDP00992', 'HGDP00877', 'HGDP00781', 'HGDP00926', 'HGDP00782', 'HGDP01255', 'HGDP00460', 'HGDP01245', 'HGDP01037', 'HGDP00930', 'HGDP00820', 'HGDP01214', 'HGDP00319', 'HGDP01186', 'HGDP01310', 'HGDP00821', 'HGDP00777', 'HGDP00984', 'HGDP01327', 'HGDP01099', 'HGDP01416', 'HGDP00972', 'HGDP01313', 'HGDP00813', 'HGDP00814', 'HGDP00971', 'HGDP01296', 'HGDP01330', 'HGDP00812', 'HGDP01213', 'HGDP01340', 'HGDP00811', 'HGDP01033', 'HGDP01090', 'HGDP01021', 'HGDP01289', 'HGDP01023', 'HGDP00917', 'HGDP00776', 'HGDP00774', 'HGDP00815', 'HGDP00779', 'HGDP00818', 'HGDP00784', 'HGDP01318', 'HGDP01100', 'HGDP01290', 'HGDP00975', 'HGDP00974', 'HGDP01196', 'HGDP00786', 'HGDP01181', 'HGDP01354', 'HGDP01294', 'HGDP01352', 'HGDP01348', 'HGDP01322', 'HGDP00977', 'HGDP00780', 'HGDP01287', 'HGDP01292', 'HGDP00976', 'HGDP01224', 'HGDP01184', 'HGDP01334', 'HGDP01321', 'HGDP01101', 'HGDP01353', 'HGDP00817', 'HGDP01180', 'HGDP01195', 'HGDP01341', 'HGDP01319', 'HGDP01311', 'HGDP01193', 'HGDP01104', 'HGDP01187', 'HGDP01347', 'HGDP01197', 'HGDP01349', 'HGDP01351', 'HGDP01328', 'HGDP01295', 'HGDP01288', 'HGDP01329', 'HGDP00747', 'HGDP01293', 'HGDP00973', 'HGDP00762', 'HGDP01185', 'HGDP01331', 'HGDP01103', 'HGDP01317', 'HGDP01346', 'HGDP01342', 'HGDP01238', 'HGDP01326', 'HGDP01356', 'HGDP00958', 'HGDP01247', 'HGDP00766', 'HGDP01233', 'HGDP01207', 'HGDP01336', 'HGDP00819', 'HGDP00382', 'HGDP00946', 'HGDP01332', 'HGDP01337', 'HGDP01222', 'HGDP01291', 'HGDP01183', 'HGDP00822', 'HGDP00755', 'HGDP00966', 'HGDP01304', 'HGDP00716', 'HGDP01182', 'HGDP01230', 'HGDP00965', 'HGDP01194', 'HGDP00376', 'HGDP00364', 'HGDP00954', 'HGDP01234', 'HGDP00712', 'HGDP00962', 'HGDP00754', 'HGDP01232', 'HGDP01102', 'HGDP01204', 'HGDP00100', 'HGDP01303', 'HGDP01206', 'HGDP00772', 'HGDP00099', 'HGDP00371', 'HGDP00758', 'HGDP00765', 'HGDP00750', 'HGDP01229', 'HGDP01237', 'HGDP00756', 'HGDP00751', 'HGDP00828', 'HGDP00108', 'HGDP00115', 'HGDP00790', 'HGDP00109', 'HGDP00963', 'HGDP00356', 'HGDP00392', 'HGDP01221', 'HGDP00953', 'HGDP01209', 'HGDP00950', 'HGDP00719', 'HGDP00104', 'HGDP01249', 'HGDP01218', 'HGDP01251', 'HGDP00960', 'HGDP00964', 'HGDP00771', 'HGDP00957', 'HGDP00968', 'HGDP01220', 'HGDP01212', 'HGDP00761', 'HGDP01205', 'HGDP00351', 'HGDP00372', 'HGDP01241', 'HGDP00760', 'HGDP00961', 'HGDP00769', 'HGDP00757', 'HGDP00952', 'HGDP00721', 'HGDP00021', 'HGDP01231', 'HGDP00969', 'HGDP00039', 'HGDP00764', 'HGDP01305', 'HGDP00060', 'HGDP00035', 'HGDP00791', 'HGDP00234', 'HGDP01227', 'HGDP01236', 'HGDP00110', 'HGDP00173', 'HGDP00955', 'HGDP00106', 'HGDP00285', 'HGDP00047', 'HGDP00049', 'HGDP00031', 'HGDP00438', 'HGDP00199', 'HGDP00313', 'HGDP00066', 'HGDP00239', 'HGDP00013', 'HGDP00323', 'HGDP00070', 'HGDP00262', 'HGDP00224', 'HGDP00304', 'HGDP00098', 'HGDP00043', 'HGDP00181', 'HGDP00247', 'HGDP01361', 'HGDP00445', 'HGDP00423', 'HGDP00189', 'HGDP00243', 'HGDP00033', 'HGDP00011', 'HGDP00210', 'HGDP00082', 'HGDP00258', 'HGDP00315', 'HGDP00052', 'HGDP00074', 'HGDP00185', 'HGDP00072', 'HGDP00192', 'HGDP00244', 'HGDP00277', 'HGDP00412', 'HGDP00092', 'HGDP01358', 'HGDP00228', 'HGDP00264', 'HGDP00290', 'HGDP00330', 'HGDP00003', 'HGDP01359', 'HGDP00417', 'HGDP00025', 'HGDP00139', 'HGDP00536', 'HGDP00539', 'HGDP00205', 'HGDP00183', 'HGDP00402', 'HGDP00169', 'HGDP00080', 'HGDP00096', 'HGDP00015', 'HGDP00141', 'HGDP00879', 'HGDP00086', 'HGDP00298', 'HGDP00146', 'HGDP00251', 'HGDP00902', 'HGDP00150', 'HGDP00226', 'HGDP00309', 'HGDP00153', 'HGDP00519', 'HGDP00512', 'HGDP00088', 'HGDP00145', 'HGDP01357', 'HGDP00134', 'HGDP00137', 'HGDP00201', 'HGDP00880', 'HGDP00513', 'HGDP00900', 'HGDP00898', 'HGDP00527', 'HGDP01363', 'HGDP00524', 'HGDP00511', 'HGDP00154', 'HGDP01404', 'HGDP00143', 'HGDP01384', 'HGDP00899', 'HGDP00901', 'HGDP00177', 'HGDP00886', 'HGDP00078', 'HGDP01388', 'HGDP01360', 'HGDP00520', 'HGDP00149', 'HGDP00522', 'HGDP00535', 'HGDP00523', 'HGDP00518', 'HGDP00158', 'HGDP00094', 'HGDP00531', 'HGDP00537', 'HGDP00528', 'HGDP00151', 'HGDP00516', 'HGDP00895', 'HGDP00133', 'HGDP00891', 'HGDP00076', 'HGDP01362', 'HGDP00529', 'HGDP00883', 'HGDP00515', 'HGDP00140', 'HGDP00882', 'HGDP00538', 'HGDP01400', 'HGDP00148', 'HGDP00155', 'HGDP01398', 'HGDP00131', 'HGDP01382', 'HGDP00144', 'HGDP00884', 'HGDP01376', 'HGDP00889', 'HGDP01397', 'HGDP00896', 'HGDP01386', 'HGDP00525', 'HGDP00890', 'HGDP01403', 'HGDP00893', 'HGDP00897', 'HGDP00517', 'HGDP00799', 'HGDP00885', 'HGDP00161', 'HGDP00892', 'HGDP00888', 'HGDP01074', 'HGDP00881', 'HGDP00671', 'HGDP00514', 'HGDP01157', 'HGDP00894', 'HGDP01164', 'HGDP01156', 'HGDP00561', 'HGDP01073', 'HGDP00563', 'HGDP01399', 'HGDP00797', 'HGDP01375', 'HGDP01065', 'HGDP00572', 'HGDP00573', 'HGDP01066', 'HGDP00808', 'HGDP00583', 'HGDP01166', 'HGDP00807', 'HGDP01387', 'HGDP01367', 'HGDP00534', 'HGDP00670', 'HGDP00582', 'HGDP00579', 'HGDP00649', 'HGDP00651', 'HGDP00691', 'HGDP01071', 'HGDP00700', 'HGDP00590', 'HGDP00668', 'HGDP00632', 'HGDP00675', 'HGDP00803', 'HGDP00575', 'HGDP00794', 'HGDP01173', 'HGDP00565', 'HGDP00741', 'HGDP00674', 'HGDP01068', 'HGDP00646', 'HGDP00122', 'HGDP00248', 'HGDP00254', 'HGDP00179', 'HGDP00241', 'HGDP01075', 'HGDP00581', 'HGDP00045', 'HGDP00578', 'HGDP01366', 'HGDP01070', 'HGDP00868', 'HGDP00970', 'HGDP00631', 'HGDP00870', 'HGDP00546', 'HGDP00661', 'HGDP00682', 'HGDP00653', 'HGDP00129', 'HGDP00604', 'HGDP00684', 'HGDP00639', 'HGDP00620', 'HGDP00800', 'HGDP01171', 'HGDP01169', 'HGDP00802', 'HGDP00566', 'HGDP01149', 'HGDP00626', 'HGDP00102', 'HGDP00767', 'HGDP00326', 'HGDP00120', 'HGDP00175', 'HGDP00333', 'HGDP01155', 'HGDP00667', 'HGDP00863', 'HGDP00588', 'HGDP00556', 'HGDP00787', 'HGDP00858', 'HGDP01001', 'HGDP01161', 'HGDP01063', 'HGDP00912', 'HGDP00595', 'HGDP00621', 'HGDP00623', 'HGDP01269', 'HGDP00685', 'HGDP01067', 'HGDP01167', 'HGDP01069', 'HGDP00696', 'HGDP00687', 'HGDP00121', 'HGDP00388', 'HGDP01248', 'HGDP00698', 'HGDP00037', 'HGDP00307', 'HGDP00407', 'HGDP00259', 'HGDP00571', 'HGDP00873', 'HGDP00663', 'HGDP01041', 'HGDP00999', 'HGDP00704', 'HGDP01277', 'HGDP01152', 'HGDP00708', 'HGDP00869', 'HGDP00909', 'HGDP00641', 'HGDP00591', 'HGDP00643', 'HGDP00676', 'HGDP01369', 'HGDP00640', 'HGDP00810', 'HGDP00673', 'HGDP01379', 'HGDP00577', 'HGDP00686', 'HGDP00614', 'HGDP00732', 'HGDP01268', 'HGDP00054', 'HGDP00191', 'HGDP00311', 'HGDP00669', 'HGDP01072', 'HGDP01162', 'HGDP00995', 'HGDP00876', 'HGDP00854', 'HGDP00875', 'HGDP01056', 'HGDP00752', 'HGDP01058', 'HGDP00753', 'HGDP00832', 'HGDP00727', 'HGDP00679', 'HGDP00688', 'HGDP01260', 'HGDP00635', 'HGDP00672', 'HGDP01378', 'HGDP00557', 'HGDP00678', 'HGDP01254', 'HGDP01217', 'HGDP00638', 'HGDP00618', 'HGDP00949', 'HGDP00759', 'HGDP00230', 'HGDP00068', 'HGDP00029', 'HGDP00553', 'HGDP00615', 'HGDP01309', 'HGDP01060', 'HGDP00628', 'HGDP00859', 'HGDP01053', 'HGDP01027', 'HGDP00805', 'HGDP00872', 'HGDP00594', 'HGDP00624', 'HGDP00598', 'HGDP00647', 'HGDP00735', 'HGDP00699', 'HGDP00602', 'HGDP00586', 'HGDP00648', 'HGDP01239', 'HGDP00690', 'HGDP00017', 'HGDP01270', 'HGDP00444', 'HGDP00197', 'HGDP00560', 'HGDP01059', 'HGDP00849', 'HGDP01276', 'HGDP01262', 'HGDP00906', 'HGDP00625', 'HGDP01282', 'HGDP01373', 'HGDP00607', 'HGDP00683', 'HGDP00738', 'HGDP00739', 'HGDP00629', 'HGDP00746', 'HGDP00619', 'HGDP00636', 'HGDP00574', 'HGDP01370', 'HGDP01077', 'HGDP00587', 'HGDP00599', 'HGDP01174', 'HGDP00637', 'HGDP00677', 'HGDP00748', 'HGDP00171', 'HGDP00041', 'HGDP00023', 'HGDP01372', 'HGDP01151', 'HGDP00558', 'HGDP01275', 'HGDP00454', 'HGDP00860', 'HGDP00455', 'HGDP00549', 'HGDP00861', 'HGDP00551', 'HGDP00611', 'HGDP00730', 'HGDP00745', 'HGDP00564', 'HGDP01377', 'HGDP00666', 'HGDP00959', 'HGDP01271', 'HGDP00433', 'HGDP00397', 'HGDP00237', 'HGDP00806', 'HGDP01177', 'HGDP01302', 'HGDP00804', 'HGDP01019', 'HGDP01055', 'HGDP00729', 'HGDP01010', 'HGDP01014', 'HGDP00871', 'HGDP00862', 'HGDP00634', 'HGDP00693', 'HGDP00644', 'HGDP00613', 'HGDP00654', 'HGDP00734', 'HGDP00645', 'HGDP01267', 'HGDP00701', 'HGDP00733', 'HGDP00744', 'HGDP01208', 'HGDP00302', 'HGDP01380', 'HGDP00795', 'HGDP00913', 'HGDP01258', 'HGDP00864', 'HGDP01339', 'HGDP00568', 'HGDP01280', 'HGDP01261', 'HGDP00622', 'HGDP01264', 'HGDP00692', 'HGDP00736', 'HGDP00612', 'HGDP00740', 'HGDP00584', 'HGDP00600', 'HGDP00627', 'HGDP01374', 'HGDP00542', 'HGDP00559', 'HGDP00838', 'HGDP01301', 'HGDP00642', 'HGDP00694', 'HGDP01259', 'HGDP00187', 'HGDP00274', 'HGDP00281', 'HGDP01263', 'HGDP01057', 'HGDP00606', 'HGDP00601', 'HGDP00689', 'HGDP00697', 'HGDP00064', 'HGDP00222', 'HGDP00007', 'HGDP01062', 'HGDP00567', 'HGDP00967', 'HGDP00206', 'HGDP00865', 'HGDP00731', 'HGDP00664', 'HGDP01266', 'HGDP01265', 'HGDP00630', 'HGDP01064', 'HGDP01272', 'HGDP01279', 'HGDP00680', 'HGDP00521', 'HGDP01284', 'HGDP00456', 'HGDP00778', 'HGDP00927', 'HGDP00998', 'HGDP01307', 'HGDP00665', 'HGDP01079', 'HGDP01078', 'HGDP01323', 'HGDP00616', 'HGDP00725', 'HGDP01338', 'HGDP01333', 'HGDP00449', 'HGDP00476', 'HGDP00027', 'HGDP01345', 'HGDP00548', 'HGDP01402', 'HGDP00737', 'HGDP00232', 'HGDP01246', 'HGDP00773', 'HGDP00749', 'HGDP00597', 'HGDP01198', 'HGDP00058', 'HGDP00785', 'HGDP00903', 'HGDP00540', 'HGDP01098', 'HGDP00706', 'HGDP01253', 'HGDP00569', 'HGDP01240', 'HGDP01315', 'HGDP00160', 'HGDP01364', 'HGDP01032', 'HGDP01153', 'HGDP00932', 'HGDP01047', 'HGDP00338', 'HGDP00846', 'HGDP00991', 'HGDP00936', 'HGDP01274', 'HGDP01030', 'HGDP00660', 'HGDP00216', 'HGDP00656', 'HGDP01076', 'HGDP01286', 'HGDP01044', 'HGDP01242', 'HGDP01417', 'HGDP00956', 'HGDP01320', 'HGDP01179', 'HGDP00124', 'HGDP01034', 'HGDP01414', 'HGDP01308', 'HGDP00090', 'HGDP00195', 'HGDP01188', 'HGDP01250', 'HGDP00474', 'HGDP01199', 'HGDP01018', 'HGDP00650', 'HGDP00157', 'HGDP00286', 'HGDP01036', 'HGDP00526', 'HGDP00717', 'HGDP00783', 'HGDP01401', 'HGDP01365', 'HGDP00722', 'HGDP00887', 'HGDP01335', 'HGDP01306', 'HGDP00982', 'HGDP00987', 'HGDP00951', 'HGDP00713', 'HGDP00775', 'HGDP01172', 'HGDP00533', 'HGDP01163', 'HGDP01035', 'HGDP01215', 'HGDP00428', 'HGDP00552', 'HGDP01350', 'HGDP00855', 'HGDP01015', 'HGDP00852', 'HGDP01314', 'HGDP00702', 'HGDP00208', 'HGDP01095', 'HGDP01012', 'HGDP01223', 'HGDP01228', 'HGDP01168', 'HGDP00554', 'HGDP00125', 'HGDP01028', 'HGDP01297', 'HGDP01191', 'HGDP00328', 'HGDP00019', 'HGDP00461', 'HGDP01312', 'HGDP00915', 'HGDP00928', 'HGDP00530', 'HGDP00857', 'HGDP00457', 'HGDP01355', 'HGDP01211', 'HGDP00798', 'HGDP01203', 'HGDP00796', sep='\t', file=finalfile)
with open('all_ids.txt', 'r+') as first:
    for line in first:
        rsid2 = line
        with gzip.open('hgdp_wgs.20190516.full.chr17.vcf.gz', 'rb') as second:
            for line2 in second:
                line2 = line2.decode('utf-8')
                if rsid2 in line2:
                    print(line2, file=finalfile)