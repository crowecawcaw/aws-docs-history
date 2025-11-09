# OpenSearch Structured Query Language

(SQL)

This section contains a basic introduction to querying CloudWatch Logs using OpenSearch SQL.
It provides a familiar option if you're used to working with relational databases.
OpenSearch SQL offers a subset of SQL functionality, making it a good choice for
performing ad-hoc queries and data analysis tasks. With OpenSearch SQL, you can use
commands such as SELECT, FROM, WHERE, GROUP BY, HAVING, and various other SQL
commands and functions. You can execute JOINs across log groups, correlate data
across log groups using sub-queries, and use the rich set of JSON, mathematical,
string, conditional, and other SQL functions to perform powerful analysis on log and
security data.

You can use OpenSearch SQL only for queries of log groups in the Standard Log
Class.

###### Note

The following table lists the SQL commands and functions supported in CloudWatch Logs
For information about all OpenSearch SQL commands including syntax, see [Supported SQL commands](../../../opensearch-service/latest/developerguide/supported-directquery-sql.md "../../../opensearch-service/latest/developerguide/supported-directquery-sql.md") in the OpenSearch Service Developer Guide.

For information on other query languages you can use, see[CloudWatch Logs Insights](CWL_QuerySyntax.md "CWL_QuerySyntax.md"), [OpenSearch Service
PPL](CWL_AnalyzeLogData_PPL.md "CWL_AnalyzeLogData_PPL.md"), and [CloudWatch Metrics Insights](../monitoring/query_with_cloudwatch-metrics-insights.md "../monitoring/query_with_cloudwatch-metrics-insights.md").

## Supported SQL commands

###### Note

In the example query column, replace
`<logGroup>` as needed
depending on which data source you're querying.

| Command or function        | Example query                                                                                                                                        | Description                                                                                                                                                                                                                                      |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| SELECT                     | `SELECT `@message`, Operation FROM<br>`LogGroupA``                                                                                                   | Displays projected values.                                                                                                                                                                                                                       |
| FROM                       | `SELECT `@message`, Operation FROM<br>`LogGroupA``                                                                                                   | Built-in clause that specifies the source table(s) or<br>view(s) from which to retrieve data, supporting various<br>types of joins and subqueries.                                                                                               |
| WHERE                      | `SELECT<br>• FROM `LogGroupA` WHERE Operation =<br>'x'`                                                                                              | Filters log events based on the provided field<br>criteria.                                                                                                                                                                                      |
| GROUP BY                   | `SELECT `@logStream`, COUNT(*) as log_count FROM<br>`LogGroupA`GROUP BY`@logStream``                                                                 | Groups log events based on category and finds the<br>average based on stats.                                                                                                                                                                     |
| HAVING                     | `SELECT `@logStream`, COUNT(*) as log_count FROM<br>`LogGroupA`GROUP BY`@logStream` HAVING log_count ><br>100`                                       | Filters the results based on grouping conditions.                                                                                                                                                                                                |
| ORDER BY                   | `SELECT<br>• FROM `LogGroupA`ORDER BY`@timestamp`<br>DESC`                                                                                           | Orders the results based on fields in the ORDER BY clause.<br>You can sort in either descending or ascending order.                                                                                                                              |
| JOIN                       | `SELECT A.`@message`, B.`@timestamp`FROM `LogGroupA`<br>as A INNER JOIN `LogGroupB` as B ON A.`requestId` =<br>B.`requestId``                        | Joins the results for two tables based on common fields.<br>Inner JOIN or Left Outer Join must be specified                                                                                                                                      |
| LIMIT                      | `Select<br>• from `LogGroupA` limit 10`                                                                                                              | Limits the displayed query results to the first N<br>rows.                                                                                                                                                                                       |
| String functions           | `SELECT upper(Operation) , lower(Operation),<br>Operation FROM `LogGroupA``                                                                          | Built-in functions in SQL that can manipulate and<br>transform string and text data within SQL queries. For<br>example, converting case, combining strings, extracting<br>parts, and cleaning text.                                              |
| Date functions             | `SELECT current_date() as today,<br>date_add(current_date(), 30) as thirty_days_later,<br>last_day(current_date()) as month_end FROM<br>`LogGroupA`` | Built-in functions for handling and transforming date and<br>timestamp data in SQL queries. For example, date_add,<br>date_format, datediff, and current_date.                                                                                   |
| Conditional functions      | `SELECT Operation, IF(Error > 0, 'High', 'Low') as<br>error_category FROM `LogGroupA`;`                                                              | Built-in functions that perform actions based on specified<br>conditions, or that evaluate expressions conditionally. For<br>example, CASE and IF.                                                                                               |
| Aggegrate functions        | `SELECT AVG(bytes) as bytesWritten FROM<br>`LogGroupA``                                                                                              | Built-in functions that perform calculations on multiple<br>rows to produce a single summarized value. For example, SUM,<br>COUNT, AVG, MAX, and MIN.                                                                                            |
| JSON functions             | `SELECT get_json_object(json_column, '$.name') as<br>name FROM `LogGroupA``                                                                          | Built-in functions for parsing, extracting, modifying, and<br>querying JSON-formatted data within SQL queries (e.g.,<br>from_json, to_json, get_json_object, json_tuple) allowing<br>manipulation of JSON structures in datasets.                |
| Array functions            | `SELECT scores, size(scores) as length,<br>array_contains(scores, 90) as has_90 FROM<br>`LogGroupA`;`                                                | Built-in functions for working with array-type columns in<br>SQL queries, allowing operations like accessing, modifying,<br>and analyzing array data (e.g., size, explode,<br>array_contains).                                                   |
| Window functions           | `SELECT field1, field2, RANK() OVER (ORDER BY field2<br>DESC) as field2Rank FROM `LogGroupA`;`                                                       | Built-in functions that perform calculations across a<br>specified set of rows related to the current row (window),<br>enabling operations like ranking, running totals, and moving<br>averages. For example, ROW_NUMBER, RANK, LAG, and<br>LEAD |
| Conversion functions       | `SELECT CAST('123' AS INT) as converted_number,<br>CAST(123 AS STRING) as converted_string FROM<br>`LogGroupA``                                      | Built-in functions for converting data from one type to<br>another within SQL queries, enabling data type<br>transformations and format conversions. For example, CAST,<br>TO_DATE, TO_TIMESTAMP, and BINARY.                                    |
| Predicate functions        | `SELECT scores, size(scores) as length,<br>array_contains(scores, 90) as has_90 FROM<br>`LogGroupA`;`                                                | Built-in functions that evaluate conditions and return<br>boolean values (true/false) based on specified criteria or<br>patterns. For example, IN, LIKE, BETWEEN, IS NULL, and<br>EXISTS.                                                        |
| Select multiple log groups | `SELECT lg1.field1, lg1.field2 from `logGroups(<br>logGroupIdentifier: ['LogGroup1', 'LogGroup2'])` as lg1<br>where lg1.field3= "Success"`           | Enables you to specify multiple log groups in a SELECT<br>statement                                                                                                                                                                              |

## Supported SQL for multi-log-group

queries

To support the use case for querying multiple log groups in SQL, you can use
the `logGroups` command. Using this syntax, you can query multiple
log groups by specifying them in the FROM command.

Syntax:

```
`logGroups(
    logGroupIdentifier: ['LogGroup1','LogGroup2', ...'LogGroupn']
)
```

In this syntax, you can specify up to 50 log groups in the
`logGroupIdentifier` parameter. To reference log groups in a
monitoring account, use ARNs instead of `LogGroup` names.

Example query:

```
SELECT LG1.Column1, LG1.Column2 from `logGroups(
    logGroupIdentifier: ['LogGroup1', 'LogGroup2']
)` as LG1 WHERE LG1.Column1 = 'ABC'
```

The following syntax involving multiple log groups after the `FROM`
statement is NOT supported when querying CloudWatch Logs.

```
SELECT Column1, Column2 FROM 'LogGroup1', 'LogGroup2', ...'LogGroupn'
WHERE Column1 = 'ABC'
```

## Restrictions

The following restrictions apply when you use OpenSearch SQL to query in
CloudWatch Logs Insights.

- You can include only one JOIN in a SELECT statement.
- Only one level of nested subqueries is supported.
- Multiple statement queries separated by semi-colons (;) aren't
  supported.
- Queries containing field names that are identical but differ only in
  case (such as field1 and FIELD1) are not supported.

For example, the following query isn't supported:

```
Select AWSAccountId, AwsAccountId from LogGroup
```

However, the following query is supported because the field name
(`@logStream`) is identical in both log groups:

```
Select a.`@logStream`, b.`@logStream` from Table A INNER Join Table B on a.id = b.id
```

- Functions and expressions must operate on field names and be part of a
  SELECT statement with a log group specified in the FROM clause.

For example, this query is not supported:

```
SELECT cos(10) FROM LogGroup
```

This query is supported:

```
SELECT cos(field1) FROM LogGroup
```

- When using SQL or PPL commands, enclose certain fields in backticks to
  successfully query them. Backticks are necessary for fields with special
  characters (non-alphabetic and non-numeric). For example, enclose
  `@message`, `Operation.Export`, and
  `Test::Field` in backticks. You don't need to enclose
  fields with purely alphabetic names in backticks.

Example query with simple fields:

```
SELECT SessionToken, Operation, StartTime  FROM `LogGroup-A`
LIMIT 1000;
```

Similar query with backticks appended:

```
SELECT `@SessionToken`, `@Operation`, `@StartTime`  FROM `LogGroup-A` LIMIT 1000;
```
