# Invalidation

An invalidation.


## Contents





**CreateTime** 


The date and time the invalidation request was first made.


Type: Timestamp


Required: Yes




**Id** 


The identifier for the invalidation request. For example:
 `IDFDVBD632BHDS5`.


Type: String


Required: Yes




**InvalidationBatch** 


The current invalidation information for the batch request.


Type: [InvalidationBatch](API_InvalidationBatch.md "API_InvalidationBatch.md") object


Required: Yes




**Status** 


The status of the invalidation request. When the invalidation batch is finished, the
 status is `Completed`.


Type: String


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/Invalidation "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/Invalidation")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/Invalidation "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/Invalidation")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/Invalidation "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/Invalidation")
