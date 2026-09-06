

# DataDeletionJob
<a name="API_DataDeletionJob"></a>

Describes a job that deletes all references to specific users from an Amazon Personalize dataset group in batches. For information about creating a data deletion job, see [Deleting users](https://docs.aws.amazon.com/personalize/latest/dg/delete-records.html).

## Contents
<a name="API_DataDeletionJob_Contents"></a>

 ** creationDateTime **   <a name="personalize-Type-DataDeletionJob-creationDateTime"></a>
The creation date and time (in Unix time) of the data deletion job.  
Type: Timestamp  
Required: No

 ** dataDeletionJobArn **   <a name="personalize-Type-DataDeletionJob-dataDeletionJobArn"></a>
The Amazon Resource Name (ARN) of the data deletion job.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`   
Required: No

 ** datasetGroupArn **   <a name="personalize-Type-DataDeletionJob-datasetGroupArn"></a>
The Amazon Resource Name (ARN) of the dataset group the job deletes records from.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`   
Required: No

 ** dataSource **   <a name="personalize-Type-DataDeletionJob-dataSource"></a>
Describes the data source that contains the data to upload to a dataset, or the list of records to delete from Amazon Personalize.  
Type: [DataSource](API_DataSource.md) object  
Required: No

 ** failureReason **   <a name="personalize-Type-DataDeletionJob-failureReason"></a>
If a data deletion job fails, provides the reason why.  
Type: String  
Required: No

 ** jobName **   <a name="personalize-Type-DataDeletionJob-jobName"></a>
The name of the data deletion job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`   
Required: No

 ** lastUpdatedDateTime **   <a name="personalize-Type-DataDeletionJob-lastUpdatedDateTime"></a>
The date and time (in Unix time) the data deletion job was last updated.  
Type: Timestamp  
Required: No

 ** numDeleted **   <a name="personalize-Type-DataDeletionJob-numDeleted"></a>
The number of records deleted by a COMPLETED job.  
Type: Integer  
Required: No

 ** roleArn **   <a name="personalize-Type-DataDeletionJob-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that has permissions to read from the Amazon S3 data source.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`   
Required: No

 ** status **   <a name="personalize-Type-DataDeletionJob-status"></a>
The status of the data deletion job.  
A data deletion job can have one of the following statuses:  
+ PENDING > IN\_PROGRESS > COMPLETED -or- FAILED
Type: String  
Length Constraints: Maximum length of 256.  
Required: No

## See Also
<a name="API_DataDeletionJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-2018-05-22/DataDeletionJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-2018-05-22/DataDeletionJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-2018-05-22/DataDeletionJob) 