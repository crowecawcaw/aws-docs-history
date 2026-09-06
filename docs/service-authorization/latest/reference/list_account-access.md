

# Actions, resources, and condition keys for Account access manager
<a name="list_account-access"></a>

Account access manager (service prefix: `account-access`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/IAM/latest/UserGuide/account-access-manager.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/account-access/latest/APIReference/API_Operations.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/aam-security.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/account-access/account-access.json) for this service.

**Topics**
+ [API operations defined by Account access manager](#list_account-access-operations)
+ [Actions defined by Account access manager](#list_account-access-actions-as-permissions)
+ [Resource types defined by Account access manager](#list_account-access-resources-for-iam-policies)
+ [Condition keys for Account access manager](#list_account-access-policy-keys)

## API operations defined by Account access manager
<a name="list_account-access-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_account-access-actions-as-permissions).




- **   CreateApplication  **
  - **IAM action:**  [account-access:CreateApplication](#list_account-access-action-CreateApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [account-access:TagResource](#list_account-access-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateEntitlement  **
  - **IAM action:**  [account-access:CreateEntitlement](#list_account-access-action-CreateEntitlement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApplication  **
  - **IAM action:**  [account-access:DeleteApplication](#list_account-access-action-DeleteApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEntitlement  **
  - **IAM action:**  [account-access:DeleteEntitlement](#list_account-access-action-DeleteEntitlement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetApplication  **
  - **IAM action:**  [account-access:GetApplication](#list_account-access-action-GetApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEntitlement  **
  - **IAM action:**  [account-access:GetEntitlement](#list_account-access-action-GetEntitlement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListApplications  **
  - **IAM action:**  [account-access:ListApplications](#list_account-access-action-ListApplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEntitlements  **
  - **IAM action:**  [account-access:ListEntitlements](#list_account-access-action-ListEntitlements) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [account-access:ListTagsForResource](#list_account-access-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [account-access:TagResource](#list_account-access-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [account-access:UntagResource](#list_account-access-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write



## Actions defined by Account access manager
<a name="list_account-access-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateApplication](https://docs.aws.amazon.com/service-authorization/latest/reference/list_account-access.html)  **
  - **Description:** Grants permission to enable an account access manager instance and create an AWS account access application in the associated IAM Identity Center instance
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_account-access-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_account-access-aws_TagKeys)
  - **Access level:** Write

- **   [CreateEntitlement](https://docs.aws.amazon.com/service-authorization/latest/reference/list_account-access.html)  **
  - **Description:** Grants permission to create an entitlement in an account access manager instance
  - **Resource types (\*required):** [application\*](#list_account-access-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_account-access-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteApplication](https://docs.aws.amazon.com/service-authorization/latest/reference/list_account-access.html)  **
  - **Description:** Grants permission to delete an account access manager instance and its AWS account access application in the associated IAM Identity Center instance
  - **Resource types (\*required):** [application\*](#list_account-access-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_account-access-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEntitlement](https://docs.aws.amazon.com/service-authorization/latest/reference/list_account-access.html)  **
  - **Description:** Grants permission to delete an entitlement in an account access manager instance
  - **Resource types (\*required):** [application\*](#list_account-access-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_account-access-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetApplication](https://docs.aws.amazon.com/service-authorization/latest/reference/list_account-access.html)  **
  - **Description:** Grants permission to describe an account access manager instance
  - **Resource types (\*required):** [application\*](#list_account-access-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_account-access-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEntitlement](https://docs.aws.amazon.com/service-authorization/latest/reference/list_account-access.html)  **
  - **Description:** Grants permission to get entitlement details for an account access manager instance
  - **Resource types (\*required):** [application\*](#list_account-access-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_account-access-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListApplications](https://docs.aws.amazon.com/service-authorization/latest/reference/list_account-access.html)  **
  - **Description:** Grants permission to list account access manager instances
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEntitlements](https://docs.aws.amazon.com/service-authorization/latest/reference/list_account-access.html)  **
  - **Description:** Grants permission to list entitlements for an account access manager instance
  - **Resource types (\*required):** [application\*](#list_account-access-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_account-access-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/service-authorization/latest/reference/list_account-access.html)  **
  - **Description:** Grants permission to list tags for an account access manager resource
  - **Resource types (\*required):** [application\*](#list_account-access-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_account-access-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/service-authorization/latest/reference/list_account-access.html)  **
  - **Description:** Grants permission to tag an account access manager resource
  - **Resource types (\*required):** [application](#list_account-access-resource-application)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_account-access-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_account-access-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_account-access-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/service-authorization/latest/reference/list_account-access.html)  **
  - **Description:** Grants permission to remove tags from an account access manager resource
  - **Resource types (\*required):** [application](#list_account-access-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_account-access-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_account-access-aws_TagKeys)
  - **Access level:** Tagging, Write



## Resource types defined by Account access manager
<a name="list_account-access-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [application](https://docs.aws.amazon.com/service-authorization/latest/reference/list_account-access.html)  | arn:${Partition}:account-access:${Region}:${Account}:application/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_account-access-aws_ResourceTag___TagKey_) | 

## Condition keys for Account access manager
<a name="list_account-access-policy-keys"></a>

Account access manager defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by tag keys | ArrayOfString | 