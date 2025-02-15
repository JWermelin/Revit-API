#coding: utf-8

#Title
__title__ = "SetTopOffset"
__doc__ = """Verison =1.0
Date = 2025-xx-xx

Description:
This sets a new value for Wall Top Offsets.

How-to: Select xx, then push button."""


#Imports
from Autodesk.Revit import DB

import clr
clr.AddReference("System")
from System.Collections.Generic import List

#Variables
doc = __revit__.ActiveUIDocument.Document #type: Document
uidoc = __revit__.ActiveUIDocument  #type: UIDocument
app = __revit__.Application #type: Application

# Use __revit__ to access the active UIDocument in pyRevit
doc = __revit__.ActiveUIDocument.Document

# Create a collector instance and collect all the walls from the model
wall_collector = DB.FilteredElementCollector(doc)\
    .OfCategory(DB.BuiltInCategory.OST_Walls)\
    .WhereElementIsNotElementType()

# Iterate over each wall and collect area data
for wall in wall_collector:
    # Safely get the wall top offset parameter using get_Parameter
    wall_top_offset_param = wall.get_Parameter(DB.BuiltInParameter.WALL_TOP_OFFSET)

# Set new parameter value
if wall_top_offset_param:
    wall_top_offset_param.Set("500.0")