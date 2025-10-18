# CloudTrail Lake SQL constraints

CloudTrail Lake queries are SQL strings. This section provides information about the supported functions, operators, and schemas.

Only `SELECT` statements are allowed. No query strings can change or mutate data.

The CloudTrail Lake syntax for a `SELECT` statement is as follows. The event data store ID—the ID portion
 of the event data store's ARN—is specified for the `FROM` value.


```
SELECT [ DISTINCT ] columns [ Aggregate ]
[ FROM table `event_data_store_ID`]
[ WHERE columns [ Conditions ] ]
[ GROUP BY columns [ DISTINCT | Aggregate ] ]
[ HAVING columns [ Aggregate | Conditions ] ]
[ ORDER BY columns [ Aggregate | ASC | DESC | NULLS | FIRST | LAST ]
[ LIMIT [ INT ] ]
```
CloudTrail Lake supports all valid Trino SQL `SELECT` statements, functions, and operators. For more information about the 
 supported SQL functions and operators, see [Functions and Operators](https://trino.io/docs/current/functions.html "https://trino.io/docs/current/functions.html") 
 on the Trino documentation website. 
 

The CloudTrail console provides a number of sample queries that can help you get started writing your own queries. For more information, see [View sample queries with the CloudTrail console](lake-console-queries.md "lake-console-queries.md").

For information about how to optimize your queries, 
 see [Optimize CloudTrail Lake queries](lake-queries-optimization.md "lake-queries-optimization.md").

###### Topics

* [Supported functions,
 condition and join operators](#query-aggregates-condition-operators "#query-aggregates-condition-operators")
* [Advanced, multi-table query
 support](#query-advanced-multi-table "#query-advanced-multi-table")

## Supported functions,
 condition and join operators


**Supported functions**


CloudTrail Lake supports all Trino functions. For more information about the supported functions, see [Functions and Operators](https://trino.io/docs/current/functions.html "https://trino.io/docs/current/functions.html") 
 on the Trino documentation website.


**Supported condition operators**


The following are supported condition operators.



```
AND
OR
IN
NOT
IS (NOT) NULL
LIKE
BETWEEN
GREATEST
LEAST
IS DISTINCT FROM
IS NOT DISTINCT FROM
<
>
<=
>=
<>
!=
( conditions ) #parenthesised conditions
```

**Supported join operators**


The following are the supported `JOIN` operators. For more information about
 running multi-table queries, see [Advanced, multi-table query
 support](#query-advanced-multi-table "#query-advanced-multi-table").



```
UNION 
UNION ALL 
EXCEPT 
INTERSECT 
LEFT JOIN 
RIGHT JOIN 
INNER JOIN    
```

## Advanced, multi-table query
 support


CloudTrail Lake supports advanced query language across multiple event data stores.



* [UNION|UNION
 ALL|EXCEPT|INTERSECT](#query-multi-table-union "#query-multi-table-union")
* [LEFT|RIGHT|INNER
 JOIN](#query-multi-table-left-right "#query-multi-table-left-right")

To run your query, use the **start-query** command in the AWS CLI.
 The following is an example, using one of the sample queries in this section.



```
aws cloudtrail start-query
--query-statement "Select eventId, eventName from EXAMPLEf852-4e8f-8bd1-bcf6cEXAMPLE UNION Select eventId, eventName from EXAMPLEg741-6y1x-9p3v-bnh6iEXAMPLE UNION ALL Select eventId, eventName from EXAMPLEb529-4e8f9l3d-6m2z-lkp5sEXAMPLE ORDER BY eventId LIMIT 10;"
```

The response is a `QueryId` string. To get the status of a query, run
 `describe-query`, using the `QueryId` value returned by
 `start-query`. If the query is successful, you can run
 `get-query-results` to get results.


### `UNION|UNION
 ALL|EXCEPT|INTERSECT`


The following is an example query
 that uses `UNION` and `UNION ALL` to find events by their
 event ID and event name in three event data stores, EDS1, EDS2, and EDS3. The
 results are selected from each event data store first, then results are
 concatenated, ordered by event ID, and limited to ten events.



```
Select eventId, eventName from EDS1
UNION
Select eventId, eventName from EDS2
UNION ALL
Select eventId, eventName from EDS3 
ORDER BY eventId LIMIT 10;
```

### `LEFT|RIGHT|INNER
 JOIN`


The following is an example query
 that uses `LEFT JOIN` to find all events from an event data store
 named `eds2`, mapped to `edsB`, that match those in a
 primary (left) event data store, `edsA`. The returned events occur on
 or before January 1, 2020, and only the event names are returned.



```
SELECT edsA.eventName, edsB.eventName, element_at(edsA.map, 'test')
FROM eds1 as edsA 
LEFT JOIN eds2 as edsB
ON edsA.eventId = edsB.eventId 
WHERE edsA.eventtime <= '2020-01-01'
ORDER BY edsB.eventName;
```
