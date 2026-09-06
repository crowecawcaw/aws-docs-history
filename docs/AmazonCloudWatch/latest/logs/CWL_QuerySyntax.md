

# CloudWatch Logs Insights language query syntax
<a name="CWL_QuerySyntax"></a>

 This section provides details about the Logs Insights QL. The query syntax supports different functions and operations that include but aren't limited to general functions, arithmetic and comparison operations, and regular expressions.

**Important**  
To avoid incurring excessive charges by running large queries, keep in mind the following best practices:  
Select only the necessary log groups for each query.
Always specify the narrowest possible time range for your queries.
When you use the console to run queries, cancel all your queries before you close the CloudWatch Logs Insights console page. Otherwise, queries continue to run until completion.
When you add a CloudWatch Logs Insights widget to a dashboard, ensure that the dashboard is not refreshing at a high frequency, because each refresh starts a new query.

To create queries that contain multiple commands, separate the commands with the pipe character (**\|**).

To create queries that contain comments, set off the comments with the hash character (**\#**). 

**Note**  
 CloudWatch Logs Insights automatically discovers fields for different log types and generates fields that start with the **@** character. For more information about these fields, see [ Supported logs and discovered fields](https://docs.aws.amazon.com/en_us/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData-discoverable-fields.html) in the *Amazon CloudWatch User Guide*. 

The following table briefly describes each command. Following this table is a more comprehensive description of each command, with examples.

**Note**  
All Logs Insights QL query commands are supported on log groups in the Standard log class. Log groups in the Infrequent Access log class support all Logs Insights QL query commands except `pattern`, `diff`, and `unmask`.


|  |  | 
| --- |--- |
| **` addtotals`** | Computes row totals and column totals for numeric fields.  | 
| **` anomaly`** | Identifies unusual patterns in your log data using machine learning.  | 
| **` display`** |  Displays a specific field or fields in query results.  | 
| **` fields`** |  Displays specific fields in query results and supports functions and operations you can use to modify field values and create new fields to use in your query.  | 
| **` filter`** |  Filters the query to return only the log events that match one or more conditions.  | 
| **` filterIndex`** |  Forces a query to attempt to scan only the log groups that are both indexed on the field mentioned in a field index and also contain a value for that field index. This reduces scanned volume by attempting to scan only log events from these log groups that contain the value specified in the query for this field index. <br />This command is not supported for log groups in the Infrequent Access log class. | 
| **` pattern`** | Automatically clusters your log data into patterns. A pattern is shared text structure that recurs among your log fields. CloudWatch Logs Insights provides ways for you to analyze the patterns found in your log events. For more information, see [Pattern analysis](CWL_AnalyzeLogData_Patterns.md). | 
| **` diff`** | Compares the log events found in your requested time period with the log events from a previous time period of equal length, so that you can look for trends and find out if certain log events are new. | 
| **` parse`** |  Extracts data from a log field to create an extracted field that you can process in your query. **`parse`** supports both glob mode using wildcards, and regular expressions.  | 
| **` sort`** | Displays the returned log events in ascending (`asc`) or descending (`desc`) order.  | 
| **` SOURCE`** | Including `SOURCE` in a query is a useful way to specify a large amount of log groups to include in a query based on log group name prefix, account identifiers, log group class, data sources, or log group tags. This command is supported only when you create a query in the AWS CLI or programmatically, not in the CloudWatch console.  | 
| **` stats`** |  Calculate aggregate statistics using values in the log fields.  | 
| **` limit`** | Specifies a maximum number of log events that you want your query to return. Useful with **`sort`** to return "top 20" or "most recent 20" results. Use `limit any` to stop scanning early once enough results are found. | 
| **` dedup`** |  Removes duplicate results based on specific values in fields that you specify. | 
| **` unmask`** |  Displays all the content of a log event that has some content masked because of a data protection policy. For more information about data protection in log groups, see [Help protect sensitive log data with masking](mask-sensitive-log-data.md).  | 
|  **`[unnest](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Unnest.html)`**  |  Flattens a list taken as input to produce multiple records with a single record for each element in the list.  | 
| **` lookup`** | Enriches log events with data from a lookup table by matching field values. Use lookup tables to add reference data such as user details, application names, or product information to your query results. | 
| **` join`** | Combines log events from a source log group with events from another log group or query result based on a matching field. Use the join command to correlate related log events across different sources using keys common across them such as matching request identifiers or transaction IDs. | 
| **` subqueries`** | A subquery is a nested Logs Insights query that can be used as an input to another query. Subqueries can be used to derive intermediate result sets that are then consumed by subsequent commands. | 
| **` autoregress`** | Creates lagged (previous-row) copies of a field's values. | 
| **` logcompare`** | Compares the current time window against a baseline window shifted back by a duration. | 
| **` filldown`** | Carries the last non-null value forward to fill gaps. | 
| **` fillmissing`** | Inserts rows for empty time bins after stats by bin(), optionally filling fields with a constant. | 
| **` cidrlookup`** | Enriches events by matching an IP field against CIDR ranges in a lookup table. | 
| **` outlier`** | Detects statistical outliers based on the interquartile range (IQR) and can remove or transform outlier rows. | 
| **` accum`** | Computes a running cumulative sum of a numeric field. | 
| **` appendcols`** | Appends columns from a sub-query to the current results by positional row matching. | 
| **` sessionize`** | Groups events into sessions by identity fields and inactivity gap. | 
| **` countFrequent`** | Returns an approximate count of each unique field-value combination, sorted in descending order. | 
| **` where`** | Acts as a grammar alias for the `filter` command and accepts identical syntax. | 
| ** [Other operations and functions](CWL_QuerySyntax-operations-functions.md)** | CloudWatch Logs Insights also supports many comparison, arithmetic, datetime, numeric, string, IP address, and general functions and operations.  | 

The following sections provide more details about the CloudWatch Logs Insights query commands.

**Topics**
+ [Logs Insights QL commands supported in log classes](CWL_AnalyzeLogData_Classes.md)
+ [addtotals](CWL_QuerySyntax-Addtotals.md)
+ [anomaly](CWL_QuerySyntax-Anomaly.md)
+ [**display**](CWL_QuerySyntax-Display.md)
+ [fields](CWL_QuerySyntax-Fields.md)
+ [filter](CWL_QuerySyntax-Filter.md)
+ [filterIndex](CWL_QuerySyntax-FilterIndex.md)
+ [SOURCE](CWL_QuerySyntax-Source.md)
+ [pattern](CWL_QuerySyntax-Pattern.md)
+ [diff](CWL_QuerySyntax-Diff.md)
+ [parse](CWL_QuerySyntax-Parse.md)
+ [relevantfields](CWL_QuerySyntax-RelevantFields.md)
+ [expand](CWL_QuerySyntax-Expand.md)
+ [sort](CWL_QuerySyntax-Sort.md)
+ [stats](CWL_QuerySyntax-Stats.md)
+ [limit](CWL_QuerySyntax-Limit.md)
+ [dedup](CWL_QuerySyntax-Dedup.md)
+ [unmask](CWL_QuerySyntax-Unmask.md)
+ [unnest](CWL_QuerySyntax-Unnest.md)
+ [lookup](CWL_QuerySyntax-Lookup.md)
+ [join](CWL_QuerySyntax-Join.md)
+ [subqueries](CWL_QuerySyntax-Subqueries.md)
+ [autoregress](CWL_QuerySyntax-Autoregress.md)
+ [logcompare](CWL_QuerySyntax-Logcompare.md)
+ [filldown](CWL_QuerySyntax-Filldown.md)
+ [fillmissing](CWL_QuerySyntax-Fillmissing.md)
+ [cidrlookup](CWL_QuerySyntax-Cidrlookup.md)
+ [outlier](CWL_QuerySyntax-Outlier.md)
+ [accum](CWL_QuerySyntax-Accum.md)
+ [appendcols](CWL_QuerySyntax-Appendcols.md)
+ [sessionize](CWL_QuerySyntax-Sessionize.md)
+ [countFrequent](CWL_QuerySyntax-CountFrequent.md)
+ [where](CWL_QuerySyntax-Where.md)
+ [Boolean, comparison, numeric, datetime, and other functions](CWL_QuerySyntax-operations-functions.md)
+ [Hashing functions](CWL_QuerySyntax-hash-functions.md)
+ [Time-series functions](CWL_QuerySyntax-timeseries-functions.md)
+ [Fields that contain special characters](CWL_QuerySyntax-Guidelines.md)
+ [Use aliases and comments in queries](CWL_QuerySyntax-alias.md)