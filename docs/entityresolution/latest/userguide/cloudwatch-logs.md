# Monitoring and logging workflows using Amazon CloudWatch Logs

AWS Entity Resolution provides comprehensive logging capabilities that help you check and analyze your
matching and ID mapping workflows. Through integration with Amazon CloudWatch Logs, you can capture
detailed information about workflow execution, including event types, timestamps, processing
statistics, and error counts. You can choose to deliver these logs to CloudWatch Logs, Amazon S3, or
Amazon Data Firehose destinations. By analyzing these logs, you can evaluate service performance,
troubleshoot issues, gain insights into your customer base, and better understand your AWS Entity Resolution
usage and billing. While logging is disabled by default, you can enable it for both new and
existing workflows through the console or API.

Standard Amazon CloudWatch vending charges apply when you enable logging for AWS Entity Resolution workflows,
including costs associated with log ingestion, storage, and analysis; for detailed pricing
information, visit the [CloudWatch pricing page.](https://aws.amazon.com/cloudwatch/pricing/#Vended_Logs "https://aws.amazon.com/cloudwatch/pricing/#Vended_Logs").

###### Topics

- [Setting up log delivery](#set-up-log-delivery "#set-up-log-delivery")
- [Disabling logging (console)](#disabling-logging "#disabling-logging")
- [Reading the logs](#reading-the-logs "#reading-the-logs")

## Setting up log delivery

This section will explain the necessary permissions required to use AWS Entity Resolution logging and how
to enable log delivery using the console and APIs.

###### Topics

- [Permissions](#cloudwatch-logs-console-permissions "#cloudwatch-logs-console-permissions")
- [Enabling logging for a new workflow
  (console)](#enable-logging-new-workflow-console "#enable-logging-new-workflow-console")
- [Enabling logging for a new workflow (API)](#set-up-log-delivery-api "#set-up-log-delivery-api")
- [Enabling logging for an existing workflow
  (console)](#enable-logging-console "#enable-logging-console")

### Permissions

AWS Entity Resolution uses CloudWatch vended logs to deliver workflow logging. To deliver workflow logs, you
need permissions to the logging destination that you specify.

To see the required permissions for each logging destination, choose from the
following AWS services in the _Amazon CloudWatch Logs User
Guide_.

- [Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-CloudWatchLogs "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-CloudWatchLogs")
- [Amazon Simple Storage Service (Amazon S3)](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-S3 "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-S3")
- [Amazon Data Firehose](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-Firehose "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-Firehose")

To create, view, or change logging configuration in AWS Entity Resolution, you must have the required
permissions. Your IAM role must include the following minimum permissions to manage
workflow logging in the AWS Entity Resolution console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowLogDeliveryActionsConsoleCWL",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogGroups"
 ],
 "Resource": [
 "arn:aws:logs:us-east-1:111122223333:log-group:*"
 ]
 },
 {
 "Sid": "AllowLogDeliveryActionsConsoleS3",
 "Effect": "Allow",
 "Action": [
 "s3:ListAllMyBuckets",
 "s3:ListBucket",
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::*"
 ]
 },
 {
 "Sid": "AllowLogDeliveryActionsConsoleFH",
 "Effect": "Allow",
 "Action": [
 "firehose:ListDeliveryStreams",
 "firehose:DescribeDeliveryStream"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

For more information about permissions to manage workflow logging, see [Enable logging from AWS services](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md") in the _Amazon CloudWatch Logs
User Guide_.

### Enabling logging for a new workflow

(console)

After you set up permissions to the logging destination, you can enable logging for a
new workflow in AWS Entity Resolution using the console.

###### To enable logging for a new workflow (console)

1. Open the AWS Entity Resolution console at [https://console.aws.amazon.com/entityresolution/home](https://console.aws.amazon.com/mediapackage/ "https://console.aws.amazon.com/mediapackage/").
2. Under **Workflows**, select either **Matching**
   workflows or **ID mapping** workflows.
3. Follow the steps to create one of the following workflows:
   - [Rule-based matching
     workflow](creating-matching-workflow-rule-based.md "creating-matching-workflow-rule-based.md")
   - [Machine learning-based matching
     workflow](create-matching-workflow-ml.md "create-matching-workflow-ml.md")
   - [Provider service-based
     matching workflow](create-matching-workflow-provider.md "create-matching-workflow-provider.md")
   - [ID mapping workflow
     for one account](creating-id-mapping-workflow-same-account.md "creating-id-mapping-workflow-same-account.md")
   - [ID mapping workflow
     across two accounts](creating-id-mapping-workflow-two-accounts.md "creating-id-mapping-workflow-two-accounts.md")

4. For **Step 1 Specify Matching workflow details**, for
   **Log deliveries – EntityResolution Workflow Logs**, choose
   **Add**.
   1. Choose one of the following logging destinations.
      - **To Amazon CloudWatch Logs**
      - **To Amazon S3**
      - **To Amazon Data Firehose**

   ###### Tip

   If you choose Amazon S3 or Firehose, you can deliver your logs to a **Cross
   account** or **In current account**.

   To enable cross-account delivery, both AWS accounts must have the required
   permissions. For more information, see the [Cross-account delivery example](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#vended-logs-crossaccount-example "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#vended-logs-crossaccount-example") in the _Amazon CloudWatch Logs User Guide_.

5. For the **Destination log group**, the log groups that are
   prefixed with **'/aws/vendedlogs/'** are created automatically. If
   you are using other log groups, you them before setting up a log delivery. For more
   information, see [Working
   with log groups and log streams](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md") in the _Amazon CloudWatch Logs
   User Guide_.
6. For **More settings - optional**, choose the following:
   1. For **Field selection**, select the log fields to include in
      each log record.
   2. (CloudWatch Logs) For **Output format**, choose the output format for
      the log.
   3. For **Field delimiter**, choose how to separate each log
      field.
   4. (Amazon S3) For **Suffix**, specify the suffix path to partition
      your data.
   5. (Amazon S3) For **Hive-compatible**, choose
      **Enable** if you want to use Hive-compatible S3 paths.

7. To create another log destination, choose **Add** and repeat
   steps 4 – 6.
8. Complete the remaining steps to set up and run the workflow.
9. After the workflow jobs completes, check the workflow logs in the log delivery
   destination you specified.

### Enabling logging for a new workflow (API)

After you set up permissions to the logging destination, you can enable logging for a
new workflow in AWS Entity Resolution using the Amazon CloudWatch Logs APIs.

###### To enable logging for a new workflow (API)

1. After you a create a workflow in the AWS Entity Resolution console, get the Amazon Resource Name
   (ARN) of the workflow.

You can find the ARN from the workflow page in the AWS Entity Resolution console or you call the
`GetMatchingWorkflow` or `GetIdMappingWorkflow` API operation.

A workflow ARN follows this format:

`arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(matchingworkflow/[a-zA-Z_0-9-]{1,255})`

An ID mapping ARN follows this format:

`arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(idmappingworkflow/[a-zA-Z_0-9-]{1,255})`

For more information, see [GetMatchingWorkflow](../apireference/API_GetMatchingWorkflow.md "../apireference/API_GetMatchingWorkflow.md") or [GetIdMappingWorkflow](../apireference/API_GetIdMappingWorkflow.md "../apireference/API_GetIdMappingWorkflow.md") in the _AWS Entity Resolution API
Reference_. 2. Use the CloudWatch Logs `PutDeliverySource` API operation to create a delivery
source for the workflow logs.

For more information, see [PutDeliverySource](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md") in the Amazon CloudWatch Logs API Reference.

    1. Pass the `resourceArn`.
    2. For `logType`, the type of logs that are collected are
     `WORKFLOW_LOGS`:###### Example

Example `PutDeliverySource` API operation

```
{
    "logType": "WORKFLOW_LOGS",
    "name": "my-delivery-source",
    "resourceArn": "arn:aws:entityresolution:region:accoungId:matchingworkflow/XXXWorkflow"
}
```

3. Use the `PutDeliveryDestination` API operation to configure where to
   store your logs.

You can choose either CloudWatch Logs, Amazon S3, or Firehose as the destination. You must specify
the ARN of one of the destination options for where your logs will be stored.

For more information, see [PutDeliveryDestination](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md") in the Amazon CloudWatch Logs API Reference.

###### Example

Example `PutDeliveryDestination` API operation

```
{
   "delivery-destination-configuration": {
      "destinationResourceArn": "arn:aws:logs:region:accountId:log-group:my-log-group"
   },
   "name": "my-delivery-destination",
   "outputFormat": "json",
   }
}
```

###### Note

If you're delivering logs cross-account, you must use the
**PutDeliveryDestinationPolicy** API to assign an AWS Identity and Access Management
(IAM) policy to the destination account. The IAM policy allows delivery from one
account to another account. 4. Use the `CreateDelivery` API operation to link the delivery source to
the destination that you created in the earlier steps. This API operation associates
the delivery source with the end destination.

For more information, see [PutDeliveryDestination](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md") in the Amazon CloudWatch Logs API Reference.

###### Example

Example `CreateDelivery` API operation

```
{
   "delivery-destination-arn": "arn:aws:logs:region:accountId:log-group:my-log-group",
   "delivery-source-name": "my-delivery-source",
   "tags": {
      "string" : "string"
   }
}
```

5. Run the workflow.
6. After the workflow jobs completes, check the workflow logs in the log delivery
   destination you specified.

### Enabling logging for an existing workflow

(console)

After you set up permissions to the logging destination, you can enable logging for an
existing workflow in AWS Entity Resolution using the **Log deliveries** tab on the
console.

###### To enable logging for an existing workflow using the \*\*Log

deliveries\*\* tab (console)

1. Open the AWS Entity Resolution console at [https://console.aws.amazon.com/entityresolution/home](https://console.aws.amazon.com/mediapackage/ "https://console.aws.amazon.com/mediapackage/").
2. Under **Workflows**, select either **Matching**
   workflows or **ID mapping** workflows, and then select your existing
   workflow.
3. On the **Log deliveries** tab, under **Log
   delivery**, select **Add**, and then choose one of the
   following logging destinations.
   - To Amazon CloudWatch Logs
   - To Amazon S3
     - Cross account
     - In current account

   - To Amazon Data Firehose
     - Cross account
     - In current account

###### Tip

If you choose Amazon S3 or Firehose, you can deliver your logs to a **Cross
account** or **In current account**.

To enable cross-account delivery, both AWS accounts must have the required
permissions. For more information, see the [Cross-account delivery example](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#vended-logs-crossaccount-example "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#vended-logs-crossaccount-example") in the _Amazon CloudWatch Logs
User Guide_. 4. In the modal, do the following, depending on the type of Log delivery you chose.

    1. View the **Log type**:
     **WORKFLOW\_LOGS**.


    The **Log type** can't be changed.
    2. (CloudWatch Logs) For the **Destination log group**, the log groups
     that are prefixed with **'/aws/vendedlogs/'** are created
     automatically. If you are using other log groups, you them before setting up a log
     delivery. For more information, see [Working with log groups and log streams](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md") in the *Amazon CloudWatch Logs User Guide*.


    (Amazon S3 in current account) For **Destination S3 bucket**,
     select a bucket or enter an ARN.


    (Amazon S3 cross account) For **Delivery destination ARN**, enter
     a delivery destination ARN.


    (Firehose in current account) For **Destination delivery
     stream**, enter the ARN of the delivery destination resource that was
     created in another account.


    (Firehose cross account) For **Delivery destination ARN**, enter
     a delivery destination ARN.

5. For **More settings - optional**, choose the following:
   1. For **Field selection**, select the log fields to include in
      each log record.
   2. (CloudWatch Logs) For **Output format**, choose the output format for
      the log.
   3. For **Field delimiter**, choose how to separate each log
      field.
   4. (Amazon S3) For **Suffix**, specify the suffix path to
      partition your data.
   5. (Amazon S3) For **Hive-compatible**, choose
      **Enable** if you want to use Hive-compatible S3 paths.

6. Choose **Add**.
7. On the workflow page, choose **Run**.
8. After the workflow jobs completes, check the workflow logs in the log delivery
   destination you specified.

## Disabling logging (console)

You can disable logging for your AWS Entity Resolution workflow at any time in the console.

###### To disable workflow logging (console)

1. Open the AWS Entity Resolution console at [https://console.aws.amazon.com/entityresolution/home](https://console.aws.amazon.com/mediapackage/ "https://console.aws.amazon.com/mediapackage/").
2. Under **Workflows**, select either **Matching**
   workflows or **ID mapping** workflows, and then select your workflow.
3. On the **Log deliveries** tab, under **Log
   delivery**, select the destination, and then choose
   **Delete**.
4. Review your changes and then navigate to the next step to save your changes.

## Reading the logs

Reading Amazon CloudWatch Logs helps you maintain efficient AWS Entity Resolution workflows. Logs give detailed
visibility into your workflow execution, including important metrics like the number of
records processed and any errors encountered, helping you ensure your data processing is
running smoothly. In addition, the logs offer real-time tracking of workflow progression
through timestamps and event types, allowing you to quickly identify bottlenecks or issues
in your data processing pipeline. The comprehensive error tracking and record count
information helps you keep data quality and completeness by showing exactly how many records
were processed successfully and if any remained unprocessed.

If you're using CloudWatch Logs as the destination, you can use CloudWatch Logs Insights to read the
workflow logs. Typical CloudWatch Logs charges apply. For more information, see [Analyzing
Log Data with CloudWatch Logs Insights](../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md "../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md") in the _Amazon CloudWatch Logs
User Guide_.

###### Note

Workflow logs can take a few minutes to appear in your destination. If you don't see
the logs, wait a few minutes and refresh the page.

The workflow logs consist of a sequence of formatted log records, where each log record
represents one workflow. The order of the fields within the log can vary.

```
{
  "resource_arn": "arn:aws:ses:us-east-1:1234567890:mailmanager-ingress-point/inp-xxxxx",
  "event_type": "JOB_START",
  "event_timestamp": 1728562395042,
  "job_id": "b01eea4678d4423a4b43eeada003f6",
  "workflow_name": "TestWorkflow",
  "workflow_start_time": "2025-03-11 10:19:56",
  "data_procesing_progression": "Matching Job Starts ...",
  "total_records_processed": 1500,
  "total_records_unprocessed": 0,
  "incremental_records_processed": 0,
  "error_message": "sample error that caused workflow failure"
}
```

The following list describes the log record fields, in order:

`resource_arn`

The Amazon Resource Name (ARN) that uniquely identifies the AWS resource being
used in the workflow.

`event_type`

The type of event that occurred during the workflow execution. AWS Entity Resolution currently
supports:

`JOB_START`

`DATA_PROCESSING_STEP_START`

`DATA_PROCESSING_STEP_END`

`JOB_SUCCESS`

`JOB_FAILURE`

`event_timestamp`

The Unix timestamp indicating when the event occurred during the workflow.

`job_id`

A unique identifier assigned to the specific workflow job execution.

`workflow_name`

The name given to the workflow being executed.

`workflow_start_time`

The date and time when the workflow execution began.

`data_procesing_progression`

A description of the current stage in the data processing workflow. Examples:
`"Matching Job Starts"`, `"Loading Step Starts"`,
`"ID_Mapping Job Ends Successfully"`.

`total_records_processed`

The total number of records that were successfully processed during the
workflow.

`total_records_unprocessed`

The number of records that weren't processed during the workflow execution.

`incremental_records_processed`

The number of new records processed in an incremental workflow update.

`error_message`

The root cause of workflow failure.
