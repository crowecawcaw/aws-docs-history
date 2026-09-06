

# Actions, resources, and condition keys for AWS Auto Scaling
<a name="list_autoscaling-plans"></a>

AWS Auto Scaling (service prefix: `autoscaling-plans`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/autoscaling/plans/userguide/what-is-aws-auto-scaling.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/autoscaling/plans/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/autoscaling/plans/userguide/auth-and-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/autoscaling-plans/autoscaling-plans.json) for this service.

**Topics**
+ [API operations defined by AWS Auto Scaling](#list_autoscaling-plans-operations)
+ [Actions defined by AWS Auto Scaling](#list_autoscaling-plans-actions-as-permissions)
+ [Resource types defined by AWS Auto Scaling](#list_autoscaling-plans-resources-for-iam-policies)
+ [Condition keys for AWS Auto Scaling](#list_autoscaling-plans-policy-keys)

## API operations defined by AWS Auto Scaling
<a name="list_autoscaling-plans-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_autoscaling-plans-actions-as-permissions).




- **   CreateScalingPlan  **
  - **IAM action:**  [autoscaling-plans:CreateScalingPlan](#list_autoscaling-plans-action-CreateScalingPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteScalingPlan  **
  - **IAM action:**  [autoscaling-plans:DeleteScalingPlan](#list_autoscaling-plans-action-DeleteScalingPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeScalingPlanResources  **
  - **IAM action:**  [autoscaling-plans:DescribeScalingPlanResources](#list_autoscaling-plans-action-DescribeScalingPlanResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeScalingPlans  **
  - **IAM action:**  [autoscaling-plans:DescribeScalingPlans](#list_autoscaling-plans-action-DescribeScalingPlans) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetScalingPlanResourceForecastData  **
  - **IAM action:**  [autoscaling-plans:GetScalingPlanResourceForecastData](#list_autoscaling-plans-action-GetScalingPlanResourceForecastData) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   UpdateScalingPlan  **
  - **IAM action:**  [autoscaling-plans:UpdateScalingPlan](#list_autoscaling-plans-action-UpdateScalingPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Auto Scaling
<a name="list_autoscaling-plans-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [CreateScalingPlan](https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_CreateScalingPlan.html)  | Creates a scaling plan. |  |   | Write | 
|   [DeleteScalingPlan](https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_DeleteScalingPlan.html)  | Deletes the specified scaling plan. |  |   | Write | 
|   [DescribeScalingPlanResources](https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_DescribeScalingPlanResources.html)  | Describes the scalable resources in the specified scaling plan. |  |   | Read | 
|   [DescribeScalingPlans](https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_DescribeScalingPlans.html)  | Describes the specified scaling plans or all of your scaling plans. |  |   | Read | 
|   [GetScalingPlanResourceForecastData](https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_GetScalingPlanResourceForecastData.html)  | Retrieves the forecast data for a scalable resource. |  |   | Read | 
|   [UpdateScalingPlan](https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_UpdateScalingPlan.html)  | Updates a scaling plan. |  |   | Write | 

## Resource types defined by AWS Auto Scaling
<a name="list_autoscaling-plans-resources-for-iam-policies"></a>

AWS Auto Scaling does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Auto Scaling
<a name="list_autoscaling-plans-policy-keys"></a>

AWS Auto Scaling has no service-specific condition keys that can be used in the `Condition` element of policy statements.