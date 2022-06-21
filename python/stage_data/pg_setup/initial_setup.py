import psycopg2

class db_setup():
    def __init__(self):

        self.DEFAULT_CXN = {'db': 'postgres',
                            'user': 'danfinkel',
                            'password': 'password',
                            'host': '127.0.0.1',
                            'port': '5432'
                           }

        self.CRIMEUSER_CXN = {'db': 'crime_project',
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
            print('sql executed')
        except Exception as e:
            print('sql did not execute')
            print(e)
            conn.close()

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
        run this second
        """

        sql = '''CREATE database {crime_project}'''.format(crime_project=CRIMEUSER_CXN['db'])
        submit_sql(DEFAULT_CXN,sql)

        sql = '''GRANT ALL PRIVILEGES ON DATABASE {crime_project} TO {user};'''.format(crime_project=CRIMEUSER_CXN['db'],
                                                                                       user=CRIMEUSER_CXN['user'])
        submit_sql(DEFAULT_CXN,sql)


    def create_schema(schema_name):
        """
        """

        sql = '''CREATE schema {schema_name}'''.format(schema_name=schema_name)
        submit_sql(CRIMEUSER_CXN, sql)


    def drop_db():
        """
        Be careful
        """

        sql = '''DROP database {crime_project} WITH (FORCE)'''.format(crime_project=CRIMEUSER_CXN['db'])
        submit_sql(DEFAULT_CXN,sql)

    def run():

        # first drop the db
        self.drop_db()

        # create the project db
        create_crimedb()

        # create the nibrs schema
        create_schema(schema_name='nibrs')
