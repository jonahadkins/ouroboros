# registers a feature class with the geodatabase
import arcpy
sde = r"\\path\to\connection.sde"
arcpy.env.workspace = sde

print("Registering feature class...")
arcpy.RegisterWithGeodatabase_management('feature_class_name', "unique_id", "SHAPE", "POLYGON")
print("\t\t...done")
