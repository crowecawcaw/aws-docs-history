# Creating a cluster for

Amazon ECS Managed Instances

You create a cluster to define the infrastructure your tasks and services run on.

When you create a cluster for Amazon ECS Managed Instances, you gain access to the
`FARGATE_MANAGED_INSTANCE` capacity provider by default. This capacity provider
automatically selects the most cost-optimized instance types for your workloads. You can also
create custom capacity providers if you need specific instance attributes or types.

To make the cluster creation process as easy as possible, the console has default
selections for many choices.

- Creates a default namespace in AWS Cloud Map that is the same name as the cluster. A
  namespace allows services that you create in the cluster to connect to the other
  services in the namespace without additional configuration.

For more information, see [Interconnect Amazon ECS services](interconnecting-services.md "interconnecting-services.md").
You can modify the following options:

- Change the default namespace associated with the cluster.

A namespace allows services that you create in the cluster to connect to the
other services in the namespace without additional configuration. The default
namespace is the same as the cluster name. For more information, see [Interconnect Amazon ECS services](interconnecting-services.md "interconnecting-services.md").

- Assign a AWS KMS key for your managed storage. For information about how to create a
  key, see [Create a KMS
  key](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the _AWS Key Management Service User
  Guide_.
- Add tags to help you identify your cluster.

## Prerequisites

Before you begin, be sure that you've completed the steps in [Set up to use Amazon ECS](get-set-up-for-amazon-ecs.md "get-set-up-for-amazon-ecs.md") and
assign the appropriate IAM permission. For more information, see [Amazon ECS cluster examples](security_iam_id-based-policy-examples.md#IAM_cluster_policies "security_iam_id-based-policy-examples.md#IAM_cluster_policies").

The user creating the cluster must have an additional permission:
`iam:CreateServiceLinkedRole`.

By default, Amazon ECS chooses the instance types based on the requirements you specify in the
task definition. This is the default capacity provider. If you need specific instance
attributes or types, take note of all the requirements. You'll need to use a custom capacity
provider, and then specify the instance requirements.

Understand how to choose your instances. For more information, see [Instance selection best practices for Amazon ECS Managed Instances](managed-instances-instance-selection-best-practices.md "managed-instances-instance-selection-best-practices.md").

You have the required IAM roles for Amazon ECS Managed Instances. This includes:

- **Infrastructure role** - Allows Amazon ECS to make calls
  to AWS services on your behalf to manage Amazon ECS Managed Instances infrastructure.

For more information, see [Amazon ECS infrastructure IAM role](infrastructure_IAM_role.md "infrastructure_IAM_role.md").

- **Instance profile** - Provides permissions for the
  Amazon ECS container agent and Docker daemon running on managed instances.

For more information, see [Amazon ECS Managed Instances instance profile](managed-instances-instance-profile.md "managed-instances-instance-profile.md").

## Console procedure

###### To create a new cluster (Amazon ECS console)

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. From the navigation bar, select the Region to use.
3. In the navigation pane, choose **Clusters**.
4. On the **Clusters** page, choose **Create
   cluster**.
5. Under **Cluster configuration**, configure the following:
   - For **Cluster name**, enter a unique name.

   The name can contain up to 255 letters (uppercase and lowercase), numbers,
   and hyphens.
   - (Optional) To have the namespace used for Service Connect be different
     from the cluster name, for **Namespace**, enter a unique
     name.

6. For **Custom Capacity Provider**, do the following:
   - For **Select a method of obtaining EC2 capacity**,
     choose **Amazon ECS Managed Instances**.
   - For Instance profile, choose the instance profile role.
   - For Infrastructure role, choose the infrastructure role.
   - To use a custom capacity provider, for **Instance
     selection**, choose **Use custom**. Then,
     for each attribute, enter the **Attribute
     value**.

7. (Optional) Use Container Insights, expand **Monitoring**, and then choose one
   of the following options:
   - To use the recommended Container Insights with enhanced observability, choose
     **Container Insights with enhanced observability**.
   - To use Container Insights, choose **Container Insights**.

8. (Optional) Encrypt the data on managed storage. Under **Encryption**, for **Managed
   storage**, enter the ARN of the AWS KMS key you want to use to encrypt
   the managed storage data.
9. (Optional) To help identify your cluster, expand **Tags**, and
   then configure your tags.

[Add a tag] Choose **Add tag** and do the following:

    * For **Key**, enter the key name.
    * For **Value**, enter the key value.

10. Choose **Create**.

## AWS CLI procedure

You can create a cluster for Amazon ECS Managed Instances using the AWS CLI. Use the latest version of the AWS CLI. For more information on how to upgrade to the latest version, see [Installing or updating to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").

###### Note

You can use dual-stack service endpoints to interact with Amazon ECS from the AWS AWS CLI, SDKs, and the Amazon ECS API over both IPv4 and IPv6. For more information, see [Using Amazon ECS dual-stack endpoints](dual-stack-endpoint.md "dual-stack-endpoint.md").

###### To create a new cluster (AWS CLI)

1. Create your cluster with a unique name using the following command:

```
aws ecs create-cluster --cluster-name `managed-instances-cluster`
```

Output:

```
{
    "cluster": {
        "status": "ACTIVE",
        "defaultCapacityProviderStrategy": [],
        "statistics": [],
        "capacityProviders": [],
        "tags": [],
        "clusterName": "managed-instances-cluster",
        "settings": [
            {
                "name": "containerInsights",
                "value": "disabled"
            }
        ],
        "registeredContainerInstancesCount": 0,
        "pendingTasksCount": 0,
        "runningTasksCount": 0,
        "activeServicesCount": 0,
        "clusterArn": "arn:aws:ecs:`region`:`aws_account_id`:cluster/managed-instances-cluster"
    }
}
```

2. (Optional) To enable Container Insights with enhanced observability for your cluster, use
   the following command:

```
aws ecs put-account-setting --name containerInsights --value enhanced
```

3. (Optional) To add tags to your cluster, use the following command:

```
aws ecs tag-resource --resource-arn arn:aws:ecs:`region`:`aws_account_id`:cluster/`managed-instances-cluster` --tags key=`Environment`,value=`Production`
```

## Next steps

Create a task definition for Amazon ECS Managed Instances. For more information, see [Creating an Amazon ECS task definition using the
console](create-task-definition.md "create-task-definition.md").

Run your applications as standalone tasks, or as part of a service. For more
information, see the following:

- [Running an application as an Amazon ECS task](standalone-task-create.md "standalone-task-create.md")
- [Creating an Amazon ECS rolling update
  deployment](create-service-console-v2.md "create-service-console-v2.md")
