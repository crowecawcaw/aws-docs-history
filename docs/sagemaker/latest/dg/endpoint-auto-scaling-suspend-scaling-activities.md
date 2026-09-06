

# Temporarily turn off scaling policies
<a name="endpoint-auto-scaling-suspend-scaling-activities"></a>

After you configure auto scaling, you have the following options if you need to investigate an issue without interference from scaling policies (dynamic scaling):
+ Temporarily suspend and then resume scaling activities by calling the [register-scalable-target](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/register-scalable-target.html) CLI command or [RegisterScalableTarget](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html) API action, specifying a Boolean value for both `DynamicScalingInSuspended` and `DynamicScalingOutSuspended`.   
**Example**  

  The following example shows how to suspend scaling policies for a variant named `{{my-variant}}`, running on the `{{my-endpoint}}` endpoint.

  ```
  aws application-autoscaling register-scalable-target \
    --service-namespace sagemaker \
    --resource-id endpoint/{{my-endpoint}}/variant/{{my-variant}} \
    --scalable-dimension sagemaker:variant:DesiredInstanceCount \
    --suspended-state '{"DynamicScalingInSuspended":true,"DynamicScalingOutSuspended":true}'
  ```
+ Prevent specific target tracking scaling policies from scaling in your variant by disabling the policy's scale-in portion. This method prevents the scaling policy from deleting instances, while still allowing it to create them as needed.

  Temporarily disable and then enable scale-in activities by editing the policy using the [put-scaling-policy](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/put-scaling-policy.html) CLI command or the [PutScalingPolicy](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PutScalingPolicy.html) API action, specifying a Boolean value for `DisableScaleIn`.  
**Example**  

  The following is an example of a target tracking configuration for a scaling policy that will scale out but not scale in. 

  ```
  {
      "TargetValue": {{70.0}},
      "PredefinedMetricSpecification":
      {
          "PredefinedMetricType": "{{SageMakerVariantInvocationsPerInstance}}"
      },
      "DisableScaleIn": {{true}}
  }
  ```