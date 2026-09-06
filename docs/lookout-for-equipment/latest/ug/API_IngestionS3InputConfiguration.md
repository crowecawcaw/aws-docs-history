

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# IngestionS3InputConfiguration
<a name="API_IngestionS3InputConfiguration"></a>

 Specifies S3 configuration information for the input data for the data ingestion job. 

## Contents
<a name="API_IngestionS3InputConfiguration_Contents"></a>

 ** Bucket **   <a name="LookoutForEquipment-Type-IngestionS3InputConfiguration-Bucket"></a>
The name of the S3 bucket used for the input data for the data ingestion.   
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 63.  
Pattern: `^[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]$`   
Required: Yes

 ** KeyPattern **   <a name="LookoutForEquipment-Type-IngestionS3InputConfiguration-KeyPattern"></a>
 The pattern for matching the Amazon S3 files that will be used for ingestion. If the schema was created previously without any KeyPattern, then the default KeyPattern {prefix}/{component\_name}/\* is used to download files from Amazon S3 according to the schema. This field is required when ingestion is being done for the first time.  
Valid Values: {prefix}/{component\_name}\_\* \| {prefix}/{component\_name}/\* \| {prefix}/{component\_name}[DELIMITER]\* (Allowed delimiters : space, dot, underscore, hyphen)  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** Prefix **   <a name="LookoutForEquipment-Type-IngestionS3InputConfiguration-Prefix"></a>
The prefix for the S3 location being used for the input data for the data ingestion.   
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Pattern: `(^$)|([\u0009\u000A\u000D\u0020-\u00FF]{1,1023}/$)`   
Required: No

## See Also
<a name="API_IngestionS3InputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/IngestionS3InputConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/IngestionS3InputConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/IngestionS3InputConfiguration) 