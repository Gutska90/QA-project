.PHONY: install test report clean lint

# Default target
.DEFAULT_GOAL := help

help:
	@echo "Available commands:"
	@echo "  make install  - Install dependencies"
	@echo "  make test     - Run all tests"
	@echo "  make report   - Open the HTML test report"
	@echo "  make clean     - Clean generated files and reports"
	@echo "  make lint      - Run linting checks (optional)"

install:
	@echo "Installing Python dependencies..."
	pip install -r requirements.txt

test:
	@echo "Running tests..."
	@mkdir -p reports
	pytest

report:
	@echo "Opening test report..."
	@if [ -f reports/report.html ]; then \
		open reports/report.html || xdg-open reports/report.html || echo "Please open reports/report.html manually"; \
	else \
		echo "No report found. Run 'make test' first."; \
	fi

clean:
	@echo "Cleaning generated files..."
	rm -rf reports/
	rm -rf __pycache__/
	rm -rf .pytest_cache/
	rm -rf utils/__pycache__/
	rm -rf tests/__pycache__/
	find . -type d -name __pycache__ -exec rm -r {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

lint:
	@echo "Linting is optional. Install flake8 or pylint to use this target."
	@echo "Example: pip install flake8 && flake8 ."

