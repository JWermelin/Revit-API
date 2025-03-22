#coding: utf-8

#Title
__title__ = "Mirrored Doors and Types"
__doc__ = """Verison =1.0
Date = 2025-03-22

Description:
This prints out all the mirrored doors and their Ids and types in the active Revit model.

How-to: Push button."""

from Autodesk.Revit import DB
from Autodesk.Revit.DB import FilteredElementCollector as Fec
from Autodesk.Revit.DB import BuiltInCategory as Bic


doc = __revit__.ActiveUIDocument.Document

doors = Fec(doc).OfCategory(Bic.OST_Doors).\
	WhereElementIsNotElementType().ToElements()

for door in doors:
	print(15*"-")
	print(door.Id)
	print(door.Mirrored)
	
for door in doors:
	print(15*"-")
	print(door.Id)
	print(door.Symbol.LookupParameter("Type Name").AsString())
	
	