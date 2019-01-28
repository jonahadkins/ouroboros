# imports a list of feature classes from a file geodatabase into a sde database

import arcpy
import sys

sde = r"\\path\to\sde\connection.sde"
arcpy.env.workspace = sde

# disconnect users

print(".....disconnecting users...")
arcpy.DisconnectUser(sde, "ALL")

# delete existing layers

print("\t\t...Deleting feature classes")
features = ['featureClass1','featureClass2','featureClass3']

for values in features:
    print values,
    try:
        arcpy.Delete_management(values)
        print("\t\t ...deleted")
    except:
        print(" \t\t...failed to delete")

# set environment to fgdb for this part

fgdb = r"\\path\to\fileGeodatabase.gdb"
arcpy.env.workspace = fgdb

inFeatures = ['featureClass1','featureClass2','featureClass3']
outLocation = sde

print("\t\t..copying..")
arcpy.FeatureClassToGeodatabase_conversion(inFeatures, outLocation)
print("\t\t..dunzo...")
