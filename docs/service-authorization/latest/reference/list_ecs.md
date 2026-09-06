

# Actions, resources, and condition keys for Amazon Elastic Container Service
<a name="list_ecs"></a>

Amazon Elastic Container Service (service prefix: `ecs`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-iam-awsmanpol.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/ecs/ecs.json) for this service.

**Topics**
+ [API operations defined by Amazon Elastic Container Service](#list_ecs-operations)
+ [Actions defined by Amazon Elastic Container Service](#list_ecs-actions-as-permissions)
+ [Permission-only actions for Amazon Elastic Container Service](#list_ecs-permission-only-actions)
+ [Resource types defined by Amazon Elastic Container Service](#list_ecs-resources-for-iam-policies)
+ [Condition keys for Amazon Elastic Container Service](#list_ecs-policy-keys)

## API operations defined by Amazon Elastic Container Service
<a name="list_ecs-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_ecs-actions-as-permissions).




- **   ContinueServiceDeployment  **
  - **IAM action:**  [ecs:ContinueServiceDeployment](#list_ecs-action-ContinueServiceDeployment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateCapacityProvider  **
  - **IAM action:**  [ecs:CreateCapacityProvider](#list_ecs-action-CreateCapacityProvider)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ecs:PutClusterCapacityProviders](#list_ecs-action-PutClusterCapacityProviders)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ecs:TagResource](#list_ecs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ecs.amazonaws.com / **Access level:** Write

- **   CreateCluster  **
  - **IAM action:**  [ecs:CreateCluster](#list_ecs-action-CreateCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ecs:TagResource](#list_ecs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDaemon  **
  - **IAM action:**  [ecs:CreateDaemon](#list_ecs-action-CreateDaemon)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ecs:TagResource](#list_ecs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ecs-tasks.amazonaws.com / **Access level:** Write

- **   CreateExpressGatewayService  **
  - **IAM action:**  [ecs:CreateCluster](#list_ecs-action-CreateCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ecs:CreateExpressGatewayService](#list_ecs-action-CreateExpressGatewayService)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ecs:RegisterTaskDefinition](#list_ecs-action-RegisterTaskDefinition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ecs:TagResource](#list_ecs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ecs-tasks.amazonaws.com, ecs.amazonaws.com / **Access level:** Write

- **   CreateService  **
  - **IAM action:**  [ecs:CreateService](#list_ecs-action-CreateService)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ecs:TagResource](#list_ecs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ecs-tasks.amazonaws.com, ecs.amazonaws.com / **Access level:** Write

- **   CreateTaskSet  **
  - **IAM action:**  [ecs:CreateTaskSet](#list_ecs-action-CreateTaskSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ecs:TagResource](#list_ecs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ecs-tasks.amazonaws.com / **Access level:** Write

- **   DeleteAccountSetting  **
  - **IAM action:**  [ecs:DeleteAccountSetting](#list_ecs-action-DeleteAccountSetting) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAttributes  **
  - **IAM action:**  [ecs:DeleteAttributes](#list_ecs-action-DeleteAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCapacityProvider  **
  - **IAM action:**  [ecs:DeleteCapacityProvider](#list_ecs-action-DeleteCapacityProvider)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ecs:PutClusterCapacityProviders](#list_ecs-action-PutClusterCapacityProviders)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteCluster  **
  - **IAM action:**  [ecs:DeleteCluster](#list_ecs-action-DeleteCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDaemon  **
  - **IAM action:**  [ecs:DeleteDaemon](#list_ecs-action-DeleteDaemon) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDaemonTaskDefinition  **
  - **IAM action:**  [ecs:DeleteDaemonTaskDefinition](#list_ecs-action-DeleteDaemonTaskDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteExpressGatewayService  **
  - **IAM action:**  [ecs:DeleteExpressGatewayService](#list_ecs-action-DeleteExpressGatewayService) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteService  **
  - **IAM action:**  [ecs:DeleteService](#list_ecs-action-DeleteService) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTaskDefinitions  **
  - **IAM action:**  [ecs:DeleteTaskDefinitions](#list_ecs-action-DeleteTaskDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTaskSet  **
  - **IAM action:**  [ecs:DeleteTaskSet](#list_ecs-action-DeleteTaskSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterContainerInstance  **
  - **IAM action:**  [ecs:DeregisterContainerInstance](#list_ecs-action-DeregisterContainerInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterTaskDefinition  **
  - **IAM action:**  [ecs:DeregisterTaskDefinition](#list_ecs-action-DeregisterTaskDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeCapacityProviders  **
  - **IAM action:**  [ecs:DescribeCapacityProviders](#list_ecs-action-DescribeCapacityProviders) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeClusters  **
  - **IAM action:**  [ecs:DescribeClusters](#list_ecs-action-DescribeClusters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeContainerInstances  **
  - **IAM action:**  [ecs:DescribeContainerInstances](#list_ecs-action-DescribeContainerInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDaemon  **
  - **IAM action:**  [ecs:DescribeDaemon](#list_ecs-action-DescribeDaemon) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDaemonDeployments  **
  - **IAM action:**  [ecs:DescribeDaemonDeployments](#list_ecs-action-DescribeDaemonDeployments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDaemonRevisions  **
  - **IAM action:**  [ecs:DescribeDaemonRevisions](#list_ecs-action-DescribeDaemonRevisions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDaemonTaskDefinition  **
  - **IAM action:**  [ecs:DescribeDaemonTaskDefinition](#list_ecs-action-DescribeDaemonTaskDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeExpressGatewayService  **
  - **IAM action:**  [ecs:DescribeExpressGatewayService](#list_ecs-action-DescribeExpressGatewayService) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeServiceDeployments  **
  - **IAM action:**  [ecs:DescribeServiceDeployments](#list_ecs-action-DescribeServiceDeployments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeServiceRevisions  **
  - **IAM action:**  [ecs:DescribeServiceRevisions](#list_ecs-action-DescribeServiceRevisions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeServices  **
  - **IAM action:**  [ecs:DescribeServices](#list_ecs-action-DescribeServices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTaskDefinition  **
  - **IAM action:**  [ecs:DescribeTaskDefinition](#list_ecs-action-DescribeTaskDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTaskSets  **
  - **IAM action:**  [ecs:DescribeTaskSets](#list_ecs-action-DescribeTaskSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTasks  **
  - **IAM action:**  [ecs:DescribeTasks](#list_ecs-action-DescribeTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DiscoverPollEndpoint  **
  - **IAM action:**  [ecs:DiscoverPollEndpoint](#list_ecs-action-DiscoverPollEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ExecuteCommand  **
  - **IAM action:**  [ecs:ExecuteCommand](#list_ecs-action-ExecuteCommand) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetTaskProtection  **
  - **IAM action:**  [ecs:GetTaskProtection](#list_ecs-action-GetTaskProtection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAccountSettings  **
  - **IAM action:**  [ecs:ListAccountSettings](#list_ecs-action-ListAccountSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAttributes  **
  - **IAM action:**  [ecs:ListAttributes](#list_ecs-action-ListAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListClusters  **
  - **IAM action:**  [ecs:ListClusters](#list_ecs-action-ListClusters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListContainerInstances  **
  - **IAM action:**  [ecs:ListContainerInstances](#list_ecs-action-ListContainerInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDaemonDeployments  **
  - **IAM action:**  [ecs:ListDaemonDeployments](#list_ecs-action-ListDaemonDeployments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDaemonTaskDefinitions  **
  - **IAM action:**  [ecs:ListDaemonTaskDefinitions](#list_ecs-action-ListDaemonTaskDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDaemons  **
  - **IAM action:**  [ecs:ListDaemons](#list_ecs-action-ListDaemons) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServiceDeployments  **
  - **IAM action:**  [ecs:ListServiceDeployments](#list_ecs-action-ListServiceDeployments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServices  **
  - **IAM action:**  [ecs:ListServices](#list_ecs-action-ListServices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServicesByNamespace  **
  - **IAM action:**  [ecs:ListServicesByNamespace](#list_ecs-action-ListServicesByNamespace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [ecs:ListTagsForResource](#list_ecs-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTaskDefinitionFamilies  **
  - **IAM action:**  [ecs:ListTaskDefinitionFamilies](#list_ecs-action-ListTaskDefinitionFamilies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTaskDefinitions  **
  - **IAM action:**  [ecs:ListTaskDefinitions](#list_ecs-action-ListTaskDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTasks  **
  - **IAM action:**  [ecs:ListTasks](#list_ecs-action-ListTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutAccountSetting  **
  - **IAM action:**  [ecs:PutAccountSetting](#list_ecs-action-PutAccountSetting) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutAccountSettingDefault  **
  - **IAM action:**  [ecs:PutAccountSettingDefault](#list_ecs-action-PutAccountSettingDefault) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutAttributes  **
  - **IAM action:**  [ecs:PutAttributes](#list_ecs-action-PutAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutClusterCapacityProviders  **
  - **IAM action:**  [ecs:PutClusterCapacityProviders](#list_ecs-action-PutClusterCapacityProviders) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterContainerInstance  **
  - **IAM action:**  [ecs:RegisterContainerInstance](#list_ecs-action-RegisterContainerInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ecs:TagResource](#list_ecs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   RegisterDaemonTaskDefinition  **
  - **IAM action:**  [ecs:RegisterDaemonTaskDefinition](#list_ecs-action-RegisterDaemonTaskDefinition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ecs:TagResource](#list_ecs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ecs-tasks.amazonaws.com / **Access level:** Write

- **   RegisterTaskDefinition  **
  - **IAM action:**  [ecs:RegisterTaskDefinition](#list_ecs-action-RegisterTaskDefinition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ecs:TagResource](#list_ecs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ecs-tasks.amazonaws.com / **Access level:** Write

- **   RunTask  **
  - **IAM action:**  [ecs:RunTask](#list_ecs-action-RunTask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ecs:TagResource](#list_ecs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ecs-tasks.amazonaws.com, ecs.amazonaws.com / **Access level:** Write

- **   StartTask  **
  - **IAM action:**  [ecs:StartTask](#list_ecs-action-StartTask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ecs:TagResource](#list_ecs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ecs-tasks.amazonaws.com, ecs.amazonaws.com / **Access level:** Write

- **   StopServiceDeployment  **
  - **IAM action:**  [ecs:StopServiceDeployment](#list_ecs-action-StopServiceDeployment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopTask  **
  - **IAM action:**  [ecs:StopTask](#list_ecs-action-StopTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SubmitAttachmentStateChanges  **
  - **IAM action:**  [ecs:SubmitAttachmentStateChanges](#list_ecs-action-SubmitAttachmentStateChanges) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SubmitContainerStateChange  **
  - **IAM action:**  [ecs:SubmitContainerStateChange](#list_ecs-action-SubmitContainerStateChange) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SubmitTaskStateChange  **
  - **IAM action:**  [ecs:SubmitTaskStateChange](#list_ecs-action-SubmitTaskStateChange) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [ecs:TagResource](#list_ecs-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [ecs:UntagResource](#list_ecs-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateCapacityProvider  **
  - **IAM action:**  [ecs:PutClusterCapacityProviders](#list_ecs-action-PutClusterCapacityProviders)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ecs:UpdateCapacityProvider](#list_ecs-action-UpdateCapacityProvider)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ecs.amazonaws.com / **Access level:** Write

- **   UpdateCluster  **
  - **IAM action:**  [ecs:UpdateCluster](#list_ecs-action-UpdateCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateClusterSettings  **
  - **IAM action:**  [ecs:UpdateClusterSettings](#list_ecs-action-UpdateClusterSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateContainerAgent  **
  - **IAM action:**  [ecs:UpdateContainerAgent](#list_ecs-action-UpdateContainerAgent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateContainerInstancesState  **
  - **IAM action:**  [ecs:UpdateContainerInstancesState](#list_ecs-action-UpdateContainerInstancesState) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDaemon  **
  - **IAM action:**  [ecs:UpdateDaemon](#list_ecs-action-UpdateDaemon)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ecs-tasks.amazonaws.com / **Access level:** Write

- **   UpdateExpressGatewayService  **
  - **IAM action:**  [ecs:RegisterTaskDefinition](#list_ecs-action-RegisterTaskDefinition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ecs:UpdateExpressGatewayService](#list_ecs-action-UpdateExpressGatewayService)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ecs-tasks.amazonaws.com, ecs.amazonaws.com / **Access level:** Write

- **   UpdateService  **
  - **IAM action:**  [ecs:UpdateService](#list_ecs-action-UpdateService)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ecs-tasks.amazonaws.com, ecs.amazonaws.com / **Access level:** Write

- **   UpdateServicePrimaryTaskSet  **
  - **IAM action:**  [ecs:UpdateServicePrimaryTaskSet](#list_ecs-action-UpdateServicePrimaryTaskSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTaskProtection  **
  - **IAM action:**  [ecs:UpdateTaskProtection](#list_ecs-action-UpdateTaskProtection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTaskSet  **
  - **IAM action:**  [ecs:UpdateTaskSet](#list_ecs-action-UpdateTaskSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Elastic Container Service
<a name="list_ecs-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [ContinueServiceDeployment](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContinueServiceDeployment.html)  **
  - **Description:** Grants permission to continue a paused service deployment
  - **Resource types (\*required):** [service\*](#list_ecs-resource-service) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Resource types (\*required):** [service-deployment\*](#list_ecs-resource-service-deployment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:service](#list_ecs-ecs_service)
  - **Access level:** Write

- **   [CreateCapacityProvider](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateCapacityProvider.html)  **
  - **Description:** Grants permission to create a new capacity provider. Capacity providers are associated with an Amazon ECS cluster and are used in capacity provider strategies to facilitate cluster auto scaling
  - **Resource types (\*required):** [capacity-provider\*](#list_ecs-resource-capacity-provider)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ecs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecs-aws_TagKeys)<br />[ecs:instance-metadata-tags-propagation](#list_ecs-ecs_instance-metadata-tags-propagation)<br />[ecs:propagate-tags](#list_ecs-ecs_propagate-tags)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateCluster](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateCluster.html)  **
  - **Description:** Grants permission to create a new Amazon ECS cluster
  - **Resource types (\*required):** [cluster\*](#list_ecs-resource-cluster)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ecs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecs-aws_TagKeys)<br />[ecs:capacity-provider](#list_ecs-ecs_capacity-provider)<br />[ecs:fargate-ephemeral-storage-kms-key](#list_ecs-ecs_fargate-ephemeral-storage-kms-key)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDaemon](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateDaemon.html)  **
  - **Description:** Grants permission to create a new daemon in a specified cluster
  - **Resource types (\*required):** [daemon\*](#list_ecs-resource-daemon)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ecs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecs-aws_TagKeys)<br />[ecs:capacity-provider](#list_ecs-ecs_capacity-provider)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:daemon-task-definition](#list_ecs-ecs_daemon-task-definition)<br />[ecs:enable-ecs-managed-tags](#list_ecs-ecs_enable-ecs-managed-tags)<br />[ecs:enable-execute-command](#list_ecs-ecs_enable-execute-command)<br />[ecs:propagate-tags](#list_ecs-ecs_propagate-tags)<br />[ecs:task-cpu](#list_ecs-ecs_task-cpu)<br />[ecs:task-memory](#list_ecs-ecs_task-memory)
  - **Access level:** Write

- **   [CreateExpressGatewayService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateExpressGatewayService.html)  **
  - **Description:** Grants permission to create a new Amazon ECS Express Gateway service with cluster and task definition
  - **Resource types (\*required):** [service\*](#list_ecs-resource-service)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ecs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecs-aws_TagKeys)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:enable-ecs-managed-tags](#list_ecs-ecs_enable-ecs-managed-tags)<br />[ecs:propagate-tags](#list_ecs-ecs_propagate-tags)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)<br />[ecs:subnet](#list_ecs-ecs_subnet)<br />[ecs:task-cpu](#list_ecs-ecs_task-cpu)<br />[ecs:task-definition](#list_ecs-ecs_task-definition)<br />[ecs:task-memory](#list_ecs-ecs_task-memory)
  - **Access level:** Write

- **   [CreateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html)  **
  - **Description:** Grants permission to run and maintain a desired number of tasks from a specified task definition via service creation
  - **Resource types (\*required):** [service\*](#list_ecs-resource-service)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ecs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecs-aws_TagKeys)<br />[ecs:auto-assign-public-ip](#list_ecs-ecs_auto-assign-public-ip)<br />[ecs:capacity-provider](#list_ecs-ecs_capacity-provider)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:enable-ebs-volumes](#list_ecs-ecs_enable-ebs-volumes)<br />[ecs:enable-ecs-managed-tags](#list_ecs-ecs_enable-ecs-managed-tags)<br />[ecs:enable-execute-command](#list_ecs-ecs_enable-execute-command)<br />[ecs:enable-service-connect](#list_ecs-ecs_enable-service-connect)<br />[ecs:enable-vpc-lattice](#list_ecs-ecs_enable-vpc-lattice)<br />[ecs:namespace](#list_ecs-ecs_namespace)<br />[ecs:propagate-tags](#list_ecs-ecs_propagate-tags)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)<br />[ecs:subnet](#list_ecs-ecs_subnet)<br />[ecs:task-cpu](#list_ecs-ecs_task-cpu)<br />[ecs:task-definition](#list_ecs-ecs_task-definition)<br />[ecs:task-memory](#list_ecs-ecs_task-memory)
  - **Access level:** Write

- **   [CreateTaskSet](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateTaskSet.html)  **
  - **Description:** Grants permission to create a new Amazon ECS task set
  - **Resource types (\*required):** [task-set\*](#list_ecs-resource-task-set)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ecs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecs-aws_TagKeys)<br />[ecs:capacity-provider](#list_ecs-ecs_capacity-provider)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)<br />[ecs:service](#list_ecs-ecs_service)<br />[ecs:task-definition](#list_ecs-ecs_task-definition)
  - **Access level:** Write

- **   [DeleteAccountSetting](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteAccountSetting.html)  **
  - **Description:** Grants permission to modify the ARN and resource ID format of a resource for a specified IAM user, IAM role, or the root user for an account. You can specify whether the new ARN and resource ID format are disabled for new resources that are created
  - **Resource types (\*required):** 
  - **Condition keys:** [ecs:account-setting](#list_ecs-ecs_account-setting)
  - **Access level:** Write

- **   [DeleteAttributes](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteAttributes.html)  **
  - **Description:** Grants permission to delete one or more custom attributes from an Amazon ECS resource
  - **Resource types (\*required):** [container-instance\*](#list_ecs-resource-container-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCapacityProvider](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteCapacityProvider.html)  **
  - **Description:** Grants permission to delete the specified capacity provider
  - **Resource types (\*required):** [capacity-provider\*](#list_ecs-resource-capacity-provider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCluster](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteCluster.html)  **
  - **Description:** Grants permission to delete the specified cluster
  - **Resource types (\*required):** [cluster\*](#list_ecs-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDaemon](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteDaemon.html)  **
  - **Description:** Grants permission to delete a specified daemon within a cluster
  - **Resource types (\*required):** [daemon\*](#list_ecs-resource-daemon)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)
  - **Access level:** Write

- **   [DeleteDaemonTaskDefinition](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteDaemonTaskDefinition.html)  **
  - **Description:** Grants permission to delete the specified daemon task definition
  - **Resource types (\*required):** [daemon-task-definition\*](#list_ecs-resource-daemon-task-definition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteExpressGatewayService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteExpressGatewayService.html)  **
  - **Description:** Grants permission to delete a specified Express Gateway service
  - **Resource types (\*required):** [service\*](#list_ecs-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteService.html)  **
  - **Description:** Grants permission to delete a specified service within a cluster
  - **Resource types (\*required):** [service\*](#list_ecs-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTaskDefinitions](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteTaskDefinitions.html)  **
  - **Description:** Grants permission to delete the specified task definitions by family and revision
  - **Resource types (\*required):** [task-definition\*](#list_ecs-resource-task-definition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTaskSet](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteTaskSet.html)  **
  - **Description:** Grants permission to delete the specified task set
  - **Resource types (\*required):** [task-set\*](#list_ecs-resource-task-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)<br />[ecs:service](#list_ecs-ecs_service)
  - **Access level:** Write

- **   [DeregisterContainerInstance](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeregisterContainerInstance.html)  **
  - **Description:** Grants permission to deregister an Amazon ECS container instance from the specified cluster
  - **Resource types (\*required):** [cluster\*](#list_ecs-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterTaskDefinition](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeregisterTaskDefinition.html)  **
  - **Description:** Grants permission to deregister the specified task definition by family and revision
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeCapacityProviders](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeCapacityProviders.html)  **
  - **Description:** Grants permission to describe one or more Amazon ECS capacity providers
  - **Resource types (\*required):** [capacity-provider\*](#list_ecs-resource-capacity-provider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeClusters](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeClusters.html)  **
  - **Description:** Grants permission to describes one or more of your clusters
  - **Resource types (\*required):** [cluster\*](#list_ecs-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeContainerInstances](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeContainerInstances.html)  **
  - **Description:** Grants permission to describes Amazon ECS container instances
  - **Resource types (\*required):** [container-instance\*](#list_ecs-resource-container-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDaemon](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeDaemon.html)  **
  - **Description:** Grants permission to describe the specified daemon running in your cluster
  - **Resource types (\*required):** [daemon\*](#list_ecs-resource-daemon)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)
  - **Access level:** Read

- **   [DescribeDaemonDeployments](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeDaemonDeployments.html)  **
  - **Description:** Grants permission to describe one or more of your daemon deployments
  - **Resource types (\*required):** [daemon\*](#list_ecs-resource-daemon) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)
  - **Resource types (\*required):** [daemon-deployment\*](#list_ecs-resource-daemon-deployment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:daemon](#list_ecs-ecs_daemon)
  - **Access level:** Read

- **   [DescribeDaemonRevisions](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeDaemonRevisions.html)  **
  - **Description:** Grants permission to describe one or more of your daemon revisions
  - **Resource types (\*required):** [daemon\*](#list_ecs-resource-daemon) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)
  - **Resource types (\*required):** [daemon-revision\*](#list_ecs-resource-daemon-revision) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:daemon](#list_ecs-ecs_daemon)
  - **Access level:** Read

- **   [DescribeDaemonTaskDefinition](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeDaemonTaskDefinition.html)  **
  - **Description:** Grants permission to describe a daemon task definition
  - **Resource types (\*required):** [daemon-task-definition\*](#list_ecs-resource-daemon-task-definition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeExpressGatewayService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeExpressGatewayService.html)  **
  - **Description:** Grants permission to describe the specified Express Gateway service
  - **Resource types (\*required):** [service\*](#list_ecs-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeServiceDeployments](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServiceDeployments.html)  **
  - **Description:** Grants permission to describe one or more of your service deployments
  - **Resource types (\*required):** [service\*](#list_ecs-resource-service) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Resource types (\*required):** [service-deployment\*](#list_ecs-resource-service-deployment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:service](#list_ecs-ecs_service)
  - **Access level:** Read

- **   [DescribeServiceRevisions](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServiceRevisions.html)  **
  - **Description:** Grants permission to describe one or more of your service revisions
  - **Resource types (\*required):** [service\*](#list_ecs-resource-service) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Resource types (\*required):** [service-revision\*](#list_ecs-resource-service-revision) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:service](#list_ecs-ecs_service)
  - **Access level:** Read

- **   [DescribeServices](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServices.html)  **
  - **Description:** Grants permission to describe the specified services running in your cluster
  - **Resource types (\*required):** [service\*](#list_ecs-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTaskDefinition](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTaskDefinition.html)  **
  - **Description:** Grants permission to describe a task definition. You can specify a family and revision to find information about a specific task definition, or you can simply specify the family to find the latest ACTIVE revision in that family
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeTaskSets](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTaskSets.html)  **
  - **Description:** Grants permission to describe Amazon ECS task sets
  - **Resource types (\*required):** [task-set\*](#list_ecs-resource-task-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)<br />[ecs:service](#list_ecs-ecs_service)
  - **Access level:** Read

- **   [DescribeTasks](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTasks.html)  **
  - **Description:** Grants permission to describe a specified task or tasks
  - **Resource types (\*required):** [task\*](#list_ecs-resource-task)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DiscoverPollEndpoint](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DiscoverPollEndpoint.html)  **
  - **Description:** Grants permission to get an endpoint for the Amazon ECS agent to poll for updates
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ExecuteCommand](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ExecuteCommand.html)  **
  - **Description:** Grants permission to run a command remotely on an Amazon ECS container
  - **Resource types (\*required):** [cluster\*](#list_ecs-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:container-name](#list_ecs-ecs_container-name)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)<br />[ecs:task](#list_ecs-ecs_task)
  - **Resource types (\*required):** [task\*](#list_ecs-resource-task) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:container-name](#list_ecs-ecs_container-name)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)<br />[ecs:task](#list_ecs-ecs_task)
  - **Access level:** Write

- **   [GetTaskProtection](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_GetTaskProtection.html)  **
  - **Description:** Grants permission to retrieve the protection status of tasks in an Amazon ECS service
  - **Resource types (\*required):** [task\*](#list_ecs-resource-task)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAccountSettings](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListAccountSettings.html)  **
  - **Description:** Grants permission to list the account settings for an Amazon ECS resource for a specified principal
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListAttributes](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListAttributes.html)  **
  - **Description:** Grants permission to lists the attributes for Amazon ECS resources within a specified target type and cluster
  - **Resource types (\*required):** [cluster\*](#list_ecs-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListClusters](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html)  **
  - **Description:** Grants permission to get a list of existing clusters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListContainerInstances](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListContainerInstances.html)  **
  - **Description:** Grants permission to get a list of container instances in a specified cluster
  - **Resource types (\*required):** [cluster\*](#list_ecs-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDaemonDeployments](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListDaemonDeployments.html)  **
  - **Description:** Grants permission to get a list of daemon deployments for a specified daemon
  - **Resource types (\*required):** [daemon\*](#list_ecs-resource-daemon)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)
  - **Access level:** List

- **   [ListDaemonTaskDefinitions](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListDaemonTaskDefinitions.html)  **
  - **Description:** Grants permission to get a list of daemon task definitions that are registered to your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDaemons](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListDaemons.html)  **
  - **Description:** Grants permission to get a list of daemons that are running in a specified cluster
  - **Resource types (\*required):** 
  - **Condition keys:** [ecs:cluster](#list_ecs-ecs_cluster)
  - **Access level:** List

- **   [ListServiceDeployments](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServiceDeployments.html)  **
  - **Description:** Grants permission to get a list of service deployments for a specified service
  - **Resource types (\*required):** [service\*](#list_ecs-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListServices](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html)  **
  - **Description:** Grants permission to get a list of services that are running in a specified cluster
  - **Resource types (\*required):** 
  - **Condition keys:** [ecs:cluster](#list_ecs-ecs_cluster)
  - **Access level:** List

- **   [ListServicesByNamespace](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServicesByNamespace.html)  **
  - **Description:** Grants permission to get a list of services that are running in a specified AWS Cloud Map Namespace
  - **Resource types (\*required):** 
  - **Condition keys:** [ecs:namespace](#list_ecs-ecs_namespace)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to get a list of tags for the specified resource
  - **Resource types (\*required):** [capacity-provider](#list_ecs-resource-capacity-provider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cluster](#list_ecs-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Resource types (\*required):** [container-instance](#list_ecs-resource-container-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Resource types (\*required):** [service](#list_ecs-resource-service) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Resource types (\*required):** [task](#list_ecs-resource-task) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Resource types (\*required):** [task-definition](#list_ecs-resource-task-definition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Resource types (\*required):** [task-set](#list_ecs-resource-task-set) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTaskDefinitionFamilies](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListTaskDefinitionFamilies.html)  **
  - **Description:** Grants permission to get a list of task definition families that are registered to your account (which may include task definition families that no longer have any ACTIVE task definitions)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTaskDefinitions](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListTaskDefinitions.html)  **
  - **Description:** Grants permission to get a list of task definitions that are registered to your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTasks](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListTasks.html)  **
  - **Description:** Grants permission to get a list of tasks for a specified cluster
  - **Resource types (\*required):** [container-instance\*](#list_ecs-resource-container-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** List

- **   [PutAccountSetting](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAccountSetting.html)  **
  - **Description:** Grants permission to modify the ARN and resource ID format of a resource for a specified IAM user, IAM role, or the root user for an account. You can specify whether the new ARN and resource ID format are enabled for new resources that are created. Enabling this setting is required to use new Amazon ECS features such as resource tagging
  - **Resource types (\*required):** 
  - **Condition keys:** [ecs:account-setting](#list_ecs-ecs_account-setting)
  - **Access level:** Write

- **   [PutAccountSettingDefault](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAccountSettingDefault.html)  **
  - **Description:** Grants permission to modify the ARN and resource ID format of a resource type for all IAM users on an account for which no individual account setting has been set. Enabling this setting is required to use new Amazon ECS features such as resource tagging
  - **Resource types (\*required):** 
  - **Condition keys:** [ecs:account-setting](#list_ecs-ecs_account-setting)
  - **Access level:** Write

- **   [PutAttributes](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAttributes.html)  **
  - **Description:** Grants permission to create or update an attribute on an Amazon ECS resource
  - **Resource types (\*required):** [container-instance\*](#list_ecs-resource-container-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutClusterCapacityProviders](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutClusterCapacityProviders.html)  **
  - **Description:** Grants permission to modify the available capacity providers and the default capacity provider strategy for a cluster
  - **Resource types (\*required):** [cluster\*](#list_ecs-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:capacity-provider](#list_ecs-ecs_capacity-provider)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RegisterContainerInstance](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RegisterContainerInstance.html)  **
  - **Description:** Grants permission to register an EC2 instance into the specified cluster
  - **Resource types (\*required):** [cluster\*](#list_ecs-resource-cluster)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ecs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecs-aws_TagKeys)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RegisterDaemonTaskDefinition](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RegisterDaemonTaskDefinition.html)  **
  - **Description:** Grants permission to register a new daemon task definition from the supplied family and containerDefinitions
  - **Resource types (\*required):** [daemon-task-definition\*](#list_ecs-resource-daemon-task-definition)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ecs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecs-aws_TagKeys)<br />[ecs:privileged](#list_ecs-ecs_privileged)<br />[ecs:task-cpu](#list_ecs-ecs_task-cpu)<br />[ecs:task-memory](#list_ecs-ecs_task-memory)
  - **Access level:** Write

- **   [RegisterTaskDefinition](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RegisterTaskDefinition.html)  **
  - **Description:** Grants permission to register a new task definition from the supplied family and containerDefinitions
  - **Resource types (\*required):** [task-definition\*](#list_ecs-resource-task-definition)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ecs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecs-aws_TagKeys)<br />[ecs:compute-compatibility](#list_ecs-ecs_compute-compatibility)<br />[ecs:privileged](#list_ecs-ecs_privileged)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)<br />[ecs:task-cpu](#list_ecs-ecs_task-cpu)<br />[ecs:task-memory](#list_ecs-ecs_task-memory)
  - **Access level:** Write

- **   [RunTask](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html)  **
  - **Description:** Grants permission to start a task using random placement and the default Amazon ECS scheduler
  - **Resource types (\*required):** [task-definition\*](#list_ecs-resource-task-definition)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ecs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecs-aws_TagKeys)<br />[ecs:capacity-provider](#list_ecs-ecs_capacity-provider)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:enable-ebs-volumes](#list_ecs-ecs_enable-ebs-volumes)<br />[ecs:enable-execute-command](#list_ecs-ecs_enable-execute-command)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartTask](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_StartTask.html)  **
  - **Description:** Grants permission to start a new task from the specified task definition on the specified container instance or instances
  - **Resource types (\*required):** [task-definition\*](#list_ecs-resource-task-definition)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ecs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecs-aws_TagKeys)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:container-instances](#list_ecs-ecs_container-instances)<br />[ecs:enable-ebs-volumes](#list_ecs-ecs_enable-ebs-volumes)<br />[ecs:enable-execute-command](#list_ecs-ecs_enable-execute-command)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopServiceDeployment](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_StopServiceDeployment.html)  **
  - **Description:** Grants permission to stop an ongoing service deployment
  - **Resource types (\*required):** [service\*](#list_ecs-resource-service) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Resource types (\*required):** [service-deployment\*](#list_ecs-resource-service-deployment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:service](#list_ecs-ecs_service)
  - **Access level:** Write

- **   [StopTask](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_StopTask.html)  **
  - **Description:** Grants permission to stop a running task
  - **Resource types (\*required):** [task\*](#list_ecs-resource-task)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SubmitAttachmentStateChanges](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_SubmitAttachmentStateChanges.html)  **
  - **Description:** Grants permission to send an acknowledgement that attachments changed states
  - **Resource types (\*required):** [cluster\*](#list_ecs-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SubmitContainerStateChange](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_SubmitContainerStateChange.html)  **
  - **Description:** Grants permission to send an acknowledgement that a container changed states
  - **Resource types (\*required):** [cluster\*](#list_ecs-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SubmitTaskStateChange](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_SubmitTaskStateChange.html)  **
  - **Description:** Grants permission to send an acknowledgement that a task changed states
  - **Resource types (\*required):** [cluster\*](#list_ecs-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag the specified resource
  - **Resource types (\*required):** [capacity-provider](#list_ecs-resource-capacity-provider) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ecs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecs-aws_TagKeys)<br />[ecs:CreateAction](#list_ecs-ecs_CreateAction)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cluster](#list_ecs-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ecs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecs-aws_TagKeys)<br />[ecs:CreateAction](#list_ecs-ecs_CreateAction)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Resource types (\*required):** [container-instance](#list_ecs-resource-container-instance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ecs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecs-aws_TagKeys)<br />[ecs:CreateAction](#list_ecs-ecs_CreateAction)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Resource types (\*required):** [daemon](#list_ecs-resource-daemon) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ecs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecs-aws_TagKeys)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:CreateAction](#list_ecs-ecs_CreateAction)
  - **Resource types (\*required):** [daemon-task-definition](#list_ecs-resource-daemon-task-definition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ecs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecs-aws_TagKeys)<br />[ecs:CreateAction](#list_ecs-ecs_CreateAction)
  - **Resource types (\*required):** [service](#list_ecs-resource-service) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ecs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecs-aws_TagKeys)<br />[ecs:CreateAction](#list_ecs-ecs_CreateAction)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Resource types (\*required):** [task](#list_ecs-resource-task) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ecs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecs-aws_TagKeys)<br />[ecs:CreateAction](#list_ecs-ecs_CreateAction)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Resource types (\*required):** [task-definition](#list_ecs-resource-task-definition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ecs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecs-aws_TagKeys)<br />[ecs:CreateAction](#list_ecs-ecs_CreateAction)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Resource types (\*required):** [task-set](#list_ecs-resource-task-set) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ecs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecs-aws_TagKeys)<br />[ecs:CreateAction](#list_ecs-ecs_CreateAction)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag the specified resource
  - **Resource types (\*required):** [capacity-provider](#list_ecs-resource-capacity-provider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecs-aws_TagKeys)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cluster](#list_ecs-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecs-aws_TagKeys)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Resource types (\*required):** [container-instance](#list_ecs-resource-container-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecs-aws_TagKeys)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Resource types (\*required):** [daemon](#list_ecs-resource-daemon) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecs-aws_TagKeys)<br />[ecs:cluster](#list_ecs-ecs_cluster)
  - **Resource types (\*required):** [daemon-task-definition](#list_ecs-resource-daemon-task-definition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecs-aws_TagKeys)
  - **Resource types (\*required):** [service](#list_ecs-resource-service) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecs-aws_TagKeys)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Resource types (\*required):** [task](#list_ecs-resource-task) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecs-aws_TagKeys)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Resource types (\*required):** [task-definition](#list_ecs-resource-task-definition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecs-aws_TagKeys)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Resource types (\*required):** [task-set](#list_ecs-resource-task-set) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ecs-aws_TagKeys)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Tagging, Write

- **   [UpdateCapacityProvider](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateCapacityProvider.html)  **
  - **Description:** Grants permission to update the specified capacity provider
  - **Resource types (\*required):** [capacity-provider\*](#list_ecs-resource-capacity-provider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:instance-metadata-tags-propagation](#list_ecs-ecs_instance-metadata-tags-propagation)<br />[ecs:propagate-tags](#list_ecs-ecs_propagate-tags)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCluster](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateCluster.html)  **
  - **Description:** Grants permission to modify the configuration or settings to use for a cluster
  - **Resource types (\*required):** [cluster\*](#list_ecs-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:fargate-ephemeral-storage-kms-key](#list_ecs-ecs_fargate-ephemeral-storage-kms-key)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateClusterSettings](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateClusterSettings.html)  **
  - **Description:** Grants permission to modify the settings to use for a cluster
  - **Resource types (\*required):** [cluster\*](#list_ecs-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateContainerAgent](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateContainerAgent.html)  **
  - **Description:** Grants permission to update the Amazon ECS container agent on a specified container instance
  - **Resource types (\*required):** [container-instance\*](#list_ecs-resource-container-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateContainerInstancesState](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateContainerInstancesState.html)  **
  - **Description:** Grants permission to the user to modify the status of an Amazon ECS container instance
  - **Resource types (\*required):** [container-instance\*](#list_ecs-resource-container-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDaemon](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateDaemon.html)  **
  - **Description:** Grants permission to modify the parameters of a daemon
  - **Resource types (\*required):** [daemon\*](#list_ecs-resource-daemon)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:capacity-provider](#list_ecs-ecs_capacity-provider)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:daemon-task-definition](#list_ecs-ecs_daemon-task-definition)<br />[ecs:enable-ecs-managed-tags](#list_ecs-ecs_enable-ecs-managed-tags)<br />[ecs:enable-execute-command](#list_ecs-ecs_enable-execute-command)<br />[ecs:propagate-tags](#list_ecs-ecs_propagate-tags)<br />[ecs:task-cpu](#list_ecs-ecs_task-cpu)<br />[ecs:task-memory](#list_ecs-ecs_task-memory)
  - **Access level:** Write

- **   [UpdateExpressGatewayService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateExpressGatewayService.html)  **
  - **Description:** Grants permission to modify the parameters of an Express Gateway service
  - **Resource types (\*required):** [service\*](#list_ecs-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:enable-ecs-managed-tags](#list_ecs-ecs_enable-ecs-managed-tags)<br />[ecs:propagate-tags](#list_ecs-ecs_propagate-tags)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)<br />[ecs:subnet](#list_ecs-ecs_subnet)<br />[ecs:task-cpu](#list_ecs-ecs_task-cpu)<br />[ecs:task-definition](#list_ecs-ecs_task-definition)<br />[ecs:task-memory](#list_ecs-ecs_task-memory)
  - **Access level:** Write

- **   [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html)  **
  - **Description:** Grants permission to modify the parameters of a service
  - **Resource types (\*required):** [service\*](#list_ecs-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:auto-assign-public-ip](#list_ecs-ecs_auto-assign-public-ip)<br />[ecs:capacity-provider](#list_ecs-ecs_capacity-provider)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:enable-ebs-volumes](#list_ecs-ecs_enable-ebs-volumes)<br />[ecs:enable-ecs-managed-tags](#list_ecs-ecs_enable-ecs-managed-tags)<br />[ecs:enable-execute-command](#list_ecs-ecs_enable-execute-command)<br />[ecs:enable-service-connect](#list_ecs-ecs_enable-service-connect)<br />[ecs:enable-vpc-lattice](#list_ecs-ecs_enable-vpc-lattice)<br />[ecs:namespace](#list_ecs-ecs_namespace)<br />[ecs:propagate-tags](#list_ecs-ecs_propagate-tags)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)<br />[ecs:subnet](#list_ecs-ecs_subnet)<br />[ecs:task-cpu](#list_ecs-ecs_task-cpu)<br />[ecs:task-definition](#list_ecs-ecs_task-definition)<br />[ecs:task-memory](#list_ecs-ecs_task-memory)
  - **Access level:** Write

- **   [UpdateServicePrimaryTaskSet](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateServicePrimaryTaskSet.html)  **
  - **Description:** Grants permission to modify the primary task set used in a service
  - **Resource types (\*required):** [service\*](#list_ecs-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTaskProtection](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateTaskProtection.html)  **
  - **Description:** Grants permission to modify the protection status of a task
  - **Resource types (\*required):** [task\*](#list_ecs-resource-task)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTaskSet](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateTaskSet.html)  **
  - **Description:** Grants permission to update the specified task set
  - **Resource types (\*required):** [task-set\*](#list_ecs-resource-task-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)<br />[ecs:service](#list_ecs-ecs_service)
  - **Access level:** Write



## Permission-only actions for Amazon Elastic Container Service
<a name="list_ecs-permission-only-actions"></a>

The following actions are defined by Amazon Elastic Container Service but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AllowVendedLogDeliveryForResource](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/action-logs-getting-started.html)  **
  - **Description:** Grants permission to allow vended log delivery for a specified resource
  - **Resource types (\*required):** [cluster](#list_ecs-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [Poll](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/instance_IAM_role.html)  **
  - **Description:** Grants permission to an agent to connect with the Amazon ECS service to report status and get commands
  - **Resource types (\*required):** [container-instance\*](#list_ecs-resource-container-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutSystemLogEvents](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/logging-using-cloudtrail.html#cloudtrail-data-events)  **
  - **Description:** Grants permission to collect system logs from the container instances
  - **Resource types (\*required):** [cluster\*](#list_ecs-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Resource types (\*required):** [container-instance\*](#list_ecs-resource-container-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:capacity-provider](#list_ecs-ecs_capacity-provider)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartTelemetrySession](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-metrics.html#enable_cloudwatch)  **
  - **Description:** Grants permission to start a telemetry session
  - **Resource types (\*required):** [container-instance\*](#list_ecs-resource-container-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Elastic Container Service
<a name="list_ecs-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [capacity-provider](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-capacity-provider-console-v2.html)  | arn:${Partition}:ecs:${Region}:${Account}:capacity-provider/${CapacityProviderName} | [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_) | 
|  [cluster](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/clusters.html)  | arn:${Partition}:ecs:${Region}:${Account}:cluster/${ClusterName} | [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_) | 
|  [container-instance](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-capacity.html)  | arn:${Partition}:ecs:${Region}:${Account}:container-instance/${ClusterName}/${ContainerInstanceId} | [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_) | 
|  [daemon](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_daemons.html)  | arn:${Partition}:ecs:${Region}:${Account}:daemon/${ClusterName}/${DaemonName} | [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster) | 
|  [daemon-deployment](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/daemon-deployment.html)  | arn:${Partition}:ecs:${Region}:${Account}:daemon-deployment/${ClusterName}/${DaemonName}/${DaemonDeploymentId} | [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:daemon](#list_ecs-ecs_daemon) | 
|  [daemon-revision](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/daemon-revision.html)  | arn:${Partition}:ecs:${Region}:${Account}:daemon-revision/${ClusterName}/${DaemonName}/${DaemonRevisionId} | [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:daemon](#list_ecs-ecs_daemon) | 
|  [daemon-task-definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/daemon-task-definitions.html)  | arn:${Partition}:ecs:${Region}:${Account}:daemon-task-definition/${DaemonTaskDefinitionFamilyName}:${DaemonTaskDefinitionRevisionNumber} | [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_) | 
|  [service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html)  | arn:${Partition}:ecs:${Region}:${Account}:service/${ClusterName}/${ServiceName} | [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_) | 
|  [service-deployment](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-deployment.html)  | arn:${Partition}:ecs:${Region}:${Account}:service-deployment/${ClusterName}/${ServiceName}/${ServiceDeploymentId} | [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:service](#list_ecs-ecs_service) | 
|  [service-revision](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-revision.html)  | arn:${Partition}:ecs:${Region}:${Account}:service-revision/${ClusterName}/${ServiceName}/${ServiceRevisionId} | [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:cluster](#list_ecs-ecs_cluster)<br />[ecs:service](#list_ecs-ecs_service) | 
|  [task](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html)  | arn:${Partition}:ecs:${Region}:${Account}:task/${ClusterName}/${TaskId} | [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_) | 
|  [task-definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html)  | arn:${Partition}:ecs:${Region}:${Account}:task-definition/${TaskDefinitionFamilyName}:${TaskDefinitionRevisionNumber} | [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_) | 
|  [task-set](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-external.html)  | arn:${Partition}:ecs:${Region}:${Account}:task-set/${ClusterName}/${ServiceName}/${TaskSetId} | [aws:ResourceTag/${TagKey}](#list_ecs-aws_ResourceTag___TagKey_)<br />[ecs:ResourceTag/${TagKey}](#list_ecs-ecs_ResourceTag___TagKey_) | 

## Condition keys for Amazon Elastic Container Service
<a name="list_ecs-policy-keys"></a>

Amazon Elastic Container Service defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [ecs:CreateAction](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-createaction)  | Filters access by the name of a resource-creating API action | String | 
|   [ecs:ResourceTag/${TagKey}](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies)  | Filters access by the tag key-value pairs attached to the resource | String | 
|   [ecs:account-setting](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the Amazon ECS account setting name | String | 
|   [ecs:auto-assign-public-ip](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the public IP assignment configuration of your Amazon ECS task or Amazon ECS service that uses awsvpc network mode | Bool | 
|   [ecs:capacity-provider](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the ARN of an Amazon ECS capacity provider | ArrayOfARN | 
|   [ecs:cluster](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the ARN of an Amazon ECS cluster | ARN | 
|   [ecs:compute-compatibility](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the required compatibilities field provided in the request | ArrayOfString | 
|   [ecs:container-instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the ARN of an Amazon ECS container instance | ARN | 
|   [ecs:container-name](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the name of an Amazon ECS container which is defined in the ECS task definition | String | 
|   [ecs:daemon](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the ARN of an Amazon ECS daemon | ARN | 
|   [ecs:daemon-task-definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the ARN of an Amazon ECS daemon task definition | ARN | 
|   [ecs:enable-ebs-volumes](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the Amazon ECS managed Amazon EBS volume capability of your ECS task or service | String | 
|   [ecs:enable-ecs-managed-tags](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the enableECSManagedTags configuration of your Amazon ECS task or Amazon ECS service | Bool | 
|   [ecs:enable-execute-command](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the execute-command capability of your Amazon ECS task or Amazon ECS service | String | 
|   [ecs:enable-service-connect](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the enable field value in the Service Connect configuration | String | 
|   [ecs:enable-vpc-lattice](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the VPC lattice capability of your Amazon ECS service | String | 
|   [ecs:fargate-ephemeral-storage-kms-key](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the AWS KMS key id provided in the request | String | 
|   [ecs:gateway](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the ARN of an Amazon ECS gateway | ARN | 
|   [ecs:instance-metadata-tags-propagation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the instance metadata tags propagation setting of your Amazon ECS capacity provider | Bool | 
|   [ecs:namespace](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the ARN of AWS Cloud Map namespace which is defined in the Service Connect Configuration | ARN | 
|   [ecs:privileged](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the privileged field provided in the request | String | 
|   [ecs:propagate-tags](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the tag propagation configuration of your Amazon ECS task or Amazon ECS service | String | 
|   [ecs:service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the ARN of an Amazon ECS service | ARN | 
|   [ecs:subnet](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the subnet configuration of your Amazon ECS task or Amazon ECS service that uses awsvpc network mode | ArrayOfString | 
|   [ecs:task](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the ARN of an Amazon ECS task | ARN | 
|   [ecs:task-cpu](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the task cpu, as an integer with 1024 = 1 vCPU, provided in the request | Numeric | 
|   [ecs:task-definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the ARN of an Amazon ECS task definition | ARN | 
|   [ecs:task-memory](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the task memory, as an integer representing MiB, provided in the request | Numeric | 