

# Actions, resources, and condition keys for Amazon Managed Blockchain
<a name="list_managedblockchain"></a>

Amazon Managed Blockchain (service prefix: `managedblockchain`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/managed-blockchain/latest/managementguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/managed-blockchain/latest/managementguide/) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/managedblockchain/managedblockchain.json) for this service.

**Topics**
+ [API operations defined by Amazon Managed Blockchain](#list_managedblockchain-operations)
+ [Actions defined by Amazon Managed Blockchain](#list_managedblockchain-actions-as-permissions)
+ [Permission-only actions for Amazon Managed Blockchain](#list_managedblockchain-permission-only-actions)
+ [Resource types defined by Amazon Managed Blockchain](#list_managedblockchain-resources-for-iam-policies)
+ [Condition keys for Amazon Managed Blockchain](#list_managedblockchain-policy-keys)

## API operations defined by Amazon Managed Blockchain
<a name="list_managedblockchain-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_managedblockchain-actions-as-permissions).




- **   CreateAccessor  **
  - **IAM action:**  [managedblockchain:CreateAccessor](#list_managedblockchain-action-CreateAccessor)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [managedblockchain:TagResource](#list_managedblockchain-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateMember  **
  - **IAM action:**  [managedblockchain:CreateMember](#list_managedblockchain-action-CreateMember)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [managedblockchain:TagResource](#list_managedblockchain-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateNetwork  **
  - **IAM action:**  [managedblockchain:CreateNetwork](#list_managedblockchain-action-CreateNetwork)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [managedblockchain:TagResource](#list_managedblockchain-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateNode  **
  - **IAM action:**  [managedblockchain:CreateNode](#list_managedblockchain-action-CreateNode)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [managedblockchain:TagResource](#list_managedblockchain-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateProposal  **
  - **IAM action:**  [managedblockchain:CreateProposal](#list_managedblockchain-action-CreateProposal)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [managedblockchain:TagResource](#list_managedblockchain-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAccessor  **
  - **IAM action:**  [managedblockchain:DeleteAccessor](#list_managedblockchain-action-DeleteAccessor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMember  **
  - **IAM action:**  [managedblockchain:DeleteMember](#list_managedblockchain-action-DeleteMember) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteNode  **
  - **IAM action:**  [managedblockchain:DeleteNode](#list_managedblockchain-action-DeleteNode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAccessor  **
  - **IAM action:**  [managedblockchain:GetAccessor](#list_managedblockchain-action-GetAccessor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMember  **
  - **IAM action:**  [managedblockchain:GetMember](#list_managedblockchain-action-GetMember) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetNetwork  **
  - **IAM action:**  [managedblockchain:GetNetwork](#list_managedblockchain-action-GetNetwork) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetNode  **
  - **IAM action:**  [managedblockchain:GetNode](#list_managedblockchain-action-GetNode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProposal  **
  - **IAM action:**  [managedblockchain:GetProposal](#list_managedblockchain-action-GetProposal) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAccessors  **
  - **IAM action:**  [managedblockchain:ListAccessors](#list_managedblockchain-action-ListAccessors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInvitations  **
  - **IAM action:**  [managedblockchain:ListInvitations](#list_managedblockchain-action-ListInvitations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMembers  **
  - **IAM action:**  [managedblockchain:ListMembers](#list_managedblockchain-action-ListMembers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNetworks  **
  - **IAM action:**  [managedblockchain:ListNetworks](#list_managedblockchain-action-ListNetworks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNodes  **
  - **IAM action:**  [managedblockchain:ListNodes](#list_managedblockchain-action-ListNodes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProposalVotes  **
  - **IAM action:**  [managedblockchain:ListProposalVotes](#list_managedblockchain-action-ListProposalVotes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListProposals  **
  - **IAM action:**  [managedblockchain:ListProposals](#list_managedblockchain-action-ListProposals) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [managedblockchain:ListTagsForResource](#list_managedblockchain-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   RejectInvitation  **
  - **IAM action:**  [managedblockchain:RejectInvitation](#list_managedblockchain-action-RejectInvitation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [managedblockchain:TagResource](#list_managedblockchain-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [managedblockchain:UntagResource](#list_managedblockchain-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateMember  **
  - **IAM action:**  [managedblockchain:UpdateMember](#list_managedblockchain-action-UpdateMember) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateNode  **
  - **IAM action:**  [managedblockchain:UpdateNode](#list_managedblockchain-action-UpdateNode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   VoteOnProposal  **
  - **IAM action:**  [managedblockchain:VoteOnProposal](#list_managedblockchain-action-VoteOnProposal) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Managed Blockchain
<a name="list_managedblockchain-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateAccessor](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_CreateAccessor.html)  **
  - **Description:** Grants permission to create an Amazon Managed Blockchain accessor
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_managedblockchain-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_managedblockchain-aws_TagKeys)
  - **Access level:** Write

- **   [CreateMember](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_CreateMember.html)  **
  - **Description:** Grants permission to create a member of an Amazon Managed Blockchain network
  - **Resource types (\*required):** [network\*](#list_managedblockchain-resource-network)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_managedblockchain-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_managedblockchain-aws_TagKeys)
  - **Access level:** Write

- **   [CreateNetwork](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_CreateNetwork.html)  **
  - **Description:** Grants permission to create an Amazon Managed Blockchain network
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_managedblockchain-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_managedblockchain-aws_TagKeys)
  - **Access level:** Write

- **   [CreateNode](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_CreateNode.html)  **
  - **Description:** Grants permission to create a node within a member of an Amazon Managed Blockchain network
  - **Resource types (\*required):** [member](#list_managedblockchain-resource-member) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_managedblockchain-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_managedblockchain-aws_TagKeys)
  - **Resource types (\*required):** [network](#list_managedblockchain-resource-network) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_managedblockchain-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_managedblockchain-aws_TagKeys)
  - **Access level:** Write

- **   [CreateProposal](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_CreateProposal.html)  **
  - **Description:** Grants permission to create a proposal that other blockchain network members can vote on to add or remove a member in an Amazon Managed Blockchain network
  - **Resource types (\*required):** [network\*](#list_managedblockchain-resource-network)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_managedblockchain-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_managedblockchain-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAccessor](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_DeleteAccessor.html)  **
  - **Description:** Grants permission to delete an Amazon Managed Blockchain accessor
  - **Resource types (\*required):** [accessor\*](#list_managedblockchain-resource-accessor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMember](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_DeleteMember.html)  **
  - **Description:** Grants permission to delete a member and all associated resources from an Amazon Managed Blockchain network
  - **Resource types (\*required):** [member\*](#list_managedblockchain-resource-member)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteNode](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_DeleteNode.html)  **
  - **Description:** Grants permission to delete a node from a member of an Amazon Managed Blockchain network
  - **Resource types (\*required):** [node\*](#list_managedblockchain-resource-node)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAccessor](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_GetAccessor.html)  **
  - **Description:** Grants permission to return detailed information about an Amazon Managed Blockchain accessor
  - **Resource types (\*required):** [accessor\*](#list_managedblockchain-resource-accessor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMember](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_GetMember.html)  **
  - **Description:** Grants permission to return detailed information about a member of an Amazon Managed Blockchain network
  - **Resource types (\*required):** [member\*](#list_managedblockchain-resource-member)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetNetwork](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_GetNetwork.html)  **
  - **Description:** Grants permission to return detailed information about an Amazon Managed Blockchain network
  - **Resource types (\*required):** [network\*](#list_managedblockchain-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetNode](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_GetNode.html)  **
  - **Description:** Grants permission to return detailed information about a node within a member of an Amazon Managed Blockchain network
  - **Resource types (\*required):** [node\*](#list_managedblockchain-resource-node)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetProposal](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_GetProposal.html)  **
  - **Description:** Grants permission to return detailed information about a proposal of an Amazon Managed Blockchain network
  - **Resource types (\*required):** [proposal\*](#list_managedblockchain-resource-proposal)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [InvokeRpcBitcoinMainnet](https://docs.aws.amazon.com/managed-blockchain/latest/ambbtc-dg/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-access-bitcoin-networks)  **
  - **Description:** Grants permission to invoke the Bitcoin Mainnet RPCs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [InvokeRpcBitcoinTestnet](https://docs.aws.amazon.com/managed-blockchain/latest/ambbtc-dg/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-access-bitcoin-networks)  **
  - **Description:** Grants permission to invoke the Bitcoin Testnet RPCs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [InvokeRpcPolygonMainnet](https://docs.aws.amazon.com/managed-blockchain/latest/ambp-dg/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-access-polygon-networks)  **
  - **Description:** Grants permission to invoke the Polygon Mainnet RPCs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [InvokeRpcPolygonMumbaiTestnet](https://docs.aws.amazon.com/managed-blockchain/latest/ambp-dg/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-access-polygon-networks)  **
  - **Description:** Grants permission to invoke the Polygon Mumbai Testnet RPCs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListAccessors](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_ListAccessors.html)  **
  - **Description:** Grants permission to list the Amazon Managed Blockchain accessors owned by the current AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListInvitations](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_ListInvitations.html)  **
  - **Description:** Grants permission to list the invitations extended to the active AWS account from any Managed Blockchain network
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMembers](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_ListMembers.html)  **
  - **Description:** Grants permission to list the members of an Amazon Managed Blockchain network and the properties of their memberships
  - **Resource types (\*required):** [network\*](#list_managedblockchain-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListNetworks](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_ListNetworks.html)  **
  - **Description:** Grants permission to list the Amazon Managed Blockchain networks in which the current AWS account participates
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListNodes](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_ListNodes.html)  **
  - **Description:** Grants permission to list the nodes within a member of an Amazon Managed Blockchain network
  - **Resource types (\*required):** [member](#list_managedblockchain-resource-member) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [network](#list_managedblockchain-resource-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListProposalVotes](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_ListProposalVotes.html)  **
  - **Description:** Grants permission to list all votes for a proposal, including the value of the vote and the unique identifier of the member that cast the vote for the given Amazon Managed Blockchain network
  - **Resource types (\*required):** [proposal\*](#list_managedblockchain-resource-proposal)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListProposals](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_ListProposals.html)  **
  - **Description:** Grants permission to list proposals for the given Amazon Managed Blockchain network
  - **Resource types (\*required):** [network\*](#list_managedblockchain-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to view tags associated with an Amazon Managed Blockchain resource
  - **Resource types (\*required):** [accessor](#list_managedblockchain-resource-accessor) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [invitation](#list_managedblockchain-resource-invitation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [member](#list_managedblockchain-resource-member) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [network](#list_managedblockchain-resource-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [node](#list_managedblockchain-resource-node) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [proposal](#list_managedblockchain-resource-proposal) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [RejectInvitation](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_RejectInvitation.html)  **
  - **Description:** Grants permission to reject the invitation to join the blockchain network
  - **Resource types (\*required):** [invitation\*](#list_managedblockchain-resource-invitation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to an Amazon Managed Blockchain resource
  - **Resource types (\*required):** [accessor](#list_managedblockchain-resource-accessor) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_managedblockchain-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_managedblockchain-aws_TagKeys)
  - **Resource types (\*required):** [invitation](#list_managedblockchain-resource-invitation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_managedblockchain-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_managedblockchain-aws_TagKeys)
  - **Resource types (\*required):** [member](#list_managedblockchain-resource-member) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_managedblockchain-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_managedblockchain-aws_TagKeys)
  - **Resource types (\*required):** [network](#list_managedblockchain-resource-network) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_managedblockchain-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_managedblockchain-aws_TagKeys)
  - **Resource types (\*required):** [node](#list_managedblockchain-resource-node) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_managedblockchain-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_managedblockchain-aws_TagKeys)
  - **Resource types (\*required):** [proposal](#list_managedblockchain-resource-proposal) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_managedblockchain-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_managedblockchain-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from an Amazon Managed Blockchain resource
  - **Resource types (\*required):** [accessor](#list_managedblockchain-resource-accessor) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_managedblockchain-aws_TagKeys)
  - **Resource types (\*required):** [invitation](#list_managedblockchain-resource-invitation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_managedblockchain-aws_TagKeys)
  - **Resource types (\*required):** [member](#list_managedblockchain-resource-member) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_managedblockchain-aws_TagKeys)
  - **Resource types (\*required):** [network](#list_managedblockchain-resource-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_managedblockchain-aws_TagKeys)
  - **Resource types (\*required):** [node](#list_managedblockchain-resource-node) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_managedblockchain-aws_TagKeys)
  - **Resource types (\*required):** [proposal](#list_managedblockchain-resource-proposal) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_managedblockchain-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateMember](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_UpdateMember.html)  **
  - **Description:** Grants permission to update a member of an Amazon Managed Blockchain network
  - **Resource types (\*required):** [member\*](#list_managedblockchain-resource-member)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateNode](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_UpdateNode.html)  **
  - **Description:** Grants permission to update a node from a member of an Amazon Managed Blockchain network
  - **Resource types (\*required):** [node\*](#list_managedblockchain-resource-node)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [VoteOnProposal](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_VoteOnProposal.html)  **
  - **Description:** Grants permission to cast a vote for a proposal on behalf of the blockchain network member specified
  - **Resource types (\*required):** [proposal\*](#list_managedblockchain-resource-proposal)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon Managed Blockchain
<a name="list_managedblockchain-permission-only-actions"></a>

The following actions are defined by Amazon Managed Blockchain but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [GET](https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/security_iam_id-based-policy-examples.html)  | Grants permission to send HTTP GET requests to an Ethereum node |  |   | Permissions management, Write | 
|   [Invoke](https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/security_iam_id-based-policy-examples.html)  | Grants permission to create WebSocket connections to an Ethereum node |  |   | Permissions management, Write | 
|   [POST](https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/security_iam_id-based-policy-examples.html)  | Grants permission to send HTTP POST requests to an Ethereum node |  |   | Permissions management, Write | 

## Resource types defined by Amazon Managed Blockchain
<a name="list_managedblockchain-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [accessor](${ActionsDocRoot}API_Accessor.html)  | arn:${Partition}:managedblockchain:${Region}:${Account}:accessors/${AccessorId} | [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_) | 
|  [invitation](${ActionsDocRoot}API_Invitation.html)  | arn:${Partition}:managedblockchain:${Region}:${Account}:invitations/${InvitationId} | [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_) | 
|  [member](${ActionsDocRoot}API_Member.html)  | arn:${Partition}:managedblockchain:${Region}:${Account}:members/${MemberId} | [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_) | 
|  [network](${ActionsDocRoot}API_Network.html)  | arn:${Partition}:managedblockchain:${Region}::networks/${NetworkId} | [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_) | 
|  [node](${ActionsDocRoot}API_Node.html)  | arn:${Partition}:managedblockchain:${Region}:${Account}:nodes/${NodeId} | [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_) | 
|  [proposal](${ActionsDocRoot}API_Proposal.html)  | arn:${Partition}:managedblockchain:${Region}::proposals/${ProposalId} | [aws:ResourceTag/${TagKey}](#list_managedblockchain-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Managed Blockchain
<a name="list_managedblockchain-policy-keys"></a>

Amazon Managed Blockchain defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters actions based on the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters actions based on the tags associated with an Amazon Managed Blockchain resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters actions based on the tag keys that are passed in the request | ArrayOfString | 