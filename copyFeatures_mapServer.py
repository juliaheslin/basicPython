import arcpy

arcpy.env.overwriteOutput = True

baseURL = "https://enviroatlas.epa.gov/arcgis/rest/services/Supplemental/EPA_Regions/MapServer/1"
where = "1=1"
fields = "EPAREGION,Contact Info"

query = "?where={}&outFields={}&returnGeometry=true&f=json".format(where, fields)

fsURL = baseURL + query

fs = arcpy.FeatureSet()
fs.load(fsURL)

arcpy.CopyFeatures_management(fs, "C:\Users\jheslin\Documents\ArcGIS\Default.gdb")
