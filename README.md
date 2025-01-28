# zoomcamp_dataeng_homework1

## Homework code solutions

### Question 1. Understanding docker first run
```
docker run -it --entrypoint=bash python:3.12.8
```
```
pip --version
```
### Question 2. Understanding Docker networking and docker-compose
No code

### Question 3. Trip Segmentation Count
```
SELECT count(index)
FROM green_tripdata
WHERE 
	lpep_pickup_datetime >= '2019-10-01'::date 
	and lpep_dropoff_datetime < '2019-11-01'::date
	and trip_distance <= 1
;
```
```
SELECT count(index)
FROM green_tripdata
WHERE 
	lpep_pickup_datetime >= '2019-10-01'::date 
	and lpep_dropoff_datetime < '2019-11-01'::date
	and trip_distance > 3 and trip_distance <= 7
;
```
```
SELECT count(index)
FROM green_tripdata
WHERE 
	lpep_pickup_datetime >= '2019-10-01'::date 
	and lpep_dropoff_datetime < '2019-11-01'::date
	and trip_distance > 7 and trip_distance <= 10
;
```
```
SELECT count(index)
FROM green_tripdata
WHERE 
	lpep_pickup_datetime >= '2019-10-01'::date 
	and lpep_dropoff_datetime < '2019-11-01'::date
	and trip_distance > 10
;
```
### Question 4. Longest trip for each day
```
SELECT lpep_dropoff_datetime, trip_distance
FROM green_tripdata
WHERE lpep_pickup_datetime IN ('2019-10-11'::date, '2019-10-24'::date, '2019-10-26'::date, '2019-10-31'::date)
ORDER BY trip_distance DESC
LIMIT 1;
```
### Question 5. Three biggest pickup zones
```
SELECT 
	"Zone",
	SUM(total_amount) as total_amount
FROM 
	green_tripdata trip,
	zones
WHERE 
	trip."PULocationID" = zones."LocationID"
	and lpep_pickup_datetime::date = '2019-10-18'::date
GROUP BY "Zone"
HAVING SUM(total_amount) > 13000
ORDER BY total_amount DESC
;
```

### Question 6. Largest tip
```
SELECT 
	pickup."Zone" as pickup_zone,
	dropoff."Zone" as dropoff_zone,
	tip_amount
FROM 
	green_tripdata trip,
	zones pickup,
	zones dropoff
WHERE 
	trip."PULocationID" = pickup."LocationID" 
	and trip."DOLocationID" = dropoff."LocationID"
	and EXTRACT(MONTH FROM lpep_pickup_datetime) = 10
	and pickup."Zone" = 'East Harlem North'
ORDER BY tip_amount desc;
```

### Question 7. Terraform Workflow

No Code