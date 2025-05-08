# ServiceDesk API (Django REST Framework)

Projekt na zaliczenie przedmiotu Aplikacje WWW w ramach studiów podyplomowych Informatyka Stosowana na UWM.
Prosty system zarządzania zgłoszeniami serwisowymi typu ServiceDesk, zbudowany w Django + DRF.

## Funkcje
- Rejestracja i logowanie z tokenem (Token Auth)
- Tworzenie zgłoszeń (ticketów)
- Kategorie zgłoszeń
- Komentarze i załączniki
- Statystyki zgłoszeń (statusy)
- Panel admina Django

## Technologie
- Python 3.11.6
- Django
- Django REST Framework
- Token Authentication
- SQLite3

## 🛠 Uruchomienie lokalnie

```bash
git clone https://github.com/adamsiehen/rejestrator_zadan.git
cd rejestrator_zadan
python -m venv venv
#Windows: venv\Scripts\activate  # Linux/Mac: source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
