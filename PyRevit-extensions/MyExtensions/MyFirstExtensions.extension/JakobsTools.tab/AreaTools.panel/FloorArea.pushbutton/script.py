#coding: utf-8

#Title
__title__ = "Floor Area LOA"
__doc__ = """Verison = 1.0
Date = 2025-03-29

Description:
This prints out the Floor Areas and their Levels in the active Revit model.

How-to: Push button."""

from Autodesk.Revit import DB
from Autodesk.Revit.DB import FilteredElementCollector as Fec
from Autodesk.Revit.DB import BuiltInCategory as Bic


doc = __revit__.ActiveUIDocument.Document

floors = Fec(doc).OfCategory(Bic.OST_Floors).\
	WhereElementIsNotElementType().ToElements()

SQFT_TO_SQM = 0.092903

# Initialize total area
total_area = 0.0

# Iterate over each floor and collect area data
for floor in floors:
    # Safely get the area parameter using get_Parameter
    area_param = floor.get_Parameter(DB.BuiltInParameter.HOST_AREA_COMPUTED)
    level_id = floor.LevelId
    level = doc.GetElement(level_id) if level_id != DB.ElementId.InvalidElementId else None

    # Check if the area and level exist
    if area_param and level:   
        print(15 * "-")
        print("Floor ID: {}".format(floor.Id))
        area_in_sqft = area_param.AsDouble()  # Area in square feet
        area_in_sqm = area_in_sqft * SQFT_TO_SQM  # Convert to square meters
        rounded_num = round(area_in_sqm, 2)
        print("Area: {} m2".format(rounded_num))
        print("Level: {}".format(level.Name))
        total_area += area_in_sqm
    else:
        print(15*"-")
        print("No values found")
print(15 * "-")
rounded_total = round(total_area, 2)
print("Total Floor Area: {}m2".format(rounded_total))
