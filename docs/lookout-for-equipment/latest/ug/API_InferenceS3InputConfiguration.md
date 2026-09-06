

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# InferenceS3InputConfiguration
<a name="API_InferenceS3InputConfiguration"></a>

 Specifies configuration information for the input data for the inference, including input data S3 location. 

## Contents
<a name="API_InferenceS3InputConfiguration_Contents"></a>

 ** Bucket **   <a name="LookoutForEquipment-Type-InferenceS3InputConfiguration-Bucket"></a>
The bucket containing the input dataset for the inference.   
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 63.  
Pattern: `^[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]$`   
Required: Yes

 ** Prefix **   <a name="LookoutForEquipment-Type-InferenceS3InputConfiguration-Prefix"></a>
The prefix for the S3 bucket used for the input data for the inference.   
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Pattern: `(^$)|([\u0009\u000A\u000D\u0020-\u00FF]{1,1023}/$)`   
Required: No

## See Also
<a name="API_InferenceS3InputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/InferenceS3InputConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/InferenceS3InputConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/InferenceS3InputConfiguration) 