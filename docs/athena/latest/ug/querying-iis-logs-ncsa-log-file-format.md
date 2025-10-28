# Query NCSA log file format

IIS also uses the [NCSA
logging](https://docs.microsoft.com/en-us/windows/win32/http/ncsa-logging "https://docs.microsoft.com/en-us/windows/win32/http/ncsa-logging") format, which has a fixed number of fields in ASCII text format
separated by spaces. The structure is similar to the common log format used for Apache
access logs. Fields in the NCSA common log data format include the client IP address,
client ID (not typically used), domain\user ID, request received timestamp, text of the
client request, server status code, and size of the object returned to the
client.

The following example shows data in the NCSA common log format as documented for
IIS.

```
198.51.100.7 - ExampleCorp\Li [10/Oct/2019:13:55:36 -0700] "GET /logo.gif HTTP/1.0" 200 232
198.51.100.14 - AnyCompany\Jorge [24/Nov/2019:10:49:52 -0700] "GET /index.html HTTP/1.1" 200 2165
198.51.100.22 - ExampleCorp\Mateo [27/Dec/2019:11:38:12 -0700] "GET /about.html HTTP/1.1" 200 1287
198.51.100.9 - AnyCompany\Nikki [11/Jan/2020:11:40:11 -0700] "GET /image.png HTTP/1.1" 404 230
198.51.100.2 - ExampleCorp\Ana [15/Feb/2019:10:12:22 -0700] "GET /favicon.ico HTTP/1.1" 404 30
198.51.100.13 - AnyCompany\Saanvi [14/Mar/2019:11:40:33 -0700] "GET /intro.html HTTP/1.1" 200 1608
198.51.100.11 - ExampleCorp\Xiulan [22/Apr/2019:10:51:34 -0700] "GET /group/index.html HTTP/1.1" 200 1344
```

## Create a table

in Athena for IIS NCSA logs

For your `CREATE TABLE` statement, you can use the [Grok SerDe](grok-serde.md "grok-serde.md") and a grok pattern similar to
the one for [Apache web server logs](querying-apache-logs.md "querying-apache-logs.md"). Unlike
Apache logs, the grok pattern uses `%{DATA:user_id}` for the third field
instead of `%{USERNAME:user_id}` to account for the presence of the
backslash in `domain\user_id`. For more information about using the Grok
SerDe, see [Writing grok
custom classifiers](../../../glue/latest/dg/custom-classifier.md#custom-classifier-grok "../../../glue/latest/dg/custom-classifier.md#custom-classifier-grok") in the _AWS Glue Developer Guide_.

###### To create a table in Athena for IIS NCSA web server logs

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. Paste the following DDL statement into the Athena Query Editor. Modify the
   values in `LOCATION
's3://amzn-s3-demo-bucket/`iis-ncsa-logs`/'`
   to point to your IIS NCSA logs in Amazon S3.

```
CREATE EXTERNAL TABLE iis_ncsa_logs(
  client_ip string,
  client_id string,
  user_id string,
  request_received_time string,
  client_request string,
  server_status string,
  returned_obj_size string
  )
ROW FORMAT SERDE
   'com.amazonaws.glue.serde.GrokSerDe'
WITH SERDEPROPERTIES (
   'input.format'='^%{IPV4:client_ip} %{DATA:client_id} %{DATA:user_id} %{GREEDYDATA:request_received_time} %{QUOTEDSTRING:client_request} %{DATA:server_status} %{DATA: returned_obj_size}$'
   )
STORED AS INPUTFORMAT
   'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
   'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
   's3://amzn-s3-demo-bucket/`iis-ncsa-logs`/';
```

3. Run the query in the Athena console to register the
   `iis_ncsa_logs` table. When the query completes, the logs are
   ready for you to query from Athena.

## Example select

queries for IIS NCSA logs

###### Example – Filtering for 404 errors

The following example query selects the request received time, text of the
client request, and server status code from the `iis_ncsa_logs`
table. The `WHERE` clause filters for HTTP status code
`404` (page not found).

```
SELECT request_received_time, client_request, server_status
FROM iis_ncsa_logs
WHERE server_status = '404'
```

The following image shows the results of the query in the Athena Query
Editor.

![Querying an IIS NCSA log from Athena for HTTP 404 entries.](images/querying-iis-logs-3.png)

###### Example – Filtering for successful requests from a particular domain

The following example query selects the user ID, request received time, text
of the client request, and server status code from the
`iis_ncsa_logs` table. The `WHERE` clause filters for
requests with HTTP status code `200` (successful) from users in the
`AnyCompany` domain.

```
SELECT user_id, request_received_time, client_request, server_status
FROM iis_ncsa_logs
WHERE server_status = '200' AND user_id LIKE 'AnyCompany%'
```

The following image shows the results of the query in the Athena Query
Editor.

![Querying an IIS NCSA log from Athena for HTTP 200 entries.](images/querying-iis-logs-4.png)
