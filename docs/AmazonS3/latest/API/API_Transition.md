# Transition

Specifies when an object transitions to a specified storage class. For more information about Amazon S3
 lifecycle configuration rules, see [Transitioning Objects Using
 Amazon S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/dev/lifecycle-transition-general-considerations.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/lifecycle-transition-general-considerations.html") in the *Amazon S3 User Guide*.


## Contents





**Date** 


Indicates when objects are transitioned to the specified storage class. The date value must be in
 ISO 8601 format. The time is always midnight UTC.


Type: Timestamp


Required: No




**Days** 


Indicates the number of days after creation when objects are transitioned to the specified storage
 class. If the specified storage class is `INTELLIGENT_TIERING`, `GLACIER_IR`,
 `GLACIER`, or `DEEP_ARCHIVE`, valid values are `0` or positive
 integers. If the specified storage class is `STANDARD_IA` or `ONEZONE_IA`, valid
 values are positive integers greater than `30`. Be aware that some storage classes have a
 minimum storage duration and that you're charged for transitioning objects before their minimum storage
 duration. For more information, see  [Constraints and considerations for transitions](../userguide/lifecycle-transition-general-considerations.md#lifecycle-configuration-constraints "../userguide/lifecycle-transition-general-considerations.md#lifecycle-configuration-constraints") in the *Amazon S3 User
 Guide*.


Type: Integer


Required: No




**StorageClass** 


The storage class to which you want the object to transition.


Type: String


Valid Values: `GLACIER | STANDARD_IA | ONEZONE_IA | INTELLIGENT_TIERING | DEEP_ARCHIVE | GLACIER_IR`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Transition "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Transition")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Transition "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Transition")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Transition "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Transition")
