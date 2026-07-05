Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# CHANGE\_QUERY\_PRIORITY

CHANGE\_QUERY\_PRIORITY enables superusers to modify the priority of a query that is either running or waiting in workload management (WLM).

This function enables superusers to immediately change the priority of any query in the system.
Only one query, user, or session can run with the priority `CRITICAL`.

## Syntax

```
CHANGE_QUERY_PRIORITY(*query\_id*, *priority*)
```

## Arguments

_query\_id_

The query identifier of the query whose priority is changed. Requires an `INTEGER` value.

_priority_

The new priority to be assigned to the query. This argument must be a
string with the value `CRITICAL`, `HIGHEST`,
`HIGH`, `NORMAL`, `LOW`, or
`LOWEST`.

## Return Type

None

## Examples

To show the column `query_priority` in the STV\_WLM\_QUERY\_STATE system table, use the following example.

```
`SELECT query, service_class, query_priority, state
FROM stv_wlm_query_state WHERE service_class = 101;`

`+-------+---------------+----------------+---------+
| query | service_class | query_priority | state |
+-------+---------------+----------------+---------+
| 1076 | 101 | Lowest | Running |
| 1075 | 101 | Lowest | Running |
+-------+---------------+----------------+---------+`
```

To show the results of a superuser running the function
`change_query_priority` to change the priority to
`CRITICAL`, use the following example.

```
`SELECT CHANGE_QUERY_PRIORITY(1076, 'Critical');`

`+-------------------------------------------------------------------------------+
| change_query_priority |
+-------------------------------------------------------------------------------+
| Succeeded to change query priority. Priority changed from Lowest to Critical. |
+-------------------------------------------------------------------------------+`
```
