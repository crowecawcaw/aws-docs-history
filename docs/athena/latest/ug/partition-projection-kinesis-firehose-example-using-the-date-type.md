# How

to use the `date` type

When you use the `date` type for a projected partition key, you must
specify a range. Because you have no data for dates before the Firehose delivery stream was
created, you can use the date of creation as the start. And because you do not have data
for dates in the future, you can use the special token `NOW` as the
end.

In the `CREATE TABLE` example, the start date is specified as January 1,
2021 at midnight UTC.

###### Note

Configure a range that matches your data as closely as possible so that Athena
looks only for existing partitions.

When a query is run on the sample table, Athena uses the conditions on the
`datehour` partition key in combination with the range to generate
values. Consider the following query:

```
SELECT *
FROM my_ingested_data
WHERE datehour >= '2020/12/15/00'
AND datehour < '2021/02/03/15'
```

The first condition in the `SELECT` query uses a date that is before the
start of the date range specified by the `CREATE TABLE` statement. Because
the partition projection configuration specifies no partitions for dates before January
1, 2021, Athena looks for data only in the following locations, and ignores the earlier
dates in the query.

```
s3://amzn-s3-demo-bucket/prefix/2021/01/01/00/
s3://amzn-s3-demo-bucket/prefix/2021/01/01/01/
s3://amzn-s3-demo-bucket/prefix/2021/01/01/02/
...
s3://amzn-s3-demo-bucket/prefix/2021/02/03/12/
s3://amzn-s3-demo-bucket/prefix/2021/02/03/13/
s3://amzn-s3-demo-bucket/prefix/2021/02/03/14/
```

Similarly, if the query ran at a date and time before February 3, 2021 at 15:00, the
last partition would reflect the current date and time, not the date and time in the
query condition.

If you want to query for the most recent data, you can take advantage of the fact that
Athena does not generate future dates and specify only a beginning `datehour`,
as in the following example.

```
SELECT *
FROM my_ingested_data
WHERE datehour >= '2021/11/09/00'
```
