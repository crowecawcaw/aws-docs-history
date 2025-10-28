# Set up automatic-scaling for Amazon MSK using the API

This process describes how to use the Amazon MSK API to implement automatic scaling for storage.

1. Use the [RegisterScalableTarget](../../../autoscaling/application/APIReference/API_RegisterScalableTarget.md "../../../autoscaling/application/APIReference/API_RegisterScalableTarget.md") API to register a storage utilization
   target.
2. Use the [PutScalingPolicy](../../../autoscaling/application/APIReference/API_PutScalingPolicy.md "../../../autoscaling/application/APIReference/API_PutScalingPolicy.md") API to create an auto-expansion policy.
