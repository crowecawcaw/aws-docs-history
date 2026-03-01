# Query using date and time

The examples in this section include queries that use date and time values.

- [Return the timestamp field in human-readable ISO 8601 format](#waf-example-return-human-readable-timestamp "#waf-example-return-human-readable-timestamp")
- [Return records from the last 24 hours](#waf-example-return-records-last-24-hours "#waf-example-return-records-last-24-hours")
- [Return records for a specified date range and IP address](#waf-example-return-records-date-range-and-ip "#waf-example-return-records-date-range-and-ip")
- [For a specified date range, count the number of IP addresses in five minute intervals](#waf-example-count-ip-addresses-in-date-range "#waf-example-count-ip-addresses-in-date-range")
- [Count the number of X-Forwarded-For IP in the last 10 days](#waf-example-count-x-forwarded-for-ip "#waf-example-count-x-forwarded-for-ip")

###### Example – Return the timestamp field in human-readable ISO 8601 format

The following query uses the `from_unixtime` and
`to_iso8601` functions to return the `timestamp` field
in human-readable ISO 8601 format (for example,
`2019-12-13T23:40:12.000Z` instead of
`1576280412771`). The query also returns the HTTP source name, source
ID, and request.

```
SELECT to_iso8601(from_unixtime(timestamp / 1000)) as time_ISO_8601,
       httpsourcename,
       httpsourceid,
       httprequest
FROM waf_logs
LIMIT 10;
```

###### Example – Return records from the last 24 hours

The following query uses a filter in the `WHERE` clause to return
the HTTP source name, HTTP source ID, and HTTP request fields for records from
the last 24 hours.

```
SELECT to_iso8601(from_unixtime(timestamp/1000)) AS time_ISO_8601,
       httpsourcename,
       httpsourceid,
       httprequest
FROM waf_logs
WHERE from_unixtime(timestamp/1000) > now() - interval '1' day
LIMIT 10;
```

###### Example – Return records for a specified date range and IP address

The following query lists the records in a specified date range for a
specified client IP address.

```
SELECT *
FROM waf_logs
WHERE httprequest.clientip='53.21.198.66' AND "date" >= '2021/03/01' AND "date" < '2021/03/31'
```

###### Example – For a specified date range, count the number of IP addresses in five minute intervals

The following query counts, for a particular date range, the number of IP
addresses in five minute intervals.

```
WITH test_dataset AS
  (SELECT
     format_datetime(from_unixtime((timestamp/1000) - ((minute(from_unixtime(timestamp / 1000))%5) * 60)),'yyyy-MM-dd HH:mm') AS five_minutes_ts,
     "httprequest"."clientip"
     FROM waf_logs
     WHERE "date" >= '2021/03/01' AND "date" < '2021/03/31')
SELECT five_minutes_ts,"clientip",count(*) ip_count
FROM test_dataset
GROUP BY five_minutes_ts,"clientip"
```

###### Example – Count the number of X-Forwarded-For IP in the last 10 days

The following query filters the request headers and counts the number of
X-Forwarded-For IP in the last 10 days.

```
WITH test_dataset AS
  (SELECT header
   FROM waf_logs
   CROSS JOIN UNNEST (httprequest.headers) AS t(header)
   WHERE from_unixtime("timestamp"/1000) > now() - interval '10' DAY)
SELECT header.value AS ip,
       count(*) AS COUNT
FROM test_dataset
WHERE header.name='X-Forwarded-For'
GROUP BY header.value
ORDER BY COUNT DESC
```

For more information about date and time functions, see [Date and time
functions and operators](https://trino.io/docs/current/functions/datetime.html "https://trino.io/docs/current/functions/datetime.html") in the Trino documentation.
