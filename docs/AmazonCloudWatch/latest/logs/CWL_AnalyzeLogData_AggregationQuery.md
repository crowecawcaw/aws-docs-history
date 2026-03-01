# Tutorial: Run a query with an aggregation function

You can use aggregation functions with the `stats` command and
as arguments for other functions. In this tutorial, you run a query command
that counts the number of log events containing a specified field. The query
command returns a total count that's grouped by the specified field's value
or values. For more information about aggregation functions, see [Supported operations and functions](../../../en_us/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.md#CWL_QuerySyntax-operations-functions "../../../en_us/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.md#CWL_QuerySyntax-operations-functions") in the _Amazon CloudWatch Logs
User Guide_.

###### To run a query with an aggregation function

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Logs**, and then
   choose **Logs Insights**.
3. Confirm that the **Logs Insights QL** tab is
   selected.
4. In the **Select log group(s)** drop down, choose
   one or more log groups to query.

If this is a monitoring account in CloudWatch cross-account
observability, you can select log groups in the source accounts as
well as the monitoring account. A single query can query logs from
different accounts at once.

You can filter the log groups by log group name, account ID, or
account label.

When you select a log group, CloudWatch Logs Insights automatically detects data
fields in the log group if it is a Standard class log group. To see
discovered fields, select the **Fields** menu near
the top right of the page. 5. Delete the default query in the query editor, and enter the
following command:

```
stats count(*) by `fieldName`
```

6. Replace `fieldName` with a discovered
   field from the **Fields** menu.

The **Fields** menu is located at the top right
of the page and displays all of the discovered fields that CloudWatch Logs Insights
detects in your log group. 7. Choose **Run** to view the query results.

The query results show the number of records in your log group
that match the query command and the total count that's grouped by
the specified field's value or values.
