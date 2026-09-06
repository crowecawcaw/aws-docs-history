

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# InferenceInputNameConfiguration
<a name="API_InferenceInputNameConfiguration"></a>

Specifies configuration information for the input data for the inference, including timestamp format and delimiter. 

## Contents
<a name="API_InferenceInputNameConfiguration_Contents"></a>

 ** ComponentTimestampDelimiter **   <a name="LookoutForEquipment-Type-InferenceInputNameConfiguration-ComponentTimestampDelimiter"></a>
Indicates the delimiter character used between items in the data.   
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1.  
Pattern: `^(\-|\_|\s)?$`   
Required: No

 ** TimestampFormat **   <a name="LookoutForEquipment-Type-InferenceInputNameConfiguration-TimestampFormat"></a>
The format of the timestamp, whether Epoch time, or standard, with or without hyphens (-).   
Type: String  
Pattern: `^EPOCH|yyyy-MM-dd-HH-mm-ss|yyyyMMddHHmmss$`   
Required: No

## See Also
<a name="API_InferenceInputNameConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/InferenceInputNameConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/InferenceInputNameConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/InferenceInputNameConfiguration) 