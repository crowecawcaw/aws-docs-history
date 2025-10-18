# OriginGroup

An origin group includes two origins (a primary origin and a secondary origin to failover
 to) and a failover criteria that you specify. You create an origin group to support
 origin failover in CloudFront. When you create or update a distribution, you can specify the
 origin group instead of a single origin, and CloudFront will failover from the primary origin
 to the secondary origin under the failover conditions that you've chosen.

Optionally, you can choose selection criteria for your origin group to specify how your origins are selected when your distribution routes viewer requests.


## Contents





**FailoverCriteria** 


A complex type that contains information about the failover criteria for an origin
 group.


Type: [OriginGroupFailoverCriteria](API_OriginGroupFailoverCriteria.md "API_OriginGroupFailoverCriteria.md") object


Required: Yes




**Id** 


The origin group's ID.


Type: String


Required: Yes




**Members** 


A complex type that contains information about the origins in an origin group.


Type: [OriginGroupMembers](API_OriginGroupMembers.md "API_OriginGroupMembers.md") object


Required: Yes




**SelectionCriteria** 


The selection criteria for the origin group. For more information, see [Create an origin group](../../../AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.md#concept_origin_groups.creating "../../../AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.md#concept_origin_groups.creating") in the *Amazon CloudFront
 Developer Guide*.


Type: String


Valid Values: `default | media-quality-based`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/OriginGroup "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/OriginGroup")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/OriginGroup "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/OriginGroup")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/OriginGroup "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/OriginGroup")
