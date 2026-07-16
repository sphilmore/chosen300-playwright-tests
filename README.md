# Chosen 300 Volunteer App — Playwright Test Automation

End-to-end UI test automation for the [Chosen 300 Volunteer App](https://chosen-300-volunteer-app-prototype-pbgi.vercel.app/) using **Python**, **Playwright**, and **pytest**.

## Tech Stack

- Python 3.10+
- Playwright (sync API)
- pytest
- pytest-playwright
- python-dotenv

## Project Structure

```
playwright300/
├── pages/                  # Page Object Model classes
│   ├── base_page.py
│   ├── lang_page.py
│   ├── login_page.py
│   ├── new_login.py
│   ├── community_service_page.py
│   ├── musician_page.py
│   └── donations.py
├── tests/                  # Test suites
│   ├── test_language.py
│   ├── test_login_page.py
│   ├── test_new_login.py
│   ├── test_community_service.py
│   ├── test_musician.py
│   └── test_donations.py
├── config.py               # Loads test data from .env
├── conftest.py             # Shared pytest fixtures
├── requirements.txt
└── .env                    # Local test data (not committed)
```

## Setup

1. **Clone the repository**

   ```powershell
   git clone <your-repo-url>
   cd playwright300
   ```

2. **Create and activate a virtual environment**

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**

   ```powershell
   pip install -r requirements.txt
   playwright install chromium
   ```

4. **Configure environment variables**

   Copy the example file and fill in your test data:

   ```powershell
   copy .env.example .env
   ```

   Required variables:

   | Variable | Description |
   |----------|-------------|
   | `BASE_URL` | Application URL |
   | `PHONE_NUMBER` | Valid phone for login |
   | `INVALID_PHONE_NUMBER` | Invalid phone for negative login test |
   | `FIRST_NAME` | Volunteer first name |
   | `LAST_NAME` | Volunteer last name |
   | `EMAIL_ADDRESS` | Volunteer email |
   | `NEW_PHONE_NUMBER` | Phone for registration flows |
   | `ASSIGNING_INSTITUTION` | Institution for community service |
   | `ORG` | Organization name for donations |

## Running Tests

Run the full suite:

```powershell
pytest -v
```

Run a single test file:

```powershell
pytest tests/test_login_page.py -v
```

Run a single test:

```powershell
pytest tests/test_musician.py::test_musician_sign_up -v
```

On failure, Playwright saves a screenshot under `test-results/` (ignored by Git).

## Test Coverage

| Test File | What It Covers |
|-----------|----------------|
| `test_language.py` | English and Spanish language selection |
| `test_login_page.py` | Valid login and invalid phone error |
| `test_new_login.py` | New volunteer registration and waiver flow |
| `test_community_service.py` | Community service registration end-to-end |
| `test_musician.py` | Musician sign-up flow |
| `test_donations.py` | Donations flow through tax deduction notice |

## Architecture

- **Page Object Model (POM)** — UI interactions live in `pages/`, tests stay focused on behavior and assertions.
- **Fixtures** — `english_app` fixture opens the app and selects English before each test.
- **Externalized test data** — Credentials and form data are loaded from `.env` via `config.py`.
- **Playwright locators** — Uses role-based locators (`get_by_role`, `get_by_text`) for stable selectors.
