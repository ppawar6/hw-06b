"""
Enhanced unit tests for triangle classification.
Tests the classify_triangle() function for correctness
across multiple categories: valid triangles, invalid inputs,
boundary conditions, and right triangle detection.
"""

import unittest
import math
from triangle import classify_triangle


class TestClassifyTriangle(unittest.TestCase):
    """Comprehensive tests for classify_triangle function."""

    # -------------------------------------------------------
    # 1. Equilateral Triangle Tests
    # -------------------------------------------------------
    def test_equilateral_small(self):
        """Test equilateral triangle with small sides (1,1,1)."""
        self.assertEqual(classify_triangle(1, 1, 1), "Equilateral")

    def test_equilateral_medium(self):
        """Test equilateral triangle with medium sides (3,3,3)."""
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")

    def test_equilateral_large(self):
        """Test equilateral triangle with larger sides (10,10,10)."""
        self.assertEqual(classify_triangle(10, 10, 10), "Equilateral")

    # -------------------------------------------------------
    # 2. Isosceles Triangle Tests
    # -------------------------------------------------------
    def test_isosceles_ab_equal(self):
        """Test isosceles where a == b (5,5,8)."""
        self.assertEqual(classify_triangle(5, 5, 8), "Isosceles")

    def test_isosceles_bc_equal(self):
        """Test isosceles where b == c (8,5,5)."""
        self.assertEqual(classify_triangle(8, 5, 5), "Isosceles")

    def test_isosceles_ac_equal(self):
        """Test isosceles where a == c (5,8,5)."""
        self.assertEqual(classify_triangle(5, 8, 5), "Isosceles")

    def test_isosceles_small(self):
        """Test isosceles with small sides (2,2,3)."""
        self.assertEqual(classify_triangle(2, 2, 3), "Isosceles")

    # -------------------------------------------------------
    # 3. Scalene Triangle Tests
    # -------------------------------------------------------
    def test_scalene_basic(self):
        """Test basic scalene triangle (4,5,6)."""
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene")

    def test_scalene_another(self):
        """Test another scalene triangle (7,9,11)."""
        self.assertEqual(classify_triangle(7, 9, 11), "Scalene")

    def test_scalene_small(self):
        """Test scalene with small sides (2,3,4)."""
        self.assertEqual(classify_triangle(2, 3, 4), "Scalene")

    # -------------------------------------------------------
    # 4. Right Scalene Triangle Tests
    # -------------------------------------------------------
    def test_right_scalene_345(self):
        """Test classic 3-4-5 right triangle."""
        self.assertEqual(classify_triangle(3, 4, 5), "Right Scalene")

    def test_right_scalene_51213(self):
        """Test 5-12-13 right triangle."""
        self.assertEqual(classify_triangle(5, 12, 13), "Right Scalene")

    def test_right_scalene_81517(self):
        """Test 8-15-17 right triangle."""
        self.assertEqual(classify_triangle(8, 15, 17), "Right Scalene")

    def test_right_scalene_72425(self):
        """Test 7-24-25 right triangle."""
        self.assertEqual(classify_triangle(7, 24, 25), "Right Scalene")

    # Right triangle with different argument orders
    def test_right_scalene_order_435(self):
        """Test right triangle with sides reordered (4,3,5)."""
        self.assertEqual(classify_triangle(4, 3, 5), "Right Scalene")

    def test_right_scalene_order_534(self):
        """Test right triangle with sides reordered (5,3,4)."""
        self.assertEqual(classify_triangle(5, 3, 4), "Right Scalene")

    def test_right_scalene_order_13_5_12(self):
        """Test right triangle with largest side first (13,5,12)."""
        self.assertEqual(classify_triangle(13, 5, 12), "Right Scalene")

    # -------------------------------------------------------
    # 5. Invalid Input Tests - Negative and Zero
    # -------------------------------------------------------
    def test_invalid_negative_a(self):
        """Test negative side a."""
        self.assertEqual(classify_triangle(-1, 2, 3), "Invalid")

    def test_invalid_negative_b(self):
        """Test negative side b."""
        self.assertEqual(classify_triangle(2, -1, 3), "Invalid")

    def test_invalid_negative_c(self):
        """Test negative side c."""
        self.assertEqual(classify_triangle(2, 3, -1), "Invalid")

    def test_invalid_all_negative(self):
        """Test all sides negative."""
        self.assertEqual(classify_triangle(-3, -4, -5), "Invalid")

    def test_invalid_zero_a(self):
        """Test zero side a."""
        self.assertEqual(classify_triangle(0, 4, 5), "Invalid")

    def test_invalid_zero_b(self):
        """Test zero side b."""
        self.assertEqual(classify_triangle(4, 0, 5), "Invalid")

    def test_invalid_zero_c(self):
        """Test zero side c."""
        self.assertEqual(classify_triangle(4, 5, 0), "Invalid")

    def test_invalid_all_zero(self):
        """Test all sides zero."""
        self.assertEqual(classify_triangle(0, 0, 0), "Invalid")

    # -------------------------------------------------------
    # 6. Invalid Input Tests - Triangle Inequality
    # -------------------------------------------------------
    def test_invalid_inequality_1(self):
        """Test triangle inequality: a + b < c."""
        self.assertEqual(classify_triangle(1, 2, 10), "Invalid")

    def test_invalid_inequality_2(self):
        """Test triangle inequality: a + c < b."""
        self.assertEqual(classify_triangle(1, 10, 2), "Invalid")

    def test_invalid_inequality_3(self):
        """Test triangle inequality: b + c < a."""
        self.assertEqual(classify_triangle(10, 1, 2), "Invalid")

    def test_invalid_degenerate(self):
        """Test degenerate triangle where a + b == c (1,1,2)."""
        self.assertEqual(classify_triangle(1, 1, 2), "Invalid")

    def test_invalid_degenerate_2(self):
        """Test degenerate triangle where a + c == b (1,2,1)."""
        self.assertEqual(classify_triangle(1, 2, 1), "Invalid")

    def test_invalid_degenerate_3(self):
        """Test degenerate triangle where b + c == a (2,1,1)."""
        self.assertEqual(classify_triangle(2, 1, 1), "Invalid")

    # -------------------------------------------------------
    # 7. Invalid Input Tests - Non-numeric types
    # -------------------------------------------------------
    def test_invalid_string_input(self):
        """Test that string inputs return Invalid instead of crashing."""
        self.assertEqual(classify_triangle("a", "b", "c"), "Invalid")

    def test_invalid_none_input(self):
        """Test that None inputs return Invalid instead of crashing."""
        self.assertEqual(classify_triangle(None, 4, 5), "Invalid")

    def test_invalid_list_input(self):
        """Test that list inputs return Invalid instead of crashing."""
        self.assertEqual(classify_triangle([3], 4, 5), "Invalid")

    # -------------------------------------------------------
    # 8. Boundary / Edge Case Tests
    # -------------------------------------------------------
    def test_boundary_just_valid(self):
        """Test triangle that barely satisfies inequality (3,4,6)."""
        self.assertEqual(classify_triangle(3, 4, 6), "Scalene")

    def test_large_equilateral(self):
        """Test equilateral with large values (100,100,100)."""
        self.assertEqual(classify_triangle(100, 100, 100), "Equilateral")

    def test_float_right_triangle(self):
        """Test right triangle with float inputs (3.0, 4.0, 5.0)."""
        self.assertEqual(classify_triangle(3.0, 4.0, 5.0), "Right Scalene")


if __name__ == '__main__':
    unittest.main()
