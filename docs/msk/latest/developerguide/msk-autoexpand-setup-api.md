

# Set up automatic-scaling for Amazon MSK using the API
<a name="msk-autoexpand-setup-api"></a>

This process describes how to use the Amazon MSK API to implement automatic scaling for storage.

1. Use the [ RegisterScalableTarget](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html) API to register a storage utilization target.

1. Use the [ PutScalingPolicy](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PutScalingPolicy.html) API to create an auto-expansion policy.