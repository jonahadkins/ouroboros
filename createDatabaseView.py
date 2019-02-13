# creates a database view using ArcPY in an oracle sde database
# uses *.sql files to keep queries in source control

import arcpy
import sys
sde = r"\\path\to\sde\connection.sde"
arcpy.env.workspace = sde
sql = arcpy.ArcSDESQLExecute(sde)



print("starting database view...")
databaseVW = r"\\path\to\database_vw.sql"
openDatabaseVW = open(databaseVW).read()
arcpy.CreateDatabaseView_management( sde, 'database_vw', openDatabaseVW)
print("\t\t...finished")
