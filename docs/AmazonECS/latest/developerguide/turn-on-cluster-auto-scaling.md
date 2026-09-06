

# Turning on Amazon ECS cluster auto scaling
<a name="turn-on-cluster-auto-scaling"></a>

You turn on cluster auto scaling so that Amazon ECS manages the scaling of Amazon EC2 instances that are registered to your cluster.

If you want to use the console to turn on Cluster auto scaling, see see [Creating a capacity provider for Amazon ECS](create-capacity-provider-console-v2.md).

Before you begin, create an Auto Scaling group and a capacity provider. For more information, see [Amazon ECS capacity providers for EC2 workloads](asg-capacity-providers.md).

To turn on cluster auto scaling, you associate the capacity provider with the cluster, Then you turn on cluster auto scaling.

1. Use the `put-cluster-capacity-providers` command to associate one or more capacity providers with the cluster. 

   To add the AWS Fargate capacity providers, include the `FARGATE` and `FARGATE_SPOT` capacity providers in the request. For more information, see `[put-cluster-capacity-providers](https://docs.aws.amazon.com/cli/latest/reference/ecs/put-cluster-capacity-providers.html)` in the *AWS CLI Command Reference*.

   ```
   aws ecs put-cluster-capacity-providers \
     --cluster {{ClusterName}} \
     --capacity-providers {{CapacityProviderName}} FARGATE FARGATE_SPOT \
     --default-capacity-provider-strategy capacityProvider=CapacityProvider,weight=1
   ```

   To add an Auto Scaling group for EC2, include the Auto Scaling group name in the request. For more information, see `[put-cluster-capacity-providers](https://docs.aws.amazon.com/cli/latest/reference/ecs/put-cluster-capacity-providers.html)` in the *AWS CLI Command Reference*.

   ```
   aws ecs put-cluster-capacity-providers \
     --cluster {{ClusterName}} \
     --capacity-providers {{CapacityProviderName}} \
     --default-capacity-provider-strategy capacityProvider=CapacityProvider,weight=1
   ```

1. Use the `describe-clusters` command to verify that the association was successful. For more information, see `[describe-clusters](https://docs.aws.amazon.com/cli/latest/reference/ecs/describe-clusters.html)` in the *AWS CLI Command Reference*.

   ```
   aws ecs describe-clusters \
     --cluster {{ClusterName}} \
     --include ATTACHMENTS
   ```

1. Use the `update-capacity-provider` command to turn on managed auto scaling for the capacity provider. For more information, see `[update-capacity-provider](https://docs.aws.amazon.com/cli/latest/reference/ecs/update-capacity-provider.html)` in the *AWS CLI Command Reference*.

   ```
   aws ecs update-capacity-provider \
     --name {{CapacityProviderName}} \
     --auto-scaling-group-provider "managedScaling={status=ENABLED}"
   ```