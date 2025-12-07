# Create field indexes to improve query

performance and reduce scan volume

You can create _field indexes_ of fields in your log events for
efficient equality-based searches. When you then use a field index in a CloudWatch Logs Insights query,
the query attempts to skip processing log events that are known to not include the
indexed field. This reduces the scan volume of your queries that use field indexes,
making it possible to return results faster. This can help you quickly search petabytes
of total logs across thousands of log groups, and hone in on relevant logs faster. Good
fields to index are fields that you often need to query for. Fields that have high
cardinality of values are also good candidates for field indexes because a query using
these field indexes will complete faster because it limits the log events that are being
matched to the target value.

For example, suppose you have created a field index for `requestId`. Then,
any CloudWatch Logs Insights query on that log group that includes `requestId =
 `value``or`requestId IN
[`value`, `value`, ...]`
will attempt to process only the log events that are known to contain that indexed field
and the queried value, and that CloudWatch Logs has detected a value for that field in the
past.

You can also leverage your field indexes to create efficient queries of larger numbers
of log groups. When you use the `filterIndex` command in your query instead
of the `filter` command, the query will run against selected log groups on
log events that have field indexes. These queries can scan as many as 10,000 log groups
which you choose by specifying as many as five log group name prefixes. If this is a
monitoring account in CloudWatch cross-account observability, you can choose all the source
accounts or specify individual source accounts to select the log groups”.

Indexed fields are case-sensitive. For example, a field index of
`RequestId` won't match a log event containing
`requestId`.

Fields indexes are supported only for the structured log formats of JSON and service
logs.

CloudWatch Logs provides default field indexes for all log groups in the Standard log class. Default field
indexes are automatically available for the following fields:

- `@logStream`
- `@aws.region`
- `@aws.account`
- `@source.log`
- `@data_source_name`
- `@data_source_type`
- `@data_format`
- `traceId`
- `severityText`
- `attributes.session.id`
  CloudWatch Logs provides default field indexes for certain data source name and type combinations as well. Default field indexes are automatically available for the following data source name and type combinations:

| Data Source Name and Type                            | Default Field Indexes                                                                                                                                         |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `amazon_vpc.flow`                                    | `action`<br>`logStatus`<br>`region`<br>`flowDirection`<br>`type`                                                                                              |
| `amazon_route53.resolver_query`                      | `query_type`<br>`transport`<br>`rcode`                                                                                                                        |
| `aws_waf.access`                                     | `action`<br>`httpRequest.country`                                                                                                                             |
| `aws_cloudtrail.data`<br>`aws_cloudtrail.management` | `eventSource`<br>`eventName`<br>`awsRegion`<br>`userAgent`<br>`errorCode`<br>`eventType`<br>`managementEvent`<br>`readOnly`<br>`eventCategory`<br>`requestId` |

Default field indexes are in addition to any custom
field indexes you define within your policy. Default field indexes are not counted
towards your [field index quota](CloudWatchLogs-Field-Indexing-Syntax.md "CloudWatchLogs-Field-Indexing-Syntax.md").

CloudWatch Logs indexes only the log events ingested after an index policy is created. It
doesn't index log events ingested before the policy was created. After you create a
field index, each matching log event remains indexed for 30 days from the log event's
ingestion time.

###### Note

If you create a field index policy in a monitoring account, that policy is not
used for log groups in linked source accounts. A field index policy applies only in
the account where it is created.

The rest of the topics in this section explain how to create field indexes. For
information about referring to field indexes in your queries, see [filterIndex](CWL_QuerySyntax-FilterIndex.md "CWL_QuerySyntax-FilterIndex.md")
and [filter](CWL_QuerySyntax-Filter.md "CWL_QuerySyntax-Filter.md").

###### Topics

- [Field index syntax and
  quotas](CloudWatchLogs-Field-Indexing-Syntax.md "CloudWatchLogs-Field-Indexing-Syntax.md")
- [Create an
  account-level field index policy](CloudWatchLogs-Field-Indexing-CreateAccountLevel.md "CloudWatchLogs-Field-Indexing-CreateAccountLevel.md")
- [Create a
  log-group level field index policy](CloudWatchLogs-Field-Indexing-CreateLogGroupLevel.md "CloudWatchLogs-Field-Indexing-CreateLogGroupLevel.md")
- [Log group selection options when creating
  a query](Field-Indexing-Selection.md "Field-Indexing-Selection.md")
- [Effects of deleting a field
  index policy](CloudWatchLogs-Field-Indexing-Deletion.md "CloudWatchLogs-Field-Indexing-Deletion.md")
