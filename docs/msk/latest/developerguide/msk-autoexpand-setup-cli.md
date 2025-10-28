# Set up automatic scaling using the CLI

This process describes how to use the Amazon MSK CLI to implement automatic scaling for storage.

1. Use the [RegisterScalableTarget](../../../cli/latest/reference/application-autoscaling.md#available-commands "../../../cli/latest/reference/application-autoscaling.md#available-commands") command to register a storage utilization
   target.
2. Use the [PutScalingPolicy](../../../cli/latest/reference/application-autoscaling.md#available-commands "../../../cli/latest/reference/application-autoscaling.md#available-commands") command to create an auto-expansion policy.
