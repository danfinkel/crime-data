def default_cxn():
    return {'db': 'postgres',
            'user': 'danfinkel',
            'password': 'password',
            'host': '127.0.0.1',
            'port': '5432'}


def crimeuser_cxn():
    return {'db': 'crime_project',
            'user': 'crimeuser',
            'password': 'password',
            'host': '127.0.0.1',
            'port': '5432'}


def conn_string():
    cxn = crimeuser_cxn()
    return 'postgresql://{user}:{password}@{host}/{db}'.format(db=cxn['db'],
                                                      user=cxn['user'],
                                                      password=cxn['password'],
                                                      host=cxn['host'])
