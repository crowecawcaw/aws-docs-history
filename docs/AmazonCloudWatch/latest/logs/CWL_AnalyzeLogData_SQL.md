

# OpenSearch Structured Query Language (SQL)
<a name="CWL_AnalyzeLogData_SQL"></a>

This section contains a basic introduction to querying CloudWatch Logs using OpenSearch SQL. It provides a familiar option if you're used to working with relational databases. OpenSearch SQL offers a subset of SQL functionality, making it a good choice for performing ad-hoc queries and data analysis tasks. With OpenSearch SQL, you can use commands such as SELECT, FROM, WHERE, GROUP BY, HAVING, and various other SQL commands and functions. You can execute JOINs across log groups, correlate data across log groups using sub-queries, and use the rich set of JSON, mathematical, string, conditional, and other SQL functions to perform powerful analysis on log and security data.

Use `filterIndex` to return indexed data only, by forcing a query to scan only log groups that are indexed on a field that you specify in the query. Reduce scanned volume by skipping log groups that do not have any log events containing the field specified in the query, and only scanning log groups that match the value specified in the query for this field index. Use `filterIndex` to specify the field name, along with the field name and value to query only indexed data containing the field and value specified.

You can use OpenSearch SQL for queries of log groups in the Standard Log Class. SQL also supports querying using data source name and data source type. 

**Note**  
The following table lists the SQL commands and functions supported in CloudWatch Logs For information about all OpenSearch SQL commands including syntax, see [Supported SQL commands](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-directquery-sql.html) in the OpenSearch Service Developer Guide.  
For information on other query languages you can use, see[CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html), [OpenSearch Service PPL](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_PPL.html), and [CloudWatch Metrics Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/query_with_cloudwatch-metrics-insights.html).

## Supported SQL commands
<a name="CWL_AnalyzeLogData_SQL-table"></a>

**Note**  
In the example query column, replace `{{<logGroup>}}` as needed depending on which data source you're querying. 


| Command or function | Example query | Description | 
| --- | --- | --- | 
| SELECT | `SELECT `@message`, Operation FROM `LogGroupA`` | Displays projected values. | 
| FROM | `SELECT `@message`, Operation FROM `LogGroupA`` | Built-in clause that specifies the source table(s) or view(s) from which to retrieve data, supporting various types of joins and subqueries. | 
| WHERE | `SELECT * FROM `LogGroupA` WHERE Operation = 'x'` | Filters log events based on the provided field criteria. | 
| filterIndex | `SELECT * FROM `filterIndex('region' = 'us-east-1')` WHERE status = 200 LIMIT 10;` | Returns indexed data only, by forcing a query to scan only log groups that are indexed on a field that you specify in the query. | 
| GROUP BY | `SELECT `@logStream`, COUNT(*) as log_count FROM `LogGroupA` GROUP BY `@logStream`` | Groups log events based on category and finds the average based on stats. | 
| HAVING | `SELECT `@logStream`, COUNT(*) as log_count FROM `LogGroupA` GROUP BY `@logStream` HAVING log_count > 100` | Filters the results based on grouping conditions. | 
| ORDER BY | `SELECT * FROM `LogGroupA` ORDER BY `@timestamp` DESC` | Orders the results based on fields in the ORDER BY clause. You can sort in either descending or ascending order. | 
| JOIN | `SELECT A.`@message`, B.`@timestamp`FROM `LogGroupA` as A INNER JOIN `LogGroupB` as B ON A.`requestId` = B.`requestId`` | Joins the results for two tables based on common fields. Inner JOIN or Left Outer Join must be specified | 
| LIMIT | `Select * from `LogGroupA` limit 10` | Limits the displayed query results to the first N rows. | 
| String functions | `SELECT upper(Operation) , lower(Operation), Operation FROM `LogGroupA`` | Built-in functions in SQL that can manipulate and transform string and text data within SQL queries. For example, converting case, combining strings, extracting parts, and cleaning text. | 
| Date functions | `SELECT current_date() as today, date_add(current_date(), 30) as thirty_days_later, last_day(current_date()) as month_end FROM `LogGroupA`` | Built-in functions for handling and transforming date and timestamp data in SQL queries. For example, date\_add, date\_format, datediff, and current\_date. | 
| Conditional functions | `SELECT Operation, IF(Error > 0, 'High', 'Low') as error_category FROM `LogGroupA`;` | Built-in functions that perform actions based on specified conditions, or that evaluate expressions conditionally. For example, CASE and IF. | 
| Aggregate functions | `SELECT AVG(bytes) as bytesWritten FROM `LogGroupA`` | Built-in functions that perform calculations on multiple rows to produce a single summarized value. For example, SUM, COUNT, AVG, MAX, and MIN. | 
| JSON functions | `SELECT get_json_object(json_column, '$.name') as name FROM `LogGroupA`` | Built-in functions for parsing, extracting, modifying, and querying JSON-formatted data within SQL queries (e.g., from\_json, to\_json, get\_json\_object, json\_tuple) allowing manipulation of JSON structures in datasets. | 
| Array functions | `SELECT scores, size(scores) as length, array_contains(scores, 90) as has_90 FROM `LogGroupA`;` | Built-in functions for working with array-type columns in SQL queries, allowing operations like accessing, modifying, and analyzing array data (e.g., size, explode, array\_contains). | 
| Window functions | `SELECT field1, field2, RANK() OVER (ORDER BY field2 DESC) as field2Rank FROM `LogGroupA`;` | Built-in functions that perform calculations across a specified set of rows related to the current row (window), enabling operations like ranking, running totals, and moving averages. For example, ROW\_NUMBER, RANK, LAG, and LEAD | 
| Conversion functions | `SELECT CAST('123' AS INT) as converted_number, CAST(123 AS STRING) as converted_string FROM `LogGroupA`` | Built-in functions for converting data from one type to another within SQL queries, enabling data type transformations and format conversions. For example, CAST, TO\_DATE, TO\_TIMESTAMP, and BINARY. | 
| Predicate functions | `SELECT scores, size(scores) as length, array_contains(scores, 90) as has_90 FROM `LogGroupA`;` | Built-in functions that evaluate conditions and return boolean values (true/false) based on specified criteria or patterns. For example, IN, LIKE, BETWEEN, IS NULL, and EXISTS. | 
| Select multiple log groups | `SELECT lg1.field1, lg1.field2 from `logGroups( logGroupIdentifier: ['LogGroup1', 'LogGroup2'])` as lg1 where lg1.field3= "Success"` | Enables you to specify multiple log groups in a SELECT statement | 
| Select multiple data sources | `SELECT ds1.field1, ds1.field2 from `dataSource(['DataSource1', 'DataSource2'])` as ds1 where ds1.field3= "Success"` | Enables you to specify multiple data sources in a SELECT statement | 

## Supported SQL for multi-log-group queries
<a name="CWL_AnalyzeLogData_SQL-multi"></a>

To support the use case for querying multiple log groups in SQL, you can use the `logGroups` command. Using this syntax, you can query multiple log groups by specifying them in the FROM command.

Syntax:

```
`logGroups(
    logGroupIdentifier: ['LogGroup1','LogGroup2', ...'LogGroupn']
)
```

In this syntax, you can specify up to 50 log groups in the `logGroupIdentifier` parameter. To reference log groups in a monitoring account, use ARNs instead of `LogGroup` names.

Example query:

```
SELECT LG1.Column1, LG1.Column2 from `logGroups(
    logGroupIdentifier: ['LogGroup1', 'LogGroup2']
)` as LG1 WHERE LG1.Column1 = 'ABC'
```

The following syntax involving multiple log groups after the `FROM` statement is NOT supported when querying CloudWatch Logs.

```
SELECT Column1, Column2 FROM 'LogGroup1', 'LogGroup2', ...'LogGroupn'
WHERE Column1 = 'ABC'
```

## Supported SQL for data source queries
<a name="CWL_AnalyzeLogData_SQL-data-source"></a>

 To support the use case for querying data sources in SQL, you can use the dataSource command. Using this syntax, you can query data sources by specifying them in the `FROM` command. You can specify up to 10 data sources. 

**Syntax**

```
`dataSource(
    ['DataSource1', 'DataSource2', ...'DataSourcen']
)`
```

**Example query **

```
SELECT DS1.Column1, DS1.Column2 from `dataSource(
    ['DataSource1', 'DataSource2']
)` as DS1 WHERE DS1.Column1 = 'ABC'
```

## Query scope
<a name="CWL_AnalyzeLogData_SQL-scope"></a>

In the AWS CLI and API, you can specify which logs to query by using the log group, data source and type, and field indexes.

### Log Group
<a name="CWL_AnalyzeLogData_SQL-scope-loggroup"></a>

Log Group source selection can be used when customers know which exact log group(s) need to be searched

```
SELECT * FROM `logGroups(logGroupIdentifier: ['/aws/lambda/my-function'])`;
```

### Data Source and Type
<a name="CWL_AnalyzeLogData_SQL-scope-datasource"></a>

Customers can query their logs using data source name and data source type.

Data source and type based source selection can be used when customers know which exact data sources need to be queried. This query is executed over one or more log groups which contain the specified data source and type.

To support the use case for querying data sources in SQL, you can use the dataSource command. Using this syntax, you can query data sources by specifying them in the FROM command. You can specify up to 10 data sources.

Syntax:

```
`dataSource(
    ['DataSource1.Type1', 'DataSource2.Type2', ...'DataSourcen.Typen']
)`
```

Example query:

```
SELECT DS1.Column1, DS1.Column2 from `dataSource(
    ['DataSource1.Type1', 'DataSource2.Type2']
)` as DS1 WHERE DS1.Column1 = 'ABC'
```

For more information on querying by data sources, see [Use facets to group and explore logs](CloudWatchLogs-Facets.md).

### Combined example
<a name="CWL_AnalyzeLogData_SQL-scope-combined"></a>

Customers can specify all the source selection operators within the backticks in any order and the results would be based on the intersection of the all the conditions applied.

For example, /aws/lambda/my-function-1 might contain multiple data source & types including wide variety of indexes, when the following query was ran, the results returned will only have events of source and type DataSource1.Type1 and matching the criteria of 'status' = 200.

```
SELECT * FROM `
   logGroups(logGroupIdentifier: ['/aws/lambda/my-function'])
   filterIndex('status' = 200)
   dataSource(['DataSource1.Type1'])
`;
```

### Field Indexes
<a name="CWL_AnalyzeLogData_SQL-scope-fieldindex"></a>

Field Index-based source selection automatically identifies relevant log groups when your filters target indexed fields, reducing scan volume and query runtime. 

Use `filterIndex` to return indexed data only, by forcing a query to scan only log groups that are indexed on a field that you specify in the query. For these log groups that are indexed on this field, it further optimizes the query by skipping the log groups that do not have any log events containing the field specified in the query for the indexed field. It further reduces scanned volume by attempting to scan only log events from these log groups that match the value specified in the query for this field index. For more information about field indexes and how to create them, see [Create field indexes to improve query performance and reduce scan volume](CloudWatchLogs-Field-Indexing.md).

In SQL, filterIndex is used to specify which key value pairs should be treated as indexes. The syntax is as follows

```
SELECT * FROM `filterIndex('region' = 'us-east-1')`;
```

where,

1. filterIndex(...) specifies, treat the key values within them as field indexes. Each key value pair is separated by a comma (example below)

1. 'region' = 'us-east-1' specifies the actual condition to be applied

   1. Note: Instead of = customers can use IN to specify multiple values (example below)

Using multiple filterIndex would combine the conditions using "AND". In the example, logs matching status=200 and region in us-east-1 or us-west-2 would be queried.

```
SELECT * FROM `filterIndex('status' = 200, 'region' IN ['us-east-1', 'us-west-2'])`;
```

## Restrictions
<a name="CWL_AnalyzeLogData_SQL-restrictions"></a>

The following restrictions apply when you use OpenSearch SQL to query in CloudWatch Logs Insights.
+ You can include only one JOIN in a SELECT statement.
+ You cannot use JOIN or subqueries with data source queries.
+ Only one level of nested subqueries is supported.
+ Multiple statement queries separated by semi-colons (;) aren't supported.
+ Queries containing field names that are identical but differ only in case (such as field1 and FIELD1) are not supported.

  For example, the following query isn't supported:

  ```
  Select AWSAccountId, AwsAccountId from LogGroup
  ```

  However, the following query is supported because the field name (`@logStream`) is identical in both log groups:

  ```
  Select a.`@logStream`, b.`@logStream` from Table A INNER Join Table B on a.id = b.id
  ```
+ Functions and expressions must operate on field names and be part of a SELECT statement with a log group specified in the FROM clause.

  For example, this query is not supported:

  ```
  SELECT cos(10) FROM LogGroup
  ```

  This query is supported:

  ```
  SELECT cos(field1) FROM LogGroup
  ```
+ When using SQL or PPL commands, enclose certain fields in backticks to successfully query them. Backticks are necessary for fields with special characters (non-alphabetic and non-numeric). For example, enclose `@message`, `Operation.Export`, and `Test::Field` in backticks. You don't need to enclose fields with purely alphabetic names in backticks.

  Example query with simple fields:

  ```
  SELECT SessionToken, Operation, StartTime  FROM `LogGroup-A`
  LIMIT 1000;
  ```

  Similar query with backticks appended:

  ```
  SELECT `@SessionToken`, `@Operation`, `@StartTime`  FROM `LogGroup-A` LIMIT 1000;
  ```