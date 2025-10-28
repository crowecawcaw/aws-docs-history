# Filter arrays using `UNNEST`

To filter an array that includes a nested structure by one of its child elements,
issue a query with an `UNNEST` operator. For more information about
`UNNEST`, see [Flattening Nested
Arrays](flattening-arrays.md "flattening-arrays.md").

For example, this query finds host names of sites in the dataset.

```
WITH dataset AS (
  SELECT ARRAY[
    CAST(
      ROW('aws.amazon.com', ROW(true)) AS ROW(hostname VARCHAR, flaggedActivity ROW(isNew BOOLEAN))
    ),
    CAST(
      ROW('news.cnn.com', ROW(false)) AS ROW(hostname VARCHAR, flaggedActivity ROW(isNew BOOLEAN))
    ),
    CAST(
      ROW('netflix.com', ROW(false)) AS ROW(hostname VARCHAR, flaggedActivity ROW(isNew BOOLEAN))
    )
  ] as items
)
SELECT sites.hostname, sites.flaggedActivity.isNew
FROM dataset, UNNEST(items) t(sites)
WHERE sites.flaggedActivity.isNew = true
```

It returns:

````
+------------------------+
| hostname       | isnew | +------------------------+
| aws.amazon.com | true  | +------------------------+ ```
````
