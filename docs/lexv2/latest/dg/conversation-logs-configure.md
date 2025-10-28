# Configuring conversation

logs for your Lex V2 bot

You enable and disable conversation logs using the console or the
`conversationLogSettings` field of the
`CreateBotAlias` or `UpdateBotAlias` operation.
You can turn on or turn off audio logs, text logs, or both. Logging starts
on new bot sessions. Changes to log settings aren't reflected for active
sessions.

To store text logs, use an Amazon CloudWatch Logs log group in your AWS account.
You can use any valid log group. The log group must be in the same region
as the Amazon Lex V2 bot. For more information about creating a CloudWatch Logs log group,
see [Working with Log Groups and Log Streams](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md") in the
_Amazon CloudWatch Logs User Guide_.

To store audio logs, use an Amazon S3 bucket in your AWS account. You can
use any valid S3 bucket. The bucket must be in the same region as the
Amazon Lex V2 bot. For more information about creating an S3 bucket, see [Creating
a bucket](../../../AmazonS3/latest/gsg/CreatingABucket.md "../../../AmazonS3/latest/gsg/CreatingABucket.md") in the _Amazon Simple Storage Service Getting Started
Guide_.

When you manage conversation logs using the console, the console
updates your service role so that it has access to the log group and S3
bucket.

If you are not using the console, you must provide an IAM role
with policies that enable Amazon Lex V2 to write to the configured log group or
bucket. If you create a service-linked role using the AWS Command Line Interface, you must add
a custom suffix to the role using the `custom-suffix` option as in the following example.
For more information, see [Creating an IAM Role and
Policies for Conversation Logs](conversation-logs-policies.md#conversation-logs-role-and-policy "conversation-logs-policies.md#conversation-logs-role-and-policy").

```
aws iam create-service-linked-role \
    --aws-service-name `lexv2.amazon.aws.com` \
    --custom-suffix `suffix`
```

The IAM role that you use to enable conversation logs must have the
`iam:PassRole` permission. The following policy should be
attached to the role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::`111122223333`:role/`role`"
 }
 ]
}`

```

## Enabling conversation

logs

###### To turn on logs using the console

1. Open the Amazon Lex V2 console [https://console.aws.amazon.com/lexv2](https://console.aws.amazon.com/lexv2 "https://console.aws.amazon.com/lexv2").
2. From the list, choose a bot.
3. From the left menu, choose **Aliases**.
4. In the list of aliases, choose the alias for which you want to
   configure conversation logs.
5. In the **Conversation logs** section, choose
   **Manage conversation logs**.
6. For text logs, choose **Enable** then enter the
   Amazon CloudWatch Logs log group name.
7. For audio logs, choose **Enable** then enter
   the S3 bucket information.
8. Optional. To encrypt audio logs, choose the AWS KMS key to use for
   encryption.
9. Choose **Save** to start logging conversations.
   If necessary, Amazon Lex V2 will update your service role with permissions
   to access the CloudWatch Logs log group and selected S3 bucket.

## Disabling conversation

logs in Lex V2

###### To turn off logs using the console

1. Open the Amazon Lex V2 console [https://console.aws.amazon.com/lexv2](https://console.aws.amazon.com/lexv2 "https://console.aws.amazon.com/lexv2").
2. From the list, choose a bot.
3. From the left menu, choose **Aliases**.
4. In the list of aliases, choose the alias for which you want to
   configure conversation logs.
5. In the **Conversation logs** section, choose
   **Manage conversation logs**.
6. Disable text logging, audio logging, or both to turn off
   logging.
7. Choose **Save** to stop logging
   conversations.
