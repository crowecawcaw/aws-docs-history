# View flow log records with Amazon S3

You can view your flow log records using the Amazon S3 console. After you create your
flow log, it might take a few minutes for it to be visible in the console.

The log files are compressed. If you open the log files using the Amazon S3 console,
they are decompressed and the flow log records are displayed. If you download the
files, you must decompress them to view the flow log records.

###### To view flow log records published to Amazon S3

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Select the name of the bucket to open its details page.
3. Navigate to the folder with the log files. For example,
   `prefix`/AWSLogs/`account_id`/vpcflowlogs/`region`/`year`/`month`/`day`/.
4. Select the checkbox next to the file name, and then choose
   **Download**.
   You can also query the flow log records in the log files using Amazon Athena. Amazon Athena
   is an interactive query service that makes it easier to analyze data in Amazon S3 using
   standard SQL. For more information, see [Querying Amazon VPC Flow Logs](../../../athena/latest/ug/vpc-flow-logs.md "../../../athena/latest/ug/vpc-flow-logs.md") in the _Amazon Athena User
   Guide_.
