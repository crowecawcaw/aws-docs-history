# OpenSearch Piped Processing Language (PPL)

This section contains a basic introduction to querying CloudWatch Logs using OpenSearch PPL.
With PPL, you can retrieve, query, and analyze data using piped-together commands,
making it easier to understand and compose complex queries. Its syntax is based on
Unix pipes, and enables chaining of commands to transform and process data. With
PPL, you can filter and aggregate data, and use a rich set of math, string, date,
conditional, and other functions for analysis.

Including `SOURCE` in a PPL query is a useful way to specify the log
groups field indexes, and data sources to include in a query when you are using the
AWS CLI or API to create a query. The `SOURCE` command is supported only in
the AWS CLI and API, not in the CloudWatch console. When you use the CloudWatch
console to start a query, you use the console interface to specify the log groups
and data source name and type.

Use `aws:fieldIndex` to return indexed data only, by forcing a query to
scan only log groups that are indexed on a field that you specify in the query. The
relevant log groups are automatically selected, based on the fields specified in the
`filterIndex` command. This reduces scanned volume by
skipping log groups that do not have any log events containing the field specified
in the query, and only scanning log groups that match the value specified in the
query for this field index. Use `aws:fieldIndex` to specify the field
name, along with the field name and value in the source command to query only
indexed data containing the field and value specified. For more information, see
[Create field indexes to improve query performance and reduce scan volume](CloudWatchLogs-Field-Indexing.md "CloudWatchLogs-Field-Indexing.md")

You can use OpenSearch PPL for queries of log groups in the Standard Log Class.

###### Note

For information about all OpenSearch PPL query commands supported in CloudWatch Logs and
detailed information about syntax and restrictions, see [Supported
PPL commands](../../../opensearch-service/latest/developerguide/supported-ppl.md "../../../opensearch-service/latest/developerguide/supported-ppl.md") in the OpenSearch Service Developer Guide.

For information on other query languages you can use see, [CloudWatch Logs Insights](CWL_QuerySyntax.md "CWL_QuerySyntax.md"), [OpenSearch Service
SQL](CWL_AnalyzeLogData_SQL.md "CWL_AnalyzeLogData_SQL.md"), and [CloudWatch Metrics Insights](../monitoring/query_with_cloudwatch-metrics-insights.md "../monitoring/query_with_cloudwatch-metrics-insights.md")

| Command or function     | Example query                                                                                                                                 | Description                                                                                                                                                                                                                        |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| fields                  | `fields field1, field2`                                                                                                                       | Displays a set of fields which needs projection.                                                                                                                                                                                   |
| join                    | `LEFT JOIN left=l, right=r on l.id = r.id `join_right_lg`<br>                                                                                 | fields l.field_1, r.field_2`                                                                                                                                                                                                       | Joins two datasets together.                                                                                                                                                                                                                              |
| where                   | `where field1="success"                                                                                                                       | where field2 !=<br>"i-023fe0a90929d8822"                                                                                                                                                                                           | fields field3, field4, field5,field6<br>                                                                                                                                                                                                                  | head 1000`                                                                                                                                                                                                         | Filters the data based on the conditions that you<br>specify.                                                                                                                        |
| aws:fieldIndex          | `source = [`aws:fieldIndex`="region", `region` =<br>"us-west-2"]                                                                              | where status = 200                                                                                                                                                                                                                 | head 10`                                                                                                                                                                                                                                                  | Returns indexed data only, by forcing a query to scan only log<br>groups that are indexed on a field that you specify in the<br>query.                                                                             |
| stats                   | `stats count(), count(field1), min(field1), max(field1),<br>avg(field1) by field2                                                             | head 1000`                                                                                                                                                                                                                         | Performs aggregations and calculations                                                                                                                                                                                                                    |
| parse                   | `parse field1 ".\*/(?<field2>[^/]+$)"                                                                                                         | where field2<br>= "requestId"                                                                                                                                                                                                      | fields field1, field2                                                                                                                                                                                                                                     | head<br>1000`                                                                                                                                                                                                      | Extracts a regular expression (regex) pattern from a string<br>and displays the extracted pattern. The extracted pattern can be<br>further used to create new fields or filter data. |
| sort                    | `stats count(), count(field1), min(field1) as<br>field1Alias, max(`field1`), avg(`field1`) by field2                                          | sort<br>-field1Alias                                                                                                                                                                                                               | head 1000`                                                                                                                                                                                                                                                | Sort the displayed results by a field name. Use sort<br>-FieldName to sort in descending order.                                                                                                                    |
| eval                    | `eval field2 = field1<br>• 2                                                                                                                  | fields field1, field2                                                                                                                                                                                                              | head<br>20`                                                                                                                                                                                                                                               | Modifies or processes the value of a field and stores it in a<br>different field. This is useful to mathematically modify a<br>column, apply string functions to a column, or apply date<br>functions to a column. |
| rename                  | `rename field2 as field1                                                                                                                      | fields field1;`                                                                                                                                                                                                                    | Renames one or more fields in the search result.                                                                                                                                                                                                          |
| head                    | `fields `@message`                                                                                                                            | head 20`                                                                                                                                                                                                                           | Limits the displayed query results to the first N rows.                                                                                                                                                                                                   |
| top                     | `top 2 field1 by field2`                                                                                                                      | Finds the most frequent values for a field.                                                                                                                                                                                        |
| dedup                   | `dedup field1                                                                                                                                 | fields field1, field2,<br>field3`                                                                                                                                                                                                  | Removes duplicate entries based on the fields that you<br>specify.                                                                                                                                                                                        |
| rare                    | `rare field1 by field2`                                                                                                                       | Finds the least frequent values of all fields in the field<br>list.                                                                                                                                                                |
| subquery                | `where field_1 IN [ search source= `subquery_lg`                                                                                              | fields<br>field_2 ]                                                                                                                                                                                                                | fields id, field_1`                                                                                                                                                                                                                                       | Performs complex, nested queries within your PPL<br>statements.                                                                                                                                                    |
| trendline               | `trendline sma(2, field1) as field1Alias`                                                                                                     | Calculates the moving averages of fields.                                                                                                                                                                                          |
| eventStats              | `eventstats sum(field1) by field2`                                                                                                            | Enriches your event data with calculated summary statistics.<br>It analyzes specified fields within your events, computes<br>various statistical measures, and then appends these results to<br>each original event as new fields. |
| expand                  | `eval tags_array_string = json_extract(`@message`,<br>'$.tags')                                                                               | eval tags_array =<br>json_array(json_extract(tags_string, '$[0]'),<br>json_extract(tags_string, '$[1]'))                                                                                                                           | expand tags_array as<br>color_tags`                                                                                                                                                                                                                       | Breaks down a field containing multiple values into separate<br>rows, creating a new row for each value in the specified<br>field.                                                                                 |
| fillnull                | `fields `@timestamp`, error_code, status_code                                                                                                 | fillnull<br>using status_code = "UNKNOWN", error_code =<br>"UNKNOWN"`                                                                                                                                                              | Fills null fields with the value that you provide. It can be<br>used in one or more fields.                                                                                                                                                               |
| flatten                 | `eval metadata_struct = json_object('size',<br>json_extract(metadata_string, '$.size'), 'color',<br>json_extract(metadata_string, '$.color')) | flatten<br>metadata_struct as (meta_size, meta_color)`                                                                                                                                                                             | Flattens a field. The field must be of this type:<br>`struct<?,?>` or<br>`array<struct<?,?>>`.                                                                                                                                                            |
| cidrmatch               | `where cidrmatch(ip, '2003:db8::/32')                                                                                                         | fields ip`                                                                                                                                                                                                                         | Checks if the specified IP address is within the given CIDR<br>range.                                                                                                                                                                                     |
| fieldsummary            | `where field1 != 200                                                                                                                          | fieldsummary includefields= field1<br>nulls=true`                                                                                                                                                                                  | Calculates basic statistics for each field (count, distinct<br>count, min, max, avg, stddev, and mean).                                                                                                                                                   |
| grok                    | `grok email '.+@%{HOSTNAME:host}'                                                                                                             | fields email,<br>host`                                                                                                                                                                                                             | Parses a text field with a grok pattern and appends the<br>results to the search result.                                                                                                                                                                  |
| String functions        | `eval field1Len = LENGTH(field1)                                                                                                              | fields<br>field1Len`                                                                                                                                                                                                               | Built-in functions in PPL that can manipulate and transform<br>string and text data within PPL queries. For example, converting<br>case, combining strings, extracting parts, and cleaning<br>text.                                                       |
| Date-Time functions     | `eval newDate = ADDDATE(DATE('2020-08-26'), 1)                                                                                                | fields<br>newDate`                                                                                                                                                                                                                 | Built-in functions for handling and transforming date and<br>timestamp data in PPL queries. For example, date_add,<br>date_format, datediff, date-sub, timestampadd, timestampdiff,<br>current_timezone, utc_timestamp, and current_date.                 |
| Condition functions     | `eval field2 = isnull(field1)                                                                                                                 | fields field2, field1,<br>field3`                                                                                                                                                                                                  | Built-in functions that check for specific field conditions,<br>and evaluate expressions conditionally. For example, if field1<br>is null, return field2.                                                                                                 |
| Math functions          | `eval field2 = ACOS(field1)                                                                                                                   | fields field1`                                                                                                                                                                                                                     | Built-in functions for performing mathematical calculations<br>and transformations in PPL queries. For example, abs (absolute<br>value), round (rounds numbers), sqrt (square root), pow (power<br>calculation), and ceil (rounds up to nearest integer). |
| CryptoGraphic functions | `eval crypto = MD5(field)                                                                                                                     | head 1000`                                                                                                                                                                                                                         | To calculate the hash of given field                                                                                                                                                                                                                      |
| JSON functions          | `eval valid_json = json('[1,2,3,{"f1":1,"f2":[5,6]},4]')<br>                                                                                  | fields valid_json`                                                                                                                                                                                                                 | Built-in functions for handling JSON including arrays,<br>extracting, and validation. For example, json_object,<br>json_array, to_json_string, json_array_length, json_extract,<br>json_keys, and json_valid.                                             |

## Query scope

Including SOURCE in a query is a useful way to specify the log groups to
include in a query when you are using the AWS CLI or API to create a query. The
SOURCE command is supported only in the AWS CLI and API, not in the CloudWatch
console. When you use the CloudWatch console to start a query, you use the
console interface to specify the log groups and data source name and
type.

PPL's source command now support multiple ways to specify them:

1. Log group
2. Field indexes - New
3. Data source and type - New

### Log Group

Log Group source selection can be used when customers know which exact log
group(s) need to be searched

```
source = [lg:`/aws/lambda/my-function`] | where status = 200 | head 10
```

### Field Indexes

Field index-based source selection reduces the amount of data queried by
limiting results to only indexed data when your filters target fields that
have been indexed. The relevant log groups are automatically selected, based
on the fields specified in the `filterIndex` command. For more
information about field indexes and how to create them, see [Create field indexes to improve
query performance and reduce scan volume](CloudWatchLogs-Field-Indexing.md "CloudWatchLogs-Field-Indexing.md").

Use `aws:fieldIndex` to return indexed data only, by forcing a
query to scan only log groups that are indexed on a field that you specify
in the query. For these log groups that are indexed on this field, it
further optimizes the query by skipping the log groups that do not have any
log events containing the field specified in the query for the indexed
field. It further reduces scanned volume by attempting to scan only log
events from these log groups that match the value specified in the query for
this field index. For more information about field indexes and how to create
them, see Create field indexes to improve query performance and reduce scan
volume.

In PPL, `aws:fieldIndex` is used to specify which key value
pairs should be treated as indexes. The syntax is as follows

```
source = [`aws:fieldIndex`="region", `region` = "us-west-2"] | where status = 200 | head 10
```

where,

1. ``aws:fieldIndex`="region"` identifies region as field
   Index.
   1. Note: Instead of = customers can use IN to specify
      multiple indexes (example below)

2. ``region`="us-west-2"` identifies the filter condition
   to be applied
   1. Note: Instead of = customers can use IN to specify
      multiple values (example below)

Customers can specify multiple fieldIndexes as follows

```
source = [`aws:fieldIndex` IN ("status", "region"), `status` = 200, `region` IN ("us-west-2", "us-east-1")] | head 10
```

### Data Source and Type

Data source and type based source selection can be used when customers
know which exact data sources need to be queried. This query is executed
over one or more log groups which contain the specified data source and
type.

```
source = [ds:`data_source.type`] | where status = 200 | head 10
```

#### Supported PPL for data source queries

To support the use case for querying data sources in PPL, you can use
the dynamic source selector clause. Using this syntax, you can query
data sources by specifying them in the search command. You can specify
up to 10 data sources.

**Syntax**

```
source=[ds:`DataSource1.Type1`, ds:`DataSource2.Type2`, ...ds:`DataSourcen.Typen`]
```

**Example query**

```
search source=[ds:`DataSource1.Type1`, ds:`DataSource2.Type2`] | fields field1, field2
```

### Combined example

Customers can specify all the source selection operators in any order
& the results would be the intersection of the all the conditions
applied.

For example, /aws/lambda/my-function-1 might contain multiple data source
& types including wide variety of indexes, when the following query was
ran, the results returned will only have events of source and type
DataSource1.Type1 and matching the criteria of 'status' = 200.

```
search source=[
    ds:`DataSource1.Type1`,
    lg:`/aws/lambda/my-function-1`,
    `aws:fieldIndex` IN ("status"), `status` = 200
]
```

## Restrictions

The following restrictions apply when you use OpenSearch PPL to query in
CloudWatch Logs Insights.

- You cannot use join or subquery commands with data source
  queries.
