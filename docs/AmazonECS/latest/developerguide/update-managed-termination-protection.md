

# Updating managed termination protection for Amazon ECS capacity providers
<a name="update-managed-termination-protection"></a>

When you use managed termination protection, you need to update the setting for existing capacity providers.

## Console
<a name="update-managed-termination-protection-console"></a>

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. On the **Clusters** page, choose the cluster.

1. On the cluster page, chooset the **Infrastructure** tab.

1. Choose the capacity provider.

1. Choose **Update** to modify the capacity provider settings.

1. Under **Auto Scaling group settings**, toggle **Managed termination protection** to enable or disable the feature.

1. Choose **Update**.

## AWS CLI
<a name="update-managed-termination-protection-cli"></a>

You can update a capacity provider's managed termination protection setting using the `update-capacity-provider` command:

To enable managed termination protection:

```
aws ecs update-capacity-provider \
  --name {{CapacityProviderName}} \
  --auto-scaling-group-provider "managedScaling={status=ENABLED,targetCapacity=70,minimumScalingStepSize=1,maximumScalingStepSize=10},managedTerminationProtection=ENABLED"
```

To disable managed termination protection:

```
aws ecs update-capacity-provider \
  --name {{CapacityProviderName}} \
  --auto-scaling-group-provider "managedScaling={status=ENABLED,targetCapacity=70,minimumScalingStepSize=1,maximumScalingStepSize=10},managedTerminationProtection=DISABLED"
```

**Note**  
It might take a few minutes for the changes to take effect across your cluster. When enabling managed termination protection, instances that are already running tasks will be protected from scale-in events. When disabling managed termination protection, the protection flag will be removed from instances during the next ECS capacity provider management cycle.

## Console for running tasks
<a name="update-managed-termination-protection-console"></a>

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. On the **Clusters** page, choose the cluster.

1. On the cluster page, chooset the **Tasks** tab.

1. Choose the task.

1. Under **Configuration**, toggle **Managed termination protection** to enable or disable the feature.

1. Choose **Configure task scale-in protection**.

   The **Configure task scale-in protection** dialog box displays

   1. Under **Task scale-in protection**, toggle **Turn on**.

   1. For **Expires in minutes**, enter the number of minutes before task scale-in protection ends.

   1. Choose **Update**