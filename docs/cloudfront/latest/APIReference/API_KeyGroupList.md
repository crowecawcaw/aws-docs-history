# KeyGroupList

A list of key groups.


## Contents





**MaxItems** 


The maximum number of key groups requested.


Type: Integer


Required: Yes




**Quantity** 


The number of key groups returned in the response.


Type: Integer


Required: Yes




**Items** 


A list of key groups.


Type: Array of [KeyGroupSummary](API_KeyGroupSummary.md "API_KeyGroupSummary.md") objects


Required: No




**NextMarker** 


If there are more items in the list than are in this response, this element is
 present. It contains the value that you should use in the `Marker` field of a
 subsequent request to continue listing key groups.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/KeyGroupList "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/KeyGroupList")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/KeyGroupList "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/KeyGroupList")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/KeyGroupList "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/KeyGroupList")
