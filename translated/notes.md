## Dependencies
This code depends on (preferably latest stable builds of):
- `scipy`
- `numpy`
- `matplotlib`

## Translation notes
I've opted for an almost entirely line-by-line translation of the MATLAB code into Python (primarily to gain familiarity myself), but also because there's not much to be gained from reducing the number of lines (it's also quite difficult to do without arbitrarily making the code harder to read). Some unnecessary (single-use) variables have been removed, and I've also used Python-specific syntax in some cases (such as list comprehensions or variable swaps), but it's easy to compare to the original code if needed.