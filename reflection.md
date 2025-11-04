1. Which issues were the easiest to fix, and which were the hardest? Why?

The easiest issues to fix were style-related errors such as missing docstrings, naming convention changes (from camelCase to snake_case), and spacing errors identified by Flake8. These only required small formatting changes and were easy to verify.
The hardest issues were logical and security-related fixes, such as replacing the eval() function and removing mutable default arguments. These required understanding how the code behaved and modifying function logic without breaking functionality.

2️. Did the static analysis tools report any false positives? If so, describe one example.

Yes, Pylint flagged the use of the global keyword in load_data() as a warning, suggesting it should be avoided. In this small program, using a global dictionary was intentional and practical, not an actual issue. Therefore, this can be considered a false positive, since removing it would have made the logic unnecessarily complex.

3️. How would you integrate static analysis tools into your actual software development workflow?

I would integrate Pylint, Bandit, and Flake8 directly into a Continuous Integration (CI) pipeline, for example, using GitHub Actions. Every pull request or commit could automatically trigger these tools to check for style, logic, and security issues.
Additionally, I would use pre-commit hooks locally to run Pylint and Flake8 before allowing a commit, ensuring code quality at every stage of development.

4️. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

After applying the fixes, the code became:

More readable – consistent naming conventions and proper formatting made it easier to follow.

More secure – removing eval() and using safe file handling with with open() eliminated potential security risks.

More maintainable – adding docstrings and structured logging improved clarity for future developers.

More robust – input validation and specific exception handling made the code safer and less prone to runtime errors.

Overall, static analysis significantly improved both code quality and developer confidence in the program.

