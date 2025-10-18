# AnycastIpListCollection

The Anycast static IP list collection.


## Contents





**IsTruncated** 


If there are more items in the list collection than are in this response, this value is
 `true`.


Type: Boolean


Required: Yes




**Marker** 


Use this field when paginating results to indicate where to begin in your list. The response includes items in the list that occur
 after the marker. To get the next page of the list, set this field's value to the value
 of `NextMarker` from the current page's response.


Type: String


Required: Yes




**MaxItems** 


The maximum number of Anycast static IP list collections that you want returned in the
 response.


Type: Integer


Required: Yes




**Quantity** 


The quantity of Anycast static IP lists in the collection.


Type: Integer


Required: Yes




**Items** 


Items in the Anycast static IP list collection. Each item is of the [AnycastIpListSummary](API_AnycastIpListSummary.md "API_AnycastIpListSummary.md") structure type.


Type: Array of [AnycastIpListSummary](API_AnycastIpListSummary.md "API_AnycastIpListSummary.md") objects


Required: No




**NextMarker** 


Indicates the next page of the Anycast static IP list collection. To get the next page of the
 list, use this value in the `Marker` field of your request.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/AnycastIpListCollection "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/AnycastIpListCollection")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/AnycastIpListCollection "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/AnycastIpListCollection")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/AnycastIpListCollection "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/AnycastIpListCollection")
