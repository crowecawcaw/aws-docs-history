

# Actions, resources, and condition keys for AWS Elemental Support Cases
<a name="list_elemental-support-cases"></a>

AWS Elemental Support Cases (service prefix: `elemental-support-cases`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/elemental-appliances-software/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/elemental-appliances-software/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/elemental-appliances-software/) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/elemental-support-cases/elemental-support-cases.json) for this service.

**Topics**
+ [Actions defined by AWS Elemental Support Cases](#list_elemental-support-cases-actions-as-permissions)
+ [Permission-only actions for AWS Elemental Support Cases](#list_elemental-support-cases-permission-only-actions)
+ [Resource types defined by AWS Elemental Support Cases](#list_elemental-support-cases-resources-for-iam-policies)
+ [Condition keys for AWS Elemental Support Cases](#list_elemental-support-cases-policy-keys)

## Actions defined by AWS Elemental Support Cases
<a name="list_elemental-support-cases-actions-as-permissions"></a>

AWS Elemental Support Cases has no API operations that can be used in the `Actions` element of an IAM policy statement.

## Permission-only actions for AWS Elemental Support Cases
<a name="list_elemental-support-cases-permission-only-actions"></a>

The following actions are defined by AWS Elemental Support Cases but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AddCaseComment](https://docs.aws.amazon.com/elemental-appliances-software)  **
  - **Description:** Grants permission to add a comment to a support case
  - **Resource types (\*required):** [case\*](#list_elemental-support-cases-resource-case)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elemental-support-cases-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CheckCasePermission](https://docs.aws.amazon.com/elemental-appliances-software)  **
  - **Description:** Grants permission to verify whether the caller has the permissions to perform support case operations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CompleteMultipartUpload](https://docs.aws.amazon.com/elemental-appliances-software)  **
  - **Description:** Grants permission to complete a multipart file upload to a support case
  - **Resource types (\*required):** [case\*](#list_elemental-support-cases-resource-case)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elemental-support-cases-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateCase](https://docs.aws.amazon.com/elemental-appliances-software)  **
  - **Description:** Grants permission to create a support case
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elemental-support-cases-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_elemental-support-cases-aws_TagKeys)
  - **Access level:** Write

- **   [CreateS3CLIUploadCommand](https://docs.aws.amazon.com/elemental-appliances-software)  **
  - **Description:** Grants permission to create a cli command to allow a file upload to a support case
  - **Resource types (\*required):** [case\*](#list_elemental-support-cases-resource-case)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elemental-support-cases-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateS3DownloadUrl](https://docs.aws.amazon.com/elemental-appliances-software)  **
  - **Description:** Grants permission to download a file from a support case
  - **Resource types (\*required):** [case\*](#list_elemental-support-cases-resource-case)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elemental-support-cases-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetCase](https://docs.aws.amazon.com/elemental-appliances-software)  **
  - **Description:** Grants permission to describe a support case in your account
  - **Resource types (\*required):** [case\*](#list_elemental-support-cases-resource-case)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elemental-support-cases-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCasePermission](https://docs.aws.amazon.com/elemental-appliances-software)  **
  - **Description:** Grants permission to verify whether the caller has the permissions to perform support case operations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCases](https://docs.aws.amazon.com/elemental-appliances-software)  **
  - **Description:** Grants permission to list the support cases in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetUICache](https://docs.aws.amazon.com/elemental-appliances-software)  **
  - **Description:** Grants permission to retrieve cached case user data for use in the Console
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTagsForCase](https://docs.aws.amazon.com/elemental-appliances-software)  **
  - **Description:** Grants permission to list tags on a support case
  - **Resource types (\*required):** [case\*](#list_elemental-support-cases-resource-case)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elemental-support-cases-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [StartMultipartUpload](https://docs.aws.amazon.com/elemental-appliances-software)  **
  - **Description:** Grants permission to start a multipart file upload to a support case
  - **Resource types (\*required):** [case\*](#list_elemental-support-cases-resource-case)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elemental-support-cases-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagCase](https://docs.aws.amazon.com/elemental-appliances-software)  **
  - **Description:** Grants permission to add a tag on a support case
  - **Resource types (\*required):** [case\*](#list_elemental-support-cases-resource-case)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elemental-support-cases-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elemental-support-cases-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elemental-support-cases-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagCase](https://docs.aws.amazon.com/elemental-appliances-software)  **
  - **Description:** Grants permission to remove a tag on a support case
  - **Resource types (\*required):** [case\*](#list_elemental-support-cases-resource-case)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elemental-support-cases-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elemental-support-cases-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateCase](https://docs.aws.amazon.com/elemental-appliances-software)  **
  - **Description:** Grants permission to update a support case
  - **Resource types (\*required):** [case\*](#list_elemental-support-cases-resource-case)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elemental-support-cases-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCaseStatus](https://docs.aws.amazon.com/elemental-appliances-software)  **
  - **Description:** Grants permission to update a support case status
  - **Resource types (\*required):** [case\*](#list_elemental-support-cases-resource-case)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elemental-support-cases-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateMultipartUpload](https://docs.aws.amazon.com/elemental-appliances-software)  **
  - **Description:** Grants permission to update a multipart file upload to a support case
  - **Resource types (\*required):** [case\*](#list_elemental-support-cases-resource-case)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elemental-support-cases-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Elemental Support Cases
<a name="list_elemental-support-cases-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [case](https://docs.aws.amazon.com/elemental-appliances-software/)  | arn:${Partition}:elemental-support-cases::${Account}:case/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_elemental-support-cases-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Elemental Support Cases
<a name="list_elemental-support-cases-policy-keys"></a>

AWS Elemental Support Cases defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by tag keys that are passed in the request | ArrayOfString | 