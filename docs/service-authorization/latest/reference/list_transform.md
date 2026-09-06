

# Actions, resources, and condition keys for AWS Transform
<a name="list_transform"></a>

AWS Transform (service prefix: `transform`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/transform/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/transform/latest/userguide/security_iam_permissions.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/transform/latest/userguide/security-iam.html#security_iam_access-manage) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/transform/transform.json) for this service.

**Topics**
+ [Actions defined by AWS Transform](#list_transform-actions-as-permissions)
+ [Permission-only actions for AWS Transform](#list_transform-permission-only-actions)
+ [Resource types defined by AWS Transform](#list_transform-resources-for-iam-policies)
+ [Condition keys for AWS Transform](#list_transform-policy-keys)

## Actions defined by AWS Transform
<a name="list_transform-actions-as-permissions"></a>

AWS Transform has no API operations that can be used in the `Actions` element of an IAM policy statement.

## Permission-only actions for AWS Transform
<a name="list_transform-permission-only-actions"></a>

The following actions are defined by AWS Transform but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AccessTransformProfile](https://docs.aws.amazon.com/transform/latest/userguide/security_iam_permissions.html)  **
  - **Description:** Grants permission to invoke AccessTransformProfile on AWS Transform
  - **Resource types (\*required):** [profile\*](#list_transform-resource-profile)
  - **Condition keys:**  
  - **Access level:** Write

- **   [AssociateConnectorResource](https://docs.aws.amazon.com/transform/latest/userguide/security_iam_permissions.html)  **
  - **Description:** Grants permission to invoke AssociateConnectorResource on AWS Transform
  - **Resource types (\*required):** [connector\*](#list_transform-resource-connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateProfile](https://docs.aws.amazon.com/transform/latest/userguide/security_iam_permissions.html)  **
  - **Description:** Grants permission to invoke CreateProfile on AWS Transform
  - **Resource types (\*required):** [profile\*](#list_transform-resource-profile)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteAgentRuntimeConfiguration](https://docs.aws.amazon.com/transform/latest/userguide/security_iam_permissions.html)  **
  - **Description:** Grants permission to invoke DeleteAgentRuntimeConfiguration on AWS Transform
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteConnector](https://docs.aws.amazon.com/transform/latest/userguide/security_iam_permissions.html)  **
  - **Description:** Grants permission to invoke DeleteConnector on AWS Transform
  - **Resource types (\*required):** [connector\*](#list_transform-resource-connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProfile](https://docs.aws.amazon.com/transform/latest/userguide/security_iam_permissions.html)  **
  - **Description:** Grants permission to invoke DeleteProfile on AWS Transform
  - **Resource types (\*required):** [profile\*](#list_transform-resource-profile)
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetAccountSettings](https://docs.aws.amazon.com/transform/latest/userguide/security_iam_permissions.html)  **
  - **Description:** Grants permission to invoke GetAccountSettings on AWS Transform
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAgent](https://docs.aws.amazon.com/transform/latest/userguide/security_iam_permissions.html)  **
  - **Description:** Grants permission to invoke GetAgent on AWS Transform
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAgentRuntimeConfiguration](https://docs.aws.amazon.com/transform/latest/userguide/security_iam_permissions.html)  **
  - **Description:** Grants permission to invoke GetAgentRuntimeConfiguration on AWS Transform
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetConnector](https://docs.aws.amazon.com/transform/latest/userguide/security_iam_permissions.html)  **
  - **Description:** Grants permission to invoke GetConnector on AWS Transform
  - **Resource types (\*required):** [connector\*](#list_transform-resource-connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWebAppUrl](https://docs.aws.amazon.com/transform/latest/userguide/security_iam_permissions.html)  **
  - **Description:** Grants permission to invoke GetWebAppUrl on AWS Transform
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListAgents](https://docs.aws.amazon.com/transform/latest/userguide/security_iam_permissions.html)  **
  - **Description:** Grants permission to invoke ListAgents on AWS Transform
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListConnectors](https://docs.aws.amazon.com/transform/latest/userguide/security_iam_permissions.html)  **
  - **Description:** Grants permission to invoke ListConnectors on AWS Transform
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListProfiles](https://docs.aws.amazon.com/transform/latest/userguide/security_iam_permissions.html)  **
  - **Description:** Grants permission to invoke ListProfiles on AWS Transform
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/transform/latest/userguide/security_iam_permissions.html)  **
  - **Description:** Grants permission to invoke ListTagsForResource on AWS Transform
  - **Resource types (\*required):** [connector\*](#list_transform-resource-connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutAgentRuntimeConfiguration](https://docs.aws.amazon.com/transform/latest/userguide/security_iam_permissions.html)  **
  - **Description:** Grants permission to invoke PutAgentRuntimeConfiguration on AWS Transform
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RejectConnector](https://docs.aws.amazon.com/transform/latest/userguide/security_iam_permissions.html)  **
  - **Description:** Grants permission to invoke RejectConnector on AWS Transform
  - **Resource types (\*required):** [connector\*](#list_transform-resource-connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/transform/latest/userguide/security_iam_permissions.html)  **
  - **Description:** Grants permission to invoke TagResource on AWS Transform
  - **Resource types (\*required):** [connector\*](#list_transform-resource-connector)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_transform-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transform-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transform-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/transform/latest/userguide/security_iam_permissions.html)  **
  - **Description:** Grants permission to invoke UntagResource on AWS Transform
  - **Resource types (\*required):** [connector\*](#list_transform-resource-connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transform-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAccountSettings](https://docs.aws.amazon.com/transform/latest/userguide/security_iam_permissions.html)  **
  - **Description:** Grants permission to invoke UpdateAccountSettings on AWS Transform
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateAgentAccess](https://docs.aws.amazon.com/transform/latest/userguide/security_iam_permissions.html)  **
  - **Description:** Grants permission to invoke UpdateAgentAccess on AWS Transform
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateProfile](https://docs.aws.amazon.com/transform/latest/userguide/security_iam_permissions.html)  **
  - **Description:** Grants permission to invoke UpdateProfile on AWS Transform
  - **Resource types (\*required):** [profile\*](#list_transform-resource-profile)
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by AWS Transform
<a name="list_transform-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [connector](https://docs.aws.amazon.com/transform/latest/userguide/security_iam_permissions.html)  | arn:${Partition}:transform:${Region}:${Account}:connector/${WorkspaceId}/${ConnectorId} | [aws:ResourceTag/${TagKey}](#list_transform-aws_ResourceTag___TagKey_) | 
|  [profile](https://docs.aws.amazon.com/transform/latest/userguide/security_iam_permissions.html)  | arn:${Partition}:transform:${Region}:${Account}:profile/${Identifier} |   | 

## Condition keys for AWS Transform
<a name="list_transform-policy-keys"></a>

AWS Transform defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 