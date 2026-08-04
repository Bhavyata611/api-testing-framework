# API Testing Automation Framework

A reusable API Testing Automation Framework built using **Python**, **Requests**, and **Pytest** to automate REST API testing. The framework validates API functionality, response data, response time, headers, and JSON schema while generating HTML reports for test execution.

---

## Technologies Used

- Python 3.14
- Requests
- Pytest
- JSON Schema
- pytest-html
- Git

---

## Features

- Automated REST API Testing
- GET Request Testing
- POST Request Testing
- PUT Request Testing
- PATCH Request Testing
- DELETE Request Testing
- Status Code Validation
- Response Header Validation
- Response Body Validation
- Response Time Validation
- JSON Schema Validation
- HTML Test Report Generation
- Reusable API Client
- Pytest Fixtures
- Logging Support
- Centralized Configuration

---

## Project Structure

```
API-Testing-Framework/
│
├── tests/
│   ├── conftest.py
│   ├── test_get_users.py
│   ├── test_post_users.py
│   ├── test_put_users.py
│   ├── test_patch_users.py
│   ├── test_delete_users.py
│   └── test_schema_validation.py
│
├── utils/
│   ├── api_client.py
│   ├── config.py
│   └── logger.py
│
├── schemas/
│   └── post_schema.json
│
├── reports/
│   ├── report.html
│   └── api_test.log
│
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## API Used

JSONPlaceholder

https://jsonplaceholder.typicode.com

---

## Test Coverage

| API Method | Status |
|------------|--------|
| GET | ✅ |
| POST | ✅ |
| PUT | ✅ |
| PATCH | ✅ |
| DELETE | ✅ |

---

## Validations Performed

- HTTP Status Code
- Response Headers
- Response Body
- Response Time
- JSON Schema Validation

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Move to project directory

```bash
cd API-Testing-Framework
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Execute Tests

Run all tests

```bash
pytest -v
```

Generate HTML Report

```bash
pytest --html=reports/report.html --self-contained-html
```

---

## Sample Output

```
============================
6 Tests Collected
6 Tests Passed
============================
```

---

## Reports

- HTML Report (`reports/report.html`)
- Execution Log (`reports/api_test.log`)

---

## Future Enhancements

- Authentication Testing
- Data-Driven Testing
- Environment Variables
- CI/CD Integration using GitHub Actions
- Docker Support
- API Mocking
- Parallel Test Execution

---

## Author

**Bhavyata Suthar**