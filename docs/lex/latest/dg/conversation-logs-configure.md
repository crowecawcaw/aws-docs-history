End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Configuring Conversation Logs

You enable and disable conversation logs using the console or the
`conversationLogs` field of the `PutBotAlias`
operation. You can turn on or turn off audio logs, text logs, or both.
Logging starts on new bot sessions. Changes to log settings aren't reflected
for active sessions.

To store text logs, use an Amazon CloudWatch Logs log group in your AWS account.
You can use any valid log group. The log group must be in the same region as
the Amazon Lex bot. For more information about creating a CloudWatch Logs log group, see
[Working with Log Groups and Log Streams](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md") in the
_Amazon CloudWatch Logs User Guide_.

To store audio logs, use an Amazon S3 bucket in your AWS account. You can
use any valid S3 bucket. The bucket must be in the same region as the Amazon Lex
bot. For more information about creating an S3 bucket, see [Create a
Bucket](../../../AmazonS3/latest/gsg/CreatingABucket.md "../../../AmazonS3/latest/gsg/CreatingABucket.md") in the _Amazon Simple Storage Service Getting Started
Guide_.

You must provide an IAM role with policies that enable Amazon Lex to write
to the configured log group or bucket. For more information, see [Creating an IAM Role and
Policies for Conversation Logs](conversation-logs-policies.md#conversation-logs-role-and-policy "conversation-logs-policies.md#conversation-logs-role-and-policy").

If you create a service-linked role using the AWS Command Line Interface, you must add
a custom suffix to the role using the `custom-suffix` option as follows:

```
aws iam create-service-linked-role \
    --aws-service-name `lex.amazon.aws.com` \
    --custom-suffix `suffix`
```

The IAM role that you use to enable conversation logs must have the
`iam:PassRole` permission. The following policy should be
attached to the role.

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

## Enabling Conversation

Logs

###### To turn on logs using the console

1. Open the Amazon Lex console [https://console.aws.amazon.com/lex](https://console.aws.amazon.com/lex "https://console.aws.amazon.com/lex").
2. From the list, choose a bot.
3. Choose the **Settings** tab, and then from the left
   menu choose **Conversation logs**.
4. In the list of aliases, choose the settings icon for the alias for
   which you want to configure conversation logs.
5. Select whether to log text, audio, or both.
6. For text logging, enter the Amazon CloudWatch Logs log group name.
7. For audio logging, enter the S3 bucket information.
8. Optional. To encrypt audio logs, choose the AWS KMS key to use for
   encryption.
9. Choose an IAM role with the required permissions.
10. Choose **Save** to start logging
    conversations.

###### To turn on text logs using the API

1. Call the [PutBotAlias](API_PutBotAlias.md "API_PutBotAlias.md") operation with an entry in the
   `logSettings` member of the `conversationLogs`
   field
   - Set the `destination` member to
     `CLOUDWATCH_LOGS`
   - Set the `logType` member to `TEXT`
   - Set the `resourceArn` member to the Amazon Resource Name
     (ARN) of the CloudWatch Logs log group that is the destination for the logs

2. Set the `iamRoleArn` member of the
   `conversationLogs` field to the Amazon Resource Name (ARN) of
   an IAM role that has the required permissions for enabling conversation
   logs on the specified resources.

###### To turn on audio logs using the API

1. Call the [PutBotAlias](API_PutBotAlias.md "API_PutBotAlias.md") operation with an entry in the
   `logSettings` member of the `conversationLogs`
   field
   - Set the `destination` member to `S3`
   - Set the `logType` member to `AUDIO`
   - Set the `resourceArn` member to the ARN of the Amazon S3
     bucket where the audio logs are stored
   - Optional. To encrypt audio logs with a specific AWS KMS key, set the
     `kmsKeyArn` member of the ARN of the key that is used for
     encryption.

2. Set the `iamRoleArn` member of the
   `conversationLogs` field to the Amazon Resource Name (ARN) of
   an IAM role that has the required permissions for enabling conversation
   logs on the specified resources.

## Disabling Conversation

Logs

###### To turn off logs using the console

1. Open the Amazon Lex console [https://console.aws.amazon.com/lex](https://console.aws.amazon.com/lex "https://console.aws.amazon.com/lex").
2. From the list, choose a bot.
3. Choose the **Settings** tab, and then from the left
   menu choose **Conversation logs**.
4. In the list of aliases, choose the settings icon for the alias for
   which you want to configure conversation logs.
5. Clear the check from text, audio, or both to turn off logging.
6. Choose **Save** to stop logging
   conversations.

###### To turn off logs using the API

- Call the `PutBotAlias` operation without the
  `conversationLogs` field.

###### To turn off text logs using the API

- - If you are logging audio
    - Call the [PutBotAlias](API_PutBotAlias.md "API_PutBotAlias.md") operation with a
      `logSettings` entry only for `AUDIO`.
    - The call to the `PutBotAlias` operation must not have
      a `logSettings` entry for `TEXT`.

  - If you are not logging audio
    - Call the [PutBotAlias](API_PutBotAlias.md "API_PutBotAlias.md") operation without the
      `conversationLogs` field.

###### To turn off audio logs using the API

- - If you are logging text
    - Call the [PutBotAlias](API_PutBotAlias.md "API_PutBotAlias.md") operation with a
      `logSettings` entry only for `TEXT`.
    - The call to the `PutBotAlias` operation must not have
      a `logSettings` entry for `AUDIO`.

  - If you are not logging text
    - Call the [PutBotAlias](API_PutBotAlias.md "API_PutBotAlias.md") operation without the
      `conversationLogs` field.
