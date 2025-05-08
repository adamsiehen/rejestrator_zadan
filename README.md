# rejestrator_zadan (Django REST Framework)

Projekt na zaliczenie przedmiotu Aplikacje WWW w ramach studiów podyplomowych Informatyka Stosowana na UWM.

Prosty system zarządzania zgłoszeniami serwisowymi typu ServiceDesk, zbudowany w Django.

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
```

## Opis działania aplikacji
Aplikacja składa się z 4 modeli:

Categorys,

Tickets,

Comments,

Ticket attachments


oraz modeli users i groups

Aby móc dodać ticket, muszą być wcześniej skonfigurowane kategorie (Categorys) inaczej aplikacja zwróci błąd.

Screeny z aplikacji:
### Model users
![image](https://github.com/user-attachments/assets/9c8da69f-25ee-47d7-bbd0-6f3f110776d6)

### Model groups:
![image](https://github.com/user-attachments/assets/378d4f71-f969-4220-a752-8e1047c37db6)

### Model categorys:
![image](https://github.com/user-attachments/assets/2940a04d-cb9c-4c68-86b0-7b7a52117dcb)
![image](https://github.com/user-attachments/assets/6607960c-950f-434c-bf2b-e3adf5c16475)

### Model Tickets:
![image](https://github.com/user-attachments/assets/77d900f3-5b48-411e-acc4-ac13a45a6ec5)
![image](https://github.com/user-attachments/assets/91fa11da-c498-40fb-a564-19ed23d608b2)

### Model Comments:
![image](https://github.com/user-attachments/assets/74cb69c7-96a3-4d45-8c1f-c916cce11475)

### Model Ticket attachments:
![image](https://github.com/user-attachments/assets/f7eb0ec6-fcaa-44ec-b582-2906a05626d9)
![image](https://github.com/user-attachments/assets/e01e2d1b-18f0-4a38-bba4-447a0bd667ea)
![image](https://github.com/user-attachments/assets/8ff76d1e-0c03-463d-84bf-6f19516c5e18)

## Użycie REST API

Link do kolekcji postman: https://github.com/adamsiehen/rejestrator_zadan/blob/main/rejestrator_zadan%20API.postman_collection.json

### Rejestracja użytkownika

#### Metoda POST
```rest
http://127.0.0.1:8000/api/register/
```

#### Body
```rest
{
  "username": "ania",
  "email": "ania@example.com",
  "password": "haslo123"
}
```
Przykładowy response:
```rest
{
    "token": "9d0c887f78aed37249bd77be3bb3b4c66fcac429"
}
```
![image](https://github.com/user-attachments/assets/0a6bafcb-14d1-44c7-8e48-42b9d7a8ef14)

### Logowanie

#### Metoda POST
```rest
http://127.0.0.1:8000/api/login/
```

#### Body
```rest
{"username": "ania", "password": "haslo123"}
```
Przykładowy response:
```rest
{
    "token": "9d0c887f78aed37249bd77be3bb3b4c66fcac429"
}
```
![image](https://github.com/user-attachments/assets/21e30211-dfbd-422f-881a-3552833c4307)

### Tworzenie zgłoszenia (ticketu)

#### Metoda POST
```rest
http://127.0.0.1:8000/api/tickets/
```

#### Header
Wymagane jest uzupełnienie tokenu w polu Authorization w nagłówku zapytania (Header)
![image](https://github.com/user-attachments/assets/5f02c356-b0fd-44f0-afc5-19ff3a51769d)


#### Body
```rest
{"title": "Przykładowy tytuł", "description": "Przykładowy opis", "status": "new", "category": 2}
```
Przykładowy response:
```rest
{
    "id": 4,
    "title": "Przykładowy tytuł",
    "description": "Przykładowy opis",
    "status": "new",
    "created_at": "2025-05-08T19:41:51.301345Z",
    "updated_at": "2025-05-08T19:41:51.301345Z",
    "category": 2,
    "created_by": {
        "id": 3,
        "username": "ania",
        "email": "ania@example.com"
    },
    "assigned_to": null,
    "comments": [],
    "attachments": []
}
```
![image](https://github.com/user-attachments/assets/bd4eb55a-eb81-4c3b-9241-f11751d517d8)

### Wyszukanie zgłoszeń od użytkownika

#### Metoda GET
```rest
http://127.0.0.1:8000/api/tickets/user/
```

#### Header
Wymagane jest uzupełnienie tokenu w polu Authorization w nagłówku zapytania (Header)
![image](https://github.com/user-attachments/assets/33135123-a49e-49fa-bb21-caaaa5cff588)


Przykładowy response:
```rest
[
    {
        "id": 2,
        "title": "Ania pozdrawia",
        "description": "Wszystko działa Ania pozdrawia :)",
        "status": "in_progress",
        "created_at": "2025-05-08T19:19:32.679046Z",
        "updated_at": "2025-05-08T19:19:48.581999Z",
        "category": 2,
        "created_by": {
            "id": 3,
            "username": "ania",
            "email": "ania@example.com"
        },
        "assigned_to": null,
        "comments": [],
        "attachments": [
            {
                "id": 2,
                "file": "http://127.0.0.1:8000/attachments/test.txt",
                "uploaded_at": "2025-05-08T19:34:05.893154Z"
            }
        ]
    },
    {
        "id": 3,
        "title": "Ania pozdrawia2",
        "description": "Wszystko działa Ania pozdrawia :)2",
        "status": "new",
        "created_at": "2025-05-08T19:20:41.599023Z",
        "updated_at": "2025-05-08T19:20:41.599023Z",
        "category": 2,
        "created_by": {
            "id": 3,
            "username": "ania",
            "email": "ania@example.com"
        },
        "assigned_to": null,
        "comments": [],
        "attachments": []
    },
    {
        "id": 4,
        "title": "Przykładowy tytuł",
        "description": "Przykładowy opis",
        "status": "new",
        "created_at": "2025-05-08T19:41:51.301345Z",
        "updated_at": "2025-05-08T19:41:51.301345Z",
        "category": 2,
        "created_by": {
            "id": 3,
            "username": "ania",
            "email": "ania@example.com"
        },
        "assigned_to": null,
        "comments": [],
        "attachments": []
    }
]
```
![image](https://github.com/user-attachments/assets/f62c4744-2f34-4845-85e7-07ffba4e0bb9)


### Statystyki zgłoszeń

#### Metoda GET
```rest
http://127.0.0.1:8000/api/tickets/stats
```

#### Header
Wymagane jest uzupełnienie tokenu w polu Authorization w nagłówku zapytania (Header)
![image](https://github.com/user-attachments/assets/da757307-a5d3-420a-baa4-f430cb7f603b)

Przykładowy response:
```rest
{
    "new": 2,
    "in_progress": 1,
    "resolved": 1,
    "closed": 0
}
```
![image](https://github.com/user-attachments/assets/7e188788-a401-4651-aab2-28986121e540)














