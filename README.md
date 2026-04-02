# HW-06b: Triangle Classification Testing

## Description

This assignment involves testing and debugging an existing triangle classification program. The `classify_triangle()` function classifies triangles as Equilateral, Isosceles, Scalene, Right Scalene, or Invalid based on three side lengths.

## Files

- `Triangle.py` - Fixed implementation of the `classify_triangle()` function
- `TestTriangle.py` - Enhanced unit test suite with 37 test cases

## How to Run

```bash
python -m unittest TestTriangle -v
```

## Defects Found and Fixed

1. **Missing input type validation** - Non-numeric inputs (strings, None, lists) caused unhandled TypeError crashes. Fixed by adding an `isinstance` check.
2. **Float precision in right triangle check** - Strict `==` comparison fails for floating-point inputs. Fixed by using a tolerance-based comparison.

## Test Results

| | Test Run 1 (Buggy) | Test Run 2 (Fixed) |
|---|---|---|
| Tests Planned | 37 | 37 |
| Tests Executed | 37 | 37 |
| Tests Passed | 34 | 37 |
| Defects Found | 2 | 0 |
| Defects Fixed | 0 | 2 |
