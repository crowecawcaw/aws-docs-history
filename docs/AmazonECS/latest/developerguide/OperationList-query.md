

# Actions by Amazon ECS resource
<a name="OperationList-query"></a>

The following section lists the API actions by resource.

**Topics**
+ [Account setting actions](#OperationList-query-account)
+ [Cluster actions](#OperationList-query-cluster)
+ [Cluster capacity provider actions](#OperationList-query-cluster-capacity-provider)
+ [Container actions](#OperationList-query-containers)
+ [Container agent actions](#OperationList-query-container-agent)
+ [Container instance actions](#OperationList-query-container-instance)
+ [Namespace actions](#OperationList-query-namespace)
+ [Service actions](#OperationList-query-services)
+ [Service deployment actions](#OperationList-query-service-deployments)
+ [Service revision actions](#OperationList-query-service-revisions)
+ [Task definition actions](#OperationList-query-task-definitions)
+ [Task actions](#OperationList-query-tasks)
+ [Task set actions](#OperationList-query-task-sets)
+ [Tag actions](#OperationList-query-tags)

## Account setting actions
<a name="OperationList-query-account"></a>

The following API actions are available for account settings:
+  [DeleteAccountSetting](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteAccountSetting.html) 
+  [ListAccountSettings](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListAccountSettings.html) 
+  [PutAccountSetting](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAccountSetting.html) 
+  [PutAccountSettingDefault](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAccountSettingDefault.html) 

## Cluster actions
<a name="OperationList-query-cluster"></a>

The following API actions are available for clusters:
+  [CreateCluster](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateCluster.html) 
+  [DeleteCluster](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteCluster.html) 
+  [DescribeClusters](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeClusters.html) 
+  [ListClusters](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html) 
+  [UpdateCluster](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateCluster.html) 
+  [UpdateClusterSettings](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateClusterSettings.html) 

## Cluster capacity provider actions
<a name="OperationList-query-cluster-capacity-provider"></a>

The following APIs are available for cluster capacity providers:
+  [CreateCapacityProvider](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateCapacityProvider.html) 
+  [DeleteCapacityProvider](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteCapacityProvider.html) 
+  [DescribeCapacityProviders](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeCapacityProviders.html) 
+  [PutClusterCapacityProviders](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutClusterCapacityProviders.html) 
+  [UpdateCapacityProvider](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateCapacityProvider.html) 

## Container actions
<a name="OperationList-query-containers"></a>

The following APIs are available for containers:
+  [ExecuteCommand](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ExecuteCommand.html) 

## Container agent actions
<a name="OperationList-query-container-agent"></a>

The following APIs are available for container agents:
+  [UpdateContainerAgent](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateContainerAgent.html) 

## Container instance actions
<a name="OperationList-query-container-instance"></a>

The following APIs are available for container instances:
+  [DeregisterContainerInstance](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeregisterContainerInstance.html) 
+  [DescribeContainerInstances](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeContainerInstances.html) 
+  [DeleteAttributes](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteAttributes.html) 
+  [ListAttributes](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListAttributes.html) 
+  [ListContainerInstances](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListContainerInstances.html) 
+  [PutAttributes](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAttributes.html) 
+  [UpdateContainerInstancesState](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateContainerInstancesState.html) 

## Namespace actions
<a name="OperationList-query-namespace"></a>

**Note**  
Namespaces are an AWS Cloud Map resource. Namespaces are necessary in Amazon ECS to use the ECS Service Connect or ECS service discovery features. Amazon ECS requests namespaces from AWS Cloud Map and then displays your namespaces in the AWS Management Console. Use the AWS Cloud Map console or API for additional configuration options.

The following APIs are available for namespaces:
+  [CreateCluster](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateCluster.html) 

## Service actions
<a name="OperationList-query-services"></a>

The following APIs are available for services:
+  [CreateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html) 
+  [DeleteService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteService.html) 
+  [DescribeServices](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServices.html) 
+  [ListServices](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html) 
+  [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html) 

## Service deployment actions
<a name="OperationList-query-service-deployments"></a>

The following APIs are available for service deployments:
+  [DescribeServiceDeployments](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServiceDeployments.html) 
+  [ListServiceDeployments](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServiceDeployments.html) 
+  [StopServiceDeployment](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_StopServiceDeployment.html) 

## Service revision actions
<a name="OperationList-query-service-revisions"></a>

The following APIs are available for service revisions:
+  [DescribeServiceRevisions](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServiceRevisions.html) 

## Task definition actions
<a name="OperationList-query-task-definitions"></a>

The following APIs are available for task-definitions:
+  [DeleteTaskDefinitions](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteTaskDefinitions.html) 
+  [DeregisterTaskDefinition](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeregisterTaskDefinition.html) 
+  [DescribeTaskDefinition](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTaskDefinition.html) 
+  [ListTaskDefinitionFamilies](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListTaskDefinitionFamilies.html) 
+  [ListTaskDefinitions](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListTaskDefinitions.html) 
+  [RegisterTaskDefinition](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RegisterTaskDefinition.html) 

## Task actions
<a name="OperationList-query-tasks"></a>

The following APIs are available for tasks:
+  [DescribeTasks](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTasks.html) 
+  [GetTaskProtection](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_GetTaskProtection.html) 
+  [ListTasks](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListTasks.html) 
+  [RunTask](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html) 
+  [StartTask](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_StartTask.html) 
+  [StopTask](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_StopTask.html) 
+  [UpdateTaskProtection](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateTaskProtection.html) 

## Task set actions
<a name="OperationList-query-task-sets"></a>

The following APIs are available for task sets:
+  [CreateTaskSet](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateTaskSet.html) 
+  [DeleteTaskSet](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteTaskSet.html) 
+  [DescribeTaskSets](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTaskSets.html) 
+  [UpdateServicePrimaryTaskSet](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateServicePrimaryTaskSet.html) 
+  [UpdateTaskSet](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateTaskSet.html) 

## Tag actions
<a name="OperationList-query-tags"></a>

The following APIs are available for tags:
+  [ListTagsForResource](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListTagsForResource.html) 
+  [TagResource](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TagResource.html) 
+  [UntagResource](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UntagResource.html) 