

# Actions, resources, and condition keys for AWS Cost and Usage Report
<a name="list_cur"></a>

AWS Cost and Usage Report (service prefix: `cur`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/cur/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/cur/latest/userguide/security.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/cur/cur.json) for this service.

**Topics**
+ [API operations defined by AWS Cost and Usage Report](#list_cur-operations)
+ [Actions defined by AWS Cost and Usage Report](#list_cur-actions-as-permissions)
+ [Permission-only actions for AWS Cost and Usage Report](#list_cur-permission-only-actions)
+ [Resource types defined by AWS Cost and Usage Report](#list_cur-resources-for-iam-policies)
+ [Condition keys for AWS Cost and Usage Report](#list_cur-policy-keys)

## API operations defined by AWS Cost and Usage Report
<a name="list_cur-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_cur-actions-as-permissions).




- **   DeleteReportDefinition  **
  - **IAM action:**  [cur:DeleteReportDefinition](#list_cur-action-DeleteReportDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeReportDefinitions  **
  - **IAM action:**  [cur:DescribeReportDefinitions](#list_cur-action-DescribeReportDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [cur:ListTagsForResource](#list_cur-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ModifyReportDefinition  **
  - **IAM action:**  [cur:ModifyReportDefinition](#list_cur-action-ModifyReportDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutReportDefinition  **
  - **IAM action:**  [cur:PutReportDefinition](#list_cur-action-PutReportDefinition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cur:TagResource](#list_cur-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   TagResource  **
  - **IAM action:**  [cur:TagResource](#list_cur-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [cur:UntagResource](#list_cur-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write



## Actions defined by AWS Cost and Usage Report
<a name="list_cur-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [DeleteReportDefinition](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_cur_DeleteReportDefinition.html)  **
  - **Description:** Grants permission to delete Cost and Usage Report Definition
  - **Resource types (\*required):** [cur\*](#list_cur-resource-cur)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeReportDefinitions](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_cur_DescribeReportDefinitions.html)  **
  - **Description:** Grants permission to get Cost and Usage Report Definitions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_cur_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [cur\*](#list_cur-resource-cur)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cur-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ModifyReportDefinition](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_cur_ModifyReportDefinition.html)  **
  - **Description:** Grants permission to modify Cost and Usage Report Definition
  - **Resource types (\*required):** [cur\*](#list_cur-resource-cur)
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutReportDefinition](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_cur_PutReportDefinition.html)  **
  - **Description:** Grants permission to write Cost and Usage Report Definition
  - **Resource types (\*required):** [cur\*](#list_cur-resource-cur)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cur-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cur-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cur-aws_TagKeys)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_cur_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [cur\*](#list_cur-resource-cur)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cur-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cur-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cur-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_cur_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [cur\*](#list_cur-resource-cur)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cur-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cur-aws_TagKeys)
  - **Access level:** Tagging, Write



## Permission-only actions for AWS Cost and Usage Report
<a name="list_cur-permission-only-actions"></a>

The following actions are defined by AWS Cost and Usage Report but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [GetClassicReport](https://docs.aws.amazon.com/cur/latest/userguide/security.html#user-permissions)  | Grants permission to get Bills CSV report |  |   | Read | 
|   [GetClassicReportPreferences](https://docs.aws.amazon.com/cur/latest/userguide/security.html#user-permissions)  | Grants permission to get the classic report enablement status for Usage Reports |  |   | Read | 
|   [GetUsageReport](https://docs.aws.amazon.com/cur/latest/userguide/security.html#user-permissions)  | Grants permission to get list of AWS services, usage type and operation for the Usage Report workflow. Allows or denies download of usage reports too |  |   | Read | 
|   [PutClassicReportPreferences](https://docs.aws.amazon.com/cur/latest/userguide/security.html#user-permissions)  | Grants permission to enable classic reports |  |   | Write | 
|   [ValidateReportDestination](https://docs.aws.amazon.com/cur/latest/userguide/security.html#user-permissions)  | Grants permission to validates if the s3 bucket exists with appropriate permissions for CUR delivery |  |   | Read | 

## Resource types defined by AWS Cost and Usage Report
<a name="list_cur-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [cur](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html)  | arn:${Partition}:cur:${Region}:${Account}:definition/${ReportName} |   | 

## Condition keys for AWS Cost and Usage Report
<a name="list_cur-policy-keys"></a>

AWS Cost and Usage Report defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 