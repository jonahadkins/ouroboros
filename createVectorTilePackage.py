# Creates / Recreates Vector Tile Package From An ArcGIS Pro Project
# To run standalone use C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe or arcgispro-py3 executable path
# See http://pro.arcgis.com/en/pro-app/tool-reference/data-management/create-vector-tile-package.htm for more info
import arcpy
arcpy.env.overwriteOutput = True #overwrite exisiting file - might run into locks if Project is open


print("Opening Project....")
project = arcpy.mp.ArcGISProject(r"C:\Path\To\ArcGIS\Pro\Project.aprx")
for maps in project.listMaps():
    print("Packaging...." + maps.name)
    arcpy.management.CreateVectorTilePackage(
                                             maps,
                                             r"C:\Path\To\Output\Folder\filename.vtpk",
                                             "ONLINE", # service type
                                             "", # tiling scheme
                                             "INDEXED", # tile structure
                                             295828763.7957775, # max scale
                                             288895.2771445, # min scale
                                             r"C:\Path\To\Tile\Index\FileGDB.gdb\feature_class",
                                             "fill in item summary info",
                                             "comma,separated,tags"
                                             )

print("....Done")
