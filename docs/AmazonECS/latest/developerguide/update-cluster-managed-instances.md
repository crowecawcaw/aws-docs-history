

# Updating a cluster to use Amazon ECS Managed Instances
<a name="update-cluster-managed-instances"></a>

You can update an existing cluster to use Amazon ECS Managed Instances.

When you add Amazon ECS Managed Instances to your cluster, Amazon ECS automatically creates a managed instances capacity provider with default configurations. This capacity provider selects the most cost-optimized general-purpose instance types for your workloads. You can also create custom capacity providers if you need specific instance attributes or types.

## Prerequisites
<a name="update-cluster-managed-instances-prerequisites"></a>

When you don't specify `instanceRequirements`, Amazon ECS automatically selects the most cost-optimized instance types based on your task definition requirements. To use specific instance attributes or types, create a capacity provider with `instanceRequirements`.

You have the required IAM roles for Amazon ECS Managed Instances. This includes:
+ **Infrastructure role** - Allows Amazon ECS to make calls to AWS services on your behalf to manage Amazon ECS Managed Instances infrastructure.

  For more information, see [Amazon ECS infrastructure IAM role](infrastructure_IAM_role.md).
+ **Instance profile** - Provides permissions for the Amazon ECS container agent and Docker daemon running on managed instances.

  For more information, see [Amazon ECS Managed Instances instance profile](managed-instances-instance-profile.md).

## Update considerations
<a name="cluster-update-considerations-managed-instances"></a>

When updating a cluster for Amazon ECS Managed Instances, consider the following:
+ Running tasks - Updating cluster settings does not affect currently running tasks. Changes will apply to new tasks launched after the update.
+ Capacity provider changes - If you modify capacity provider settings, existing managed instances will continue to run, but new instances will use the updated configuration.
+ Monitoring changes - Enabling or disabling Container Insights will affect metric collection for the entire cluster.

## Console procedure
<a name="update-cluster-managed-instances-console"></a>

**To update a cluster (Amazon ECS console)**

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. From the navigation bar, select the Region to use.

1. In the navigation pane, choose **Clusters**.

1. On the **Clusters** page, select the cluster you want to update.

1. Choose **Update cluster**.

1. (Optional) To modify capacity provider settings, under **Custom Capacity Provider**, update the following as needed:
   + For **Instance profile**, choose a different instance profile role if needed.
   + For **Infrastructure role**, choose a different infrastructure role if needed.
   + To use a custom capacity provider, for **Instance selection**, update the **Attribute value** settings.

1. Choose **Update**.

## AWS CLI procedure
<a name="update-cluster-managed-instances-cli"></a>

You can update a cluster for Amazon ECS Managed Instances using the AWS CLI. Use the latest version of the AWS CLI. For more information on how to upgrade to the latest version, see [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

**Note**  
You can use dual-stack service endpoints to interact with Amazon ECS from the AWS AWS CLI, SDKs, and the Amazon ECS API over both IPv4 and IPv6. For more information, see [Using Amazon ECS dual-stack endpoints](dual-stack-endpoint.md).

**To update a cluster (AWS CLI)**

1. Create a capacity provider for . Run the following command:

   Replace the {{user-input}} with your values.

   ```
   aws ecs create-capacity-provider \
       --name {{my-managed-instances-provider}} \
       --managed-instances-provider \
       --instance-profile {{arn:aws:iam::123456789012:instance-profile/ecsInstanceProfile}} \
       --infrastructure-role-arn {{arn:aws:iam::123456789012:role/ecsInfrastructureRole}} \
       --instance-requirements '{
           "vCpuCount": {"min": 2, "max": 8},
           "memoryMiB": {"min": 4096, "max": 16384}
       }
   ```

1. Add the capacity provider to the cluster, use the following command:

   Replace the {{user-input}} with your values.

   ```
   aws ecs put-cluster-capacity-providers --cluster {{managed-instances-cluster}} --capacity-providers {{my-managed-instances-provider}} --default-capacity-provider-strategy capacityProvider={{my-managed-instances-provider}},weight=1
   ```