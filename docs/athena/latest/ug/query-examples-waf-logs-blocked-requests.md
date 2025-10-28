# Query for blocked

requests or addresses

The examples in this section query for blocked requests or addresses.

- [Extract the top 100 IP addresses blocked by a specified rule type](#waf-example-extract-top-100-blocked-ip-by-rule "#waf-example-extract-top-100-blocked-ip-by-rule")
- [Count the number of times a request from a specified country has been blocked](#waf-example-count-request-blocks-from-country "#waf-example-count-request-blocks-from-country")
- [Count the number of times a request has been blocked, grouping by specific attributes](#waf-example-count-request-blocks-by-attribute "#waf-example-count-request-blocks-by-attribute")
- [Count the number of times a specific terminating rule ID has been matched](#waf-example-count-terminating-rule-id-matches "#waf-example-count-terminating-rule-id-matches")
- [Retrieve the top 100 IP addresses blocked during a specified date range](#waf-example-top-100-ip-addresses-blocked-for-date-range "#waf-example-top-100-ip-addresses-blocked-for-date-range")

###### Example – Extract the top 100 IP addresses blocked by a specified rule

type

The following query extracts and counts the top 100 IP addresses that have
been blocked by the `RATE_BASED` terminating rule during the
specified date range.

```
SELECT COUNT(httpRequest.clientIp) as count,
httpRequest.clientIp
FROM waf_logs
WHERE terminatingruletype='RATE_BASED' AND action='BLOCK' and "date" >= '2021/03/01'
AND "date" < '2021/03/31'
GROUP BY httpRequest.clientIp
ORDER BY count DESC
LIMIT 100
```

###### Example – Count the number of times a

request from a specified country has been blocked

The following query counts the number of times the request has arrived from an
IP address that belongs to Ireland (IE) and has been blocked by the
`RATE_BASED` terminating rule.

```
SELECT
  COUNT(httpRequest.country) as count,
  httpRequest.country
FROM waf_logs
WHERE
  terminatingruletype='RATE_BASED' AND
  httpRequest.country='IE'
GROUP BY httpRequest.country
ORDER BY count
LIMIT 100;
```

###### Example – Count the number of times a

request has been blocked, grouping by specific attributes

The following query counts the number of times the request has been blocked,
with results grouped by WebACL, RuleId, ClientIP, and HTTP Request URI.

```
SELECT
  COUNT(*) AS count,
  webaclid,
  terminatingruleid,
  httprequest.clientip,
  httprequest.uri
FROM waf_logs
WHERE action='BLOCK'
GROUP BY webaclid, terminatingruleid, httprequest.clientip, httprequest.uri
ORDER BY count DESC
LIMIT 100;
```

###### Example – Count the number of times a

specific terminating rule ID has been matched

The following query counts the number of times a specific terminating rule ID
has been matched (`WHERE
 terminatingruleid='e9dd190d-7a43-4c06-bcea-409613d9506e'`). The query
then groups the results by WebACL, Action, ClientIP, and HTTP Request
URI.

```
SELECT
  COUNT(*) AS count,
  webaclid,
  action,
  httprequest.clientip,
  httprequest.uri
FROM waf_logs
WHERE terminatingruleid='e9dd190d-7a43-4c06-bcea-409613d9506e'
GROUP BY webaclid, action, httprequest.clientip, httprequest.uri
ORDER BY count DESC
LIMIT 100;
```

###### Example – Retrieve the top 100 IP addresses

blocked during a specified date range

The following query extracts the top 100 IP addresses that have been blocked
for a specified date range. The query also lists the number of times the IP
addresses have been blocked.

```
SELECT "httprequest"."clientip", "count"(*) "ipcount", "httprequest"."country"
FROM waf_logs
WHERE "action" = 'BLOCK' and "date" >= '2021/03/01'
AND "date" < '2021/03/31'
GROUP BY "httprequest"."clientip", "httprequest"."country"
ORDER BY "ipcount" DESC limit 100
```
