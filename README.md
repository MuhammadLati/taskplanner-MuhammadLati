# Tilavarausjärjestelmä

Django-pohjainen tilavarausjärjestelmä oppilaitoksille.

## Ominaisuudet

- Tilojen selaus ja haku
- Varausten tekeminen ja peruminen
- Kalenterinäkymä varauksille
- Käyttäjähallinta ja kirjautuminen
- Responsiivinen käyttöliittymä

## Asennus

1. Kloonaa repositorio:
```bash
git clone <repository-url>
cd tilavarausjarjestelma
```

2. Luo virtuaaliympäristö ja aktivoi se:
```bash
python -m venv venv
source venv/bin/activate  # Unix
venv\Scripts\activate  # Windows
```

3. Asenna riippuvuudet:
```bash
pip install -r requirements.txt
```

4. Suorita migraatiot:
```bash
python manage.py migrate
```

5. Luo pääkäyttäjä:
```bash
python manage.py createsuperuser
```

6. Käynnistä kehityspalvelin:
```bash
python manage.py runserver
```

## Käyttö

1. Kirjaudu sisään admin-paneeliin: `http://localhost:8000/admin/`
2. Lisää tiloja järjestelmään
3. Käyttäjät voivat selata tiloja ja tehdä varauksia

## Teknologiat

- Django 5.1.6
- Bootstrap 5.3
- SQLite (kehitys) / PostgreSQL (tuotanto) 