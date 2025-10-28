# Example queries

## Metadata filtering

The following example is for metadata filtering with a `SELECT` statement
with the AWS IoT SiteWise query language:

```
SELECT a.asset_name, p.property_name
FROM asset a, asset_property p
WHERE a.asset_name LIKE '`Windmill%`'

```

## Value filtering

The following is an example of value filtering using a `SELECT` statement
with the AWS IoT SiteWise query language:

```
SELECT a.asset_name, r.int_value
FROM asset a, raw_time_series r
WHERE r.int_value > 30
AND r.event_timestamp > TIMESTAMP '`2022-01-05 12:15:00`'
AND r.event_timestamp < TIMESTAMP '`2022-01-05 12:20:00`'

```
