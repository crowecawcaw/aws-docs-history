# List analysis rule

In AWS Clean Rooms, a _list analysis rule_ outputs row-level
lists of the overlap between the configured table that it's added to and the configured tables
of the member who can query. The member who can query runs queries that include a list analysis
rule.

The list analysis rule type supports uses cases such as enrichment and audience building.

For more information about the predefined query structure and syntax for this analysis rule,
see [List analysis rule predefined
structure](#intersection-list-params-template "#intersection-list-params-template").

The parameters of the list analysis rule, defined in [List analysis rule - query controls](#parameters-list-query-controls "#parameters-list-query-controls"),
have query controls. Its query controls include the ability to select the columns that can be
listed in the output. The query is required to have at least one join with a configured table
from the member who can query, either directly or transitively.

There are no query results controls like there are for the [Aggregation analysis rule](analysis-rules-aggregation.md "analysis-rules-aggregation.md").

List queries can only use mathematical operators. They can't use other functions (such as
aggregation or scalar).

###### Topics

- [List query structure and syntax](#list-query-controls "#list-query-controls")
- [List analysis rule - query controls](#parameters-list-query-controls "#parameters-list-query-controls")
- [List analysis rule predefined
  structure](#intersection-list-params-template "#intersection-list-params-template")
- [List analysis rule - example](#list-example "#list-example")

## List query structure and syntax

Queries on tables that have a list analysis rule must adhere to the following syntax.

```

--`select_list_expression`
SELECT DISTINCT column_name [[AS] column_alias ] [, ...]

--`table_expression`
FROM table_name [[AS] table_alias ]
  [[INNER] JOIN table_name [[AS] table_alias] ON join_condition] [...]

--`where_expression`
[WHERE where_condition]

--`limit_expression`
[LIMIT number]

```

The following table explains each expression listed in the preceding syntax.

| Expression               | Definition                                                                                                                                                                                                                                                                                                                                                                                        | Examples                                                                                                                                                                                      |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `select_list_expression` | A comma-separated list containing at least one table column name.<br>A `DISTINCT` parameter is required.<br>NoteThe `select_list_expression` can alias columns with or without the<br>`AS` parameter. For more information, see the [AWS Clean Rooms SQL Reference](../sql-reference/sql-reference.md "../sql-reference/sql-reference.md").                                                       | `SELECT DISTINCT segment`                                                                                                                                                                     |
| `table_expression`       | A table, or join of tables, with `join_condition` to connect it to<br>`join_condition`.<br>`join_condition` returns a Boolean.<br>The `table_expression` supports:<br>• A specific JOIN type (INNER JOIN)<br>• The equality comparison conditions within a `join_condition`<br>(`=`)<br>• Logical operators (`AND`, `OR`).                                                                        | `<br>FROM consumer_table<br>INNER JOIN provider_table<br>ON<br>consumer_table.identifier1 = provider_table.identifier1<br>AND<br>consumer_table.identifier2 = provider_table.identifier2<br>` |
| `where_expression`       | A conditional expression that returns a Boolean. It can be comprised of the following:<br>• Table column names<br>• Mathematical operators<br>• String literals<br>• Numerical literals<br>Supported comparison conditions are (`=, >, <, <=, >=,<br><>, !=, NOT, IN, NOT IN, LIKE, IS NULL, IS NOT NULL`).<br>Supported logical operators are (`AND, OR`).The<br>`where_expression` is optional. | `WHERE state + '_' + city = 'NY_NYC'`<br>`WHERE timestampColumn = timestampColumn2<br>• 14`                                                                                                   |
| `limit_expression`       | This expression must take a positive integer.<br>The `limit_expression` is optional.                                                                                                                                                                                                                                                                                                              | `LIMIT 100`                                                                                                                                                                                   |

For list query structure and syntax, be aware of the following:

- SQL commands other than SELECT are not supported.
- Subqueries and common table expressions (for example, WITH) are not
  supported
- HAVING, GROUP
  BY, and ORDER BY clauses are not supported
- OFFSET parameter is not supported

## List analysis rule - query controls

With list query controls, you can control how the columns in your table are used to query
the table. For example, you can control which column is used for joining, or which column can
be used in SELECT statement and WHERE clause.

The following sections explain each control.

###### Topics

- [Join controls](#list-controls-join-controls "#list-controls-join-controls")
- [List controls](#list-controls "#list-controls")

### Join controls

With _Join controls_, you can control how your table
can be joined to other tables in the **table_expression**.
AWS Clean Rooms only supports INNER JOIN. In the list analysis rule, at least one
INNER JOIN is required and the member who can query is required to include
a table they own in the INNER JOIN. This means they must join your table with
theirs, either directly or transitively.

Following is an example of transitivity.

```
ON
my_table.identifer = third_party_table.identifier
....
ON
third_party_table.identifier = member_who_can_query_table.id
```

INNER JOIN statements can only use columns that have been explicitly
categorized as a `joinColumn` in your analysis rule.

The INNER JOIN must operate on a `joinColumn` from your
configured table and a `joinColumn` from another configured table in the
collaboration. You decide which columns from your table can be used as
`joinColumn`.

Each match condition within the ON clause is required to use the equality
comparison condition (`=`) between two columns.

Multiple match conditions within an ON clause can be:

- Combined using the `AND` logical operator
- Separated using the `OR` logical operator

###### Note

All JOIN match conditions must match one row from each side of the
JOIN. All conditionals connected by an `OR` or an
`AND` logical operator must adhere to this requirement as well.

The following is an example of a query with an `AND` logical operator.

```
SELECT some_col, other_col
FROM table1
    JOIN table2
    ON table1.id = table2.id AND table1.name = table2.name
```

The following is an example of a query with an `OR` logical operator.

```
SELECT some_col, other_col
FROM table1
    JOIN table2
    ON table1.id = table2.id OR table1.name = table2.name
```

| Control       | Definition                                                                                         | Usage                                                                                                                                                                                                                           |
| ------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `joinColumns` | The columns that you want to allow the member who can query to use in the<br>INNER JOIN statement. | The same column can't be categorized as both a `joinColumn` and<br>`listColumn` (see [List controls](#list-controls "#list-controls")).<br>`joinColumn` can't be used in any other parts of the query other<br>than INNER JOIN. |

### List controls

_List controls_ control the columns that can be listed
in the query output (that is, used in the SELECT statement) or used to filter results (that
is, used in the WHERE statement).

| Control       | Definition                                                                            | Usage                                                                                                                       |
| ------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `listColumns` | The columns that you allow the member who can query to use in the SELECT and<br>WHERE | A `listColumn` can be used in SELECT and<br>WHERE.The same column can't be used as both a<br>`listColumn` and `joinColumn`. |

## List analysis rule predefined

structure

The following example includes a predefined structure that shows how you complete a list
analysis rule.

In the following example, `MyTable` refers to your
data table. You can replace each `user input placeholder` with your
own information.

```
{
  "joinColumns": [`MyTable column name(s)`],
  "listColumns": [`MyTable column name(s)`],
}
```

## List analysis rule - example

The following example demonstrates how two companies can collaborate in AWS Clean Rooms using
list analysis.

Company A has customer relationship management (CRM) data. Company A wants to obtain
additional segment data on its customers to learn more about their customers and potentially
use attributes as input into other analyses. Company B has segment data comprised of unique
segment attributes that they created based on their first party data. Company B wants to
provide the unique segment attributes to Company A only on customers that are overlapping
between their data and Company A data.

The companies decide to collaborate so that Company A can enrich the overlapping data.
Company A is the member who can query, and Company B is the contributor.

To create a collaboration and run list analysis in collaboration, the companies do the
following:

1. Company A creates a collaboration and creates a membership. The collaboration has
   Company B as another member on the collaboration. Company A enables query logging in the
   collaboration, and it enables query logging in its account.
2. Company B creates a membership in the collaboration. It enables query logging in its
   account.
3. Company A creates a CRM configured table
4. Company A adds the analysis rule to the customer configured table, as shown in the
   following example.

```
{
  "joinColumns": [
    "identifier1",
    "identifier2"
  ],
  "listColumns": [
    "internalid",
    "segment1",
    "segment2",
    "customercategory"
  ]
}
```

`joinColumns` – Company A wants to use `hashedemail`
and/or `thirdpartyid` (obtained from an identity vendor) to match customers
from CRM data to customers from segment data. This will help ensure Company A matches
enriched data for the right customers. They have two joinColumns to potentially improve
the match rate of the analysis.

`listColumns` – Company A uses `listColumns` to obtain
enriched columns beside an `internalid` they use within their own systems. They
add `segment1`, `segment2`, and `customercategory` to
potentially limit the enrichment to specific segments by using them in filters. 5. Company B creates a segment configured table. 6. Company B adds the analysis rule to the segment configured table.

```
{
  "joinColumns": [
    "identifier2"
  ],
  "listColumns": [
    "segment3",
    "segment4"
  ]
}
```

`joinColumns` – Company B enables Company A to join on
`identifier2` to match customers from segment data to CRM data. Company A and
Company B worked with the identity vendor to obtain `identifier2` which would
match for this collaboration. They didn't add other `joinColumns` because they
believed `identifier2` provides the highest and most accurate match rate and
other identifiers aren't required for the queries.

`listColumns` – Company B enables Company A to enrich their data
with `segment3` and `segment4` attributes which are unique
attributes they have created, collected and aligned on (with customer A) to be a part of
data enrichment. They want Company A to obtain these segments for the overlap at a
row-level because this is a data enrichment collaboration. 7. Company A creates a CRM table association to the collaboration. 8. Company B creates a segment table association to the collaboration. 9. Company A runs queries, such as the following one to enrich overlapping customer data.

```
SELECT companyA.internalid, companyB.segment3, companyB.segment4
INNER JOIN returns companyB
 ON companyA.identifier2 = companyB.identifier2
WHERE companyA.customercategory > 'xxx'
```

10. Company A and Company B review query logs. Company B verifies that the query aligns
    with what was agreed upon in the collaboration agreement.
