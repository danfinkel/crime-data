# move nibrs data from raw into postgres

# Nibrs Data Citation
# Kaplan, Jacob.
# Jacob Kaplan’s Concatenated Files: National Incident-Based Reporting System (NIBRS) Data,
# 1991-2020. Ann Arbor,
# MI: Inter-university Consortium for Political and Social Research [distributor],
# 2022-05-09. https://doi.org/10.3886/E118281V5
# see: https://www.openicpsr.org/openicpsr/project/118281/version/V5/view?path=/openicpsr/118281/fcr:versions/V5&type=project

import pandas as pd
import os

class nibrs_raw():
    def __init__(self, fpath):
        self.fpath = fpath

    def get_stata_files():
        return [f for f in os.listdir(self.fpath) if 'dta' in f]

    def
