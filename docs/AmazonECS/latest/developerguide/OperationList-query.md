# Actions by Amazon ECS resource

The following section lists the API actions by resource.

###### Topics

- [Account setting actions](#OperationList-query-account "#OperationList-query-account")
- [Cluster actions](#OperationList-query-cluster "#OperationList-query-cluster")
- [Cluster capacity provider actions](#OperationList-query-cluster-capacity-provider "#OperationList-query-cluster-capacity-provider")
- [Container actions](#OperationList-query-containers "#OperationList-query-containers")
- [Container agent actions](#OperationList-query-container-agent "#OperationList-query-container-agent")
- [Container instance actions](#OperationList-query-container-instance "#OperationList-query-container-instance")
- [Namespace actions](#OperationList-query-namespace "#OperationList-query-namespace")
- [Service actions](#OperationList-query-services "#OperationList-query-services")
- [Service deployment actions](#OperationList-query-service-deployments "#OperationList-query-service-deployments")
- [Service revision actions](#OperationList-query-service-revisions "#OperationList-query-service-revisions")
- [Task definition actions](#OperationList-query-task-definitions "#OperationList-query-task-definitions")
- [Task actions](#OperationList-query-tasks "#OperationList-query-tasks")
- [Task set actions](#OperationList-query-task-sets "#OperationList-query-task-sets")
- [Tag actions](#OperationList-query-tags "#OperationList-query-tags")

## Account setting actions

The following API actions are available for account settings:

- [DeleteAccountSetting](../APIReference/API_DeleteAccountSetting.md "../APIReference/API_DeleteAccountSetting.md")
- [ListAccountSettings](../APIReference/API_ListAccountSettings.md "../APIReference/API_ListAccountSettings.md")
- [PutAccountSetting](../APIReference/API_PutAccountSetting.md "../APIReference/API_PutAccountSetting.md")
- [PutAccountSettingDefault](../APIReference/API_PutAccountSettingDefault.md "../APIReference/API_PutAccountSettingDefault.md")

## Cluster actions

The following API actions are available for clusters:

- [CreateCluster](../APIReference/API_CreateCluster.md "../APIReference/API_CreateCluster.md")
- [DeleteCluster](../APIReference/API_DeleteCluster.md "../APIReference/API_DeleteCluster.md")
- [DescribeClusters](../APIReference/API_DescribeClusters.md "../APIReference/API_DescribeClusters.md")
- [ListClusters](../APIReference/API_ListClusters.md "../APIReference/API_ListClusters.md")
- [UpdateCluster](../APIReference/API_UpdateCluster.md "../APIReference/API_UpdateCluster.md")
- [UpdateClusterSettings](../APIReference/API_UpdateClusterSettings.md "../APIReference/API_UpdateClusterSettings.md")

## Cluster capacity provider actions

The following APIs are available for cluster capacity providers:

- [CreateCapacityProvider](../APIReference/API_CreateCapacityProvider.md "../APIReference/API_CreateCapacityProvider.md")
- [DeleteCapacityProvider](../APIReference/API_DeleteCapacityProvider.md "../APIReference/API_DeleteCapacityProvider.md")
- [DescribeCapacityProviders](../APIReference/API_DescribeCapacityProviders.md "../APIReference/API_DescribeCapacityProviders.md")
- [PutClusterCapacityProviders](../APIReference/API_PutClusterCapacityProviders.md "../APIReference/API_PutClusterCapacityProviders.md")
- [UpdateCapacityProvider](../APIReference/API_UpdateCapacityProvider.md "../APIReference/API_UpdateCapacityProvider.md")

## Container actions

The following APIs are available for containers:

- [ExecuteCommand](../APIReference/API_ExecuteCommand.md "../APIReference/API_ExecuteCommand.md")

## Container agent actions

The following APIs are available for container agents:

- [UpdateContainerAgent](../APIReference/API_UpdateContainerAgent.md "../APIReference/API_UpdateContainerAgent.md")

## Container instance actions

The following APIs are available for container instances:

- [DeregisterContainerInstance](../APIReference/API_DeregisterContainerInstance.md "../APIReference/API_DeregisterContainerInstance.md")
- [DescribeContainerInstances](../APIReference/API_DescribeContainerInstances.md "../APIReference/API_DescribeContainerInstances.md")
- [DeleteAttributes](../APIReference/API_DeleteAttributes.md "../APIReference/API_DeleteAttributes.md")
- [ListAttributes](../APIReference/API_ListAttributes.md "../APIReference/API_ListAttributes.md")
- [ListContainerInstances](../APIReference/API_ListContainerInstances.md "../APIReference/API_ListContainerInstances.md")
- [PutAttributes](../APIReference/API_PutAttributes.md "../APIReference/API_PutAttributes.md")
- [UpdateContainerInstancesState](../APIReference/API_UpdateContainerInstancesState.md "../APIReference/API_UpdateContainerInstancesState.md")

## Namespace actions

###### Note

Namespaces are an AWS Cloud Map resource. Namespaces are necessary in Amazon ECS to use
the ECS Service Connect or ECS service discovery features. Amazon ECS requests
namespaces from AWS Cloud Map and then displays your namespaces in the AWS Management Console. Use
the AWS Cloud Map console or API for additional configuration options.

The following APIs are available for namespaces:

- [CreateCluster](../APIReference/API_CreateCluster.md "../APIReference/API_CreateCluster.md")

## Service actions

The following APIs are available for services:

- [CreateService](../APIReference/API_CreateService.md "../APIReference/API_CreateService.md")
- [DeleteService](../APIReference/API_DeleteService.md "../APIReference/API_DeleteService.md")
- [DescribeServices](../APIReference/API_DescribeServices.md "../APIReference/API_DescribeServices.md")
- [ListServices](../APIReference/API_ListServices.md "../APIReference/API_ListServices.md")
- [UpdateService](../APIReference/API_UpdateService.md "../APIReference/API_UpdateService.md")

## Service deployment actions

The following APIs are available for service deployments:

- [DescribeServiceDeployments](../APIReference/API_DescribeServiceDeployments.md "../APIReference/API_DescribeServiceDeployments.md")
- [ListServiceDeployments](../APIReference/API_ListServiceDeployments.md "../APIReference/API_ListServiceDeployments.md")
- [StopServiceDeployment](../APIReference/API_StopServiceDeployment.md "../APIReference/API_StopServiceDeployment.md")

## Service revision actions

The following APIs are available for service revisions:

- [DescribeServiceRevisions](../APIReference/API_DescribeServiceRevisions.md "../APIReference/API_DescribeServiceRevisions.md")

## Task definition actions

The following APIs are available for task-definitions:

- [DeleteTaskDefinitions](../APIReference/API_DeleteTaskDefinitions.md "../APIReference/API_DeleteTaskDefinitions.md")
- [DeregisterTaskDefinition](../APIReference/API_DeregisterTaskDefinition.md "../APIReference/API_DeregisterTaskDefinition.md")
- [DescribeTaskDefinition](../APIReference/API_DescribeTaskDefinition.md "../APIReference/API_DescribeTaskDefinition.md")
- [ListTaskDefinitionFamilies](../APIReference/API_ListTaskDefinitionFamilies.md "../APIReference/API_ListTaskDefinitionFamilies.md")
- [ListTaskDefinitions](../APIReference/API_ListTaskDefinitions.md "../APIReference/API_ListTaskDefinitions.md")
- [RegisterTaskDefinition](../APIReference/API_RegisterTaskDefinition.md "../APIReference/API_RegisterTaskDefinition.md")

## Task actions

The following APIs are available for tasks:

- [DescribeTasks](../APIReference/API_DescribeTasks.md "../APIReference/API_DescribeTasks.md")
- [GetTaskProtection](../APIReference/API_GetTaskProtection.md "../APIReference/API_GetTaskProtection.md")
- [ListTasks](../APIReference/API_ListTasks.md "../APIReference/API_ListTasks.md")
- [RunTask](../APIReference/API_RunTask.md "../APIReference/API_RunTask.md")
- [StartTask](../APIReference/API_StartTask.md "../APIReference/API_StartTask.md")
- [StopTask](../APIReference/API_StopTask.md "../APIReference/API_StopTask.md")
- [UpdateTaskProtection](../APIReference/API_UpdateTaskProtection.md "../APIReference/API_UpdateTaskProtection.md")

## Task set actions

The following APIs are available for task sets:

- [CreateTaskSet](../APIReference/API_CreateTaskSet.md "../APIReference/API_CreateTaskSet.md")
- [DeleteTaskSet](../APIReference/API_DeleteTaskSet.md "../APIReference/API_DeleteTaskSet.md")
- [DescribeTaskSets](../APIReference/API_DescribeTaskSets.md "../APIReference/API_DescribeTaskSets.md")
- [UpdateServicePrimaryTaskSet](../APIReference/API_UpdateServicePrimaryTaskSet.md "../APIReference/API_UpdateServicePrimaryTaskSet.md")
- [UpdateTaskSet](../APIReference/API_UpdateTaskSet.md "../APIReference/API_UpdateTaskSet.md")

## Tag actions

The following APIs are available for tags:

- [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md")
- [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md")
- [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")
