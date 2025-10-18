# DistributionIdList

A list of distribution IDs.


## Contents





**IsTruncated** 


A flag that indicates whether more distribution IDs remain to be listed. If your
 results were truncated, you can make a subsequent request using the `Marker`
 request field to retrieve more distribution IDs in the list.


Type: Boolean


Required: Yes




**Marker** 


The value provided in the `Marker` request field.


Type: String


Required: Yes




**MaxItems** 


The maximum number of distribution IDs requested.


Type: Integer


Required: Yes




**Quantity** 


The total number of distribution IDs returned in the response.


Type: Integer


Required: Yes




**Items** 


Contains the distribution IDs in the list.


Type: Array of strings


Required: No




**NextMarker** 


Contains the value that you should use in the `Marker` field of a
 subsequent request to continue listing distribution IDs where you left off.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DistributionIdList "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DistributionIdList")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DistributionIdList "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DistributionIdList")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DistributionIdList "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DistributionIdList")
