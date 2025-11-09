Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STL_LIMIT

Analyzes the execution steps that occur when a LIMIT clause is used in a SELECT
query.

STL_LIMIT is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

###### Note

STL_LIMIT only contains queries run on main provisioned clusters. It doesn't contain queries run on concurrency scaling clusters
or on serverless namespaces.
To access explain plans for queries run on both main clusters, concurrency scaling clusters, and serverless namespaces, we recommend that you use the SYS monitoring view
[SYS_QUERY_DETAIL](SYS_QUERY_DETAIL.md "SYS_QUERY_DETAIL.md")
. The data in the SYS monitoring view is formatted to be easier to use and understand.

## Table columns

| Column name | Data type | Description                                                                                                                                                                   |
| ----------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| userid      | integer   | ID of the user who generated the entry.                                                                                                                                       |
| query       | integer   | Query ID. The query column can be used to join other system tables and views.                                                                                                 |
| slice       | integer   | Number that identifies the slice where the query was running.                                                                                                                 |
| segment     | integer   | Number that identifies the query segment.                                                                                                                                     |
| step        | integer   | Query step that ran.                                                                                                                                                          |
| starttime   | timestamp | Time in UTC that the query started. Total time includes queuing and execution. with 6 digits of precision for fractional seconds. For example: `2009-06-12 11:29:19.131358`.  |
| endtime     | timestamp | Time in UTC that the query finished. Total time includes queuing and execution. with 6 digits of precision for fractional seconds. For example: `2009-06-12 11:29:19.131358`. |
| tasknum     | integer   | Number of the query task process that was assigned to run the step.                                                                                                           |
| rows        | bigint    | Total number of rows that were processed.                                                                                                                                     |
| checksum    | bigint    | This information is for internal use only.                                                                                                                                    |

## Sample queries

In order to generate a row in STL_LIMIT, this example first runs the following
query against the VENUE table using the LIMIT clause.

```
select * from venue
order by 1
limit 10;
```

```
 venueid |         venuename          |    venuecity    | venuestate | venueseats
---------+----------------------------+-----------------+------------+------------
       1 | Toyota Park                | Bridgeview      | IL         |          0
       2 | Columbus Crew Stadium      | Columbus        | OH         |          0
       3 | RFK Stadium                | Washington      | DC         |          0
       4 | CommunityAmerica Ballpark  | Kansas City     | KS         |          0
       5 | Gillette Stadium           | Foxborough      | MA         |      68756
       6 | New York Giants Stadium    | East Rutherford | NJ         |      80242
       7 | BMO Field                  | Toronto         | ON         |          0
       8 | The Home Depot Center      | Carson          | CA         |          0
       9 | Dick's Sporting Goods Park | Commerce City   | CO         |          0
      10 | Pizza Hut Park             | Frisco          | TX         |          0
(10 rows)
```

Next, run the following query to find the query ID of the last query you ran
against the VENUE table.

```
select max(query)
from stl_query;
```

```
  max
--------
 127128
(1 row)
```

Optionally, you can run the following query to verify that the query ID
corresponds to the LIMIT query you previously ran.

```
select query, trim(querytxt)
from stl_query
where query=127128;
```

```
 query  |                  btrim
--------+------------------------------------------
 127128 | select * from venue order by 1 limit 10;
(1 row)
```

Finally, run the following query to return information about the LIMIT query from
the STL_LIMIT table.

```
select slice, segment, step, starttime, endtime, tasknum
from stl_limit
where query=127128
order by starttime, endtime;
```

```
  slice | segment | step |         starttime          |          endtime           | tasknum
 -------+---------+------+----------------------------+----------------------------+---------
      1 |       1 |    3 | 2013-09-06 22:56:43.608114 | 2013-09-06 22:56:43.609383 |      15
      0 |       1 |    3 | 2013-09-06 22:56:43.608708 | 2013-09-06 22:56:43.609521 |      15
  10000 |       2 |    2 | 2013-09-06 22:56:43.612506 | 2013-09-06 22:56:43.612668 |       0
(3 rows)
```
