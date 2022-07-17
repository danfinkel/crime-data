# Convenient online links
# variables can be found
# https://api.census.gov/data/2010/acs/acs5/variables.html
# (replace year with your year)

import pandas as pd

# constants
CENSUS_API_KEY = '7b9018f85cb787c75cbb14e626f20c8484a38f1c'
CENSUS_BASE = 'https://api.census.gov/data/'

def build_api_census_query(year, columns, state):

    url = CENSUS_BASE + str(year) + '/acs/acs5?get=NAME,'

    url += ','.join(columns)
    url += '&for=county%20subdivision:*'
    url += '&in=state:{state}'.format(state=state)
    url += '&key={api_key}'.format(api_key=CENSUS_API_KEY)

    return url

def get_census_varnameframe(year):

    url = CENSUS_BASE + str(year) + '/acs/acs5/variables.json'
    r = re.get(url)

    df = pd.DataFrame.from_dict(r.json()['variables'])

    return df.transpose()

def get_census_data(url):

    r = r.get(url)
    return pd.DataFrame(r.json())


# https://api.census.gov/data/2020/acs/acs5?get=NAME,B01001_001E&for=county%20subdivision:*&in=state:25&key=7b9018f85cb787c75cbb14e626f20c8484a38f1c
# https://api.census.gov/data/2020/acs/acs5?get=NAME,B01001_001E&for=county%20subdivision:*&in=state:30&key=7b9018f85cb787c75cbb14e626f20c8484a38f1c
