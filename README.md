# Yosemite Campings
Find available Yosemite Campings

### Creating new project
https://docs.djangoproject.com/en/1.8/intro/tutorial01/


### How to Run
```python
python3 manage.py runserver
```

### Endpoints
Call endpoint passing the campsite id

Example:
```
curl http://127.0.0.1:8000/campsites/232449
curl http://127.0.0.1:8000/campsites/232447
curl http://127.0.0.1:8000/campsites/232450

```

For all campsites on CAMPSITE_ID env var
```
curl http://127.0.0.1:8000/campsites
```

Some Campings
| id | name | url|
|---|---|---|
|232447 | Upper Pines Campground | https://www.recreation.gov/camping/campgrounds/10004152
|232450 | Lower Pines Campground |  https://www.recreation.gov/camping/campgrounds/232450
| 232449 | North Pines Campground |  https://www.recreation.gov/camping/campgrounds/232449


______
Copyright Daniele Boscolo.