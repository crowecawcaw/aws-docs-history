# VpcOriginList

A list of CloudFront VPC origins.


## Contents





**IsTruncated** 


A flag that indicates whether more VPC origins remain to be listed. If
 your results were truncated, you can make a follow-up pagination request using the
 `Marker` request parameter to retrieve more VPC origins in the
 list.


Type: Boolean


Required: Yes




**Marker** 


The marker associated with the VPC origins list.


Type: String


Required: Yes




**MaxItems** 


The maximum number of items included in the list.


Type: Integer


Required: Yes




**Quantity** 


The number of VPC origins in the list.


Type: Integer


Required: Yes




**Items** 


The items of the VPC origins list.


Type: Array of [VpcOriginSummary](API_VpcOriginSummary.md "API_VpcOriginSummary.md") objects


Required: No




**NextMarker** 


The next marker associated with the VPC origins list.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/VpcOriginList "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/VpcOriginList")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/VpcOriginList "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/VpcOriginList")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/VpcOriginList "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/VpcOriginList")
