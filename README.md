# Yosemite Campings
Find available Yosemite Campings

### Creating new project
https://docs.djangoproject.com/en/1.8/intro/tutorial01/

## Install python on MacOs
```bash
brew install python3
```

### How to Run

Before run, configure:
```bash
pip3 install -r requirements.txt
source .env.example
```

Then run:
```bash
python3 manage.py runserver
```

### Endpoints
Call endpoint passing the campsite id

Example:
```bash
curl http://127.0.0.1:8000/campsites/232449?start_date=2022-07-01
curl http://127.0.0.1:8000/campsites/232447?start_date=2022-08-01
curl http://127.0.0.1:8000/campsites/232450?start_date=2022-09-01

```

For all campsites on CAMPSITE_ID env var
```bash
curl http://127.0.0.1:8000/campsites?start_date=2022-08-01
```

Some Campings
| id | name | url|
|---|---|---|
|232447 | Upper Pines Campground | https://www.recreation.gov/camping/campgrounds/10004152
|232450 | Lower Pines Campground |  https://www.recreation.gov/camping/campgrounds/232450
| 232449 | North Pines Campground |  https://www.recreation.gov/camping/campgrounds/232449


______
Copyright Daniele Boscolo.
