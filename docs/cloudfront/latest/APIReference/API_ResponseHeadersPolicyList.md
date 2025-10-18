# ResponseHeadersPolicyList

A list of response headers policies.


## Contents





**MaxItems** 


The maximum number of response headers policies requested.


Type: Integer


Required: Yes




**Quantity** 


The number of response headers policies returned.


Type: Integer


Required: Yes




**Items** 


The response headers policies in the list.


Type: Array of [ResponseHeadersPolicySummary](API_ResponseHeadersPolicySummary.md "API_ResponseHeadersPolicySummary.md") objects


Required: No




**NextMarker** 


If there are more items in the list than are in this response, this element is
 present. It contains the value that you should use in the `Marker` field of a
 subsequent request to continue listing response headers policies where you left
 off.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyList "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyList")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyList "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyList")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyList "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyList")
