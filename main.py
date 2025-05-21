import csv
import smtplib
import tkinter as tk
from tkinter import filedialog, messagebox
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587


def send_emails():
    email_login = entry_email.get()
    email_password = entry_password.get()
    subject = entry_subject.get()
    message_template = text_body.get("1.0", tk.END)

    try:
        with open(csv_path.get(), newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['Imię']
                to_email = row['Email']

                msg = MIMEMultipart()
                msg['From'] = email_login
                msg['To'] = to_email
                msg['Subject'] = subject

                body = message_template.format(name=name)
                msg.attach(MIMEText(body, 'plain'))

                with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                    server.starttls()
                    server.login(email_login, email_password)
                    server.sendmail(email_login, to_email, msg.as_string())
        messagebox.showinfo("Sukces", "Wiadomości wysłane pomyślnie!")
    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił błąd: {e}")


def choose_file():
    file = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    csv_path.set(file)



root = tk.Tk()
root.title("Wysyłka e-maili z CSV")
root.geometry("500x600")

csv_path = tk.StringVar()

tk.Label(root, text="Twój adres e-mail (np. Gmail):").pack()
entry_email = tk.Entry(root, width=50)
entry_email.pack()

tk.Label(root, text="Hasło aplikacji:").pack()
entry_password = tk.Entry(root, width=50, show="*")
entry_password.pack()

tk.Label(root, text="Temat wiadomości:").pack()
entry_subject = tk.Entry(root, width=50)
entry_subject.pack()

tk.Label(root, text="Treść wiadomości (użyj {name} aby wstawić imię):").pack()
text_body = tk.Text(root, height=10, width=60)
text_body.pack()

tk.Label(root, text="Plik CSV:").pack()
tk.Entry(root, textvariable=csv_path, width=40).pack(side=tk.LEFT, padx=10)
tk.Button(root, text="Wybierz plik", command=choose_file).pack(side=tk.LEFT)

tk.Button(root, text="Wyślij maile", command=send_emails, bg="green", fg="white").pack(pady=20)

root.mainloop()
