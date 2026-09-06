

# Actions, resources, and condition keys for Amazon Resource Group Tagging API
<a name="list_resourcegroupstaggingapi"></a>

Amazon Resource Group Tagging API (service prefix: `tag`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/ARG/latest/userguide/tag-editor.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-prereqs.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/tag/tag.json) for this service.

**Topics**
+ [API operations defined by Amazon Resource Group Tagging API](#list_resourcegroupstaggingapi-operations)
+ [Actions defined by Amazon Resource Group Tagging API](#list_resourcegroupstaggingapi-actions-as-permissions)
+ [Resource types defined by Amazon Resource Group Tagging API](#list_resourcegroupstaggingapi-resources-for-iam-policies)
+ [Condition keys for Amazon Resource Group Tagging API](#list_resourcegroupstaggingapi-policy-keys)

## API operations defined by Amazon Resource Group Tagging API
<a name="list_resourcegroupstaggingapi-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_resourcegroupstaggingapi-actions-as-permissions).




- **   DescribeReportCreation  **
  - **IAM action:**  [tag:DescribeReportCreation](#list_resourcegroupstaggingapi-action-DescribeReportCreation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetComplianceSummary  **
  - **IAM action:**  [tag:GetComplianceSummary](#list_resourcegroupstaggingapi-action-GetComplianceSummary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResources  **
  - **IAM action:**  [tag:GetResources](#list_resourcegroupstaggingapi-action-GetResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTagKeys  **
  - **IAM action:**  [tag:GetTagKeys](#list_resourcegroupstaggingapi-action-GetTagKeys) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTagValues  **
  - **IAM action:**  [tag:GetTagValues](#list_resourcegroupstaggingapi-action-GetTagValues) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListRequiredTags  **
  - **IAM action:**  [tag:ListRequiredTags](#list_resourcegroupstaggingapi-action-ListRequiredTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   StartReportCreation  **
  - **IAM action:**  [tag:StartReportCreation](#list_resourcegroupstaggingapi-action-StartReportCreation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResources  **
  - **IAM action:**  [tag:TagResources](#list_resourcegroupstaggingapi-action-TagResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResources  **
  - **IAM action:**  [tag:UntagResources](#list_resourcegroupstaggingapi-action-UntagResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write



## Actions defined by Amazon Resource Group Tagging API
<a name="list_resourcegroupstaggingapi-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [DescribeReportCreation](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_DescribeReportCreation.html)  | Grants permission to describe the status of the StartReportCreation operation |  |   | Read | 
|   [GetComplianceSummary](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetComplianceSummary.html)  | Grants permission to retrieve a summary of how many resources are noncompliant with their effective tag policies |  |   | Read | 
|   [GetResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html)  | Grants permission to return tagged or previously tagged resources in the specified AWS Region for the calling account |  |   | Read | 
|   [GetTagKeys](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetTagKeys.html)  | Grants permission to returns tag keys currently in use in the specified AWS Region for the calling account |  |   | Read | 
|   [GetTagValues](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetTagValues.html)  | Grants permission to return tag values for the specified key that are used in the specified AWS Region for the calling account |  |   | Read | 
|   [ListRequiredTags](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_ListRequiredTags.html)  | Grants permission to list required tags for supported resource types in the calling account |  |   | List | 
|   [StartReportCreation](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_StartReportCreation.html)  | Grants permission to start generating a report listing all tagged resources in accounts across your organization, and whether each resource is compliant with the effective tag policy |  |   | Write | 
|   [TagResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_TagResources.html)  | Grants permission to apply one or more tags to the specified resources |  |   | Tagging, Write | 
|   [UntagResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_UntagResources.html)  | Grants permission to remove the specified tags from the specified resources |  |   | Tagging, Write | 

## Resource types defined by Amazon Resource Group Tagging API
<a name="list_resourcegroupstaggingapi-resources-for-iam-policies"></a>

Amazon Resource Group Tagging API does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for Amazon Resource Group Tagging API
<a name="list_resourcegroupstaggingapi-policy-keys"></a>

Amazon Resource Group Tagging API has no service-specific condition keys that can be used in the `Condition` element of policy statements.