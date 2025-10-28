For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Subquery support

Timestream supports subqueries in `EXISTS` and `IN` predicates. The
`EXISTS` predicate determines if a subquery returns any rows. The `IN`
predicate determines if values produced by the subquery match the values or expression of in IN
clause. The Timestream query language supports correlated and other subqueries.

```
SELECT t.c1
FROM (VALUES 1, 2, 3, 4, 5) AS t(c1)
WHERE EXISTS
(SELECT t.c2
 FROM (VALUES 1, 2, 3) AS t(c2)
 WHERE t.c1= t.c2
)
ORDER BY t.c1
```

| c1  |
| --- | ---------------------------------------------------------------------------------------------------------------------------- |
| 1   |
| 2   |
| 3   | `SELECT t.c1 FROM (VALUES 1, 2, 3, 4, 5) AS t(c1) WHERE t.c1 IN (SELECT t.c2 FROM (VALUES 2, 3, 4) AS t(c2) ) ORDER BY t.c1` |
| c1  |
| --- |
| 2   |
| 3   |
| 4   |
