

# Actions, resources, and condition keys for AWS Interconnect
<a name="list_interconnect"></a>

AWS Interconnect (service prefix: `interconnect`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/interconnect/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/interconnect/latest/api/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/interconnect/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/interconnect/interconnect.json) for this service.

**Topics**
+ [API operations defined by AWS Interconnect](#list_interconnect-operations)
+ [Actions defined by AWS Interconnect](#list_interconnect-actions-as-permissions)
+ [Resource types defined by AWS Interconnect](#list_interconnect-resources-for-iam-policies)
+ [Condition keys for AWS Interconnect](#list_interconnect-policy-keys)

## API operations defined by AWS Interconnect
<a name="list_interconnect-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_interconnect-actions-as-permissions).




- **   AcceptConnectionProposal  **
  - **IAM action:**  [interconnect:AcceptConnectionProposal](#list_interconnect-action-AcceptConnectionProposal)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [interconnect:TagResource](#list_interconnect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateConnection  **
  - **IAM action:**  [interconnect:CreateConnection](#list_interconnect-action-CreateConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [interconnect:TagResource](#list_interconnect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteConnection  **
  - **IAM action:**  [interconnect:DeleteConnection](#list_interconnect-action-DeleteConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeConnectionProposal  **
  - **IAM action:**  [interconnect:DescribeConnectionProposal](#list_interconnect-action-DescribeConnectionProposal) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConnection  **
  - **IAM action:**  [interconnect:GetConnection](#list_interconnect-action-GetConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEnvironment  **
  - **IAM action:**  [interconnect:GetEnvironment](#list_interconnect-action-GetEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAttachPoints  **
  - **IAM action:**  [interconnect:ListAttachPoints](#list_interconnect-action-ListAttachPoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListConnections  **
  - **IAM action:**  [interconnect:ListConnections](#list_interconnect-action-ListConnections) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEnvironments  **
  - **IAM action:**  [interconnect:ListEnvironments](#list_interconnect-action-ListEnvironments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [interconnect:ListTagsForResource](#list_interconnect-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [interconnect:TagResource](#list_interconnect-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [interconnect:UntagResource](#list_interconnect-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateConnection  **
  - **IAM action:**  [interconnect:UpdateConnection](#list_interconnect-action-UpdateConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Interconnect
<a name="list_interconnect-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptConnectionProposal](https://docs.aws.amazon.com/interconnect/latest/api/API_AcceptConnectionProposal.html)  **
  - **Description:** Grants permission to accept a connection proposal generated elsewhere
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_interconnect-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_interconnect-aws_TagKeys)
  - **Access level:** Write

- **   [CreateConnection](https://docs.aws.amazon.com/interconnect/latest/api/API_CreateConnection.html)  **
  - **Description:** Grants permission to create a connection
  - **Resource types (\*required):** [connection\*](#list_interconnect-resource-connection)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_interconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interconnect-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteConnection](https://docs.aws.amazon.com/interconnect/latest/api/API_DeleteConnection.html)  **
  - **Description:** Grants permission to delete an existing connection
  - **Resource types (\*required):** [connection\*](#list_interconnect-resource-connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeConnectionProposal](https://docs.aws.amazon.com/interconnect/latest/api/API_DescribeConnectionProposal.html)  **
  - **Description:** Grants permission to describe a connection proposal
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetConnection](https://docs.aws.amazon.com/interconnect/latest/api/API_GetConnection.html)  **
  - **Description:** Grants permission to describe a connection
  - **Resource types (\*required):** [connection\*](#list_interconnect-resource-connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEnvironment](https://docs.aws.amazon.com/interconnect/latest/api/API_GetEnvironment.html)  **
  - **Description:** Grants permission to describe an environment
  - **Resource types (\*required):** [environment\*](#list_interconnect-resource-environment)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListAttachPoints](https://docs.aws.amazon.com/interconnect/latest/api/API_ListAttachPoints.html)  **
  - **Description:** Grants permission to list available attach points
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListConnections](https://docs.aws.amazon.com/interconnect/latest/api/API_ListConnections.html)  **
  - **Description:** Grants permission to list connections
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEnvironments](https://docs.aws.amazon.com/interconnect/latest/api/API_ListEnvironments.html)  **
  - **Description:** Grants permission to list available environments
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/interconnect/latest/api/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags on a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/interconnect/latest/api/API_TagResource.html)  **
  - **Description:** Grants permission to apply tags to a resource
  - **Resource types (\*required):** [connection\*](#list_interconnect-resource-connection)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_interconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interconnect-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/interconnect/latest/api/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a resource
  - **Resource types (\*required):** [connection\*](#list_interconnect-resource-connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interconnect-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateConnection](https://docs.aws.amazon.com/interconnect/latest/api/API_UpdateConnection.html)  **
  - **Description:** Grants permission to update an existing connection
  - **Resource types (\*required):** [connection\*](#list_interconnect-resource-connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Interconnect
<a name="list_interconnect-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [connection](https://docs.aws.amazon.com/interconnect/latest/api/Connection.html)  | arn:${Partition}:interconnect:${Region}:${Account}:connection/${Id} | [aws:ResourceTag/${TagKey}](#list_interconnect-aws_ResourceTag___TagKey_) | 
|  [environment](https://docs.aws.amazon.com/interconnect/latest/api/Environment.html)  | arn:${Partition}:interconnect:${Region}:${Account}:environment/${Id} |   | 

## Condition keys for AWS Interconnect
<a name="list_interconnect-policy-keys"></a>

AWS Interconnect defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag key and value pair that is allowed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by a tag key and value pair of a resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by a list of tag keys that are allowed in the request | ArrayOfString | 