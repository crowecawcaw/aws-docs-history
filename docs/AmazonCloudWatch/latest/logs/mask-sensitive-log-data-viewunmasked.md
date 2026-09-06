

# View unmasked data
<a name="mask-sensitive-log-data-viewunmasked"></a>

To view unmasked data, a user must have the `logs:Unmask` permission. Users with this permission can see the unmasked data in the following ways:
+ When viewing the events in a log stream, choose **Display**, **Unmask**.
+ Use a CloudWatch Logs Insights query that includes the **unmask(@message)** command. The following example query displays the 20 most recent log events in the stream, unmasked:

  ```
  fields @timestamp, @message, unmask(@message)
  | sort @timestamp desc
  | limit 20
  ```

  For more information about CloudWatch Logs Insights commands, see [CloudWatch Logs Insights language query syntax](CWL_QuerySyntax.md).
+ Use a [ GetLogEvents](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogEvents.html) or [ FilterLogEvents](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_FilterLogEvents.html) operation with the `unmask` parameter.

The **CloudWatchLogsFullAccess** policy includes the `logs:Unmask` permission. To grant `logs:Unmask` to a user who does not have **CloudWatchLogsFullAccess**, you can attach a custom IAM policy to that user. For more information, see [ Adding permissions to a user (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console).