import yaml
import pprint


lul={'name': 'test data product definition',
 'description':'This is a test product data definition for a program written by a turnip',
'metadata_type': 'eo',

'metadata':{'platform':{'code':'BoM'},'Instrument':{'name':'Rain Gauge'},'product_type':'rainfall','format':{'name':'NETCDF'}},

'storage':{'crs':'EPSG: 4326','resolution':{'longitude':'0.5','latitude': '-0.5'},'measurements':{'name':'temperature','dtype':'float32','units': 'C','nodata':'-999'}}}



pprint.pprint(lul)

with open('data.yml', 'w') as outfile:
    yaml.dump(lul, outfile, default_flow_style=False)