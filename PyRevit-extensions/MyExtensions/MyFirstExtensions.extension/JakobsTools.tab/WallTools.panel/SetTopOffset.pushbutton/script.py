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

        if wall_top_offset_param and wall_top_offset_param.CanSet():  # Check if the parameter exists and can be set
            try:
                # Set the new parameter value for this wall
                wall_top_offset_param.Set(500.0)
            except Exception as e:
                # Print an error message for the wall if it fails
                print("Error updating wall {0}: {1}".format(wall.Id, str(e)))
                # If an error occurs with a specific wall, continue to the next one
                continue
        else:
            print("Wall {0} does not have a valid wall_top_offset_param.".format(wall.Id))

    # Commit the transaction after all changes
    t.Commit()

except Exception as e:
    # If anything goes wrong, rollback the transaction
    print("Error: {}".format(str(e)))
    t.RollBack()