import yaml
import pprint


product_def={'name': 'test data product definition',
 'description':'This is a test product data definition',
'metadata_type': 'eo',

'metadata':{'platform':{'code':'TST01'},'Instrument':{'name':'Rain Gauge'},'product_type':'rainfall','format':{'name':'NETCDF'}},

'storage':{'crs':'spatial projection','resolution':{'longitude':'0.5','latitude': '-0.5'},

'measurements':{'name':'temperature','dtype':'float32','units': 'cm','nodata':'-999'}}}



pprint.pprint(product_def)

with open('product_definition_example.yml', 'w') as outfile:
    yaml.dump(product_def, outfile, default_flow_style=False)