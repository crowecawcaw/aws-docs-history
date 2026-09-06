

# Actions, resources, and condition keys for Amazon CodeGuru Security
<a name="list_codeguru-security"></a>

Amazon CodeGuru Security (service prefix: `codeguru-security`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/codeguru/latest/security-ug/what-is-codeguru-security.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/codeguru/latest/security-api/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/codeguru/latest/security-ug/permissions-reference.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/codeguru-security/codeguru-security.json) for this service.

**Topics**
+ [API operations defined by Amazon CodeGuru Security](#list_codeguru-security-operations)
+ [Actions defined by Amazon CodeGuru Security](#list_codeguru-security-actions-as-permissions)
+ [Permission-only actions for Amazon CodeGuru Security](#list_codeguru-security-permission-only-actions)
+ [Resource types defined by Amazon CodeGuru Security](#list_codeguru-security-resources-for-iam-policies)
+ [Condition keys for Amazon CodeGuru Security](#list_codeguru-security-policy-keys)

## API operations defined by Amazon CodeGuru Security
<a name="list_codeguru-security-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_codeguru-security-actions-as-permissions).




- **   BatchGetFindings  **
  - **IAM action:**  [codeguru-security:BatchGetFindings](#list_codeguru-security-action-BatchGetFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CreateScan  **
  - **IAM action:**  [codeguru-security:CreateScan](#list_codeguru-security-action-CreateScan)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codeguru-security:TagResource](#list_codeguru-security-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateUploadUrl  **
  - **IAM action:**  [codeguru-security:CreateUploadUrl](#list_codeguru-security-action-CreateUploadUrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAccountConfiguration  **
  - **IAM action:**  [codeguru-security:GetAccountConfiguration](#list_codeguru-security-action-GetAccountConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFindings  **
  - **IAM action:**  [codeguru-security:GetFindings](#list_codeguru-security-action-GetFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetMetricsSummary  **
  - **IAM action:**  [codeguru-security:GetMetricsSummary](#list_codeguru-security-action-GetMetricsSummary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetScan  **
  - **IAM action:**  [codeguru-security:GetScan](#list_codeguru-security-action-GetScan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListFindingsMetrics  **
  - **IAM action:**  [codeguru-security:ListFindingsMetrics](#list_codeguru-security-action-ListFindingsMetrics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListScans  **
  - **IAM action:**  [codeguru-security:ListScans](#list_codeguru-security-action-ListScans) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [codeguru-security:ListTagsForResource](#list_codeguru-security-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [codeguru-security:TagResource](#list_codeguru-security-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [codeguru-security:UntagResource](#list_codeguru-security-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAccountConfiguration  **
  - **IAM action:**  [codeguru-security:UpdateAccountConfiguration](#list_codeguru-security-action-UpdateAccountConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon CodeGuru Security
<a name="list_codeguru-security-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchGetFindings](https://docs.aws.amazon.com/codeguru/latest/security-api/API_BatchGetFindings.html)  **
  - **Description:** Grants permission to batch retrieve specific findings generated by CodeGuru Security
  - **Resource types (\*required):** [ScanName\*](#list_codeguru-security-resource-ScanName)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguru-security-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [CreateScan](https://docs.aws.amazon.com/codeguru/latest/security-api/API_CreateScan.html)  **
  - **Description:** Grants permission to create a CodeGuru Security scan
  - **Resource types (\*required):** [ScanName\*](#list_codeguru-security-resource-ScanName)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codeguru-security-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codeguru-security-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codeguru-security-aws_TagKeys)
  - **Access level:** Write

- **   [CreateUploadUrl](https://docs.aws.amazon.com/codeguru/latest/security-api/API_CreateUploadUrl.html)  **
  - **Description:** Grants permission to generate a presigned url for uploading code archives
  - **Resource types (\*required):** [ScanName\*](#list_codeguru-security-resource-ScanName)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguru-security-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAccountConfiguration](https://docs.aws.amazon.com/codeguru/latest/security-api/API_GetAccountConfiguration.html)  **
  - **Description:** Grants permission to retrieve the account level configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetFindings](https://docs.aws.amazon.com/codeguru/latest/security-api/API_GetFindings.html)  **
  - **Description:** Grants permission to retrieve findings for a scan generated by CodeGuru Security
  - **Resource types (\*required):** [ScanName\*](#list_codeguru-security-resource-ScanName)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguru-security-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetMetricsSummary](https://docs.aws.amazon.com/codeguru/latest/security-api/API_GetMetricsSummary.html)  **
  - **Description:** Grants permission to retrieve AWS accout level metrics summary generated by CodeGuru Security
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetScan](https://docs.aws.amazon.com/codeguru/latest/security-api/API_GetScan.html)  **
  - **Description:** Grants permission to retrieve CodeGuru Security scan metadata
  - **Resource types (\*required):** [ScanName\*](#list_codeguru-security-resource-ScanName)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguru-security-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListFindingsMetrics](https://docs.aws.amazon.com/codeguru/latest/security-api/API_ListFindingsMetrics.html)  **
  - **Description:** Grants permission to retrieve a list of account level findings metrics within a date range
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListScans](https://docs.aws.amazon.com/codeguru/latest/security-api/API_ListScans.html)  **
  - **Description:** Grants permission to retrieve list of CodeGuru Security scan metadata
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/codeguru/latest/security-api/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to retrieve a list of tags for a scan name ARN
  - **Resource types (\*required):** [ScanName\*](#list_codeguru-security-resource-ScanName)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguru-security-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/codeguru/latest/security-api/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a scan name ARN
  - **Resource types (\*required):** [ScanName\*](#list_codeguru-security-resource-ScanName)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codeguru-security-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codeguru-security-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codeguru-security-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/codeguru/latest/security-api/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a scan name ARN
  - **Resource types (\*required):** [ScanName\*](#list_codeguru-security-resource-ScanName)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguru-security-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codeguru-security-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAccountConfiguration](https://docs.aws.amazon.com/codeguru/latest/security-api/API_UpdateAccountConfiguration.html)  **
  - **Description:** Grants permission to update the account level configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Permission-only actions for Amazon CodeGuru Security
<a name="list_codeguru-security-permission-only-actions"></a>

The following actions are defined by Amazon CodeGuru Security but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [DeleteScansByCategory](${AuthZDocPage})  | Grants permission to delete all the scans and related findings from CodeGuru Security by given category |  |   | Write | 
|   [ListFindings](${AuthZDocPage})  | Grants permission to retrieve findings generated by CodeGuru Security |  |   | List | 

## Resource types defined by Amazon CodeGuru Security
<a name="list_codeguru-security-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [ScanName](https://docs.aws.amazon.com/codeguru/latest/security-ug/working-with-code-scans.html)  | arn:${Partition}:codeguru-security:${Region}:${Account}:scans/${ScanName} | [aws:ResourceTag/${TagKey}](#list_codeguru-security-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon CodeGuru Security
<a name="list_codeguru-security-policy-keys"></a>

Amazon CodeGuru Security defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 