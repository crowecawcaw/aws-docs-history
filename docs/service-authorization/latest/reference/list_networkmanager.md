

# Actions, resources, and condition keys for AWS Network Manager
<a name="list_networkmanager"></a>

AWS Network Manager (service prefix: `networkmanager`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/vpc/latest/tgw/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/networkmanager/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/vpc/latest/tgw/nm-security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/networkmanager/networkmanager.json) for this service.

**Topics**
+ [API operations defined by AWS Network Manager](#list_networkmanager-operations)
+ [Actions defined by AWS Network Manager](#list_networkmanager-actions-as-permissions)
+ [Resource types defined by AWS Network Manager](#list_networkmanager-resources-for-iam-policies)
+ [Condition keys for AWS Network Manager](#list_networkmanager-policy-keys)

## API operations defined by AWS Network Manager
<a name="list_networkmanager-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_networkmanager-actions-as-permissions).




- **   AcceptAttachment  **
  - **IAM action:**  [networkmanager:AcceptAttachment](#list_networkmanager-action-AcceptAttachment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateConnectPeer  **
  - **IAM action:**  [networkmanager:AssociateConnectPeer](#list_networkmanager-action-AssociateConnectPeer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateCustomerGateway  **
  - **IAM action:**  [networkmanager:AssociateCustomerGateway](#list_networkmanager-action-AssociateCustomerGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateLink  **
  - **IAM action:**  [networkmanager:AssociateLink](#list_networkmanager-action-AssociateLink) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateTransitGatewayConnectPeer  **
  - **IAM action:**  [networkmanager:AssociateTransitGatewayConnectPeer](#list_networkmanager-action-AssociateTransitGatewayConnectPeer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateConnectAttachment  **
  - **IAM action:**  [networkmanager:CreateConnectAttachment](#list_networkmanager-action-CreateConnectAttachment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [networkmanager:PutAttachmentRoutingPolicyLabel](#list_networkmanager-action-PutAttachmentRoutingPolicyLabel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [networkmanager:TagResource](#list_networkmanager-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateConnectPeer  **
  - **IAM action:**  [networkmanager:CreateConnectPeer](#list_networkmanager-action-CreateConnectPeer)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [networkmanager:TagResource](#list_networkmanager-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateConnection  **
  - **IAM action:**  [networkmanager:CreateConnection](#list_networkmanager-action-CreateConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [networkmanager:TagResource](#list_networkmanager-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCoreNetwork  **
  - **IAM action:**  [networkmanager:CreateCoreNetwork](#list_networkmanager-action-CreateCoreNetwork)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [networkmanager:TagResource](#list_networkmanager-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCoreNetworkPrefixListAssociation  **
  - **IAM action:**  [networkmanager:CreateCoreNetworkPrefixListAssociation](#list_networkmanager-action-CreateCoreNetworkPrefixListAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDevice  **
  - **IAM action:**  [networkmanager:CreateDevice](#list_networkmanager-action-CreateDevice)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [networkmanager:TagResource](#list_networkmanager-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDirectConnectGatewayAttachment  **
  - **IAM action:**  [networkmanager:CreateDirectConnectGatewayAttachment](#list_networkmanager-action-CreateDirectConnectGatewayAttachment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [networkmanager:PutAttachmentRoutingPolicyLabel](#list_networkmanager-action-PutAttachmentRoutingPolicyLabel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [networkmanager:TagResource](#list_networkmanager-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateGlobalNetwork  **
  - **IAM action:**  [networkmanager:CreateGlobalNetwork](#list_networkmanager-action-CreateGlobalNetwork)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [networkmanager:TagResource](#list_networkmanager-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateLink  **
  - **IAM action:**  [networkmanager:CreateLink](#list_networkmanager-action-CreateLink)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [networkmanager:TagResource](#list_networkmanager-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSite  **
  - **IAM action:**  [networkmanager:CreateSite](#list_networkmanager-action-CreateSite)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [networkmanager:TagResource](#list_networkmanager-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSiteToSiteVpnAttachment  **
  - **IAM action:**  [networkmanager:CreateSiteToSiteVpnAttachment](#list_networkmanager-action-CreateSiteToSiteVpnAttachment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [networkmanager:PutAttachmentRoutingPolicyLabel](#list_networkmanager-action-PutAttachmentRoutingPolicyLabel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [networkmanager:TagResource](#list_networkmanager-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateTransitGatewayPeering  **
  - **IAM action:**  [networkmanager:CreateTransitGatewayPeering](#list_networkmanager-action-CreateTransitGatewayPeering)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [networkmanager:TagResource](#list_networkmanager-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateTransitGatewayRouteTableAttachment  **
  - **IAM action:**  [networkmanager:CreateTransitGatewayRouteTableAttachment](#list_networkmanager-action-CreateTransitGatewayRouteTableAttachment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [networkmanager:PutAttachmentRoutingPolicyLabel](#list_networkmanager-action-PutAttachmentRoutingPolicyLabel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [networkmanager:TagResource](#list_networkmanager-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateVpcAttachment  **
  - **IAM action:**  [networkmanager:CreateVpcAttachment](#list_networkmanager-action-CreateVpcAttachment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [networkmanager:PutAttachmentRoutingPolicyLabel](#list_networkmanager-action-PutAttachmentRoutingPolicyLabel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [networkmanager:TagResource](#list_networkmanager-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAttachment  **
  - **IAM action:**  [networkmanager:DeleteAttachment](#list_networkmanager-action-DeleteAttachment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConnectPeer  **
  - **IAM action:**  [networkmanager:DeleteConnectPeer](#list_networkmanager-action-DeleteConnectPeer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConnection  **
  - **IAM action:**  [networkmanager:DeleteConnection](#list_networkmanager-action-DeleteConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCoreNetwork  **
  - **IAM action:**  [networkmanager:DeleteCoreNetwork](#list_networkmanager-action-DeleteCoreNetwork) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCoreNetworkPolicyVersion  **
  - **IAM action:**  [networkmanager:DeleteCoreNetworkPolicyVersion](#list_networkmanager-action-DeleteCoreNetworkPolicyVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCoreNetworkPrefixListAssociation  **
  - **IAM action:**  [networkmanager:DeleteCoreNetworkPrefixListAssociation](#list_networkmanager-action-DeleteCoreNetworkPrefixListAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDevice  **
  - **IAM action:**  [networkmanager:DeleteDevice](#list_networkmanager-action-DeleteDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGlobalNetwork  **
  - **IAM action:**  [networkmanager:DeleteGlobalNetwork](#list_networkmanager-action-DeleteGlobalNetwork) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLink  **
  - **IAM action:**  [networkmanager:DeleteLink](#list_networkmanager-action-DeleteLink) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePeering  **
  - **IAM action:**  [networkmanager:DeletePeering](#list_networkmanager-action-DeletePeering) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcePolicy  **
  - **IAM action:**  [networkmanager:DeleteResourcePolicy](#list_networkmanager-action-DeleteResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteSite  **
  - **IAM action:**  [networkmanager:DeleteSite](#list_networkmanager-action-DeleteSite) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterTransitGateway  **
  - **IAM action:**  [networkmanager:DeregisterTransitGateway](#list_networkmanager-action-DeregisterTransitGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeGlobalNetworks  **
  - **IAM action:**  [networkmanager:DescribeGlobalNetworks](#list_networkmanager-action-DescribeGlobalNetworks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DisassociateConnectPeer  **
  - **IAM action:**  [networkmanager:DisassociateConnectPeer](#list_networkmanager-action-DisassociateConnectPeer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateCustomerGateway  **
  - **IAM action:**  [networkmanager:DisassociateCustomerGateway](#list_networkmanager-action-DisassociateCustomerGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateLink  **
  - **IAM action:**  [networkmanager:DisassociateLink](#list_networkmanager-action-DisassociateLink) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateTransitGatewayConnectPeer  **
  - **IAM action:**  [networkmanager:DisassociateTransitGatewayConnectPeer](#list_networkmanager-action-DisassociateTransitGatewayConnectPeer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ExecuteCoreNetworkChangeSet  **
  - **IAM action:**  [networkmanager:ExecuteCoreNetworkChangeSet](#list_networkmanager-action-ExecuteCoreNetworkChangeSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetConnectAttachment  **
  - **IAM action:**  [networkmanager:GetConnectAttachment](#list_networkmanager-action-GetConnectAttachment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConnectPeer  **
  - **IAM action:**  [networkmanager:GetConnectPeer](#list_networkmanager-action-GetConnectPeer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConnectPeerAssociations  **
  - **IAM action:**  [networkmanager:GetConnectPeerAssociations](#list_networkmanager-action-GetConnectPeerAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConnections  **
  - **IAM action:**  [networkmanager:GetConnections](#list_networkmanager-action-GetConnections) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetCoreNetwork  **
  - **IAM action:**  [networkmanager:GetCoreNetwork](#list_networkmanager-action-GetCoreNetwork) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCoreNetworkChangeEvents  **
  - **IAM action:**  [networkmanager:GetCoreNetworkChangeEvents](#list_networkmanager-action-GetCoreNetworkChangeEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCoreNetworkChangeSet  **
  - **IAM action:**  [networkmanager:GetCoreNetworkChangeSet](#list_networkmanager-action-GetCoreNetworkChangeSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCoreNetworkPolicy  **
  - **IAM action:**  [networkmanager:GetCoreNetworkPolicy](#list_networkmanager-action-GetCoreNetworkPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCustomerGatewayAssociations  **
  - **IAM action:**  [networkmanager:GetCustomerGatewayAssociations](#list_networkmanager-action-GetCustomerGatewayAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetDevices  **
  - **IAM action:**  [networkmanager:GetDevices](#list_networkmanager-action-GetDevices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetDirectConnectGatewayAttachment  **
  - **IAM action:**  [networkmanager:GetDirectConnectGatewayAttachment](#list_networkmanager-action-GetDirectConnectGatewayAttachment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLinkAssociations  **
  - **IAM action:**  [networkmanager:GetLinkAssociations](#list_networkmanager-action-GetLinkAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetLinks  **
  - **IAM action:**  [networkmanager:GetLinks](#list_networkmanager-action-GetLinks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetNetworkResourceCounts  **
  - **IAM action:**  [networkmanager:GetNetworkResourceCounts](#list_networkmanager-action-GetNetworkResourceCounts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetNetworkResourceRelationships  **
  - **IAM action:**  [networkmanager:GetNetworkResourceRelationships](#list_networkmanager-action-GetNetworkResourceRelationships) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetNetworkResources  **
  - **IAM action:**  [networkmanager:GetNetworkResources](#list_networkmanager-action-GetNetworkResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetNetworkRoutes  **
  - **IAM action:**  [networkmanager:GetNetworkRoutes](#list_networkmanager-action-GetNetworkRoutes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetNetworkTelemetry  **
  - **IAM action:**  [networkmanager:GetNetworkTelemetry](#list_networkmanager-action-GetNetworkTelemetry) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePolicy  **
  - **IAM action:**  [networkmanager:GetResourcePolicy](#list_networkmanager-action-GetResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRouteAnalysis  **
  - **IAM action:**  [networkmanager:GetRouteAnalysis](#list_networkmanager-action-GetRouteAnalysis) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSiteToSiteVpnAttachment  **
  - **IAM action:**  [networkmanager:GetSiteToSiteVpnAttachment](#list_networkmanager-action-GetSiteToSiteVpnAttachment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSites  **
  - **IAM action:**  [networkmanager:GetSites](#list_networkmanager-action-GetSites) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetTransitGatewayConnectPeerAssociations  **
  - **IAM action:**  [networkmanager:GetTransitGatewayConnectPeerAssociations](#list_networkmanager-action-GetTransitGatewayConnectPeerAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetTransitGatewayPeering  **
  - **IAM action:**  [networkmanager:GetTransitGatewayPeering](#list_networkmanager-action-GetTransitGatewayPeering) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTransitGatewayRegistrations  **
  - **IAM action:**  [networkmanager:GetTransitGatewayRegistrations](#list_networkmanager-action-GetTransitGatewayRegistrations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetTransitGatewayRouteTableAttachment  **
  - **IAM action:**  [networkmanager:GetTransitGatewayRouteTableAttachment](#list_networkmanager-action-GetTransitGatewayRouteTableAttachment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetVpcAttachment  **
  - **IAM action:**  [networkmanager:GetVpcAttachment](#list_networkmanager-action-GetVpcAttachment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAttachmentRoutingPolicyAssociations  **
  - **IAM action:**  [networkmanager:ListAttachmentRoutingPolicyAssociations](#list_networkmanager-action-ListAttachmentRoutingPolicyAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAttachments  **
  - **IAM action:**  [networkmanager:ListAttachments](#list_networkmanager-action-ListAttachments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConnectPeers  **
  - **IAM action:**  [networkmanager:ListConnectPeers](#list_networkmanager-action-ListConnectPeers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCoreNetworkPolicyVersions  **
  - **IAM action:**  [networkmanager:ListCoreNetworkPolicyVersions](#list_networkmanager-action-ListCoreNetworkPolicyVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCoreNetworkPrefixListAssociations  **
  - **IAM action:**  [networkmanager:ListCoreNetworkPrefixListAssociations](#list_networkmanager-action-ListCoreNetworkPrefixListAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCoreNetworkRoutingInformation  **
  - **IAM action:**  [networkmanager:ListCoreNetworkRoutingInformation](#list_networkmanager-action-ListCoreNetworkRoutingInformation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCoreNetworks  **
  - **IAM action:**  [networkmanager:ListCoreNetworks](#list_networkmanager-action-ListCoreNetworks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOrganizationServiceAccessStatus  **
  - **IAM action:**  [networkmanager:ListOrganizationServiceAccessStatus](#list_networkmanager-action-ListOrganizationServiceAccessStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPeerings  **
  - **IAM action:**  [networkmanager:ListPeerings](#list_networkmanager-action-ListPeerings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [networkmanager:ListTagsForResource](#list_networkmanager-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutAttachmentRoutingPolicyLabel  **
  - **IAM action:**  [networkmanager:PutAttachmentRoutingPolicyLabel](#list_networkmanager-action-PutAttachmentRoutingPolicyLabel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutCoreNetworkPolicy  **
  - **IAM action:**  [networkmanager:PutCoreNetworkPolicy](#list_networkmanager-action-PutCoreNetworkPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutResourcePolicy  **
  - **IAM action:**  [networkmanager:PutResourcePolicy](#list_networkmanager-action-PutResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   RegisterTransitGateway  **
  - **IAM action:**  [networkmanager:RegisterTransitGateway](#list_networkmanager-action-RegisterTransitGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RejectAttachment  **
  - **IAM action:**  [networkmanager:RejectAttachment](#list_networkmanager-action-RejectAttachment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveAttachmentRoutingPolicyLabel  **
  - **IAM action:**  [networkmanager:RemoveAttachmentRoutingPolicyLabel](#list_networkmanager-action-RemoveAttachmentRoutingPolicyLabel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RestoreCoreNetworkPolicyVersion  **
  - **IAM action:**  [networkmanager:RestoreCoreNetworkPolicyVersion](#list_networkmanager-action-RestoreCoreNetworkPolicyVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartOrganizationServiceAccessUpdate  **
  - **IAM action:**  [networkmanager:StartOrganizationServiceAccessUpdate](#list_networkmanager-action-StartOrganizationServiceAccessUpdate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   StartRouteAnalysis  **
  - **IAM action:**  [networkmanager:StartRouteAnalysis](#list_networkmanager-action-StartRouteAnalysis) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [networkmanager:TagResource](#list_networkmanager-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [networkmanager:UntagResource](#list_networkmanager-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateConnection  **
  - **IAM action:**  [networkmanager:UpdateConnection](#list_networkmanager-action-UpdateConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCoreNetwork  **
  - **IAM action:**  [networkmanager:UpdateCoreNetwork](#list_networkmanager-action-UpdateCoreNetwork) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDevice  **
  - **IAM action:**  [networkmanager:UpdateDevice](#list_networkmanager-action-UpdateDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDirectConnectGatewayAttachment  **
  - **IAM action:**  [networkmanager:UpdateDirectConnectGatewayAttachment](#list_networkmanager-action-UpdateDirectConnectGatewayAttachment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateGlobalNetwork  **
  - **IAM action:**  [networkmanager:UpdateGlobalNetwork](#list_networkmanager-action-UpdateGlobalNetwork) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLink  **
  - **IAM action:**  [networkmanager:UpdateLink](#list_networkmanager-action-UpdateLink) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateNetworkResourceMetadata  **
  - **IAM action:**  [networkmanager:UpdateNetworkResourceMetadata](#list_networkmanager-action-UpdateNetworkResourceMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSite  **
  - **IAM action:**  [networkmanager:UpdateSite](#list_networkmanager-action-UpdateSite) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateVpcAttachment  **
  - **IAM action:**  [networkmanager:UpdateVpcAttachment](#list_networkmanager-action-UpdateVpcAttachment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Network Manager
<a name="list_networkmanager-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptAttachment](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_AcceptAttachment.html)  **
  - **Description:** Grants permission to accept creation of an attachment between a source and destination in a core network
  - **Resource types (\*required):** [attachment\*](#list_networkmanager-resource-attachment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateConnectPeer](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_AssociateConnectPeer.html)  **
  - **Description:** Grants permission to associate a Connect Peer
  - **Resource types (\*required):** [device\*](#list_networkmanager-resource-device) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateCustomerGateway](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_AssociateCustomerGateway.html)  **
  - **Description:** Grants permission to associate a customer gateway to a device
  - **Resource types (\*required):** [device\*](#list_networkmanager-resource-device) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[networkmanager:cgwArn](#list_networkmanager-networkmanager_cgwArn)
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[networkmanager:cgwArn](#list_networkmanager-networkmanager_cgwArn)
  - **Resource types (\*required):** [link](#list_networkmanager-resource-link) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[networkmanager:cgwArn](#list_networkmanager-networkmanager_cgwArn)
  - **Access level:** Write

- **   [AssociateLink](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_AssociateLink.html)  **
  - **Description:** Grants permission to associate a link to a device
  - **Resource types (\*required):** [device\*](#list_networkmanager-resource-device) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [link\*](#list_networkmanager-resource-link) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateTransitGatewayConnectPeer](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_AssociateTransitGatewayConnectPeer.html)  **
  - **Description:** Grants permission to associate a transit gateway connect peer to a device
  - **Resource types (\*required):** [device\*](#list_networkmanager-resource-device) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[networkmanager:tgwConnectPeerArn](#list_networkmanager-networkmanager_tgwConnectPeerArn)
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[networkmanager:tgwConnectPeerArn](#list_networkmanager-networkmanager_tgwConnectPeerArn)
  - **Resource types (\*required):** [link](#list_networkmanager-resource-link) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[networkmanager:tgwConnectPeerArn](#list_networkmanager-networkmanager_tgwConnectPeerArn)
  - **Access level:** Write

- **   [CreateConnectAttachment](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CreateConnectAttachment.html)  **
  - **Description:** Grants permission to create a Connect attachment
  - **Resource types (\*required):** [attachment\*](#list_networkmanager-resource-attachment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)
  - **Resource types (\*required):** [core-network\*](#list_networkmanager-resource-core-network) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)
  - **Access level:** Write

- **   [CreateConnectPeer](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CreateConnectPeer.html)  **
  - **Description:** Grants permission to create a Connect Peer connection
  - **Resource types (\*required):** [attachment\*](#list_networkmanager-resource-attachment)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)
  - **Access level:** Write

- **   [CreateConnection](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CreateConnection.html)  **
  - **Description:** Grants permission to create a new connection
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCoreNetwork](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CreateCoreNetwork.html)  **
  - **Description:** Grants permission to create a new core network
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCoreNetworkPrefixListAssociation](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CreateCoreNetworkPrefixListAssociation.html)  **
  - **Description:** Grants permission to create a prefix list core network association
  - **Resource types (\*required):** [core-network\*](#list_networkmanager-resource-core-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDevice](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CreateDevice.html)  **
  - **Description:** Grants permission to create a new device
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDirectConnectGatewayAttachment](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CreateDirectConnectGatewayAttachment.html)  **
  - **Description:** Grants permission to create a Direct Connect gateway attachment
  - **Resource types (\*required):** [core-network\*](#list_networkmanager-resource-core-network)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)<br />[networkmanager:directConnectGatewayArn](#list_networkmanager-networkmanager_directConnectGatewayArn)<br />[networkmanager:edgeLocations](#list_networkmanager-networkmanager_edgeLocations)
  - **Access level:** Write

- **   [CreateGlobalNetwork](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CreateGlobalNetwork.html)  **
  - **Description:** Grants permission to create a new global network
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkmanager-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLink](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CreateLink.html)  **
  - **Description:** Grants permission to create a new link
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)
  - **Resource types (\*required):** [site](#list_networkmanager-resource-site) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSite](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CreateSite.html)  **
  - **Description:** Grants permission to create a new site
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSiteToSiteVpnAttachment](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CreateSiteToSiteVpnAttachment.html)  **
  - **Description:** Grants permission to create a site-to-site VPN attachment
  - **Resource types (\*required):** [core-network\*](#list_networkmanager-resource-core-network)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)<br />[networkmanager:vpnConnectionArn](#list_networkmanager-networkmanager_vpnConnectionArn)
  - **Access level:** Write

- **   [CreateTransitGatewayPeering](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CreateTransitGatewayPeering.html)  **
  - **Description:** Grants permission to create a Transit Gateway peering
  - **Resource types (\*required):** [core-network\*](#list_networkmanager-resource-core-network)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)<br />[networkmanager:tgwArn](#list_networkmanager-networkmanager_tgwArn)
  - **Access level:** Write

- **   [CreateTransitGatewayRouteTableAttachment](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CreateTransitGatewayRouteTableAttachment.html)  **
  - **Description:** Grants permission to create a TGW RTB attachment
  - **Resource types (\*required):** [peering\*](#list_networkmanager-resource-peering)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)<br />[networkmanager:tgwRtbArn](#list_networkmanager-networkmanager_tgwRtbArn)
  - **Access level:** Write

- **   [CreateVpcAttachment](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CreateVpcAttachment.html)  **
  - **Description:** Grants permission to create a VPC attachment
  - **Resource types (\*required):** [core-network\*](#list_networkmanager-resource-core-network)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)<br />[networkmanager:subnetArns](#list_networkmanager-networkmanager_subnetArns)<br />[networkmanager:vpcArn](#list_networkmanager-networkmanager_vpcArn)
  - **Access level:** Write

- **   [DeleteAttachment](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_DeleteAttachment.html)  **
  - **Description:** Grants permission to delete an attachment
  - **Resource types (\*required):** [attachment\*](#list_networkmanager-resource-attachment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConnectPeer](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_DeleteConnectPeer.html)  **
  - **Description:** Grants permission to delete a Connect Peer
  - **Resource types (\*required):** [connect-peer\*](#list_networkmanager-resource-connect-peer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConnection](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_DeleteConnection.html)  **
  - **Description:** Grants permission to delete a connection
  - **Resource types (\*required):** [connection\*](#list_networkmanager-resource-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCoreNetwork](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_DeleteCoreNetwork.html)  **
  - **Description:** Grants permission to delete a core network
  - **Resource types (\*required):** [core-network\*](#list_networkmanager-resource-core-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCoreNetworkPolicyVersion](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_DeleteCoreNetworkPolicyVersion.html)  **
  - **Description:** Grants permission to delete the core network policy version
  - **Resource types (\*required):** [core-network\*](#list_networkmanager-resource-core-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCoreNetworkPrefixListAssociation](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_DeleteCoreNetworkPrefixListAssociation.html)  **
  - **Description:** Grants permission to delete a prefix list core network association
  - **Resource types (\*required):** [core-network\*](#list_networkmanager-resource-core-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDevice](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_DeleteDevice.html)  **
  - **Description:** Grants permission to delete a device
  - **Resource types (\*required):** [device\*](#list_networkmanager-resource-device) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteGlobalNetwork](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_DeleteGlobalNetwork.html)  **
  - **Description:** Grants permission to delete a global network
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLink](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_DeleteLink.html)  **
  - **Description:** Grants permission to delete a link
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [link\*](#list_networkmanager-resource-link) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePeering](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_DeletePeering.html)  **
  - **Description:** Grants permission to delete a peering
  - **Resource types (\*required):** [peering\*](#list_networkmanager-resource-peering)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to delete a resource
  - **Resource types (\*required):** [core-network\*](#list_networkmanager-resource-core-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteSite](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_DeleteSite.html)  **
  - **Description:** Grants permission to delete a site
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [site\*](#list_networkmanager-resource-site) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterTransitGateway](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_DeregisterTransitGateway.html)  **
  - **Description:** Grants permission to deregister a transit gateway from a global network
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[networkmanager:tgwArn](#list_networkmanager-networkmanager_tgwArn)
  - **Access level:** Write

- **   [DescribeGlobalNetworks](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_DescribeGlobalNetworks.html)  **
  - **Description:** Grants permission to describe global networks
  - **Resource types (\*required):** [global-network](#list_networkmanager-resource-global-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DisassociateConnectPeer](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_DisassociateConnectPeer.html)  **
  - **Description:** Grants permission to disassociate a Connect Peer
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateCustomerGateway](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_DisassociateCustomerGateway.html)  **
  - **Description:** Grants permission to disassociate a customer gateway from a device
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[networkmanager:cgwArn](#list_networkmanager-networkmanager_cgwArn)
  - **Access level:** Write

- **   [DisassociateLink](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_DisassociateLink.html)  **
  - **Description:** Grants permission to disassociate a link from a device
  - **Resource types (\*required):** [device\*](#list_networkmanager-resource-device) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [link\*](#list_networkmanager-resource-link) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateTransitGatewayConnectPeer](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_DisassociateTransitGatewayConnectPeer.html)  **
  - **Description:** Grants permission to disassociate a transit gateway connect peer from a device
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[networkmanager:tgwConnectPeerArn](#list_networkmanager-networkmanager_tgwConnectPeerArn)
  - **Access level:** Write

- **   [ExecuteCoreNetworkChangeSet](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_ExecuteCoreNetworkChangeSet.html)  **
  - **Description:** Grants permission to apply changes to the core network
  - **Resource types (\*required):** [core-network\*](#list_networkmanager-resource-core-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetConnectAttachment](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetConnectAttachment.html)  **
  - **Description:** Grants permission to retrieve a Connect attachment
  - **Resource types (\*required):** [attachment\*](#list_networkmanager-resource-attachment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetConnectPeer](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetConnectPeer.html)  **
  - **Description:** Grants permission to retrieve a Connect Peer
  - **Resource types (\*required):** [connect-peer\*](#list_networkmanager-resource-connect-peer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetConnectPeerAssociations](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetConnectPeerAssociations.html)  **
  - **Description:** Grants permission to describe Connect Peer associations
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetConnections](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetConnections.html)  **
  - **Description:** Grants permission to describe connections
  - **Resource types (\*required):** [connection](#list_networkmanager-resource-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetCoreNetwork](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetCoreNetwork.html)  **
  - **Description:** Grants permission to retrieve a core network
  - **Resource types (\*required):** [core-network\*](#list_networkmanager-resource-core-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCoreNetworkChangeEvents](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetCoreNetworkChangeEvents.html)  **
  - **Description:** Grants permission to retrieve a list of core network change events
  - **Resource types (\*required):** [core-network\*](#list_networkmanager-resource-core-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCoreNetworkChangeSet](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetCoreNetworkChangeSet.html)  **
  - **Description:** Grants permission to retrieve a list of core network change sets
  - **Resource types (\*required):** [core-network\*](#list_networkmanager-resource-core-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCoreNetworkPolicy](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetCoreNetworkPolicy.html)  **
  - **Description:** Grants permission to retrieve core network policy
  - **Resource types (\*required):** [core-network\*](#list_networkmanager-resource-core-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCustomerGatewayAssociations](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetCustomerGatewayAssociations.html)  **
  - **Description:** Grants permission to describe customer gateway associations
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetDevices](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetDevices.html)  **
  - **Description:** Grants permission to describe devices
  - **Resource types (\*required):** [device](#list_networkmanager-resource-device) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetDirectConnectGatewayAttachment](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetDirectConnectGatewayAttachment.html)  **
  - **Description:** Grants permission to retrieve a Direct Connect gateway attachment
  - **Resource types (\*required):** [attachment\*](#list_networkmanager-resource-attachment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLinkAssociations](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetLinkAssociations.html)  **
  - **Description:** Grants permission to describe link associations
  - **Resource types (\*required):** [device](#list_networkmanager-resource-device) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [link](#list_networkmanager-resource-link) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetLinks](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetLinks.html)  **
  - **Description:** Grants permission to describe links
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [link](#list_networkmanager-resource-link) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetNetworkResourceCounts](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetNetworkResourceCounts.html)  **
  - **Description:** Grants permission to return the number of resources for a global network grouped by type
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetNetworkResourceRelationships](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetNetworkResourceRelationships.html)  **
  - **Description:** Grants permission to retrieve related resources for a resource within the global network
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetNetworkResources](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetNetworkResources.html)  **
  - **Description:** Grants permission to retrieve a global network resource
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetNetworkRoutes](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetNetworkRoutes.html)  **
  - **Description:** Grants permission to retrieve routes for a route table within the global network
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetNetworkTelemetry](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetNetworkTelemetry.html)  **
  - **Description:** Grants permission to retrieve network telemetry objects for the global network
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResourcePolicy](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetResourcePolicy.html)  **
  - **Description:** Grants permission to retrieve a resource policy
  - **Resource types (\*required):** [core-network\*](#list_networkmanager-resource-core-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRouteAnalysis](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetRouteAnalysis.html)  **
  - **Description:** Grants permission to retrieve a route analysis configuration and result
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSiteToSiteVpnAttachment](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetSiteToSiteVpnAttachment.html)  **
  - **Description:** Grants permission to retrieve a site-to-site VPN attachment
  - **Resource types (\*required):** [attachment\*](#list_networkmanager-resource-attachment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSites](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetSites.html)  **
  - **Description:** Grants permission to describe global networks
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [site](#list_networkmanager-resource-site) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetTransitGatewayConnectPeerAssociations](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetTransitGatewayConnectPeerAssociations.html)  **
  - **Description:** Grants permission to describe transit gateway connect peer associations
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetTransitGatewayPeering](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetTransitGatewayPeering.html)  **
  - **Description:** Grants permission to retrieve a Transit Gateway peering
  - **Resource types (\*required):** [peering\*](#list_networkmanager-resource-peering)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTransitGatewayRegistrations](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetTransitGatewayRegistrations.html)  **
  - **Description:** Grants permission to describe transit gateway registrations
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetTransitGatewayRouteTableAttachment](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetTransitGatewayRouteTableAttachment.html)  **
  - **Description:** Grants permission to retrieve a TGW RTB attachment
  - **Resource types (\*required):** [attachment\*](#list_networkmanager-resource-attachment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetVpcAttachment](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetVpcAttachment.html)  **
  - **Description:** Grants permission to retrieve a VPC attachment
  - **Resource types (\*required):** [attachment\*](#list_networkmanager-resource-attachment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAttachmentRoutingPolicyAssociations](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_ListAttachmentRoutingPolicyAssociations.html)  **
  - **Description:** Grants permission to list all routing policies associated to core network attachments
  - **Resource types (\*required):** [core-network\*](#list_networkmanager-resource-core-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAttachments](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_ListAttachments.html)  **
  - **Description:** Grants permission to describe attachments
  - **Resource types (\*required):** [attachment\*](#list_networkmanager-resource-attachment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListConnectPeers](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_ListConnectPeers.html)  **
  - **Description:** Grants permission to describe Connect Peers
  - **Resource types (\*required):** [connect-peer\*](#list_networkmanager-resource-connect-peer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCoreNetworkPolicyVersions](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_ListCoreNetworkPolicyVersions.html)  **
  - **Description:** Grants permission to list core network policy versions
  - **Resource types (\*required):** [core-network\*](#list_networkmanager-resource-core-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCoreNetworkPrefixListAssociations](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_ListCoreNetworkPrefixListAssociations.html)  **
  - **Description:** Grants permission to list core network prefix list associaitons
  - **Resource types (\*required):** [core-network\*](#list_networkmanager-resource-core-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCoreNetworkRoutingInformation](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_ListCoreNetworkRoutingInformation.html)  **
  - **Description:** Grants permission to list core network routing information
  - **Resource types (\*required):** [core-network\*](#list_networkmanager-resource-core-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCoreNetworks](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_ListCoreNetworks.html)  **
  - **Description:** Grants permission to list core networks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOrganizationServiceAccessStatus](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_ListOrganizationServiceAccessStatus.html)  **
  - **Description:** Grants permission to list organization service access status
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPeerings](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_ListPeerings.html)  **
  - **Description:** Grants permission to describe peerings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a Network Manager resource
  - **Resource types (\*required):** [attachment](#list_networkmanager-resource-attachment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [connect-peer](#list_networkmanager-resource-connect-peer) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [connection](#list_networkmanager-resource-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [core-network](#list_networkmanager-resource-core-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [device](#list_networkmanager-resource-device) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [global-network](#list_networkmanager-resource-global-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [link](#list_networkmanager-resource-link) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [peering](#list_networkmanager-resource-peering) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [site](#list_networkmanager-resource-site) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutAttachmentRoutingPolicyLabel](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_PutAttachmentRoutingPolicyLabel.html)  **
  - **Description:** Grants permission to put an attachment routing policy label
  - **Resource types (\*required):** [attachment\*](#list_networkmanager-resource-attachment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [core-network\*](#list_networkmanager-resource-core-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutCoreNetworkPolicy](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_PutCoreNetworkPolicy.html)  **
  - **Description:** Grants permission to create a core network policy
  - **Resource types (\*required):** [core-network\*](#list_networkmanager-resource-core-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutResourcePolicy](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_PutResourcePolicy.html)  **
  - **Description:** Grants permission to create or update a resource policy
  - **Resource types (\*required):** [core-network\*](#list_networkmanager-resource-core-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [RegisterTransitGateway](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_RegisterTransitGateway.html)  **
  - **Description:** Grants permission to register a transit gateway to a global network
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[networkmanager:tgwArn](#list_networkmanager-networkmanager_tgwArn)
  - **Access level:** Write

- **   [RejectAttachment](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_RejectAttachment.html)  **
  - **Description:** Grants permission to reject attachment request
  - **Resource types (\*required):** [attachment\*](#list_networkmanager-resource-attachment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RemoveAttachmentRoutingPolicyLabel](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_RemoveAttachmentRoutingPolicyLabel.html)  **
  - **Description:** Grants permission to remove an attachment routing policy label
  - **Resource types (\*required):** [attachment\*](#list_networkmanager-resource-attachment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [core-network\*](#list_networkmanager-resource-core-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RestoreCoreNetworkPolicyVersion](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_RestoreCoreNetworkPolicyVersion.html)  **
  - **Description:** Grants permission to restore the core network policy to a previous version
  - **Resource types (\*required):** [core-network\*](#list_networkmanager-resource-core-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartOrganizationServiceAccessUpdate](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_StartOrganizationServiceAccessUpdate.html)  **
  - **Description:** Grants permission to start organization service access update
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [StartRouteAnalysis](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_StartRouteAnalysis.html)  **
  - **Description:** Grants permission to start a route analysis and stores analysis configuration
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a Network Manager resource
  - **Resource types (\*required):** [attachment](#list_networkmanager-resource-attachment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)
  - **Resource types (\*required):** [connect-peer](#list_networkmanager-resource-connect-peer) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)
  - **Resource types (\*required):** [connection](#list_networkmanager-resource-connection) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)
  - **Resource types (\*required):** [core-network](#list_networkmanager-resource-core-network) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)
  - **Resource types (\*required):** [device](#list_networkmanager-resource-device) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)
  - **Resource types (\*required):** [global-network](#list_networkmanager-resource-global-network) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)
  - **Resource types (\*required):** [link](#list_networkmanager-resource-link) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)
  - **Resource types (\*required):** [peering](#list_networkmanager-resource-peering) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)
  - **Resource types (\*required):** [site](#list_networkmanager-resource-site) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a Network Manager resource
  - **Resource types (\*required):** [attachment](#list_networkmanager-resource-attachment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)
  - **Resource types (\*required):** [connect-peer](#list_networkmanager-resource-connect-peer) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)
  - **Resource types (\*required):** [connection](#list_networkmanager-resource-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)
  - **Resource types (\*required):** [core-network](#list_networkmanager-resource-core-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)
  - **Resource types (\*required):** [device](#list_networkmanager-resource-device) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)
  - **Resource types (\*required):** [global-network](#list_networkmanager-resource-global-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)
  - **Resource types (\*required):** [link](#list_networkmanager-resource-link) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)
  - **Resource types (\*required):** [peering](#list_networkmanager-resource-peering) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)
  - **Resource types (\*required):** [site](#list_networkmanager-resource-site) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateConnection](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_UpdateConnection.html)  **
  - **Description:** Grants permission to update a connection
  - **Resource types (\*required):** [connection\*](#list_networkmanager-resource-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCoreNetwork](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_UpdateCoreNetwork.html)  **
  - **Description:** Grants permission to update a core network
  - **Resource types (\*required):** [core-network\*](#list_networkmanager-resource-core-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDevice](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_UpdateDevice.html)  **
  - **Description:** Grants permission to update a device
  - **Resource types (\*required):** [device\*](#list_networkmanager-resource-device) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDirectConnectGatewayAttachment](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_UpdateDirectConnectGatewayAttachment.html)  **
  - **Description:** Grants permission to update a Direct Connect gateway attachment
  - **Resource types (\*required):** [attachment\*](#list_networkmanager-resource-attachment)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)<br />[networkmanager:edgeLocations](#list_networkmanager-networkmanager_edgeLocations)
  - **Access level:** Write

- **   [UpdateGlobalNetwork](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_UpdateGlobalNetwork.html)  **
  - **Description:** Grants permission to update a global network
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateLink](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_UpdateLink.html)  **
  - **Description:** Grants permission to update a link
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [link\*](#list_networkmanager-resource-link) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateNetworkResourceMetadata](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_UpdateNetworkResourceMetadata.html)  **
  - **Description:** Grants permission to add or update metadata key/value pairs on network resource
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSite](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_UpdateSite.html)  **
  - **Description:** Grants permission to update a site
  - **Resource types (\*required):** [global-network\*](#list_networkmanager-resource-global-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [site\*](#list_networkmanager-resource-site) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateVpcAttachment](https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_UpdateVpcAttachment.html)  **
  - **Description:** Grants permission to update a VPC attachment
  - **Resource types (\*required):** [attachment\*](#list_networkmanager-resource-attachment)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_networkmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_networkmanager-aws_TagKeys)<br />[networkmanager:subnetArns](#list_networkmanager-networkmanager_subnetArns)
  - **Access level:** Write



## Resource types defined by AWS Network Manager
<a name="list_networkmanager-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [attachment](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-network-manager.html)  | arn:${Partition}:networkmanager::${Account}:attachment/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_) | 
|  [connect-peer](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-network-manager.html)  | arn:${Partition}:networkmanager::${Account}:connect-peer/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_) | 
|  [connection](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-network-manager.html)  | arn:${Partition}:networkmanager::${Account}:connection/${GlobalNetworkId}/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_) | 
|  [core-network](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-network-manager.html)  | arn:${Partition}:networkmanager::${Account}:core-network/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_) | 
|  [device](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-network-manager.html)  | arn:${Partition}:networkmanager::${Account}:device/${GlobalNetworkId}/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_) | 
|  [global-network](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-network-manager.html)  | arn:${Partition}:networkmanager::${Account}:global-network/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_) | 
|  [link](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-network-manager.html)  | arn:${Partition}:networkmanager::${Account}:link/${GlobalNetworkId}/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_) | 
|  [peering](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-network-manager.html)  | arn:${Partition}:networkmanager::${Account}:peering/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_) | 
|  [site](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-network-manager.html)  | arn:${Partition}:networkmanager::${Account}:site/${GlobalNetworkId}/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_networkmanager-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Network Manager
<a name="list_networkmanager-policy-keys"></a>

AWS Network Manager defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [networkmanager:cgwArn](https://docs.aws.amazon.com/vpc/latest/tgw/nm-security-iam.html)  | Filters access by which customer gateways can be associated or disassociated | ARN | 
|   [networkmanager:directConnectGatewayArn](https://docs.aws.amazon.com/vpc/latest/tgw/nm-security-iam.html)  | Filters access by which Direct Connect gateway can be used to a create/update attachment | ARN | 
|   [networkmanager:edgeLocations](https://docs.aws.amazon.com/vpc/latest/tgw/nm-security-iam.html)  | Filters access by which edge locations can be added or removed from a Direct Connect gateway attachment | ArrayOfString | 
|   [networkmanager:subnetArns](https://docs.aws.amazon.com/vpc/latest/tgw/nm-security-iam.html)  | Filters access by which VPC subnets can be added or removed from a VPC attachment | ArrayOfARN | 
|   [networkmanager:tgwArn](https://docs.aws.amazon.com/vpc/latest/tgw/nm-security-iam.html)  | Filters access by which transit gateways can be registered, deregistered, or peered | ARN | 
|   [networkmanager:tgwConnectPeerArn](https://docs.aws.amazon.com/vpc/latest/tgw/nm-security-iam.html)  | Filters access by which transit gateway connect peers can be associated or disassociated | ARN | 
|   [networkmanager:tgwRtbArn](https://docs.aws.amazon.com/vpc/latest/tgw/nm-security-iam.html)  | Filters access by which Transit Gateway Route Table can be used to create an attachment | ARN | 
|   [networkmanager:vpcArn](https://docs.aws.amazon.com/vpc/latest/tgw/nm-security-iam.html)  | Filters access by which VPC can be used to a create/update attachment | ARN | 
|   [networkmanager:vpnConnectionArn](https://docs.aws.amazon.com/vpc/latest/tgw/nm-security-iam.html)  | Filters access by which Site-to-Site VPN can be used to a create/update attachment | ARN | 