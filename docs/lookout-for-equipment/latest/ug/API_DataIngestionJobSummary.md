

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# DataIngestionJobSummary
<a name="API_DataIngestionJobSummary"></a>

Provides information about a specified data ingestion job, including dataset information, data ingestion configuration, and status. 

## Contents
<a name="API_DataIngestionJobSummary_Contents"></a>

 ** DatasetArn **   <a name="LookoutForEquipment-Type-DataIngestionJobSummary-DatasetArn"></a>
The Amazon Resource Name (ARN) of the dataset used in the data ingestion job.   
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:dataset\/[0-9a-zA-Z_-]{1,200}\/.+`   
Required: No

 ** DatasetName **   <a name="LookoutForEquipment-Type-DataIngestionJobSummary-DatasetName"></a>
The name of the dataset used for the data ingestion job.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z_-]{1,200}$`   
Required: No

 ** IngestionInputConfiguration **   <a name="LookoutForEquipment-Type-DataIngestionJobSummary-IngestionInputConfiguration"></a>
 Specifies information for the input data for the data inference job, including data Amazon S3 location parameters.   
Type: [IngestionInputConfiguration](API_IngestionInputConfiguration.md) object  
Required: No

 ** JobId **   <a name="LookoutForEquipment-Type-DataIngestionJobSummary-JobId"></a>
Indicates the job ID of the data ingestion job.   
Type: String  
Length Constraints: Maximum length of 32.  
Pattern: `[A-Fa-f0-9]{0,32}`   
Required: No

 ** Status **   <a name="LookoutForEquipment-Type-DataIngestionJobSummary-Status"></a>
Indicates the status of the data ingestion job.   
Type: String  
Valid Values: `IN_PROGRESS | SUCCESS | FAILED | IMPORT_IN_PROGRESS`   
Required: No

## See Also
<a name="API_DataIngestionJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/DataIngestionJobSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/DataIngestionJobSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/DataIngestionJobSummary) 