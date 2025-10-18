# PublicKeyList

A list of public keys that you can use with [signed URLs and signed cookies](../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md "../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md"), or with [field-level encryption](../../../AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.md "../../../AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.md").


## Contents





**MaxItems** 


The maximum number of public keys you want in the response.


Type: Integer


Required: Yes




**Quantity** 


The number of public keys in the list.


Type: Integer


Required: Yes




**Items** 


A list of public keys.


Type: Array of [PublicKeySummary](API_PublicKeySummary.md "API_PublicKeySummary.md") objects


Required: No




**NextMarker** 


If there are more elements to be listed, this element is present and contains the
 value that you can use for the `Marker` request parameter to continue listing
 your public keys where you left off.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/PublicKeyList "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/PublicKeyList")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/PublicKeyList "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/PublicKeyList")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/PublicKeyList "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/PublicKeyList")
