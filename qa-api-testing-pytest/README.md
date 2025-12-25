# QA API Testing - Pytest + Requests

## Overview

This project provides comprehensive API testing for the ReqRes public REST API using Pytest and Requests. The test suite covers CRUD operations, schema validation, and negative test scenarios.

## Scope

The test suite covers the following scenarios:
- ✅ GET list of users - returns 200 and validates schema
- ✅ GET single user - returns expected id and fields
- ✅ POST create user - returns 201 and validates created object
- ✅ PUT update user - returns 200 and validates updated fields
- ✅ Negative test: GET non-existing resource returns 404

## Test Strategy

- **Framework**: Pytest with Requests library
- **Pattern**: Fixture-based test organization with helper utilities
- **Validation**: Manual schema validation (key presence and type checking)
- **Reporting**: pytest-html for test reports
- **CI/CD**: GitHub Actions for automated test execution
- **Parametrization**: Multiple test cases with different data sets

## Tech Stack

- **Python**: 3.8+
- **Pytest**: Test framework
- **Requests**: HTTP library for API calls
- **pytest-html**: HTML test reports
- **pytest-xdist**: Optional parallel execution

## API Choice

**Target API**: https://jsonplaceholder.typicode.com

**Why JSONPlaceholder?**
- Stable and reliable public REST API
- Well-documented endpoints
- Supports all CRUD operations
- Predictable responses
- No authentication required
- No rate limiting or Cloudflare protection
- Designed specifically for testing and prototyping

## Project Structure

```
qa-api-testing-pytest/
├── tests/              # Test cases
│   ├── __init__.py
│   ├── test_users_api.py
│   └── test_posts_api.py
├── utils/              # Helper utilities
│   ├── __init__.py
│   └── api_client.py
├── reports/            # Test reports (gitignored)
├── conftest.py         # Pytest fixtures and configuration
├── pytest.ini          # Pytest configuration
├── requirements.txt    # Python dependencies
├── Makefile           # Convenience commands
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## How to Run

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Internet connection (for API calls)

### Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd qa-api-testing-pytest
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running Tests

**Using Makefile** (recommended):
```bash
make install      # Install dependencies
make test         # Run all tests
make report       # Open the HTML report
```

**Using pytest directly**:
```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_users_api.py

# Run with markers
pytest -m smoke
```

### Test Data

Test data is defined within test cases using parametrization. The API uses mock data, so no external test data files are required.

## Reporting

Test reports are generated in the `reports/` directory:
- **HTML Report**: `reports/report.html` (opens automatically after test run)

To view the report:
```bash
make report
# or
open reports/report.html
```

## CI/CD

GitHub Actions workflow (`.github/workflows/test.yml`) runs automatically on:
- Push to main/master branch
- Pull requests

The workflow:
1. Sets up Python environment
2. Installs dependencies
3. Runs tests
4. Uploads test reports as artifacts

## Schema Validation

The project uses lightweight manual schema validation:
- Checks for required keys in response JSON
- Validates data types (string, int, etc.)
- No heavy dependencies (like JSON Schema validators)

Example:
```python
assert "id" in response_data
assert isinstance(response_data["id"], int)
assert "email" in response_data
assert isinstance(response_data["email"], str)
```

## Notes

- **Target API**: https://reqres.in (public demo REST API)
- **Rate Limiting**: ReqRes has minimal rate limiting; tests should run smoothly
- **Data Persistence**: ReqRes is a mock API; created/updated data doesn't persist
- **Response Times**: API responses are typically fast (< 1 second)
- **Error Handling**: Tests include proper error handling and assertions

## Troubleshooting

**Issue**: Connection errors or timeouts
- **Solution**: Check internet connectivity and API availability

**Issue**: Import errors
- **Solution**: Ensure virtual environment is activated and dependencies are installed

**Issue**: Tests fail with 429 (Too Many Requests)
- **Solution**: Add delays between requests or reduce test execution frequency

## License

MIT License - see LICENSE file for details.

