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

# Iterate over each wall and collect area data
for floor in floors:
    # Safely get the area parameter using get_Parameter
    area_param = floor.get_Parameter(DB.BuiltInParameter.HOST_AREA_COMPUTED)
    level_param = floor.get_Parameter(DB.BuiltInParameter.LEVEL_PARAM)   

    # Check if the area and level parameter exists and has a value
    if area_param and level_param:   
        print(15*"-")
        print(floor.Id)
        area_in_sqft = area_param.AsDouble()  # Area in square feet
        area_in_sqm = area_in_sqft * SQFT_TO_SQM  # Convert to square meters
        print(area_in_sqm)     
        print(level_param.AsString())
    else:
        print(15*"-")
        print("No values found")
