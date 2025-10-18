# AdvancedEventSelector

Advanced event selectors let you create fine-grained selectors for AWS CloudTrail management, data, and network activity events. They help you control costs by logging only those
 events that are important to you. For more information about configuring advanced event selectors, see
 the [Logging data events](../userguide/logging-data-events-with-cloudtrail.md "../userguide/logging-data-events-with-cloudtrail.md"), [Logging network activity events](../userguide/logging-network-events-with-cloudtrail.md "../userguide/logging-network-events-with-cloudtrail.md"), and [Logging management events](../userguide/logging-management-events-with-cloudtrail.md "../userguide/logging-management-events-with-cloudtrail.md") topics in the *AWS CloudTrail User Guide*.

You cannot apply both event selectors and advanced event selectors to a trail.


**Supported CloudTrail event record fields for management events**



* `eventCategory` (required)
* `eventSource`
* `readOnly`
The following additional fields are available for event data stores:


* `eventName`
* `eventType`
* `sessionCredentialFromConsole`
* `userIdentity.arn`

**Supported CloudTrail event record fields for data events**



* `eventCategory` (required)
* `eventName`
* `eventSource`
* `eventType`
* `resources.ARN`
* `resources.type` (required)
* `readOnly`
* `sessionCredentialFromConsole`
* `userIdentity.arn`

**Supported CloudTrail event record fields for network activity events**



* `eventCategory` (required)
* `eventSource` (required)
* `eventName`
* `errorCode` - The only valid value for `errorCode` is `VpceAccessDenied`.
* `vpcEndpointId`
###### Note

For event data stores for CloudTrail Insights events, AWS Config configuration items, Audit Manager evidence, or events outside of AWS, the only supported field is
 `eventCategory`. 


## Contents





**FieldSelectors** 


Contains all selector statements in an advanced event selector.


Type: Array of [AdvancedFieldSelector](API_AdvancedFieldSelector.md "API_AdvancedFieldSelector.md") objects


Array Members: Minimum number of 1 item.


Required: Yes




**Name** 


An optional, descriptive name for an advanced event selector, such as "Log data events
 for only two S3 buckets".


Type: String


Length Constraints: Minimum length of 0. Maximum length of 1000.


Pattern: `.*`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/AdvancedEventSelector "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/AdvancedEventSelector")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/AdvancedEventSelector "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/AdvancedEventSelector")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/AdvancedEventSelector "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/AdvancedEventSelector")
