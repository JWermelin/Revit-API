#coding: utf-8

#Title
__title__ = "Recenter Rooms"
__doc__ = """Verison =1.00
Date = 2025-04-28

Description:
This recenters all rooms in a model.

How-to: Push button."""

from Autodesk.Revit import DB
from Autodesk.Revit.DB import XYZ

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
view = uidoc.ActiveGraphicalView

# Start a Transaction, because you are modifying the document
t = DB.Transaction(doc, "Move Rooms to Center of Bounding Boxes")
t.Start()

room_collector = DB.FilteredElementCollector(doc)\
    .OfCategory(DB.BuiltInCategory.OST_Rooms)\
    .WhereElementIsNotElementType()

unplaced_rooms_count = 0  # Counter for unplaced rooms

for room in room_collector:
    # Get the Room's Location
    location = room.Location

    # Unplaced rooms have no Location
    if location is None:
        unplaced_rooms_count += 1
        continue

    if not isinstance(location, DB.LocationPoint):
        print("Room {0} does not have a LocationPoint. Skipping.".format(room.Id))
        continue  # Only handle LocationPoint, not LocationCurve

    # Get BoundingBox
    bounding_box = room.get_BoundingBox(view)
    if bounding_box is None:
        print("Room {0} has no bounding box. Skipping.".format(room.Id))
        continue

    # Calculate center of bounding box
    min_pt = bounding_box.Min
    max_pt = bounding_box.Max
    center_x = (min_pt.X + max_pt.X) / 2
    center_y = (min_pt.Y + max_pt.Y) / 2
    center_z = (min_pt.Z + max_pt.Z) / 2
    center_pt = DB.XYZ(center_x, center_y, center_z)

    # Current Room location
    current_pt = location.Point

    # Vector from current location to center point
    move_vector = center_pt - current_pt

    # Move the Room
    location.Move(move_vector)

    # Get Room Name and Area
    # Get Room Name safely
    name_param = room.get_Parameter(DB.BuiltInParameter.ROOM_NAME)
    if name_param and name_param.HasValue:
        room_name = name_param.AsString()
    else:
        room_name = "Unnamed Room"

    area_param = room.get_Parameter(DB.BuiltInParameter.ROOM_AREA)
    if area_param and area_param.HasValue:
        room_area = area_param.AsDouble()  # Revit stores area in square feet (internal units)
        # convert to m², multiply by 0.092903
        room_area = room_area * 0.092903
    else:
        room_area = None

    # Print details
    if room_area is not None:
        print("Moved Room '{0}' (Area: {1:.2f} m²) to center of its bounding box.".format(room_name, room_area))
    else:
        print("Moved Room '{0}' (Area: Unknown) to center of its bounding box.".format(room_name))

t.Commit()

# After transaction ends
print("Ignored {0} unplaced rooms.".format(unplaced_rooms_count))
