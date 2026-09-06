

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# DatasetSummary
<a name="API_DatasetSummary"></a>

Contains information about the specific data set, including name, ARN, and status. 

## Contents
<a name="API_DatasetSummary_Contents"></a>

 ** CreatedAt **   <a name="LookoutForEquipment-Type-DatasetSummary-CreatedAt"></a>
The time at which the dataset was created in Amazon Lookout for Equipment.   
Type: Timestamp  
Required: No

 ** DatasetArn **   <a name="LookoutForEquipment-Type-DatasetSummary-DatasetArn"></a>
The Amazon Resource Name (ARN) of the specified dataset.   
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:dataset\/[0-9a-zA-Z_-]{1,200}\/.+`   
Required: No

 ** DatasetName **   <a name="LookoutForEquipment-Type-DatasetSummary-DatasetName"></a>
The name of the dataset.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z_-]{1,200}$`   
Required: No

 ** Status **   <a name="LookoutForEquipment-Type-DatasetSummary-Status"></a>
Indicates the status of the dataset.   
Type: String  
Valid Values: `CREATED | INGESTION_IN_PROGRESS | ACTIVE | IMPORT_IN_PROGRESS`   
Required: No

## See Also
<a name="API_DatasetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/DatasetSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/DatasetSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/DatasetSummary) 