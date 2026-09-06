

# Actions, resources, and condition keys for AWS RTB Fabric
<a name="list_rtbfabric"></a>

AWS RTB Fabric (service prefix: `rtbfabric`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/rtb-fabric/latest/api/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/security.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/rtbfabric/rtbfabric.json) for this service.

**Topics**
+ [API operations defined by AWS RTB Fabric](#list_rtbfabric-operations)
+ [Actions defined by AWS RTB Fabric](#list_rtbfabric-actions-as-permissions)
+ [Resource types defined by AWS RTB Fabric](#list_rtbfabric-resources-for-iam-policies)
+ [Condition keys for AWS RTB Fabric](#list_rtbfabric-policy-keys)

## API operations defined by AWS RTB Fabric
<a name="list_rtbfabric-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_rtbfabric-actions-as-permissions).




- **   AcceptLink  **
  - **IAM action:**  [rtbfabric:AcceptLink](#list_rtbfabric-action-AcceptLink) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateCertificate  **
  - **IAM action:**  [rtbfabric:AssociateCertificate](#list_rtbfabric-action-AssociateCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateInboundExternalLink  **
  - **IAM action:**  [rtbfabric:CreateInboundExternalLink](#list_rtbfabric-action-CreateInboundExternalLink)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rtbfabric:TagResource](#list_rtbfabric-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateLink  **
  - **IAM action:**  [rtbfabric:CreateLink](#list_rtbfabric-action-CreateLink)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rtbfabric:TagResource](#list_rtbfabric-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateLinkRoutingRule  **
  - **IAM action:**  [rtbfabric:CreateLinkRoutingRule](#list_rtbfabric-action-CreateLinkRoutingRule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rtbfabric:TagResource](#list_rtbfabric-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateOutboundExternalLink  **
  - **IAM action:**  [rtbfabric:CreateOutboundExternalLink](#list_rtbfabric-action-CreateOutboundExternalLink)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rtbfabric:TagResource](#list_rtbfabric-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRequesterGateway  **
  - **IAM action:**  [rtbfabric:CreateRequesterGateway](#list_rtbfabric-action-CreateRequesterGateway)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rtbfabric:TagResource](#list_rtbfabric-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateResponderGateway  **
  - **IAM action:**  [rtbfabric:CreateResponderGateway](#list_rtbfabric-action-CreateResponderGateway)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rtbfabric:TagResource](#list_rtbfabric-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteInboundExternalLink  **
  - **IAM action:**  [rtbfabric:DeleteInboundExternalLink](#list_rtbfabric-action-DeleteInboundExternalLink) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLink  **
  - **IAM action:**  [rtbfabric:DeleteLink](#list_rtbfabric-action-DeleteLink) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLinkRoutingRule  **
  - **IAM action:**  [rtbfabric:DeleteLinkRoutingRule](#list_rtbfabric-action-DeleteLinkRoutingRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteOutboundExternalLink  **
  - **IAM action:**  [rtbfabric:DeleteOutboundExternalLink](#list_rtbfabric-action-DeleteOutboundExternalLink) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRequesterGateway  **
  - **IAM action:**  [rtbfabric:DeleteRequesterGateway](#list_rtbfabric-action-DeleteRequesterGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResponderGateway  **
  - **IAM action:**  [rtbfabric:DeleteResponderGateway](#list_rtbfabric-action-DeleteResponderGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateCertificate  **
  - **IAM action:**  [rtbfabric:DisassociateCertificate](#list_rtbfabric-action-DisassociateCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetCertificateAssociation  **
  - **IAM action:**  [rtbfabric:GetCertificateAssociation](#list_rtbfabric-action-GetCertificateAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInboundExternalLink  **
  - **IAM action:**  [rtbfabric:GetInboundExternalLink](#list_rtbfabric-action-GetInboundExternalLink) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLink  **
  - **IAM action:**  [rtbfabric:GetLink](#list_rtbfabric-action-GetLink) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLinkRoutingRule  **
  - **IAM action:**  [rtbfabric:GetLinkRoutingRule](#list_rtbfabric-action-GetLinkRoutingRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOutboundExternalLink  **
  - **IAM action:**  [rtbfabric:GetOutboundExternalLink](#list_rtbfabric-action-GetOutboundExternalLink) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRequesterGateway  **
  - **IAM action:**  [rtbfabric:GetRequesterGateway](#list_rtbfabric-action-GetRequesterGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResponderGateway  **
  - **IAM action:**  [rtbfabric:GetResponderGateway](#list_rtbfabric-action-GetResponderGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListCertificateAssociations  **
  - **IAM action:**  [rtbfabric:ListCertificateAssociations](#list_rtbfabric-action-ListCertificateAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLinkRoutingRules  **
  - **IAM action:**  [rtbfabric:ListLinkRoutingRules](#list_rtbfabric-action-ListLinkRoutingRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLinks  **
  - **IAM action:**  [rtbfabric:ListLinks](#list_rtbfabric-action-ListLinks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRequesterGateways  **
  - **IAM action:**  [rtbfabric:ListRequesterGateways](#list_rtbfabric-action-ListRequesterGateways) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResponderGateways  **
  - **IAM action:**  [rtbfabric:ListResponderGateways](#list_rtbfabric-action-ListResponderGateways) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [rtbfabric:ListTagsForResource](#list_rtbfabric-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   RejectLink  **
  - **IAM action:**  [rtbfabric:RejectLink](#list_rtbfabric-action-RejectLink) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [rtbfabric:TagResource](#list_rtbfabric-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [rtbfabric:UntagResource](#list_rtbfabric-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateLink  **
  - **IAM action:**  [rtbfabric:UpdateLink](#list_rtbfabric-action-UpdateLink) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLinkModuleFlow  **
  - **IAM action:**  [rtbfabric:UpdateLinkModuleFlow](#list_rtbfabric-action-UpdateLinkModuleFlow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLinkRoutingRule  **
  - **IAM action:**  [rtbfabric:UpdateLinkRoutingRule](#list_rtbfabric-action-UpdateLinkRoutingRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRequesterGateway  **
  - **IAM action:**  [rtbfabric:UpdateRequesterGateway](#list_rtbfabric-action-UpdateRequesterGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateResponderGateway  **
  - **IAM action:**  [rtbfabric:UpdateResponderGateway](#list_rtbfabric-action-UpdateResponderGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS RTB Fabric
<a name="list_rtbfabric-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptLink](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_AcceptLink.html)  **
  - **Description:** Grants permission to accept a link invitation from another Gateway
  - **Resource types (\*required):** [Link\*](#list_rtbfabric-resource-Link)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:LinkLinkId](#list_rtbfabric-rtbfabric_LinkLinkId)<br />[rtbfabric:RequesterGatewayGatewayId](#list_rtbfabric-rtbfabric_RequesterGatewayGatewayId)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Access level:** Write

- **   [AssociateCertificate](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_AssociateCertificate.html)  **
  - **Description:** Grants permission to associate an ACM certificate with a responder gateway
  - **Resource types (\*required):** [ResponderGateway\*](#list_rtbfabric-resource-ResponderGateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Access level:** Write

- **   [CreateInboundExternalLink](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_CreateInboundExternalLink.html)  **
  - **Description:** Grants permission to create an inbound external link for a responder gateway
  - **Resource types (\*required):** [ResponderGateway\*](#list_rtbfabric-resource-ResponderGateway)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rtbfabric-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rtbfabric-aws_TagKeys)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Access level:** Write

- **   [CreateLink](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_CreateLink.html)  **
  - **Description:** Grants permission to create a new link between RTB applications
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rtbfabric-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_rtbfabric-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLinkRoutingRule](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_CreateLinkRoutingRule.html)  **
  - **Description:** Grants permission to create a routing rule for a link
  - **Resource types (\*required):** [Link\*](#list_rtbfabric-resource-Link)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rtbfabric-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rtbfabric-aws_TagKeys)<br />[rtbfabric:LinkLinkId](#list_rtbfabric-rtbfabric_LinkLinkId)<br />[rtbfabric:RequesterGatewayGatewayId](#list_rtbfabric-rtbfabric_RequesterGatewayGatewayId)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Access level:** Write

- **   [CreateOutboundExternalLink](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_CreateOutboundExternalLink.html)  **
  - **Description:** Grants permission to create an outbound external link for a requester gateway to connect to external public responder endpoints
  - **Resource types (\*required):** [RequesterGateway\*](#list_rtbfabric-resource-RequesterGateway)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rtbfabric-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rtbfabric-aws_TagKeys)<br />[rtbfabric:RequesterGatewayGatewayId](#list_rtbfabric-rtbfabric_RequesterGatewayGatewayId)
  - **Access level:** Write

- **   [CreateRequesterGateway](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_CreateRequesterGateway.html)  **
  - **Description:** Grants permission to create a requester gateway
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rtbfabric-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_rtbfabric-aws_TagKeys)
  - **Access level:** Write

- **   [CreateResponderGateway](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_CreateResponderGateway.html)  **
  - **Description:** Grants permission to create a responder gateway
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rtbfabric-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_rtbfabric-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteInboundExternalLink](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_DeleteInboundExternalLink.html)  **
  - **Description:** Grants permission to delete an inbound external link
  - **Resource types (\*required):** [InboundExternalLink\*](#list_rtbfabric-resource-InboundExternalLink) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:InboundExternalLinkLinkId](#list_rtbfabric-rtbfabric_InboundExternalLinkLinkId)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Resource types (\*required):** [ResponderGateway\*](#list_rtbfabric-resource-ResponderGateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Access level:** Write

- **   [DeleteLink](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_DeleteLink.html)  **
  - **Description:** Grants permission to delete a link between RTB applications
  - **Resource types (\*required):** [Link\*](#list_rtbfabric-resource-Link)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:LinkLinkId](#list_rtbfabric-rtbfabric_LinkLinkId)<br />[rtbfabric:RequesterGatewayGatewayId](#list_rtbfabric-rtbfabric_RequesterGatewayGatewayId)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Access level:** Write

- **   [DeleteLinkRoutingRule](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_DeleteLinkRoutingRule.html)  **
  - **Description:** Grants permission to delete a routing rule from a link
  - **Resource types (\*required):** [Link\*](#list_rtbfabric-resource-Link) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:LinkLinkId](#list_rtbfabric-rtbfabric_LinkLinkId)<br />[rtbfabric:RequesterGatewayGatewayId](#list_rtbfabric-rtbfabric_RequesterGatewayGatewayId)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Resource types (\*required):** [LinkRoutingRule\*](#list_rtbfabric-resource-LinkRoutingRule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:LinkLinkId](#list_rtbfabric-rtbfabric_LinkLinkId)<br />[rtbfabric:LinkRoutingRuleRuleId](#list_rtbfabric-rtbfabric_LinkRoutingRuleRuleId)
  - **Access level:** Write

- **   [DeleteOutboundExternalLink](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_DeleteOutboundExternalLink.html)  **
  - **Description:** Grants permission to delete an outbound external link
  - **Resource types (\*required):** [OutboundExternalLink\*](#list_rtbfabric-resource-OutboundExternalLink) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:OutboundExternalLinkLinkId](#list_rtbfabric-rtbfabric_OutboundExternalLinkLinkId)<br />[rtbfabric:RequesterGatewayGatewayId](#list_rtbfabric-rtbfabric_RequesterGatewayGatewayId)
  - **Resource types (\*required):** [RequesterGateway\*](#list_rtbfabric-resource-RequesterGateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:RequesterGatewayGatewayId](#list_rtbfabric-rtbfabric_RequesterGatewayGatewayId)
  - **Access level:** Write

- **   [DeleteRequesterGateway](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_DeleteRequesterGateway.html)  **
  - **Description:** Grants permission to delete a requester gateway
  - **Resource types (\*required):** [RequesterGateway\*](#list_rtbfabric-resource-RequesterGateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:RequesterGatewayGatewayId](#list_rtbfabric-rtbfabric_RequesterGatewayGatewayId)
  - **Access level:** Write

- **   [DeleteResponderGateway](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_DeleteResponderGateway.html)  **
  - **Description:** Grants permission to delete a responder gateway
  - **Resource types (\*required):** [ResponderGateway\*](#list_rtbfabric-resource-ResponderGateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Access level:** Write

- **   [DisassociateCertificate](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_DisassociateCertificate.html)  **
  - **Description:** Grants permission to remove a certificate association from a responder gateway
  - **Resource types (\*required):** [ResponderGateway\*](#list_rtbfabric-resource-ResponderGateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Access level:** Write

- **   [GetCertificateAssociation](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_GetCertificateAssociation.html)  **
  - **Description:** Grants permission to retrieve details of a certificate association with a responder gateway
  - **Resource types (\*required):** [ResponderGateway\*](#list_rtbfabric-resource-ResponderGateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Access level:** Read

- **   [GetInboundExternalLink](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_GetInboundExternalLink.html)  **
  - **Description:** Grants permission to retrieve information about an inbound external link
  - **Resource types (\*required):** [InboundExternalLink\*](#list_rtbfabric-resource-InboundExternalLink) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:InboundExternalLinkLinkId](#list_rtbfabric-rtbfabric_InboundExternalLinkLinkId)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Resource types (\*required):** [ResponderGateway\*](#list_rtbfabric-resource-ResponderGateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Access level:** Read

- **   [GetLink](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_GetLink.html)  **
  - **Description:** Grants permission to retrieve information about a link between RTB applications
  - **Resource types (\*required):** [Link\*](#list_rtbfabric-resource-Link)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:LinkLinkId](#list_rtbfabric-rtbfabric_LinkLinkId)<br />[rtbfabric:RequesterGatewayGatewayId](#list_rtbfabric-rtbfabric_RequesterGatewayGatewayId)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Access level:** Read

- **   [GetLinkRoutingRule](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_GetLinkRoutingRule.html)  **
  - **Description:** Grants permission to retrieve information about a routing rule for a link
  - **Resource types (\*required):** [Link\*](#list_rtbfabric-resource-Link) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:LinkLinkId](#list_rtbfabric-rtbfabric_LinkLinkId)<br />[rtbfabric:RequesterGatewayGatewayId](#list_rtbfabric-rtbfabric_RequesterGatewayGatewayId)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Resource types (\*required):** [LinkRoutingRule\*](#list_rtbfabric-resource-LinkRoutingRule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:LinkLinkId](#list_rtbfabric-rtbfabric_LinkLinkId)<br />[rtbfabric:LinkRoutingRuleRuleId](#list_rtbfabric-rtbfabric_LinkRoutingRuleRuleId)
  - **Access level:** Read

- **   [GetOutboundExternalLink](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_GetOutboundExternalLink.html)  **
  - **Description:** Grants permission to retrieve information about an outbound external link
  - **Resource types (\*required):** [OutboundExternalLink\*](#list_rtbfabric-resource-OutboundExternalLink) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:OutboundExternalLinkLinkId](#list_rtbfabric-rtbfabric_OutboundExternalLinkLinkId)<br />[rtbfabric:RequesterGatewayGatewayId](#list_rtbfabric-rtbfabric_RequesterGatewayGatewayId)
  - **Resource types (\*required):** [RequesterGateway\*](#list_rtbfabric-resource-RequesterGateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:RequesterGatewayGatewayId](#list_rtbfabric-rtbfabric_RequesterGatewayGatewayId)
  - **Access level:** Read

- **   [GetRequesterGateway](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_GetRequesterGateway.html)  **
  - **Description:** Grants permission to retrieve information about a requester gateway
  - **Resource types (\*required):** [RequesterGateway\*](#list_rtbfabric-resource-RequesterGateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:RequesterGatewayGatewayId](#list_rtbfabric-rtbfabric_RequesterGatewayGatewayId)
  - **Access level:** Read

- **   [GetResponderGateway](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_GetResponderGateway.html)  **
  - **Description:** Grants permission to retrieve information about a responder gateway
  - **Resource types (\*required):** [ResponderGateway\*](#list_rtbfabric-resource-ResponderGateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Access level:** Read

- **   [ListCertificateAssociations](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_ListCertificateAssociations.html)  **
  - **Description:** Grants permission to list certificate associations for a responder gateway
  - **Resource types (\*required):** [ResponderGateway\*](#list_rtbfabric-resource-ResponderGateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Access level:** List

- **   [ListLinkRoutingRules](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_ListLinkRoutingRules.html)  **
  - **Description:** Grants permission to list routing rules for a link
  - **Resource types (\*required):** [Link\*](#list_rtbfabric-resource-Link)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:LinkLinkId](#list_rtbfabric-rtbfabric_LinkLinkId)<br />[rtbfabric:RequesterGatewayGatewayId](#list_rtbfabric-rtbfabric_RequesterGatewayGatewayId)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Access level:** List

- **   [ListLinks](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_ListLinks.html)  **
  - **Description:** Grants permission to list links associated with an RTB application
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRequesterGateways](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_ListRequesterGateways.html)  **
  - **Description:** Grants permission to list requester gateways with optional filtering and pagination
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListResponderGateways](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_ListResponderGateways.html)  **
  - **Description:** Grants permission to list responder gateways with optional filtering and pagination
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [InboundExternalLink](#list_rtbfabric-resource-InboundExternalLink) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:InboundExternalLinkLinkId](#list_rtbfabric-rtbfabric_InboundExternalLinkLinkId)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Resource types (\*required):** [Link](#list_rtbfabric-resource-Link) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:LinkLinkId](#list_rtbfabric-rtbfabric_LinkLinkId)<br />[rtbfabric:RequesterGatewayGatewayId](#list_rtbfabric-rtbfabric_RequesterGatewayGatewayId)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Resource types (\*required):** [LinkRoutingRule](#list_rtbfabric-resource-LinkRoutingRule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:LinkLinkId](#list_rtbfabric-rtbfabric_LinkLinkId)<br />[rtbfabric:LinkRoutingRuleRuleId](#list_rtbfabric-rtbfabric_LinkRoutingRuleRuleId)
  - **Resource types (\*required):** [OutboundExternalLink](#list_rtbfabric-resource-OutboundExternalLink) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:OutboundExternalLinkLinkId](#list_rtbfabric-rtbfabric_OutboundExternalLinkLinkId)<br />[rtbfabric:RequesterGatewayGatewayId](#list_rtbfabric-rtbfabric_RequesterGatewayGatewayId)
  - **Resource types (\*required):** [RequesterGateway](#list_rtbfabric-resource-RequesterGateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:RequesterGatewayGatewayId](#list_rtbfabric-rtbfabric_RequesterGatewayGatewayId)
  - **Resource types (\*required):** [ResponderGateway](#list_rtbfabric-resource-ResponderGateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Access level:** Read

- **   [RejectLink](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_RejectLink.html)  **
  - **Description:** Grants permission to reject a link request between RTB applications
  - **Resource types (\*required):** [Link\*](#list_rtbfabric-resource-Link)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:LinkLinkId](#list_rtbfabric-rtbfabric_LinkLinkId)<br />[rtbfabric:RequesterGatewayGatewayId](#list_rtbfabric-rtbfabric_RequesterGatewayGatewayId)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_TagResource.html)  **
  - **Description:** Grants permission to assign one or more tags (key-value pairs) to the specified resource
  - **Resource types (\*required):** [InboundExternalLink](#list_rtbfabric-resource-InboundExternalLink) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rtbfabric-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rtbfabric-aws_TagKeys)<br />[rtbfabric:InboundExternalLinkLinkId](#list_rtbfabric-rtbfabric_InboundExternalLinkLinkId)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Resource types (\*required):** [Link](#list_rtbfabric-resource-Link) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rtbfabric-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rtbfabric-aws_TagKeys)<br />[rtbfabric:LinkLinkId](#list_rtbfabric-rtbfabric_LinkLinkId)<br />[rtbfabric:RequesterGatewayGatewayId](#list_rtbfabric-rtbfabric_RequesterGatewayGatewayId)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Resource types (\*required):** [LinkRoutingRule](#list_rtbfabric-resource-LinkRoutingRule) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rtbfabric-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rtbfabric-aws_TagKeys)<br />[rtbfabric:LinkLinkId](#list_rtbfabric-rtbfabric_LinkLinkId)<br />[rtbfabric:LinkRoutingRuleRuleId](#list_rtbfabric-rtbfabric_LinkRoutingRuleRuleId)
  - **Resource types (\*required):** [OutboundExternalLink](#list_rtbfabric-resource-OutboundExternalLink) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rtbfabric-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rtbfabric-aws_TagKeys)<br />[rtbfabric:OutboundExternalLinkLinkId](#list_rtbfabric-rtbfabric_OutboundExternalLinkLinkId)<br />[rtbfabric:RequesterGatewayGatewayId](#list_rtbfabric-rtbfabric_RequesterGatewayGatewayId)
  - **Resource types (\*required):** [RequesterGateway](#list_rtbfabric-resource-RequesterGateway) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rtbfabric-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rtbfabric-aws_TagKeys)<br />[rtbfabric:RequesterGatewayGatewayId](#list_rtbfabric-rtbfabric_RequesterGatewayGatewayId)
  - **Resource types (\*required):** [ResponderGateway](#list_rtbfabric-resource-ResponderGateway) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rtbfabric-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rtbfabric-aws_TagKeys)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_UntagResource.html)  **
  - **Description:** Grants permission to remove a tag or tags from a resource
  - **Resource types (\*required):** [InboundExternalLink](#list_rtbfabric-resource-InboundExternalLink) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rtbfabric-aws_TagKeys)<br />[rtbfabric:InboundExternalLinkLinkId](#list_rtbfabric-rtbfabric_InboundExternalLinkLinkId)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Resource types (\*required):** [Link](#list_rtbfabric-resource-Link) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rtbfabric-aws_TagKeys)<br />[rtbfabric:LinkLinkId](#list_rtbfabric-rtbfabric_LinkLinkId)<br />[rtbfabric:RequesterGatewayGatewayId](#list_rtbfabric-rtbfabric_RequesterGatewayGatewayId)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Resource types (\*required):** [LinkRoutingRule](#list_rtbfabric-resource-LinkRoutingRule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rtbfabric-aws_TagKeys)<br />[rtbfabric:LinkLinkId](#list_rtbfabric-rtbfabric_LinkLinkId)<br />[rtbfabric:LinkRoutingRuleRuleId](#list_rtbfabric-rtbfabric_LinkRoutingRuleRuleId)
  - **Resource types (\*required):** [OutboundExternalLink](#list_rtbfabric-resource-OutboundExternalLink) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rtbfabric-aws_TagKeys)<br />[rtbfabric:OutboundExternalLinkLinkId](#list_rtbfabric-rtbfabric_OutboundExternalLinkLinkId)<br />[rtbfabric:RequesterGatewayGatewayId](#list_rtbfabric-rtbfabric_RequesterGatewayGatewayId)
  - **Resource types (\*required):** [RequesterGateway](#list_rtbfabric-resource-RequesterGateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rtbfabric-aws_TagKeys)<br />[rtbfabric:RequesterGatewayGatewayId](#list_rtbfabric-rtbfabric_RequesterGatewayGatewayId)
  - **Resource types (\*required):** [ResponderGateway](#list_rtbfabric-resource-ResponderGateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rtbfabric-aws_TagKeys)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Access level:** Tagging, Write

- **   [UpdateLink](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_UpdateLink.html)  **
  - **Description:** Grants permission to update configuration settings for an existing link
  - **Resource types (\*required):** [Link\*](#list_rtbfabric-resource-Link)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:LinkLinkId](#list_rtbfabric-rtbfabric_LinkLinkId)<br />[rtbfabric:RequesterGatewayGatewayId](#list_rtbfabric-rtbfabric_RequesterGatewayGatewayId)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Access level:** Write

- **   [UpdateLinkModuleFlow](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_UpdateLinkModuleFlow.html)  **
  - **Description:** Grants permission to update a link module flow
  - **Resource types (\*required):** [Link\*](#list_rtbfabric-resource-Link)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:LinkLinkId](#list_rtbfabric-rtbfabric_LinkLinkId)<br />[rtbfabric:RequesterGatewayGatewayId](#list_rtbfabric-rtbfabric_RequesterGatewayGatewayId)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Access level:** Write

- **   [UpdateLinkRoutingRule](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_UpdateLinkRoutingRule.html)  **
  - **Description:** Grants permission to update a routing rule for a link
  - **Resource types (\*required):** [Link\*](#list_rtbfabric-resource-Link) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:LinkLinkId](#list_rtbfabric-rtbfabric_LinkLinkId)<br />[rtbfabric:RequesterGatewayGatewayId](#list_rtbfabric-rtbfabric_RequesterGatewayGatewayId)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Resource types (\*required):** [LinkRoutingRule\*](#list_rtbfabric-resource-LinkRoutingRule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:LinkLinkId](#list_rtbfabric-rtbfabric_LinkLinkId)<br />[rtbfabric:LinkRoutingRuleRuleId](#list_rtbfabric-rtbfabric_LinkRoutingRuleRuleId)
  - **Access level:** Write

- **   [UpdateRequesterGateway](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_UpdateRequesterGateway.html)  **
  - **Description:** Grants permission to update a requester gateway
  - **Resource types (\*required):** [RequesterGateway\*](#list_rtbfabric-resource-RequesterGateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:RequesterGatewayGatewayId](#list_rtbfabric-rtbfabric_RequesterGatewayGatewayId)
  - **Access level:** Write

- **   [UpdateResponderGateway](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_UpdateResponderGateway.html)  **
  - **Description:** Grants permission to update a responder gateway
  - **Resource types (\*required):** [ResponderGateway\*](#list_rtbfabric-resource-ResponderGateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId)
  - **Access level:** Write



## Resource types defined by AWS RTB Fabric
<a name="list_rtbfabric-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [InboundExternalLink](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/links.html)  | arn:${Partition}:rtbfabric:${Region}:${Account}:gateway/${GatewayId}/link/${LinkId} | [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:InboundExternalLinkLinkId](#list_rtbfabric-rtbfabric_InboundExternalLinkLinkId)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId) | 
|  [Link](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/links.html)  | arn:${Partition}:rtbfabric:${Region}:${Account}:gateway/${GatewayId}/link/${LinkId} | [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:LinkLinkId](#list_rtbfabric-rtbfabric_LinkLinkId)<br />[rtbfabric:RequesterGatewayGatewayId](#list_rtbfabric-rtbfabric_RequesterGatewayGatewayId)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId) | 
|  [LinkRoutingRule](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/links.html)  | arn:${Partition}:rtbfabric:${Region}:${Account}:gateway/${GatewayId}/link/${LinkId}/routing-rule/${RuleId} | [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:LinkLinkId](#list_rtbfabric-rtbfabric_LinkLinkId)<br />[rtbfabric:LinkRoutingRuleRuleId](#list_rtbfabric-rtbfabric_LinkRoutingRuleRuleId) | 
|  [OutboundExternalLink](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/links.html)  | arn:${Partition}:rtbfabric:${Region}:${Account}:gateway/${GatewayId}/link/${LinkId} | [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:OutboundExternalLinkLinkId](#list_rtbfabric-rtbfabric_OutboundExternalLinkLinkId)<br />[rtbfabric:RequesterGatewayGatewayId](#list_rtbfabric-rtbfabric_RequesterGatewayGatewayId) | 
|  [RequesterGateway](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/working-with-requester-rtb-applications.html)  | arn:${Partition}:rtbfabric:${Region}:${Account}:gateway/${GatewayId} | [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:RequesterGatewayGatewayId](#list_rtbfabric-rtbfabric_RequesterGatewayGatewayId) | 
|  [ResponderGateway](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/working-with-responder-rtb-applications.html)  | arn:${Partition}:rtbfabric:${Region}:${Account}:gateway/${GatewayId} | [aws:ResourceTag/${TagKey}](#list_rtbfabric-aws_ResourceTag___TagKey_)<br />[rtbfabric:ResponderGatewayGatewayId](#list_rtbfabric-rtbfabric_ResponderGatewayGatewayId) | 

## Condition keys for AWS RTB Fabric
<a name="list_rtbfabric-policy-keys"></a>

AWS RTB Fabric defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag key and value pair that is allowed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by a tag key and value pair of a resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by a list of tag keys that are allowed in the request | ArrayOfString | 
|   [rtbfabric:InboundExternalLinkGatewayId](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/security_iam_service-with-iam.html)  | Filters access by gateway identifier supporting rtb-gw-\* formats | String | 
|   [rtbfabric:InboundExternalLinkLinkId](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/security_iam_service-with-iam.html)  | Filters access by InboundExternalLink resource linkId identifier | String | 
|   [rtbfabric:LinkLinkId](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/security_iam_service-with-iam.html)  | Filters access by Link resource linkId identifier | String | 
|   [rtbfabric:LinkRoutingRuleRuleId](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/security_iam_service-with-iam.html)  | Filters access by routing rule identifier supporting rule-\* formats | String | 
|   [rtbfabric:OutboundExternalLinkLinkId](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/security_iam_service-with-iam.html)  | Filters access by OutboundExternalLink resource linkId identifier | String | 
|   [rtbfabric:RequesterGatewayGatewayId](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/security_iam_service-with-iam.html)  | Filters access by gateway identifier supporting rtb-gw-\* formats | String | 
|   [rtbfabric:ResponderGatewayGatewayId](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/security_iam_service-with-iam.html)  | Filters access by gateway identifier supporting rtb-gw-\* formats | String | 