# Exporting logs from Amazon Cognito user pools

You can configure your user pool to send detailed logs of some additional activity to
another AWS service, like a CloudWatch log group. These logs are of a finer granularity than those
in AWS CloudTrail, and can be useful to troubleshoot your user pool and analyze user sign-in
activity with [threat
protection](cognito-user-pool-settings-threat-protection.md "cognito-user-pool-settings-threat-protection.md"). When you want to stream logs of SMS and email notification errors, your
user pool sends `ERROR`-level logs to a CloudWatch log group. When you want to stream
logs of user sign-in activity, your user pool sends `INFO`-level logs to a log
group, a Amazon Data Firehose stream, or an Amazon S3 bucket. You can combine both options in a user
pool.

###### Topics

- [Things to know about log
  export](#exporting-quotas-and-usage-things-to-know "#exporting-quotas-and-usage-things-to-know")
- [Exporting email and SMS message
  delivery errors](#exporting-quotas-and-usage-messages "#exporting-quotas-and-usage-messages")
- [Exporting threat protection user
  activity logs](#exporting-quotas-and-usage-user-activity "#exporting-quotas-and-usage-user-activity")

## Things to know about log

export

**Cost impact**

Amazon Data Firehose, Amazon S3, and CloudWatch Logs incur costs for data ingestion and retrieval. Your
logging configuration might affect your AWS bill. For more information, see the
following:

- [Vended
  Logs](https://aws.amazon.com/cloudwatch/pricing/#Vended_Logs "https://aws.amazon.com/cloudwatch/pricing/#Vended_Logs") in _Amazon CloudWatch Pricing_.
- [Amazon Data Firehose
  pricing](https://aws.amazon.com/firehose/pricing/ "https://aws.amazon.com/firehose/pricing/")
- [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/")

User-activity log exports contain security assessments and are a function of user
pool [threat
protection](cognito-user-pool-settings-threat-protection.md "cognito-user-pool-settings-threat-protection.md"). Amazon Cognito only generates these logs when threat protection is in
**Audit-only** or **Full-function** mode and your
user pool is on the Plus [feature
plan](cognito-sign-in-feature-plans.md "cognito-sign-in-feature-plans.md").

**User activity logs are `INFO` level**

Exported user-activity logs are at the `INFO` error level only and
provide information for statistical and security analysis of authentication activity.
Messages at the `WARNING` and `ERROR` error levels, for example
throttling errors, aren't included in the exported logs.

**Best-effort delivery**

Delivery of logs from Amazon Cognito is best effort. The volume of logs that your user pool
delivers, and your service quotas for CloudWatch Logs, Amazon S3, and Firehose can affect the delivery
of logs.

**Existing external logs are unaffected**

These logging options don't replace or change the following log functions of user
pools.

1. CloudTrail logs of routine user activity like sign-up and sign-in.
2. Analysis of user activity at scale with CloudWatch metrics.

Separately, you can also find logs from [Viewing the user pool import
results in the CloudWatch console](cognito-user-pools-using-import-tool.md#cognito-user-pools-using-import-tool-cloudwatch "cognito-user-pools-using-import-tool.md#cognito-user-pools-using-import-tool-cloudwatch") and [Customizing user pool
workflows with Lambda triggers](cognito-user-pools-working-with-lambda-triggers.md "cognito-user-pools-working-with-lambda-triggers.md") in CloudWatch Logs. Amazon Cognito and
Lambda store these logs in different log groups from the ones that you specify for user
activity logs.

**Applies only to user pools**

No log export capabilities exist for identity pools.

**Requires user permissions and service-linked role**

The AWS principal that sets up log export must have permissions to modify the
target resources, as described in the topics that follow. Amazon Cognito creates a [service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") on your behalf and assumes the role to deliver logs to
the target resource.

For more information about the authorization model for sending logs from Amazon Cognito,
see [Enable logging from AWS services](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-vended-logs-permissions "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-vended-logs-permissions") in the _Amazon CloudWatch Logs
User Guide_.

**Log level is exclusive to log type**

Message-delivery logs are of the `userNotification` type and of the
`ERROR` errorlevel. Advanced security user activity logs are of the
`userAuthEvents` type and of the `INFO` errorlevel. You can
combine two members of `LogConfigurations`, one for
`userNotification` to CloudWatch Logs, and one for `userAuthEvents` to
Firehose, Amazon S3, or CloudWatch Logs.

You can't send user-activity logs to multiple destinations. You can't send
user-notification logs to any destination other than CloudWatch Logs.

**Different configuration options**

You can only configure user-notification logs with the Amazon Cognito user pools API or an AWS
SDK. You can configure advanced security user-activity logs with the API or in the
Amazon Cognito console. To set both, use the API as demonstrated in the example request at
[SetLogDeliveryConfiguration](../../../cognito-user-identity-pools/latest/APIReference/API_SetLogDeliveryConfiguration.md "../../../cognito-user-identity-pools/latest/APIReference/API_SetLogDeliveryConfiguration.md").

**Additional configuration required with large resource-based policies**

To send logs to log groups with a resource policy of a size greater than 5120
characters, configure a log group with a path that starts with
`/aws/vendedlogs`. For more information, see [Enabling
logging from certain AWS services](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md").

**Automatic creation of a folder in Amazon S3**

When you configure threat protection log export to an Amazon S3 bucket, Amazon Cognito might
create an `AWSLogs` folder in your bucket. That folder is not created in
all cases, and the configuration can succeed without creating it.

## Exporting email and SMS message

delivery errors

For email and SMS message delivery errors, you can deliver **Error**-level user notification logs from your user pool. When you activate this
feature, you can choose the log group where you want Amazon Cognito to send logs. User notification
logging is useful when you want to find out the status of email and SMS messages that your
user pool delivered with Amazon SNS and Amazon SES. This log export option, unlike [user-activity export](#exporting-quotas-and-usage-user-activity.title "#exporting-quotas-and-usage-user-activity.title"),
doesn't require the Plus feature plan.

You can configure detailed notification logs with the Amazon Cognito user pools API in a [SetLogDeliveryConfiguration](../../../cognito-user-identity-pools/latest/APIReference/API_SetLogDeliveryConfiguration.md "../../../cognito-user-identity-pools/latest/APIReference/API_SetLogDeliveryConfiguration.md") API request. You can view the
logging configuration of a user pool in a [GetLogDeliveryConfiguration](../../../cognito-user-identity-pools/latest/APIReference/API_GetLogDeliveryConfiguration.md "../../../cognito-user-identity-pools/latest/APIReference/API_GetLogDeliveryConfiguration.md") API request. The following is an
example request body.

```
{
   "LogConfigurations": [
      {
         "CloudWatchLogsConfiguration": {
            "LogGroupArn": "arn:aws:logs:us-west-2:123456789012:log-group:example-user-pool-exported"
         },
         "EventSource": "userNotification",
         "LogLevel": "ERROR"
      }
   ],
   "UserPoolId": "us-west-2_EXAMPLE"
}
```

You must authorize these requests with AWS credentials that have the following
permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ManageUserPoolLogs",
 "Action": [
 "cognito-idp:SetLogDeliveryConfiguration",
 "cognito-idp:GetLogDeliveryConfiguration"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "CognitoLog",
 "Action": [
 "logs:CreateLogDelivery",
 "logs:GetLogDelivery",
 "logs:UpdateLogDelivery",
 "logs:DeleteLogDelivery",
 "logs:ListLogDeliveries"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "CognitoLoggingCWL",
 "Action": [
 "logs:PutResourcePolicy",
 "logs:DescribeResourcePolicies",
 "logs:DescribeLogGroups"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow"
 }
 ]
}`

```

The following is an example event from a user pool. This log schema is subject to
change. Some fields might be logged with null values.

```
{
    "eventTimestamp": "1687297330677",
    "eventSource": "USER_NOTIFICATION",
    "logLevel": "ERROR",
    "message": {
        "details": "String"
    },
    "logSourceId": {
        "userPoolId": "String"
    }
}
```

## Exporting threat protection user

activity logs

User pools with the Plus feature plan and threat protection log user activity events:
the details and security assessment of user sign-in, sign-out, and other authentication
operations with your user pool. You might want to review user activity logs in your own
log-management system, or create an archive. You can export this data to a Amazon CloudWatch Logs log
group, an Amazon Data Firehose stream, or an Amazon Simple Storage Service (Amazon S3) bucket. From there, you can ingest this
data into other systems that analyze, normalize or otherwise process data in ways that fit
it in to your operational processes. To export data of this type, your user pool must be on
the Plus feature plan and [threat protection](cognito-user-pool-settings-threat-protection.md "cognito-user-pool-settings-threat-protection.md") must be active in your user pool.

With the information in these user activity logs, you can view a profile of user sign-in
and account-management activity. By default, Amazon Cognito captures these events to storage that's
based in your user pool. The following example is an example event for a user who signed in
and was evaluated to have no risk factors. You can retrieve this information with the
`AdminListUserAuthEvents` API operation. The following is an example
output:

```
{
    "AuthEvents": [
        {
            "EventId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "EventType": "SignIn",
            "CreationDate": "2024-06-27T10:49:59.139000-07:00",
            "EventResponse": "Pass",
            "EventRisk": {
                "RiskDecision": "NoRisk",
                "CompromisedCredentialsDetected": false
            },
            "ChallengeResponses": [
                {
                    "ChallengeName": "Password",
                    "ChallengeResponse": "Success"
                }
            ],
            "EventContextData": {
                "IpAddress": "192.0.2.1",
                "DeviceName": "Chrome 126, Windows 10",
                "Timezone": "-07:00",
                "City": "null",
                "Country": "United States"
            }
        }
    ],
    "NextToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222#2024-06-27T17:49:59.139Z"
}
```

You can activate log export for user activity in the Amazon Cognito console or with the [SetLogDeliveryConfiguration](../../../cognito-user-identity-pools/latest/APIReference/API_SetLogDeliveryConfiguration.md "../../../cognito-user-identity-pools/latest/APIReference/API_SetLogDeliveryConfiguration.md") API operation.

AWS Management Console

1. If you don't already have one that you want to use, create an [S3 bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md"), [Firehose stream](../../../firehose/latest/dev/basic-create.md "../../../firehose/latest/dev/basic-create.md"), or [CloudWatch
   log group](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md").
2. Sign in to the [Amazon Cognito
   console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home").
3. Choose **User Pools**.
4. Choose an existing user pool from the list, or [create a user
   pool](cognito-user-pool-as-user-directory.md "cognito-user-pool-as-user-directory.md").
5. Choose the **Advanced security** tab. Locate **Export
   user activity logs** and choose **Edit**
6. Under **Logging status**, select the checkbox next to
   **Activate user activity log export**.
7. Under **Logging destination**, choose the AWS service that
   you want to handle your logs: **CloudWatch log group**,
   **Amazon Data Firehose stream**, or **S3 bucket**.
8. Your selection will populate the resource selector with the corresponding
   resource type. Select a log group, stream, or bucket from the list. You can also
   select the **Create** button to navigate to the AWS Management Console for the
   selected service and create a new resource.
9. Select **Save changes**.

API
Choose one type of destination for your user activity logs.

The following is an example `SetLogDeliveryConfiguration` request body
that sets a Firehose stream as the log destination.

```
{
   "LogConfigurations": [
      {
         "EventSource": "userAuthEvents",
         "FirehoseConfiguration": {
            "StreamArn": "`arn:aws:firehose:us-west-2:123456789012:deliverystream/example-user-pool-activity-exported`"
         },
         "LogLevel": "INFO"
      }
   ],
   "UserPoolId": "us-west-2_EXAMPLE"
}
```

The following is an example `SetLogDeliveryConfiguration` request body
that sets a Amazon S3 bucket as the log destination.

```
{
   "LogConfigurations": [
      {
         "EventSource": "userAuthEvents",
         "S3Configuration": {
            "BucketArn": "`arn:aws:s3:::amzn-s3-demo-logging-bucket`"
         },
         "LogLevel": "INFO"
      }
   ],
   "UserPoolId": "us-west-2_EXAMPLE"
}
```

The following is an example `SetLogDeliveryConfiguration` request body
that sets a CloudWatch log group as the log destination.

```
{
   "LogConfigurations": [
      {
         "EventSource": "userAuthEvents",
         "CloudWatchLogsConfiguration": {
            "LogGroupArn": "`arn:aws:logs:us-west-2:123456789012:log-group:DOC-EXAMPLE-LOG-GROUP`"
         },
         "LogLevel": "INFO"
      }
   ],
   "UserPoolId": "us-west-2_EXAMPLE"
}
```

The user that configures log delivery must be a user pool administrator and have the
following additional permissions:

Amazon S3
JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ManageUserPoolLogs",
 "Action": [
 "cognito-idp:SetLogDeliveryConfiguration",
 "cognito-idp:GetLogDeliveryConfiguration"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "ManageLogsS3",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogDelivery",
 "s3:PutBucketPolicy",
 "s3:GetBucketPolicy"
 ],
 "Resource": "*"
 }
 ]
}`

```

CloudWatch Logs
JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ManageUserPoolLogs",
 "Action": [
 "cognito-idp:SetLogDeliveryConfiguration",
 "cognito-idp:GetLogDeliveryConfiguration"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "ManageLogsCWL",
 "Action": [
 "logs:CreateLogDelivery",
 "logs:GetLogDelivery",
 "logs:UpdateLogDelivery",
 "logs:DeleteLogDelivery",
 "logs:ListLogDeliveries",
 "logs:PutResourcePolicy",
 "logs:DescribeResourcePolicies",
 "logs:DescribeLogGroups"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow"
 }
 ]
}`

```

Amazon Data Firehose
JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ManageUserPoolLogs",
 "Action": [
 "cognito-idp:SetLogDeliveryConfiguration",
 "cognito-idp:GetLogDeliveryConfiguration"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "ManageUserPoolLogsFirehose",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogDelivery",
 "iam:CreateServiceLinkedRole",
 "firehose:TagDeliveryStream"
 ],
 "Resource": "*"
 }
 ]
}`

```

The following is an example event from a user pool. This log schema is subject to
change. Some fields might be logged with null values.

```
{
    "eventTimestamp": "1687297330677",
    "eventSource": "USER_ACTIVITY",
    "logLevel": "INFO",
    "message": {
        "version": "1",
        "eventId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "eventType": "SignUp",
        "userSub": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "userName": "test-user",
        "userPoolId": "us-west-2_EXAMPLE",
        "clientId": "1example23456789",
        "creationDate": "Wed Jul 17 17:25:55 UTC 2024",
        "eventResponse": "InProgress",
        "riskLevel": "",
        "riskDecision": "PASS",
        "challenges": [],
        "deviceName": "Other, Other",
        "ipAddress": "192.0.2.1",
        "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
        "idpName": "",
        "compromisedCredentialDetected": "false",
        "city": "Seattle",
        "country": "United States",
        "eventFeedbackValue": "",
        "eventFeedbackDate": "",
        "eventFeedbackProvider": "",
        "hasContextData": "true"
    },
    "logSourceId": {
        "userPoolId": "us-west-2_EXAMPLE"
    }
}
```
