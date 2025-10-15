# Logging with AWS CloudTrail for S3 Tables

 Amazon S3 is integrated with AWS CloudTrail, a service that provides a record of actions taken by a
 user, role, or an AWS service. CloudTrail captures all API calls for Amazon S3 as events. Using
 the information collected by CloudTrail, you can determine the request that was made to Amazon S3,
 the IP address from which the request was made, when it was made, and additional details.
 When a supported event activity occurs in Amazon S3, that activity is recorded in a CloudTrail
 event. You can use AWS CloudTrail trail to log management events and data events for S3 Tables.
 For more information, see [Amazon S3 CloudTrail events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html")
 and [What is
 AWS CloudTrail?](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html")  in the *AWS CloudTrailUser Guide*.


## CloudTrail management events for S3 Tables


Management events provide information about management operations that are performed on resources in your AWS account. 


By default, CloudTrail logs management events for S3 Tables. The `eventsource` for CloudTrail management events for S3 Tables is  `s3tables.amazonaws.com`. 
 When you set up your AWS account, CloudTrail management events are enabled by default. The following management events are logged to CloudTrail. 
 



* [`CreateNamespace`](../API/API_s3TableBuckets_CreateNamespace.md "../API/API_s3TableBuckets_CreateNamespace.md")
* [`CreateTable`](../API/API_s3TableBuckets_CreateTable.md "../API/API_s3TableBuckets_CreateTable.md")
* [`CreateTableBucket`](../API/API_s3TableBuckets_CreateTableBucket.md "../API/API_s3TableBuckets_CreateTableBucket.md")
* [`DeleteNamespace`](../API/API_s3TableBuckets_DeleteNamespace.md "../API/API_s3TableBuckets_DeleteNamespace.md")
* [`DeleteTable`](../API/API_s3TableBuckets_DeleteTable.md "../API/API_s3TableBuckets_DeleteTable.md")
* [`DeleteTableBucket`](../API/API_s3TableBuckets_DeleteTableBucket.md "../API/API_s3TableBuckets_DeleteTableBucket.md")
* [`DeleteTableBucketPolicy`](../API/API_s3TableBuckets_DeleteTableBucketPolicy.md "../API/API_s3TableBuckets_DeleteTableBucketPolicy.md")
* [`DeleteTablePolicy`](../API/API_s3TableBuckets_DeleteTablePolicy.md "../API/API_s3TableBuckets_DeleteTablePolicy.md")
* [`GetNamespace`](../API/API_s3TableBuckets_GetNamespace.md "../API/API_s3TableBuckets_GetNamespace.md")
* [`GetTable`](../API/API_s3TableBuckets_GetTable.md "../API/API_s3TableBuckets_GetTable.md")
* [`GetTableBucket`](../API/API_s3TableBuckets_GetTableBucket.md "../API/API_s3TableBuckets_GetTableBucket.md")
* [`GetTableBucketMaintenanceConfiguration`](../API/API_s3TableBuckets_GetTableBucketMaintenanceConfiguration.md "../API/API_s3TableBuckets_GetTableBucketMaintenanceConfiguration.md")
* [`GetTableBucketPolicy`](../API/API_s3TableBuckets_GetTableBucketPolicy.md "../API/API_s3TableBuckets_GetTableBucketPolicy.md")
* [`GetTableMaintenanceConfiguration`](../API/API_s3TableBuckets_GetTableMaintenanceConfiguration.md "../API/API_s3TableBuckets_GetTableMaintenanceConfiguration.md")
* [`GetTableMaintenanceJobStatus`](../API/API_s3TableBuckets_GetTableMaintenanceJobStatus.md "../API/API_s3TableBuckets_GetTableMaintenanceJobStatus.md")
* [`GetTableMetadataLocation`](../API/API_s3TableBuckets_GetTableMetadataLocation.md "../API/API_s3TableBuckets_GetTableMetadataLocation.md")
* [`GetTablePolicy`](../API/API_s3TableBuckets_GetTablePolicy.md "../API/API_s3TableBuckets_GetTablePolicy.md")
* [`ListNamespaces`](../API/API_s3TableBuckets_ListNamespaces.md "../API/API_s3TableBuckets_ListNamespaces.md")
* [`ListTableBuckets`](../API/API_s3TableBuckets_ListTableBuckets.md "../API/API_s3TableBuckets_ListTableBuckets.md")
* [`ListTables`](../API/API_s3TableBuckets_ListTables.md "../API/API_s3TableBuckets_ListTables.md")
* [`PutTableBucketMaintenanceConfiguration`](../API/API_s3TableBuckets_PutTableBucketMaintenanceConfiguration.md "../API/API_s3TableBuckets_PutTableBucketMaintenanceConfiguration.md")
* [`PutTableMaintenanceConfiguration`](../API/API_s3TableBuckets_PutTableMaintenanceConfiguration.md "../API/API_s3TableBuckets_PutTableMaintenanceConfiguration.md")
* [`PutBucketPolicy`](../API/API_s3TableBuckets_PutBucketPolicy.md "../API/API_s3TableBuckets_PutBucketPolicy.md")
* [`PutTablePolicy`](../API/API_s3TableBuckets_PutTablePolicy.md "../API/API_s3TableBuckets_PutTablePolicy.md")
* [`RenameTable`](../API/API_s3TableBuckets_RenameTable.md "../API/API_s3TableBuckets_RenameTable.md")
* [`UpdateTableMetadataLocation`](../API/API_s3TableBuckets_UpdateTableMetadataLocation.md "../API/API_s3TableBuckets_UpdateTableMetadataLocation.md")

For more information on CloudTrail management events, see [Logging management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html") in the *AWS CloudTrail User
 Guide*. 


## CloudTrail data events for S3 Tables


Data events provide information about the resource operations performed on or in a
 resource.By default, CloudTrail trails don't log data events, but you can configure trails to log data events. 


When you log data events for a trail in CloudTrail, you will choose or specify the
 resource type. S3 Tables has two resources types, `AWS::S3Tables::Table` and
 `AWS::S3Tables::TableBucket`.
 
 


The following data events are logged to CloudTrail. 



* [`AbortMultipartUpload`](../API/API_AbortMultipartUpload.md "../API/API_AbortMultipartUpload.md")
* [`CompleteMultipartUpload`](../API/API_CompleteMultipartUpload.md "../API/API_CompleteMultipartUpload.md")
* [`CreateMultipartUpload`](../API/API_CreateMultipartUpload.md "../API/API_CreateMultipartUpload.md")
* [`GetObject`](../API/API_GetObject.md "../API/API_GetObject.md")
* [`HeadObject`](../API/API_HeadObject.md "../API/API_HeadObject.md")
* [`ListParts`](../API/API_ListParts.md "../API/API_ListParts.md")
* [`PutObject`](../API/API_PutObject.md "../API/API_PutObject.md")
* [`UploadPart`](../API/API_UploadPart.md "../API/API_UploadPart.md")

For more information on CloudTrail data events, see [Logging data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html") in the *AWS CloudTrail User
 Guide*. 


For additional information about CloudTrail events for S3 Tables, see the following
 topics: 

###### Topics

* [AWS CloudTrail data event log file examples for S3 Tables](s3-tables-log-files.md "s3-tables-log-files.md")
