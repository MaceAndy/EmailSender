## EmailSender 📧

Prosty program w Pythonie z graficznym interfejsem (GUI), który umożliwia wysyłanie spersonalizowanych e-maili do klientów z pliku CSV.

## 🔧 Funkcje

- Wczytywanie pliku `.csv` z danymi klientów (imię, e-mail)
- Wysyłka wiadomości e-mail przez SMTP (np. Gmail)
- Personalizacja treści wiadomości (`{name}` → imię klienta)
- Graficzny interfejs (GUI) w bibliotece `tkinter`

## 📂 Wymagane pliki

- `main.py` – główny plik programu
- `klienci.csv` – plik z kolumnami `Imię` i `Email`

## 🚀 Uruchomienie

1. Upewnij się, że masz zainstalowanego Pythona.
2. Uruchom program:

```bash
python main.py
```

## 🛡️ Bezpieczeństwo

- Użyj **hasła aplikacji** (np. z Gmaila) zamiast swojego prawdziwego hasła.
- Plik CSV nigdy nie trafia do Internetu – wszystko działa lokalnie.

## 📝 Przykład pliku CSV

```csv
Imię,Email
Anna,anna@example.com
Michał,michal@example.com
```

## 📌 Autor

Ten projekt został stworzony do celów edukacyjnych i własnych zastosowań automatyzacyjnych.
