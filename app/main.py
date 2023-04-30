import psycopg2
from psycopg2.extras import execute_values
import pandas as pd
import warnings

warnings.filterwarnings("ignore")


def creete_tabels():

    try:
        cur.execute("CREATE SCHEMA IF NOT EXISTS newschema;")
    except Exception as e:
        print("Table 'newschema' has already created")
    else:
        print("Table 'newschema' created")

    conn.commit() # <--- makes sure the change is shown in the database


    try:
         cur.execute('''CREATE TABLE IF NOT EXISTS newschema.eo (
        EONAME varchar not null primary key,
        EOTYPENAME varchar,
        EOREGNAME varchar,
        EOAREANAME varchar,
        EOTERNAME varchar,
        EOPARENT varchar);''')
    except:
        print("Table 'eo' has already created")
    else:
        print("Table 'eo' created")

    conn.commit() # <--- makes sure the change is shown in the database


    try:
         cur.execute('''CREATE TABLE IF NOT EXISTS newschema.reg_info (
        REGNAME varchar,
        AREANAME varchar NOT NULL,
        TERNAME varchar NOT NULL,
        TERTYPENAME varchar,
        constraint pk_test primary key (AREANAME, TERNAME));''')
    except:
        print("Table 'reg_info' has already created")
    else:
        print("Table 'reg_info' created")

    conn.commit() # <--- makes sure the change is shown in the database


    try:
         cur.execute('''CREATE TABLE IF NOT EXISTS newschema.student_info (OUTID varchar not null primary key,
        BIRTH integer,
        SEXTYPENAME varchar,
        AREANAME varchar,
        TERNAME varchar,
        REGTYPENAME varchar,
        CLASSPROFILENAME varchar,
        CLASSLANGNAME varchar,
        EONAME varchar,
        YEAR integer,
        CONSTRAINT reg_info_cons FOREIGN KEY (AREANAME, TERNAME) REFERENCES newschema.reg_info(AREANAME, TERNAME) ON DELETE CASCADE,
        CONSTRAINT eo_info_cons FOREIGN KEY (EONAME) REFERENCES newschema.eo(EONAME) ON DELETE CASCADE);''')
    except:
        print("Table 'student_info' has already created")
    else:
        print("Table 'student_info' created")

    conn.commit() # <--- makes sure the change is shown in the database

    try:
        cur.execute('''CREATE TABLE IF NOT EXISTS newschema.locations (PTNAME varchar not null primary key,
        PTREGNAME varchar,
        PTAREANAME varchar,
        PTTERNAME varchar);''')
    except Exception as e:
        print("Table 'locations' has already created")
    else:
        print("Table 'locations' created")

    conn.commit() # <--- makes sure the change is shown in the database



    try:
         cur.execute('''CREATE TABLE IF NOT EXISTS newschema.uml (OUTID varchar not null primary key,
        UMLTEST varchar,
        UMLTESTSTATUS varchar,
        UMLBALL100 numeric,
        UMLBALL12 numeric,
        UMLBALL numeric,
        UMLADAPTSCALE numeric,
        UMLPTNAME varchar,
        CONSTRAINT student_info FOREIGN KEY (OUTID) REFERENCES newschema.student_info(OUTID) ON DELETE CASCADE,
        CONSTRAINT location_cons FOREIGN KEY (UMLPTNAME) REFERENCES newschema.locations(PTNAME) ON DELETE CASCADE);''')
    except Exception as e:
        print("Table 'uml' has already created")
    else:
        print("Table 'uml' created")

    conn.commit() # <--- makes sure the change is shown in the database
        

    try:
         cur.execute('''CREATE TABLE IF NOT EXISTS newschema.ukr (OUTID varchar not null primary key,
        UKRTEST varchar,
        UKRSUBTEST  varchar,
        UKRTESTSTATUS  varchar,
        UKRBALL100 numeric,
        UKRBALL12 numeric,
        UKRBALL numeric,
        UKRADAPTSCALE numeric,
        UKRPTNAME varchar,
        CONSTRAINT student_info FOREIGN KEY (OUTID) REFERENCES newschema.student_info(OUTID) ON DELETE CASCADE,
        CONSTRAINT location_cons FOREIGN KEY (UKRPTNAME) REFERENCES newschema.locations(PTNAME) ON DELETE CASCADE);''')
    except Exception as e:
        print("Table 'ukr' has already created")
    else:
        print("Table 'ukr' created")

    conn.commit() # <--- makes sure the change is shown in the database

    try:
         cur.execute('''CREATE TABLE IF NOT EXISTS newschema.hist (OUTID varchar not null primary key,
        HISTTEST varchar,
        HISTLANG varchar,
        HISTTESTSTATUS varchar,
        HISTBALL100 numeric,
        HISTBALL12 numeric,
        HISTBALL numeric,
        HISTPTNAME varchar,
        CONSTRAINT student_info FOREIGN KEY (OUTID) REFERENCES newschema.student_info(OUTID) ON DELETE CASCADE,
        CONSTRAINT location_cons FOREIGN KEY (HISTPTNAME) REFERENCES newschema.locations(PTNAME) ON DELETE CASCADE);''')
    except Exception as e:
        print("Table 'hist' has already created")
    else:
        print("Table 'hist' created")

    conn.commit() # <--- makes sure the change is shown in the database


    try:
         cur.execute('''CREATE TABLE IF NOT EXISTS newschema.math (OUTID varchar not null primary key,
        MATHTEST varchar,
        MATHLANG varchar,
        MATHTESTSTATUS varchar,
        MATHBALL100 numeric,
        MATHBALL12 numeric,
        MATHDPALEVEL varchar,
        MATHBALL numeric,
        MATHPTNAME varchar,
        CONSTRAINT student_info FOREIGN KEY (OUTID) REFERENCES newschema.student_info(OUTID) ON DELETE CASCADE,
        CONSTRAINT location_cons FOREIGN KEY (MATHPTNAME) REFERENCES newschema.locations(PTNAME) ON DELETE CASCADE);''')
    except Exception as e:
        print("Table 'math' has already created")
    else:
        print("Table 'math' created")

    conn.commit() # <--- makes sure the change is shown in the database

    
    try:
         cur.execute('''CREATE TABLE IF NOT EXISTS newschema.mathst (OUTID varchar not null primary key,
        MATHSTTEST varchar,
        MATHSTLANG  varchar,
        MATHSTTESTSTATUS varchar,
        MATHSTBALL12 numeric,
        MATHSTBALL numeric,
        MATHSTPTNAME varchar,
        CONSTRAINT student_info FOREIGN KEY (OUTID) REFERENCES newschema.student_info(OUTID) ON DELETE CASCADE,
        CONSTRAINT location_cons FOREIGN KEY (MATHSTPTNAME) REFERENCES newschema.locations(PTNAME) ON DELETE CASCADE);''')
    except Exception as e:
        print("Table 'mathst' has already created")
    else:
        print("Table 'mathst' created")

    conn.commit() # <--- makes sure the change is shown in the database

    
    try:
         cur.execute('''CREATE TABLE IF NOT EXISTS newschema.phys (OUTID varchar not null primary key,
        PHYSTEST varchar,
        PHYSLANG varchar,
        PHYSTESTSTATUS varchar,
        PHYSBALL100 numeric,
        PHYSBALL12 numeric,
        PHYSBALL numeric,
        PHYSPTNAME varchar,
        CONSTRAINT student_info FOREIGN KEY (OUTID) REFERENCES newschema.student_info(OUTID) ON DELETE CASCADE,
        CONSTRAINT location_cons FOREIGN KEY (PHYSPTNAME) REFERENCES newschema.locations(PTNAME) ON DELETE CASCADE);''')
    except Exception as e:
        print("Table 'phys' has already created")
    else:
        print("Table 'phys' created")

    conn.commit() # <--- makes sure the change is shown in the database


    try:
         cur.execute('''CREATE TABLE IF NOT EXISTS newschema.chem (OUTID varchar not null primary key,
        CHEMTEST varchar,
        CHEMLANG varchar,
        CHEMTESTSTATUS varchar,
        CHEMBALL100 numeric,
        CHEMBALL12 numeric,
        CHEMBALL numeric,
        CHEMPTNAME varchar,
        CONSTRAINT student_info FOREIGN KEY (OUTID) REFERENCES newschema.student_info(OUTID) ON DELETE CASCADE,
        CONSTRAINT location_cons FOREIGN KEY (CHEMPTNAME) REFERENCES newschema.locations(PTNAME) ON DELETE CASCADE);''')
    except Exception as e:
        print("Table 'chem' has already created")
    else:
        print("Table 'chem' created")

    conn.commit() # <--- makes sure the change is shown in the database


    try:
         cur.execute('''CREATE TABLE IF NOT EXISTS newschema.bio (OUTID varchar not null primary key,
        BIOTEST varchar,
        BIOLANG varchar,
        BIOTESTSTATUS varchar,
        BIOBALL100 numeric,
        BIOBALL12 numeric,
        BIOBALL numeric,
        BIOPTNAME varchar,
        CONSTRAINT student_info FOREIGN KEY (OUTID) REFERENCES newschema.student_info(OUTID) ON DELETE CASCADE,
        CONSTRAINT location_cons FOREIGN KEY (BIOPTNAME) REFERENCES newschema.locations(PTNAME) ON DELETE CASCADE);''')
    except Exception as e:
        print("Table 'bio' has already created")
    else:
        print("Table 'bio' created")

    conn.commit() # <--- makes sure the change is shown in the database

    try:
         cur.execute('''CREATE TABLE IF NOT EXISTS newschema.geo (OUTID varchar not null primary key,
        GEOTEST varchar,
        GEOLANG varchar,
        GEOTESTSTATUS varchar,
        GEOBALL100 numeric,
        GEOBALL12 numeric,
        GEOBALL numeric,
        GEOPTNAME varchar,
        CONSTRAINT student_info FOREIGN KEY (OUTID) REFERENCES newschema.student_info(OUTID) ON DELETE CASCADE,
        CONSTRAINT location_cons FOREIGN KEY (GEOPTNAME) REFERENCES newschema.locations(PTNAME) ON DELETE CASCADE);''')
    except Exception as e:
        print("Table 'geo' has already created")
    else:
        print("Table 'geo' created")

    conn.commit() # <--- makes sure the change is shown in the database


    try:
         cur.execute('''CREATE TABLE IF NOT EXISTS newschema.eng (OUTID varchar not null primary key,
        ENGTEST varchar,
        ENGTESTSTATUS varchar,
        ENGBALL100 numeric,
        ENGBALL12 numeric,
        ENGDPALEVEL varchar,
        ENGBALL numeric,
        ENGPTNAME varchar,
        CONSTRAINT student_info FOREIGN KEY (OUTID) REFERENCES newschema.student_info(OUTID) ON DELETE CASCADE,
        CONSTRAINT location_cons FOREIGN KEY (ENGPTNAME) REFERENCES newschema.locations(PTNAME) ON DELETE CASCADE);''')
    except Exception as e:
        print("Table 'eng' has already created")
    else:
        print("Table 'eng' created")

    conn.commit() # <--- makes sure the change is shown in the database


    try:
         cur.execute('''CREATE TABLE IF NOT EXISTS newschema.fra (OUTID varchar not null primary key,
        FRATEST varchar,
        FRATESTSTATUS varchar,
        FRABALL100 numeric,
        FRABALL12 numeric,
        FRADPALEVEL varchar,
        FRABALL numeric,
        FRAPTNAME varchar,
        CONSTRAINT student_info FOREIGN KEY (OUTID) REFERENCES newschema.student_info(OUTID) ON DELETE CASCADE,
        CONSTRAINT location_cons FOREIGN KEY (FRAPTNAME) REFERENCES newschema.locations(PTNAME) ON DELETE CASCADE);''')
    except Exception as e:
        print("Table 'fra' has already created")
    else:
        print("Table 'fra' created")

    conn.commit() # <--- makes sure the change is shown in the database


    try:
         cur.execute('''CREATE TABLE IF NOT EXISTS newschema.deu (OUTID varchar not null primary key,
        DEUTEST varchar,
        DEUTESTSTATUS varchar,
        DEUBALL100 numeric,
        DEUBALL12 numeric,
        DEUDPALEVEL varchar,
        DEUBALL numeric,
        DEUPTNAME varchar,
        CONSTRAINT student_info FOREIGN KEY (OUTID) REFERENCES newschema.student_info(OUTID) ON DELETE CASCADE,
        CONSTRAINT location_cons FOREIGN KEY (DEUPTNAME) REFERENCES newschema.locations(PTNAME) ON DELETE CASCADE);''')
    except Exception as e:
        print("Table 'deu' has already created")
    else:
        print("Table 'deu' created")

    conn.commit() # <--- makes sure the change is shown in the database

    try:
         cur.execute('''CREATE TABLE IF NOT EXISTS newschema.spa (OUTID varchar not null primary key,
        SPATEST varchar,
        SPATESTSTATUS varchar,
        SPABALL100 numeric,
        SPABALL12 numeric,
        SPADPALEVEL varchar,
        SPABALL numeric,
        SPAPTNAME varchar,
        CONSTRAINT student_info FOREIGN KEY (OUTID) REFERENCES newschema.student_info(OUTID) ON DELETE CASCADE,
        CONSTRAINT location_cons FOREIGN KEY (SPAPTNAME) REFERENCES newschema.locations(PTNAME) ON DELETE CASCADE);''')
    except Exception as e:
        print("Table 'spa' has already created")
    else:
        print("Table 'spa' created")

    conn.commit() # <--- makes sure the change is shown in the database


    try:
        cur.execute('''CREATE TABLE IF NOT EXISTS newschema.log_table (log_id SERIAL  primary key,
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
    sql_query = '''select * from newschema.log_table
                   where log_id = (select max(log_id) from newschema.log_table)'''
    info_df = pd.read_sql_query(sql_query, conn)

    import_dict = pd.Series({'Odata2021File.csv': 'utf-8', 'Odata2020File.csv': 'Windows-1251', 
                'Odata2019File.csv': 'Windows-1251', 'OpenData2018.csv': 'utf-8',
                'OpenData2017.csv': 'utf-8', 'OpenData2016.csv': 'Windows-1251'})
    
    import_dict = pd.Series({'Odata2021File.csv': 'utf-8',
                              'Odata2020File.csv': 'Windows-1251'})


    if len(info_df) == 0:
        return (import_dict, 2021, 0)
    else:
        return(import_dict[info_df.file_name.values[0]:], info_df.year.values[0], info_df.log_number.values[0] + 1)


def save_problem_rows(row):
    with open("problemRows.txt", "a+") as file:
        file.write(' '.join(map(str, row)) + '\n')
        


def insert_data(df, column_names, n, year, file_name):
    
    location_list = []
    user = df.loc[:,['OUTID', 'BIRTH', 'SEXTYPENAME', 'AREANAME', 'TERNAME', 'REGTYPENAME', 'CLASSPROFILENAME', 'CLASSLANGNAME', 'EONAME', 'YEAR']]
    user['EONAME'] = df.loc[:,['EONAME']]
    eo = df.loc[:, 'EONAME':'EOPARENT'].drop_duplicates()
    reg_info = df.loc[:, ['REGNAME', 'AREANAME', 'TERNAME', 'TERTYPENAME']].drop_duplicates()
    if year == 2021:
        uml = df.loc[:, 'UMLTEST': 'UMLPTNAME'] 
        uml['OUTID'] = df['OUTID']
        location_list.append(df.loc[:, 'UMLPTNAME': 'UMLPTTERNAME'] )

        mathst = df.loc[:, 'MATHSTTEST': 'MATHSTPTNAME']
        mathst['OUTID'] = df['OUTID']
        location_list.append(df.loc[:, 'MATHSTPTNAME': 'MATHSTPTTERNAME'] )
    
    ukr = df.loc[:, 'UKRTEST': 'UKRPTNAME']
    ukr['OUTID'] = df['OUTID']
    location_list.append(df.loc[:, 'UKRPTNAME': 'UKRPTTERNAME'] )

    hist = df.loc[:, 'HISTTEST': 'HISTPTNAME']
    hist['OUTID'] = df['OUTID']
    location_list.append(df.loc[:, 'HISTPTNAME': 'HISTPTTERNAME'] )

    math = df.loc[:, 'MATHTEST': 'MATHPTNAME']
    math['OUTID'] = df['OUTID']
    location_list.append(df.loc[:, 'MATHPTNAME': 'MATHPTTERNAME'] )

    phys = df.loc[:, 'PHYSTEST': 'PHYSPTNAME']
    phys['OUTID'] = df['OUTID']
    location_list.append(df.loc[:, 'PHYSPTNAME': 'PHYSPTTERNAME'] )

    chem = df.loc[:, 'CHEMTEST': 'CHEMPTNAME']
    chem['OUTID'] = df['OUTID']
    location_list.append(df.loc[:, 'CHEMPTNAME': 'CHEMPTTERNAME'] )

    bio = df.loc[:, 'BIOTEST': 'BIOPTNAME']
    bio['OUTID'] = df['OUTID']
    location_list.append(df.loc[:, 'BIOPTNAME': 'BIOPTTERNAME'] )

    geo = df.loc[:, 'GEOTEST': 'GEOPTNAME']
    geo['OUTID'] = df['OUTID']
    location_list.append(df.loc[:, 'GEOPTNAME': 'GEOPTTERNAME'] )

    eng = df.loc[:, 'ENGTEST': 'ENGPTNAME']
    eng['OUTID'] = df['OUTID']
    location_list.append(df.loc[:, 'ENGPTNAME': 'ENGPTTERNAME'] )

    fra = df.loc[:, 'FRATEST': 'FRAPTNAME']
    fra['OUTID'] = df['OUTID']
    location_list.append(df.loc[:, 'FRAPTNAME': 'FRAPTTERNAME'] )

    deu = df.loc[:, 'DEUTEST': 'DEUPTNAME']
    deu['OUTID'] = df['OUTID']
    location_list.append(df.loc[:, 'DEUPTNAME': 'DEUPTTERNAME'] )

    spa = df.loc[:, 'SPATEST': 'SPAPTNAME']
    spa['OUTID'] = df['OUTID']
    location_list.append(df.loc[:, 'SPAPTNAME': 'SPAPTTERNAME'] )
    
    

    try:
        for row in eo.values:
            if row[0] != None:
                try:
                    cur.execute("SAVEPOINT my_savepoint")
                    execute_values(cur, f'INSERT INTO newschema.eo ({", ".join(eo.columns.values)}) values %s;', [tuple(row)])
                    cur.execute("RELEASE my_savepoint")
                except:
                    cur.execute("ROLLBACK TO my_savepoint")
        for row in reg_info.values:
            if row[1] != None:
                try:
                    cur.execute("SAVEPOINT my_savepoint")
                    execute_values(cur, f'INSERT INTO newschema.reg_info ({", ".join(reg_info.columns.values)}) values %s;', [tuple(row)])
                    cur.execute("RELEASE my_savepoint")
                except:
                    cur.execute("ROLLBACK TO my_savepoint")
        for userrow in user.values:
            execute_values(cur, f'INSERT INTO newschema.student_info ({", ".join(user.columns.values)}) values %s;', [tuple(userrow)])

        for location in location_list:
            for row in location.values:
                if row[0] != None:
                    try:
                        cur.execute("SAVEPOINT my_savepoint")
                        execute_values(cur, f'INSERT INTO newschema.locations values %s;', [tuple(row)])
                        cur.execute("RELEASE my_savepoint")
                    except:
                        cur.execute("ROLLBACK TO my_savepoint")

        if year == 2021:
            for row in uml.values:
                if row[0] != None:
                    execute_values(cur, f'INSERT INTO newschema.uml ({", ".join(uml.columns.values)}) values %s;', [tuple(row)])

            for row in mathst.values:
                if row[0] != None:
                    execute_values(cur, f'INSERT INTO newschema.mathst ({", ".join(mathst.columns.values)}) values %s;', [tuple(row)])
        
        for row in ukr.values:
            if row[0] != None:
                execute_values(cur, f'INSERT INTO newschema.ukr ({", ".join(ukr.columns.values)}) values %s;', [tuple(row)])

        for row in hist.values:
            if row[0] != None:
                execute_values(cur, f'INSERT INTO newschema.hist ({", ".join(hist.columns.values)}) values %s;', [tuple(row)])
        
        for row in math.values:
            if row[0] != None:
                execute_values(cur, f'INSERT INTO newschema.math ({", ".join(math.columns.values)}) values %s;', [tuple(row)])
        
        for row in phys.values:
            if row[0] != None:
                execute_values(cur, f'INSERT INTO newschema.phys ({", ".join(phys.columns.values)}) values %s;', [tuple(row)])
        
        for row in chem.values:
            if row[0] != None:
                execute_values(cur, f'INSERT INTO newschema.chem ({", ".join(chem.columns.values)}) values %s;', [tuple(row)])
        
        for row in bio.values:
            if row[0] != None:
                execute_values(cur, f'INSERT INTO newschema.bio ({", ".join(bio.columns.values)}) values %s;', [tuple(row)])

        for row in geo.values:
            if row[0] != None:
                execute_values(cur, f'INSERT INTO newschema.geo ({", ".join(geo.columns.values)}) values %s;', [tuple(row)])\
                
        for row in eng.values:
            if row[0] != None:
                execute_values(cur, f'INSERT INTO newschema.eng ({", ".join(eng.columns.values)}) values %s;', [tuple(row)])

        for row in deu.values:
            if row[0] != None:
                execute_values(cur, f'INSERT INTO newschema.deu ({", ".join(deu.columns.values)}) values %s;', [tuple(row)])

        for row in spa.values:
            if row[0] != None:
                execute_values(cur, f'INSERT INTO newschema.spa ({", ".join(spa.columns.values)}) values %s;', [tuple(row)])
    


                    
        cur.execute("INSERT INTO newschema.log_table(usr_name, log_number, year, file_name, datetime) values(user, {}, {}, '{}', LOCALTIMESTAMP(0))".format(n, year, file_name))
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
    sql_query = '''select newschema.student_info.year, newschema.reg_info.regname, MIN(newschema.phys.physball100) as physball100 from (newschema.student_info inner join newschema.reg_info ON reg_info.areaname = student_info.areaname) inner join newschema.phys using(outid) 
                   where newschema.student_info.year in (2021, 2020) and newschema.phys.physteststatus = 'Зараховано'
                   group by newschema.student_info.year , newschema.reg_info.regname 
                   order by newschema.reg_info.regname'''
    
    try:
        task_df = pd.read_sql_query(sql_query, conn)
    except:
        print('Sql query error: this error appeared in my_tusk function')
    else:    
        task_df.to_csv('task_result.csv', encoding='Windows-1251', index=False)


def save_result():

    sql_query = '''select count(*) from newschema.student_info'''
    sql_query_time = '''select datetime from newschema.log_table
                        where newschema.log_table.log_id in (1, (select max(newschema.log_table.log_id) from newschema.log_table))'''
    
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
           print('--')
           pass

create_connection()

creete_tabels()
load_data()
my_task()
save_result()

cur.close()
conn.close()