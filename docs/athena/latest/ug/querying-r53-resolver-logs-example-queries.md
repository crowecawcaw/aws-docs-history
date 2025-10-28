# Example queries

The following examples show some queries that you can perform from Athena on your
Resolver query logs.

## Example 1 - query logs in descending query_timestamp order

The following query displays log results in descending
`query_timestamp` order.

```
SELECT * FROM "r53_rlogs"
ORDER BY query_timestamp DESC
```

## Example 2 - query logs within specified start and end times

The following query queries logs between midnight and 8am on September 24, 2020.
Substitute the start and end times according to your own requirements.

```
SELECT query_timestamp, srcids.instance, srcaddr, srcport, query_name, rcode
FROM "r53_rlogs"
WHERE (parse_datetime(query_timestamp,'yyyy-MM-dd''T''HH:mm:ss''Z')
     BETWEEN parse_datetime('`2020-09-24-00:00:00`','yyyy-MM-dd-HH:mm:ss')
     AND parse_datetime('`2020-09-24-00:08:00`','yyyy-MM-dd-HH:mm:ss'))
ORDER BY query_timestamp DESC

```

## Example 3 - query logs based on a specified DNS query name pattern

The following query selects records whose query name includes the string
"example.com".

```
SELECT query_timestamp, srcids.instance, srcaddr, srcport, query_name, rcode, answers
FROM "r53_rlogs"
WHERE query_name LIKE '%example.com%'
ORDER BY query_timestamp DESC
```

## Example 4 - query log requests with no answer

The following query selects log entries in which the request received no
answer.

```
SELECT query_timestamp, srcids.instance, srcaddr, srcport, query_name, rcode, answers
FROM "r53_rlogs"
WHERE cardinality(answers) = 0
```

## Example 5 - query logs with a specific answer

The following query shows logs in which the `answer.Rdata` value has
the specified IP address.

```
SELECT query_timestamp, srcids.instance, srcaddr, srcport, query_name, rcode, answer.Rdata
FROM "r53_rlogs"
CROSS JOIN UNNEST(r53_rlogs.answers) as st(answer)
WHERE answer.Rdata='203.0.113.16';
```
