# Updating managed termination

protection for Amazon ECS capacity providers

When you use managed termination protection, you need to update the
setting for existing capacity providers.

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. On the **Clusters** page, choose the
   cluster.
3. On the cluster page, chooset the **Infrastructure**
   tab.
4. Choose the capacity provider.
5. Choose **Update** to modify the capacity provider settings.
6. Under **Auto Scaling group settings**, toggle **Managed termination protection** to enable or disable the feature.
7. Choose **Update**.
   You can update a capacity provider's managed termination protection setting using the `update-capacity-provider` command:

To enable managed termination protection:

```
`aws ecs update-capacity-provider \
 --name `CapacityProviderName` \
 --auto-scaling-group-provider "managedScaling={status=ENABLED,targetCapacity=70,minimumScalingStepSize=1,maximumScalingStepSize=10},managedTerminationProtection=ENABLED"`
```

To disable managed termination protection:

```
`aws ecs update-capacity-provider \
 --name `CapacityProviderName` \
 --auto-scaling-group-provider "managedScaling={status=ENABLED,targetCapacity=70,minimumScalingStepSize=1,maximumScalingStepSize=10},managedTerminationProtection=DISABLED"`
```

###### Note

It might take a few minutes for the changes to take effect across your
cluster. When enabling managed termination protection, instances that
are already running tasks will be protected from scale-in events. When
disabling managed termination protection, the protection flag will be
removed from instances during the next ECS capacity provider management
cycle.

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. On the **Clusters** page, choose the
   cluster.
3. On the cluster page, chooset the **Tasks**
   tab.
4. Choose the task.
5. Under **Configuration**, toggle **Managed termination protection** to enable or disable the feature.
6. Choose **Configure task scale-in protection**.

The **Configure task scale-in protection** dialog box displays

    1. Under **Task scale-in protection**, toggle **Turn on**.
    2. For **Expires in minutes**, enter the number of minutes before task scale-in
     protection ends.
    3. Choose **Update**
