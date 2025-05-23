#coding: utf-8

#Title
__title__ = "Calculate Wall Volume"

"""Calculates total volume of all walls in the model."""

from Autodesk.Revit import DB

doc = __revit__.ActiveUIDocument.Document

# Creating collector instance and collecting all the walls from the model
wall_collector = DB.FilteredElementCollector(doc)\
.OfCategory(DB.BuiltInCategory.OST_Walls)\
.WhereElementIsNotElementType()

# Iterate over wall and collect Volume data
total_volume = 0.0 # This is defining a starting point (i.e. start the counting at 0.0)

for wall in wall_collector:
    vol_param = wall.Parameter[DB.BuiltInParameter.HOST_VOLUME_COMPUTED]
    if vol_param:
        total_volume = total_volume + vol_param.AsDouble()

rounded_volume = round(total_volume, 2)
# now that results are collected, print the total
print("Total Volume is: {}".format(rounded_volume))