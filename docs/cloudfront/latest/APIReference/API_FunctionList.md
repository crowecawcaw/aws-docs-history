# FunctionList

A list of CloudFront functions.


## Contents





**MaxItems** 


The maximum number of functions requested.


Type: Integer


Required: Yes




**Quantity** 


The number of functions returned in the response.


Type: Integer


Required: Yes




**Items** 


Contains the functions in the list.


Type: Array of [FunctionSummary](API_FunctionSummary.md "API_FunctionSummary.md") objects


Required: No




**NextMarker** 


If there are more items in the list than are in this response, this element is
 present. It contains the value that you should use in the `Marker` field of a
 subsequent request to continue listing functions where you left off.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/FunctionList "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/FunctionList")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/FunctionList "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/FunctionList")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/FunctionList "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/FunctionList")
