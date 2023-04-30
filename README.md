<div>
    <h1 align="center">Laboratory work №1</h1>
    <h2 align="center">From database discipline</h2>
    <p align="right"><b>Khok Maksym КМ-03</b></p>
</div>
<div>
   <hr>
        <h4>Run code</h4>
        <p>To start the program, you need to :</p>
         <ol>
            <li>Put .csv files in ./app/data and ./app_lab1/data. There should be a least two files with names 'Odata2021File.csv', 'Odata2020File.csv'.</li>
            <li>Run the following command in the terminal:
            <p style="background-color: #E5ECEB">docker-compose build --no-cache && docker-compose up -d --force-recreate<p>
            </li>
            <li>For the convenience of testing, you can use Adminer, run it from the container.<br> User: Admin<br> Password: example<br> db: postgres</li>
         </ol>
   </hr>
     <hr>
        <h4>Short description</h4>
        <p>The project script implements data loading from the <i>.csv</i> files in the <i>data</i> folder. After starting the program, data for 2021 and 2020 will be loaded into the database, but it is possible to download information for all years. For convenience of testing, the data is transmitted into the database in only two years, which is further used for an individual task. The data are collected in the created tables and the logs in the table  <i>log_table</i>.</p>
<p>Individual Task (Option 12):<br>
Compare the worst physics score in each region in 2020 and 2021 among those who were credited with the test.</p>
<p>SQL query fro task:<br></p>
<p style="background-color: #E5ECEB">select newschema.student_info.year, newschema.reg_info.regname, MIN(newschema.phys.physball100) as physball100<br>
from (newschema.student_info inner join newschema.reg_info ON reg_info.areaname = student_info.areaname) inner join newschema.phys using(outid)<br> 
                   where newschema.student_info.year in (2021, 2020) and newschema.phys.physteststatus = 'Зараховано'<br> 
                   group by newschema.student_info.year , newschema.reg_info.regname<br> 
                   order by newschema.reg_info.regname</p>
<p>The results of the individual task are stored in the file <i>task_result.csv</i>.
The work time of the program and count of records in DB(SELECT count(*)...) are stored in the file <i>time.txt</i>.</p>
     </hr>
     <hr>
        <h4>Tech stack</h4>
        <ul>
            <li>Implementation language - Python (psycopg2, pandas modules)</li>
            <li>DBMS — PostgreSQL</li>
            <li>Client-Server DBMS — pgAdmin, Adminer</li>
            <li>Migration tool — flyway</li>
        </ul>
     </hr>
</div>