# OriginGroupFailoverCriteria

A complex data type that includes information about the failover criteria for an
 origin group, including the status codes for which CloudFront will failover from the
 primary origin to the second origin.


## Contents





**StatusCodes** 


The status codes that, when returned from the primary origin, will trigger CloudFront to failover to the second origin.


Type: [StatusCodes](API_StatusCodes.md "API_StatusCodes.md") object


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/OriginGroupFailoverCriteria "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/OriginGroupFailoverCriteria")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/OriginGroupFailoverCriteria "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/OriginGroupFailoverCriteria")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/OriginGroupFailoverCriteria "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/OriginGroupFailoverCriteria")
