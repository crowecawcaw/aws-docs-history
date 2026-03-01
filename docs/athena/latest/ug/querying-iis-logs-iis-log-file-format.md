# Query IIS log file format

Unlike the W3C extended format, the [IIS log file format](<https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc728311(v%3dws.10)> "https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc728311(v%3dws.10)") has a fixed set of fields and includes a comma as a
delimiter. The LazySimpleSerDe treats the comma as the delimiter and the space after the
comma as the beginning of the next field.

The following example shows sample data in the IIS log file format.

```
203.0.113.15, -, 2020-02-24, 22:48:38, W3SVC2, SERVER5, 198.51.100.4, 254, 501, 488, 200, 0, GET, /index.htm, -,
203.0.113.4, -, 2020-02-24, 22:48:39, W3SVC2, SERVER6, 198.51.100.6, 147, 411, 388, 200, 0, GET, /about.html, -,
203.0.113.11, -, 2020-02-24, 22:48:40, W3SVC2, SERVER7, 198.51.100.18, 170, 531, 468, 200, 0, GET, /image.png, -,
203.0.113.8, -, 2020-02-24, 22:48:41, W3SVC2, SERVER8, 198.51.100.14, 125, 711, 868, 200, 0, GET, /intro.htm, -,
```

## Create a table in Athena for IIS log files

To query your IIS log file format logs in Amazon S3, you first create a table schema so
that Athena can read the log data.

###### To create a table in Athena for IIS log file format logs

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. Paste the following DDL statement into the Athena console, noting the
   following points:
   1. To specify the comma delimiter, use `FIELDS TERMINATED BY
','`.
   2. Modify the values in LOCATION
      's3://amzn-s3-demo-bucket/`iis-log-file-folder`/'
      to point to your IIS log format log files in Amazon S3.

```
CREATE EXTERNAL TABLE `iis_format_logs`(
client_ip_address string,
user_name string,
request_date string,
request_time string,
service_and_instance string,
server_name string,
server_ip_address string,
time_taken_millisec string,
client_bytes_sent string,
server_bytes_sent string,
service_status_code string,
windows_status_code string,
request_type string,
target_of_operation string,
script_parameters string
   )
ROW FORMAT DELIMITED
  FIELDS TERMINATED BY ','
STORED AS INPUTFORMAT
  'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://amzn-s3-demo-bucket/`iis-log-file-folder`/'
```

3. Run the query in the Athena console to register the
   `iis_format_logs` table. When the query completes, the logs
   are ready for you to query from Athena.

## Example IIS log format select query

The following example query selects the request date, request time, request
target, and time taken in milliseconds from the table `iis_format_logs`.
The `WHERE` clause filters for cases in which the request type is
`GET` and the HTTP status code is `200` (successful). In
the query, note that the leading spaces in `' GET'` and `'
 200'` are required to make the query successful.

```
SELECT request_date, request_time, target_of_operation, time_taken_millisec
FROM iis_format_logs
WHERE request_type = ' GET' AND service_status_code = ' 200'
```

The following image shows the results of the query of the sample data.

![Example query results in Athena of IIS log file format log files stored in Amazon S3.](images/querying-iis-logs-2.png)
