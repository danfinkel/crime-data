# move nibrs data from raw into postgres

# Nibrs Data Citation
# 2010: https://www.icpsr.umich.edu/web/NACJD/studies/33601
# 2011: https://www.icpsr.umich.edu/web/NACJD/studies/34603


import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import os

from def_libs.stage_data.pg_setup.util import conn_string, submit_sql, crimeuser_cxn
from def_libs.stage_data.pg_setup.constants import INCIDENT_COLS

class nibrs_pg():
    def __init__(self, fpath, table_name, overwrite_table):
        """
            fpath : path to the files (reads everyting in folder)
            table_name : table where data is headed
            overwrite_table : T/F to overwrite or append table
        """
        self.fpath = fpath
        self.table_name = table_name
        self.overwrite_table = overwrite_table

        self.conn_string = conn_string()

    def get_stata_files(self):
        return [f for f in os.listdir(self.fpath) if 'dta' in f]

    def write_to_pg(self, df):
        db = create_engine(self.conn_string)
        conn = db.connect()

        df.to_sql(self.table_name,
                            con=conn,
                            schema='nibrs',
                            if_exists='append',
                            index=False)

    def read_stata_files(self, fname):
        return pd.read_stata(fname)

    def drop_table(self):
        sql = '''DROP TABLE nibrs.{table_name};'''.format(table_name=self.table_name)
        submit_sql(crimeuser_cxn(), sql)

    def prune_frame(self, df):

        # prune and rename columns
        cols = [c[0] for c in INCIDENT_COLS]
        df_out = df[cols]
        df_out.columns = [c[2] for c in INCIDENT_COLS]

        return df[cols]

    def build_table(self):

        if self.overwrite_table:
            self.drop_table()

        stata_files = self.get_stata_files()

        for fname in stata_files:
            print("starting file: {fname}".format(fname=fname))
            df = self.read_stata_files(self.fpath + '/' + fname)
            df = self.prune_frame(df)
            self.write_to_pg(df)
