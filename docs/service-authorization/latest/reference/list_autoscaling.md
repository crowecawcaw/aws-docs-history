

# Actions, resources, and condition keys for Amazon EC2 Auto Scaling
<a name="list_autoscaling"></a>

Amazon EC2 Auto Scaling (service prefix: `autoscaling`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/autoscaling/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/autoscaling/latest/userguide/IAM.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/autoscaling/autoscaling.json) for this service.

**Topics**
+ [API operations defined by Amazon EC2 Auto Scaling](#list_autoscaling-operations)
+ [Actions defined by Amazon EC2 Auto Scaling](#list_autoscaling-actions-as-permissions)
+ [Resource types defined by Amazon EC2 Auto Scaling](#list_autoscaling-resources-for-iam-policies)
+ [Condition keys for Amazon EC2 Auto Scaling](#list_autoscaling-policy-keys)

## API operations defined by Amazon EC2 Auto Scaling
<a name="list_autoscaling-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_autoscaling-actions-as-permissions).




- **   AttachInstances  **
  - **IAM action:**  [autoscaling:AttachInstances](#list_autoscaling-action-AttachInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AttachLoadBalancerTargetGroups  **
  - **IAM action:**  [autoscaling:AttachLoadBalancerTargetGroups](#list_autoscaling-action-AttachLoadBalancerTargetGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AttachLoadBalancers  **
  - **IAM action:**  [autoscaling:AttachLoadBalancers](#list_autoscaling-action-AttachLoadBalancers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AttachTrafficSources  **
  - **IAM action:**  [autoscaling:AttachTrafficSources](#list_autoscaling-action-AttachTrafficSources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDeleteScheduledAction  **
  - **IAM action:**  [autoscaling:BatchDeleteScheduledAction](#list_autoscaling-action-BatchDeleteScheduledAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchPutScheduledUpdateGroupAction  **
  - **IAM action:**  [autoscaling:BatchPutScheduledUpdateGroupAction](#list_autoscaling-action-BatchPutScheduledUpdateGroupAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelInstanceRefresh  **
  - **IAM action:**  [autoscaling:CancelInstanceRefresh](#list_autoscaling-action-CancelInstanceRefresh) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CompleteLifecycleAction  **
  - **IAM action:**  [autoscaling:CompleteLifecycleAction](#list_autoscaling-action-CompleteLifecycleAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAutoScalingGroup  **
  - **IAM action:**  [autoscaling:CreateAutoScalingGroup](#list_autoscaling-action-CreateAutoScalingGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [autoscaling:CreateOrUpdateTags](#list_autoscaling-action-CreateOrUpdateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** autoscaling.amazonaws.com, ec2.amazonaws.com / **Access level:** Write

- **   CreateLaunchConfiguration  **
  - **IAM action:**  [autoscaling:CreateLaunchConfiguration](#list_autoscaling-action-CreateLaunchConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ec2.amazonaws.com / **Access level:** Write

- **   CreateOrUpdateTags  **
  - **IAM action:**  [autoscaling:CreateOrUpdateTags](#list_autoscaling-action-CreateOrUpdateTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   DeleteAutoScalingGroup  **
  - **IAM action:**  [autoscaling:DeleteAutoScalingGroup](#list_autoscaling-action-DeleteAutoScalingGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLaunchConfiguration  **
  - **IAM action:**  [autoscaling:DeleteLaunchConfiguration](#list_autoscaling-action-DeleteLaunchConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLifecycleHook  **
  - **IAM action:**  [autoscaling:DeleteLifecycleHook](#list_autoscaling-action-DeleteLifecycleHook) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteNotificationConfiguration  **
  - **IAM action:**  [autoscaling:DeleteNotificationConfiguration](#list_autoscaling-action-DeleteNotificationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePolicy  **
  - **IAM action:**  [autoscaling:DeletePolicy](#list_autoscaling-action-DeletePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteScheduledAction  **
  - **IAM action:**  [autoscaling:DeleteScheduledAction](#list_autoscaling-action-DeleteScheduledAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTags  **
  - **IAM action:**  [autoscaling:DeleteTags](#list_autoscaling-action-DeleteTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   DeleteWarmPool  **
  - **IAM action:**  [autoscaling:DeleteWarmPool](#list_autoscaling-action-DeleteWarmPool) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAccountLimits  **
  - **IAM action:**  [autoscaling:DescribeAccountLimits](#list_autoscaling-action-DescribeAccountLimits) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeAdjustmentTypes  **
  - **IAM action:**  [autoscaling:DescribeAdjustmentTypes](#list_autoscaling-action-DescribeAdjustmentTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeAutoScalingGroups  **
  - **IAM action:**  [autoscaling:DescribeAutoScalingGroups](#list_autoscaling-action-DescribeAutoScalingGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeAutoScalingInstances  **
  - **IAM action:**  [autoscaling:DescribeAutoScalingInstances](#list_autoscaling-action-DescribeAutoScalingInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeAutoScalingNotificationTypes  **
  - **IAM action:**  [autoscaling:DescribeAutoScalingNotificationTypes](#list_autoscaling-action-DescribeAutoScalingNotificationTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeInstanceRefreshes  **
  - **IAM action:**  [autoscaling:DescribeInstanceRefreshes](#list_autoscaling-action-DescribeInstanceRefreshes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeLaunchConfigurations  **
  - **IAM action:**  [autoscaling:DescribeLaunchConfigurations](#list_autoscaling-action-DescribeLaunchConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeLifecycleHookTypes  **
  - **IAM action:**  [autoscaling:DescribeLifecycleHookTypes](#list_autoscaling-action-DescribeLifecycleHookTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeLifecycleHooks  **
  - **IAM action:**  [autoscaling:DescribeLifecycleHooks](#list_autoscaling-action-DescribeLifecycleHooks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeLoadBalancerTargetGroups  **
  - **IAM action:**  [autoscaling:DescribeLoadBalancerTargetGroups](#list_autoscaling-action-DescribeLoadBalancerTargetGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeLoadBalancers  **
  - **IAM action:**  [autoscaling:DescribeLoadBalancers](#list_autoscaling-action-DescribeLoadBalancers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeMetricCollectionTypes  **
  - **IAM action:**  [autoscaling:DescribeMetricCollectionTypes](#list_autoscaling-action-DescribeMetricCollectionTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeNotificationConfigurations  **
  - **IAM action:**  [autoscaling:DescribeNotificationConfigurations](#list_autoscaling-action-DescribeNotificationConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribePolicies  **
  - **IAM action:**  [autoscaling:DescribePolicies](#list_autoscaling-action-DescribePolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeScalingActivities  **
  - **IAM action:**  [autoscaling:DescribeScalingActivities](#list_autoscaling-action-DescribeScalingActivities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeScalingProcessTypes  **
  - **IAM action:**  [autoscaling:DescribeScalingProcessTypes](#list_autoscaling-action-DescribeScalingProcessTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeScheduledActions  **
  - **IAM action:**  [autoscaling:DescribeScheduledActions](#list_autoscaling-action-DescribeScheduledActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeTags  **
  - **IAM action:**  [autoscaling:DescribeTags](#list_autoscaling-action-DescribeTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTerminationPolicyTypes  **
  - **IAM action:**  [autoscaling:DescribeTerminationPolicyTypes](#list_autoscaling-action-DescribeTerminationPolicyTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeTrafficSources  **
  - **IAM action:**  [autoscaling:DescribeTrafficSources](#list_autoscaling-action-DescribeTrafficSources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeWarmPool  **
  - **IAM action:**  [autoscaling:DescribeWarmPool](#list_autoscaling-action-DescribeWarmPool) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DetachInstances  **
  - **IAM action:**  [autoscaling:DetachInstances](#list_autoscaling-action-DetachInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DetachLoadBalancerTargetGroups  **
  - **IAM action:**  [autoscaling:DetachLoadBalancerTargetGroups](#list_autoscaling-action-DetachLoadBalancerTargetGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DetachLoadBalancers  **
  - **IAM action:**  [autoscaling:DetachLoadBalancers](#list_autoscaling-action-DetachLoadBalancers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DetachTrafficSources  **
  - **IAM action:**  [autoscaling:DetachTrafficSources](#list_autoscaling-action-DetachTrafficSources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisableMetricsCollection  **
  - **IAM action:**  [autoscaling:DisableMetricsCollection](#list_autoscaling-action-DisableMetricsCollection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableMetricsCollection  **
  - **IAM action:**  [autoscaling:EnableMetricsCollection](#list_autoscaling-action-EnableMetricsCollection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnterStandby  **
  - **IAM action:**  [autoscaling:EnterStandby](#list_autoscaling-action-EnterStandby) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ExecutePolicy  **
  - **IAM action:**  [autoscaling:ExecutePolicy](#list_autoscaling-action-ExecutePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ExitStandby  **
  - **IAM action:**  [autoscaling:ExitStandby](#list_autoscaling-action-ExitStandby) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetPredictiveScalingForecast  **
  - **IAM action:**  [autoscaling:GetPredictiveScalingForecast](#list_autoscaling-action-GetPredictiveScalingForecast) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   LaunchInstances  **
  - **IAM action:**  [autoscaling:LaunchInstances](#list_autoscaling-action-LaunchInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutLifecycleHook  **
  - **IAM action:**  [autoscaling:PutLifecycleHook](#list_autoscaling-action-PutLifecycleHook)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** autoscaling.amazonaws.com / **Access level:** Write

- **   PutNotificationConfiguration  **
  - **IAM action:**  [autoscaling:PutNotificationConfiguration](#list_autoscaling-action-PutNotificationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutScalingPolicy  **
  - **IAM action:**  [autoscaling:PutScalingPolicy](#list_autoscaling-action-PutScalingPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutScheduledUpdateGroupAction  **
  - **IAM action:**  [autoscaling:PutScheduledUpdateGroupAction](#list_autoscaling-action-PutScheduledUpdateGroupAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutWarmPool  **
  - **IAM action:**  [autoscaling:PutWarmPool](#list_autoscaling-action-PutWarmPool) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RecordLifecycleActionHeartbeat  **
  - **IAM action:**  [autoscaling:RecordLifecycleActionHeartbeat](#list_autoscaling-action-RecordLifecycleActionHeartbeat) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ResumeProcesses  **
  - **IAM action:**  [autoscaling:ResumeProcesses](#list_autoscaling-action-ResumeProcesses) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RollbackInstanceRefresh  **
  - **IAM action:**  [autoscaling:RollbackInstanceRefresh](#list_autoscaling-action-RollbackInstanceRefresh) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetDesiredCapacity  **
  - **IAM action:**  [autoscaling:SetDesiredCapacity](#list_autoscaling-action-SetDesiredCapacity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetInstanceHealth  **
  - **IAM action:**  [autoscaling:SetInstanceHealth](#list_autoscaling-action-SetInstanceHealth) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetInstanceProtection  **
  - **IAM action:**  [autoscaling:SetInstanceProtection](#list_autoscaling-action-SetInstanceProtection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartInstanceRefresh  **
  - **IAM action:**  [autoscaling:StartInstanceRefresh](#list_autoscaling-action-StartInstanceRefresh) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SuspendProcesses  **
  - **IAM action:**  [autoscaling:SuspendProcesses](#list_autoscaling-action-SuspendProcesses) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TerminateInstanceInAutoScalingGroup  **
  - **IAM action:**  [autoscaling:TerminateInstanceInAutoScalingGroup](#list_autoscaling-action-TerminateInstanceInAutoScalingGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAutoScalingGroup  **
  - **IAM action:**  [autoscaling:UpdateAutoScalingGroup](#list_autoscaling-action-UpdateAutoScalingGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** autoscaling.amazonaws.com / **Access level:** Write



## Actions defined by Amazon EC2 Auto Scaling
<a name="list_autoscaling-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AttachInstances](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_AttachInstances.html)  **
  - **Description:** Grants permission to attach one or more EC2 instances to the specified Auto Scaling group
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AttachLoadBalancerTargetGroups](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_AttachLoadBalancerTargetGroups.html)  **
  - **Description:** Grants permission to attach one or more target groups to the specified Auto Scaling group
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[autoscaling:TargetGroupARNs](#list_autoscaling-autoscaling_TargetGroupARNs)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AttachLoadBalancers](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_AttachLoadBalancers.html)  **
  - **Description:** Grants permission to attach one or more load balancers to the specified Auto Scaling group
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:LoadBalancerNames](#list_autoscaling-autoscaling_LoadBalancerNames)<br />[autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AttachTrafficSources](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_AttachTrafficSources.html)  **
  - **Description:** Grants permission to attach one or more traffic sources to an Auto Scaling group
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[autoscaling:TrafficSourceIdentifiers](#list_autoscaling-autoscaling_TrafficSourceIdentifiers)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDeleteScheduledAction](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_BatchDeleteScheduledAction.html)  **
  - **Description:** Grants permission to delete the specified scheduled actions
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchPutScheduledUpdateGroupAction](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_BatchPutScheduledUpdateGroupAction.html)  **
  - **Description:** Grants permission to create or update multiple scheduled scaling actions for an Auto Scaling group
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelInstanceRefresh](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_CancelInstanceRefresh.html)  **
  - **Description:** Grants permission to cancel an instance refresh operation in progress
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CompleteLifecycleAction](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_CompleteLifecycleAction.html)  **
  - **Description:** Grants permission to complete the lifecycle action for the specified token or instance with the specified result
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAutoScalingGroup](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_CreateAutoScalingGroup.html)  **
  - **Description:** Grants permission to create an Auto Scaling group with the specified name and attributes
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:CapacityReservationIds](#list_autoscaling-autoscaling_CapacityReservationIds)<br />[autoscaling:CapacityReservationResourceGroupArns](#list_autoscaling-autoscaling_CapacityReservationResourceGroupArns)<br />[autoscaling:ImageId](#list_autoscaling-autoscaling_ImageId)<br />[autoscaling:InstanceTypes](#list_autoscaling-autoscaling_InstanceTypes)<br />[autoscaling:LaunchConfigurationName](#list_autoscaling-autoscaling_LaunchConfigurationName)<br />[autoscaling:LaunchTemplateVersionSpecified](#list_autoscaling-autoscaling_LaunchTemplateVersionSpecified)<br />[autoscaling:LoadBalancerNames](#list_autoscaling-autoscaling_LoadBalancerNames)<br />[autoscaling:MaxSize](#list_autoscaling-autoscaling_MaxSize)<br />[autoscaling:MinSize](#list_autoscaling-autoscaling_MinSize)<br />[autoscaling:OperatorPrincipal](#list_autoscaling-autoscaling_OperatorPrincipal)<br />[autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[autoscaling:TargetCapacityTypes](#list_autoscaling-autoscaling_TargetCapacityTypes)<br />[autoscaling:TargetGroupARNs](#list_autoscaling-autoscaling_TargetGroupARNs)<br />[autoscaling:TrafficSourceIdentifiers](#list_autoscaling-autoscaling_TrafficSourceIdentifiers)<br />[autoscaling:VPCZoneIdentifiers](#list_autoscaling-autoscaling_VPCZoneIdentifiers)<br />[aws:RequestTag/${TagKey}](#list_autoscaling-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_autoscaling-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLaunchConfiguration](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_CreateLaunchConfiguration.html)  **
  - **Description:** Grants permission to create a launch configuration
  - **Resource types (\*required):** [launchConfiguration\*](#list_autoscaling-resource-launchConfiguration)
  - **Condition keys:** [autoscaling:ImageId](#list_autoscaling-autoscaling_ImageId)<br />[autoscaling:InstanceType](#list_autoscaling-autoscaling_InstanceType)<br />[autoscaling:MetadataHttpEndpoint](#list_autoscaling-autoscaling_MetadataHttpEndpoint)<br />[autoscaling:MetadataHttpPutResponseHopLimit](#list_autoscaling-autoscaling_MetadataHttpPutResponseHopLimit)<br />[autoscaling:MetadataHttpTokens](#list_autoscaling-autoscaling_MetadataHttpTokens)<br />[autoscaling:SpotPrice](#list_autoscaling-autoscaling_SpotPrice)
  - **Access level:** Write

- **   [CreateOrUpdateTags](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_CreateOrUpdateTags.html)  **
  - **Description:** Grants permission to create or update tags for the specified Auto Scaling group
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:RequestTag/${TagKey}](#list_autoscaling-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_autoscaling-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [DeleteAutoScalingGroup](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DeleteAutoScalingGroup.html)  **
  - **Description:** Grants permission to delete the specified Auto Scaling group
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ForceDelete](#list_autoscaling-autoscaling_ForceDelete)<br />[autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLaunchConfiguration](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DeleteLaunchConfiguration.html)  **
  - **Description:** Grants permission to delete the specified launch configuration
  - **Resource types (\*required):** [launchConfiguration\*](#list_autoscaling-resource-launchConfiguration)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteLifecycleHook](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DeleteLifecycleHook.html)  **
  - **Description:** Grants permission to deletes the specified lifecycle hook
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteNotificationConfiguration](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DeleteNotificationConfiguration.html)  **
  - **Description:** Grants permission to delete the specified notification
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePolicy](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DeletePolicy.html)  **
  - **Description:** Grants permission to delete the specified Auto Scaling policy
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteScheduledAction](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DeleteScheduledAction.html)  **
  - **Description:** Grants permission to delete the specified scheduled action
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTags](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DeleteTags.html)  **
  - **Description:** Grants permission to delete the specified tags
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:RequestTag/${TagKey}](#list_autoscaling-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_autoscaling-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [DeleteWarmPool](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DeleteWarmPool.html)  **
  - **Description:** Grants permission to delete the warm pool associated with the Auto Scaling group
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeAccountLimits](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeAccountLimits.html)  **
  - **Description:** Grants permission to describe the current Auto Scaling resource limits for your AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeAccountSettings](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeAccountSettings.html)  **
  - **Description:** Grants permission to describe the current Amazon EC2 Auto Scaling account settings for your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeAdjustmentTypes](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeAdjustmentTypes.html)  **
  - **Description:** Grants permission to describe the policy adjustment types for use with PutScalingPolicy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeAutoScalingGroups](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeAutoScalingGroups.html)  **
  - **Description:** Grants permission to describe one or more Auto Scaling groups. If a list of names is not provided, the call describes all Auto Scaling groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeAutoScalingInstances](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeAutoScalingInstances.html)  **
  - **Description:** Grants permission to describe one or more Auto Scaling instances. If a list is not provided, the call describes all instances
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeAutoScalingNotificationTypes](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeAutoScalingNotificationTypes.html)  **
  - **Description:** Grants permission to describe the notification types that are supported by Auto Scaling
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeInstanceRefreshes](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeInstanceRefreshes.html)  **
  - **Description:** Grants permission to describe one or more instance refreshes for an Auto Scaling group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeLaunchConfigurations](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeLaunchConfigurations.html)  **
  - **Description:** Grants permission to describe one or more launch configurations. If you omit the list of names, then the call describes all launch configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeLifecycleHookTypes](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeLifecycleHookTypes.html)  **
  - **Description:** Grants permission to describe the available types of lifecycle hooks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeLifecycleHooks](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeLifecycleHooks.html)  **
  - **Description:** Grants permission to describe the lifecycle hooks for the specified Auto Scaling group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeLoadBalancerTargetGroups](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeLoadBalancerTargetGroups.html)  **
  - **Description:** Grants permission to describe the target groups for the specified Auto Scaling group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeLoadBalancers](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeLoadBalancers.html)  **
  - **Description:** Grants permission to describe the load balancers for the specified Auto Scaling group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeMetricCollectionTypes](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeMetricCollectionTypes.html)  **
  - **Description:** Grants permission to describe the available CloudWatch metrics for Auto Scaling
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeNotificationConfigurations](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeNotificationConfigurations.html)  **
  - **Description:** Grants permission to describe the notification actions associated with the specified Auto Scaling group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribePolicies](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribePolicies.html)  **
  - **Description:** Grants permission to describe the policies for the specified Auto Scaling group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeScalingActivities](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeScalingActivities.html)  **
  - **Description:** Grants permission to describe one or more scaling activities for the specified Auto Scaling group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeScalingProcessTypes](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeScalingProcessTypes.html)  **
  - **Description:** Grants permission to describe the scaling process types for use with ResumeProcesses and SuspendProcesses
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeScheduledActions](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeScheduledActions.html)  **
  - **Description:** Grants permission to describe the actions scheduled for your Auto Scaling group that haven't run
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeTags](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeTags.html)  **
  - **Description:** Grants permission to describe the specified tags
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeTerminationPolicyTypes](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeTerminationPolicyTypes.html)  **
  - **Description:** Grants permission to describe the termination policies supported by Auto Scaling
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeTrafficSources](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeTrafficSources.html)  **
  - **Description:** Grants permission to describe the target groups for the specified Auto Scaling group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeWarmPool](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeWarmPool.html)  **
  - **Description:** Grants permission to describe the warm pool associated with the Auto Scaling group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DetachInstances](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DetachInstances.html)  **
  - **Description:** Grants permission to remove one or more instances from the specified Auto Scaling group
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DetachLoadBalancerTargetGroups](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DetachLoadBalancerTargetGroups.html)  **
  - **Description:** Grants permission to detach one or more target groups from the specified Auto Scaling group
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[autoscaling:TargetGroupARNs](#list_autoscaling-autoscaling_TargetGroupARNs)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DetachLoadBalancers](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DetachLoadBalancers.html)  **
  - **Description:** Grants permission to remove one or more load balancers from the specified Auto Scaling group
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:LoadBalancerNames](#list_autoscaling-autoscaling_LoadBalancerNames)<br />[autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DetachTrafficSources](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DetachTrafficSources.html)  **
  - **Description:** Grants permission to detach one or more traffic sources from an Auto Scaling group
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[autoscaling:TrafficSourceIdentifiers](#list_autoscaling-autoscaling_TrafficSourceIdentifiers)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisableMetricsCollection](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DisableMetricsCollection.html)  **
  - **Description:** Grants permission to disable monitoring of the specified metrics for the specified Auto Scaling group
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableMetricsCollection](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_EnableMetricsCollection.html)  **
  - **Description:** Grants permission to enable monitoring of the specified metrics for the specified Auto Scaling group
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnterStandby](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_EnterStandby.html)  **
  - **Description:** Grants permission to move the specified instances into Standby mode
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ExecutePolicy](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_ExecutePolicy.html)  **
  - **Description:** Grants permission to execute the specified policy
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ExitStandby](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_ExitStandby.html)  **
  - **Description:** Grants permission to move the specified instances out of Standby mode
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetPredictiveScalingForecast](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_GetPredictiveScalingForecast.html)  **
  - **Description:** Grants permission to retrieve the forecast data for a predictive scaling policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [LaunchInstances](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_LaunchInstances.html)  **
  - **Description:** Grants permission to launch one or more EC2 instances in the specified Auto Scaling group
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutAccountSetting](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_PutAccountSetting.html)  **
  - **Description:** Grants permission to modify an account setting for your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutLifecycleHook](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_PutLifecycleHook.html)  **
  - **Description:** Grants permission to create or update a lifecycle hook for the specified Auto Scaling Group
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutNotificationConfiguration](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_PutNotificationConfiguration.html)  **
  - **Description:** Grants permission to configure an Auto Scaling group to send notifications when specified events take place
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutScalingPolicy](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_PutScalingPolicy.html)  **
  - **Description:** Grants permission to create or update a policy for an Auto Scaling group
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutScheduledUpdateGroupAction](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_PutScheduledUpdateGroupAction.html)  **
  - **Description:** Grants permission to create or update a scheduled scaling action for an Auto Scaling group
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:MaxSize](#list_autoscaling-autoscaling_MaxSize)<br />[autoscaling:MinSize](#list_autoscaling-autoscaling_MinSize)<br />[autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutWarmPool](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_PutWarmPool.html)  **
  - **Description:** Grants permission to create or update the warm pool associated with the specified Auto Scaling group
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RecordLifecycleActionHeartbeat](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_RecordLifecycleActionHeartbeat.html)  **
  - **Description:** Grants permission to record a heartbeat for the lifecycle action associated with the specified token or instance
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ResumeProcesses](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_ResumeProcesses.html)  **
  - **Description:** Grants permission to resume the specified suspended Auto Scaling processes, or all suspended process, for the specified Auto Scaling group
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RollbackInstanceRefresh](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_RollbackInstanceRefresh.html)  **
  - **Description:** Grants permission to rollback an instance refresh operation in progress
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetDesiredCapacity](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_SetDesiredCapacity.html)  **
  - **Description:** Grants permission to set the size of the specified Auto Scaling group
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetInstanceHealth](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_SetInstanceHealth.html)  **
  - **Description:** Grants permission to set the health status of the specified instance
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetInstanceProtection](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_SetInstanceProtection.html)  **
  - **Description:** Grants permission to update the instance protection settings of the specified instances
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartInstanceRefresh](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_StartInstanceRefresh.html)  **
  - **Description:** Grants permission to start a new instance refresh operation
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ImageId](#list_autoscaling-autoscaling_ImageId)<br />[autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[autoscaling:TargetCapacityTypes](#list_autoscaling-autoscaling_TargetCapacityTypes)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SuspendProcesses](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_SuspendProcesses.html)  **
  - **Description:** Grants permission to suspend the specified Auto Scaling processes, or all processes, for the specified Auto Scaling group
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TerminateInstanceInAutoScalingGroup](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_TerminateInstanceInAutoScalingGroup.html)  **
  - **Description:** Grants permission to terminate the specified instance and optionally adjust the desired group size
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAutoScalingGroup](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_UpdateAutoScalingGroup.html)  **
  - **Description:** Grants permission to update the configuration for the specified Auto Scaling group
  - **Resource types (\*required):** [autoScalingGroup\*](#list_autoscaling-resource-autoScalingGroup)
  - **Condition keys:** [autoscaling:CapacityReservationIds](#list_autoscaling-autoscaling_CapacityReservationIds)<br />[autoscaling:CapacityReservationResourceGroupArns](#list_autoscaling-autoscaling_CapacityReservationResourceGroupArns)<br />[autoscaling:ImageId](#list_autoscaling-autoscaling_ImageId)<br />[autoscaling:InstanceTypes](#list_autoscaling-autoscaling_InstanceTypes)<br />[autoscaling:LaunchConfigurationName](#list_autoscaling-autoscaling_LaunchConfigurationName)<br />[autoscaling:LaunchTemplateVersionSpecified](#list_autoscaling-autoscaling_LaunchTemplateVersionSpecified)<br />[autoscaling:MaxSize](#list_autoscaling-autoscaling_MaxSize)<br />[autoscaling:MinSize](#list_autoscaling-autoscaling_MinSize)<br />[autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[autoscaling:TargetCapacityTypes](#list_autoscaling-autoscaling_TargetCapacityTypes)<br />[autoscaling:VPCZoneIdentifiers](#list_autoscaling-autoscaling_VPCZoneIdentifiers)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon EC2 Auto Scaling
<a name="list_autoscaling-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [autoScalingGroup](https://docs.aws.amazon.com/autoscaling/latest/userguide/control-access-using-iam.html#policy-auto-scaling-resources)  | arn:${Partition}:autoscaling:${Region}:${Account}:autoScalingGroup:${GroupId}:autoScalingGroupName/${GroupFriendlyName} | [autoscaling:ResourceTag/${TagKey}](#list_autoscaling-autoscaling_ResourceTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_autoscaling-aws_ResourceTag___TagKey_) | 
|  [launchConfiguration](https://docs.aws.amazon.com/autoscaling/latest/userguide/control-access-using-iam.html#policy-auto-scaling-resources)  | arn:${Partition}:autoscaling:${Region}:${Account}:launchConfiguration:${Id}:launchConfigurationName/${LaunchConfigurationName} |   | 

## Condition keys for Amazon EC2 Auto Scaling
<a name="list_autoscaling-policy-keys"></a>

Amazon EC2 Auto Scaling defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [autoscaling:CapacityReservationIds](https://docs.aws.amazon.com/autoscaling/latest/userguide/control-access-using-iam.html#policy-auto-scaling-condition-keys)  | Filters access based on the Capacity Reservation IDs | ArrayOfString | 
|   [autoscaling:CapacityReservationResourceGroupArns](https://docs.aws.amazon.com/autoscaling/latest/userguide/control-access-using-iam.html#policy-auto-scaling-condition-keys)  | Filters access based on the ARN of a Capacity Reservation resource group | ArrayOfString | 
|   [autoscaling:ForceDelete](https://docs.aws.amazon.com/autoscaling/latest/userguide/control-access-using-iam.html#policy-auto-scaling-condition-keys)  | Filters access based on whether the force delete option is specified when deleting an Auto Scaling group | Bool | 
|   [autoscaling:ImageId](https://docs.aws.amazon.com/autoscaling/latest/userguide/control-access-using-iam.html#policy-auto-scaling-condition-keys)  | Filters access based on the AMI ID for the launch configuration | String | 
|   [autoscaling:InstanceType](https://docs.aws.amazon.com/autoscaling/latest/userguide/control-access-using-iam.html#policy-auto-scaling-condition-keys)  | Filters access based on the instance type for the launch configuration | String | 
|   [autoscaling:InstanceTypes](https://docs.aws.amazon.com/autoscaling/latest/userguide/control-access-using-iam.html#policy-auto-scaling-condition-keys)  | Filters access based on the instance types present as overrides to a launch template for a mixed instances policy. Use it to qualify which instance types can be explicitly defined in the policy | String | 
|   [autoscaling:LaunchConfigurationName](https://docs.aws.amazon.com/autoscaling/latest/userguide/control-access-using-iam.html#policy-auto-scaling-condition-keys)  | Filters access based on the name of a launch configuration | String | 
|   [autoscaling:LaunchTemplateVersionSpecified](https://docs.aws.amazon.com/autoscaling/latest/userguide/control-access-using-iam.html#policy-auto-scaling-condition-keys)  | Filters access based on whether users can specify any version of a launch template or only the Latest or Default version | Bool | 
|   [autoscaling:LoadBalancerNames](https://docs.aws.amazon.com/autoscaling/latest/userguide/control-access-using-iam.html#policy-auto-scaling-condition-keys)  | Filters access based on the name of the load balancer | ArrayOfString | 
|   [autoscaling:MaxSize](https://docs.aws.amazon.com/autoscaling/latest/userguide/control-access-using-iam.html#policy-auto-scaling-condition-keys)  | Filters access based on the maximum scaling size in the request | Numeric | 
|   [autoscaling:MetadataHttpEndpoint](https://docs.aws.amazon.com/autoscaling/latest/userguide/control-access-using-iam.html#policy-auto-scaling-condition-keys)  | Filters access based on whether the HTTP endpoint is enabled for the instance metadata service | String | 
|   [autoscaling:MetadataHttpPutResponseHopLimit](https://docs.aws.amazon.com/autoscaling/latest/userguide/control-access-using-iam.html#policy-auto-scaling-condition-keys)  | Filters access based on the allowed number of hops when calling the instance metadata service | Numeric | 
|   [autoscaling:MetadataHttpTokens](https://docs.aws.amazon.com/autoscaling/latest/userguide/control-access-using-iam.html#policy-auto-scaling-condition-keys)  | Filters access based on whether tokens are required when calling the instance metadata service (optional or required) | String | 
|   [autoscaling:MinSize](https://docs.aws.amazon.com/autoscaling/latest/userguide/control-access-using-iam.html#policy-auto-scaling-condition-keys)  | Filters access based on the minimum scaling size in the request | Numeric | 
|   [autoscaling:OperatorPrincipal](https://docs.aws.amazon.com/autoscaling/latest/userguide/control-access-using-iam.html#policy-auto-scaling-condition-keys)  | Filters access based on the the operator for EC2 Managed Instances | String | 
|   [autoscaling:ResourceTag/${TagKey}](https://docs.aws.amazon.com/autoscaling/latest/userguide/control-access-using-iam.html#policy-auto-scaling-condition-keys)  | Filters access based on the tags associated with the resource | String | 
|   [autoscaling:SpotPrice](https://docs.aws.amazon.com/autoscaling/latest/userguide/control-access-using-iam.html#policy-auto-scaling-condition-keys)  | Filters access based on the price for Spot Instances for the launch configuration | Numeric | 
|   [autoscaling:TargetCapacityTypes](https://docs.aws.amazon.com/autoscaling/latest/userguide/control-access-using-iam.html#policy-auto-scaling-condition-keys)  | Filters access based on the target capacity types present in the distribution segments of a mixed instances policy. Use it to qualify which capacity types can be explicitly defined in the policy | ArrayOfString | 
|   [autoscaling:TargetGroupARNs](https://docs.aws.amazon.com/autoscaling/latest/userguide/control-access-using-iam.html#policy-auto-scaling-condition-keys)  | Filters access based on the ARN of a target group | ArrayOfARN | 
|   [autoscaling:TrafficSourceIdentifiers](https://docs.aws.amazon.com/autoscaling/latest/userguide/control-access-using-iam.html#policy-auto-scaling-condition-keys)  | Filters access based on the identifiers of the traffic sources | ArrayOfString | 
|   [autoscaling:VPCZoneIdentifiers](https://docs.aws.amazon.com/autoscaling/latest/userguide/control-access-using-iam.html#policy-auto-scaling-condition-keys)  | Filters access based on the identifier of a VPC zone | ArrayOfString | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/autoscaling/latest/userguide/control-access-using-iam.html#policy-auto-scaling-condition-keys)  | Filters access based on the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/autoscaling/latest/userguide/control-access-using-iam.html#policy-auto-scaling-condition-keys)  | Filters access based on the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/autoscaling/latest/userguide/control-access-using-iam.html#policy-auto-scaling-condition-keys)  | Filters access based on the tag keys that are passed in the request | ArrayOfString | 