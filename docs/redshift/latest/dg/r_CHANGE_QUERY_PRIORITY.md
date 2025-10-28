Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CHANGE_QUERY_PRIORITY

CHANGE_QUERY_PRIORITY enables superusers to modify the priority of a query that is either running or waiting in workload management (WLM).

This function enables superusers to immediately change the priority of any query in the system.
Only one query, user, or session can run with the priority `CRITICAL`.

## Syntax

```
CHANGE_QUERY_PRIORITY(*query\_id*, *priority*)
```

## Arguments

_query_id_

The query identifier of the query whose priority is changed. Requires an `INTEGER` value.

_priority_

The new priority to be assigned to the query. This argument must be a
string with the value `CRITICAL`, `HIGHEST`,
`HIGH`, `NORMAL`, `LOW`, or
`LOWEST`.

## Return Type

None

## Examples

To show the column `query_priority` in the STV_WLM_QUERY_STATE system table, use the following example.

````
`SELECT query, service_class, query_priority, state
FROM stv_wlm_query_state WHERE service_class = 101;`

`+-------+---------------+----------------+---------+
| query | service_class | query_priority | state | +-------+---------------+----------------+---------+
| 1076 | 101 | Lowest | Running |
| 1075 | 101 | Lowest | Running | +-------+---------------+----------------+---------+` ``` To show the results of a superuser running the function `change_query_priority` to change the priority to `CRITICAL`, use the following example. ``` `SELECT CHANGE_QUERY_PRIORITY(1076, 'Critical');` `+-------------------------------------------------------------------------------+
| change_query_priority | +-------------------------------------------------------------------------------+ | Succeeded to change query priority. Priority changed from Lowest to Critical. | +-------------------------------------------------------------------------------+` ```
````
