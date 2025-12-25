# QA Web E2E Automation - Playwright + Pytest

## Overview

This project provides end-to-end web automation tests for the SauceDemo e-commerce demo application using Playwright and Pytest. The tests cover critical user flows including authentication, shopping cart operations, and checkout processes.

## Scope

The test suite covers the following scenarios:
- ✅ Successful user login
- ✅ Invalid login error handling
- ✅ Add item to cart and verify cart count
- ✅ Checkout flow verification (up to overview page)
- ✅ User logout functionality

## Test Strategy

- **Framework**: Playwright with Pytest
- **Pattern**: Page Object Model (POM) for maintainability
- **Reporting**: pytest-html with screenshots on failure
- **CI/CD**: GitHub Actions for automated test execution
- **Browser**: Chromium (configurable)

## Tech Stack

- **Python**: 3.8+
- **Playwright**: Latest stable version
- **Pytest**: Test framework
- **pytest-html**: HTML test reports
- **pytest-xdist**: Optional parallel execution

## Project Structure

```
qa-web-e2e-playwright/
├── pages/              # Page Object Model classes
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/              # Test cases
│   ├── __init__.py
│   └── test_e2e_flows.py
├── reports/            # Test reports and screenshots (gitignored)
│   └── screenshots/
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

### Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd qa-web-e2e-playwright
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

4. **Install Playwright browsers**:
   ```bash
   python -m playwright install chromium
   ```

### Running Tests

**Using Makefile** (recommended):
```bash
make install      # Install dependencies and browsers
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
pytest tests/test_e2e_flows.py

# Run with markers
pytest -m smoke
```

### Test Data

Default test credentials for SauceDemo:
- **Valid user**: `standard_user` / `secret_sauce`
- **Invalid user**: `invalid_user` / `wrong_password`

## Reporting

Test reports are generated in the `reports/` directory:
- **HTML Report**: `reports/report.html` (opens automatically after test run)
- **Screenshots**: `reports/screenshots/` (captured on test failures)

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
3. Installs Playwright browsers
4. Runs tests
5. Uploads test reports and screenshots as artifacts

## Notes

- **Target Application**: https://www.saucedemo.com (public demo site)
- **Browser**: Chromium (default, configurable in `conftest.py`)
- **Timeouts**: Default wait timeout is 10 seconds (configurable)
- **Headless Mode**: Enabled by default in CI, can be toggled locally
- **Screenshots**: Automatically captured on test failures

## Troubleshooting

**Issue**: Playwright browsers not found
- **Solution**: Run `python -m playwright install chromium`

**Issue**: Tests fail with timeout errors
- **Solution**: Check network connectivity and target site availability

**Issue**: Import errors
- **Solution**: Ensure virtual environment is activated and dependencies are installed

## License

MIT License - see LICENSE file for details.

