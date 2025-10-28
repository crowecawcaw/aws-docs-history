# Logging errors with error logs in Lex V2

You enable _error logs_ to store bot
interactions. You can use these error logs to review the performance of your bot
and to troubleshoot errors with conversations.

Error logs are configured for an version. Each version can have
different settings for their error logs. Text logs store text input in CloudWatch Logs.
You can enable encryption of text logs using AWS KMS
customer managed CMKs.

## IAM Policies for Error

Logs

Depending on the type of logging that you select, Amazon Lex V2 requires
permission to use Amazon CloudWatch Logs and Amazon Simple Storage Service (S3) buckets to store your logs. You
must create AWS Identity and Access Management roles and permissions to enable Amazon Lex V2 to access these
resources.

### Creating an IAM Role and

Policies for Error Logs

To enable conversation logs, you must grant write permission for CloudWatch Logs
and Amazon S3. If you enable object encryption for your S3 objects, you need to
grant access permission to the AWS KMS keys used to encrypt the objects.

You can use the IAM console, the IAM API, or the AWS Command Line Interface to
create the role and policies. These instructions use the AWS CLI to create the
role and policies.

To create an IAM role for error logs

The IAM role that you use to enable conversation logs must have the iam:PassRole permission.
The following policy should be attached to the role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::`111122223333`:role/role"
 }
 ]
}`

```

## Enabling Error Logs in Lex V2

To turn on error logs using the Amazon Lex V2 console:

1. Sign in to the AWS Management Console and open the Amazon Lex console at
   [https://console.aws.amazon.com/lex/](https://console.aws.amazon.com/lex/ "https://console.aws.amazon.com/lex/").
2. From the list of **Bots**, choose the bot you want to enable for error logs.
3. From the left menu, choose **Version**.
4. In the list of **Version**, choose the Version for which you want to configure error logs.
5. In the **Version detail** section, choose **Enable**.
6. Choose **Save** to start logging conversations. If necessary, Amazon Lex V2 will update your service role with permissions to access the CloudWatch Logs log group.

## Disabling Error Logs in Lex V2

To turn off error logs using the Amazon Lex V2 console:

1. Sign in to the AWS Management Console and open the Amazon Lex console at
   [https://console.aws.amazon.com/lex/](https://console.aws.amazon.com/lex/ "https://console.aws.amazon.com/lex/").
2. From the list of **Bots**, choose the bot you want to enable for error logs.
3. From the left menu, choose **Version**.
4. In the list of **Version**, choose the Version for which you want to configure error logs.
5. In the **Version detail** section, choose **Disable**.
6. Choose **Save** to stop logging conversations.
