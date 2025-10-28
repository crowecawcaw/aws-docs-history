# Custom analysis rule in AWS Clean Rooms

In AWS Clean Rooms, a _custom analysis rule_ is a new type of
analysis rule that allows custom queries to be run on the configured table. Custom SQL queries
are still restricted to having only the SELECT command but can use more SQL
constructs than [aggregation](analysis-rules-aggregation.md#agg-query-controls "analysis-rules-aggregation.md#agg-query-controls") and [list](analysis-rules-list.md#list-query-controls "analysis-rules-list.md#list-query-controls") queries (for example, window functions, OUTER JOIN,
CTEs, or subqueries; see the [AWS Clean Rooms
SQL Reference](../sql-reference/sql-reference.md "../sql-reference/sql-reference.md") for a complete list). Custom SQL queries don’t have to follow a query
structure like [aggregation](analysis-rules-aggregation.md#agg-query-structure-syntax "analysis-rules-aggregation.md#agg-query-structure-syntax") and [list](analysis-rules-list.md#list-query-controls "analysis-rules-list.md#list-query-controls") queries.

The custom analysis rule supports more advanced use cases than those that can be supported
by the aggregation and list analysis rule such as custom attribution analysis, benchmarking,
incrementality analysis, and audience discovery. This is in addition to a superset of the use
cases supported by aggregation and list analysis rule.

The custom analysis rule also supports differential privacy. Differential privacy is a
mathematically-rigorous framework for data privacy protection. For more information, see [AWS Clean Rooms Differential Privacy](differential-privacy.md "differential-privacy.md"). When you create an
analysis template, AWS Clean Rooms Differential Privacy checks the template to determine whether it is
compatible with the general-purpose query structure for AWS Clean Rooms Differential Privacy. This
validation ensures that you don't create an analysis template that isn't allowed with a
differential privacy protected table.

To configure the custom analysis rule, data owners can choose to allow specific custom
queries, stored in [analysis templates](create-analysis-template.md "create-analysis-template.md"), to run on
their configured tables. Data owners review analysis templates before adding them to the allowed
analysis control in the custom analysis rule. Analysis templates are available and visible only
in the collaboration in which they are created (even if the table is associated to other
collaborations) and can be run only by the member who can query in that collaboration.

Alternatively, members can choose to allow other members (query providers) to create queries
without review. Members add query providers’ accounts the allowed query providers control in the
custom analysis rule. If the query provider is the member who can query, they could run any
query directly on the configured table. Query providers could also create queries by [creating analysis templates](create-analysis-template.md "create-analysis-template.md"). Any queries that have
been created by the query providers are automatically allowed to run on the table in all
collaborations in which the AWS account is present and the table is associated.

Data owners can only allow analysis templates or accounts to create queries, not both. If
the data owner leaves it empty, the member who can query can't run queries on the configured
table.

###### Topics

- [Custom analysis rule predefined
  structure](#custom-predefined-structure "#custom-predefined-structure")
- [Custom analysis rule example](#custom-example "#custom-example")
- [Custom analysis rule with differential privacy](#custom-diff-privacy "#custom-diff-privacy")

## Custom analysis rule predefined

structure

The following example includes a predefined structure that shows you how to complete a
custom analysis rule with differential privacy turned on. The `userIdentifier`
value is the column that uniquely identifies your users, such as _user_id_.
When you have two or more tables with differential privacy turned on in a collaboration, AWS Clean Rooms
requires you to configure the same column as the user identifier column in both of the
analysis rules to maintain a consistent definition of the users across tables.

```
{
  "allowedAnalyses": ["ANY_QUERY"] | string[],
  "allowedAnalysisProviders": [],
  "differentialPrivacy": {
    "columns": [
      {
        "name": "`userIdentifier`"
      }
    ]
  }
}
```

You can either:

- Add analysis template ARNs to allowed analyses control. In this case, the
  `allowedAnalysisProviders` control is not included.

```
{
  allowedAnalyses: string[]
}
```

- Add member AWS account IDs to the `allowedAnalysisProviders` control. In
  this case, you add `ANY_QUERY` to the `allowedAnalyses` control.

```
{
  allowedAnalyses: ["ANY_QUERY"],
  allowedAnalysisProviders: string[]
}
```

## Custom analysis rule example

The following example demonstrates how two companies can collaborate in AWS Clean Rooms using
the custom analysis rule.

Company A has customer and sales data. Company A is interested in understanding the sales
incrementality of an advertising campaign on Company B site. Company B has viewership data and
segment attributes that are useful to Company (for example, the device they used when viewing
the advertising).

Company A has a specific incrementality query they want to run in the collaboration.

To create a collaboration and run a custom analysis in collaboration, the companies do the
following:

1. Company A creates a collaboration and creates a membership. The collaboration has
   Company B as another member on the collaboration. Company A enables query logging in the
   collaboration, and it enables query logging in its account.
2. Company B creates a membership in the collaboration. It enables query logging in its
   account.
3. Company A creates a CRM configured table
4. Company A adds empty custom analysis rule to sales configured table.
5. Company A associates sales configured table to the collaboration.
6. Company B creates viewership configured table.
7. Company B adds an empty custom analysis rule to the viewership configured
   table.
8. Company B associates viewership configured table to the collaboration.
9. Company A views the sales table and viewership table associated to the collaboration
   and creates analysis template, adding the incrementality query and parameter for campaign
   month.

```
{
    "analysisParameters": [
    {
        "defaultValue": ""
        "type": "DATE"
        "name": "campaign_month"
    }
    ],
    "description": "Monthly incrementality query using sales and viewership data"
    "format": "SQL"
    "name": "Incrementality analysis"
    "source":
        "WITH labeleddata AS
        (
        SELECT hashedemail, deviceid, purchases, unitprice, purchasedate,
        CASE
            WHEN testvalue IN ('value1', 'value2', 'value3') THEN 0
            ELSE 1
        END AS testgroup
        FROM viewershipdata
        )
        SELECT labeleddata.purchases, provider.impressions
        FROM labeleddata
        INNER JOIN salesdata
          ON labeleddata.hashedemail = provider.hashedemail
        WHERE MONTH(labeleddata.purchasedate) > :campaignmonth
        AND testgroup = :group
       "
}
```

10. Company A adds their account (for example, 444455556666) to the allowed analysis
    provider control in the custom analysis rule. They use the allowed analysis provider
    control because they want to allow any queries they create to run on their sales
    configured table.

```
{
  "allowedAnalyses": [
    "ANY_QUERY"
  ],
  "allowedAnalysisProviders": [
    "444455556666"
  ]
}
```

11. Company B sees the created analysis template in the collaboration and reviews its
    contents including the query string and parameter.
12. Company B determines that the analysis template achieves the incrementality use case
    and meets their privacy requirements for how their viewership configured table can be
    queried.
13. Company B adds the analysis template ARN to the allowed analysis control in the custom
    analysis rule of the viewership table. They use the allowed analysis control because they
    only want to allow the incrementality query to run on their viewership configured
    table.

```
{
  "allowedAnalyses": [
    "arn:aws:cleanrooms:us-east-1:111122223333:membership/41327cc4-bbf0-43f1-b70c-a160dddceb08/analysistemplate/1ff1bf9d-781c-418d-a6ac-2b80c09d6292"
  ]
}
```

14. Company A runs the analysis template and uses the parameter value
    `05-01-2023`.

## Custom analysis rule with differential privacy

In AWS Clean Rooms, the custom analysis rule supports differential privacy. Differential privacy
is a mathematically-rigorous framework for data privacy protection that helps you protect your
data against re-identification attempts.

Differential privacy supports aggregate analysis such as ad campaign planning,
post-ad-campaign measurement, benchmarking in a financial institution consortium, and A/B
testing for healthcare research.

The supported query structure and syntax are defined in [Query structure and syntax](#dp-query-structure-syntax "#dp-query-structure-syntax").

### Custom analysis rule with differential privacy

example

###### Note

AWS Clean Rooms Differential Privacy is only available for collaborations using AWS Clean Rooms SQL as the analytics engine
and data stored in Amazon S3.

Consider the [custom
analysis rule example](#custom-example "#custom-example") presented in the previous section. This example demonstrates
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

### Query structure and syntax

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
- Final_select allows COUNT DISTINCT, COUNT, SUM, AVG, and STDDEV aggregate
  functions.

For
more details about which SQL keywords are supported for differential privacy, see [SQL capabilities of AWS Clean Rooms Differential Privacy](dp-sql-capabilities.md "dp-sql-capabilities.md").
