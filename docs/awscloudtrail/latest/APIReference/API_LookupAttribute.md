# LookupAttribute

Specifies an attribute and value that filter the events returned.


## Contents





**AttributeKey** 


Specifies an attribute on which to filter the events returned.


Type: String


Valid Values: `EventId | EventName | ReadOnly | Username | ResourceType | ResourceName | EventSource | AccessKeyId`



Required: Yes




**AttributeValue** 


Specifies a value for the specified `AttributeKey`.


The maximum length for the `AttributeValue` is 2000 characters. The
 following characters ('`_`', '', '`,`',
 '`\\n`') count as two characters towards the 2000 character limit.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2000.


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/LookupAttribute "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/LookupAttribute")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/LookupAttribute "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/LookupAttribute")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/LookupAttribute "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/LookupAttribute")
