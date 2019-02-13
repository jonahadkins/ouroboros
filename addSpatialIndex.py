# adds/rebuilds spatial index on feature class

import arcpy
import sys
sde = r"\\path\to\sde\connection.sde"
arcpy.env.workspace = sde

print("starting spatial indexes...")
arcpy.AddSpatialIndex_management("schema.feature_class_name")
print("\t\t...finished")
