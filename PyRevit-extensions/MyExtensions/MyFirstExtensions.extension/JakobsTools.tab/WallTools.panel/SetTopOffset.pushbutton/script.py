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
from Autodesk.Revit.DB import Transaction

import clr
clr.AddReference("System")
from System.Collections.Generic import List
from pyrevit import forms

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

# Start a new transaction for all walls
t = Transaction(doc, "Set Wall Top Offset")  # Start a single transaction
t.Start()

try:
    # Iterate over each wall and collect Parameter data
    for wall in wall_collector:
        # Safely get the wall top offset parameter using get_Parameter
        wall_top_offset_param = wall.get_Parameter(DB.BuiltInParameter.WALL_TOP_OFFSET)
        input_form = forms.ask_for_string(prompt='Enter new top offset value:') # prompt input from user
        user_input = float(input_form) / 304.8
        wall_top_offset_param.Set(user_input) # set parameter value
        

    # Commit the transaction after all changes
    t.Commit()

except Exception as e:
    # If anything goes wrong, rollback the transaction
    print("Error: {}".format(str(e)))
    t.RollBack()