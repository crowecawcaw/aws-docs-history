# Create a log-group level field index policy

Use the steps in this section to create a field index policy that applies to a
single log group.

###### To create a log-group level field index policy

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, choose **Logs**,
   **Log groups**.
3. Choose the name of the log group.
4. Choose the **Field indexes** tab.
5. Choose **Manage field indexes for this log group**
6. For **Manage log group level field indexes**, choose
   **Add field path** to enter the first field to
   index.

Then enter the string to use as the value of the field name. This must be
an exact case match to what appears in the log events. For example, if your
log events include `requestId`, you must enter
`requestId` here. `RequestId`,
`requestID`, and `request Id` would not
match.

If you want to index a custom log field that starts with the
`@` character, you must include an extra `@`
character when you enter the index string. For example, if you have a custom
log field `@emailname`, enter `@@emailname` in the
**Add field path** box.

You can also create indexes for the `@ingestionTime` and
`@logStream` fields that CloudWatch Logs automatically generates. If
you do, do not need to add an extra `@` when specifying
them. 7. (Optional) In addition to specifying the field path, you can select **Set as a facet** to create the field as a facet. 8. Repeat the previous step to add as many as 20 field indexes. 9. When you have finished, choose **Save**.
