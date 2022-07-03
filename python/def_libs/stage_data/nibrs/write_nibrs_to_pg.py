# move nibrs data from raw into postgres

# Nibrs Data Citation
# Kaplan, Jacob.
# Jacob Kaplan’s Concatenated Files: National Incident-Based Reporting System (NIBRS) Data,
# 1991-2020. Ann Arbor,
# MI: Inter-university Consortium for Political and Social Research [distributor],
# 2022-05-09. https://doi.org/10.3886/E118281V5
# see: https://www.openicpsr.org/openicpsr/project/118281/version/V5/view?path=/openicpsr/118281/fcr:versions/V5&type=project

import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import os

from def_libs.stage_data.pg_setup.util import conn_string, submit_sql, crimeuser_cxn
from def_libs.stage_data.pg_setup.constants import DB_COLS

class nibrs_pg():
    def __init__(self, fpath, table_name):
        self.fpath = fpath
        self.table_name = table_name

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
        cols = [c[0] for c in DB_COLS]
        return df[cols]

    def build_table(self):

        self.drop_table()

        stata_files = self.get_stata_files()

        for fname in stata_files:
            print("starting file: {fname}".format(fname=fname))
            df = self.read_stata_files(self.fpath + '/' + fname)
            df = self.prune_frame(df)
            self.write_to_pg(df)
