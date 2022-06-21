from def_libs.stage_data.nibrs.write_nibrs_to_pg import nibrs_pg

nibrs_admin = nibrs_pg(fpath='/Users/danfinkel/data/nibrs/raw/118281-V5/nibrs_1991_2020_administrative_segment_dta',
                       table_name='admin_arrests'
                      )

nibrs_admin.build_table()
