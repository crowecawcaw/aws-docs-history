

# Actions, resources, and condition keys for AWS service providing managed private networks
<a name="list_private-networks"></a>

AWS service providing managed private networks (service prefix: `private-networks`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/private-networks/latest/userguide/how-private-5g-works.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/private-networks/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/private-networks/latest/userguide/identity-access-management.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/private-networks/private-networks.json) for this service.

**Topics**
+ [Actions defined by AWS service providing managed private networks](#list_private-networks-actions-as-permissions)
+ [Resource types defined by AWS service providing managed private networks](#list_private-networks-resources-for-iam-policies)
+ [Condition keys for AWS service providing managed private networks](#list_private-networks-policy-keys)

## Actions defined by AWS service providing managed private networks
<a name="list_private-networks-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcknowledgeOrderReceipt](https://docs.aws.amazon.com/private-networks/latest/APIReference/API_AcknowledgeOrderReceipt.html)  **
  - **Description:** Grants permission to acknowledge that an order has been received
  - **Resource types (\*required):** [order\*](#list_private-networks-resource-order)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ActivateDeviceIdentifier](https://docs.aws.amazon.com/private-networks/latest/APIReference/API_ActivateDeviceIdentifier.html)  **
  - **Description:** Grants permission to activate a device identifier
  - **Resource types (\*required):** [device-identifier\*](#list_private-networks-resource-device-identifier)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ActivateNetworkSite](https://docs.aws.amazon.com/private-networks/latest/APIReference/API_ActivateNetworkSite.html)  **
  - **Description:** Grants permission to activate a network site
  - **Resource types (\*required):** [network-site\*](#list_private-networks-resource-network-site) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_private-networks-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_private-networks-aws_TagKeys)
  - **Resource types (\*required):** [order\*](#list_private-networks-resource-order) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_private-networks-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_private-networks-aws_TagKeys)
  - **Access level:** Write

- **   [ConfigureAccessPoint](https://docs.aws.amazon.com/private-networks/latest/APIReference/API_ConfigureAccessPoint.html)  **
  - **Description:** Grants permission to configure an access point
  - **Resource types (\*required):** [network-resource\*](#list_private-networks-resource-network-resource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateNetwork](https://docs.aws.amazon.com/private-networks/latest/APIReference/API_CreateNetwork.html)  **
  - **Description:** Grants permission to create a network
  - **Resource types (\*required):** [network\*](#list_private-networks-resource-network)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_private-networks-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_private-networks-aws_TagKeys)
  - **Access level:** Write

- **   [CreateNetworkSite](https://docs.aws.amazon.com/private-networks/latest/APIReference/API_CreateNetworkSite.html)  **
  - **Description:** Grants permission to create a network site
  - **Resource types (\*required):** [network\*](#list_private-networks-resource-network)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_private-networks-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_private-networks-aws_TagKeys)
  - **Access level:** Write

- **   [DeactivateDeviceIdentifier](https://docs.aws.amazon.com/private-networks/latest/APIReference/API_DeactivateDeviceIdentifier.html)  **
  - **Description:** Grants permission to deactivate a device identifier
  - **Resource types (\*required):** [device-identifier\*](#list_private-networks-resource-device-identifier)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteNetwork](https://docs.aws.amazon.com/private-networks/latest/APIReference/API_DeleteNetwork.html)  **
  - **Description:** Grants permission to delete a network
  - **Resource types (\*required):** [network\*](#list_private-networks-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteNetworkSite](https://docs.aws.amazon.com/private-networks/latest/APIReference/API_DeleteNetworkSite.html)  **
  - **Description:** Grants permission to delete a network site
  - **Resource types (\*required):** [network-site\*](#list_private-networks-resource-network-site)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetDeviceIdentifier](https://docs.aws.amazon.com/private-networks/latest/APIReference/API_GetDeviceIdentifier.html)  **
  - **Description:** Grants permission to get a device identifier
  - **Resource types (\*required):** [device-identifier\*](#list_private-networks-resource-device-identifier)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetNetwork](https://docs.aws.amazon.com/private-networks/latest/APIReference/API_GetNetwork.html)  **
  - **Description:** Grants permission to get a network
  - **Resource types (\*required):** [network\*](#list_private-networks-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetNetworkResource](https://docs.aws.amazon.com/private-networks/latest/APIReference/API_GetNetworkResource.html)  **
  - **Description:** Grants permission to get a network resource
  - **Resource types (\*required):** [network-resource\*](#list_private-networks-resource-network-resource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetNetworkSite](https://docs.aws.amazon.com/private-networks/latest/APIReference/API_GetNetworkSite.html)  **
  - **Description:** Grants permission to get a network site
  - **Resource types (\*required):** [network-site\*](#list_private-networks-resource-network-site)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetOrder](https://docs.aws.amazon.com/private-networks/latest/APIReference/API_GetOrder.html)  **
  - **Description:** Grants permission to get a network order
  - **Resource types (\*required):** [order\*](#list_private-networks-resource-order)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDeviceIdentifiers](https://docs.aws.amazon.com/private-networks/latest/APIReference/API_ListDeviceIdentifiers.html)  **
  - **Description:** Grants permission to list device identifiers
  - **Resource types (\*required):** [network\*](#list_private-networks-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListNetworkResources](https://docs.aws.amazon.com/private-networks/latest/APIReference/API_ListNetworkResources.html)  **
  - **Description:** Grants permission to list network resources
  - **Resource types (\*required):** [network\*](#list_private-networks-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListNetworkSites](https://docs.aws.amazon.com/private-networks/latest/APIReference/API_ListNetworkSites.html)  **
  - **Description:** Grants permission to list network sites
  - **Resource types (\*required):** [network\*](#list_private-networks-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListNetworks](https://docs.aws.amazon.com/private-networks/latest/APIReference/API_ListNetworks.html)  **
  - **Description:** Grants permission to list networks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOrders](https://docs.aws.amazon.com/private-networks/latest/APIReference/API_ListOrders.html)  **
  - **Description:** Grants permission to list network orders
  - **Resource types (\*required):** [network\*](#list_private-networks-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/private-networks/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to return a list of tags for a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [Ping](https://docs.aws.amazon.com/private-networks/latest/APIReference/API_Ping.html)  **
  - **Description:** Grants permission to check the health of the service
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [StartNetworkResourceUpdate](https://docs.aws.amazon.com/private-networks/latest/APIReference/API_StartNetworkResourceUpdate.html)  **
  - **Description:** Grants permission to start an update on the specified network resource
  - **Resource types (\*required):** [network-resource\*](#list_private-networks-resource-network-resource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_private-networks-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_private-networks-aws_TagKeys)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/private-networks/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to adds tags to the specified resource
  - **Resource types (\*required):** [device-identifier](#list_private-networks-resource-device-identifier) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_private-networks-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_private-networks-aws_TagKeys)
  - **Resource types (\*required):** [network](#list_private-networks-resource-network) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_private-networks-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_private-networks-aws_TagKeys)
  - **Resource types (\*required):** [network-resource](#list_private-networks-resource-network-resource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_private-networks-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_private-networks-aws_TagKeys)
  - **Resource types (\*required):** [network-site](#list_private-networks-resource-network-site) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_private-networks-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_private-networks-aws_TagKeys)
  - **Resource types (\*required):** [order](#list_private-networks-resource-order) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_private-networks-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_private-networks-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/private-networks/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to removes tags from the specified resource
  - **Resource types (\*required):** [device-identifier](#list_private-networks-resource-device-identifier) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_private-networks-aws_TagKeys)
  - **Resource types (\*required):** [network](#list_private-networks-resource-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_private-networks-aws_TagKeys)
  - **Resource types (\*required):** [network-resource](#list_private-networks-resource-network-resource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_private-networks-aws_TagKeys)
  - **Resource types (\*required):** [network-site](#list_private-networks-resource-network-site) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_private-networks-aws_TagKeys)
  - **Resource types (\*required):** [order](#list_private-networks-resource-order) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_private-networks-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateNetworkSite](https://docs.aws.amazon.com/private-networks/latest/APIReference/API_UpdateNetworkSite.html)  **
  - **Description:** Grants permission to update a network site
  - **Resource types (\*required):** [network-site\*](#list_private-networks-resource-network-site)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateNetworkSitePlan](https://docs.aws.amazon.com/private-networks/latest/APIReference/API_UpdateNetworkSitePlan.html)  **
  - **Description:** Grants permission to update a plan at a network site
  - **Resource types (\*required):** [network-site\*](#list_private-networks-resource-network-site)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS service providing managed private networks
<a name="list_private-networks-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [device-identifier](https://docs.aws.amazon.com/private-networks/latest/userguide/identity-access-management.html)  | arn:${Partition}:private-networks:${Region}:${Account}:device-identifier/${NetworkName}/${DeviceId} | [aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_) | 
|  [network](https://docs.aws.amazon.com/private-networks/latest/userguide/identity-access-management.html)  | arn:${Partition}:private-networks:${Region}:${Account}:network/${NetworkName} | [aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_) | 
|  [network-resource](https://docs.aws.amazon.com/private-networks/latest/userguide/identity-access-management.html)  | arn:${Partition}:private-networks:${Region}:${Account}:network-resource/${NetworkName}/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_) | 
|  [network-site](https://docs.aws.amazon.com/private-networks/latest/userguide/identity-access-management.html)  | arn:${Partition}:private-networks:${Region}:${Account}:network-site/${NetworkName}/${NetworkSiteName} | [aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_) | 
|  [order](https://docs.aws.amazon.com/private-networks/latest/userguide/identity-access-management.html)  | arn:${Partition}:private-networks:${Region}:${Account}:order/${NetworkName}/${OrderId} | [aws:ResourceTag/${TagKey}](#list_private-networks-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS service providing managed private networks
<a name="list_private-networks-policy-keys"></a>

AWS service providing managed private networks defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by checking the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by checking tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by presence of tag keys in the request | ArrayOfString | 