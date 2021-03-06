"""
This file generates the dirs of the each person.
It reads the information form the database and then 
generate information according to the names of authors

@auther yuangao
@project matching system
@time 27.05.2014

"""

from __future__ import print_function
import sys
import os

from ..database_messager.mysql_messager import MysqlMessenger


def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)

def mkdir(path):
    try:
        os.makedirs(path)
    except Exception, e:
        warning(e)

table_name = "Persons"
mysqldb = MysqlMessenger()
sql = "select * from %s;" % table_name
mysqldb.execute_sql(sql)
docs_path = "./docs/papers/"

# for each row
# ID, FirstName, LastName, Link
iter = mysqldb.fetch()
for row in iter:
    first_name = row[1].lstrip().decode('latin1')
    last_name = row[2].lstrip().decode('latin1')
    mkdir(docs_path + first_name + "_" + last_name)
    paper_sql = ""
