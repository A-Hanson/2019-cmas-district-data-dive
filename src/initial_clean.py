import psycopg2
from pipeline import Pipeline

if __name__ == '__main__':
    conn = psycopg2.connect(dbname='school_and_district', user='postgres', 
                            host='localhost', port='5435')

    pipeline = Pipeline(conn)

    pipeline.execute()
    pipeline.close()