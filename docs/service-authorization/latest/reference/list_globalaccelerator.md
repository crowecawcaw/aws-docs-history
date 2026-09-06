

# Actions, resources, and condition keys for AWS Global Accelerator
<a name="list_globalaccelerator"></a>

AWS Global Accelerator (service prefix: `globalaccelerator`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/global-accelerator/latest/api/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/global-accelerator/latest/dg/auth-and-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/globalaccelerator/globalaccelerator.json) for this service.

**Topics**
+ [API operations defined by AWS Global Accelerator](#list_globalaccelerator-operations)
+ [Actions defined by AWS Global Accelerator](#list_globalaccelerator-actions-as-permissions)
+ [Resource types defined by AWS Global Accelerator](#list_globalaccelerator-resources-for-iam-policies)
+ [Condition keys for AWS Global Accelerator](#list_globalaccelerator-policy-keys)

## API operations defined by AWS Global Accelerator
<a name="list_globalaccelerator-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_globalaccelerator-actions-as-permissions).




- **   AddCustomRoutingEndpoints  **
  - **IAM action:**  [globalaccelerator:AddCustomRoutingEndpoints](#list_globalaccelerator-action-AddCustomRoutingEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AddEndpoints  **
  - **IAM action:**  [globalaccelerator:AddEndpoints](#list_globalaccelerator-action-AddEndpoints)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [globalaccelerator:UpdateEndpointGroup](#list_globalaccelerator-action-UpdateEndpointGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   AdvertiseByoipCidr  **
  - **IAM action:**  [globalaccelerator:AdvertiseByoipCidr](#list_globalaccelerator-action-AdvertiseByoipCidr) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AllowCustomRoutingTraffic  **
  - **IAM action:**  [globalaccelerator:AllowCustomRoutingTraffic](#list_globalaccelerator-action-AllowCustomRoutingTraffic) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAccelerator  **
  - **IAM action:**  [globalaccelerator:CreateAccelerator](#list_globalaccelerator-action-CreateAccelerator)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [globalaccelerator:TagResource](#list_globalaccelerator-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCrossAccountAttachment  **
  - **IAM action:**  [globalaccelerator:CreateCrossAccountAttachment](#list_globalaccelerator-action-CreateCrossAccountAttachment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [globalaccelerator:TagResource](#list_globalaccelerator-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCustomRoutingAccelerator  **
  - **IAM action:**  [globalaccelerator:CreateCustomRoutingAccelerator](#list_globalaccelerator-action-CreateCustomRoutingAccelerator)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [globalaccelerator:TagResource](#list_globalaccelerator-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCustomRoutingEndpointGroup  **
  - **IAM action:**  [globalaccelerator:CreateCustomRoutingEndpointGroup](#list_globalaccelerator-action-CreateCustomRoutingEndpointGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateCustomRoutingListener  **
  - **IAM action:**  [globalaccelerator:CreateCustomRoutingListener](#list_globalaccelerator-action-CreateCustomRoutingListener) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateEndpointGroup  **
  - **IAM action:**  [globalaccelerator:CreateEndpointGroup](#list_globalaccelerator-action-CreateEndpointGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateListener  **
  - **IAM action:**  [globalaccelerator:CreateListener](#list_globalaccelerator-action-CreateListener) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAccelerator  **
  - **IAM action:**  [globalaccelerator:DeleteAccelerator](#list_globalaccelerator-action-DeleteAccelerator) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCrossAccountAttachment  **
  - **IAM action:**  [globalaccelerator:DeleteCrossAccountAttachment](#list_globalaccelerator-action-DeleteCrossAccountAttachment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCustomRoutingAccelerator  **
  - **IAM action:**  [globalaccelerator:DeleteCustomRoutingAccelerator](#list_globalaccelerator-action-DeleteCustomRoutingAccelerator) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCustomRoutingEndpointGroup  **
  - **IAM action:**  [globalaccelerator:DeleteCustomRoutingEndpointGroup](#list_globalaccelerator-action-DeleteCustomRoutingEndpointGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCustomRoutingListener  **
  - **IAM action:**  [globalaccelerator:DeleteCustomRoutingListener](#list_globalaccelerator-action-DeleteCustomRoutingListener) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEndpointGroup  **
  - **IAM action:**  [globalaccelerator:DeleteEndpointGroup](#list_globalaccelerator-action-DeleteEndpointGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteListener  **
  - **IAM action:**  [globalaccelerator:DeleteListener](#list_globalaccelerator-action-DeleteListener) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DenyCustomRoutingTraffic  **
  - **IAM action:**  [globalaccelerator:DenyCustomRoutingTraffic](#list_globalaccelerator-action-DenyCustomRoutingTraffic) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeprovisionByoipCidr  **
  - **IAM action:**  [globalaccelerator:DeprovisionByoipCidr](#list_globalaccelerator-action-DeprovisionByoipCidr) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAccelerator  **
  - **IAM action:**  [globalaccelerator:DescribeAccelerator](#list_globalaccelerator-action-DescribeAccelerator) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAcceleratorAttributes  **
  - **IAM action:**  [globalaccelerator:DescribeAcceleratorAttributes](#list_globalaccelerator-action-DescribeAcceleratorAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCrossAccountAttachment  **
  - **IAM action:**  [globalaccelerator:DescribeCrossAccountAttachment](#list_globalaccelerator-action-DescribeCrossAccountAttachment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCustomRoutingAccelerator  **
  - **IAM action:**  [globalaccelerator:DescribeCustomRoutingAccelerator](#list_globalaccelerator-action-DescribeCustomRoutingAccelerator) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCustomRoutingAcceleratorAttributes  **
  - **IAM action:**  [globalaccelerator:DescribeCustomRoutingAcceleratorAttributes](#list_globalaccelerator-action-DescribeCustomRoutingAcceleratorAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCustomRoutingEndpointGroup  **
  - **IAM action:**  [globalaccelerator:DescribeCustomRoutingEndpointGroup](#list_globalaccelerator-action-DescribeCustomRoutingEndpointGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCustomRoutingListener  **
  - **IAM action:**  [globalaccelerator:DescribeCustomRoutingListener](#list_globalaccelerator-action-DescribeCustomRoutingListener) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEndpointGroup  **
  - **IAM action:**  [globalaccelerator:DescribeEndpointGroup](#list_globalaccelerator-action-DescribeEndpointGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeListener  **
  - **IAM action:**  [globalaccelerator:DescribeListener](#list_globalaccelerator-action-DescribeListener) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAccelerators  **
  - **IAM action:**  [globalaccelerator:ListAccelerators](#list_globalaccelerator-action-ListAccelerators) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListByoipCidrs  **
  - **IAM action:**  [globalaccelerator:ListByoipCidrs](#list_globalaccelerator-action-ListByoipCidrs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCrossAccountAttachments  **
  - **IAM action:**  [globalaccelerator:ListCrossAccountAttachments](#list_globalaccelerator-action-ListCrossAccountAttachments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCrossAccountResourceAccounts  **
  - **IAM action:**  [globalaccelerator:ListCrossAccountResourceAccounts](#list_globalaccelerator-action-ListCrossAccountResourceAccounts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCrossAccountResources  **
  - **IAM action:**  [globalaccelerator:ListCrossAccountResources](#list_globalaccelerator-action-ListCrossAccountResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCustomRoutingAccelerators  **
  - **IAM action:**  [globalaccelerator:ListCustomRoutingAccelerators](#list_globalaccelerator-action-ListCustomRoutingAccelerators) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCustomRoutingEndpointGroups  **
  - **IAM action:**  [globalaccelerator:ListCustomRoutingEndpointGroups](#list_globalaccelerator-action-ListCustomRoutingEndpointGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCustomRoutingListeners  **
  - **IAM action:**  [globalaccelerator:ListCustomRoutingListeners](#list_globalaccelerator-action-ListCustomRoutingListeners) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCustomRoutingPortMappings  **
  - **IAM action:**  [globalaccelerator:ListCustomRoutingPortMappings](#list_globalaccelerator-action-ListCustomRoutingPortMappings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCustomRoutingPortMappingsByDestination  **
  - **IAM action:**  [globalaccelerator:ListCustomRoutingPortMappingsByDestination](#list_globalaccelerator-action-ListCustomRoutingPortMappingsByDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEndpointGroups  **
  - **IAM action:**  [globalaccelerator:ListEndpointGroups](#list_globalaccelerator-action-ListEndpointGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListListeners  **
  - **IAM action:**  [globalaccelerator:ListListeners](#list_globalaccelerator-action-ListListeners) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [globalaccelerator:ListTagsForResource](#list_globalaccelerator-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ProvisionByoipCidr  **
  - **IAM action:**  [globalaccelerator:ProvisionByoipCidr](#list_globalaccelerator-action-ProvisionByoipCidr) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveCustomRoutingEndpoints  **
  - **IAM action:**  [globalaccelerator:RemoveCustomRoutingEndpoints](#list_globalaccelerator-action-RemoveCustomRoutingEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveEndpoints  **
  - **IAM action:**  [globalaccelerator:RemoveEndpoints](#list_globalaccelerator-action-RemoveEndpoints)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [globalaccelerator:UpdateEndpointGroup](#list_globalaccelerator-action-UpdateEndpointGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [globalaccelerator:TagResource](#list_globalaccelerator-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [globalaccelerator:UntagResource](#list_globalaccelerator-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAccelerator  **
  - **IAM action:**  [globalaccelerator:UpdateAccelerator](#list_globalaccelerator-action-UpdateAccelerator) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAcceleratorAttributes  **
  - **IAM action:**  [globalaccelerator:UpdateAcceleratorAttributes](#list_globalaccelerator-action-UpdateAcceleratorAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCrossAccountAttachment  **
  - **IAM action:**  [globalaccelerator:UpdateCrossAccountAttachment](#list_globalaccelerator-action-UpdateCrossAccountAttachment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCustomRoutingAccelerator  **
  - **IAM action:**  [globalaccelerator:UpdateCustomRoutingAccelerator](#list_globalaccelerator-action-UpdateCustomRoutingAccelerator) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCustomRoutingAcceleratorAttributes  **
  - **IAM action:**  [globalaccelerator:UpdateCustomRoutingAcceleratorAttributes](#list_globalaccelerator-action-UpdateCustomRoutingAcceleratorAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCustomRoutingListener  **
  - **IAM action:**  [globalaccelerator:UpdateCustomRoutingListener](#list_globalaccelerator-action-UpdateCustomRoutingListener) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEndpointGroup  **
  - **IAM action:**  [globalaccelerator:UpdateEndpointGroup](#list_globalaccelerator-action-UpdateEndpointGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateListener  **
  - **IAM action:**  [globalaccelerator:UpdateListener](#list_globalaccelerator-action-UpdateListener) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   WithdrawByoipCidr  **
  - **IAM action:**  [globalaccelerator:WithdrawByoipCidr](#list_globalaccelerator-action-WithdrawByoipCidr) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Global Accelerator
<a name="list_globalaccelerator-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddCustomRoutingEndpoints](https://docs.aws.amazon.com/global-accelerator/latest/api/API_AddCustomRoutingEndpoints.html)  **
  - **Description:** Grants permission to add a virtual private cloud (VPC) subnet endpoint to a custom routing accelerator endpoint group
  - **Resource types (\*required):** [endpointgroup\*](#list_globalaccelerator-resource-endpointgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AddEndpoints](https://docs.aws.amazon.com/global-accelerator/latest/api/API_AddEndpoints.html)  **
  - **Description:** Grants permission to add an endpoint to a standard accelerator endpoint group
  - **Resource types (\*required):** [endpointgroup\*](#list_globalaccelerator-resource-endpointgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AdvertiseByoipCidr](https://docs.aws.amazon.com/global-accelerator/latest/api/API_AdvertiseByoipCidr.html)  **
  - **Description:** Grants permission to advertises an IPv4 address range that is provisioned for use with your accelerator through bring your own IP addresses (BYOIP)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [AllowCustomRoutingTraffic](https://docs.aws.amazon.com/global-accelerator/latest/api/API_AllowCustomRoutingTraffic.html)  **
  - **Description:** Grants permission to allows custom routing of user traffic to a private destination IP:PORT in a specific VPC subnet
  - **Resource types (\*required):** [endpointgroup\*](#list_globalaccelerator-resource-endpointgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAccelerator](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CreateAccelerator.html)  **
  - **Description:** Grants permission to create a standard accelerator
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_globalaccelerator-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_globalaccelerator-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCrossAccountAttachment](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CreateCrossAccountAttachment.html)  **
  - **Description:** Grants permission to create a CrossAccountAttachment
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_globalaccelerator-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_globalaccelerator-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCustomRoutingAccelerator](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CreateCustomRoutingAccelerator.html)  **
  - **Description:** Grants permission to create a Custom Routing accelerator
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_globalaccelerator-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_globalaccelerator-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCustomRoutingEndpointGroup](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CreateCustomRoutingEndpointGroup.html)  **
  - **Description:** Grants permission to create an endpoint group for the specified listener for a custom routing accelerator
  - **Resource types (\*required):** [listener\*](#list_globalaccelerator-resource-listener)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateCustomRoutingListener](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CreateCustomRoutingListener.html)  **
  - **Description:** Grants permission to create a listener to process inbound connections from clients to a custom routing accelerator
  - **Resource types (\*required):** [accelerator\*](#list_globalaccelerator-resource-accelerator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateEndpointGroup](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CreateEndpointGroup.html)  **
  - **Description:** Grants permission to add an endpoint group to a standard accelerator listener
  - **Resource types (\*required):** [listener\*](#list_globalaccelerator-resource-listener)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateListener](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CreateListener.html)  **
  - **Description:** Grants permission to add a listener to a standard accelerator
  - **Resource types (\*required):** [accelerator\*](#list_globalaccelerator-resource-accelerator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAccelerator](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DeleteAccelerator.html)  **
  - **Description:** Grants permission to delete a standard accelerator
  - **Resource types (\*required):** [accelerator\*](#list_globalaccelerator-resource-accelerator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCrossAccountAttachment](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DeleteCrossAccountAttachment.html)  **
  - **Description:** Grants permission to delete a CrossAccountAttachment
  - **Resource types (\*required):** [attachment\*](#list_globalaccelerator-resource-attachment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCustomRoutingAccelerator](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DeleteCustomRoutingAccelerator.html)  **
  - **Description:** Grants permission to delete a custom routing accelerator
  - **Resource types (\*required):** [accelerator\*](#list_globalaccelerator-resource-accelerator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCustomRoutingEndpointGroup](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DeleteCustomRoutingEndpointGroup.html)  **
  - **Description:** Grants permission to delete an endpoint group from a listener for a custom routing accelerator
  - **Resource types (\*required):** [endpointgroup\*](#list_globalaccelerator-resource-endpointgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCustomRoutingListener](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DeleteCustomRoutingListener.html)  **
  - **Description:** Grants permission to delete a listener for a custom routing accelerator
  - **Resource types (\*required):** [listener\*](#list_globalaccelerator-resource-listener)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEndpointGroup](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DeleteEndpointGroup.html)  **
  - **Description:** Grants permission to delete an endpoint group associated with a standard accelerator listener
  - **Resource types (\*required):** [endpointgroup\*](#list_globalaccelerator-resource-endpointgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteListener](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DeleteListener.html)  **
  - **Description:** Grants permission to delete a listener from a standard accelerator
  - **Resource types (\*required):** [listener\*](#list_globalaccelerator-resource-listener)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DenyCustomRoutingTraffic](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DenyCustomRoutingTraffic.html)  **
  - **Description:** Grants permission to disallows custom routing of user traffic to a private destination IP:PORT in a specific VPC subnet
  - **Resource types (\*required):** [endpointgroup\*](#list_globalaccelerator-resource-endpointgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeprovisionByoipCidr](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DeprovisionByoipCidr.html)  **
  - **Description:** Grants permission to releases the specified address range that you provisioned for use with your accelerator through bring your own IP addresses (BYOIP)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeAccelerator](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DescribeAccelerator.html)  **
  - **Description:** Grants permissions to describe a standard accelerator
  - **Resource types (\*required):** [accelerator\*](#list_globalaccelerator-resource-accelerator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAcceleratorAttributes](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DescribeAcceleratorAttributes.html)  **
  - **Description:** Grants permission to describe a standard accelerator attributes
  - **Resource types (\*required):** [accelerator\*](#list_globalaccelerator-resource-accelerator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCrossAccountAttachment](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DescribeCrossAccountAttachment.html)  **
  - **Description:** Grants permissions to describe a CrossAccountAttachment
  - **Resource types (\*required):** [attachment\*](#list_globalaccelerator-resource-attachment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCustomRoutingAccelerator](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DescribeCustomRoutingAccelerator.html)  **
  - **Description:** Grants permission to describe a custom routing accelerator
  - **Resource types (\*required):** [accelerator\*](#list_globalaccelerator-resource-accelerator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCustomRoutingAcceleratorAttributes](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DescribeCustomRoutingAcceleratorAttributes.html)  **
  - **Description:** Grants permission to describe the attributes of a custom routing accelerator
  - **Resource types (\*required):** [accelerator\*](#list_globalaccelerator-resource-accelerator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCustomRoutingEndpointGroup](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DescribeCustomRoutingEndpointGroup.html)  **
  - **Description:** Grants permission to describe an endpoint group for a custom routing accelerator
  - **Resource types (\*required):** [endpointgroup\*](#list_globalaccelerator-resource-endpointgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCustomRoutingListener](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DescribeCustomRoutingListener.html)  **
  - **Description:** Grants permission to describe a listener for a custom routing accelerator
  - **Resource types (\*required):** [listener\*](#list_globalaccelerator-resource-listener)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeEndpointGroup](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DescribeEndpointGroup.html)  **
  - **Description:** Grants permission to describe a standard accelerator endpoint group
  - **Resource types (\*required):** [endpointgroup\*](#list_globalaccelerator-resource-endpointgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeListener](https://docs.aws.amazon.com/global-accelerator/latest/api/API_DescribeListener.html)  **
  - **Description:** Grants permission to describe a standard accelerator listener
  - **Resource types (\*required):** [listener\*](#list_globalaccelerator-resource-listener)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAccelerators](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListAccelerators.html)  **
  - **Description:** Grants permission to list all standard accelerators
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListByoipCidrs](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListByoipCidrs.html)  **
  - **Description:** Grants permission to list the BYOIP cidrs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCrossAccountAttachments](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListCrossAccountAttachments.html)  **
  - **Description:** Grants permission to list all CrossAccountAttachments
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCrossAccountResourceAccounts](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListCrossAccountResourceAccounts.html)  **
  - **Description:** Grants permission to list accounts with CrossAccountAttachments listing caller as a principal
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCrossAccountResources](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListCrossAccountResources.html)  **
  - **Description:** Grants permission to list all CrossAccountAttachment resources usable by caller
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCustomRoutingAccelerators](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListCustomRoutingAccelerators.html)  **
  - **Description:** Grants permission to list the custom routing accelerators for an AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCustomRoutingEndpointGroups](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListCustomRoutingEndpointGroups.html)  **
  - **Description:** Grants permission to list the endpoint groups that are associated with a listener for a custom routing accelerator
  - **Resource types (\*required):** [listener\*](#list_globalaccelerator-resource-listener)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCustomRoutingListeners](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListCustomRoutingListeners.html)  **
  - **Description:** Grants permission to list the listeners for a custom routing accelerator
  - **Resource types (\*required):** [accelerator\*](#list_globalaccelerator-resource-accelerator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCustomRoutingPortMappings](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListCustomRoutingPortMappings.html)  **
  - **Description:** Grants permission to list the port mappings for a custom routing accelerator
  - **Resource types (\*required):** [accelerator\*](#list_globalaccelerator-resource-accelerator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCustomRoutingPortMappingsByDestination](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListCustomRoutingPortMappingsByDestination.html)  **
  - **Description:** Grants permission to list the port mappings for a specific endpoint IP address (a destination address) in a subnet
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEndpointGroups](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListEndpointGroups.html)  **
  - **Description:** Grants permission to list all endpoint groups associated with a standard accelerator listener
  - **Resource types (\*required):** [listener\*](#list_globalaccelerator-resource-listener)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListListeners](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListListeners.html)  **
  - **Description:** Grants permission to list all listeners associated with a standard accelerator
  - **Resource types (\*required):** [accelerator\*](#list_globalaccelerator-resource-accelerator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a globalaccelerator resource
  - **Resource types (\*required):** [accelerator](#list_globalaccelerator-resource-accelerator) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [attachment](#list_globalaccelerator-resource-attachment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ProvisionByoipCidr](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ProvisionByoipCidr.html)  **
  - **Description:** Grants permission to provisions an address range for use with your accelerator through bring your own IP addresses (BYOIP)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RemoveCustomRoutingEndpoints](https://docs.aws.amazon.com/global-accelerator/latest/api/API_RemoveCustomRoutingEndpoints.html)  **
  - **Description:** Grants permission to remove virtual private cloud (VPC) subnet endpoints from a custom routing accelerator endpoint group
  - **Resource types (\*required):** [endpointgroup\*](#list_globalaccelerator-resource-endpointgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RemoveEndpoints](https://docs.aws.amazon.com/global-accelerator/latest/api/API_RemoveEndpoints.html)  **
  - **Description:** Grants permission to remove an endpoint from a standard accelerator endpoint group
  - **Resource types (\*required):** [endpointgroup\*](#list_globalaccelerator-resource-endpointgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/global-accelerator/latest/api/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a globalaccelerator resource
  - **Resource types (\*required):** [accelerator](#list_globalaccelerator-resource-accelerator) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_globalaccelerator-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_globalaccelerator-aws_TagKeys)
  - **Resource types (\*required):** [attachment](#list_globalaccelerator-resource-attachment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_globalaccelerator-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_globalaccelerator-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/global-accelerator/latest/api/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a globalaccelerator resource
  - **Resource types (\*required):** [accelerator](#list_globalaccelerator-resource-accelerator) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_globalaccelerator-aws_TagKeys)
  - **Resource types (\*required):** [attachment](#list_globalaccelerator-resource-attachment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_globalaccelerator-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAccelerator](https://docs.aws.amazon.com/global-accelerator/latest/api/API_UpdateAccelerator.html)  **
  - **Description:** Grants permission to update a standard accelerator
  - **Resource types (\*required):** [accelerator\*](#list_globalaccelerator-resource-accelerator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAcceleratorAttributes](https://docs.aws.amazon.com/global-accelerator/latest/api/API_UpdateAcceleratorAttributes.html)  **
  - **Description:** Grants permission to update a standard accelerator attributes
  - **Resource types (\*required):** [accelerator\*](#list_globalaccelerator-resource-accelerator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCrossAccountAttachment](https://docs.aws.amazon.com/global-accelerator/latest/api/API_UpdateCrossAccountAttachment.html)  **
  - **Description:** Grants permission to update a CrossAccountAttachment
  - **Resource types (\*required):** [attachment\*](#list_globalaccelerator-resource-attachment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCustomRoutingAccelerator](https://docs.aws.amazon.com/global-accelerator/latest/api/API_UpdateCustomRoutingAccelerator.html)  **
  - **Description:** Grants permission to update a custom routing accelerator
  - **Resource types (\*required):** [accelerator\*](#list_globalaccelerator-resource-accelerator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCustomRoutingAcceleratorAttributes](https://docs.aws.amazon.com/global-accelerator/latest/api/API_UpdateCustomRoutingAcceleratorAttributes.html)  **
  - **Description:** Grants permission to update the attributes for a custom routing accelerator
  - **Resource types (\*required):** [accelerator\*](#list_globalaccelerator-resource-accelerator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCustomRoutingListener](https://docs.aws.amazon.com/global-accelerator/latest/api/API_UpdateCustomRoutingListener.html)  **
  - **Description:** Grants permission to update a listener for a custom routing accelerator
  - **Resource types (\*required):** [listener\*](#list_globalaccelerator-resource-listener)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateEndpointGroup](https://docs.aws.amazon.com/global-accelerator/latest/api/API_UpdateEndpointGroup.html)  **
  - **Description:** Grants permission to update an endpoint group on a standard accelerator listener
  - **Resource types (\*required):** [endpointgroup\*](#list_globalaccelerator-resource-endpointgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateListener](https://docs.aws.amazon.com/global-accelerator/latest/api/API_UpdateListener.html)  **
  - **Description:** Grants permission to update a listener on a standard accelerator
  - **Resource types (\*required):** [listener\*](#list_globalaccelerator-resource-listener)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [WithdrawByoipCidr](https://docs.aws.amazon.com/global-accelerator/latest/api/API_WithdrawByoipCidr.html)  **
  - **Description:** Grants permission to stops advertising a BYOIP IPv4 address
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by AWS Global Accelerator
<a name="list_globalaccelerator-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [accelerator](https://docs.aws.amazon.com/global-accelerator/latest/api/API_Accelerator.html)  | arn:${Partition}:globalaccelerator::${Account}:accelerator/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_) | 
|  [attachment](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CrossAccountAttachment.html)  | arn:${Partition}:globalaccelerator::${Account}:attachment/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_) | 
|  [endpointgroup](https://docs.aws.amazon.com/global-accelerator/latest/api/API_EndpointGroup.html)  | arn:${Partition}:globalaccelerator::${Account}:accelerator/${ResourceId}/listener/${ListenerId}/endpoint-group/${EndpointGroupId} | [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_) | 
|  [listener](https://docs.aws.amazon.com/global-accelerator/latest/api/API_Listener.html)  | arn:${Partition}:globalaccelerator::${Account}:accelerator/${ResourceId}/listener/${ListenerId} | [aws:ResourceTag/${TagKey}](#list_globalaccelerator-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Global Accelerator
<a name="list_globalaccelerator-policy-keys"></a>

AWS Global Accelerator defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 