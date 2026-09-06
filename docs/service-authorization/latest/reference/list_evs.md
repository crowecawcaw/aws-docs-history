

# Actions, resources, and condition keys for Amazon Elastic VMware Service
<a name="list_evs"></a>

Amazon Elastic VMware Service (service prefix: `evs`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/evs/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/evs/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/evs/latest/userguide/security-iam.html#security-iam-access-manage) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/evs/evs.json) for this service.

**Topics**
+ [API operations defined by Amazon Elastic VMware Service](#list_evs-operations)
+ [Actions defined by Amazon Elastic VMware Service](#list_evs-actions-as-permissions)
+ [Resource types defined by Amazon Elastic VMware Service](#list_evs-resources-for-iam-policies)
+ [Condition keys for Amazon Elastic VMware Service](#list_evs-policy-keys)

## API operations defined by Amazon Elastic VMware Service
<a name="list_evs-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_evs-actions-as-permissions).




- **   AssociateEipToVlan  **
  - **IAM action:**  [evs:AssociateEipToVlan](#list_evs-action-AssociateEipToVlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateEntitlement  **
  - **IAM action:**  [evs:CreateEntitlement](#list_evs-action-CreateEntitlement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateEnvironment  **
  - **IAM action:**  [evs:CreateEnvironment](#list_evs-action-CreateEnvironment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [evs:TagResource](#list_evs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateEnvironmentConnector  **
  - **IAM action:**  [evs:CreateEnvironmentConnector](#list_evs-action-CreateEnvironmentConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateEnvironmentHost  **
  - **IAM action:**  [evs:CreateEnvironmentHost](#list_evs-action-CreateEnvironmentHost) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEntitlement  **
  - **IAM action:**  [evs:DeleteEntitlement](#list_evs-action-DeleteEntitlement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEnvironment  **
  - **IAM action:**  [evs:DeleteEnvironment](#list_evs-action-DeleteEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEnvironmentConnector  **
  - **IAM action:**  [evs:DeleteEnvironmentConnector](#list_evs-action-DeleteEnvironmentConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEnvironmentHost  **
  - **IAM action:**  [evs:DeleteEnvironmentHost](#list_evs-action-DeleteEnvironmentHost) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateEipFromVlan  **
  - **IAM action:**  [evs:DisassociateEipFromVlan](#list_evs-action-DisassociateEipFromVlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAccountSettings  **
  - **IAM action:**  [evs:GetAccountSettings](#list_evs-action-GetAccountSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDepotUrl  **
  - **IAM action:**  [evs:GetDepotUrl](#list_evs-action-GetDepotUrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEnvironment  **
  - **IAM action:**  [evs:GetEnvironment](#list_evs-action-GetEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetVersions  **
  - **IAM action:**  [evs:GetVersions](#list_evs-action-GetVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListEnvironmentConnectors  **
  - **IAM action:**  [evs:ListEnvironmentConnectors](#list_evs-action-ListEnvironmentConnectors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEnvironmentHosts  **
  - **IAM action:**  [evs:ListEnvironmentHosts](#list_evs-action-ListEnvironmentHosts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEnvironmentVlans  **
  - **IAM action:**  [evs:ListEnvironmentVlans](#list_evs-action-ListEnvironmentVlans) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEnvironments  **
  - **IAM action:**  [evs:ListEnvironments](#list_evs-action-ListEnvironments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [evs:ListTagsForResource](#list_evs-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListVmEntitlements  **
  - **IAM action:**  [evs:ListVmEntitlements](#list_evs-action-ListVmEntitlements) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutAccountSettings  **
  - **IAM action:**  [evs:PutAccountSettings](#list_evs-action-PutAccountSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [evs:TagResource](#list_evs-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [evs:UntagResource](#list_evs-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateEnvironmentConnector  **
  - **IAM action:**  [evs:UpdateEnvironmentConnector](#list_evs-action-UpdateEnvironmentConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Elastic VMware Service
<a name="list_evs-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateEipToVlan](https://docs.aws.amazon.com/evs/latest/APIReference/API_AssociateEipToVlan.html)  **
  - **Description:** Grants permission to associate an Elastic IP address (EIP) with a public VLAN in an Amazon EVS environment
  - **Resource types (\*required):** [environment\*](#list_evs-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateEntitlement](https://docs.aws.amazon.com/evs/latest/APIReference/API_CreateEntitlement.html)  **
  - **Description:** Grants permission to create an entitlement in an Amazon EVS environment
  - **Resource types (\*required):** [environment\*](#list_evs-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateEnvironment](https://docs.aws.amazon.com/evs/latest/APIReference/API_CreateEnvironment.html)  **
  - **Description:** Grants permission to create an Amazon EVS environment
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_evs-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_evs-aws_TagKeys)
  - **Access level:** Write

- **   [CreateEnvironmentConnector](https://docs.aws.amazon.com/evs/latest/APIReference/API_CreateEnvironmentConnector.html)  **
  - **Description:** Grants permission to create a connector in an Amazon EVS environment
  - **Resource types (\*required):** [environment\*](#list_evs-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateEnvironmentHost](https://docs.aws.amazon.com/evs/latest/APIReference/API_CreateEnvironmentHost.html)  **
  - **Description:** Grants permission to add host to an Amazon EVS environment
  - **Resource types (\*required):** [environment\*](#list_evs-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEntitlement](https://docs.aws.amazon.com/evs/latest/APIReference/API_DeleteEntitlement.html)  **
  - **Description:** Grants permission to delete an entitlement from an Amazon EVS environment
  - **Resource types (\*required):** [environment\*](#list_evs-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEnvironment](https://docs.aws.amazon.com/evs/latest/APIReference/API_DeleteEnvironment.html)  **
  - **Description:** Grants permission to delete an Amazon EVS environment
  - **Resource types (\*required):** [environment\*](#list_evs-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEnvironmentConnector](https://docs.aws.amazon.com/evs/latest/APIReference/API_DeleteEnvironmentConnector.html)  **
  - **Description:** Grants permission to delete a connector from an Amazon EVS environment
  - **Resource types (\*required):** [environment\*](#list_evs-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEnvironmentHost](https://docs.aws.amazon.com/evs/latest/APIReference/API_DeleteEnvironmentHost.html)  **
  - **Description:** Grants permission to delete a host from an Amazon EVS environment
  - **Resource types (\*required):** [environment\*](#list_evs-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateEipFromVlan](https://docs.aws.amazon.com/evs/latest/APIReference/API_DisassociateEipFromVlan.html)  **
  - **Description:** Grants permission to disassociate an Elastic IP address (EIP) from a public VLAN in an Amazon EVS environment
  - **Resource types (\*required):** [environment\*](#list_evs-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAccountSettings](https://docs.aws.amazon.com/evs/latest/APIReference/API_GetAccountSettings.html)  **
  - **Description:** Grants permission to get EVS account settings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDepotUrl](https://docs.aws.amazon.com/evs/latest/APIReference/API_GetDepotUrl.html)  **
  - **Description:** Grants permission to get an Amazon EVS environment depot url
  - **Resource types (\*required):** [environment\*](#list_evs-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEnvironment](https://docs.aws.amazon.com/evs/latest/APIReference/API_GetEnvironment.html)  **
  - **Description:** Grants permission to get an Amazon EVS environment
  - **Resource types (\*required):** [environment\*](#list_evs-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetVersions](https://docs.aws.amazon.com/evs/latest/APIReference/API_GetVersions.html)  **
  - **Description:** Grants permission to get versions provided for launch by Amazon EVS
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListEnvironmentConnectors](https://docs.aws.amazon.com/evs/latest/APIReference/API_ListEnvironmentConnectors.html)  **
  - **Description:** Grants permission to retrieve a list of connectors associated with an Amazon EVS environment
  - **Resource types (\*required):** [environment\*](#list_evs-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evs-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListEnvironmentHosts](https://docs.aws.amazon.com/evs/latest/APIReference/API_ListEnvironmentHosts.html)  **
  - **Description:** Grants permission to retrieve a list of hosts associated with an Amazon EVS environment
  - **Resource types (\*required):** [environment\*](#list_evs-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evs-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListEnvironmentVlans](https://docs.aws.amazon.com/evs/latest/APIReference/API_ListEnvironmentVlans.html)  **
  - **Description:** Grants permission to retrieve a list of Amazon EVS environment VLANs
  - **Resource types (\*required):** [environment\*](#list_evs-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evs-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListEnvironments](https://docs.aws.amazon.com/evs/latest/APIReference/API_ListEnvironments.html)  **
  - **Description:** Grants permission to retrieve a list of Amazon EVS environments in an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/evs/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags on a specified resource ARN
  - **Resource types (\*required):** [environment](#list_evs-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListVmEntitlements](https://docs.aws.amazon.com/evs/latest/APIReference/API_ListVmEntitlements.html)  **
  - **Description:** Grants permission to retrieve a list of entitlements associated with an Amazon EVS environment
  - **Resource types (\*required):** [environment\*](#list_evs-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evs-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [PutAccountSettings](https://docs.aws.amazon.com/evs/latest/APIReference/API_PutAccountSettings.html)  **
  - **Description:** Grants permission to get EVS account settings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/evs/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a specified resource ARN
  - **Resource types (\*required):** [environment\*](#list_evs-resource-environment)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_evs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_evs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_evs-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/evs/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a specified resource ARN
  - **Resource types (\*required):** [environment\*](#list_evs-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_evs-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateEnvironmentConnector](https://docs.aws.amazon.com/evs/latest/APIReference/API_UpdateEnvironmentConnector.html)  **
  - **Description:** Grants permission to update a connector in an Amazon EVS environment
  - **Resource types (\*required):** [environment\*](#list_evs-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evs-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Elastic VMware Service
<a name="list_evs-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [environment](https://docs.aws.amazon.com/evs/latest/userguide/concepts.html#concepts-evs-virt-env)  | arn:${Partition}:evs:${Region}:${Account}:environment/${EnvironmentIdentifier} | [aws:ResourceTag/${TagKey}](#list_evs-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Elastic VMware Service
<a name="list_evs-policy-keys"></a>

Amazon Elastic VMware Service defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/evs/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by a tag key and value pair that is allowed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/evs/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by a tag key and value pair of a resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/evs/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by a list of tag keys that are allowed in the request | ArrayOfString | 