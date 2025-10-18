# OriginAccessControlList

A list of CloudFront origin access controls.


## Contents





**IsTruncated** 


If there are more items in the list than are in this response, this value is
 `true`.


Type: Boolean


Required: Yes




**Marker** 


The value of the `Marker` field that was provided in the request.


Type: String


Required: Yes




**MaxItems** 


The maximum number of origin access controls requested.


Type: Integer


Required: Yes




**Quantity** 


The number of origin access controls returned in the response.


Type: Integer


Required: Yes




**Items** 


Contains the origin access controls in the list.


Type: Array of [OriginAccessControlSummary](API_OriginAccessControlSummary.md "API_OriginAccessControlSummary.md") objects


Required: No




**NextMarker** 


If there are more items in the list than are in this response, this element is
 present. It contains the value to use in the `Marker` field of another
 request to continue listing origin access controls.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/OriginAccessControlList "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/OriginAccessControlList")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/OriginAccessControlList "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/OriginAccessControlList")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/OriginAccessControlList "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/OriginAccessControlList")
