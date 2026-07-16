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
chosen300-playwright-tests/
├── pages/                      # Page Object Model classes
│   ├── base_page.py
│   ├── lang_page.py
│   ├── login_page.py
│   ├── new_login.py
│   ├── community_service_page.py
│   ├── musician_page.py
│   └── donations.py
├── tests/                      # Test suites
│   ├── test_language.py
│   ├── test_login_page.py
│   ├── test_new_login.py
│   ├── test_community_service.py
│   ├── test_musician.py
│   └── test_donations.py
├── test_data/                  # UI constants and selectable options
│   ├── volunteer_data.py
│   ├── community_data.py
│   ├── musician_data.py
│   └── donations_data.py
├── config.py                   # Loads secrets/form data from .env
├── conftest.py                 # Shared pytest fixtures
├── pytest.ini                  # Pytest defaults (verbose + screenshots)
├── requirements.txt
├── .env.example                # Template for local env vars
└── .env                        # Local test data (not committed)
```

## Setup

1. **Clone the repository**

   ```powershell
   git clone https://github.com/sphilmore/chosen300-playwright-tests.git
   cd chosen300-playwright-tests
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

`pytest.ini` already sets `-v` and `--screenshot=only-on-failure`, so you can run:

```powershell
pytest
```

Run a single test file:

```powershell
pytest tests/test_login_page.py
```

Run a single test:

```powershell
pytest tests/test_musician.py::test_musician_sign_up
```

Run headed (see the browser):

```powershell
pytest --headed
```

On failure, Playwright saves a screenshot under `test-results/` (ignored by Git).

## Test Coverage

| Test File | What It Covers |
|-----------|----------------|
| `test_language.py` | English and Spanish language selection |
| `test_login_page.py` | Valid login and invalid phone error |
| `test_new_login.py` | New volunteer registration, waiver flow, and missing-field validation |
| `test_community_service.py` | Community service registration end-to-end |
| `test_musician.py` | Musician sign-up flow |
| `test_donations.py` | Donations flow through tax deduction notice |

## Architecture

- **Page Object Model (POM)** — UI interactions live in `pages/`; tests focus on flow and assertions.
- **Fixtures** — `english_app` uses pytest-playwright’s `page` fixture, opens the app, and selects English.
- **Env-driven secrets** — Credentials and personal form data come from `.env` via `config.py`.
- **Test data constants** — Selectable UI values (instruments, sites, service reasons, donation categories) live in `test_data/`.
- **Parameterized page methods** — Tests pass scenario data into page methods (for example `select_instrument(DRUMS)`).
- **Role-based locators** — Uses Playwright locators like `get_by_role` and `get_by_text` for stable selectors.
- **Failure screenshots** — Configured in `pytest.ini` with `--screenshot=only-on-failure`.
