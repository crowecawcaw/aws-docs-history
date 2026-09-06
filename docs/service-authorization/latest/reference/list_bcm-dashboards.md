

# Actions, resources, and condition keys for AWS Billing and Cost Management Dashboards
<a name="list_bcm-dashboards"></a>

AWS Billing and Cost Management Dashboards (service prefix: `bcm-dashboards`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/cost-management/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/cost-management/latest/userguide/) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/bcm-dashboards/bcm-dashboards.json) for this service.

**Topics**
+ [API operations defined by AWS Billing and Cost Management Dashboards](#list_bcm-dashboards-operations)
+ [Actions defined by AWS Billing and Cost Management Dashboards](#list_bcm-dashboards-actions-as-permissions)
+ [Resource types defined by AWS Billing and Cost Management Dashboards](#list_bcm-dashboards-resources-for-iam-policies)
+ [Condition keys for AWS Billing and Cost Management Dashboards](#list_bcm-dashboards-policy-keys)

## API operations defined by AWS Billing and Cost Management Dashboards
<a name="list_bcm-dashboards-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_bcm-dashboards-actions-as-permissions).




- **   CreateDashboard  **
  - **IAM action:**  [bcm-dashboards:CreateDashboard](#list_bcm-dashboards-action-CreateDashboard)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bcm-dashboards:TagResource](#list_bcm-dashboards-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateScheduledReport  **
  - **IAM action:**  [bcm-dashboards:CreateScheduledReport](#list_bcm-dashboards-action-CreateScheduledReport)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bcm-dashboards:TagResource](#list_bcm-dashboards-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bcm-dashboards.amazonaws.com / **Access level:** Write

- **   DeleteDashboard  **
  - **IAM action:**  [bcm-dashboards:DeleteDashboard](#list_bcm-dashboards-action-DeleteDashboard) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteScheduledReport  **
  - **IAM action:**  [bcm-dashboards:DeleteScheduledReport](#list_bcm-dashboards-action-DeleteScheduledReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ExecuteScheduledReport  **
  - **IAM action:**  [bcm-dashboards:ExecuteScheduledReport](#list_bcm-dashboards-action-ExecuteScheduledReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetDashboard  **
  - **IAM action:**  [bcm-dashboards:GetDashboard](#list_bcm-dashboards-action-GetDashboard) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePolicy  **
  - **IAM action:**  [bcm-dashboards:GetResourcePolicy](#list_bcm-dashboards-action-GetResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetScheduledReport  **
  - **IAM action:**  [bcm-dashboards:GetScheduledReport](#list_bcm-dashboards-action-GetScheduledReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDashboards  **
  - **IAM action:**  [bcm-dashboards:ListDashboards](#list_bcm-dashboards-action-ListDashboards) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListScheduledReports  **
  - **IAM action:**  [bcm-dashboards:ListScheduledReports](#list_bcm-dashboards-action-ListScheduledReports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [bcm-dashboards:ListTagsForResource](#list_bcm-dashboards-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [bcm-dashboards:TagResource](#list_bcm-dashboards-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [bcm-dashboards:UntagResource](#list_bcm-dashboards-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateDashboard  **
  - **IAM action:**  [bcm-dashboards:UpdateDashboard](#list_bcm-dashboards-action-UpdateDashboard) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateScheduledReport  **
  - **IAM action:**  [bcm-dashboards:UpdateScheduledReport](#list_bcm-dashboards-action-UpdateScheduledReport)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bcm-dashboards.amazonaws.com / **Access level:** Write



## Actions defined by AWS Billing and Cost Management Dashboards
<a name="list_bcm-dashboards-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [CreateDashboard](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_CreateDashboard.html)  | Grants permission to create a dashboard |  |   | Write | 
|   [CreateScheduledReport](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_CreateScheduledReport.html)  | Grants permission to create a scheduled report |  | [aws:ResourceTag/${TagKey}](#list_bcm-dashboards-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bcm-dashboards-aws_TagKeys) | Write | 
|   [DeleteDashboard](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_DeleteDashboard.html)  | Grants permission to delete a dashboard |  |   | Write | 
|   [DeleteScheduledReport](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_DeleteScheduledReport.html)  | Grants permission to delete a scheduled report |  |   | Write | 
|   [ExecuteScheduledReport](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_ExecuteScheduledReport.html)  | Grants permission to execute a scheduled report |  |   | Write | 
|   [GetDashboard](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_GetDashboard.html)  | Grants permission to get dashboard information |  |   | Read | 
|   [GetResourcePolicy](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_GetResourcePolicy.html)  | Grants permission to get the resource policy for a dashboard |  |   | Read | 
|   [GetScheduledReport](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_GetScheduledReport.html)  | Grants permission to get scheduled report information |  |   | Read | 
|   [ListDashboards](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_ListDashboards.html)  | Grants permission to list information about all of the dashboards for a user |  |   | Read | 
|   [ListScheduledReports](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_ListScheduledReports.html)  | Grants permission to list information about all of the scheduled reports for a user |  |   | List | 
|   [ListTagsForResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_ListTagsForResource.html)  | Grants permission to list all of the tags for a resource |  |   | Read | 
|   [TagResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_TagResource.html)  | Grants permission to create a tag for a resource |  | [aws:RequestTag/${TagKey}](#list_bcm-dashboards-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bcm-dashboards-aws_TagKeys) | Tagging, Write | 
|   [UntagResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_UntagResource.html)  | Grants permission to remove a tag for a resource |  | [aws:TagKeys](#list_bcm-dashboards-aws_TagKeys) | Tagging, Write | 
|   [UpdateDashboard](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_UpdateDashboard.html)  | Grants permission to update an existing dashboard |  |   | Write | 
|   [UpdateScheduledReport](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_UpdateScheduledReport.html)  | Grants permission to update an existing scheduled report |  |   | Write | 

## Resource types defined by AWS Billing and Cost Management Dashboards
<a name="list_bcm-dashboards-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [dashboard](https://docs.aws.amazon.com/cost-management/latest/userguide/)  | arn:${Partition}:bcm-dashboards::${Account}:dashboard/${DashboardName} | [aws:ResourceTag/${TagKey}](#list_bcm-dashboards-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bcm-dashboards-aws_TagKeys) | 
|  [scheduled-report](https://docs.aws.amazon.com/cost-management/latest/userguide/)  | arn:${Partition}:bcm-dashboards::${Account}:scheduled-report/${ScheduledReportName} | [aws:ResourceTag/${TagKey}](#list_bcm-dashboards-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bcm-dashboards-aws_TagKeys) | 

## Condition keys for AWS Billing and Cost Management Dashboards
<a name="list_bcm-dashboards-policy-keys"></a>

AWS Billing and Cost Management Dashboards defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/cost-management/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-tags)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 