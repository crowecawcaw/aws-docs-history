Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# TypedAttributeValueRange

A range of attribute values. For more information, see [Range Filters](../developerguide/directory_objects_range_filters.md "../developerguide/directory_objects_range_filters.md").


## Contents





**EndMode** 


The inclusive or exclusive range end.


Type: String


Valid Values: `FIRST | LAST | LAST_BEFORE_MISSING_VALUES | INCLUSIVE | EXCLUSIVE`



Required: Yes




**StartMode** 


The inclusive or exclusive range start.


Type: String


Valid Values: `FIRST | LAST | LAST_BEFORE_MISSING_VALUES | INCLUSIVE | EXCLUSIVE`



Required: Yes




**EndValue** 


The attribute value to terminate the range at.


Type: [TypedAttributeValue](API_TypedAttributeValue.md "API_TypedAttributeValue.md") object


Required: No




**StartValue** 


The value to start the range at.


Type: [TypedAttributeValue](API_TypedAttributeValue.md "API_TypedAttributeValue.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/TypedAttributeValueRange "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/TypedAttributeValueRange")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/TypedAttributeValueRange "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/TypedAttributeValueRange")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/TypedAttributeValueRange "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/TypedAttributeValueRange")
