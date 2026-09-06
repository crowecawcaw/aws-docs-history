

# Actions, resources, and condition keys for AWS OpsWorks
<a name="list_opsworks"></a>

AWS OpsWorks (service prefix: `opsworks`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/opsworks/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/opsworks/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/opsworks/latest/userguide/workingsecurity.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/opsworks/opsworks.json) for this service.

**Topics**
+ [Actions defined by AWS OpsWorks](#list_opsworks-actions-as-permissions)
+ [Resource types defined by AWS OpsWorks](#list_opsworks-resources-for-iam-policies)
+ [Condition keys for AWS OpsWorks](#list_opsworks-policy-keys)

## Actions defined by AWS OpsWorks
<a name="list_opsworks-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssignInstance](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_AssignInstance.html)  **
  - **Description:** Grants permission to assign a registered instance to a layer
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [AssignVolume](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_AssignVolume.html)  **
  - **Description:** Grants permission to assign one of the stack's registered Amazon EBS volumes to a specified instance
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [AssociateElasticIp](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_AssociateElasticIp.html)  **
  - **Description:** Grants permission to associate one of the stack's registered Elastic IP addresses with a specified instance
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [AttachElasticLoadBalancer](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_AttachElasticLoadBalancer.html)  **
  - **Description:** Grants permission to attach an Elastic Load Balancing load balancer to a specified layer
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CloneStack](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_CloneStack.html)  **
  - **Description:** Grants permission to create a clone of a specified stack
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateApp](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_CreateApp.html)  **
  - **Description:** Grants permission to create an app for a specified stack
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateDeployment](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_CreateDeployment.html)  **
  - **Description:** Grants permission to run deployment or stack commands
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateInstance](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_CreateInstance.html)  **
  - **Description:** Grants permission to create an instance in a specified stack
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateLayer](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_CreateLayer.html)  **
  - **Description:** Grants permission to create a layer
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateStack](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_CreateStack.html)  **
  - **Description:** Grants permission to create a new stack
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateUserProfile](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_CreateUserProfile.html)  **
  - **Description:** Grants permission to create a new user profile
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteApp](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DeleteApp.html)  **
  - **Description:** Grants permission to delete a specified app
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteInstance](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DeleteInstance.html)  **
  - **Description:** Grants permission to delete a specified instance, which terminates the associated Amazon EC2 instance
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteLayer](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DeleteLayer.html)  **
  - **Description:** Grants permission to delete a specified layer
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteStack](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DeleteStack.html)  **
  - **Description:** Grants permission to delete a specified stack
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteUserProfile](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DeleteUserProfile.html)  **
  - **Description:** Grants permission to delete a user profile
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeregisterEcsCluster](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DeregisterEcsCluster.html)  **
  - **Description:** Grants permission to delete a user profile
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeregisterElasticIp](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DeregisterElasticIp.html)  **
  - **Description:** Grants permission to deregister a specified Elastic IP address
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeregisterInstance](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DeregisterInstance.html)  **
  - **Description:** Grants permission to deregister a registered Amazon EC2 or on-premises instance
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeregisterRdsDbInstance](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DeregisterRdsDbInstance.html)  **
  - **Description:** Grants permission to deregister an Amazon RDS instance
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeregisterVolume](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DeregisterVolume.html)  **
  - **Description:** Grants permission to deregister an Amazon EBS volume
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeAgentVersions](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DescribeAgentVersions.html)  **
  - **Description:** Grants permission to describe the available AWS OpsWorks agent versions
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeApps](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DescribeApps.html)  **
  - **Description:** Grants permission to request a description of a specified set of apps
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeCommands](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DescribeCommands.html)  **
  - **Description:** Grants permission to describe the results of specified commands
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeDeployments](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DescribeDeployments.html)  **
  - **Description:** Grants permission to request a description of a specified set of deployments
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeEcsClusters](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DescribeEcsClusters.html)  **
  - **Description:** Grants permission to describe Amazon ECS clusters that are registered with a stack
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeElasticIps](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DescribeElasticIps.html)  **
  - **Description:** Grants permission to describe Elastic IP addresses
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeElasticLoadBalancers](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DescribeElasticLoadBalancers.html)  **
  - **Description:** Grants permission to describe a stack's Elastic Load Balancing instances
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeInstances](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DescribeInstances.html)  **
  - **Description:** Grants permission to request a description of a set of instances
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeLayers](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DescribeLayers.html)  **
  - **Description:** Grants permission to request a description of one or more layers in a specified stack
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeLoadBasedAutoScaling](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DescribeLoadBasedAutoScaling.html)  **
  - **Description:** Grants permission to describe load-based auto scaling configurations for specified layers
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeMyUserProfile](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DescribeMyUserProfile.html)  **
  - **Description:** Grants permission to describe a user's SSH information
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeOperatingSystems](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DescribeOperatingSystems.html)  **
  - **Description:** Grants permission to describe the operating systems that are supported by AWS OpsWorks Stacks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribePermissions](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DescribePermissions.html)  **
  - **Description:** Grants permission to describe the permissions for a specified stack
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeRaidArrays](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DescribeRaidArrays.html)  **
  - **Description:** Grants permission to describe an instance's RAID arrays
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeRdsDbInstances](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DescribeRdsDbInstances.html)  **
  - **Description:** Grants permission to describe Amazon RDS instances
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeServiceErrors](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DescribeServiceErrors.html)  **
  - **Description:** Grants permission to describe AWS OpsWorks service errors
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeStackProvisioningParameters](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DescribeStackProvisioningParameters.html)  **
  - **Description:** Grants permission to request a description of a stack's provisioning parameters
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeStackSummary](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DescribeStackSummary.html)  **
  - **Description:** Grants permission to describe the number of layers and apps in a specified stack, and the number of instances in each state, such as running\_setup or online
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeStacks](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DescribeStacks.html)  **
  - **Description:** Grants permission to request a description of one or more stacks
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeTimeBasedAutoScaling](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DescribeTimeBasedAutoScaling.html)  **
  - **Description:** Grants permission to describe time-based auto scaling configurations for specified instances
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeUserProfiles](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DescribeUserProfiles.html)  **
  - **Description:** Grants permission to describe specified users
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeVolumes](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DescribeVolumes.html)  **
  - **Description:** Grants permission to describe an instance's Amazon EBS volumes
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** List

- **   [DetachElasticLoadBalancer](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DetachElasticLoadBalancer.html)  **
  - **Description:** Grants permission to detache a specified Elastic Load Balancing instance from its layer
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateElasticIp](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_DisassociateElasticIp.html)  **
  - **Description:** Grants permission to disassociate an Elastic IP address from its instance
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetHostnameSuggestion](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_GetHostnameSuggestion.html)  **
  - **Description:** Grants permission to get a generated host name for the specified layer, based on the current host name theme
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GrantAccess](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_RebootInstance.html)  **
  - **Description:** Grants permission to grant RDP access to a Windows instance for a specified time period
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [ListTags](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_ListTags.html)  **
  - **Description:** Grants permission to return a list of tags that are applied to the specified stack or layer
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** List

- **   [RebootInstance](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_RebootInstance.html)  **
  - **Description:** Grants permission to reboot a specified instance
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [RegisterEcsCluster](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_RegisterEcsCluster.html)  **
  - **Description:** Grants permission to register a specified Amazon ECS cluster with a stack
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [RegisterElasticIp](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_RegisterElasticIp.html)  **
  - **Description:** Grants permission to register an Elastic IP address with a specified stack
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [RegisterInstance](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_RegisterInstance.html)  **
  - **Description:** Grants permission to register instances with a specified stack that were created outside of AWS OpsWorks
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [RegisterRdsDbInstance](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_RegisterRdsDbInstance.html)  **
  - **Description:** Grants permission to register an Amazon RDS instance with a stack
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [RegisterVolume](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_RegisterVolume.html)  **
  - **Description:** Grants permission to register an Amazon EBS volume with a specified stack
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [SetLoadBasedAutoScaling](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_SetLoadBasedAutoScaling.html)  **
  - **Description:** Grants permission to specify the load-based auto scaling configuration for a specified layer
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [SetPermission](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_SetPermission.html)  **
  - **Description:** Grants permission to specify a user's permissions
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [SetTimeBasedAutoScaling](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_SetTimeBasedAutoScaling.html)  **
  - **Description:** Grants permission to specify the time-based auto scaling configuration for a specified instance
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartInstance](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_StartInstance.html)  **
  - **Description:** Grants permission to start a specified instance
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartStack](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_StartStack.html)  **
  - **Description:** Grants permission to start a stack's instances
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [StopInstance](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_StopInstance.html)  **
  - **Description:** Grants permission to stop a specified instance
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [StopStack](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_StopStack.html)  **
  - **Description:** Grants permission to stop a specified stack
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to apply tags to a specified stack or layer
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Tagging, Write

- **   [UnassignInstance](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_UnassignInstance.html)  **
  - **Description:** Grants permission to unassign a registered instance from all of it's layers
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UnassignVolume](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_UnassignVolume.html)  **
  - **Description:** Grants permission to unassign an assigned Amazon EBS volume
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a specified stack or layer
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Tagging, Write

- **   [UpdateApp](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_UpdateApp.html)  **
  - **Description:** Grants permission to update a specified app
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateElasticIp](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_UpdateElasticIp.html)  **
  - **Description:** Grants permission to update a registered Elastic IP address's name
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateInstance](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_UpdateInstance.html)  **
  - **Description:** Grants permission to update a specified instance
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateLayer](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_UpdateLayer.html)  **
  - **Description:** Grants permission to update a specified layer
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateMyUserProfile](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_UpdateMyUserProfile.html)  **
  - **Description:** Grants permission to update a user's SSH public key
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateRdsDbInstance](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_UpdateRdsDbInstance.html)  **
  - **Description:** Grants permission to update an Amazon RDS instance
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateStack](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_UpdateStack.html)  **
  - **Description:** Grants permission to update a specified stack
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateUserProfile](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_UpdateUserProfile.html)  **
  - **Description:** Grants permission to update a specified user profile
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [UpdateVolume](https://docs.aws.amazon.com/opsworks/latest/APIReference/API_UpdateVolume.html)  **
  - **Description:** Grants permission to update an Amazon EBS volume's name or mount point
  - **Resource types (\*required):** [stack](#list_opsworks-resource-stack)
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by AWS OpsWorks
<a name="list_opsworks-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [stack](https://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks.html)  | arn:${Partition}:opsworks:${Region}:${Account}:stack/${StackId}/ |   | 

## Condition keys for AWS OpsWorks
<a name="list_opsworks-policy-keys"></a>

AWS OpsWorks has no service-specific condition keys that can be used in the `Condition` element of policy statements.