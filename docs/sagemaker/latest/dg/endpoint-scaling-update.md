# Update endpoints that use auto scaling

When you update an endpoint, Application Auto Scaling checks to see whether any of the models on that
endpoint are targets for auto scaling. If the update would change the instance type for
any model that is a target for auto scaling, the update fails.

In the AWS Management Console, you see a warning that you must deregister the model from auto
scaling before you can update it. If you are trying to update the endpoint by calling
the [UpdateEndpoint](../APIReference/API_UpdateEndpoint.md "../APIReference/API_UpdateEndpoint.md")
API, the call fails. Before you update the endpoint, delete any scaling policies
configured for it and deregister the variant as a scalable target by calling the [DeregisterScalableTarget](../../../autoscaling/application/APIReference/API_DeregisterScalableTarget.md "../../../autoscaling/application/APIReference/API_DeregisterScalableTarget.md") Application Auto Scaling API action. After you update the
endpoint, you can register the updated variant as a scalable target and attach a scaling
policy.

There is one exception. If you change the model for a variant that is configured for
auto scaling, Amazon SageMaker AI auto scaling allows the update. This is because changing the
model doesn't typically affect performance enough to change scaling behavior. If you do
update a model for a variant configured for auto scaling, ensure that the change to the
model doesn't significantly affect performance and scaling behavior.

When you update SageMaker AI endpoints that have auto scaling applied, complete the following
steps:

###### To update an endpoint that has auto scaling applied

1. Deregister the endpoint as a scalable target by calling [DeregisterScalableTarget](../../../autoscaling/application/APIReference/API_DeregisterScalableTarget.md "../../../autoscaling/application/APIReference/API_DeregisterScalableTarget.md").
2. Because auto scaling is blocked while the update operation is in progress (or
   if you turned off auto scaling in the previous step), you might want to take the
   additional precaution of increasing the number of instances for your endpoint
   during the update. To do this, update the instance counts for the production
   variants hosted at the endpoint by calling [UpdateEndpointWeightsAndCapacities](../APIReference/API_UpdateEndpointWeightsAndCapacities.md "../APIReference/API_UpdateEndpointWeightsAndCapacities.md").
3. Call [DescribeEndpoint](../APIReference/API_DescribeEndpoint.md "../APIReference/API_DescribeEndpoint.md") repeatedly until the value of the
   `EndpointStatus` field of the response is
   `InService`.
4. Call [DescribeEndpointConfig](../APIReference/API_DescribeEndpointConfig.md "../APIReference/API_DescribeEndpointConfig.md") to get the values of the current endpoint
   config.
5. Create a new endpoint config by calling [CreateEndpointConfig](../APIReference/API_CreateEndpointConfig.md "../APIReference/API_CreateEndpointConfig.md"). For the production variants where you want to
   keep the existing instance count or weight, use the same variant name from the
   response from the call to [DescribeEndpointConfig](../APIReference/API_DescribeEndpointConfig.md "../APIReference/API_DescribeEndpointConfig.md") in the previous step. For all other values,
   use the values that you got as the response when you called [DescribeEndpointConfig](../APIReference/API_DescribeEndpointConfig.md "../APIReference/API_DescribeEndpointConfig.md") in the previous step.
6. Update the endpoint by calling [UpdateEndpoint](../APIReference/API_UpdateEndpoint.md "../APIReference/API_UpdateEndpoint.md"). Specify the endpoint config you created in the
   previous step as the `EndpointConfig` field. If you want to retain
   the variant properties like instance count or weight, set the value of the
   `RetainAllVariantProperties` parameter to `True`. This
   specifies that production variants with the same name will are updated with the
   most recent `DesiredInstanceCount` from the response from the call to
   `DescribeEndpoint`, regardless of the values of the
   `InitialInstanceCount` field in the new
   `EndpointConfig`.
7. (Optional) Re-activate auto scaling by calling [RegisterScalableTarget](../../../autoscaling/application/APIReference/API_RegisterScalableTarget.md "../../../autoscaling/application/APIReference/API_RegisterScalableTarget.md") and [PutScalingPolicy](../../../autoscaling/application/APIReference/API_PutScalingPolicy.md "../../../autoscaling/application/APIReference/API_PutScalingPolicy.md").

###### Note

Steps 1 and 7 are required only if you are updating an endpoint with the following
changes:

- Changing the instance type for a production variant that has auto scaling
  configured
- Removing a production variant that has auto scaling configured.
