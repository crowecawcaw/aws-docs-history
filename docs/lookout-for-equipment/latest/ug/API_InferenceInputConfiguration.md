

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# InferenceInputConfiguration
<a name="API_InferenceInputConfiguration"></a>

Specifies configuration information for the input data for the inference, including Amazon S3 location of input data.. 

## Contents
<a name="API_InferenceInputConfiguration_Contents"></a>

 ** InferenceInputNameConfiguration **   <a name="LookoutForEquipment-Type-InferenceInputConfiguration-InferenceInputNameConfiguration"></a>
Specifies configuration information for the input data for the inference, including timestamp format and delimiter.   
Type: [InferenceInputNameConfiguration](API_InferenceInputNameConfiguration.md) object  
Required: No

 ** InputTimeZoneOffset **   <a name="LookoutForEquipment-Type-InferenceInputConfiguration-InputTimeZoneOffset"></a>
Indicates the difference between your time zone and Coordinated Universal Time (UTC).  
Type: String  
Pattern: `^(\+|\-)[0-9]{2}\:[0-9]{2}$`   
Required: No

 ** S3InputConfiguration **   <a name="LookoutForEquipment-Type-InferenceInputConfiguration-S3InputConfiguration"></a>
 Specifies configuration information for the input data for the inference, including Amazon S3 location of input data.  
Type: [InferenceS3InputConfiguration](API_InferenceS3InputConfiguration.md) object  
Required: No

## See Also
<a name="API_InferenceInputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/InferenceInputConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/InferenceInputConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/InferenceInputConfiguration) 