# RecordExpiration


 The journal table record expiration settings for a journal table in an S3 Metadata configuration.
 


## Contents





**Expiration** 



 Specifies whether journal table record expiration is enabled or disabled.
 


Type: String


Valid Values: `ENABLED | DISABLED`



Required: Yes




**Days** 



 If you enable journal table record expiration, you can set the number of days to retain your 
 journal table records. Journal table records must be retained for a minimum of 7 days. To set 
 this value, specify any whole number from `7` to `2147483647`. For example, 
 to retain your journal table records for one year, set this value to `365`.
 


Type: Integer


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/RecordExpiration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/RecordExpiration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/RecordExpiration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/RecordExpiration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/RecordExpiration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/RecordExpiration")
