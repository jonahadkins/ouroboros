# creates a materialized spatial view in an oracle sde database
# uses *.sql files to keep queries in source control

import arcpy
import sys
sde = r"\\path\to\sde\connection.sde"
arcpy.env.workspace = sde
sql = arcpy.ArcSDESQLExecute(sde)

# first create a datbase view using esri tools

print("starting database view...")
databaseVW = r"\\path\to\database_vw.sql"
openDatabaseVW = open(databaseVW).read()
arcpy.CreateDatabaseView_management( sde, 'database_vw', openDatabaseVW)
print("\t\t...finished")

# then create a materialized view using oracle tools

databaseMVW = r"\\path\to\materialized_vw.sql"
openDatabaseMVW  = open(databaseMVW, 'r')
sqlDatabaseMVW = openDatabaseMVW.read()
openDatabaseMVW.close()
databaseMVWCommands = sqlDatabaseMVW.split(';')

# sql file deletes and re-creates materialized view instead of using rebuild
# sql file includes tabular index creation on several fields

print("creating materialized view...")
for commands in databaseMVWCommands:
    try:
        sql.execute(commands)
    except Exception as err:
        print(err)
print("...done")

# finally build spatial indexes on materialized view

print("starting spatial indexes...")
arcpy.AddSpatialIndex_management("schema.materialized_view_name")
print("\t\t...finished")
