# Automatically indexed fields

CloudWatch Logs automatically indexes fields based on their recent use in CloudWatch Logs Insights equality
filters that use the `=` or `IN` operators. These indexes are
in addition to default field indexes and the field indexes that you configure in
policies. You do not need to configure a policy for automatically indexed
fields.

CloudWatch Logs updates the set of automatically indexed fields based on recent query
activity. When CloudWatch Logs removes a field from the set, it stops indexing newly ingested
events for that field. CloudWatch Logs manages automatically indexed fields and retains them
for 30 days. To keep a field indexed permanently, add it to an account-level or
log-group level field index policy.

###### Use filter instead of filterIndex for automatically indexed fields

We recommend that you use `filter` instead of
`filterIndex` with automatically indexed fields. CloudWatch Logs can update
or remove these fields based on query patterns. CloudWatch Logs retains them for only 30
days. The `filterIndex` command returns only indexed data. Because
CloudWatch Logs updates the set based on query activity, a
`filterIndex` query does not search events ingested before CloudWatch Logs
selected the field or after CloudWatch Logs stopped indexing it. If you use
`filterIndex`, add the field to a field index policy to keep it
indexed regardless of query activity. For more information, see [filterIndex compared to filter](CWL_QuerySyntax-FilterIndex.md#CWL_QuerySyntax-FilterIndex-Filter "CWL_QuerySyntax-FilterIndex.md#CWL_QuerySyntax-FilterIndex-Filter").

The **Field indexes** tab for a log group lists automatically
indexed fields.

You can also use the [`DescribeFieldIndexes`](../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeFieldIndexes.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeFieldIndexes.md") operation to list automatically
indexed fields. Include `AUTO` in the `indexCategories`
request parameter. The response sets `indexCategory` to
`AUTO` for automatically indexed fields. Requests that omit
`indexCategories` do not return automatically indexed fields.

###### To add an automatically indexed field to a log-group level index policy

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, choose **Logs**,
   **Log groups**.
3. Choose the name of the log group.
4. Choose the **Field indexes** tab, and then choose
   **Manage field indexes**.
5. On the **Manage log group level field indexes** page,
   review the fields in the policy. Add or remove fields as needed, and then
   choose **Save**.
