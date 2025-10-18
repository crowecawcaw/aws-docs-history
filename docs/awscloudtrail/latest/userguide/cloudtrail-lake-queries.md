# CloudTrail Lake queries

Queries in CloudTrail Lake are authored in SQL. You can build a query
 on the CloudTrail Lake **Editor** tab by writing the query in SQL from
 scratch, by opening a saved or sample query and editing it, or by using the query generator 
 to produce a query from an English language prompt. You cannot overwrite an included sample
 query with your changes, but you can save it as a new query. For more information about
 the SQL query language that is allowed, 
 see [CloudTrail Lake SQL constraints](query-limitations.md "query-limitations.md").

An unbounded query (such as `SELECT * FROM
 `edsID``) scans all data in your event data store. To
 help control costs, we recommend that you constrain queries by adding starting and
 ending `eventTime` time stamps to queries. The following is an example that
 searches for all events in a specified event data store where the event time is after
 (`>`) January 5, 2023 at 1:51 p.m. and before (`<`) January
 19, 2023 at 1:51 p.m. Because an event data store has a minimum retention period of
 seven days, the minimum time span between starting and ending `eventTime`
 values is also seven days.


```
SELECT *
FROM `eds-ID`
WHERE
     eventtime >='2023-01-05 13:51:00' and eventtime < ='2023-01-19 13:51:00'
```
For information about how to optimize your queries, 
 see [Optimize CloudTrail Lake queries](lake-queries-optimization.md "lake-queries-optimization.md").

###### Topics

* [Query editor tools](#query-editor-format-controls "#query-editor-format-controls")
* [Create CloudTrail Lake queries from natural language
 prompts](lake-query-generator.md "lake-query-generator.md")
* [View sample queries with the CloudTrail console](lake-console-queries.md "lake-console-queries.md")
* [Create or edit a query with the CloudTrail console](query-create-edit-query.md "query-create-edit-query.md")
* [Run a query and save query results with the console](query-run-query.md "query-run-query.md")
* [View query results with the console](query-results.md "query-results.md")
* [Summarize query results in natural language](query-results-summary.md "query-results-summary.md")
* [Download saved query results](view-download-cloudtrail-lake-query-results.md "view-download-cloudtrail-lake-query-results.md")
* [Validate CloudTrail Lake saved query results](cloudtrail-query-results-validation.md "cloudtrail-query-results-validation.md")
* [Optimize CloudTrail Lake queries](lake-queries-optimization.md "lake-queries-optimization.md")
* [Run and manage CloudTrail Lake queries with the AWS CLI](lake-queries-cli.md "lake-queries-cli.md")

## Query editor tools


A toolbar at the upper right of the query editor offers commands to help author
 and format your SQL query.



![Query editor toolbar](images/query-editor-toolbar.png)

The following list describes the commands on the toolbar.



* **Undo** – Reverts the last content change made in the
 query editor.
* **Redo** – Repeats the last content change made in the
 query editor.
* **Format selected** – Arranges the query editor content
 according to SQL formatting and spacing conventions.
* **Comment/uncomment selected** - Comments the selected portion of the query if it is not already commented. If the selected portion is already commented, choosing this option removes the comment.
