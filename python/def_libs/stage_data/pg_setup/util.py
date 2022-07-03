import psycopg2

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
def submit_sql(cxn, sql):
    """
    one off sql execution via psycopg2
    """

    conn = psycopg2.connect(
                 database= cxn['db'],
                 user= cxn['user'],
                 password= cxn['password'],
                 host= cxn['host'],
                 port= cxn['port']
            )
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    try:
        cursor.execute(sql)
        print('sql executed')
    except Exception as e:
        print('sql did not execute')
        print(e)
        conn.close()

    conn.close()
