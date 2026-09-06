

# Monitoring snapshot exports for Amazon RDS
<a name="USER_ExportSnapshot.Monitoring"></a>

You can monitor DB snapshot exports using the AWS Management Console, the AWS CLI, or the RDS API.

## Console
<a name="USER_ExportSnapshot.MonitorConsole"></a>

**To monitor DB snapshot exports**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Snapshots**.

1. To view the list of snapshot exports, choose the **Exports in Amazon S3** tab.

1. To view information about a specific snapshot export, choose the export task.

## AWS CLI
<a name="USER_ExportSnapshot.MonitorCLI"></a>

To monitor DB snapshot exports using the AWS CLI, use the [ describe-export-tasks](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-export-tasks.html) command.

The following example shows how to display current information about all of your snapshot exports.

**Example**  

```
 1. aws rds describe-export-tasks
 2. 
 3. {
 4.     "ExportTasks": [
 5.         {
 6.             "Status": "CANCELED",
 7.             "TaskEndTime": "2019-11-01T17:36:46.961Z",
 8.             "S3Prefix": "something",
 9.             "ExportTime": "2019-10-24T20:23:48.364Z",
10.             "S3Bucket": "{{amzn-s3-demo-bucket}}",
11.             "PercentProgress": 0,
12.             "KmsKeyId": "arn:aws:kms:{{AWS_Region}}:123456789012:key/K7MDENG/bPxRfiCYEXAMPLEKEY",
13.             "ExportTaskIdentifier": "anewtest",
14.             "IamRoleArn": "arn:aws:iam::123456789012:role/export-to-s3",
15.             "TotalExtractedDataInGB": 0,
16.             "TaskStartTime": "2019-10-25T19:10:58.885Z",
17.             "SourceArn": "arn:aws:rds:{{AWS_Region}}:123456789012:snapshot:parameter-groups-test"
18.         },
19. {
20.             "Status": "COMPLETE",
21.             "TaskEndTime": "2019-10-31T21:37:28.312Z",
22.             "WarningMessage": "{\"skippedTables\":[],\"skippedObjectives\":[],\"general\":[{\"reason\":\"FAILED_TO_EXTRACT_TABLES_LIST_FOR_DATABASE\"}]}",
23.             "S3Prefix": "",
24.             "ExportTime": "2019-10-31T06:44:53.452Z",
25.             "S3Bucket": "{{amzn-s3-demo-bucket1}}",
26.             "PercentProgress": 100,
27.             "KmsKeyId": "arn:aws:kms:{{AWS_Region}}:123456789012:key/2Zp9Utk/h3yCo8nvbEXAMPLEKEY",
28.             "ExportTaskIdentifier": "thursday-events-test", 
29.             "IamRoleArn": "arn:aws:iam::123456789012:role/export-to-s3",
30.             "TotalExtractedDataInGB": 263,
31.             "TaskStartTime": "2019-10-31T20:58:06.998Z",
32.             "SourceArn": "arn:aws:rds:{{AWS_Region}}:123456789012:snapshot:rds:example-1-2019-10-31-06-44"
33.         },
34.         {
35.             "Status": "FAILED",
36.             "TaskEndTime": "2019-10-31T02:12:36.409Z",
37.             "FailureCause": "The S3 bucket edgcuc-export isn't located in the current AWS Region. Please, review your S3 bucket name and retry the export.",
38.             "S3Prefix": "",
39.             "ExportTime": "2019-10-30T06:45:04.526Z",
40.             "S3Bucket": "{{amzn-s3-demo-bucket2}}",
41.             "PercentProgress": 0,
42.             "KmsKeyId": "arn:aws:kms:{{AWS_Region}}:123456789012:key/2Zp9Utk/h3yCo8nvbEXAMPLEKEY",
43.             "ExportTaskIdentifier": "wednesday-afternoon-test",
44.             "IamRoleArn": "arn:aws:iam::123456789012:role/export-to-s3",
45.             "TotalExtractedDataInGB": 0,
46.             "TaskStartTime": "2019-10-30T22:43:40.034Z",
47.             "SourceArn": "arn:aws:rds:{{AWS_Region}}:123456789012:snapshot:rds:example-1-2019-10-30-06-45"
48.         }
49.     ]
50. }
```
To display information about a specific snapshot export, include the `--export-task-identifier` option with the `describe-export-tasks` command. To filter the output, include the `--Filters` option. For more options, see the [ describe-export-tasks](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-export-tasks.html) command.

## RDS API
<a name="USER_ExportSnapshot.MonitorAPI"></a>

To display information about DB snapshot exports using the Amazon RDS API, use the [DescribeExportTasks](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeExportTasks.html) operation.

To track completion of the export workflow or to initiate another workflow, you can subscribe to Amazon Simple Notification Service topics. For more information on Amazon SNS, see [Working with Amazon RDS event notification](USER_Events.md).