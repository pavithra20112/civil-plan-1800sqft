import ezdxf

# Create new drawing
doc = ezdxf.new(dxfversion='R2010')
msp = doc.modelspace()

# 30 x 60 ft main boundary
msp.add_lwpolyline([(0, 0), (30, 0), (30, 60), (0, 60), (0, 0)], close=True)

# Hall (15 x 20)
msp.add_lwpolyline([(0, 0), (15, 0), (15, 20), (0, 20), (0, 0)], close=True)
msp.add_text('Hall', dxfattribs={'height': 1.0}).dxf.insert = (5, 10)

# Kitchen (10 x 10)
msp.add_lwpolyline([(15, 0), (25, 0), (25, 10), (15, 10), (15, 0)], close=True)
msp.add_text('Kitchen', dxfattribs={'height': 1.0}).dxf.insert = (17, 5)

# Bedroom1 (12x12)
msp.add_lwpolyline([(0, 20), (12, 20), (12, 32), (0, 32), (0, 20)], close=True)
msp.add_text('Bedroom 1', dxfattribs={'height': 1.0}).dxf.insert = (2, 25)

# North Arrow
msp.add_line((28, 58), (28, 63))  # Arrow line
msp.add_text("NORTH", dxfattribs={'height': 1.5}).dxf.insert = (26, 64)

# Door in Hall
msp.add_line((0, 10), (3, 10))

# Save the file
doc.saveas("civil_plan_1800sqft.dxf")


