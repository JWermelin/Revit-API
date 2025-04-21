#coding: utf-8

#Title
__title__ = "Floor Area"
__doc__ = """Version = 1.1 
Date = 2025-04-21

Description:
This prints out the Floor Areas and their Levels in the active Revit model.

How-to: Push button."""


from Autodesk.Revit import DB
from Autodesk.Revit.DB import FilteredElementCollector as Fec
from Autodesk.Revit.DB import BuiltInCategory as Bic

doc = __revit__.ActiveUIDocument.Document

floors = Fec(doc).OfCategory(Bic.OST_Floors).WhereElementIsNotElementType().ToElements()

SQFT_TO_SQM = 0.092903

# Dictionary to group floor areas by level name
floors_by_level = {}

# Iterate over each floor and collect area data
for floor in floors:
    area_param = floor.get_Parameter(DB.BuiltInParameter.HOST_AREA_COMPUTED)
    level_id = floor.LevelId
    level = doc.GetElement(level_id) if level_id != DB.ElementId.InvalidElementId else None

    if area_param and level:
        area_in_sqft = area_param.AsDouble()
        area_in_sqm = area_in_sqft * SQFT_TO_SQM
        rounded_area = round(area_in_sqm, 2)

        level_name = level.Name

        # Add to level grouping
        if level_name not in floors_by_level:
            floors_by_level[level_name] = []

        floors_by_level[level_name].append({
            "floor_id": floor.Id,
            "area_sqm": rounded_area
        })
    else:
        if "Unknown" not in floors_by_level:
            floors_by_level["Unknown"] = []
        floors_by_level["Unknown"].append({
            "floor_id": floor.Id,
            "area_sqm": 0.0
        })

# Sort level names
sorted_levels = sorted(floors_by_level.keys())

# Print grouped and sorted results
total_area = 0.0
for level_name in sorted_levels:
    print("=" * 30)
    print("Level: {}".format(level_name))
    print("=" * 30)

    level_area_total = 0.0  # Reset per level
    floor_list = floors_by_level[level_name]

    for floor_info in floor_list:
        print("-" * 15)
        print("Floor ID: {}".format(floor_info["floor_id"]))
        print("Area: {} m2".format(floor_info["area_sqm"]))
        level_area_total += floor_info["area_sqm"]

    if len(floor_list) > 1:
        print("-" * 15)
        print("Subtotal for {}: {} m2".format(level_name, round(level_area_total, 2)))

    total_area += level_area_total

# Final total
print("=" * 30)
print("Total Floor Area: {} m2".format(round(total_area, 2)))