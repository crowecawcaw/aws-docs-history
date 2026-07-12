# Actions, resources, and condition keys for AWS Cost Optimization Hub

AWS Cost Optimization Hub (service prefix: `cost-optimization-hub`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../cost-management/latest/userguide/cost-optimization-hub.md "../../../cost-management/latest/userguide/cost-optimization-hub.md").
- View a list of the [API operations available for
  this service](../../../aws-cost-management/latest/APIReference.md "../../../aws-cost-management/latest/APIReference.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../cost-management/latest/userguide/security-iam.md "../../../cost-management/latest/userguide/security-iam.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/cost-optimization-hub/cost-optimization-hub.json "https://servicereference.us-east-1.amazonaws.com/v1/cost-optimization-hub/cost-optimization-hub.json") for this service.

###### Topics

- [API operations defined by AWS Cost Optimization Hub](#list_cost-optimization-hub-operations "#list_cost-optimization-hub-operations")
- [Actions defined by AWS Cost Optimization Hub](#list_cost-optimization-hub-actions-as-permissions "#list_cost-optimization-hub-actions-as-permissions")
- [Resource types defined by AWS Cost Optimization Hub](#list_cost-optimization-hub-resources-for-iam-policies "#list_cost-optimization-hub-resources-for-iam-policies")
- [Condition keys for AWS Cost Optimization Hub](#list_cost-optimization-hub-policy-keys "#list_cost-optimization-hub-policy-keys")

## API operations defined by AWS Cost Optimization Hub

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_cost-optimization-hub-actions-as-permissions "#list_cost-optimization-hub-actions-as-permissions").

| Operation                   | IAM action                                                                                                                                                                           | Condition key | Possible value(s) | Access level |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- | ----------------- | ------------ |
| GetPreferences              | [cost-optimization-hub:GetPreferences](#list_cost-optimization-hub-action-GetPreferences "#list_cost-optimization-hub-action-GetPreferences")                                        |               |                   | Read         |
| GetRecommendation           | [cost-optimization-hub:GetRecommendation](#list_cost-optimization-hub-action-GetRecommendation "#list_cost-optimization-hub-action-GetRecommendation")                               |               |                   | Read         |
| ListEfficiencyMetrics       | [cost-optimization-hub:ListEfficiencyMetrics](#list_cost-optimization-hub-action-ListEfficiencyMetrics "#list_cost-optimization-hub-action-ListEfficiencyMetrics")                   |               |                   | List         |
| ListEnrollmentStatuses      | [cost-optimization-hub:ListEnrollmentStatuses](#list_cost-optimization-hub-action-ListEnrollmentStatuses "#list_cost-optimization-hub-action-ListEnrollmentStatuses")                |               |                   | List         |
| ListRecommendationSummaries | [cost-optimization-hub:ListRecommendationSummaries](#list_cost-optimization-hub-action-ListRecommendationSummaries "#list_cost-optimization-hub-action-ListRecommendationSummaries") |               |                   | List         |
| ListRecommendations         | [cost-optimization-hub:ListRecommendations](#list_cost-optimization-hub-action-ListRecommendations "#list_cost-optimization-hub-action-ListRecommendations")                         |               |                   | List         |
| UpdateEnrollmentStatus      | [cost-optimization-hub:UpdateEnrollmentStatus](#list_cost-optimization-hub-action-UpdateEnrollmentStatus "#list_cost-optimization-hub-action-UpdateEnrollmentStatus")                |               |                   | Write        |
| UpdatePreferences           | [cost-optimization-hub:UpdatePreferences](#list_cost-optimization-hub-action-UpdatePreferences "#list_cost-optimization-hub-action-UpdatePreferences")                               |               |                   | Write        |

## Actions defined by AWS Cost Optimization Hub

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                                                                                          | Description                                                                                                       | Resource types (\*required) | Condition keys | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [GetPreferences](../../../aws-cost-management/latest/APIReference/API_CostOptimizationHub_GetPreferences.md "../../../aws-cost-management/latest/APIReference/API_CostOptimizationHub_GetPreferences.md")                                        | Grants permission to get preferences                                                                              |                             |                | Read         |
| [GetRecommendation](../../../aws-cost-management/latest/APIReference/API_CostOptimizationHub_GetRecommendation.md "../../../aws-cost-management/latest/APIReference/API_CostOptimizationHub_GetRecommendation.md")                               | Grants permission to get resource configuration and estimated cost impact for a recommendation                    |                             |                | Read         |
| [ListEfficiencyMetrics](../../../aws-cost-management/latest/APIReference/API_CostOptimizationHub_ListEfficiencyMetrics.md "../../../aws-cost-management/latest/APIReference/API_CostOptimizationHub_ListEfficiencyMetrics.md")                   | Grants permission to list efficiency metric scores by group                                                       |                             |                | List         |
| [ListEnrollmentStatuses](../../../aws-cost-management/latest/APIReference/API_CostOptimizationHub_ListEnrollmentStatuses.md "../../../aws-cost-management/latest/APIReference/API_CostOptimizationHub_ListEnrollmentStatuses.md")                | Grants permission to list enrollment statuses for the specified account or all members under a management account |                             |                | List         |
| [ListRecommendationSummaries](../../../aws-cost-management/latest/APIReference/API_CostOptimizationHub_ListRecommendationSummaries.md "../../../aws-cost-management/latest/APIReference/API_CostOptimizationHub_ListRecommendationSummaries.md") | Grants permission to list recommendation summaries by group                                                       |                             |                | List         |
| [ListRecommendations](../../../aws-cost-management/latest/APIReference/API_CostOptimizationHub_ListRecommendations.md "../../../aws-cost-management/latest/APIReference/API_CostOptimizationHub_ListRecommendations.md")                         | Grants permission to list summary view of recommendations                                                         |                             |                | List         |
| [UpdateEnrollmentStatus](../../../aws-cost-management/latest/APIReference/API_CostOptimizationHub_UpdateEnrollmentStatus.md "../../../aws-cost-management/latest/APIReference/API_CostOptimizationHub_UpdateEnrollmentStatus.md")                | Grants permission to update the enrollment status                                                                 |                             |                | Write        |
| [UpdatePreferences](../../../aws-cost-management/latest/APIReference/API_CostOptimizationHub_UpdatePreferences.md "../../../aws-cost-management/latest/APIReference/API_CostOptimizationHub_UpdatePreferences.md")                               | Grants permission to update preferences                                                                           |                             |                | Write        |

## Resource types defined by AWS Cost Optimization Hub

AWS Cost Optimization Hub does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS Cost Optimization Hub

AWS Cost Optimization Hub has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
