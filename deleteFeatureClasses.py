# deletes a list of feature classes

import arcpy
import sys
sde = r"\\path\to\sde\connection.sde"
arcpy.env.workspace = sde

# might help to disconnect users before deleting stuff
print(".....disconnecting users...")
arcpy.DisconnectUser(neip, "ALL")

# delete this fc's
print("\t\t...Deleting feature classes")
features = ['feature_class_1','feature_class_2','Sfeature_class_3']

for values in features:
    print values,
    try:
        arcpy.Delete_management(values)
        print("\t\t ...deleted")
    except:
        print(" \t\t...failed to delete")
        
print(".....done...")
