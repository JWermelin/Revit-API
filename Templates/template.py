#Title
__title__ = "JW Template.min"
__doc__ = """Verison =1.0
Date = 2025-xx-xx

Description:
This is a template file for pyRevit scripts.

How-to: Select xx, then push button."""


#Imports
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Architecture import *

import clr
clr.AddReference("System")
from System.Collections.Generic import List

#Variables
doc = __revit__.ActiveUIDocument.Document #type: Document
#verkar inte funka att få till autocomplete, lista ut varför.
uidoc = __revit__.ActiveUIDocument  #type: UIDocument
app = __revit__.Application #type: Application