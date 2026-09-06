

# DynamoDB data export to Amazon S3: how it works
<a name="S3DataExport.HowItWorks"></a>

DynamoDB export to S3 is a fully managed solution for exporting your DynamoDB data to an Amazon S3 bucket at scale. Using DynamoDB export to S3, you can export data from an Amazon DynamoDB table from any time within your [point-in-time recovery (PITR)](Point-in-time-recovery.md) window to an Amazon S3 bucket. You need to enable PITR on your table to use the export functionality. This feature enables you to perform analytics and complex queries on your data using other AWS services such as Athena, AWS Glue, Amazon SageMaker AI, Amazon EMR, and AWS Lake Formation.

DynamoDB export to S3 allows you to export both full and incremental data from your DynamoDB table. Exports are asynchronous, they don't consume [read capacity units (RCUs)](provisioned-capacity-mode.md) and have no impact on table performance and availability. The export file formats supported are DynamoDB JSON and Amazon Ion formats. You can also export data to an S3 bucket owned by another AWS account and to a different AWS region. Your data is always encrypted end-to-end.

**Note**  
No service-level agreement (SLA) guarantees export completion times, and these times can vary. An export's duration depends on factors such as the size of the table or data being exported, how the data is distributed across the table, and other exports that are in progress. For this reason, avoid building workflows that depend on an export completing within a fixed amount of time.

DynamoDB full exports are charged based on the size of the DynamoDB table (table data and local secondary indexes) at the point in time for which the export is done. DynamoDB incremental exports are charged based on the size of data processed from your continuous backups for the time period being exported. Incremental export has a minimum charge of 10MB. Additional charges apply for storing exported data in Amazon S3 and for `PUT` requests made against your Amazon S3 bucket. For more information about these charges, see [Amazon DynamoDB pricing](https://aws.amazon.com/dynamodb/pricing/) and [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/).

For specifics on service quotas, see [Table export to Amazon S3](ServiceQuotas.md#limits-table-export). 

**Topics**
+ [Requesting a table export in DynamoDB](S3DataExport_Requesting.md)
+ [DynamoDB table export output format](S3DataExport.Output.md)