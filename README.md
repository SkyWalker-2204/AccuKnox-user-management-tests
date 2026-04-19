# AccuKnox QA Trainee Practical Assessment

## 📋 Project Overview
End-to-End User Management automation for OrangeHRM using Playwright and Python with Page Object Model (POM).

| Detail | Value |
|--------|-------|
| **Application Under Test** 
|https://opensource-demo.orangehrmlive.com/ |
| **Username** | Admin |
| **Password** | admin123 |
| **Test Framework** | Pytest + Playwright |
| **Design Pattern** | Page Object Model (POM) |
| **Language** | Python 3.11.9 |
| **Browser** | Chromium 120.0.6099.28 |

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.11.9 | Programming Language |
| Playwright | 1.40.0 | Browser Automation |
| Pytest | 7.4.4 | Test Framework |
| pytest-playwright | 0.4.3 | Playwright + Pytest Integration |
| pytest-base-url | 2.1.0 | Base URL Management |

---

## 📁 Project Structure

```
AccuKnox-user-management-tests/
│
├── 📂 pages/                      # Page Object Model Classes
│   ├── __init__.py               # Package initializer
│   ├── login_page.py             # Login page actions & locators
│   └── admin_page.py             # Admin/User Management actions
│
├── 📂 tests/                      # Test Cases
│   ├── __init__.py               # Package initializer
│   └── test_user.py              # E2E User CRUD test cases
│
├── 📂 utils/                      # Utility/Helper Classes
│   ├── __init__.py               # Package initializer
│   └── test_reporter.py          # QA Test Report Generator
│
├── 📂 reports/                    # Auto-generated Test Reports
│   ├── test_report.html          # HTML format report
│   └── test_report.json          # JSON format report
│
├── 📄 conftest.py                # Pytest fixtures & configuration
├── 📄 pytest.ini                 # Pytest settings
├── 📄 requirements.txt           # Python dependencies
├── 📄 .gitignore                 # Git ignore rules
└── 📄 README.md                  # This file
```

---

## 🚀 Setup Instructions

### Prerequisites
- Python 3.11+ installed
- Git installed (optional, for clone)
- Internet connection (for OrangeHRM demo site)

### Step 1: Clone Repository
```bash
git clone https://github.com/SkyWalker-2204/AccuKnox-user-management-tests.git
cd AccuKnox-user-management-tests
```

**OR** Download ZIP from GitHub and extract.

### Step 2: Create Virtual Environment

**Windows (PowerShell/CMD):**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux (Terminal):**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Install Playwright Browsers
```bash
playwright install chromium
```

### Step 5: Verify Installation
```bash
pytest --version
playwright --version
```

**Expected Output:**
```
pytest 7.4.4
Version 1.40.0
```

---

## ▶️ How to Run Tests

### 🎯 Run All Tests (Headed Mode - See Browser Action) ✅ Recommended
```bash
pytest tests/test_user.py -v -s --headed
```

### 🎯 Run All Tests (Headless Mode - Background)
```bash
pytest tests/test_user.py -v -s
```

### 🎯 Run with Slow Motion (Debugging - Watch Each Step)
```bash
pytest tests/test_user.py -v -s --headed --slowmo=1000
```

### 🎯 Run with Different Browsers
```bash
# Firefox
pytest tests/test_user.py --browser=firefox --headed

# WebKit (Safari engine)
pytest tests/test_user.py --browser=webkit --headed

# Chromium (default)
pytest tests/test_user.py --browser=chromium --headed
```

### 🎯 Run Single Test Method
```bash
pytest tests/test_user.py::TestUserManagement::test_complete_qa_flow -v -s --headed
```

### 🎯 Quick One-Command Setup + Run (Windows)
```bash
python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt && playwright install chromium && pytest tests/test_user.py -v -s --headed
```





## 📊 Sample Test Execution Output

```
============================================= test session starts ==============================================
platform win32 -- Python 3.11.9, pytest-7.4.4, pluggy-1.6.0
rootdir: C:\Users\shika\AccuKnox-user-management-tests
configfile: pytest.ini
plugins: base-url-2.1.0, playwright-0.4.3
collected 1 item

tests/test_user.py::TestUserManagement::test_complete_qa_flow[chromium] 
✅ Login successful

🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪
QA TEST EXECUTION STARTED
🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪🧪

[STEP 1] Navigating to Admin page...
Navigating to Admin...
✅ Admin page loaded

[STEP 2] Creating new user: qauser_1776503207
Adding user...
Employee selected ✅
✅ Success toast detected
User created ✅

[STEP 3] Search & Verify created user
🔍 Searching user: qauser_1776503207...
Reset clicked
✅ Username 'qauser_1776503207' entered
✅ Search button clicked
🔍 Search executed for: qauser_1776503207

============================================================
🔎 QA VERIFICATION: Checking if user 'qauser_1776503207' exists
============================================================
ℹ️ INFO: User 'qauser_1776503207' found in row 1
✅✅✅ PASS: User 'qauser_1776503207' FOUND successfully!
============================================================

[STEP 4] Edit user

============================================================
✏️ QA EDIT: Updating user 'qauser_1776503207'
============================================================
🔍 Step 1: Searching user before edit...
User found in row 1
✏️ Step 2: Clicking pencil/edit icon...
✅ Pencil icon clicked for row 1
✅ Edit form loaded
📝 Step 3: Changing status to 'Enabled'...
✅ Status updated
💾 Step 4: Saving changes...
✅✅✅ User 'qauser_1776503207' updated successfully!
============================================================

[STEP 5] Search after edit
✅✅✅ PASS: User 'qauser_1776503207' FOUND successfully!

[STEP 6] Delete user

============================================================
🗑️ QA DELETE: Removing user 'qauser_1776503207'
============================================================
🔍 Step 1: Searching user before delete...
User found in row 1
🗑️ Step 2: Clicking dustbin/delete icon...
✅ Dustbin icon clicked for row 1
⚠️ Step 3: Confirmation popup appeared
👉 Clicking 'Yes, Delete' button...
✅✅✅ User 'qauser_1776503207' deleted successfully!
============================================================

[STEP 7] Verify deletion
🔍 Searching user: qauser_1776503207...

============================================================
🔎 QA VERIFICATION: Checking if user 'qauser_1776503207' exists
============================================================
ℹ️ INFO: Table body not found
✅✅✅ PASS: User 'qauser_1776503207' NOT FOUND (Deleted successfully)!
============================================================

🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉
🎉 ALL QA TESTS PASSED! 🎉
🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉

PASSED
======================================== 1 passed in 105.30s =========================================
```




## 📋 Requirements.txt

```
pytest==7.4.4
playwright==1.40.0
pytest-playwright==0.4.3
pytest-base-url==2.1.0
```



## 📄 pytest.ini Configuration

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v -s --tb=short
timeout = 300
```



**🎉 Status: COMPLETE - Ready for Review! 🎉**

