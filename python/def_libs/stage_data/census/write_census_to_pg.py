import pandas as pd
import requests

from util import build_api_census_query, get_census_varnameframe, get_census_data
from def_libs.stage_data.pg_setup.constants import CENSUS_VARS


def get_census_frame(year, state):

    # get the census variables
    df_vars = get_census_varnameframe(year)

    # grab census codes
    var_names =[]
    for k in CENSUS_VARS.keys():
        concept = CENSUS_VARS[k]['concept']
        label = CENSUS_VARS[k]['label']
        query_str = """concept == '{concept}' and label = '{label}'""".format(concept=concept,
                                                                              label=label
                                                                             )
        var_names.append(df_vars.query(query_str).index[0])

    # construct url for census api query
    url = build_api_census_query(year, var_names, state)

    return get_census_data(url)
