import yaml
import pprint


metadata_def={'id': 'unique id string',
              'creation_dt':'yyyy-mm-dd:HH:MM',
              'product_type': 'eo',
              'platform':{'code': 'SRTM'},
              'instrument':{'name':'SIR'},
              'format':{'name':'ENVI'},
              'extent':{'coord':{'ll':{'lat':{'-44'},'lon':{'44'}},
                                 'lr':{'lat':{'-44'},'lon':{'44'}},
                                 'ul':{'lat':{'-44'},'lon':{'44'}},
                                 'ur':{'lat':{'-44'},'lon':{'44'}}},
                        'from_dt':{'yyyy-mm-dd:HH:MM'},
                        'center_dt':{'yyyy-mm-dd:HH:MM'},
                        'to_dt':{'yyyy-mm-dd:HH:MM'}},
              'grid_spatial':{'projection':{'geo_ref_points':{'ll':{'lat':{'-44'},'lon':{'44'}},
                                                              'lr':{'lat':{'-44'},'lon':{'44'}},
                                                              'ul':{'lat':{'-44'},'lon':{'44'}},
                                                              'ur':{'lat':{'-44'},'lon':{'44'}}}},
                              'spatial_reference':{'GEOGCS["GCS_WGS_1984",DATUM["WGS_1984",SPHEROID["WGS_84",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["degree",0.0174532925199433],AUTHORITY["EPSG","4326"]]'}},
              'image':{'bands':{'elevation':{'path':{'/foo/bar/example.tiff'}}}},
              'lineage':{'source_datasets':{'NaN'}}
              }

pprint.pprint(metadata_def)

with open('product_definition_example.yml', 'w') as outfile:
    yaml.dump(product_def, outfile, default_flow_style=False)