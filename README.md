# Spendly — Personal Finance Tracker

Spendly is a lightweight, modern web application built with Flask to help users log expenses, monitor their budgets, and understand spending patterns.

---

## 🛠️ Technology Stack

* **Backend:** [Flask](https://flask.palletsprojects.com/) (Python)
* **Frontend:** HTML5, Vanilla CSS (with Google Fonts: Outfit, DM Sans, DM Serif Display)
* **Testing:** [pytest](https://docs.pytest.org/) & `pytest-flask`

---

## 📁 Project Structure

Here is the directory layout of the application:

* **[app.py](file:///C:/Users/hp/Downloads/expense-tracker/expense-tracker/app.py):** Main application entrypoint containing the routing logic.
* **`templates/`:** HTML templates extending a common base layout:
  * **[base.html](file:///C:/Users/hp/Downloads/expense-tracker/expense-tracker/templates/base.html):** The master template containing the navigation bar and footer.
  * **[landing.html](file:///C:/Users/hp/Downloads/expense-tracker/expense-tracker/templates/landing.html):** The landing page showing features and mock statistics.
  * **[privacy_policy.html](file:///C:/Users/hp/Downloads/expense-tracker/expense-tracker/templates/privacy_policy.html):** Privacy Policy details page.
  * **[terms_and_conditions.html](file:///C:/Users/hp/Downloads/expense-tracker/expense-tracker/templates/terms_and_conditions.html):** Terms and Conditions details page.
  * **[login.html](file:///C:/Users/hp/Downloads/expense-tracker/expense-tracker/templates/login.html) / [register.html](file:///C:/Users/hp/Downloads/expense-tracker/expense-tracker/templates/register.html):** Authentication views.
* **`static/`:** Contains static files:
  * **[style.css](file:///C:/Users/hp/Downloads/expense-tracker/expense-tracker/static/css/style.css):** Custom styling rules for layouts, legal sections, features, and responsive adjustments.
* **[test_app.py](file:///C:/Users/hp/Downloads/expense-tracker/expense-tracker/test_app.py):** Automated testing suite verifying routes and footer links.
* **[requirements.txt](file:///C:/Users/hp/Downloads/expense-tracker/expense-tracker/requirements.txt):** Core dependencies required by the project.

---

## 🚀 Getting Started

### 1. Set Up Environment
It is recommended to run the app using a Python virtual environment:
```bash
# Create a virtual environment
python -m venv venv

# Activate it (Windows)
.\venv\Scripts\activate
```

### 2. Install Dependencies
Install all package requirements:
```bash
pip install -r requirements.txt
```

### 3. Run the Development Server
Start the Flask application:
```bash
python app.py
```
Open [http://127.0.0.1:5001](http://127.0.0.1:5001) in your browser to view the site.

---

## 🧪 Testing

We use `pytest` to ensure all pages render correctly and footer links are active. To run tests:

```bash
pytest
```
