# filterIndex

Use `filterIndex` to return indexed data only, by forcing a
query to scan only log groups that are indexed on a field that you specify
in the query. For these log groups that are indexed on this field, it
further optimizes the query by skipping the log groups that do not have any
log events containing the field specified in the query for the indexed
field. It further reduces scanned volume by attempting to scan only log
events from these log groups that match the value specified in the query for
this field index. For more information about field indexes and how to create
them, see [Create field indexes to improve query
performance and reduce scan volume](CloudWatchLogs-Field-Indexing.md "CloudWatchLogs-Field-Indexing.md").

Using `filterIndex` with indexed fields can help you query log
groups that include petabytes of log data efficiently by limiting the actual
search space to log groups and log events that have field indexes.

For example, suppose that you have created a field index for
`IPaddress` in some of the log groups in your account. You
can then create the following query and choose to query all log groups in
the account to find log events that include the value
`198.51.100.0` in the `IPaddress` field.

````
fields @timestamp, @message
| filterIndex IPaddress = "198.51.100.0"
| limit 20 ``` The `filterIndex` command causes this query to attempt to skip all log groups that are not indexed for `IPaddress`. Additionally, within the log groups that are indexed, the query skips log events that have an `IPaddress` field but not observed `198.51.100.0` as the value for that field. Use the `IN` operator to expand the results to any of multiple values for the indexed fields. The following example finds logs events that include either the value `198.51.100.0` or `198.51.100.1` in the `IPaddress` field. ``` fields @timestamp, @message
| filterIndex IPaddress in ["198.51.100.0", "198.51.100.1"]
| limit 20 ``` CloudWatch Logs provides default field indexes for all log groups in the Standard log class. Default field indexes are automatically available for the following fields: <br>• `@logStream` <br>• `@aws.region` <br>• `@aws.account` <br>• `@source.log` <br>• `traceId` Default field indexes are in addition to any custom field indexes you define within your policy. Default field indexes are not counted towards your [field index quota](CloudWatchLogs-Field-Indexing-Syntax.md "CloudWatchLogs-Field-Indexing-Syntax.md"). ## filterIndex compared to filter To illustrate the difference between `filterIndex` and `filter`, consider the following example queries. Assume that you have created a field index for `IPaddress`, for four of your log groups, but not for a fifth log group. The following query using `filterIndex` will skip scanning the log group that doesn't have the field indexed. For each indexed log group, it attempts to scan only log events that have the indexed field, and it also returns only results from after the field index was created. ``` fields @timestamp, @message
| filterIndex IPaddress = "198.51.100.0"
| limit 20 ``` In contrast, if you use `filter` instead of `filterIndex` for a query of the same five log groups, the query will attempt to scan not only the log events that contain the value in the indexed log groups, but will also scan the fifth log group that isn't indexed, and it will scan every log event in that fifth log group. ``` fields @timestamp, @message
| filter IPaddress = "198.51.100.0"
| limit 20 ```
````
