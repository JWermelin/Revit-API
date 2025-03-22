#coding: utf-8

#Title
__title__ = "Print Room Areas"
__doc__ = """Verison =1.0
Date = 2025-03-14

Description:
This prints the total surface area for all rooms in model.

How-to: Push button."""

from Autodesk.Revit import DB

# Use __revit__ to access the active UIDocument in pyRevit
doc = __revit__.ActiveUIDocument.Document

# Create a collector instance and collect all the walls from the model
room_collector = DB.FilteredElementCollector(doc)\
    .OfCategory(DB.BuiltInCategory.OST_Rooms)\
    .WhereElementIsNotElementType()

# Initialize total area
total_area = 0.0

# Iterate over each room and collect area data
for room in room_collector:
    # Safely get the area parameter using get_Parameter
    area_param = room.get_Parameter(DB.BuiltInParameter.ROOM_AREA)
    
    # Check if the area parameter exists and has a value
    if area_param and area_param.HasValue:
        # Add the area to the total (note: area is in Revit internal units, like square feet)
        total_area += area_param.AsDouble()

# Conversion factor from square feet to square meters
SQFT_TO_SQM = 0.092903

# Convert total area from square feet to square meters
total_area_sqm = total_area * SQFT_TO_SQM

print("Total Room Area in Square Meters is: {} m2".format(total_area_sqm))