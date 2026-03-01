# Query W3C extended log file format

The [W3C
extended](https://docs.microsoft.com/en-us/windows/win32/http/w3c-logging "https://docs.microsoft.com/en-us/windows/win32/http/w3c-logging") log file data format has space-separated fields. The fields that
appear in W3C extended logs are determined by a web server administrator who chooses
which log fields to include. The following example log data has the fields `date,
 time`, `c-ip`, `s-ip`, `cs-method`,
`cs-uri-stem`, `sc-status`, `sc-bytes`,
`cs-bytes`, `time-taken`, and `cs-version`.

```
2020-01-19 22:48:39 203.0.113.5 198.51.100.2 GET /default.html 200 540 524 157 HTTP/1.0
2020-01-19 22:49:40 203.0.113.10 198.51.100.12 GET /index.html 200 420 324 164 HTTP/1.0
2020-01-19 22:50:12 203.0.113.12 198.51.100.4 GET /image.gif 200 324 320 358 HTTP/1.0
2020-01-19 22:51:44 203.0.113.15 198.51.100.16 GET /faq.html 200 330 324 288 HTTP/1.0
```

## Create a table in Athena for W3C extended logs

Before you can query your W3C extended logs, you must create a table schema so
that Athena can read the log data.

###### To create a table in Athena for W3C extended logs

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. Paste a DDL statement like the following into the Athena console, noting
   the following points:
   1. Add or remove the columns in the example to correspond to the
      fields in the logs that you want to query.
   2. Column names in the W3C extended log file format contain hyphens
      (`-`). However, in accordance with [Athena naming
      conventions](tables-databases-columns-names.md "tables-databases-columns-names.md"), the example `CREATE TABLE`
      statement replaces them with underscores (`_`).
   3. To specify the space delimiter, use `FIELDS TERMINATED BY '
'`.
   4. Modify the values in `LOCATION
's3://amzn-s3-demo-bucket/`w3c-log-folder`/'`
      to point to your W3C extended logs in Amazon S3.

```
CREATE EXTERNAL TABLE `iis_w3c_logs`(
  date_col string,
  time_col string,
  c_ip string,
  s_ip string,
  cs_method string,
  cs_uri_stem string,
  sc_status string,
  sc_bytes string,
  cs_bytes string,
  time_taken string,
  cs_version string
  )
ROW FORMAT DELIMITED
  FIELDS TERMINATED BY ' '
STORED AS INPUTFORMAT
  'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION   's3://amzn-s3-demo-bucket/`w3c-log-folder`/'
```

3. Run the query in the Athena console to register the
   `iis_w3c_logs` table. When the query completes, the logs are
   ready for you to query from Athena.

## Example W3C extended log select query

The following example query selects the date, time, request target, and time taken
for the request from the table `iis_w3c_logs`. The `WHERE`
clause filters for cases in which the HTTP method is `GET` and the HTTP
status code is `200` (successful).

```
SELECT date_col, time_col, cs_uri_stem, time_taken
FROM iis_w3c_logs
WHERE cs_method = 'GET' AND sc_status = '200'
```

The following image shows the results of the query in the Athena Query
Editor.

![Example query results in Athena of W3C extended log files stored in Amazon S3.](images/querying-iis-logs-1.png)

## Combine the date and time fields

The space delimited `date` and `time` fields are separate
entries in the log source data, but you can combine them into a timestamp if you
want. Use the [concat()](https://prestodb.io/docs/current/functions/string.html#concat "https://prestodb.io/docs/current/functions/string.html#concat") and [date_parse()](https://prestodb.io/docs/current/functions/datetime.html#date_parse "https://prestodb.io/docs/current/functions/datetime.html#date_parse") functions in a [SELECT](select.md "select.md") or [CREATE TABLE AS SELECT](create-table-as.md "create-table-as.md") query to
concatenate and convert the date and time columns into timestamp format. The
following example uses a CTAS query to create a new table with a
`derived_timestamp` column.

```
CREATE TABLE iis_w3c_logs_w_timestamp AS
SELECT
  date_parse(concat(date_col,' ', time_col),'%Y-%m-%d %H:%i:%s') as derived_timestamp,
  c_ip,
  s_ip,
  cs_method,
  cs_uri_stem,
  sc_status,
  sc_bytes,
  cs_bytes,
  time_taken,
  cs_version
FROM iis_w3c_logs
```

After the table is created, you can query the new timestamp column directly, as in
the following example.

```
SELECT derived_timestamp, cs_uri_stem, time_taken
FROM iis_w3c_logs_w_timestamp
WHERE cs_method = 'GET' AND sc_status = '200'
```

The following image shows the results of the query.

![W3C extended log file query results on an table with a derived timestamp column.](images/querying-iis-logs-1a.png)
