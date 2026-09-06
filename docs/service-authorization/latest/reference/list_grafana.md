

# Actions, resources, and condition keys for Amazon Managed Grafana
<a name="list_grafana"></a>

Amazon Managed Grafana (service prefix: `grafana`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/grafana/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/grafana/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/grafana/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/grafana/grafana.json) for this service.

**Topics**
+ [API operations defined by Amazon Managed Grafana](#list_grafana-operations)
+ [Actions defined by Amazon Managed Grafana](#list_grafana-actions-as-permissions)
+ [Resource types defined by Amazon Managed Grafana](#list_grafana-resources-for-iam-policies)
+ [Condition keys for Amazon Managed Grafana](#list_grafana-policy-keys)

## API operations defined by Amazon Managed Grafana
<a name="list_grafana-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_grafana-actions-as-permissions).




- **   AssociateLicense  **
  - **IAM action:**  [grafana:AssociateLicense](#list_grafana-action-AssociateLicense) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateWorkspace  **
  - **IAM action:**  [grafana:CreateWorkspace](#list_grafana-action-CreateWorkspace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [grafana:TagResource](#list_grafana-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** grafana.amazonaws.com / **Access level:** Write

- **   CreateWorkspaceApiKey  **
  - **IAM action:**  [grafana:CreateWorkspaceApiKey](#list_grafana-action-CreateWorkspaceApiKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateWorkspaceServiceAccount  **
  - **IAM action:**  [grafana:CreateWorkspaceServiceAccount](#list_grafana-action-CreateWorkspaceServiceAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateWorkspaceServiceAccountToken  **
  - **IAM action:**  [grafana:CreateWorkspaceServiceAccountToken](#list_grafana-action-CreateWorkspaceServiceAccountToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWorkspace  **
  - **IAM action:**  [grafana:DeleteWorkspace](#list_grafana-action-DeleteWorkspace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWorkspaceApiKey  **
  - **IAM action:**  [grafana:DeleteWorkspaceApiKey](#list_grafana-action-DeleteWorkspaceApiKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWorkspaceServiceAccount  **
  - **IAM action:**  [grafana:DeleteWorkspaceServiceAccount](#list_grafana-action-DeleteWorkspaceServiceAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWorkspaceServiceAccountToken  **
  - **IAM action:**  [grafana:DeleteWorkspaceServiceAccountToken](#list_grafana-action-DeleteWorkspaceServiceAccountToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeWorkspace  **
  - **IAM action:**  [grafana:DescribeWorkspace](#list_grafana-action-DescribeWorkspace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeWorkspaceAuthentication  **
  - **IAM action:**  [grafana:DescribeWorkspaceAuthentication](#list_grafana-action-DescribeWorkspaceAuthentication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeWorkspaceConfiguration  **
  - **IAM action:**  [grafana:DescribeWorkspaceConfiguration](#list_grafana-action-DescribeWorkspaceConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisassociateLicense  **
  - **IAM action:**  [grafana:DisassociateLicense](#list_grafana-action-DisassociateLicense) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListPermissions  **
  - **IAM action:**  [grafana:ListPermissions](#list_grafana-action-ListPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [grafana:ListTagsForResource](#list_grafana-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListVersions  **
  - **IAM action:**  [grafana:DescribeWorkspace](#list_grafana-action-DescribeWorkspace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [grafana:ListVersions](#list_grafana-action-ListVersions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListWorkspaceServiceAccountTokens  **
  - **IAM action:**  [grafana:ListWorkspaceServiceAccountTokens](#list_grafana-action-ListWorkspaceServiceAccountTokens) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListWorkspaceServiceAccounts  **
  - **IAM action:**  [grafana:ListWorkspaceServiceAccounts](#list_grafana-action-ListWorkspaceServiceAccounts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListWorkspaces  **
  - **IAM action:**  [grafana:ListWorkspaces](#list_grafana-action-ListWorkspaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [grafana:TagResource](#list_grafana-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [grafana:UntagResource](#list_grafana-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdatePermissions  **
  - **IAM action:**  [grafana:UpdatePermissions](#list_grafana-action-UpdatePermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   UpdateWorkspace  **
  - **IAM action:**  [grafana:UpdateWorkspace](#list_grafana-action-UpdateWorkspace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** grafana.amazonaws.com / **Access level:** Write

- **   UpdateWorkspaceAuthentication  **
  - **IAM action:**  [grafana:UpdateWorkspaceAuthentication](#list_grafana-action-UpdateWorkspaceAuthentication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateWorkspaceConfiguration  **
  - **IAM action:**  [grafana:UpdateWorkspaceConfiguration](#list_grafana-action-UpdateWorkspaceConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Managed Grafana
<a name="list_grafana-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateLicense](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-and-IAM.html)  **
  - **Description:** Grants permission to upgrade a workspace with a license
  - **Resource types (\*required):** [workspace\*](#list_grafana-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_grafana-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateWorkspace](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-and-IAM.html)  **
  - **Description:** Grants permission to create a workspace
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_grafana-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_grafana-aws_TagKeys)
  - **Access level:** Write

- **   [CreateWorkspaceApiKey](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-and-IAM.html)  **
  - **Description:** Grants permission to create API keys for a workspace
  - **Resource types (\*required):** [workspace\*](#list_grafana-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_grafana-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateWorkspaceServiceAccount](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-and-IAM.html)  **
  - **Description:** Grants permission to create service accounts for a workspace
  - **Resource types (\*required):** [workspace\*](#list_grafana-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_grafana-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateWorkspaceServiceAccountToken](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-and-IAM.html)  **
  - **Description:** Grants permission to create service account tokens for a workspace
  - **Resource types (\*required):** [workspace\*](#list_grafana-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_grafana-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWorkspace](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-and-IAM.html)  **
  - **Description:** Grants permission to delete a workspace
  - **Resource types (\*required):** [workspace\*](#list_grafana-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_grafana-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWorkspaceApiKey](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-and-IAM.html)  **
  - **Description:** Grants permission to delete API keys from a workspace
  - **Resource types (\*required):** [workspace\*](#list_grafana-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_grafana-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWorkspaceServiceAccount](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-and-IAM.html)  **
  - **Description:** Grants permission to delete service accounts for a workspace
  - **Resource types (\*required):** [workspace\*](#list_grafana-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_grafana-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWorkspaceServiceAccountToken](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-and-IAM.html)  **
  - **Description:** Grants permission to delete service account tokens for a workspace
  - **Resource types (\*required):** [workspace\*](#list_grafana-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_grafana-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeWorkspace](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-and-IAM.html)  **
  - **Description:** Grants permission to describe a workspace
  - **Resource types (\*required):** [workspace\*](#list_grafana-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_grafana-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeWorkspaceAuthentication](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-and-IAM.html)  **
  - **Description:** Grants permission to describe authentication providers on a workspace
  - **Resource types (\*required):** [workspace\*](#list_grafana-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_grafana-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeWorkspaceConfiguration](https://docs.aws.amazon.com/grafana/latest/APIReference/API_DescribeWorkspaceConfiguration.html)  **
  - **Description:** Grants permission to describe the current configuration string for the given workspace
  - **Resource types (\*required):** [workspace\*](#list_grafana-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_grafana-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DisassociateLicense](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-and-IAM.html)  **
  - **Description:** Grants permission to remove a license from a workspace
  - **Resource types (\*required):** [workspace\*](#list_grafana-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_grafana-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListPermissions](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-and-IAM.html)  **
  - **Description:** Grants permission to list the permissions on a wokspace
  - **Resource types (\*required):** [workspace\*](#list_grafana-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_grafana-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/grafana/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags associated with a workspace
  - **Resource types (\*required):** [workspace](#list_grafana-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_grafana-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListVersions](https://docs.aws.amazon.com/grafana/latest/APIReference/API_ListVersions.html)  **
  - **Description:** Grants permission to list all available supported Grafana versions. Optionally, include a workspace to list the versions to which it can be upgraded
  - **Resource types (\*required):** [workspace](#list_grafana-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_grafana-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListWorkspaceServiceAccountTokens](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-and-IAM.html)  **
  - **Description:** Grants permission to list service account tokens for a workspace
  - **Resource types (\*required):** [workspace\*](#list_grafana-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_grafana-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListWorkspaceServiceAccounts](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-and-IAM.html)  **
  - **Description:** Grants permission to list service accounts for a workspace
  - **Resource types (\*required):** [workspace\*](#list_grafana-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_grafana-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListWorkspaces](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-and-IAM.html)  **
  - **Description:** Grants permission to list workspaces
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/grafana/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to, or update tag values of, a workspace
  - **Resource types (\*required):** [workspace\*](#list_grafana-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_grafana-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_grafana-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_grafana-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/grafana/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a workspace
  - **Resource types (\*required):** [workspace\*](#list_grafana-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_grafana-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_grafana-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdatePermissions](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-and-IAM.html)  **
  - **Description:** Grants permission to modify the permissions on a workspace
  - **Resource types (\*required):** [workspace\*](#list_grafana-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_grafana-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [UpdateWorkspace](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-and-IAM.html)  **
  - **Description:** Grants permission to modify a workspace
  - **Resource types (\*required):** [workspace\*](#list_grafana-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_grafana-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateWorkspaceAuthentication](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-and-IAM.html)  **
  - **Description:** Grants permission to modify authentication providers on a workspace
  - **Resource types (\*required):** [workspace\*](#list_grafana-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_grafana-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateWorkspaceConfiguration](https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdateWorkspaceConfiguration.html)  **
  - **Description:** Grants permission to update the configuration string for the given workspace
  - **Resource types (\*required):** [workspace\*](#list_grafana-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_grafana-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Managed Grafana
<a name="list_grafana-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [workspace](https://docs.aws.amazon.com/grafana/latest/userguide/security-iam.html)  | arn:${Partition}:grafana:${Region}:${Account}:/workspaces/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_grafana-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Managed Grafana
<a name="list_grafana-policy-keys"></a>

Amazon Managed Grafana defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/grafana/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-tags)  | Filters access by actions based on the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/grafana/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-tags)  | Filters access by actions based on tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/grafana/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-tags)  | Filters access by actions based on the presence of tag keys in the request | ArrayOfString | 