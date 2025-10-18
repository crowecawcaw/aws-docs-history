# ProposedSegmentChange

Describes a proposed segment change. In some cases, the segment change must first be evaluated and accepted. 


## Contents





**AttachmentPolicyRuleNumber** 


The rule number in the policy document that applies to this change.


Type: Integer


Required: No




**SegmentName** 


The name of the segment to change.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**Tags** 


The list of key-value tags that changed for the segment.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ProposedSegmentChange "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ProposedSegmentChange")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ProposedSegmentChange "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ProposedSegmentChange")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ProposedSegmentChange "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ProposedSegmentChange")
