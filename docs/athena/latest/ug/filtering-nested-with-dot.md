# Filter arrays with nested values

Large arrays often contain nested structures, and you need to be able to filter, or
search, for values within them.

To define a dataset for an array of values that includes a nested `BOOLEAN`
value, issue this query:

```
WITH dataset AS (
  SELECT
    CAST(
      ROW('aws.amazon.com', ROW(true)) AS ROW(hostname VARCHAR, flaggedActivity ROW(isNew BOOLEAN))
    ) AS sites
)
SELECT * FROM dataset
```

It returns this result:

```
+----------------------------------------------------------+
| sites                                                    |
+----------------------------------------------------------+
| {HOSTNAME=aws.amazon.com, FLAGGEDACTIVITY={ISNEW=true}}  |
+----------------------------------------------------------+
```

Next, to filter and access the `BOOLEAN` value of that element, continue to
use the dot `.` notation.

```
WITH dataset AS (
  SELECT
    CAST(
      ROW('aws.amazon.com', ROW(true)) AS ROW(hostname VARCHAR, flaggedActivity ROW(isNew BOOLEAN))
    ) AS sites
)
SELECT sites.hostname, sites.flaggedactivity.isnew
FROM dataset
```

This query selects the nested fields and returns this result:

```
+------------------------+
| hostname       | isnew |
+------------------------+
| aws.amazon.com | true  |
+------------------------+
```
