# 📧 Bulk Email Automation using Python

This project is a Python-based automation tool for sending personalized emails in bulk using a CSV file. It supports attachments, batching, and delay mechanisms to ensure safe email delivery.

---

## 🚀 Features

- Send personalized emails using CSV data
- Attach files (e.g., resume)
- Batch sending to avoid spam detection
- Random delay between emails
- Error handling for failed emails

---

## 📂 Project Structure
├── send_emails.py
├── sample_contacts.csv
├── sample_resume.pdf
└── README.md


---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Suraj2429/bulk-email-automation-python.git
cd bulk-email-automation-python
```


### 2. Install Dependencies
``` bash
pip install pandas
```


### 3. Enable Gmail App Password
-Go to: https://myaccount.google.com/apppasswords
-Generate App Password
-Replace in code


###4. Update Configuration
EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_app_password"


### 5. Run Script
```bash
python send_emails.py
```
