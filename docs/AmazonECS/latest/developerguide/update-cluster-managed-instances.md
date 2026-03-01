# Updating a cluster to use Amazon ECS Managed Instances

You can update an existing cluster to use Amazon ECS Managed Instances.

When you add Amazon ECS Managed Instances to your cluster, you gain access to the
`FARGATE_MANAGED_INSTANCE` capacity provider by default. This capacity provider
automatically selects the most cost-optimized general-purpose instance types for your workloads. You can also
create custom capacity providers if you need specific instance attributes or types.

## Prerequisites

By default, Amazon ECS chooses the instance types based on the requirements you specify in
the task definition. This is the default capacity provider. If you need specific
instance attributes or types, take note of all the requirements. You'll need to use a
custom capacity provider, and then specify the instance requirements.

You have the required IAM roles for Amazon ECS Managed Instances. This includes:

- **Infrastructure role** - Allows Amazon ECS to make
  calls to AWS services on your behalf to manage Amazon ECS Managed Instances
  infrastructure.

For more information, see [Amazon ECS infrastructure IAM role](infrastructure_IAM_role.md "infrastructure_IAM_role.md").

- **Instance profile** - Provides permissions for
  the Amazon ECS container agent and Docker daemon running on managed instances.

For more information, see [Amazon ECS Managed Instances instance profile](managed-instances-instance-profile.md "managed-instances-instance-profile.md").

## Update considerations

When updating a cluster for Amazon ECS Managed Instances, consider the following:

- Running tasks - Updating cluster settings does not affect
  currently running tasks. Changes will apply to new tasks launched after the update.
- Capacity provider changes - If you modify capacity provider
  settings, existing managed instances will continue to run, but new instances will use the
  updated configuration.
- Monitoring changes - Enabling or disabling Container Insights will
  affect metric collection for the entire cluster.

## Console procedure

###### To update a cluster (Amazon ECS console)

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. From the navigation bar, select the Region to use.
3. In the navigation pane, choose **Clusters**.
4. On the **Clusters** page, select the cluster you want to update.
5. Choose **Update cluster**.
6. (Optional) To modify capacity provider settings, under **Custom Capacity Provider**,
   update the following as needed:
   - For **Instance profile**, choose a different instance profile role if needed.
   - For **Infrastructure role**, choose a different infrastructure role if needed.
   - To use a custom capacity provider, for **Instance
     selection**, update the **Attribute
     value** settings.

7. Choose **Update**.

## AWS CLI procedure

You can update a cluster for Amazon ECS Managed Instances using the AWS CLI. Use the latest version of the AWS CLI. For more information on how to upgrade to the latest version, see [Installing or updating to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").

###### Note

You can use dual-stack service endpoints to interact with Amazon ECS from the AWS AWS CLI, SDKs, and the Amazon ECS API over both IPv4 and IPv6. For more information, see [Using Amazon ECS dual-stack endpoints](dual-stack-endpoint.md "dual-stack-endpoint.md").

###### To update a cluster (AWS CLI)

1. Create a capacity provider for . Run the following command:

Replace the `user-input` with your values.

```
aws ecs create-capacity-provider \
    --name `my-managed-instances-provider` \
    --managed-instances-provider \
    --instance-profile `arn:aws:iam::123456789012:instance-profile/ecsInstanceProfile` \
    --infrastructure-role-arn `arn:aws:iam::123456789012:role/ecsInfrastructureRole` \
    --instance-requirements '{
        "vCpuCount": {"min": 2, "max": 8},
        "memoryMiB": {"min": 4096, "max": 16384}
    }
```

2. Add the capacity provider to the cluster, use the following command:

Replace the `user-input` with your values.

```
aws ecs put-cluster-capacity-providers --cluster `managed-instances-cluster` --capacity-providers `my-managed-instances-provider` --default-capacity-provider-strategy capacityProvider=`my-managed-instances-provider`,weight=1
```
