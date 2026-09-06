

# Actions, resources, and condition keys for AWS Direct Connect
<a name="list_directconnect"></a>

AWS Direct Connect (service prefix: `directconnect`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/directconnect/latest/UserGuide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/directconnect/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/directconnect/latest/UserGuide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/directconnect/directconnect.json) for this service.

**Topics**
+ [API operations defined by AWS Direct Connect](#list_directconnect-operations)
+ [Actions defined by AWS Direct Connect](#list_directconnect-actions-as-permissions)
+ [Resource types defined by AWS Direct Connect](#list_directconnect-resources-for-iam-policies)
+ [Condition keys for AWS Direct Connect](#list_directconnect-policy-keys)

## API operations defined by AWS Direct Connect
<a name="list_directconnect-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_directconnect-actions-as-permissions).




- **   AcceptDirectConnectGatewayAssociationProposal  **
  - **IAM action:**  [directconnect:AcceptDirectConnectGatewayAssociationProposal](#list_directconnect-action-AcceptDirectConnectGatewayAssociationProposal) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AllocateConnectionOnInterconnect  **
  - **IAM action:**  [directconnect:AllocateConnectionOnInterconnect](#list_directconnect-action-AllocateConnectionOnInterconnect) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AllocateHostedConnection  **
  - **IAM action:**  [directconnect:AllocateHostedConnection](#list_directconnect-action-AllocateHostedConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [directconnect:TagResource](#list_directconnect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   AllocatePrivateVirtualInterface  **
  - **IAM action:**  [directconnect:AllocatePrivateVirtualInterface](#list_directconnect-action-AllocatePrivateVirtualInterface)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [directconnect:TagResource](#list_directconnect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   AllocatePublicVirtualInterface  **
  - **IAM action:**  [directconnect:AllocatePublicVirtualInterface](#list_directconnect-action-AllocatePublicVirtualInterface)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [directconnect:TagResource](#list_directconnect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   AllocateTransitVirtualInterface  **
  - **IAM action:**  [directconnect:AllocateTransitVirtualInterface](#list_directconnect-action-AllocateTransitVirtualInterface)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [directconnect:TagResource](#list_directconnect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   AssociateConnectionWithLag  **
  - **IAM action:**  [directconnect:AssociateConnectionWithLag](#list_directconnect-action-AssociateConnectionWithLag) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateHostedConnection  **
  - **IAM action:**  [directconnect:AssociateHostedConnection](#list_directconnect-action-AssociateHostedConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateMacSecKey  **
  - **IAM action:**  [directconnect:AssociateMacSecKey](#list_directconnect-action-AssociateMacSecKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateVirtualInterface  **
  - **IAM action:**  [directconnect:AssociateVirtualInterface](#list_directconnect-action-AssociateVirtualInterface) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ConfirmConnection  **
  - **IAM action:**  [directconnect:ConfirmConnection](#list_directconnect-action-ConfirmConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ConfirmCustomerAgreement  **
  - **IAM action:**  [directconnect:ConfirmCustomerAgreement](#list_directconnect-action-ConfirmCustomerAgreement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ConfirmPrivateVirtualInterface  **
  - **IAM action:**  [directconnect:ConfirmPrivateVirtualInterface](#list_directconnect-action-ConfirmPrivateVirtualInterface) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ConfirmPublicVirtualInterface  **
  - **IAM action:**  [directconnect:ConfirmPublicVirtualInterface](#list_directconnect-action-ConfirmPublicVirtualInterface) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ConfirmTransitVirtualInterface  **
  - **IAM action:**  [directconnect:ConfirmTransitVirtualInterface](#list_directconnect-action-ConfirmTransitVirtualInterface) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateBGPPeer  **
  - **IAM action:**  [directconnect:CreateBGPPeer](#list_directconnect-action-CreateBGPPeer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateConnection  **
  - **IAM action:**  [directconnect:CreateConnection](#list_directconnect-action-CreateConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [directconnect:TagResource](#list_directconnect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDirectConnectGateway  **
  - **IAM action:**  [directconnect:CreateDirectConnectGateway](#list_directconnect-action-CreateDirectConnectGateway)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [directconnect:TagResource](#list_directconnect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDirectConnectGatewayAssociation  **
  - **IAM action:**  [directconnect:CreateDirectConnectGatewayAssociation](#list_directconnect-action-CreateDirectConnectGatewayAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDirectConnectGatewayAssociationProposal  **
  - **IAM action:**  [directconnect:CreateDirectConnectGatewayAssociationProposal](#list_directconnect-action-CreateDirectConnectGatewayAssociationProposal) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateInterconnect  **
  - **IAM action:**  [directconnect:CreateInterconnect](#list_directconnect-action-CreateInterconnect)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [directconnect:TagResource](#list_directconnect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateLag  **
  - **IAM action:**  [directconnect:CreateLag](#list_directconnect-action-CreateLag)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [directconnect:TagResource](#list_directconnect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePrivateVirtualInterface  **
  - **IAM action:**  [directconnect:CreatePrivateVirtualInterface](#list_directconnect-action-CreatePrivateVirtualInterface)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [directconnect:TagResource](#list_directconnect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePublicVirtualInterface  **
  - **IAM action:**  [directconnect:CreatePublicVirtualInterface](#list_directconnect-action-CreatePublicVirtualInterface)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [directconnect:TagResource](#list_directconnect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateTransitVirtualInterface  **
  - **IAM action:**  [directconnect:CreateTransitVirtualInterface](#list_directconnect-action-CreateTransitVirtualInterface)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [directconnect:TagResource](#list_directconnect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteBGPPeer  **
  - **IAM action:**  [directconnect:DeleteBGPPeer](#list_directconnect-action-DeleteBGPPeer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConnection  **
  - **IAM action:**  [directconnect:DeleteConnection](#list_directconnect-action-DeleteConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDirectConnectGateway  **
  - **IAM action:**  [directconnect:DeleteDirectConnectGateway](#list_directconnect-action-DeleteDirectConnectGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDirectConnectGatewayAssociation  **
  - **IAM action:**  [directconnect:DeleteDirectConnectGatewayAssociation](#list_directconnect-action-DeleteDirectConnectGatewayAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDirectConnectGatewayAssociationProposal  **
  - **IAM action:**  [directconnect:DeleteDirectConnectGatewayAssociationProposal](#list_directconnect-action-DeleteDirectConnectGatewayAssociationProposal) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteInterconnect  **
  - **IAM action:**  [directconnect:DeleteInterconnect](#list_directconnect-action-DeleteInterconnect) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLag  **
  - **IAM action:**  [directconnect:DeleteLag](#list_directconnect-action-DeleteLag) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVirtualInterface  **
  - **IAM action:**  [directconnect:DeleteVirtualInterface](#list_directconnect-action-DeleteVirtualInterface) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeConnectionLoa  **
  - **IAM action:**  [directconnect:DescribeConnectionLoa](#list_directconnect-action-DescribeConnectionLoa) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeConnections  **
  - **IAM action:**  [directconnect:DescribeConnections](#list_directconnect-action-DescribeConnections) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeConnectionsOnInterconnect  **
  - **IAM action:**  [directconnect:DescribeConnectionsOnInterconnect](#list_directconnect-action-DescribeConnectionsOnInterconnect) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCustomerMetadata  **
  - **IAM action:**  [directconnect:DescribeCustomerMetadata](#list_directconnect-action-DescribeCustomerMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDirectConnectGatewayAssociationProposals  **
  - **IAM action:**  [directconnect:DescribeDirectConnectGatewayAssociationProposals](#list_directconnect-action-DescribeDirectConnectGatewayAssociationProposals) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDirectConnectGatewayAssociations  **
  - **IAM action:**  [directconnect:DescribeDirectConnectGatewayAssociations](#list_directconnect-action-DescribeDirectConnectGatewayAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDirectConnectGatewayAttachments  **
  - **IAM action:**  [directconnect:DescribeDirectConnectGatewayAttachments](#list_directconnect-action-DescribeDirectConnectGatewayAttachments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDirectConnectGateways  **
  - **IAM action:**  [directconnect:DescribeDirectConnectGateways](#list_directconnect-action-DescribeDirectConnectGateways) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeHostedConnections  **
  - **IAM action:**  [directconnect:DescribeHostedConnections](#list_directconnect-action-DescribeHostedConnections) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeInterconnectLoa  **
  - **IAM action:**  [directconnect:DescribeInterconnectLoa](#list_directconnect-action-DescribeInterconnectLoa) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeInterconnects  **
  - **IAM action:**  [directconnect:DescribeInterconnects](#list_directconnect-action-DescribeInterconnects) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLags  **
  - **IAM action:**  [directconnect:DescribeLags](#list_directconnect-action-DescribeLags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLoa  **
  - **IAM action:**  [directconnect:DescribeLoa](#list_directconnect-action-DescribeLoa) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLocations  **
  - **IAM action:**  [directconnect:DescribeLocations](#list_directconnect-action-DescribeLocations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRouterConfiguration  **
  - **IAM action:**  [directconnect:DescribeRouterConfiguration](#list_directconnect-action-DescribeRouterConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTags  **
  - **IAM action:**  [directconnect:DescribeTags](#list_directconnect-action-DescribeTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeVirtualGateways  **
  - **IAM action:**  [directconnect:DescribeVirtualGateways](#list_directconnect-action-DescribeVirtualGateways) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeVirtualInterfaces  **
  - **IAM action:**  [directconnect:DescribeVirtualInterfaces](#list_directconnect-action-DescribeVirtualInterfaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisassociateConnectionFromLag  **
  - **IAM action:**  [directconnect:DisassociateConnectionFromLag](#list_directconnect-action-DisassociateConnectionFromLag) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateMacSecKey  **
  - **IAM action:**  [directconnect:DisassociateMacSecKey](#list_directconnect-action-DisassociateMacSecKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListVirtualInterfaceRoutes  **
  - **IAM action:**  [directconnect:ListVirtualInterfaceRoutes](#list_directconnect-action-ListVirtualInterfaceRoutes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListVirtualInterfaceTestHistory  **
  - **IAM action:**  [directconnect:ListVirtualInterfaceTestHistory](#list_directconnect-action-ListVirtualInterfaceTestHistory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   StartBgpFailoverTest  **
  - **IAM action:**  [directconnect:StartBgpFailoverTest](#list_directconnect-action-StartBgpFailoverTest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopBgpFailoverTest  **
  - **IAM action:**  [directconnect:StopBgpFailoverTest](#list_directconnect-action-StopBgpFailoverTest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [directconnect:TagResource](#list_directconnect-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [directconnect:UntagResource](#list_directconnect-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateConnection  **
  - **IAM action:**  [directconnect:UpdateConnection](#list_directconnect-action-UpdateConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDirectConnectGateway  **
  - **IAM action:**  [directconnect:UpdateDirectConnectGateway](#list_directconnect-action-UpdateDirectConnectGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDirectConnectGatewayAssociation  **
  - **IAM action:**  [directconnect:UpdateDirectConnectGatewayAssociation](#list_directconnect-action-UpdateDirectConnectGatewayAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLag  **
  - **IAM action:**  [directconnect:UpdateLag](#list_directconnect-action-UpdateLag) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateVirtualInterfaceAttributes  **
  - **IAM action:**  [directconnect:UpdateVirtualInterfaceAttributes](#list_directconnect-action-UpdateVirtualInterfaceAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Direct Connect
<a name="list_directconnect-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptDirectConnectGatewayAssociationProposal](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AcceptDirectConnectGatewayAssociationProposal.html)  **
  - **Description:** Grants permission to accept a proposal request to attach a virtual private gateway to a Direct Connect gateway
  - **Resource types (\*required):** [dx-gateway\*](#list_directconnect-resource-dx-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AllocateConnectionOnInterconnect](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AllocateConnectionOnInterconnect.html)  **
  - **Description:** Grants permission to create a hosted connection on an interconnect
  - **Resource types (\*required):** [dxcon\*](#list_directconnect-resource-dxcon)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AllocateHostedConnection](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AllocateHostedConnection.html)  **
  - **Description:** Grants permission to create a new hosted connection between a AWS Direct Connect partner's network and a specific AWS Direct Connect location
  - **Resource types (\*required):** [dxcon](#list_directconnect-resource-dxcon) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_directconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_directconnect-aws_TagKeys)
  - **Resource types (\*required):** [dxlag](#list_directconnect-resource-dxlag) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_directconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_directconnect-aws_TagKeys)
  - **Access level:** Write

- **   [AllocatePrivateVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AllocatePrivateVirtualInterface.html)  **
  - **Description:** Grants permission to provision a private virtual interface to be owned by a different customer
  - **Resource types (\*required):** [dxcon](#list_directconnect-resource-dxcon) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_directconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_directconnect-aws_TagKeys)
  - **Resource types (\*required):** [dxlag](#list_directconnect-resource-dxlag) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_directconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_directconnect-aws_TagKeys)
  - **Access level:** Write

- **   [AllocatePublicVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AllocatePublicVirtualInterface.html)  **
  - **Description:** Grants permission to provision a public virtual interface to be owned by a different customer
  - **Resource types (\*required):** [dxcon](#list_directconnect-resource-dxcon) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_directconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_directconnect-aws_TagKeys)
  - **Resource types (\*required):** [dxlag](#list_directconnect-resource-dxlag) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_directconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_directconnect-aws_TagKeys)
  - **Access level:** Write

- **   [AllocateTransitVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AllocateTransitVirtualInterface.html)  **
  - **Description:** Grants permission to provision a transit virtual interface to be owned by a different customer
  - **Resource types (\*required):** [dxcon](#list_directconnect-resource-dxcon) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_directconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_directconnect-aws_TagKeys)
  - **Resource types (\*required):** [dxlag](#list_directconnect-resource-dxlag) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_directconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_directconnect-aws_TagKeys)
  - **Access level:** Write

- **   [AssociateConnectionWithLag](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AssociateConnectionWithLag.html)  **
  - **Description:** Grants permission to associate a connection with a LAG
  - **Resource types (\*required):** [dxcon\*](#list_directconnect-resource-dxcon) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dxlag\*](#list_directconnect-resource-dxlag) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateHostedConnection](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AssociateHostedConnection.html)  **
  - **Description:** Grants permission to associate a hosted connection and its virtual interfaces with a link aggregation group (LAG) or interconnect
  - **Resource types (\*required):** [dxcon\*](#list_directconnect-resource-dxcon) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dxcon\*](#list_directconnect-resource-dxcon) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dxlag](#list_directconnect-resource-dxlag) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateMacSecKey](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AssociateMacSecKey.html)  **
  - **Description:** Grants permission to associate a MAC Security (MACsec) Connection Key Name (CKN)/ Connectivity Association Key (CAK) pair with an AWS Direct Connect dedicated connection
  - **Resource types (\*required):** [dxcon](#list_directconnect-resource-dxcon) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dxlag](#list_directconnect-resource-dxlag) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AssociateVirtualInterface.html)  **
  - **Description:** Grants permission to associate a virtual interface with a specified link aggregation group (LAG) or connection
  - **Resource types (\*required):** [dxcon](#list_directconnect-resource-dxcon) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dxlag](#list_directconnect-resource-dxlag) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dxvif\*](#list_directconnect-resource-dxvif) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ConfirmConnection](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ConfirmConnection.html)  **
  - **Description:** Grants permission to confirm the creation of a hosted connection on an interconnect
  - **Resource types (\*required):** [dxcon\*](#list_directconnect-resource-dxcon)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ConfirmCustomerAgreement](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ConfirmCustomerAgreement.html)  **
  - **Description:** Grants permission to confirm the the terms of agreement when creating the connection or link aggregation group (LAG)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ConfirmPrivateVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ConfirmPrivateVirtualInterface.html)  **
  - **Description:** Grants permission to accept ownership of a private virtual interface created by another customer
  - **Resource types (\*required):** [dxvif\*](#list_directconnect-resource-dxvif)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ConfirmPublicVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ConfirmPublicVirtualInterface.html)  **
  - **Description:** Grants permission to accept ownership of a public virtual interface created by another customer
  - **Resource types (\*required):** [dxvif\*](#list_directconnect-resource-dxvif)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ConfirmTransitVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ConfirmTransitVirtualInterface.html)  **
  - **Description:** Grants permission to accept ownership of a transit virtual interface created by another customer
  - **Resource types (\*required):** [dxvif\*](#list_directconnect-resource-dxvif)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateBGPPeer](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateBGPPeer.html)  **
  - **Description:** Grants permission to create a BGP peer on the specified virtual interface
  - **Resource types (\*required):** [dxvif\*](#list_directconnect-resource-dxvif)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateConnection](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateConnection.html)  **
  - **Description:** Grants permission to create a new connection between the customer network and a specific AWS Direct Connect location
  - **Resource types (\*required):** [dxlag](#list_directconnect-resource-dxlag)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_directconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_directconnect-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDirectConnectGateway](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateDirectConnectGateway.html)  **
  - **Description:** Grants permission to create a Direct Connect gateway, which is an intermediate object that enables you to connect a set of virtual interfaces and virtual private gateways
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_directconnect-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_directconnect-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDirectConnectGatewayAssociation](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateDirectConnectGatewayAssociation.html)  **
  - **Description:** Grants permission to create an association between a Direct Connect gateway and a virtual private gateway
  - **Resource types (\*required):** [dx-gateway\*](#list_directconnect-resource-dx-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDirectConnectGatewayAssociationProposal](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateDirectConnectGatewayAssociationProposal.html)  **
  - **Description:** Grants permission to create a proposal to associate the specified virtual private gateway with the specified Direct Connect gateway
  - **Resource types (\*required):** [dx-gateway\*](#list_directconnect-resource-dx-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateInterconnect](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateInterconnect.html)  **
  - **Description:** Grants permission to create a new interconnect between a AWS Direct Connect partner's network and a specific AWS Direct Connect location
  - **Resource types (\*required):** [dxlag](#list_directconnect-resource-dxlag)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_directconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_directconnect-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLag](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateLag.html)  **
  - **Description:** Grants permission to create a link aggregation group (LAG) with the specified number of bundled physical connections between the customer network and a specific AWS Direct Connect location
  - **Resource types (\*required):** [dxcon](#list_directconnect-resource-dxcon)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_directconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_directconnect-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePrivateVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreatePrivateVirtualInterface.html)  **
  - **Description:** Grants permission to create a new private virtual interface
  - **Resource types (\*required):** [dxcon](#list_directconnect-resource-dxcon) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_directconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_directconnect-aws_TagKeys)
  - **Resource types (\*required):** [dxlag](#list_directconnect-resource-dxlag) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_directconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_directconnect-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePublicVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreatePublicVirtualInterface.html)  **
  - **Description:** Grants permission to create a new public virtual interface
  - **Resource types (\*required):** [dxcon](#list_directconnect-resource-dxcon) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_directconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_directconnect-aws_TagKeys)
  - **Resource types (\*required):** [dxlag](#list_directconnect-resource-dxlag) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_directconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_directconnect-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTransitVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateTransitVirtualInterface.html)  **
  - **Description:** Grants permission to create a new transit virtual interface
  - **Resource types (\*required):** [dxcon](#list_directconnect-resource-dxcon) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_directconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_directconnect-aws_TagKeys)
  - **Resource types (\*required):** [dxlag](#list_directconnect-resource-dxlag) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_directconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_directconnect-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteBGPPeer](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteBGPPeer.html)  **
  - **Description:** Grants permission to delete the specified BGP peer on the specified virtual interface with the specified customer address and ASN
  - **Resource types (\*required):** [dxvif\*](#list_directconnect-resource-dxvif)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConnection](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteConnection.html)  **
  - **Description:** Grants permission to delete the connection
  - **Resource types (\*required):** [dxcon\*](#list_directconnect-resource-dxcon)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDirectConnectGateway](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteDirectConnectGateway.html)  **
  - **Description:** Grants permission to delete the specified Direct Connect gateway
  - **Resource types (\*required):** [dx-gateway\*](#list_directconnect-resource-dx-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDirectConnectGatewayAssociation](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteDirectConnectGatewayAssociation.html)  **
  - **Description:** Grants permission to delete the association between the specified Direct Connect gateway and virtual private gateway
  - **Resource types (\*required):** [dx-gateway\*](#list_directconnect-resource-dx-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDirectConnectGatewayAssociationProposal](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteDirectConnectGatewayAssociationProposal.html)  **
  - **Description:** Grants permission to delete the association proposal request between the specified Direct Connect gateway and virtual private gateway
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteInterconnect](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteInterconnect.html)  **
  - **Description:** Grants permission to delete the specified interconnect
  - **Resource types (\*required):** [dxcon\*](#list_directconnect-resource-dxcon)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLag](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteLag.html)  **
  - **Description:** Grants permission to delete the specified link aggregation group (LAG)
  - **Resource types (\*required):** [dxlag\*](#list_directconnect-resource-dxlag)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteVirtualInterface](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteVirtualInterface.html)  **
  - **Description:** Grants permission to delete a virtual interface
  - **Resource types (\*required):** [dxvif\*](#list_directconnect-resource-dxvif)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeConnectionLoa](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeConnectionLoa.html)  **
  - **Description:** Grants permission to describe the LOA-CFA for a Connection
  - **Resource types (\*required):** [dxcon\*](#list_directconnect-resource-dxcon)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeConnections](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeConnections.html)  **
  - **Description:** Grants permission to describe all connections in this region
  - **Resource types (\*required):** [dxcon](#list_directconnect-resource-dxcon)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeConnectionsOnInterconnect](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeConnectionsOnInterconnect.html)  **
  - **Description:** Grants permission to describe a list of connections that have been provisioned on the given interconnect
  - **Resource types (\*required):** [dxcon\*](#list_directconnect-resource-dxcon)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCustomerMetadata](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeCustomerMetadata.html)  **
  - **Description:** Grants permission to view a list of customer agreements, along with their signed status and whether the customer is an NNIPartner, NNIPartnerV2, or a nonPartner
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeDirectConnectGatewayAssociationProposals](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeDirectConnectGatewayAssociationProposals.html)  **
  - **Description:** Grants permission to describe one or more association proposals for connection between a virtual private gateway and a Direct Connect gateway
  - **Resource types (\*required):** [dx-gateway](#list_directconnect-resource-dx-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDirectConnectGatewayAssociations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeDirectConnectGatewayAssociations.html)  **
  - **Description:** Grants permission to describe the associations between your Direct Connect gateways and virtual private gateways
  - **Resource types (\*required):** [dx-gateway](#list_directconnect-resource-dx-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDirectConnectGatewayAttachments](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeDirectConnectGatewayAttachments.html)  **
  - **Description:** Grants permission to describe the attachments between your Direct Connect gateways and virtual interfaces
  - **Resource types (\*required):** [dx-gateway](#list_directconnect-resource-dx-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDirectConnectGateways](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeDirectConnectGateways.html)  **
  - **Description:** Grants permission to describe all your Direct Connect gateways or only the specified Direct Connect gateway
  - **Resource types (\*required):** [dx-gateway](#list_directconnect-resource-dx-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeHostedConnections](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeHostedConnections.html)  **
  - **Description:** Grants permission to describe the hosted connections that have been provisioned on the specified interconnect or link aggregation group (LAG)
  - **Resource types (\*required):** [dxcon](#list_directconnect-resource-dxcon) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dxlag](#list_directconnect-resource-dxlag) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeInterconnectLoa](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeInterconnectLoa.html)  **
  - **Description:** Grants permission to describe the LOA-CFA for an Interconnect
  - **Resource types (\*required):** [dxcon\*](#list_directconnect-resource-dxcon)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeInterconnects](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeInterconnects.html)  **
  - **Description:** Grants permission to describe a list of interconnects owned by the AWS account
  - **Resource types (\*required):** [dxcon](#list_directconnect-resource-dxcon)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeLags](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLags.html)  **
  - **Description:** Grants permission to describe all your link aggregation groups (LAG) or the specified LAG
  - **Resource types (\*required):** [dxlag](#list_directconnect-resource-dxlag)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeLoa](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLoa.html)  **
  - **Description:** Grants permission to describe the LOA-CFA for a connection, interconnect, or link aggregation group (LAG)
  - **Resource types (\*required):** [dxcon](#list_directconnect-resource-dxcon) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dxlag](#list_directconnect-resource-dxlag) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeLocations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html)  **
  - **Description:** Grants permission to describe the list of AWS Direct Connect locations in the current AWS region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeRouterConfiguration](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeRouterConfiguration.html)  **
  - **Description:** Grants permission to describe Details about the router for a virtual interface
  - **Resource types (\*required):** [dxvif\*](#list_directconnect-resource-dxvif)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTags](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeTags.html)  **
  - **Description:** Grants permission to describe the tags associated with the specified AWS Direct Connect resources
  - **Resource types (\*required):** [dx-gateway](#list_directconnect-resource-dx-gateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dxcon](#list_directconnect-resource-dxcon) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dxlag](#list_directconnect-resource-dxlag) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dxvif](#list_directconnect-resource-dxvif) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeVirtualGateways](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeVirtualGateways.html)  **
  - **Description:** Grants permission to describe a list of virtual private gateways owned by the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeVirtualInterfaces](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeVirtualInterfaces.html)  **
  - **Description:** Grants permission to describe all virtual interfaces for an AWS account
  - **Resource types (\*required):** [dxcon](#list_directconnect-resource-dxcon) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dxlag](#list_directconnect-resource-dxlag) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dxvif](#list_directconnect-resource-dxvif) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DisassociateConnectionFromLag](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DisassociateConnectionFromLag.html)  **
  - **Description:** Grants permission to disassociate a connection from a link aggregation group (LAG)
  - **Resource types (\*required):** [dxcon\*](#list_directconnect-resource-dxcon) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dxlag\*](#list_directconnect-resource-dxlag) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateMacSecKey](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DisassociateMacSecKey.html)  **
  - **Description:** Grants permission to remove the association between a MAC Security (MACsec) security key and an AWS Direct Connect dedicated connection
  - **Resource types (\*required):** [dxcon](#list_directconnect-resource-dxcon) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dxlag](#list_directconnect-resource-dxlag) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListVirtualInterfaceRoutes](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ListVirtualInterfaceRoutes.html)  **
  - **Description:** Grants permission to list the routes accepted and advertised over a virtual interface
  - **Resource types (\*required):** [dxvif\*](#list_directconnect-resource-dxvif)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListVirtualInterfaceTestHistory](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ListVirtualInterfaceTestHistory.html)  **
  - **Description:** Grants permission to list the virtual interface failover test history
  - **Resource types (\*required):** [dxvif\*](#list_directconnect-resource-dxvif)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [StartBgpFailoverTest](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_StartBgpFailoverTest.html)  **
  - **Description:** Grants permission to start the virtual interface failover test that verifies your configuration meets your resiliency requirements by placing the BGP peering session in the DOWN state. You can then send traffic to verify that there are no outages
  - **Resource types (\*required):** [dxvif\*](#list_directconnect-resource-dxvif)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopBgpFailoverTest](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_StopBgpFailoverTest.html)  **
  - **Description:** Grants permission to stop the virtual interface failover test
  - **Resource types (\*required):** [dxvif\*](#list_directconnect-resource-dxvif)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add the specified tags to the specified AWS Direct Connect resource. Each resource can have a maximum of 50 tags
  - **Resource types (\*required):** [dx-gateway](#list_directconnect-resource-dx-gateway) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_directconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_directconnect-aws_TagKeys)
  - **Resource types (\*required):** [dxcon](#list_directconnect-resource-dxcon) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_directconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_directconnect-aws_TagKeys)
  - **Resource types (\*required):** [dxlag](#list_directconnect-resource-dxlag) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_directconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_directconnect-aws_TagKeys)
  - **Resource types (\*required):** [dxvif](#list_directconnect-resource-dxvif) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_directconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_directconnect-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove one or more tags from the specified AWS Direct Connect resource
  - **Resource types (\*required):** [dx-gateway](#list_directconnect-resource-dx-gateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_directconnect-aws_TagKeys)
  - **Resource types (\*required):** [dxcon](#list_directconnect-resource-dxcon) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_directconnect-aws_TagKeys)
  - **Resource types (\*required):** [dxlag](#list_directconnect-resource-dxlag) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_directconnect-aws_TagKeys)
  - **Resource types (\*required):** [dxvif](#list_directconnect-resource-dxvif) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_directconnect-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateConnection](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_UpdateConnection.html)  **
  - **Description:** Grants permission to update the AWS Direct Connect dedicated connection configuration. You can update the following parameters for a connection: The connection name or The connection's MAC Security (MACsec) encryption mode
  - **Resource types (\*required):** [dxcon\*](#list_directconnect-resource-dxcon)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDirectConnectGateway](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_UpdateDirectConnectGateway.html)  **
  - **Description:** Grants permission to update the name of a Direct Connect gateway
  - **Resource types (\*required):** [dx-gateway\*](#list_directconnect-resource-dx-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDirectConnectGatewayAssociation](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_UpdateDirectConnectGatewayAssociation.html)  **
  - **Description:** Grants permission to update the specified attributes of the Direct Connect gateway association
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateLag](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_UpdateLag.html)  **
  - **Description:** Grants permission to update the attributes of the specified link aggregation group (LAG)
  - **Resource types (\*required):** [dxlag\*](#list_directconnect-resource-dxlag)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateVirtualInterfaceAttributes](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_UpdateVirtualInterfaceAttributes.html)  **
  - **Description:** Grants permission to update the specified attributes of the specified virtual private interface
  - **Resource types (\*required):** [dxvif\*](#list_directconnect-resource-dxvif)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Direct Connect
<a name="list_directconnect-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [dx-gateway](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DirectConnectGateway.html)  | arn:${Partition}:directconnect::${Account}:dx-gateway/${DirectConnectGatewayId} | [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_) | 
|  [dxcon](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_Connection.html)  | arn:${Partition}:directconnect:${Region}:${Account}:dxcon/${ConnectionId} | [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_) | 
|  [dxlag](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_Lag.html)  | arn:${Partition}:directconnect:${Region}:${Account}:dxlag/${LagId} | [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_) | 
|  [dxvif](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_VirtualInterface.html)  | arn:${Partition}:directconnect:${Region}:${Account}:dxvif/${VirtualInterfaceId} | [aws:ResourceTag/${TagKey}](#list_directconnect-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Direct Connect
<a name="list_directconnect-policy-keys"></a>

AWS Direct Connect defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by actions based on the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by actions based on tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by actions based on the presence of tag keys in the request | ArrayOfString | 