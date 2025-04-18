# Unit 9: Packaging and Testing

## 🧠 Learning Focus

This unit focused on preparing Python code for reuse and maintainability through packaging, documentation, and testing. It also explored the impact of code complexity and the importance of clean, modular programming practices.

Key topics covered include:
- Structuring reusable Python modules and packages
- Writing PEP 257-compliant docstrings for better documentation
- Creating and running unit tests using Python’s `unittest` module
- Handling exceptions with proper error messages
- Understanding software quality through testing and design simplicity

## 📁 Artefacts Included

### 1. Package Initializer – `__init__.py`
- **File:** `math_utils/__init__.py`  
- **Description:** Exposes the `Calculator` class as part of the package interface. Ensures clean import paths for external use.

### 2. Python Package – `math_utils`
- **File:** `math_utils/calculator.py`  
- **Description:** Contains a `Calculator` class implementing basic arithmetic operations. All methods are documented using PEP 257-style docstrings.

### 3. Unit Tests – `test_calculator.py`
- **File:** `test/test_calculator.py`  
- **Description:** Contains a full test suite for the `Calculator` class using Python’s built-in `unittest` framework. Tests include all four arithmetic operations, including divide-by-zero handling.

## ✅ Learning Outcomes Demonstrated

- Created a modular, testable Python package with reusable components
- Applied proper exception handling within reusable methods
- Used unit testing to verify functional correctness
- Applied software quality principles through structure, naming, and documentation
- Followed professional best practices for maintainability and distribution

