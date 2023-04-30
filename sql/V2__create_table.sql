CREATE TABLE IF NOT EXISTS eo (
        EONAME varchar not null primary key,
        EOTYPENAME varchar,
        EOREGNAME varchar,
        EOAREANAME varchar,
        EOTERNAME varchar,
        EOPARENT varchar);

CREATE TABLE IF NOT EXISTS reg_info (
        REGNAME varchar,
        AREANAME varchar NOT NULL,
        TERNAME varchar NOT NULL,
        TERTYPENAME varchar,
        constraint pk_test primary key (AREANAME, TERNAME));


CREATE TABLE IF NOT EXISTS student_info (OUTID varchar not null primary key,
        BIRTH integer,
        SEXTYPENAME varchar,
        AREANAME varchar,
        TERNAME varchar,
        REGTYPENAME varchar,
        CLASSPROFILENAME varchar,
        CLASSLANGNAME varchar,
        EONAME varchar,
        YEAR integer,
        CONSTRAINT reg_info_cons FOREIGN KEY (AREANAME, TERNAME) REFERENCES reg_info(AREANAME, TERNAME) ON DELETE CASCADE,
        CONSTRAINT eo_info_cons FOREIGN KEY (EONAME) REFERENCES eo(EONAME) ON DELETE CASCADE);


CREATE TABLE IF NOT EXISTS locations (PTNAME varchar not null primary key,
        PTREGNAME varchar,
        PTAREANAME varchar,
        PTTERNAME varchar);


CREATE TABLE IF NOT EXISTS uml (OUTID varchar not null primary key,
        UMLTEST varchar,
        UMLTESTSTATUS varchar,
        UMLBALL100 numeric,
        UMLBALL12 numeric,
        UMLBALL numeric,
        UMLADAPTSCALE numeric,
        UMLPTNAME varchar,
        CONSTRAINT student_info FOREIGN KEY (OUTID) REFERENCES student_info(OUTID) ON DELETE CASCADE,
        CONSTRAINT location_cons FOREIGN KEY (UMLPTNAME) REFERENCES locations(PTNAME) ON DELETE CASCADE);


CREATE TABLE IF NOT EXISTS ukr (OUTID varchar not null primary key,
        UKRTEST varchar,
        UKRSUBTEST  varchar,
        UKRTESTSTATUS  varchar,
        UKRBALL100 numeric,
        UKRBALL12 numeric,
        UKRBALL numeric,
        UKRADAPTSCALE numeric,
        UKRPTNAME varchar,
        CONSTRAINT student_info FOREIGN KEY (OUTID) REFERENCES student_info(OUTID) ON DELETE CASCADE,
        CONSTRAINT location_cons FOREIGN KEY (UKRPTNAME) REFERENCES locations(PTNAME) ON DELETE CASCADE);

CREATE TABLE IF NOT EXISTS hist (OUTID varchar not null primary key,
        HISTTEST varchar,
        HISTLANG varchar,
        HISTTESTSTATUS varchar,
        HISTBALL100 numeric,
        HISTBALL12 numeric,
        HISTBALL numeric,
        HISTPTNAME varchar,
        CONSTRAINT student_info FOREIGN KEY (OUTID) REFERENCES student_info(OUTID) ON DELETE CASCADE,
        CONSTRAINT location_cons FOREIGN KEY (HISTPTNAME) REFERENCES locations(PTNAME) ON DELETE CASCADE);


CREATE TABLE IF NOT EXISTS math (OUTID varchar not null primary key,
        MATHTEST varchar,
        MATHLANG varchar,
        MATHTESTSTATUS varchar,
        MATHBALL100 numeric,
        MATHBALL12 numeric,
        MATHDPALEVEL varchar,
        MATHBALL numeric,
        MATHPTNAME varchar,
        CONSTRAINT student_info FOREIGN KEY (OUTID) REFERENCES student_info(OUTID) ON DELETE CASCADE,
        CONSTRAINT location_cons FOREIGN KEY (MATHPTNAME) REFERENCES locations(PTNAME) ON DELETE CASCADE);


CREATE TABLE IF NOT EXISTS mathst (OUTID varchar not null primary key,
        MATHSTTEST varchar,
        MATHSTLANG  varchar,
        MATHSTTESTSTATUS varchar,
        MATHSTBALL12 numeric,
        MATHSTBALL numeric,
        MATHSTPTNAME varchar,
        CONSTRAINT student_info FOREIGN KEY (OUTID) REFERENCES student_info(OUTID) ON DELETE CASCADE,
        CONSTRAINT location_cons FOREIGN KEY (MATHSTPTNAME) REFERENCES locations(PTNAME) ON DELETE CASCADE);


CREATE TABLE IF NOT EXISTS phys (OUTID varchar not null primary key,
        PHYSTEST varchar,
        PHYSLANG varchar,
        PHYSTESTSTATUS varchar,
        PHYSBALL100 numeric,
        PHYSBALL12 numeric,
        PHYSBALL numeric,
        PHYSPTNAME varchar,
        CONSTRAINT student_info FOREIGN KEY (OUTID) REFERENCES student_info(OUTID) ON DELETE CASCADE,
        CONSTRAINT location_cons FOREIGN KEY (PHYSPTNAME) REFERENCES locations(PTNAME) ON DELETE CASCADE);


CREATE TABLE IF NOT EXISTS chem (OUTID varchar not null primary key,
        CHEMTEST varchar,
        CHEMLANG varchar,
        CHEMTESTSTATUS varchar,
        CHEMBALL100 numeric,
        CHEMBALL12 numeric,
        CHEMBALL numeric,
        CHEMPTNAME varchar,
        CONSTRAINT student_info FOREIGN KEY (OUTID) REFERENCES student_info(OUTID) ON DELETE CASCADE,
        CONSTRAINT location_cons FOREIGN KEY (CHEMPTNAME) REFERENCES locations(PTNAME) ON DELETE CASCADE);


CREATE TABLE IF NOT EXISTS bio (OUTID varchar not null primary key,
        BIOTEST varchar,
        BIOLANG varchar,
        BIOTESTSTATUS varchar,
        BIOBALL100 numeric,
        BIOBALL12 numeric,
        BIOBALL numeric,
        BIOPTNAME varchar,
        CONSTRAINT student_info FOREIGN KEY (OUTID) REFERENCES student_info(OUTID) ON DELETE CASCADE,
        CONSTRAINT location_cons FOREIGN KEY (BIOPTNAME) REFERENCES locations(PTNAME) ON DELETE CASCADE);


CREATE TABLE IF NOT EXISTS geo (OUTID varchar not null primary key,
        GEOTEST varchar,
        GEOLANG varchar,
        GEOTESTSTATUS varchar,
        GEOBALL100 numeric,
        GEOBALL12 numeric,
        GEOBALL numeric,
        GEOPTNAME varchar,
        CONSTRAINT student_info FOREIGN KEY (OUTID) REFERENCES student_info(OUTID) ON DELETE CASCADE,
        CONSTRAINT location_cons FOREIGN KEY (GEOPTNAME) REFERENCES locations(PTNAME) ON DELETE CASCADE);


CREATE TABLE IF NOT EXISTS eng (OUTID varchar not null primary key,
        ENGTEST varchar,
        ENGTESTSTATUS varchar,
        ENGBALL100 numeric,
        ENGBALL12 numeric,
        ENGDPALEVEL varchar,
        ENGBALL numeric,
        ENGPTNAME varchar,
        CONSTRAINT student_info FOREIGN KEY (OUTID) REFERENCES student_info(OUTID) ON DELETE CASCADE,
        CONSTRAINT location_cons FOREIGN KEY (ENGPTNAME) REFERENCES locations(PTNAME) ON DELETE CASCADE);


CREATE TABLE IF NOT EXISTS fra (OUTID varchar not null primary key,
        FRATEST varchar,
        FRATESTSTATUS varchar,
        FRABALL100 numeric,
        FRABALL12 numeric,
        FRADPALEVEL varchar,
        FRABALL numeric,
        FRAPTNAME varchar,
        CONSTRAINT student_info FOREIGN KEY (OUTID) REFERENCES student_info(OUTID) ON DELETE CASCADE,
        CONSTRAINT location_cons FOREIGN KEY (FRAPTNAME) REFERENCES locations(PTNAME) ON DELETE CASCADE);


CREATE TABLE IF NOT EXISTS deu (OUTID varchar not null primary key,
        DEUTEST varchar,
        DEUTESTSTATUS varchar,
        DEUBALL100 numeric,
        DEUBALL12 numeric,
        DEUDPALEVEL varchar,
        DEUBALL numeric,
        DEUPTNAME varchar,
        CONSTRAINT student_info FOREIGN KEY (OUTID) REFERENCES student_info(OUTID) ON DELETE CASCADE,
        CONSTRAINT location_cons FOREIGN KEY (DEUPTNAME) REFERENCES locations(PTNAME) ON DELETE CASCADE);


CREATE TABLE IF NOT EXISTS spa (OUTID varchar not null primary key,
        SPATEST varchar,
        SPATESTSTATUS varchar,
        SPABALL100 numeric,
        SPABALL12 numeric,
        SPADPALEVEL varchar,
        SPABALL numeric,
        SPAPTNAME varchar,
        CONSTRAINT student_info FOREIGN KEY (OUTID) REFERENCES student_info(OUTID) ON DELETE CASCADE,
        CONSTRAINT location_cons FOREIGN KEY (SPAPTNAME) REFERENCES locations(PTNAME) ON DELETE CASCADE);


INSERT INTO eo
SELECT DISTINCT(EONAME), EOTYPENAME, EOREGNAME, EOAREANAME, EOTERNAME, EOPARENT from test_results
where EONAME is not NULL;

INSERT INTO reg_info
SELECT DISTINCT REGNAME, AREANAME, TERNAME, TERTYPENAME from test_results
where AREANAME is not NULL and TERNAME is not NULL;

INSERT INTO student_info
SELECT DISTINCT(OUTID), BIRTH, SEXTYPENAME, AREANAME, TERNAME, REGTYPENAME, CLASSPROFILENAME, CLASSLANGNAME, EONAME, YEAR from test_results
where AREANAME is not NULL and TERNAME is not NULL;


INSERT INTO locations
SELECT DISTINCT PTNAME
FROM (
    SELECT UMLPTNAME as PTNAME, UMLPTREGNAME, UMLPTAREANAME, UMLPTTERNAME from test_results
    where UMLPTNAME is not NULL

    UNION

    SELECT UKRPTNAME PTNAME, UKRPTREGNAME, UKRPTAREANAME, UKRPTTERNAME from test_results
    where UKRPTNAME is not NULL

    UNION

    SELECT HISTPTNAME PTNAME, HISTPTREGNAME, HISTPTAREANAME, HISTPTTERNAME from test_results
    where HISTPTNAME is not NULL

    UNION

    SELECT MATHPTNAME PTNAME, MATHPTREGNAME, MATHPTAREANAME, MATHPTTERNAME from test_results
    where MATHPTNAME is not NULL

    UNION

    SELECT MATHSTPTNAME PTNAME, MATHSTPTREGNAME, MATHSTPTAREANAME, MATHSTPTTERNAME from test_results
    where MATHSTPTNAME is not NULL

    UNION

    SELECT PHYSPTNAME PTNAME, PHYSPTREGNAME, PHYSPTAREANAME, PHYSPTTERNAME from test_results
    where PHYSPTNAME is not NULL

    UNION

    SELECT CHEMPTNAME PTNAME, CHEMPTREGNAME, CHEMPTAREANAME, CHEMPTTERNAME from test_results
    where CHEMPTNAME is not NULL

    UNION

    SELECT BIOPTNAME PTNAME, BIOPTREGNAME, BIOPTAREANAME, BIOPTTERNAME from test_results
    where BIOPTNAME is not NULL

    UNION

    SELECT GEOPTNAME PTNAME, GEOPTREGNAME, GEOPTAREANAME, GEOPTTERNAME from test_results
    where GEOPTNAME is not NULL

    UNION

    SELECT ENGPTNAME PTNAME, ENGPTREGNAME, ENGPTAREANAME, ENGPTTERNAME from test_results
    where ENGPTNAME is not NULL

    UNION

    SELECT FRAPTNAME PTNAME, FRAPTREGNAME, FRAPTAREANAME, FRAPTTERNAME from test_results
    where FRAPTNAME is not NULL

    UNION

    SELECT DEUPTNAME PTNAME, DEUPTREGNAME, DEUPTAREANAME, DEUPTTERNAME from test_results
    where DEUPTNAME is not NULL

    UNION

    SELECT SPAPTNAME PTNAME, SPAPTREGNAME, SPAPTAREANAME, SPAPTTERNAME from test_results
    where SPAPTNAME is not NULL
    
) as subqueries;



INSERT INTO uml
SELECT DISTINCT(OUTID), UMLTEST, UMLTESTSTATUS, UMLBALL100, UMLBALL12, UMLBALL, UMLADAPTSCALE, UMLPTNAME from test_results
where UMLTEST is not NULL;


INSERT INTO ukr
SELECT DISTINCT(OUTID), UKRTEST,
        UKRSUBTEST,
        UKRTESTSTATUS,
        UKRBALL100,
        UKRBALL12,
        UKRBALL,
        UKRADAPTSCALE,
        UKRPTNAME from test_results
where UKRTEST is not NULL;


INSERT INTO hist
SELECT DISTINCT(OUTID),
        HISTTEST,
        HISTLANG,
        HISTTESTSTATUS,
        HISTBALL100,
        HISTBALL12,
        HISTBALL,
        HISTPTNAME from test_results
where HISTTEST is not NULL;


INSERT INTO math
SELECT DISTINCT(OUTID),
        MATHTEST,
        MATHLANG,
        MATHTESTSTATUS,
        MATHBALL100,
        MATHBALL12,
        MATHDPALEVEL,
        MATHBALL,
        MATHPTNAME from test_results
where MATHTEST is not NULL;


INSERT INTO mathst
SELECT DISTINCT(OUTID),
        MATHSTTEST,
        MATHSTLANG ,
        MATHSTTESTSTATUS,
        MATHSTBALL12,
        MATHSTBALL,
        MATHSTPTNAME from test_results
where MATHSTTEST is not NULL;


INSERT INTO phys
SELECT DISTINCT(OUTID),
        PHYSTEST,
        PHYSLANG,
        PHYSTESTSTATUS,
        PHYSBALL100,
        PHYSBALL12,
        PHYSBALL,
        PHYSPTNAME from test_results
where PHYSTEST is not NULL;


INSERT INTO chem
SELECT DISTINCT(OUTID),
        CHEMTEST,
        CHEMLANG,
        CHEMTESTSTATUS,
        CHEMBALL100,
        CHEMBALL12,
        CHEMBALL,
        CHEMPTNAME from test_results
where CHEMTEST is not NULL;


INSERT INTO bio
SELECT DISTINCT(OUTID),
        BIOTEST,
        BIOLANG,
        BIOTESTSTATUS,
        BIOBALL100,
        BIOBALL12,
        BIOBALL,
        BIOPTNAME from test_results
where BIOTEST is not NULL;


INSERT INTO geo
SELECT DISTINCT(OUTID),
        GEOTEST,
        GEOLANG,
        GEOTESTSTATUS,
        GEOBALL100,
        GEOBALL12,
        GEOBALL,
        GEOPTNAME from test_results
where GEOTEST is not NULL;


INSERT INTO eng
SELECT DISTINCT(OUTID),
        ENGTEST,
        ENGTESTSTATUS,
        ENGBALL100,
        ENGBALL12,
        ENGDPALEVEL,
        ENGBALL,
        ENGPTNAME from test_results
where ENGTEST is not NULL;


INSERT INTO deu
SELECT DISTINCT(OUTID),
        DEUTEST,
        DEUTESTSTATUS,
        DEUBALL100,
        DEUBALL12,
        DEUDPALEVEL,
        DEUBALL,
        DEUPTNAME from test_results
where DEUTEST is not NULL;


INSERT INTO spa
SELECT DISTINCT(OUTID),
        SPATEST,
        SPATESTSTATUS,
        SPABALL100,
        SPABALL12,
        SPADPALEVEL,
        SPABALL,
        SPAPTNAME from test_results
where SPATEST is not NULL;








