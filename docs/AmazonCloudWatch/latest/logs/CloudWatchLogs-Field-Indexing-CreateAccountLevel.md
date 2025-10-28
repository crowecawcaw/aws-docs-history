# Create an

account-level field index policy

Use the steps in this section to create a field index policy that applies to all
log groups in the account, or to multiple log groups that have log group names that
start with the same string.

###### To create an account-level field index policy

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, choose **Settings** and then
   choose the **Logs** tab.
3. In the **Account level index policies** section, choose
   **Manage**.
4. Choose **Create index policy**.
5. For **Policy name**, enter a name for your new
   poiicy.
6. For **Select log groups**, do one of the
   following:
   - Choose **All standard log groups** to have the
     index policy apply to all Standard Class log groups in the
     account.
   - choose **Select log group(s) by prefix match** to
     apply the policy to a subset of log groups that all have names that
     start with the same string. Then, enter the prefix for these log
     groups in **Enter a prefix name**.

   After you enter your prefix, you can choose **Preview
   prefix matched log groups** to confirm that your prefix
   matches the log groups that you expected.

7. For **Custom index field configuration**, choose
   **Add field path** to enter the first field to
   index.

Then enter the string to use as the value of the field name. This must be
an exact case match to what appears in the log events. For example, if your
log events include `requestId`, you must enter
`requestId` here. `RequestId`,
`requestID`, and `request Id` wouldn't
match.

If you want to index a custom log field that starts with the
`@` character, you must include an extra `@`
character when you enter the index string. For example, if you have a custom
log field `@emailname`, enter `@@emailname` in the
**Add field path** box.

You can also create indexes for the `@ingestionTime` and
`@logStream` fields that CloudWatch Logs automatically generates. If
you do, you don't need to add an extra `@` when specifying
them. 8. Repeat the previous step to add as many as 20 field indexes. 9. When you have finished, choose **Create**.
