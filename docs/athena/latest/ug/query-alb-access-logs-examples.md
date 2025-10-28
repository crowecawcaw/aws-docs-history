# Example queries for ALB access

logs

The following query counts the number of HTTP GET requests received by the load
balancer grouped by the client IP address:

```
SELECT COUNT(request_verb) AS
 count,
 request_verb,
 client_ip
FROM alb_access_logs
GROUP BY request_verb, client_ip
LIMIT 100;
```

Another query shows the URLs visited by Safari browser users:

```
SELECT request_url
FROM alb_access_logs
WHERE user_agent LIKE '%Safari%'
LIMIT 10;
```

The following query shows records that have ELB status code values greater than or
equal to 500.

```
SELECT * FROM alb_access_logs
WHERE elb_status_code >= 500
```

The following example shows how to parse the logs by `datetime`:

```
SELECT client_ip, sum(received_bytes)
FROM alb_access_logs
WHERE parse_datetime(time,'yyyy-MM-dd''T''HH:mm:ss.SSSSSS''Z')
     BETWEEN parse_datetime('2018-05-30-12:00:00','yyyy-MM-dd-HH:mm:ss')
     AND parse_datetime('2018-05-31-00:00:00','yyyy-MM-dd-HH:mm:ss')
GROUP BY client_ip;
```

The following query queries the table that uses partition projection for all ALB
access logs from the specified day.

```
SELECT *
FROM alb_access_logs
WHERE day = '2022/02/12'
```
