

# DataDeletionJobSummary
<a name="API_DataDeletionJobSummary"></a>

Provides a summary of the properties of a data deletion job. For a complete listing, call the [DescribeDataDeletionJob](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeDataDeletionJob.html) API operation.

## Contents
<a name="API_DataDeletionJobSummary_Contents"></a>

 ** creationDateTime **   <a name="personalize-Type-DataDeletionJobSummary-creationDateTime"></a>
The creation date and time (in Unix time) of the data deletion job.  
Type: Timestamp  
Required: No

 ** dataDeletionJobArn **   <a name="personalize-Type-DataDeletionJobSummary-dataDeletionJobArn"></a>
The Amazon Resource Name (ARN) of the data deletion job.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`   
Required: No

 ** datasetGroupArn **   <a name="personalize-Type-DataDeletionJobSummary-datasetGroupArn"></a>
The Amazon Resource Name (ARN) of the dataset group the job deleted records from.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`   
Required: No

 ** failureReason **   <a name="personalize-Type-DataDeletionJobSummary-failureReason"></a>
If a data deletion job fails, provides the reason why.  
Type: String  
Required: No

 ** jobName **   <a name="personalize-Type-DataDeletionJobSummary-jobName"></a>
The name of the data deletion job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`   
Required: No

 ** lastUpdatedDateTime **   <a name="personalize-Type-DataDeletionJobSummary-lastUpdatedDateTime"></a>
The date and time (in Unix time) the data deletion job was last updated.  
Type: Timestamp  
Required: No

 ** status **   <a name="personalize-Type-DataDeletionJobSummary-status"></a>
The status of the data deletion job.  
A data deletion job can have one of the following statuses:  
+ PENDING > IN\_PROGRESS > COMPLETED -or- FAILED
Type: String  
Length Constraints: Maximum length of 256.  
Required: No

## See Also
<a name="API_DataDeletionJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-2018-05-22/DataDeletionJobSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-2018-05-22/DataDeletionJobSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-2018-05-22/DataDeletionJobSummary) 