# DSSEKMSFilter

A filter that returns objects that are encrypted by dual-layer server-side encryption with AWS Key Management
 Service (AWS KMS) keys (DSSE-KMS). You can further refine your filtering by optionally providing a KMS Key ARN 
 to create an object list of DSSE-KMS objects with that specific KMS Key ARN.


## Contents





**KmsKeyArn** 


The Amazon Resource Name (ARN) of the customer managed KMS key to use for the filter 
 to return objects that are encrypted by the specified key. For best performance, 
 we recommend using the `KMSKeyArn` filter in conjunction with other object metadata filters, like `MatchAnyPrefix`, `CreatedAfter`, or 
 `MatchAnyStorageClass`.


###### Note

You must provide the full KMS Key ARN. You can't use an alias name or alias ARN. 
 For more information, see [AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN") in the *AWS Key Management Service Developer Guide*.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2000.


Pattern: `arn:aws[a-zA-Z0-9-]*:kms:[a-z0-9-]+:[0-9]{12}:key/[a-zA-Z0-9-]+`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/DSSEKMSFilter "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/DSSEKMSFilter")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/DSSEKMSFilter "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/DSSEKMSFilter")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/DSSEKMSFilter "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/DSSEKMSFilter")
