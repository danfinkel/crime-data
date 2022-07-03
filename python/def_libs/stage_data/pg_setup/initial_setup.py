from util import default_cxn, crimeuser_cxn, submit_sql

class db_setup():
    def __init__(self):
        self.DEFAULT_CXN = default_cxn()
        self.CRIMEUSER_CXN = crimeuser_cxn()

    def create_crimeuser():
        """
        run this first
        """

        sql = '''CREATE role {crimeuser} LOGIN password '{password}' '''.format(crimeuser=CRIMEUSER_CXN['user'],
                                                                                password=CRIMEUSER_CXN['password']
                                                                               )
        submit_sql(self.DEFAULT_CXN,sql)

    def create_crimedb():
        """
        run this second
        """

        sql = '''CREATE database {crime_project}'''.format(crime_project=CRIMEUSER_CXN['db'])
        submit_sql(self.DEFAULT_CXN,sql)

        sql = '''GRANT ALL PRIVILEGES ON DATABASE {crime_project} TO {user};'''.format(crime_project=CRIMEUSER_CXN['db'],
                                                                                       user=CRIMEUSER_CXN['user'])
        submit_sql(self.DEFAULT_CXN,sql)

    def create_schema(schema_name):
        """
        """

        sql = '''CREATE schema {schema_name}'''.format(schema_name=schema_name)
        submit_sql(self.CRIMEUSER_CXN, sql)

    def drop_db():
        """
        Be careful
        """

        sql = '''DROP database {crime_project} WITH (FORCE)'''.format(crime_project=CRIMEUSER_CXN['db'])
        submit_sql(self.DEFAULT_CXN,sql)

    def run():

        # first drop the db
        self.drop_db()

        # create the project db
        create_crimedb()

        # create the nibrs schema
        create_schema(schema_name='nibrs')
