"""
equilateral triangles have all three sides with the same length
isosceles triangles have two sides with the same length
scalene triangles have three sides with different lengths
right triangles have three sides with lengths, a, b, and c where a2 + b2 = c2
"""


def classify_triangle(a, b, c):
    """Classify a triangle based on side lengths."""

    # Input type validation - must be int or float
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))
            and isinstance(c, (int, float))):
        return "Invalid"

    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid"

    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid"

    if a == b == c:
        return "Equilateral"

    if a == b or b == c or a == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    sides = sorted([a, b, c])
    if abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 0.0001:
        triangle_type = "Right " + triangle_type

    return triangle_type
