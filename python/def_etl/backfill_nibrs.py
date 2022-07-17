from def_libs.stage_data.nibrs.write_nibrs_to_pg import nibrs_pg

build_incidents2010 = True
if build_incidents2010:
    nibrs_incidents = nibrs_pg(fpath='/Users/danfinkel/data/nibrs/raw/nibrs_download/ICPSR_33601/DS0001',
                               table_name='incidents',
                               overwrite_table = True
                          )

    nibrs_incidents.build_table()
