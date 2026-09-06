

# Actions, resources, and condition keys for AWS Billing And Cost Management Data Exports
<a name="list_bcm-data-exports"></a>

AWS Billing And Cost Management Data Exports (service prefix: `bcm-data-exports`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Operations_AWS_Billing_and_Cost_Management_Data_Exports.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/cur/latest/userguide/bcm-data-exports-access.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/bcm-data-exports/bcm-data-exports.json) for this service.

**Topics**
+ [API operations defined by AWS Billing And Cost Management Data Exports](#list_bcm-data-exports-operations)
+ [Actions defined by AWS Billing And Cost Management Data Exports](#list_bcm-data-exports-actions-as-permissions)
+ [Resource types defined by AWS Billing And Cost Management Data Exports](#list_bcm-data-exports-resources-for-iam-policies)
+ [Condition keys for AWS Billing And Cost Management Data Exports](#list_bcm-data-exports-policy-keys)

## API operations defined by AWS Billing And Cost Management Data Exports
<a name="list_bcm-data-exports-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_bcm-data-exports-actions-as-permissions).




- **   CreateExport  **
  - **IAM action:**  [bcm-data-exports:CreateExport](#list_bcm-data-exports-action-CreateExport)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bcm-data-exports:TagResource](#list_bcm-data-exports-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [cost-optimization-hub:GetRecommendation](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_GetRecommendation.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [cost-optimization-hub:ListRecommendations](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_ListRecommendations.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [cur:PutReportDefinition](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_cur_PutReportDefinition.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sustainability:GetCarbonFootprintSummary](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-create-standard.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DeleteExport  **
  - **IAM action:**  [bcm-data-exports:DeleteExport](#list_bcm-data-exports-action-DeleteExport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetExecution  **
  - **IAM action:**  [bcm-data-exports:GetExecution](#list_bcm-data-exports-action-GetExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetExport  **
  - **IAM action:**  [bcm-data-exports:GetExport](#list_bcm-data-exports-action-GetExport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTable  **
  - **IAM action:**  [bcm-data-exports:GetTable](#list_bcm-data-exports-action-GetTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListExecutions  **
  - **IAM action:**  [bcm-data-exports:ListExecutions](#list_bcm-data-exports-action-ListExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListExports  **
  - **IAM action:**  [bcm-data-exports:ListExports](#list_bcm-data-exports-action-ListExports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTables  **
  - **IAM action:**  [bcm-data-exports:ListTables](#list_bcm-data-exports-action-ListTables) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [bcm-data-exports:ListTagsForResource](#list_bcm-data-exports-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [bcm-data-exports:TagResource](#list_bcm-data-exports-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [bcm-data-exports:UntagResource](#list_bcm-data-exports-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateExport  **
  - **IAM action:**  [bcm-data-exports:UpdateExport](#list_bcm-data-exports-action-UpdateExport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Billing And Cost Management Data Exports
<a name="list_bcm-data-exports-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateExport](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_CreateExport.html)  **
  - **Description:** Grants permission to create an export
  - **Resource types (\*required):** [billingview](#list_bcm-data-exports-resource-billingview) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bcm-data-exports-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bcm-data-exports-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bcm-data-exports-aws_TagKeys)
  - **Resource types (\*required):** [table\*](#list_bcm-data-exports-resource-table) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bcm-data-exports-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bcm-data-exports-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteExport](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_DeleteExport.html)  **
  - **Description:** Grants permission to delete an export
  - **Resource types (\*required):** [export\*](#list_bcm-data-exports-resource-export)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bcm-data-exports-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetExecution](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_GetExecution.html)  **
  - **Description:** Grants permission to get the execution of an export
  - **Resource types (\*required):** [export\*](#list_bcm-data-exports-resource-export)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bcm-data-exports-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetExport](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_GetExport.html)  **
  - **Description:** Grants permission to get an export
  - **Resource types (\*required):** [export\*](#list_bcm-data-exports-resource-export)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bcm-data-exports-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTable](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_GetTable.html)  **
  - **Description:** Grants permission to get the details of a table
  - **Resource types (\*required):** [table\*](#list_bcm-data-exports-resource-table)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListExecutions](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_ListExecutions.html)  **
  - **Description:** Grants permission to list all executions of an export
  - **Resource types (\*required):** [export\*](#list_bcm-data-exports-resource-export)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bcm-data-exports-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListExports](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_ListExports.html)  **
  - **Description:** Grants permission to list all exports
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTables](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_ListTables.html)  **
  - **Description:** Grants permission to list all available tables
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [export\*](#list_bcm-data-exports-resource-export)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bcm-data-exports-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [export\*](#list_bcm-data-exports-resource-export)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bcm-data-exports-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bcm-data-exports-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bcm-data-exports-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [export\*](#list_bcm-data-exports-resource-export)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bcm-data-exports-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bcm-data-exports-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateExport](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_UpdateExport.html)  **
  - **Description:** Grants permission to update an export
  - **Resource types (\*required):** [billingview](#list_bcm-data-exports-resource-billingview) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bcm-data-exports-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [export\*](#list_bcm-data-exports-resource-export) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bcm-data-exports-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [table\*](#list_bcm-data-exports-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bcm-data-exports-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Billing And Cost Management Data Exports
<a name="list_bcm-data-exports-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [billingview](https://docs.aws.amazon.com/cur/latest/userguide/)  | arn:${Partition}:billing::${Account}:billingview/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_bcm-data-exports-aws_ResourceTag___TagKey_) | 
|  [export](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_Export.html)  | arn:${Partition}:bcm-data-exports:${Region}:${Account}:export/${Identifier} | [aws:ResourceTag/${TagKey}](#list_bcm-data-exports-aws_ResourceTag___TagKey_) | 
|  [table](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_Table.html)  | arn:${Partition}:bcm-data-exports:${Region}:${Account}:table/${Identifier} |   | 

## Condition keys for AWS Billing And Cost Management Data Exports
<a name="list_bcm-data-exports-policy-keys"></a>

AWS Billing And Cost Management Data Exports defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 