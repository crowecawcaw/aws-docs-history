# Custom analysis rule with differential privacy

In AWS Clean Rooms, the custom analysis rule supports differential privacy. Differential privacy
is a mathematically-rigorous framework for data privacy protection that helps you protect your
data against re-identification attempts.

Differential privacy supports aggregate analysis such as ad campaign planning,
post-ad-campaign measurement, benchmarking in a financial institution consortium, and A/B
testing for healthcare research.

The supported query structure and syntax are defined in [Query structure and syntax](#dp-query-structure-syntax "#dp-query-structure-syntax").

## Custom analysis rule with differential privacy example

###### Note

AWS Clean Rooms Differential Privacy is only available for collaborations where the data is stored in Amazon S3.

Consider the [custom
analysis rule example](analysis-rules-custom.md#custom-example "analysis-rules-custom.md#custom-example") presented in the previous section. This example demonstrates
how you can use differential privacy to protect your data against re-identification attempts
while allowing your partner to learn business-critical insights from your data. Assume that
Company B, who has the viewership data, wants to protect their data using differential
privacy. To complete the differential privacy setup, Company B completes the following
steps:

1. Company B turns on differential privacy while adding custom analysis rule to the
   viewership configured table. Company B selects `viewershipdata.hashedemail`
   as the user identifier column.
2. Company B [adds a differential privacy
   policy](configure-differential-privacy.md "configure-differential-privacy.md") in the collaboration to make their viewership data table available for
   querying. Company B selects the default policy to quickly complete the setup.

Company A, who wants to understand the sales incrementality of an advertising campaign
on Company B's site, runs the analysis template. Because the query is compatible with the
general-purpose [query structure](#dp-query-structure-syntax "#dp-query-structure-syntax") of AWS Clean Rooms Differential
Privacy, the query runs successfully.

## Query structure and syntax

Queries containing at least one table that have the differential privacy turned on must
adhere to the following syntax.

```
query_statement:
    [cte, ...] final_select

 cte:
    WITH sub_query AS (
       inner_select
       [ UNION | INTERSECT | UNION_ALL | EXCEPT/MINUS ]
       [ inner_select ]
    )

 inner_select:
     SELECT [user_id_column, ] expression [, ...]
     FROM table_reference [, ...]
     [ WHERE condition ]
     [ GROUP BY user_id_column[, expression] [, ...] ]
     [ HAVING condition ]

 final_select:
     SELECT [expression, ...] | COUNT | COUNT_DISTINCT | SUM | AVG | STDDEV
     FROM table_reference [, ...]
     [ WHERE condition ]
     [ GROUP BY expression [, ...] ]
     [ HAVING COUNT | COUNT_DISTINCT | SUM | AVG | STDDEV | condition ]
     [ ORDER BY column_list ASC | DESC ]
     [ OFFSET literal ]
     [ LIMIT literal ]

 expression:
    column_name [, ...] | expression AS alias | aggregation_functions | window_functions_on_user_id | scalar_function | CASE | column_name math_expression [, expression]

 window_functions_on_user_id:
    function () OVER (PARTITION BY user_id_column, [column_name] [ORDER BY column_list ASC|DESC])
```

###### Note

For differential privacy query structure and syntax, be aware of the following:

- Sub-queries are not supported.
- Common Table Expressions (CTEs) should emit the user identifier column if a table
  or CTE involve data protected by differential privacy. Filters, groupings, and
  aggregations should be done at the user level.
- Final\_select allows COUNT DISTINCT, COUNT, SUM, AVG, and STDDEV aggregate
  functions.

For
more details about which SQL keywords are supported for differential privacy, see [SQL capabilities of AWS Clean Rooms Differential Privacy](dp-sql-capabilities.md "dp-sql-capabilities.md").
