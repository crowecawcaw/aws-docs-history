# ConnectionGroupSummary

A summary that contains details about your connection groups.


## Contents





**Arn** 


The Amazon Resource Name (ARN) of the connection group.


Type: String


Required: Yes




**CreatedTime** 


The date and time when the connection group was created.


Type: Timestamp


Required: Yes




**ETag** 


The current version of the connection group.


Type: String


Required: Yes




**Id** 


The ID of the connection group.


Type: String


Required: Yes




**LastModifiedTime** 


The date and time when the connection group was updated.


Type: Timestamp


Required: Yes




**Name** 


The name of the connection group.


Type: String


Required: Yes




**RoutingEndpoint** 


The routing endpoint (also known as the DNS name) that is assigned to the connection group, such as d111111abcdef8.cloudfront.net.


Type: String


Required: Yes




**AnycastIpListId** 


The ID of the Anycast static IP list.


Type: String


Required: No




**Enabled** 


Whether the connection group is enabled


Type: Boolean


Required: No




**IsDefault** 


Whether the connection group is the default connection group for the distribution tenants.


Type: Boolean


Required: No




**Status** 


The status of the connection group.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ConnectionGroupSummary "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ConnectionGroupSummary")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ConnectionGroupSummary "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ConnectionGroupSummary")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ConnectionGroupSummary "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ConnectionGroupSummary")
