# Attachment

Describes a core network attachment.


## Contents





**AttachmentId** 


The ID of the attachment.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `^attachment-([0-9a-f]{8,17})$`



Required: No




**AttachmentPolicyRuleNumber** 


The policy rule number associated with the attachment.


Type: Integer


Required: No




**AttachmentType** 


The type of attachment.


Type: String


Valid Values: `CONNECT | SITE_TO_SITE_VPN | VPC | DIRECT_CONNECT_GATEWAY | TRANSIT_GATEWAY_ROUTE_TABLE`



Required: No




**CoreNetworkArn** 


The ARN of a core network.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 500.


Pattern: `[\s\S]*`



Required: No




**CoreNetworkId** 


The ID of a core network.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `^core-network-([0-9a-f]{8,17})$`



Required: No




**CreatedAt** 


The timestamp when the attachment was created.


Type: Timestamp


Required: No




**EdgeLocation** 


The Region where the edge is located. This is returned for all attachment types except a Direct Connect gateway attachment, which instead returns `EdgeLocations`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 63.


Pattern: `[\s\S]*`



Required: No




**EdgeLocations** 


The edge locations that the Direct Connect gateway is associated with. This is returned only for Direct Connect gateway attachments. All other attachment types retrun `EdgeLocation`.


Type: Array of strings


Length Constraints: Minimum length of 1. Maximum length of 63.


Pattern: `[\s\S]*`



Required: No




**LastModificationErrors** 


Describes the error associated with the attachment request.


Type: Array of [AttachmentError](API_AttachmentError.md "API_AttachmentError.md") objects


Array Members: Minimum number of 0 items. Maximum number of 20 items.


Required: No




**NetworkFunctionGroupName** 


The name of the network function group.


Type: String


Pattern: `[\s\S]*`



Required: No




**OwnerAccountId** 


The ID of the attachment account owner.


Type: String


Length Constraints: Fixed length of 12.


Pattern: `[\s\S]*`



Required: No




**ProposedNetworkFunctionGroupChange** 


Describes a proposed change to a network function group associated with the attachment.


Type: [ProposedNetworkFunctionGroupChange](API_ProposedNetworkFunctionGroupChange.md "API_ProposedNetworkFunctionGroupChange.md") object


Required: No




**ProposedSegmentChange** 


The attachment to move from one segment to another.


Type: [ProposedSegmentChange](API_ProposedSegmentChange.md "API_ProposedSegmentChange.md") object


Required: No




**ResourceArn** 


The attachment resource ARN.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 1500.


Pattern: `[\s\S]*`



Required: No




**SegmentName** 


The name of the segment attachment.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**State** 


The state of the attachment.


Type: String


Valid Values: `REJECTED | PENDING_ATTACHMENT_ACCEPTANCE | CREATING | FAILED | AVAILABLE | UPDATING | PENDING_NETWORK_UPDATE | PENDING_TAG_ACCEPTANCE | DELETING`



Required: No




**Tags** 


The tags associated with the attachment.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Required: No




**UpdatedAt** 


The timestamp when the attachment was last updated.


Type: Timestamp


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/Attachment "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/Attachment")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/Attachment "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/Attachment")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/Attachment "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/Attachment")
