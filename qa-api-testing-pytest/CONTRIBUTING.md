# Contributing Guidelines

Thank you for your interest in contributing to this QA automation project!

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a virtual environment and install dependencies (see README.md)
4. Create a new branch for your changes

## Code Style

- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add docstrings to classes and functions
- Keep functions focused and single-purpose
- Use type hints where appropriate

## Writing Tests

- Use descriptive test names that explain what is being tested
- Add appropriate pytest markers (smoke, regression, get, post, put, negative)
- Include both positive and negative test cases
- Use parametrization for testing multiple scenarios
- Ensure tests are independent and can run in any order
- Validate response schemas appropriately

## Commit Messages

Use clear, descriptive commit messages:
- Use present tense ("Add test" not "Added test")
- Be specific about what changed
- Reference issue numbers if applicable

Example:
```
Add test for user update endpoint
```

## Pull Request Process

1. Ensure all tests pass locally
2. Update documentation if needed
3. Create a clear PR description
4. Reference any related issues
5. Request review from maintainers

## Reporting Issues

When reporting bugs or suggesting features:
- Provide clear description of the issue
- Include steps to reproduce
- Add relevant API request/response examples
- Specify environment details (OS, Python version, etc.)

## Questions?

Feel free to open an issue for questions or discussions.

Thank you for contributing! 🎉

