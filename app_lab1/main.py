import psycopg2
from psycopg2.extras import execute_values
import pandas as pd
import warnings
import sys

warnings.filterwarnings("ignore")


def creete_tabels():
    try:
        cur.execute('''CREATE TABLE IF NOT EXISTS test_results (OUTID varchar not null primary key,
 BIRTH integer,
 SEXTYPENAME varchar,
 REGNAME varchar,
 AREANAME varchar,
 TERNAME varchar,
 REGTYPENAME varchar,
 TERTYPENAME varchar,
 CLASSPROFILENAME varchar,
 CLASSLANGNAME varchar,
 EONAME varchar,
 EOTYPENAME varchar,
 EOREGNAME varchar,
 EOAREANAME varchar,
 EOTERNAME varchar,
 EOPARENT varchar,
 UMLTEST varchar,
 UMLTESTSTATUS varchar,
 UMLBALL100 numeric,
 UMLBALL12 numeric,
 UMLBALL numeric,
 UMLADAPTSCALE numeric,
 UMLPTNAME varchar,
 UMLPTREGNAME varchar,
 UMLPTAREANAME varchar,
 UMLPTTERNAME varchar,
 UKRTEST varchar,
 UKRSUBTEST  varchar,
 UKRTESTSTATUS  varchar,
 UKRBALL100 numeric,
 UKRBALL12 numeric,
 UKRBALL numeric,
 UKRADAPTSCALE numeric,
 UKRPTNAME varchar,
 UKRPTREGNAME varchar,
 UKRPTAREANAME  varchar,
 UKRPTTERNAME varchar,
 HISTTEST varchar,
 HISTLANG varchar,
 HISTTESTSTATUS varchar,
 HISTBALL100 numeric,
 HISTBALL12 numeric,
 HISTBALL numeric,
 HISTPTNAME varchar,
 HISTPTREGNAME varchar,
 HISTPTAREANAME varchar,
 HISTPTTERNAME varchar,
 MATHTEST varchar,
 MATHLANG varchar,
 MATHTESTSTATUS varchar,
 MATHBALL100 numeric,
 MATHBALL12 numeric,
 MATHDPALEVEL varchar,
 MATHBALL numeric,
 MATHPTNAME varchar,
 MATHPTREGNAME varchar,
 MATHPTAREANAME varchar,
 MATHPTTERNAME varchar,
 MATHSTTEST varchar,
 MATHSTLANG  varchar,
 MATHSTTESTSTATUS varchar,
 MATHSTBALL12 numeric,
 MATHSTBALL numeric,
 MATHSTPTNAME varchar,
 MATHSTPTREGNAME varchar,
 MATHSTPTAREANAME varchar,
 MATHSTPTTERNAME varchar,
 PHYSTEST varchar,
 PHYSLANG varchar,
 PHYSTESTSTATUS varchar,
 PHYSBALL100 numeric,
 PHYSBALL12 numeric,
 PHYSBALL numeric,
 PHYSPTNAME varchar,
 PHYSPTREGNAME varchar,
 PHYSPTAREANAME varchar,
 PHYSPTTERNAME varchar,
 CHEMTEST varchar,
 CHEMLANG varchar,
 CHEMTESTSTATUS varchar,
 CHEMBALL100 numeric,
 CHEMBALL12 numeric,
 CHEMBALL numeric,
 CHEMPTNAME varchar,
 CHEMPTREGNAME varchar,
 CHEMPTAREANAME varchar,
 CHEMPTTERNAME varchar,
 BIOTEST varchar,
 BIOLANG varchar,
 BIOTESTSTATUS varchar,
 BIOBALL100 numeric,
 BIOBALL12 numeric,
 BIOBALL numeric,
 BIOPTNAME varchar,
 BIOPTREGNAME varchar,
 BIOPTAREANAME varchar,
 BIOPTTERNAME varchar,
 GEOTEST varchar,
 GEOLANG varchar,
 GEOTESTSTATUS varchar,
 GEOBALL100 numeric,
 GEOBALL12 numeric,
 GEOBALL numeric,
 GEOPTNAME  varchar,
 GEOPTREGNAME varchar,
 GEOPTAREANAME varchar,
 GEOPTTERNAME varchar,
 ENGTEST varchar,
 ENGTESTSTATUS varchar,
 ENGBALL100 numeric,
 ENGBALL12 numeric,
 ENGDPALEVEL varchar,
 ENGBALL numeric,
 ENGPTNAME varchar,
 ENGPTREGNAME varchar,
 ENGPTAREANAME varchar,
 ENGPTTERNAME varchar,
 FRATEST varchar,
 FRATESTSTATUS varchar,
 FRABALL100 numeric,
 FRABALL12 numeric,
 FRADPALEVEL varchar,
 FRABALL numeric,
 FRAPTNAME varchar,
 FRAPTREGNAME varchar,
 FRAPTAREANAME varchar,
 FRAPTTERNAME varchar,
 DEUTEST varchar,
 DEUTESTSTATUS varchar,
 DEUBALL100 numeric,
 DEUBALL12 numeric,
 DEUDPALEVEL varchar,
 DEUBALL numeric,
 DEUPTNAME varchar,
 DEUPTREGNAME varchar,
 DEUPTAREANAME varchar,
 DEUPTTERNAME varchar,
 SPATEST varchar,
 SPATESTSTATUS varchar,
 SPABALL100 numeric,
 SPABALL12 numeric,
 SPADPALEVEL varchar,
 SPABALL numeric,
 SPAPTNAME varchar,
 SPAPTREGNAME varchar,
 SPAPTAREANAME varchar,
 SPAPTTERNAME varchar,
 YEAR integer,
 STID varchar,
 RUSTEST varchar,
 RUSTESTSTATUS varchar,
 RUSBALL100 numeric,
 RUSBALL12 numeric,
 RUSPTNAME varchar,
 RUSPTREGNAME varchar,
 RUSPTAREANAME varchar,
 RUSPTTERNAME varchar,
 RUSPATNAME varchar,
 RUSPATREGNAME varchar,
 RUSPATAREANAME varchar,
 RUSPATTERNAME varchar);''')
    except:
        print("Table 'test' has already created")
    else:
        print("Table 'test' created")

    conn.commit() # <--- makes sure the change is shown in the database


    try:
        cur.execute('''CREATE TABLE IF NOT EXISTS log_table (log_id SERIAL  primary key,
        usr_name varchar NOT NULL,
        log_number integer NOT NULL,
        year integer NOT NULL,
        file_name varchar NOT NULL,
        datetime timestamp NOT NULL);''')
    except:
        print("Table 'log_table' has already created")
    else:
        print("Table 'log_table' created")

    conn.commit() # <--- makes sure the change is shown in the database

def load_dataset(file_name, encoding, year):
    '''
    This function load and processing datasets, refactor columns names  and missed values and 
    adding necessary information to DataFrames.  
    '''
    #loading data from file
    data = pd.read_csv('data/{}'.format(file_name), sep=';', decimal=',', encoding= encoding)

    #addind a column with year information
    data['YEAR'] = year
        
    #refactoring data columns, makeing the same register for all columns names
    data.columns = map(str.upper, data.columns)

    #in dataset that contains data about 2016 year same columns have invalide names
    #this code processing this data 
    if year == 2016:
        def re_func(x):
            x = x.replace('FR','FRA')
            x = x.replace('SP', 'SPA')
            x = x.replace('PHYSPAT', 'PHYSPT')
            return x
            
        data.columns = map(re_func, data.columns)
        
    #this code replase NaN on None in non-numeric columns 
    data = data.where((pd.notnull(data)), None)

    return data

def get_load_data_parameters():
    sql_query = '''select * from log_table
                   where log_id = (select max(log_id) from log_table)'''
    info_df = pd.read_sql_query(sql_query, conn)

    import_dict = pd.Series({'Odata2021File.csv': 'utf-8', 'Odata2020File.csv': 'Windows-1251', 
                'Odata2019File.csv': 'Windows-1251', 'OpenData2018.csv': 'utf-8',
                'OpenData2017.csv': 'utf-8', 'OpenData2016.csv': 'Windows-1251'})
    
    import_dict = pd.Series({'Odata2021File.csv': 'utf-8', 'Odata2020File.csv': 'Windows-1251'})


    if len(info_df) == 0:
        return (import_dict, 2021, 0)
    else:
        return(import_dict[info_df.file_name.values[0]:], info_df.year.values[0], info_df.log_number.values[0] + 1)


def save_problem_rows(row):
    with open("problemRows.txt", "a+") as file:
        file.write(' '.join(map(str, row)) + '\n')
        


def insert_data(df, column_names, n, year, file_name):

    try:
        for row in df.values:
            execute_values(cur, f'INSERT INTO test_results ({column_names}) values %s;', [tuple(row)])
                    
        cur.execute("INSERT INTO log_table(usr_name, log_number, year, file_name, datetime) values(user, {}, {}, '{}', LOCALTIMESTAMP(0))".format(n, year, file_name))
        conn.commit()
    except psycopg2.OperationalError:
    
        print('Connection error:  server closed the connection unexpectedly')

        create_connection()
        insert_data(df, column_names, n, year, file_name)

    except Exception as e:
        print(e)
        print('Row error')
        save_problem_rows(row)
        conn.rollback()
        df = df[df.OUTID != row[0]]
        insert_data(df, column_names, n, year, file_name)





def load_data():

    import_sets, year, n = get_load_data_parameters()

    for file_name, encoding in import_sets.items():

        data = load_dataset(file_name, encoding, year)
        column_names = ', '.join(data.columns.values)
        print('File {} loaded'.format(file_name))
        
        while True:
   
            df = data.iloc[n*100 : n*100 + 100]
            
            if len(df) <= 0:
                n = 0
                break

            insert_data(df, column_names, n, year, file_name)    
            del df
            n += 1
        
        del data
        year -= 1


def my_task():
    sql_query = '''select test_results.year, regname, MIN(physball100) as physball100 from test_results
                   where year in (2021, 2020) and physteststatus = 'Зараховано'
                   group by test_results.year , regname 
                   order by test_results.regname'''
    
    try:
        task_df = pd.read_sql_query(sql_query, conn)
    except:
        print('Sql query error: this error appeared in my_tusk function')
    else:    
        task_df.to_csv('task_result.csv', encoding='Windows-1251', index=False)


def save_result():

    sql_query = '''select count(*) from test_results'''
    sql_query_time = '''select datetime from log_table
                        where log_id in (1, (select max(log_id) from log_table))'''
    
    try:
        count = pd.read_sql_query(sql_query, conn).values[0][0]
        time_df = pd.read_sql_query(sql_query_time, conn)
        time = time_df.iloc[1] - time_df.iloc[0]
        time = time.astype(str)

        with open("time.txt", "w") as file:
            file.write('Time: '+ time.values[0] + '\n')
            file.write('Number of records in DB: {}'.format(str(count)))
    except:
        print('Sql query error: this error appeared in save_result function')
        

def create_connection():
    print('Waiting for connection...')
    while True:
        try:
            global conn, cur
            conn = psycopg2.connect(database = "postgres", user = "Admin", password = "example", host = "db", port = "5432")
            cur = conn.cursor()
            break
        except:
           pass

create_connection()

creete_tabels()
load_data()
my_task()
save_result()

cur.close()
conn.close()