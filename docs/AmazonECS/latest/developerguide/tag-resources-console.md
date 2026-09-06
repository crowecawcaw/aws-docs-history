

# Adding tags to Amazon ECS resources
<a name="tag-resources-console"></a>

You can tag new or existing tasks, services, task definitions, or clusters. For information about tagging your container instances, see [Adding tags to an Amazon EC2 container instance for Amazon ECS](instance-details-tags.md).

**Warning**  
Do not add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including billing. Tags are not intended to be used for private or sensitive data.

You can use the following resources to specify tags when you create the resource.


|  Task  |  Console  |  AWS CLI  |  API Action  | 
| --- | --- | --- | --- | 
| Run one or more tasks. | [Running an application as an Amazon ECS task](standalone-task-create.md) | [run-task](https://docs.aws.amazon.com/cli/latest/reference/ecs/run-task.html) | [RunTask](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html) | 
| Create a service. | [Creating an Amazon ECS rolling update deployment](create-service-console-v2.md) | [create-service](https://docs.aws.amazon.com/cli/latest/reference/ecs/create-service.html) | [CreateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html) | 
| Create a task set. | [Deploy Amazon ECS services using a third-party controller](deployment-type-external.md) | [create-task-set](https://docs.aws.amazon.com/cli/latest/reference/ecs/create-task-set.html) | [CreateTaskSet](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateTaskSet.html) | 
| Register a task definition. | [Creating an Amazon ECS task definition using the console](create-task-definition.md) | [register-task-definition](https://docs.aws.amazon.com/cli/latest/reference/ecs/register-task-definition.html) | [RegisterTaskDefinition](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RegisterTaskDefinition.html) | 
| Create a cluster. | [Creating an Amazon ECS cluster for Fargate workloads](create-cluster-console-v2.md)  | [create-cluster](https://docs.aws.amazon.com/cli/latest/reference/ecs/create-cluster.html) | [CreateCluster](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateCluster.html) | 
| Run one or more container instances. | [Launching an Amazon ECS Linux container instance](launch_container_instance.md) | [run-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html) | [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html) | 
| Create a capacity provider for Amazon ECS Managed Instances. | [Creating a capacity provider for Amazon ECS Managed Instances](create-capacity-provider-managed-instances.md) | [create-capacity-provider](https://docs.aws.amazon.com/cli/latest/reference/ecs/create-capacity-provider.html) | [CreateCapacityProvider](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateCapacityProvider.html) | 

## Adding tags to existing resources (Amazon ECS console)
<a name="adding-or-deleting-tags"></a>

You can add or delete tags that are associated with your clusters, services, tasks, and task definitions directly from the resource's page.

**To modify a tag for an individual resource**

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. From the navigation bar, select the AWS Region to use.

1. In the navigation pane, select a resource type (for example, **Clusters**).

1. Select the resource from the resource list, choose the **Tags** tab, and then choose **Manage tags**.

1. Configure your tags.

   [Add a tag] Choose **Add tag**, and then do the following:
   + For **Key**, enter the key name.
   + For **Value**, enter the key value.

1. Choose **Save**.

## Adding tags to existing resources (AWS CLI)
<a name="tag-resources-api-sdk"></a>

You can add or overwrite one or more tags by using the AWS CLI or an API.

**Note**  
You can use dual-stack service endpoints to interact with Amazon ECS from the AWS CLI, SDKs, and the Amazon ECS API over both IPv4 and IPv6. For more information, see [Using Amazon ECS dual-stack endpoints](dual-stack-endpoint.md).
+ AWS CLI - [tag-resource](https://docs.aws.amazon.com/cli/latest/reference/ecs/tag-resource.html)
+ API action - [TagResource](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TagResource.html)