# Monitor with Amazon CloudWatch Logs

Configure AWS IoT SiteWise to log information to CloudWatch Logs to monitor and troubleshoot the
service.

When you use the AWS IoT SiteWise console, AWS IoT SiteWise creates a service-linked role that allows the
service to log information on your behalf. If you don't use the AWS IoT SiteWise console, you must create
a service-linked role manually to receive logs. For more information, see [Create a service-linked role for
AWS IoT SiteWise](create-service-linked-role.md "create-service-linked-role.md").

You must have a resource policy that allows AWS IoT SiteWise to put log events into CloudWatch streams. To
create and update a resource policy for CloudWatch Logs, run the following command. Replace
`logging-policy-name` with the name of the policy to create.

```
aws logs put-resource-policy --policy-name `logging-policy-name` --policy-document "{ \"Version\": \"2012-10-17\", \"Statement\": [ { \"Sid\": \"IoTSiteWiseToCloudWatchLogs\", \"Effect\": \"Allow\", \"Principal\": { \"Service\": [ \"iotsitewise.amazonaws.com\" ] }, \"Action\":\"logs:PutLogEvents\", \"Resource\": \"*\" } ] }"
```

CloudWatch Logs also supports [aws:SourceArn](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [aws:SourceAccount](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-ke-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-ke-sourceaccount") condition context keys. These condition context keys are
optional.

To create or update a resource policy that allows AWS IoT SiteWise to only put logs associated with
the specified AWS IoT SiteWise resource into CloudWatch streams, run the command and do the following:

- Replace `logging-policy-name` with the name of the policy to
  create.
- Replace `source-ARN` with the ARN of your AWS IoT SiteWise resource, such
  as an asset model or asset. To find the ARN for each AWS IoT SiteWise resource type, see [Resource types defined by AWS IoT SiteWise](../../../service-authorization/latest/reference/list_awsiotsitewise.md#awsiotsitewise-resources-for-iam-policies "../../../service-authorization/latest/reference/list_awsiotsitewise.md#awsiotsitewise-resources-for-iam-policies") in the _Service Authorization
  Reference_.
- Replace `account-ID` with the AWS account ID associated with
  the specified AWS IoT SiteWise resource.

```
aws logs put-resource-policy --policy-name `logging-policy-name` --policy-document "{ \"Version\": \"2012-10-17\", \"Statement\": [ { \"Sid\": \"IoTSiteWiseToCloudWatchLogs\", \"Effect\": \"Allow\", \"Principal\": { \"Service\": [ \"iotsitewise.amazonaws.com\" ] }, \"Action\":\"logs:PutLogEvents\", \"Resource\": \"*\", \"Condition\":{\"StringLike\":{\"aws:SourceArn\":[\"`source-ARN`\"],\"aws:SourceAccount\":[\"`account-ID`\"]}}}]}"
```

By default, AWS IoT SiteWise doesn't log information to CloudWatch Logs. To activate logging, choose a logging
level other than **Disabled** (`OFF`). AWS IoT SiteWise supports the following
logging levels:

- `OFF` – Logging is turned off.
- `ERROR` – Errors are logged.
- `INFO` – Errors and informational messages are logged.
  You can configure SiteWise Edge gateways to log information to CloudWatch Logs through AWS IoT Greengrass. For more
  information, see [Monitor SiteWise Edge gateway logs](monitor-gateway-logs.md "monitor-gateway-logs.md").

You can also configure AWS IoT Core to log information to CloudWatch Logs if you are troubleshooting an
AWS IoT SiteWise rule action. For more information, see [Troubleshoot an AWS IoT SiteWise rule action](troubleshoot-rule.md "troubleshoot-rule.md").

###### Contents

- [Manage logging in AWS IoT SiteWise](monitor-cloudwatch-logs.md#manage-cloudwatch-logs "monitor-cloudwatch-logs.md#manage-cloudwatch-logs")
  - [Find your logging level](monitor-cloudwatch-logs.md#find-logging-level "monitor-cloudwatch-logs.md#find-logging-level")
  - [Change your logging level](monitor-cloudwatch-logs.md#change-logging-level "monitor-cloudwatch-logs.md#change-logging-level")

- [Example: AWS IoT SiteWise log file entries](monitor-cloudwatch-logs.md#sitewise-log-format "monitor-cloudwatch-logs.md#sitewise-log-format")

## Manage logging in AWS IoT SiteWise

Use the AWS IoT SiteWise console or AWS CLI for the following logging configuration tasks.

### Find your logging level

Console
Use the following procedure to find your current logging level in the AWS IoT SiteWise
console.

###### To find your current AWS IoT SiteWise logging level

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the left navigation pane, choose **Logging
   options**.

The current logging status appears under **Logging status**.
If logging is activated, the current logging level appears under **Level
of verbosity**.

AWS CLI
Run the following command to find your current AWS IoT SiteWise logging level with the
AWS CLI.

```
aws iotsitewise describe-logging-options
```

The operation returns a response that contains your logging level in the following
format.

```
{
  "loggingOptions": {
    "level": "`String`"
  }
}
```

### Change your logging level

Use the following procedure to change your logging level in the AWS IoT SiteWise console or using
AWS CLI.

Console

###### To change your AWS IoT SiteWise logging level

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the left navigation pane, choose **Logging
   options**.
3. Choose **Edit**.
4. Choose the **Level of verbosity** to activate.
5. Choose **Save**.

AWS CLI
Run the following AWS CLI command to change your AWS IoT SiteWise logging level. Replace
`logging-level` with the logging level you want.

```
aws iotsitewise put-logging-options --logging-options level=`logging-level`
```

## Example: AWS IoT SiteWise log file entries

Each AWS IoT SiteWise log entry includes event information and relevant resources for that event, so
you can understand and analyze log data.

The following example shows a CloudWatch Logs entry that AWS IoT SiteWise logs when you successfully create an
asset model.

```
{
  "eventTime": "2020-05-05T00:10:22.902Z",
  "logLevel": "INFO",
  "eventType": "AssetModelCreationSuccess",
  "message": "Successfully created asset model.",
  "resources": {
    "assetModelId": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE"
  }
}
```
