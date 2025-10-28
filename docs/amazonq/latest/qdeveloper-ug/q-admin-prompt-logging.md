# Logging users' prompts in Amazon Q Developer

Administrators can enable the logging of all [inline
suggestions](inline-suggestions.md "inline-suggestions.md") and [chat conversations](q-in-IDE-chat.md "q-in-IDE-chat.md") that users have
with Amazon Q in their integrated development environment (IDE). These logs can help with auditing,
debugging, analytics, and ensuring compliance.

When developers use inline suggestions, Amazon Q will log the accepted and actively rejected suggestions.
When developers chat with Amazon Q, Amazon Q will log both the developers' prompts and Amazon Q's responses. When
developers chat with [the Amazon Q Agent for software development](q-in-IDE-chat.md#develop-code "q-in-IDE-chat.md#develop-code")
using the `/dev` command, only the prompts will be logged.

Amazon Q stores the logs in an Amazon S3 bucket that you create, at the following path:

``bucketName`/`prefix`/AWSLogs/`accountId`/QDeveloperLogs/`log-type`/`region`/`year`/`month`/`day`/`utc-hour`/`zipFile`.gz/`logFile`.json`

At the previous path, `log-type` is one of the
following:

- `GenerateAssistantResponse` — holds chat logs
- `GenerateCompletions` — holds inline completion logs
- `StartTaskAssistCodeGeneration` — holds
  `/dev` logs
  For examples and explanations of log file contents, see [Prompt log examples in Amazon Q Developer](q-admin-prompt-log-examples.md "q-admin-prompt-log-examples.md").

There is no charge for the prompt logging feature other than the storage cost of the Amazon S3 bucket
used to hold the logs, and a small fee for the optional KMS key used to encrypt the bucket.

Use the following instructions to enable prompt logging.

**Prerequisites**

- Make sure users are subscribed in a standalone account or, if you're using [AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md"), a management account. Currently, Q Developer does not support logging
  the prompts of users who are subscribed in member accounts in AWS Organizations.
- Create an Amazon S3 bucket to hold the prompt logs. The bucket must:
  - Be in the AWS Region where the Amazon Q Developer profile was installed. This profile was
    installed when you subscribed users to Amazon Q Developer Pro for the first time. For more
    information about this profile and the Regions where it's supported, see [What is the Amazon Q Developer profile?](subscribe-understanding-profile.md "subscribe-understanding-profile.md"), and [Supported Regions for the Q Developer
    console and Q Developer profile](q-admin-setup-subscribe-regions.md#qdev-console-and-profile-regions "q-admin-setup-subscribe-regions.md#qdev-console-and-profile-regions").
  - Be in the AWS account where users are subscribed.
  - Have a bucket policy like the one that follows. Replace
    `bucketName`, `region`,
    `accountId`, and `prefix` with
    your own information.

  JSON

  ```
  `{
   "Version":"2012-10-17",
   "Statement": [
   {
   "Sid": "QDeveloperLogsWrite",
   "Effect": "Allow",
   "Principal": {
   "Service": "q.amazonaws.com"
   },
   "Action": [
   "s3:PutObject"
   ],
   "Resource": [
   "arn:aws:s3:::`bucketName`/`prefix`/*"
   ],
   "Condition": {
   "StringEquals": {
   "aws:SourceAccount": "`111122223333`"
   },
   "ArnLike": {
   "aws:SourceArn": "arn:aws:codewhisperer:`us-east-1`:`111122223333`:*"
   }
   }
   }
   ]
  }`

  ```

  If you're configuring SSE-KMS on the bucket, add the following policy on the KMS
  key:

  ```
  {
      "Effect": "Allow",
      "Principal": {
          "Service": "q.amazonaws.com"
      },
      "Action": "kms:GenerateDataKey",
      "Resource": "*",
      "Condition": {
          "StringEquals": {
            "aws:SourceAccount": "`accountId`"
          },
          "ArnLike": {
             "aws:SourceArn": "arn:aws:codewhisperer:`region`:`accountId`:*"
          }
      }
  }
  ```

  To learn about protecting the data in your Amazon S3 bucket, see [Protecting data with encryption](../../../AmazonS3/latest/userguide/UsingEncryption.md "../../../AmazonS3/latest/userguide/UsingEncryption.md") in the _Amazon Simple Storage Service User
  Guide_.

###### To enable prompt logging

1. Open the Amazon Q Developer console.

To use the Amazon Q Developer console, you must have the permissions defined in [Allow administrators to use the Amazon Q Developer console](id-based-policy-examples-admins.md#q-admin-setup-admin-users "id-based-policy-examples-admins.md#q-admin-setup-admin-users").

###### Note

You must sign in as a standalone account administrator, or management account
administrator. Member account administrators cannot enable prompt logging because prompt
logging is not supported for users subscribed in member accounts. 2. Choose **Settings**. 3. Under **Preferences**, choose **Edit**. 4. In the Edit preferences window, toggle **Q Developer prompt
logging**. 5. Under Amazon S3 location, enter the Amazon S3 URI that you will use to receive the logs. Example:
`s3://amzn-s3-demo-bucket/qdev-prompt-logs/`
