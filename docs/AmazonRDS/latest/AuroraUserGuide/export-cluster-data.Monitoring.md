

# Monitoring DB cluster export tasks
<a name="export-cluster-data.Monitoring"></a>

You can monitor DB cluster exports using the AWS Management Console, the AWS CLI, or the RDS API.

## Console
<a name="export-cluster-data.MonitorConsole"></a>

**To monitor DB cluster exports**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Exports in Amazon S3**.

   DB cluster exports are indicated in the **Source type** column. Export status is displayed in the **Status** column.

1. To view detailed information about a specific DB cluster export, choose the export task.

## AWS CLI
<a name="export-cluster-data.MonitorCLI"></a>

To monitor DB cluster export tasks using the AWS CLI, use the [ describe-export-tasks](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-export-tasks.html) command.

The following example shows how to display current information about all of your DB cluster exports.

**Example**  

```
 1. aws rds describe-export-tasks
 2. 
 3. {
 4.     "ExportTasks": [
 5.         {
 6.             "Status": "CANCELED",
 7.             "TaskEndTime": "2022-11-01T17:36:46.961Z",
 8.             "S3Prefix": "something",
 9.             "S3Bucket": "{{amzn-s3-demo-bucket}}",
10.             "PercentProgress": 0,
11.             "KmsKeyId": "arn:aws:kms:{{us-west-2}}:123456789012:key/K7MDENG/bPxRfiCYEXAMPLEKEY",
12.             "ExportTaskIdentifier": "anewtest",
13.             "IamRoleArn": "arn:aws:iam::123456789012:role/export-to-s3",
14.             "TotalExtractedDataInGB": 0,
15.             "SourceArn": "arn:aws:rds:{{us-west-2}}:123456789012:cluster:parameter-groups-test"
16.         },
17. {
18.             "Status": "COMPLETE",
19.             "TaskStartTime": "2022-10-31T20:58:06.998Z",
20.             "TaskEndTime": "2022-10-31T21:37:28.312Z",
21.             "WarningMessage": "{\"skippedTables\":[],\"skippedObjectives\":[],\"general\":[{\"reason\":\"FAILED_TO_EXTRACT_TABLES_LIST_FOR_DATABASE\"}]}",
22.             "S3Prefix": "",
23.             "S3Bucket": "{{amzn-s3-demo-bucket1}}",
24.             "PercentProgress": 100,
25.             "KmsKeyId": "arn:aws:kms:{{us-west-2}}:123456789012:key/2Zp9Utk/h3yCo8nvbEXAMPLEKEY",
26.             "ExportTaskIdentifier": "thursday-events-test", 
27.             "IamRoleArn": "arn:aws:iam::123456789012:role/export-to-s3",
28.             "TotalExtractedDataInGB": 263,
29.             "SourceArn": "arn:aws:rds:{{us-west-2}}:123456789012:cluster:example-1-2019-10-31-06-44"
30.         },
31.         {
32.             "Status": "FAILED",
33.             "TaskEndTime": "2022-10-31T02:12:36.409Z",
34.             "FailureCause": "The S3 bucket {{amzn-s3-demo-bucket2}} isn't located in the current AWS Region. Please, review your S3 bucket name and retry the export.",
35.             "S3Prefix": "",
36.             "S3Bucket": "{{amzn-s3-demo-bucket2}}",
37.             "PercentProgress": 0,
38.             "KmsKeyId": "arn:aws:kms:{{us-west-2}}:123456789012:key/2Zp9Utk/h3yCo8nvbEXAMPLEKEY",
39.             "ExportTaskIdentifier": "wednesday-afternoon-test",
40.             "IamRoleArn": "arn:aws:iam::123456789012:role/export-to-s3",
41.             "TotalExtractedDataInGB": 0,
42.             "SourceArn": "arn:aws:rds:{{us-west-2}}:123456789012:cluster:example-1-2019-10-30-06-45"
43.         }
44.     ]
45. }
```
To display information about a specific export task, include the `--export-task-identifier` option with the `describe-export-tasks` command. To filter the output, include the `--Filters` option. For more options, see the [ describe-export-tasks](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-export-tasks.html) command.

## RDS API
<a name="export-cluster-data.MonitorAPI"></a>

To display information about DB cluster exports using the Amazon RDS API, use the [DescribeExportTasks](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeExportTasks.html) operation.

To track completion of the export workflow or to initiate another workflow, you can subscribe to Amazon Simple Notification Service topics. For more information on Amazon SNS, see [Working with Amazon RDS event notification](USER_Events.md).