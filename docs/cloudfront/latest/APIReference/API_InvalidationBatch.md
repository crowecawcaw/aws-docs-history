# InvalidationBatch

An invalidation batch.


## Contents





**CallerReference** 


A value that you specify to uniquely identify an invalidation request. CloudFront uses the
 value to prevent you from accidentally resubmitting an identical request. Whenever you
 create a new invalidation request, you must specify a new value for
 `CallerReference` and change other values in the request as applicable.
 One way to ensure that the value of `CallerReference` is unique is to use a
 `timestamp`, for example, `20120301090000`.


If you make a second invalidation request with the same value for
 `CallerReference`, and if the rest of the request is the same, CloudFront
 doesn't create a new invalidation request. Instead, CloudFront returns information about the
 invalidation request that you previously created with the same
 `CallerReference`.


If `CallerReference` is a value you already sent in a previous invalidation
 batch request but the content of any `Path` is different from the original
 request, CloudFront returns an `InvalidationBatchAlreadyExists` error.


Type: String


Required: Yes




**Paths** 


A complex type that contains information about the objects that you want to
 invalidate. For more information, see [Specifying the Objects to Invalidate](../../../AmazonCloudFront/latest/DeveloperGuide/Invalidation.md#invalidation-specifying-objects "../../../AmazonCloudFront/latest/DeveloperGuide/Invalidation.md#invalidation-specifying-objects") in the
 *Amazon CloudFront Developer Guide*.


Type: [Paths](API_Paths.md "API_Paths.md") object


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/InvalidationBatch "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/InvalidationBatch")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/InvalidationBatch "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/InvalidationBatch")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/InvalidationBatch "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/InvalidationBatch")
