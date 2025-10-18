# ConnectionGroup

The connection group for your distribution tenants. When you first create a distribution tenant and you don't specify a connection group, CloudFront will automatically create a default connection group for you. When you create a new distribution tenant and don't specify a connection group, the default one will be associated with your distribution tenant.


## Contents





**AnycastIpListId** 


The ID of the Anycast static IP list.


Type: String


Required: No




**Arn** 


The Amazon Resource Name (ARN) of the connection group.


Type: String


Required: No




**CreatedTime** 


The date and time when the connection group was created.


Type: Timestamp


Required: No




**Enabled** 


Whether the connection group is enabled.


Type: Boolean


Required: No




**Id** 


The ID of the connection group.


Type: String


Required: No




**Ipv6Enabled** 


IPv6 is enabled for the connection group.


Type: Boolean


Required: No




**IsDefault** 


Whether the connection group is the default connection group for the distribution tenants.


Type: Boolean


Required: No




**LastModifiedTime** 


The date and time when the connection group was updated.


Type: Timestamp


Required: No




**Name** 


The name of the connection group.


Type: String


Required: No




**RoutingEndpoint** 


The routing endpoint (also known as the DNS name) that is assigned to the connection group, such as d111111abcdef8.cloudfront.net.


Type: String


Required: No




**Status** 


The status of the connection group.


Type: String


Required: No




**Tags** 


A complex type that contains zero or more `Tag` elements.


Type: [Tags](API_Tags.md "API_Tags.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ConnectionGroup "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ConnectionGroup")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ConnectionGroup "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ConnectionGroup")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ConnectionGroup "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ConnectionGroup")
