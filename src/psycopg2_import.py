import psycopg2
from pipeline import Pipeline

if __name__ == '__main__':
    conn = psycopg2.connect(dbname='school_and_district', password='mirabel', user='postgres',
                            host='localhost', port='5432')

    pipeline = Pipeline(conn)

    pipeline.add_step('''
                    COPY school_and_district
                    FROM '../data/school_and_district.csv'
                    DELIMITER ','
                    CSV HEADER;
                    ''')
    pipeline.add_step('''
                        SELECT *
                        FROM school_and_district
                        LIMIT 10;
                        ''')

    pipeline.execute()
    pipeline.close()