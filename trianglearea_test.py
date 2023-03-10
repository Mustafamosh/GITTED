import trianglearea
def test_triangle_area_0_0():
    area = trianglearea.triangle_area(0,0)
    assert area == 0

def test_triangle_area_3_4():
    area = trianglearea.triangle_area(3,4)
    assert area == 12

def test_triangle_negative_area():
    area = trianglearea.triangle_area(-3,-4)
    assert area == None

