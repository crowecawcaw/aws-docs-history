# FieldLevelEncryptionList

List of field-level encryption configurations.


## Contents





**MaxItems** 


The maximum number of elements you want in the response body.


Type: Integer


Required: Yes




**Quantity** 


The number of field-level encryption items.


Type: Integer


Required: Yes




**Items** 


An array of field-level encryption items.


Type: Array of [FieldLevelEncryptionSummary](API_FieldLevelEncryptionSummary.md "API_FieldLevelEncryptionSummary.md") objects


Required: No




**NextMarker** 


If there are more elements to be listed, this element is present and contains the
 value that you can use for the `Marker` request parameter to continue listing
 your configurations where you left off.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/FieldLevelEncryptionList "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/FieldLevelEncryptionList")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/FieldLevelEncryptionList "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/FieldLevelEncryptionList")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/FieldLevelEncryptionList "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/FieldLevelEncryptionList")
