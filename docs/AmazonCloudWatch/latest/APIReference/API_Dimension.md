# Dimension

A dimension is a name/value pair that is part of the identity of a metric. Because
 dimensions are part of the unique identifier for a metric, whenever you add a unique
 name/value pair to one of your metrics, you are creating a new variation of that metric.
 For example, many Amazon EC2 metrics publish `InstanceId` as a
 dimension name, and the actual instance ID as the value for that dimension.

You can assign up to 30 dimensions to a metric.


## Contents





**Name** 


The name of the dimension. Dimension names must contain only ASCII characters, must
 include at least one non-whitespace character, and cannot start with a colon
 (`:`). ASCII control characters are not supported as part of dimension
 names.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: Yes




**Value** 


The value of the dimension. Dimension values must contain only ASCII characters and
 must include at least one non-whitespace character. ASCII control characters are not
 supported as part of dimension values.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/Dimension "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/Dimension")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/Dimension "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/Dimension")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/Dimension "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/Dimension")
