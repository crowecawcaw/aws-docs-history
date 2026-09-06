

# Actions, resources, and condition keys for AWS Cost Optimization Hub
<a name="list_cost-optimization-hub"></a>

AWS Cost Optimization Hub (service prefix: `cost-optimization-hub`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/cost-management/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/cost-optimization-hub/cost-optimization-hub.json) for this service.

**Topics**
+ [API operations defined by AWS Cost Optimization Hub](#list_cost-optimization-hub-operations)
+ [Actions defined by AWS Cost Optimization Hub](#list_cost-optimization-hub-actions-as-permissions)
+ [Resource types defined by AWS Cost Optimization Hub](#list_cost-optimization-hub-resources-for-iam-policies)
+ [Condition keys for AWS Cost Optimization Hub](#list_cost-optimization-hub-policy-keys)

## API operations defined by AWS Cost Optimization Hub
<a name="list_cost-optimization-hub-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_cost-optimization-hub-actions-as-permissions).




- **   GetPreferences  **
  - **IAM action:**  [cost-optimization-hub:GetPreferences](#list_cost-optimization-hub-action-GetPreferences) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRecommendation  **
  - **IAM action:**  [cost-optimization-hub:GetRecommendation](#list_cost-optimization-hub-action-GetRecommendation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListEfficiencyMetrics  **
  - **IAM action:**  [cost-optimization-hub:ListEfficiencyMetrics](#list_cost-optimization-hub-action-ListEfficiencyMetrics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEnrollmentStatuses  **
  - **IAM action:**  [cost-optimization-hub:ListEnrollmentStatuses](#list_cost-optimization-hub-action-ListEnrollmentStatuses) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRecommendationSummaries  **
  - **IAM action:**  [cost-optimization-hub:ListRecommendationSummaries](#list_cost-optimization-hub-action-ListRecommendationSummaries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRecommendations  **
  - **IAM action:**  [cost-optimization-hub:ListRecommendations](#list_cost-optimization-hub-action-ListRecommendations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   UpdateEnrollmentStatus  **
  - **IAM action:**  [cost-optimization-hub:UpdateEnrollmentStatus](#list_cost-optimization-hub-action-UpdateEnrollmentStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePreferences  **
  - **IAM action:**  [cost-optimization-hub:UpdatePreferences](#list_cost-optimization-hub-action-UpdatePreferences) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Cost Optimization Hub
<a name="list_cost-optimization-hub-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [GetPreferences](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_GetPreferences.html)  | Grants permission to get preferences |  |   | Read | 
|   [GetRecommendation](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_GetRecommendation.html)  | Grants permission to get resource configuration and estimated cost impact for a recommendation |  |   | Read | 
|   [ListEfficiencyMetrics](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_ListEfficiencyMetrics.html)  | Grants permission to list efficiency metric scores by group |  |   | List | 
|   [ListEnrollmentStatuses](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_ListEnrollmentStatuses.html)  | Grants permission to list enrollment statuses for the specified account or all members under a management account |  |   | List | 
|   [ListRecommendationSummaries](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_ListRecommendationSummaries.html)  | Grants permission to list recommendation summaries by group |  |   | List | 
|   [ListRecommendations](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_ListRecommendations.html)  | Grants permission to list summary view of recommendations |  |   | List | 
|   [UpdateEnrollmentStatus](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_UpdateEnrollmentStatus.html)  | Grants permission to update the enrollment status |  |   | Write | 
|   [UpdatePreferences](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_UpdatePreferences.html)  | Grants permission to update preferences |  |   | Write | 

## Resource types defined by AWS Cost Optimization Hub
<a name="list_cost-optimization-hub-resources-for-iam-policies"></a>

AWS Cost Optimization Hub does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Cost Optimization Hub
<a name="list_cost-optimization-hub-policy-keys"></a>

AWS Cost Optimization Hub has no service-specific condition keys that can be used in the `Condition` element of policy statements.