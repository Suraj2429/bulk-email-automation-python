import smtplib
import pandas as pd
import time
import random
from email.message import EmailMessage

EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_app_password"
CSV_FILE = "sample_contacts.csv"
RESUME_PATH = "sample_resume.pdf"

BATCH_SIZE = 50
DELAY_MIN = 8
DELAY_MAX = 15

df = pd.read_csv(CSV_FILE)
df.columns = df.columns.str.strip()
df = df.dropna(subset=["Name", "Email"])
df = df[df["Email"].str.contains("@", na=False)]

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(EMAIL, APP_PASSWORD)

sent_count = 0

for index, row in df.iterrows():
    if sent_count >= BATCH_SIZE:
        break

    try:
        name = str(row["Name"]).strip()
        to_email = str(row["Email"]).strip()

        msg = EmailMessage()
        msg["From"] = EMAIL
        msg["To"] = to_email
        msg["Subject"] = "Opportunity Inquiry"

        body = f"""Dear {name},

I hope this message finds you well.

I am reaching out to explore potential opportunities within your organization. I have experience in backend development and DevOps practices, including Docker, CI/CD pipelines, and cloud fundamentals.

I would appreciate any guidance or opportunities that match my profile.

Thank you for your time and consideration.

Best regards,  
Your Name  
your_email@gmail.com
"""

        msg.set_content(body)

        with open(RESUME_PATH, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="pdf",
                filename="resume.pdf"
            )

        server.send_message(msg)
        sent_count += 1
        print(f"Sent {sent_count}: {to_email}")

        time.sleep(random.randint(DELAY_MIN, DELAY_MAX))

    except Exception as e:
        print(f"Failed: {to_email} | {e}")

server.quit()
print(f"Done. Total sent: {sent_count}")