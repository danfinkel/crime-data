import psycopg2

DEFAULT_CXN = {'db': 'postgres',
               'user': 'danfinkel',
               'password': 'password',
               'host': '127.0.0.1',
               'port': '5432'
              }

CRIMEUSER_CXN = {'db': 'crime_project',
                 'user': 'crimeuser',
                 'password': 'password',
                 'host': '127.0.0.1',
                 'port': '5432'
              }


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
    except:
        print('sql did not execute')
        conn.close()

    print('sql executed')
    conn.close()


def create_crimeuser():
    """
    run this first
    """

    sql = '''CREATE role {crimeuser} LOGIN password '{password}' '''.format(crimeuser=CRIMEUSER_CXN['user'],
                                                                            password=CRIMEUSER_CXN['password']
                                                                           )
    submit_sql(DEFAULT_CXN,sql)


def create_crimedb():
    """
    """

    sql = '''CREATE database {crime_project}'''.format(crime_project=CRIMEUSER_CXN['db'])
    submit_sql(DEFAULT_CXN,sql)
