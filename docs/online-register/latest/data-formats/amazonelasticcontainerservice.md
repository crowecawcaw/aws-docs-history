

# Data retrieval APIs for Amazon Elastic Container Service
<a name="amazonelasticcontainerservice"></a>

Amazon Elastic Container Service provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="ecs-DescribeCapacityProviders"></a>[DescribeCapacityProviders](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeCapacityProviders.html) | Describe one or more Amazon ECS capacity providers | Read | 
| <a name="ecs-DescribeClusters"></a>[DescribeClusters](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeClusters.html) | Describes one or more of your clusters | Read | 
| <a name="ecs-DescribeContainerInstances"></a>[DescribeContainerInstances](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeContainerInstances.html) | Describes Amazon ECS container instances | Read | 
| <a name="ecs-DescribeDaemon"></a>[DescribeDaemon](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeDaemon.html) | Describe the specified daemon running in your cluster | Read | 
| <a name="ecs-DescribeDaemonDeployments"></a>[DescribeDaemonDeployments](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeDaemonDeployments.html) | Describe one or more of your daemon deployments | Read | 
| <a name="ecs-DescribeDaemonRevisions"></a>[DescribeDaemonRevisions](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeDaemonRevisions.html) | Describe one or more of your daemon revisions | Read | 
| <a name="ecs-DescribeDaemonTaskDefinition"></a>[DescribeDaemonTaskDefinition](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeDaemonTaskDefinition.html) | Describe a daemon task definition | Read | 
| <a name="ecs-DescribeExpressGatewayService"></a>[DescribeExpressGatewayService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeExpressGatewayService.html) | Describe the specified Express Gateway service | Read | 
| <a name="ecs-DescribeServiceDeployments"></a>[DescribeServiceDeployments](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServiceDeployments.html) | Describe one or more of your service deployments | Read | 
| <a name="ecs-DescribeServiceRevisions"></a>[DescribeServiceRevisions](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServiceRevisions.html) | Describe one or more of your service revisions | Read | 
| <a name="ecs-DescribeServices"></a>[DescribeServices](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServices.html) | Describe the specified services running in your cluster | Read | 
| <a name="ecs-DescribeTaskDefinition"></a>[DescribeTaskDefinition](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTaskDefinition.html) | Describe a task definition. You can specify a family and revision to find information about a specific task definition, or you can simply specify the family to find the latest ACTIVE revision in that family | Read | 
| <a name="ecs-DescribeTaskSets"></a>[DescribeTaskSets](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTaskSets.html) | Describe Amazon ECS task sets | Read | 
| <a name="ecs-DescribeTasks"></a>[DescribeTasks](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTasks.html) | Describe a specified task or tasks | Read | 
| <a name="ecs-GetTaskProtection"></a>[GetTaskProtection](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_GetTaskProtection.html) | Retrieve the protection status of tasks in an Amazon ECS service | Read | 
| <a name="ecs-ListAccountSettings"></a>[ListAccountSettings](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListAccountSettings.html) | List the account settings for an Amazon ECS resource for a specified principal | Read | 
| <a name="ecs-ListAttributes"></a>[ListAttributes](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListAttributes.html) | Lists the attributes for Amazon ECS resources within a specified target type and cluster | List | 
| <a name="ecs-ListClusters"></a>[ListClusters](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html) | Get a list of existing clusters | List | 
| <a name="ecs-ListContainerInstances"></a>[ListContainerInstances](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListContainerInstances.html) | Get a list of container instances in a specified cluster | List | 
| <a name="ecs-ListDaemonDeployments"></a>[ListDaemonDeployments](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListDaemonDeployments.html) | Get a list of daemon deployments for a specified daemon | List | 
| <a name="ecs-ListDaemonTaskDefinitions"></a>[ListDaemonTaskDefinitions](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListDaemonTaskDefinitions.html) | Get a list of daemon task definitions that are registered to your account | List | 
| <a name="ecs-ListDaemons"></a>[ListDaemons](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListDaemons.html) | Get a list of daemons that are running in a specified cluster | List | 
| <a name="ecs-ListServiceDeployments"></a>[ListServiceDeployments](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServiceDeployments.html) | Get a list of service deployments for a specified service | List | 
| <a name="ecs-ListServices"></a>[ListServices](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html) | Get a list of services that are running in a specified cluster | List | 
| <a name="ecs-ListServicesByNamespace"></a>[ListServicesByNamespace](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServicesByNamespace.html) | Get a list of services that are running in a specified AWS Cloud Map Namespace | List | 
| <a name="ecs-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListTagsForResource.html) | Get a list of tags for the specified resource | Read | 
| <a name="ecs-ListTaskDefinitionFamilies"></a>[ListTaskDefinitionFamilies](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListTaskDefinitionFamilies.html) | Get a list of task definition families that are registered to your account (which may include task definition families that no longer have any ACTIVE task definitions) | List | 
| <a name="ecs-ListTaskDefinitions"></a>[ListTaskDefinitions](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListTaskDefinitions.html) | Get a list of task definitions that are registered to your account | List | 
| <a name="ecs-ListTasks"></a>[ListTasks](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListTasks.html) | Get a list of tasks for a specified cluster | List | 