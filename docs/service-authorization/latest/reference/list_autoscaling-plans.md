# Actions, resources, and condition keys for AWS Auto Scaling

AWS Auto Scaling (service prefix: `autoscaling-plans`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../autoscaling/plans/userguide/what-is-aws-auto-scaling.md "../../../autoscaling/plans/userguide/what-is-aws-auto-scaling.md").
- View a list of the [API operations available for
  this service](../../../autoscaling/plans/APIReference/Welcome.md "../../../autoscaling/plans/APIReference/Welcome.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../autoscaling/plans/userguide/auth-and-access-control.md "../../../autoscaling/plans/userguide/auth-and-access-control.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/autoscaling-plans/autoscaling-plans.json "https://servicereference.us-east-1.amazonaws.com/v1/autoscaling-plans/autoscaling-plans.json") for this service.

###### Topics

- [API operations defined by AWS Auto Scaling](#list_autoscaling-plans-operations "#list_autoscaling-plans-operations")
- [Actions defined by AWS Auto Scaling](#list_autoscaling-plans-actions-as-permissions "#list_autoscaling-plans-actions-as-permissions")
- [Resource types defined by AWS Auto Scaling](#list_autoscaling-plans-resources-for-iam-policies "#list_autoscaling-plans-resources-for-iam-policies")
- [Condition keys for AWS Auto Scaling](#list_autoscaling-plans-policy-keys "#list_autoscaling-plans-policy-keys")

## API operations defined by AWS Auto Scaling

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_autoscaling-plans-actions-as-permissions "#list_autoscaling-plans-actions-as-permissions").

| Operation                          | IAM action                                                                                                                                                                                    | Condition key | Possible value(s) | Access level |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ----------------- | ------------ |
| CreateScalingPlan                  | [autoscaling-plans:CreateScalingPlan](#list_autoscaling-plans-action-CreateScalingPlan "#list_autoscaling-plans-action-CreateScalingPlan")                                                    |               |                   | Write        |
| DeleteScalingPlan                  | [autoscaling-plans:DeleteScalingPlan](#list_autoscaling-plans-action-DeleteScalingPlan "#list_autoscaling-plans-action-DeleteScalingPlan")                                                    |               |                   | Write        |
| DescribeScalingPlanResources       | [autoscaling-plans:DescribeScalingPlanResources](#list_autoscaling-plans-action-DescribeScalingPlanResources "#list_autoscaling-plans-action-DescribeScalingPlanResources")                   |               |                   | Read         |
| DescribeScalingPlans               | [autoscaling-plans:DescribeScalingPlans](#list_autoscaling-plans-action-DescribeScalingPlans "#list_autoscaling-plans-action-DescribeScalingPlans")                                           |               |                   | Read         |
| GetScalingPlanResourceForecastData | [autoscaling-plans:GetScalingPlanResourceForecastData](#list_autoscaling-plans-action-GetScalingPlanResourceForecastData "#list_autoscaling-plans-action-GetScalingPlanResourceForecastData") |               |                   | Read         |
| UpdateScalingPlan                  | [autoscaling-plans:UpdateScalingPlan](#list_autoscaling-plans-action-UpdateScalingPlan "#list_autoscaling-plans-action-UpdateScalingPlan")                                                    |               |                   | Write        |

## Actions defined by AWS Auto Scaling

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                                                     | Description                                                         | Resource types (\*required) | Condition keys | Access level |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [CreateScalingPlan](../../../autoscaling/plans/APIReference/API_CreateScalingPlan.md "../../../autoscaling/plans/APIReference/API_CreateScalingPlan.md")                                                    | Creates a scaling plan.                                             |                             |                | Write        |
| [DeleteScalingPlan](../../../autoscaling/plans/APIReference/API_DeleteScalingPlan.md "../../../autoscaling/plans/APIReference/API_DeleteScalingPlan.md")                                                    | Deletes the specified scaling plan.                                 |                             |                | Write        |
| [DescribeScalingPlanResources](../../../autoscaling/plans/APIReference/API_DescribeScalingPlanResources.md "../../../autoscaling/plans/APIReference/API_DescribeScalingPlanResources.md")                   | Describes the scalable resources in the specified scaling plan.     |                             |                | Read         |
| [DescribeScalingPlans](../../../autoscaling/plans/APIReference/API_DescribeScalingPlans.md "../../../autoscaling/plans/APIReference/API_DescribeScalingPlans.md")                                           | Describes the specified scaling plans or all of your scaling plans. |                             |                | Read         |
| [GetScalingPlanResourceForecastData](../../../autoscaling/plans/APIReference/API_GetScalingPlanResourceForecastData.md "../../../autoscaling/plans/APIReference/API_GetScalingPlanResourceForecastData.md") | Retrieves the forecast data for a scalable resource.                |                             |                | Read         |
| [UpdateScalingPlan](../../../autoscaling/plans/APIReference/API_UpdateScalingPlan.md "../../../autoscaling/plans/APIReference/API_UpdateScalingPlan.md")                                                    | Updates a scaling plan.                                             |                             |                | Write        |

## Resource types defined by AWS Auto Scaling

AWS Auto Scaling does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS Auto Scaling

AWS Auto Scaling has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
