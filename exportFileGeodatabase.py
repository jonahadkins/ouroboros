# exports several sde feature classes to a file geodatabase

import arcpy
import datetime
sde = r"\\path\to\sde\connection.sde"
arcpy.env.workspace = sde

# creates an output file geodatabase with the data appended to the name

out_folder_path = r"\\path\to\output\folder"
nowstart = datetime.datetime.now()
YearMonthDay = nowstart.strftime("%Y_%m_%d")
out_name = "\fgdbName_" + YearMonthDay + ".gdb"

print("creating...")
arcpy.CreateFileGDB_management(out_folder_path, out_name)

# sends sde layers in list to file geodatabase
print("copying..")
arcpy.env.workspace = sde
layers = ['featureClass1','featureClass2','featureClass3']
outLocation = out_folder_path  + out_name


for fc in layers:
    arcpy.FeatureClassToGeodatabase_conversion(fc, outLocation)
print("voila...")
