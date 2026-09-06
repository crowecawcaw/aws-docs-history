

# Actions, resources, and condition keys for AWS Elemental MediaConnect
<a name="list_mediaconnect"></a>

AWS Elemental MediaConnect (service prefix: `mediaconnect`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/mediaconnect/latest/ug/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/mediaconnect/latest/api/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/mediaconnect/latest/ug/security.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/mediaconnect/mediaconnect.json) for this service.

**Topics**
+ [API operations defined by AWS Elemental MediaConnect](#list_mediaconnect-operations)
+ [Actions defined by AWS Elemental MediaConnect](#list_mediaconnect-actions-as-permissions)
+ [Resource types defined by AWS Elemental MediaConnect](#list_mediaconnect-resources-for-iam-policies)
+ [Condition keys for AWS Elemental MediaConnect](#list_mediaconnect-policy-keys)

## API operations defined by AWS Elemental MediaConnect
<a name="list_mediaconnect-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_mediaconnect-actions-as-permissions).




- **   AddBridgeOutputs  **
  - **IAM action:**  [mediaconnect:AddBridgeOutputs](#list_mediaconnect-action-AddBridgeOutputs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AddBridgeSources  **
  - **IAM action:**  [mediaconnect:AddBridgeSources](#list_mediaconnect-action-AddBridgeSources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AddFlowMediaStreams  **
  - **IAM action:**  [mediaconnect:AddFlowMediaStreams](#list_mediaconnect-action-AddFlowMediaStreams)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconnect:TagResource](#list_mediaconnect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   AddFlowOutputs  **
  - **IAM action:**  [mediaconnect:AddFlowOutputs](#list_mediaconnect-action-AddFlowOutputs)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconnect:TagResource](#list_mediaconnect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mediaconnect.amazonaws.com / **Access level:** Write

- **   AddFlowSources  **
  - **IAM action:**  [mediaconnect:AddFlowSources](#list_mediaconnect-action-AddFlowSources)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconnect:TagResource](#list_mediaconnect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mediaconnect.amazonaws.com / **Access level:** Write

- **   AddFlowVpcInterfaces  **
  - **IAM action:**  [mediaconnect:AddFlowVpcInterfaces](#list_mediaconnect-action-AddFlowVpcInterfaces)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconnect:TagResource](#list_mediaconnect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mediaconnect.amazonaws.com / **Access level:** Write

- **   BatchGetRouterInput  **
  - **IAM action:**  [mediaconnect:GetRouterInput](#list_mediaconnect-action-GetRouterInput) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetRouterNetworkInterface  **
  - **IAM action:**  [mediaconnect:GetRouterNetworkInterface](#list_mediaconnect-action-GetRouterNetworkInterface) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetRouterOutput  **
  - **IAM action:**  [mediaconnect:GetRouterOutput](#list_mediaconnect-action-GetRouterOutput) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CreateBridge  **
  - **IAM action:**  [mediaconnect:AddBridgeOutputs](#list_mediaconnect-action-AddBridgeOutputs)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconnect:AddBridgeSources](#list_mediaconnect-action-AddBridgeSources)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconnect:CreateBridge](#list_mediaconnect-action-CreateBridge)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateFlow  **
  - **IAM action:**  [mediaconnect:AddFlowMediaStreams](#list_mediaconnect-action-AddFlowMediaStreams)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconnect:AddFlowOutputs](#list_mediaconnect-action-AddFlowOutputs)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconnect:AddFlowSources](#list_mediaconnect-action-AddFlowSources)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconnect:AddFlowVpcInterfaces](#list_mediaconnect-action-AddFlowVpcInterfaces)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconnect:CreateFlow](#list_mediaconnect-action-CreateFlow)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconnect:GrantFlowEntitlements](#list_mediaconnect-action-GrantFlowEntitlements)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconnect:TagResource](#list_mediaconnect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mediaconnect.amazonaws.com / **Access level:** Write

- **   CreateGateway  **
  - **IAM action:**  [mediaconnect:CreateGateway](#list_mediaconnect-action-CreateGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateRouterInput  **
  - **IAM action:**  [mediaconnect:AssociateRouterNetworkInterface](#list_mediaconnect-action-AssociateRouterNetworkInterface)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconnect:CreateRouterInput](#list_mediaconnect-action-CreateRouterInput)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconnect:TagResource](#list_mediaconnect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [mediaconnect:UpdateFlowOutput](#list_mediaconnect-action-UpdateFlowOutput)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mediaconnect.amazonaws.com / **Access level:** Write

- **   CreateRouterNetworkInterface  **
  - **IAM action:**  [mediaconnect:CreateRouterNetworkInterface](#list_mediaconnect-action-CreateRouterNetworkInterface)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconnect:TagResource](#list_mediaconnect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRouterOutput  **
  - **IAM action:**  [mediaconnect:AssociateRouterNetworkInterface](#list_mediaconnect-action-AssociateRouterNetworkInterface)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconnect:CreateRouterOutput](#list_mediaconnect-action-CreateRouterOutput)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconnect:TagResource](#list_mediaconnect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [mediaconnect:UpdateFlowSource](#list_mediaconnect-action-UpdateFlowSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mediaconnect.amazonaws.com / **Access level:** Write

- **   DeleteBridge  **
  - **IAM action:**  [mediaconnect:DeleteBridge](#list_mediaconnect-action-DeleteBridge)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconnect:RemoveBridgeOutput](#list_mediaconnect-action-RemoveBridgeOutput)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconnect:RemoveBridgeSource](#list_mediaconnect-action-RemoveBridgeSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteFlow  **
  - **IAM action:**  [mediaconnect:DeleteFlow](#list_mediaconnect-action-DeleteFlow)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconnect:RemoveFlowMediaStream](#list_mediaconnect-action-RemoveFlowMediaStream)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconnect:RemoveFlowOutput](#list_mediaconnect-action-RemoveFlowOutput)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconnect:RemoveFlowSource](#list_mediaconnect-action-RemoveFlowSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconnect:RemoveFlowVpcInterface](#list_mediaconnect-action-RemoveFlowVpcInterface)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconnect:RevokeFlowEntitlement](#list_mediaconnect-action-RevokeFlowEntitlement)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteGateway  **
  - **IAM action:**  [mediaconnect:DeleteGateway](#list_mediaconnect-action-DeleteGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRouterInput  **
  - **IAM action:**  [mediaconnect:DeleteRouterInput](#list_mediaconnect-action-DeleteRouterInput)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconnect:UpdateFlowOutput](#list_mediaconnect-action-UpdateFlowOutput)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteRouterNetworkInterface  **
  - **IAM action:**  [mediaconnect:DeleteRouterNetworkInterface](#list_mediaconnect-action-DeleteRouterNetworkInterface) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRouterOutput  **
  - **IAM action:**  [mediaconnect:DeleteRouterOutput](#list_mediaconnect-action-DeleteRouterOutput)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconnect:UpdateFlowSource](#list_mediaconnect-action-UpdateFlowSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeregisterGatewayInstance  **
  - **IAM action:**  [mediaconnect:DeregisterGatewayInstance](#list_mediaconnect-action-DeregisterGatewayInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeBridge  **
  - **IAM action:**  [mediaconnect:DescribeBridge](#list_mediaconnect-action-DescribeBridge) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFlow  **
  - **IAM action:**  [mediaconnect:DescribeFlow](#list_mediaconnect-action-DescribeFlow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFlowSourceMetadata  **
  - **IAM action:**  [mediaconnect:DescribeFlowSourceMetadata](#list_mediaconnect-action-DescribeFlowSourceMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFlowSourceThumbnail  **
  - **IAM action:**  [mediaconnect:DescribeFlowSourceThumbnail](#list_mediaconnect-action-DescribeFlowSourceThumbnail) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeGateway  **
  - **IAM action:**  [mediaconnect:DescribeGateway](#list_mediaconnect-action-DescribeGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeGatewayInstance  **
  - **IAM action:**  [mediaconnect:DescribeGatewayInstance](#list_mediaconnect-action-DescribeGatewayInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeOffering  **
  - **IAM action:**  [mediaconnect:DescribeOffering](#list_mediaconnect-action-DescribeOffering) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeReservation  **
  - **IAM action:**  [mediaconnect:DescribeReservation](#list_mediaconnect-action-DescribeReservation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRouterInput  **
  - **IAM action:**  [mediaconnect:GetRouterInput](#list_mediaconnect-action-GetRouterInput) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRouterInputSourceMetadata  **
  - **IAM action:**  [mediaconnect:GetRouterInputSourceMetadata](#list_mediaconnect-action-GetRouterInputSourceMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRouterInputThumbnail  **
  - **IAM action:**  [mediaconnect:GetRouterInputThumbnail](#list_mediaconnect-action-GetRouterInputThumbnail) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRouterNetworkInterface  **
  - **IAM action:**  [mediaconnect:GetRouterNetworkInterface](#list_mediaconnect-action-GetRouterNetworkInterface) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRouterOutput  **
  - **IAM action:**  [mediaconnect:GetRouterOutput](#list_mediaconnect-action-GetRouterOutput) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GrantFlowEntitlements  **
  - **IAM action:**  [mediaconnect:GrantFlowEntitlements](#list_mediaconnect-action-GrantFlowEntitlements)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconnect:TagResource](#list_mediaconnect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mediaconnect.amazonaws.com / **Access level:** Write

- **   ListBridges  **
  - **IAM action:**  [mediaconnect:ListBridges](#list_mediaconnect-action-ListBridges) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEntitlements  **
  - **IAM action:**  [mediaconnect:ListEntitlements](#list_mediaconnect-action-ListEntitlements) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFlows  **
  - **IAM action:**  [mediaconnect:ListFlows](#list_mediaconnect-action-ListFlows) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGatewayInstances  **
  - **IAM action:**  [mediaconnect:ListGatewayInstances](#list_mediaconnect-action-ListGatewayInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGateways  **
  - **IAM action:**  [mediaconnect:ListGateways](#list_mediaconnect-action-ListGateways) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOfferings  **
  - **IAM action:**  [mediaconnect:ListOfferings](#list_mediaconnect-action-ListOfferings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReservations  **
  - **IAM action:**  [mediaconnect:ListReservations](#list_mediaconnect-action-ListReservations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRouterInputs  **
  - **IAM action:**  [mediaconnect:ListRouterInputs](#list_mediaconnect-action-ListRouterInputs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRouterNetworkInterfaces  **
  - **IAM action:**  [mediaconnect:ListRouterNetworkInterfaces](#list_mediaconnect-action-ListRouterNetworkInterfaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRouterOutputs  **
  - **IAM action:**  [mediaconnect:ListRouterOutputs](#list_mediaconnect-action-ListRouterOutputs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [mediaconnect:ListTagsForResource](#list_mediaconnect-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PurchaseOffering  **
  - **IAM action:**  [mediaconnect:PurchaseOffering](#list_mediaconnect-action-PurchaseOffering) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveBridgeOutput  **
  - **IAM action:**  [mediaconnect:RemoveBridgeOutput](#list_mediaconnect-action-RemoveBridgeOutput) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveBridgeSource  **
  - **IAM action:**  [mediaconnect:RemoveBridgeSource](#list_mediaconnect-action-RemoveBridgeSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveFlowMediaStream  **
  - **IAM action:**  [mediaconnect:RemoveFlowMediaStream](#list_mediaconnect-action-RemoveFlowMediaStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveFlowOutput  **
  - **IAM action:**  [mediaconnect:RemoveFlowOutput](#list_mediaconnect-action-RemoveFlowOutput) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveFlowSource  **
  - **IAM action:**  [mediaconnect:RemoveFlowSource](#list_mediaconnect-action-RemoveFlowSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveFlowVpcInterface  **
  - **IAM action:**  [mediaconnect:RemoveFlowVpcInterface](#list_mediaconnect-action-RemoveFlowVpcInterface) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RestartRouterInput  **
  - **IAM action:**  [mediaconnect:RestartRouterInput](#list_mediaconnect-action-RestartRouterInput) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RestartRouterOutput  **
  - **IAM action:**  [mediaconnect:RestartRouterOutput](#list_mediaconnect-action-RestartRouterOutput) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RevokeFlowEntitlement  **
  - **IAM action:**  [mediaconnect:RevokeFlowEntitlement](#list_mediaconnect-action-RevokeFlowEntitlement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartFlow  **
  - **IAM action:**  [mediaconnect:StartFlow](#list_mediaconnect-action-StartFlow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartRouterInput  **
  - **IAM action:**  [mediaconnect:StartRouterInput](#list_mediaconnect-action-StartRouterInput) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartRouterOutput  **
  - **IAM action:**  [mediaconnect:StartRouterOutput](#list_mediaconnect-action-StartRouterOutput) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopFlow  **
  - **IAM action:**  [mediaconnect:StopFlow](#list_mediaconnect-action-StopFlow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopRouterInput  **
  - **IAM action:**  [mediaconnect:StopRouterInput](#list_mediaconnect-action-StopRouterInput) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopRouterOutput  **
  - **IAM action:**  [mediaconnect:StopRouterOutput](#list_mediaconnect-action-StopRouterOutput) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [mediaconnect:TagResource](#list_mediaconnect-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TakeRouterInput  **
  - **IAM action:**  [mediaconnect:TakeRouterInput](#list_mediaconnect-action-TakeRouterInput) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [mediaconnect:UntagResource](#list_mediaconnect-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateBridge  **
  - **IAM action:**  [mediaconnect:UpdateBridge](#list_mediaconnect-action-UpdateBridge) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateBridgeOutput  **
  - **IAM action:**  [mediaconnect:UpdateBridgeOutput](#list_mediaconnect-action-UpdateBridgeOutput) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateBridgeSource  **
  - **IAM action:**  [mediaconnect:UpdateBridgeSource](#list_mediaconnect-action-UpdateBridgeSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateBridgeState  **
  - **IAM action:**  [mediaconnect:UpdateBridgeState](#list_mediaconnect-action-UpdateBridgeState) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFlow  **
  - **IAM action:**  [mediaconnect:UpdateFlow](#list_mediaconnect-action-UpdateFlow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFlowEntitlement  **
  - **IAM action:**  [mediaconnect:UpdateFlowEntitlement](#list_mediaconnect-action-UpdateFlowEntitlement)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mediaconnect.amazonaws.com / **Access level:** Write

- **   UpdateFlowMediaStream  **
  - **IAM action:**  [mediaconnect:UpdateFlowMediaStream](#list_mediaconnect-action-UpdateFlowMediaStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFlowOutput  **
  - **IAM action:**  [mediaconnect:UpdateFlowOutput](#list_mediaconnect-action-UpdateFlowOutput)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mediaconnect.amazonaws.com / **Access level:** Write

- **   UpdateFlowSource  **
  - **IAM action:**  [mediaconnect:UpdateFlowSource](#list_mediaconnect-action-UpdateFlowSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mediaconnect.amazonaws.com / **Access level:** Write

- **   UpdateGatewayInstance  **
  - **IAM action:**  [mediaconnect:UpdateGatewayInstance](#list_mediaconnect-action-UpdateGatewayInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRouterInput  **
  - **IAM action:**  [mediaconnect:AssociateRouterNetworkInterface](#list_mediaconnect-action-AssociateRouterNetworkInterface)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconnect:UpdateFlowOutput](#list_mediaconnect-action-UpdateFlowOutput)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconnect:UpdateRouterInput](#list_mediaconnect-action-UpdateRouterInput)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mediaconnect.amazonaws.com / **Access level:** Write

- **   UpdateRouterNetworkInterface  **
  - **IAM action:**  [mediaconnect:UpdateRouterNetworkInterface](#list_mediaconnect-action-UpdateRouterNetworkInterface) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRouterOutput  **
  - **IAM action:**  [mediaconnect:AssociateRouterNetworkInterface](#list_mediaconnect-action-AssociateRouterNetworkInterface)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconnect:UpdateFlowSource](#list_mediaconnect-action-UpdateFlowSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediaconnect:UpdateRouterOutput](#list_mediaconnect-action-UpdateRouterOutput)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** mediaconnect.amazonaws.com / **Access level:** Write



## Actions defined by AWS Elemental MediaConnect
<a name="list_mediaconnect-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddBridgeOutputs](https://docs.aws.amazon.com/mediaconnect/latest/api/API_AddBridgeOutputs.html)  **
  - **Description:** Grants permission to add outputs to an existing bridge
  - **Resource types (\*required):** [Bridge\*](#list_mediaconnect-resource-Bridge)
  - **Condition keys:**  
  - **Access level:** Write

- **   [AddBridgeSources](https://docs.aws.amazon.com/mediaconnect/latest/api/API_AddBridgeSources.html)  **
  - **Description:** Grants permission to add sources to an existing bridge
  - **Resource types (\*required):** [Bridge\*](#list_mediaconnect-resource-Bridge)
  - **Condition keys:**  
  - **Access level:** Write

- **   [AddFlowMediaStreams](https://docs.aws.amazon.com/mediaconnect/latest/api/API_AddFlowMediaStreams.html)  **
  - **Description:** Grants permission to add media streams to any flow
  - **Resource types (\*required):** [Flow\*](#list_mediaconnect-resource-Flow) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Resource types (\*required):** [MediaStream\*](#list_mediaconnect-resource-MediaStream) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Access level:** Write

- **   [AddFlowOutputs](https://docs.aws.amazon.com/mediaconnect/latest/api/API_AddFlowOutputs.html)  **
  - **Description:** Grants permission to add outputs to any flow
  - **Resource types (\*required):** [Flow\*](#list_mediaconnect-resource-Flow) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Resource types (\*required):** [Output\*](#list_mediaconnect-resource-Output) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Access level:** Write

- **   [AddFlowSources](https://docs.aws.amazon.com/mediaconnect/latest/api/API_AddFlowSources.html)  **
  - **Description:** Grants permission to add sources to any flow
  - **Resource types (\*required):** [Flow\*](#list_mediaconnect-resource-Flow) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Resource types (\*required):** [Source\*](#list_mediaconnect-resource-Source) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Access level:** Write

- **   [AddFlowVpcInterfaces](https://docs.aws.amazon.com/mediaconnect/latest/api/API_AddFlowVpcInterfaces.html)  **
  - **Description:** Grants permission to add VPC interfaces to any flow
  - **Resource types (\*required):** [Flow\*](#list_mediaconnect-resource-Flow) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Resource types (\*required):** [VpcInterface\*](#list_mediaconnect-resource-VpcInterface) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Access level:** Write

- **   [AssociateRouterNetworkInterface](https://docs.aws.amazon.com/mediaconnect/latest/api/API_AssociateRouterNetworkInterface.html)  **
  - **Description:** Grants permission to associate a router network interface
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateBridge](https://docs.aws.amazon.com/mediaconnect/latest/api/API_CreateBridge.html)  **
  - **Description:** Grants permission to create bridges
  - **Resource types (\*required):** [Bridge\*](#list_mediaconnect-resource-Bridge)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateFlow](https://docs.aws.amazon.com/mediaconnect/latest/api/API_CreateFlow.html)  **
  - **Description:** Grants permission to create flows
  - **Resource types (\*required):** [Flow\*](#list_mediaconnect-resource-Flow)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Access level:** Write

- **   [CreateGateway](https://docs.aws.amazon.com/mediaconnect/latest/api/API_CreateGateway.html)  **
  - **Description:** Grants permission to create gateways
  - **Resource types (\*required):** [Gateway\*](#list_mediaconnect-resource-Gateway)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateRouterInput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_CreateRouterInput.html)  **
  - **Description:** Grants permission to create a new router input in AWS Elemental MediaConnect
  - **Resource types (\*required):** [RouterInput\*](#list_mediaconnect-resource-RouterInput)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRouterNetworkInterface](https://docs.aws.amazon.com/mediaconnect/latest/api/API_CreateRouterNetworkInterface.html)  **
  - **Description:** Grants permission to create a new router network interface in AWS Elemental MediaConnect
  - **Resource types (\*required):** [RouterNetworkInterface\*](#list_mediaconnect-resource-RouterNetworkInterface)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRouterOutput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_CreateRouterOutput.html)  **
  - **Description:** Grants permission to create a new router output in AWS Elemental MediaConnect
  - **Resource types (\*required):** [RouterOutput\*](#list_mediaconnect-resource-RouterOutput)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteBridge](https://docs.aws.amazon.com/mediaconnect/latest/api/API_DeleteBridge.html)  **
  - **Description:** Grants permission to delete bridges
  - **Resource types (\*required):** [Bridge\*](#list_mediaconnect-resource-Bridge)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteFlow](https://docs.aws.amazon.com/mediaconnect/latest/api/API_DeleteFlow.html)  **
  - **Description:** Grants permission to delete flows
  - **Resource types (\*required):** [Flow\*](#list_mediaconnect-resource-Flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteGateway](https://docs.aws.amazon.com/mediaconnect/latest/api/API_DeleteGateway.html)  **
  - **Description:** Grants permission to delete gateways
  - **Resource types (\*required):** [Gateway\*](#list_mediaconnect-resource-Gateway)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteRouterInput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_DeleteRouterInput.html)  **
  - **Description:** Grants permission to delete a router input in AWS Elemental MediaConnect
  - **Resource types (\*required):** [RouterInput\*](#list_mediaconnect-resource-RouterInput)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRouterNetworkInterface](https://docs.aws.amazon.com/mediaconnect/latest/api/API_DeleteRouterNetworkInterface.html)  **
  - **Description:** Grants permission to delete a router network interface from AWS Elemental MediaConnect
  - **Resource types (\*required):** [RouterNetworkInterface\*](#list_mediaconnect-resource-RouterNetworkInterface)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRouterOutput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_DeleteRouterOutput.html)  **
  - **Description:** Grants permission to delete a router output from AWS Elemental MediaConnect
  - **Resource types (\*required):** [RouterOutput\*](#list_mediaconnect-resource-RouterOutput)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterGatewayInstance](https://docs.aws.amazon.com/mediaconnect/latest/api/API_DeregisterGatewayInstance.html)  **
  - **Description:** Grants permission to deregister gateway instance
  - **Resource types (\*required):** [GatewayInstance\*](#list_mediaconnect-resource-GatewayInstance)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeBridge](https://docs.aws.amazon.com/mediaconnect/latest/api/API_DescribeBridge.html)  **
  - **Description:** Grants permission to display the details of a bridge
  - **Resource types (\*required):** [Bridge\*](#list_mediaconnect-resource-Bridge)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeFlow](https://docs.aws.amazon.com/mediaconnect/latest/api/API_DescribeFlow.html)  **
  - **Description:** Grants permission to display the details of a flow including the flow ARN, name, and Availability Zone, as well as details about the source, outputs, and entitlements
  - **Resource types (\*required):** [Flow\*](#list_mediaconnect-resource-Flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFlowSourceMetadata](https://docs.aws.amazon.com/mediaconnect/latest/api/API_DescribeFlowSourceMetadata.html)  **
  - **Description:** Grants permission to view information about the flow's source transport stream and programs
  - **Resource types (\*required):** [Flow\*](#list_mediaconnect-resource-Flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFlowSourceThumbnail](https://docs.aws.amazon.com/mediaconnect/latest/api/API_DescribeFlowSourceThumbnail.html)  **
  - **Description:** Grants permission to view flow's source thumbnail
  - **Resource types (\*required):** [Flow\*](#list_mediaconnect-resource-Flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeGateway](https://docs.aws.amazon.com/mediaconnect/latest/api/API_DescribeGateway.html)  **
  - **Description:** Grants permission to display the details of a gateway including the gateway ARN, name, and CIDR blocks, as well as details about the networks
  - **Resource types (\*required):** [Gateway\*](#list_mediaconnect-resource-Gateway)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeGatewayInstance](https://docs.aws.amazon.com/mediaconnect/latest/api/API_DescribeGatewayInstance.html)  **
  - **Description:** Grants permission to display the details of a gateway instance
  - **Resource types (\*required):** [GatewayInstance\*](#list_mediaconnect-resource-GatewayInstance)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeOffering](https://docs.aws.amazon.com/mediaconnect/latest/api/API_DescribeOffering.html)  **
  - **Description:** Grants permission to display the details of an offering
  - **Resource types (\*required):** [Offering\*](#list_mediaconnect-resource-Offering)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeReservation](https://docs.aws.amazon.com/mediaconnect/latest/api/API_DescribeReservation.html)  **
  - **Description:** Grants permission to display the details of a reservation
  - **Resource types (\*required):** [Reservation\*](#list_mediaconnect-resource-Reservation)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DiscoverGatewayPollEndpoint](https://docs.aws.amazon.com/mediaconnect/latest/api/API_DiscoverGatewayPollEndpoint.html)  **
  - **Description:** Grants permission to discover gateway poll endpoint
  - **Resource types (\*required):** [Gateway\*](#list_mediaconnect-resource-Gateway)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRouterInput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_GetRouterInput.html)  **
  - **Description:** Grants permission to retrieve information about a specific router input in AWS Elemental MediaConnect
  - **Resource types (\*required):** [RouterInput\*](#list_mediaconnect-resource-RouterInput)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRouterInputSourceMetadata](https://docs.aws.amazon.com/mediaconnect/latest/api/API_GetRouterInputSourceMetadata.html)  **
  - **Description:** Grants permission to retrieve metadata about a router input source in AWS Elemental MediaConnect
  - **Resource types (\*required):** [RouterInput\*](#list_mediaconnect-resource-RouterInput)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRouterInputThumbnail](https://docs.aws.amazon.com/mediaconnect/latest/api/API_GetRouterInputThumbnail.html)  **
  - **Description:** Grants permission to retrieve the thumbnail for a router input in AWS Elemental MediaConnect
  - **Resource types (\*required):** [RouterInput\*](#list_mediaconnect-resource-RouterInput)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRouterNetworkInterface](https://docs.aws.amazon.com/mediaconnect/latest/api/API_GetRouterNetworkInterface.html)  **
  - **Description:** Grants permission to retrieve information about a specific router network interface in AWS Elemental MediaConnect
  - **Resource types (\*required):** [RouterNetworkInterface\*](#list_mediaconnect-resource-RouterNetworkInterface)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRouterOutput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_GetRouterOutput.html)  **
  - **Description:** Grants permission to retrieve information about a specific router output in AWS Elemental MediaConnect
  - **Resource types (\*required):** [RouterOutput\*](#list_mediaconnect-resource-RouterOutput)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GrantFlowEntitlements](https://docs.aws.amazon.com/mediaconnect/latest/api/API_GrantFlowEntitlements.html)  **
  - **Description:** Grants permission to grant entitlements on any flow
  - **Resource types (\*required):** [Entitlement\*](#list_mediaconnect-resource-Entitlement) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Resource types (\*required):** [Flow\*](#list_mediaconnect-resource-Flow) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Access level:** Write

- **   [ListBridges](https://docs.aws.amazon.com/mediaconnect/latest/api/API_ListBridges.html)  **
  - **Description:** Grants permission to display a list of bridges that are associated with this account and an optionally specified Arn
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEntitlements](https://docs.aws.amazon.com/mediaconnect/latest/api/API_ListEntitlements.html)  **
  - **Description:** Grants permission to display a list of all entitlements that have been granted to the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFlows](https://docs.aws.amazon.com/mediaconnect/latest/api/API_ListFlows.html)  **
  - **Description:** Grants permission to display a list of flows that are associated with this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListGatewayInstances](https://docs.aws.amazon.com/mediaconnect/latest/api/API_ListGatewayInstances.html)  **
  - **Description:** Grants permission to display a list of instances that are associated with this gateway
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListGateways](https://docs.aws.amazon.com/mediaconnect/latest/api/API_ListGateways.html)  **
  - **Description:** Grants permission to display a list of gateways that are associated with this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOfferings](https://docs.aws.amazon.com/mediaconnect/latest/api/API_ListOfferings.html)  **
  - **Description:** Grants permission to display a list of all offerings that are available to the account in the current AWS Region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListReservations](https://docs.aws.amazon.com/mediaconnect/latest/api/API_ListReservations.html)  **
  - **Description:** Grants permission to display a list of all reservations that have been purchased by the account in the current AWS Region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRouterInputs](https://docs.aws.amazon.com/mediaconnect/latest/api/API_ListRouterInputs.html)  **
  - **Description:** Grants permission to retrieve a list of router inputs in AWS Elemental MediaConnect
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRouterNetworkInterfaces](https://docs.aws.amazon.com/mediaconnect/latest/api/API_ListRouterNetworkInterfaces.html)  **
  - **Description:** Grants permission to retrieve a list of router network interfaces in AWS Elemental MediaConnect
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRouterOutputs](https://docs.aws.amazon.com/mediaconnect/latest/api/API_ListRouterOutputs.html)  **
  - **Description:** Grants permission to retrieve a list of router outputs in AWS Elemental MediaConnect
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/mediaconnect/latest/api/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to display a list of all tags associated with a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [PollGateway](https://docs.aws.amazon.com/mediaconnect/latest/api/API_PollGateway.html)  **
  - **Description:** Grants permission to poll gateway
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PurchaseOffering](https://docs.aws.amazon.com/mediaconnect/latest/api/API_PurchaseOffering.html)  **
  - **Description:** Grants permission to purchase an offering
  - **Resource types (\*required):** [Reservation\*](#list_mediaconnect-resource-Reservation)
  - **Condition keys:**  
  - **Access level:** Write

- **   [RemoveBridgeOutput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_RemoveBridgeOutput.html)  **
  - **Description:** Grants permission to remove an output of an existing bridge
  - **Resource types (\*required):** [Bridge\*](#list_mediaconnect-resource-Bridge)
  - **Condition keys:**  
  - **Access level:** Write

- **   [RemoveBridgeSource](https://docs.aws.amazon.com/mediaconnect/latest/api/API_RemoveBridgeSource.html)  **
  - **Description:** Grants permission to remove a source of an existing bridge
  - **Resource types (\*required):** [Bridge\*](#list_mediaconnect-resource-Bridge)
  - **Condition keys:**  
  - **Access level:** Write

- **   [RemoveFlowMediaStream](https://docs.aws.amazon.com/mediaconnect/latest/api/API_RemoveFlowMediaStream.html)  **
  - **Description:** Grants permission to remove media streams from any flow
  - **Resource types (\*required):** [Flow\*](#list_mediaconnect-resource-Flow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [MediaStream\*](#list_mediaconnect-resource-MediaStream) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RemoveFlowOutput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_RemoveFlowOutput.html)  **
  - **Description:** Grants permission to remove outputs from any flow
  - **Resource types (\*required):** [Flow\*](#list_mediaconnect-resource-Flow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Output\*](#list_mediaconnect-resource-Output) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RemoveFlowSource](https://docs.aws.amazon.com/mediaconnect/latest/api/API_RemoveFlowSource.html)  **
  - **Description:** Grants permission to remove sources from any flow
  - **Resource types (\*required):** [Flow\*](#list_mediaconnect-resource-Flow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Source\*](#list_mediaconnect-resource-Source) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RemoveFlowVpcInterface](https://docs.aws.amazon.com/mediaconnect/latest/api/API_RemoveFlowVpcInterface.html)  **
  - **Description:** Grants permission to remove VPC interfaces from any flow
  - **Resource types (\*required):** [Flow\*](#list_mediaconnect-resource-Flow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [VpcInterface\*](#list_mediaconnect-resource-VpcInterface) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RestartRouterInput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_RestartRouterInput.html)  **
  - **Description:** Grants permission to restart a router input in AWS Elemental MediaConnect
  - **Resource types (\*required):** [RouterInput\*](#list_mediaconnect-resource-RouterInput)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RestartRouterOutput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_RestartRouterOutput.html)  **
  - **Description:** Grants permission to restart a router output in AWS Elemental MediaConnect
  - **Resource types (\*required):** [RouterOutput\*](#list_mediaconnect-resource-RouterOutput)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RevokeFlowEntitlement](https://docs.aws.amazon.com/mediaconnect/latest/api/API_RevokeFlowEntitlement.html)  **
  - **Description:** Grants permission to revoke entitlements on any flow
  - **Resource types (\*required):** [Entitlement\*](#list_mediaconnect-resource-Entitlement) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Flow\*](#list_mediaconnect-resource-Flow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartFlow](https://docs.aws.amazon.com/mediaconnect/latest/api/API_StartFlow.html)  **
  - **Description:** Grants permission to start flows
  - **Resource types (\*required):** [Flow\*](#list_mediaconnect-resource-Flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartRouterInput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_StartRouterInput.html)  **
  - **Description:** Grants permission to start a router input in AWS Elemental MediaConnect
  - **Resource types (\*required):** [RouterInput\*](#list_mediaconnect-resource-RouterInput)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartRouterOutput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_StartRouterOutput.html)  **
  - **Description:** Grants permission to start a router output in AWS Elemental MediaConnect
  - **Resource types (\*required):** [RouterOutput\*](#list_mediaconnect-resource-RouterOutput)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopFlow](https://docs.aws.amazon.com/mediaconnect/latest/api/API_StopFlow.html)  **
  - **Description:** Grants permission to stop flows
  - **Resource types (\*required):** [Flow\*](#list_mediaconnect-resource-Flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopRouterInput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_StopRouterInput.html)  **
  - **Description:** Grants permission to stop a router input in AWS Elemental MediaConnect
  - **Resource types (\*required):** [RouterInput\*](#list_mediaconnect-resource-RouterInput)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopRouterOutput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_StopRouterOutput.html)  **
  - **Description:** Grants permission to stops a router output in AWS Elemental MediaConnect
  - **Resource types (\*required):** [RouterOutput\*](#list_mediaconnect-resource-RouterOutput)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SubmitGatewayStateChange](https://docs.aws.amazon.com/mediaconnect/latest/api/API_SubmitGatewayStateChange.html)  **
  - **Description:** Grants permission to submit gateway state change
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/mediaconnect/latest/api/API_TagResource.html)  **
  - **Description:** Grants permission to associate tags with resources
  - **Resource types (\*required):** [Entitlement](#list_mediaconnect-resource-Entitlement) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Resource types (\*required):** [Flow](#list_mediaconnect-resource-Flow) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Resource types (\*required):** [MediaStream](#list_mediaconnect-resource-MediaStream) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Resource types (\*required):** [Output](#list_mediaconnect-resource-Output) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Resource types (\*required):** [RouterInput](#list_mediaconnect-resource-RouterInput) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Resource types (\*required):** [RouterNetworkInterface](#list_mediaconnect-resource-RouterNetworkInterface) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Resource types (\*required):** [RouterOutput](#list_mediaconnect-resource-RouterOutput) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Resource types (\*required):** [Source](#list_mediaconnect-resource-Source) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Resource types (\*required):** [VpcInterface](#list_mediaconnect-resource-VpcInterface) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediaconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TakeRouterInput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_TakeRouterInput.html)  **
  - **Description:** Grants permission to associate a router input with a router output in AWS Elemental MediaConnect
  - **Resource types (\*required):** [RouterOutput\*](#list_mediaconnect-resource-RouterOutput)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/mediaconnect/latest/api/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from resources
  - **Resource types (\*required):** [Entitlement](#list_mediaconnect-resource-Entitlement) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Resource types (\*required):** [Flow](#list_mediaconnect-resource-Flow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Resource types (\*required):** [MediaStream](#list_mediaconnect-resource-MediaStream) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Resource types (\*required):** [Output](#list_mediaconnect-resource-Output) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Resource types (\*required):** [RouterInput](#list_mediaconnect-resource-RouterInput) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Resource types (\*required):** [RouterNetworkInterface](#list_mediaconnect-resource-RouterNetworkInterface) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Resource types (\*required):** [RouterOutput](#list_mediaconnect-resource-RouterOutput) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Resource types (\*required):** [Source](#list_mediaconnect-resource-Source) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Resource types (\*required):** [VpcInterface](#list_mediaconnect-resource-VpcInterface) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediaconnect-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateBridge](https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateBridge.html)  **
  - **Description:** Grants permission to update bridges
  - **Resource types (\*required):** [Bridge\*](#list_mediaconnect-resource-Bridge)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateBridgeOutput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateBridgeOutput.html)  **
  - **Description:** Grants permission to update an output of an existing bridge
  - **Resource types (\*required):** [Bridge\*](#list_mediaconnect-resource-Bridge)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateBridgeSource](https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateBridgeSource.html)  **
  - **Description:** Grants permission to update a source of an existing bridge
  - **Resource types (\*required):** [Bridge\*](#list_mediaconnect-resource-Bridge)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateBridgeState](https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateBridgeState.html)  **
  - **Description:** Grants permission to update the state of an existing bridge
  - **Resource types (\*required):** [Bridge\*](#list_mediaconnect-resource-Bridge)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateFlow](https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateFlow.html)  **
  - **Description:** Grants permission to update flows
  - **Resource types (\*required):** [Flow\*](#list_mediaconnect-resource-Flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFlowEntitlement](https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateFlowEntitlement.html)  **
  - **Description:** Grants permission to update entitlements on any flow
  - **Resource types (\*required):** [Flow\*](#list_mediaconnect-resource-Flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFlowMediaStream](https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateFlowMediaStream.html)  **
  - **Description:** Grants permission to update media streams on any flow
  - **Resource types (\*required):** [Flow\*](#list_mediaconnect-resource-Flow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [MediaStream\*](#list_mediaconnect-resource-MediaStream) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFlowOutput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateFlowOutput.html)  **
  - **Description:** Grants permission to update outputs on any flow
  - **Resource types (\*required):** [Flow\*](#list_mediaconnect-resource-Flow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Output\*](#list_mediaconnect-resource-Output) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFlowSource](https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateFlowSource.html)  **
  - **Description:** Grants permission to update the source of any flow
  - **Resource types (\*required):** [Flow\*](#list_mediaconnect-resource-Flow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Source\*](#list_mediaconnect-resource-Source) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateGatewayInstance](https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateGatewayInstance.html)  **
  - **Description:** Grants permission to update the configuration of an existing Gateway Instance
  - **Resource types (\*required):** [GatewayInstance\*](#list_mediaconnect-resource-GatewayInstance)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateRouterInput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateRouterInput.html)  **
  - **Description:** Grants permission to update the configuration of a router input in AWS Elemental MediaConnect
  - **Resource types (\*required):** [RouterInput\*](#list_mediaconnect-resource-RouterInput)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRouterNetworkInterface](https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateRouterNetworkInterface.html)  **
  - **Description:** Grants permission to updated the configuration of a router network interface in AWS Elemental MediaConnect
  - **Resource types (\*required):** [RouterNetworkInterface\*](#list_mediaconnect-resource-RouterNetworkInterface)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRouterOutput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateRouterOutput.html)  **
  - **Description:** Grants permission to update the configuration of a router output in AWS Elemental MediaConnect
  - **Resource types (\*required):** [RouterOutput\*](#list_mediaconnect-resource-RouterOutput)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Elemental MediaConnect
<a name="list_mediaconnect-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Bridge](https://docs.aws.amazon.com/mediaconnect/latest/ug/gateway-components-bridges.html)  | arn:${Partition}:mediaconnect:${Region}:${Account}:bridge:${BridgeId}:${BridgeName} |   | 
|  [Entitlement](https://docs.aws.amazon.com/mediaconnect/latest/ug/entitlements.html)  | arn:${Partition}:mediaconnect:${Region}:${Account}:entitlement:${FlowId}:${EntitlementName} | [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_) | 
|  [Flow](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows.html)  | arn:${Partition}:mediaconnect:${Region}:${Account}:flow:${FlowId}:${FlowName} | [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_) | 
|  [Gateway](https://docs.aws.amazon.com/mediaconnect/latest/ug/gateway.html)  | arn:${Partition}:mediaconnect:${Region}:${Account}:gateway:${GatewayId}:${GatewayName} |   | 
|  [GatewayInstance](https://docs.aws.amazon.com/mediaconnect/latest/ug/gateway-components-instances.html)  | arn:${Partition}:mediaconnect:${Region}:${Account}:gateway:${GatewayId}:${GatewayName}:instance:${InstanceId} |   | 
|  [MediaStream](https://docs.aws.amazon.com/mediaconnect/latest/ug/media-streams.html)  | arn:${Partition}:mediaconnect:${Region}:${Account}:flow:${FlowId}:${FlowName}/mediaStream/${MediaStreamName} | [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_) | 
|  [Offering](https://docs.aws.amazon.com/mediaconnect/latest/ug/offerings.html)  | arn:${Partition}:mediaconnect:${Region}:offering:${OfferingId} |   | 
|  [Output](https://docs.aws.amazon.com/mediaconnect/latest/ug/outputs.html)  | arn:${Partition}:mediaconnect:${Region}:${Account}:output:${OutputId}:${OutputName} | [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_) | 
|  [Reservation](https://docs.aws.amazon.com/mediaconnect/latest/ug/reservations.html)  | arn:${Partition}:mediaconnect:${Region}:${Account}:reservation:${ReservationId}:${ReservationName} |   | 
|  [RouterInput](https://docs.aws.amazon.com/mediaconnect/latest/ug/managing-router-io.html)  | arn:${Partition}:mediaconnect:${Region}:${Account}:routerInput:${RouterInputId} | [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_) | 
|  [RouterNetworkInterface](https://docs.aws.amazon.com/mediaconnect/latest/ug/managing-router-network-interfaces.html)  | arn:${Partition}:mediaconnect:${Region}:${Account}:routerNetworkInterface:${RouterNetworkInterfaceId} | [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_) | 
|  [RouterOutput](https://docs.aws.amazon.com/mediaconnect/latest/ug/managing-router-io.html)  | arn:${Partition}:mediaconnect:${Region}:${Account}:routerOutput:${RouterOutputId} | [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_) | 
|  [Source](https://docs.aws.amazon.com/mediaconnect/latest/ug/sources.html)  | arn:${Partition}:mediaconnect:${Region}:${Account}:source:${SourceId}:${SourceName} | [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_) | 
|  [VpcInterface](https://docs.aws.amazon.com/mediaconnect/latest/ug/vpc-interfaces.html)  | arn:${Partition}:mediaconnect:${Region}:${Account}:flow:${FlowId}:${FlowName}/vpcInterface/${VpcInterfaceName} | [aws:ResourceTag/${TagKey}](#list_mediaconnect-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Elemental MediaConnect
<a name="list_mediaconnect-policy-keys"></a>

AWS Elemental MediaConnect defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by tag keys that are passed in the request | ArrayOfString | 