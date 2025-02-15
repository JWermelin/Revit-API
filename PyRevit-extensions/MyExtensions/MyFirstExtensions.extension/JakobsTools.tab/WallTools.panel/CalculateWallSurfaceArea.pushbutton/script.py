#coding: utf-8

#Title
__title__ = "CalculateWallSurfaceArea"
__doc__ = """Verison =1.0
Date = 2025-02-15

Description:
This calculates the total surface area for all walls in model.

How-to: Push button."""

from Autodesk.Revit import DB

# Use __revit__ to access the active UIDocument in pyRevit
doc = __revit__.ActiveUIDocument.Document

# Create a collector instance and collect all the walls from the model
wall_collector = DB.FilteredElementCollector(doc)\
    .OfCategory(DB.BuiltInCategory.OST_Walls)\
    .WhereElementIsNotElementType()

# Initialize total area
total_area = 0.0

# Iterate over each wall and collect area data
for wall in wall_collector:
    # Safely get the area parameter using get_Parameter
    area_param = wall.get_Parameter(DB.BuiltInParameter.HOST_AREA_COMPUTED)
    
    # Check if the area parameter exists and has a value
    if area_param and area_param.HasValue:
        # Add the area to the total (note: area is in Revit internal units, like square feet)
        total_area += area_param.AsDouble()

# Conversion factor from square feet to square meters
SQFT_TO_SQM = 0.092903

# Convert total area from square feet to square meters
total_area_sqm = total_area * SQFT_TO_SQM

print("Total Wall Area in Square Meters is: {} m2".format(total_area_sqm))