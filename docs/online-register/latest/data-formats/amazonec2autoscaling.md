

# Data retrieval APIs for Amazon EC2 Auto Scaling
<a name="amazonec2autoscaling"></a>

Amazon EC2 Auto Scaling provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="autoscaling-DescribeAccountLimits"></a>[DescribeAccountLimits](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeAccountLimits.html) | Describe the current Auto Scaling resource limits for your AWS account | List | 
| <a name="autoscaling-DescribeAccountSettings"></a>[DescribeAccountSettings](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeAccountSettings.html) | Describe the current Amazon EC2 Auto Scaling account settings for your account | List | 
| <a name="autoscaling-DescribeAdjustmentTypes"></a>[DescribeAdjustmentTypes](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeAdjustmentTypes.html) | Describe the policy adjustment types for use with PutScalingPolicy | List | 
| <a name="autoscaling-DescribeAutoScalingGroups"></a>[DescribeAutoScalingGroups](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeAutoScalingGroups.html) | Describe one or more Auto Scaling groups. If a list of names is not provided, the call describes all Auto Scaling groups | List | 
| <a name="autoscaling-DescribeAutoScalingInstances"></a>[DescribeAutoScalingInstances](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeAutoScalingInstances.html) | Describe one or more Auto Scaling instances. If a list is not provided, the call describes all instances | List | 
| <a name="autoscaling-DescribeAutoScalingNotificationTypes"></a>[DescribeAutoScalingNotificationTypes](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeAutoScalingNotificationTypes.html) | Describe the notification types that are supported by Auto Scaling | List | 
| <a name="autoscaling-DescribeInstanceRefreshes"></a>[DescribeInstanceRefreshes](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeInstanceRefreshes.html) | Describe one or more instance refreshes for an Auto Scaling group | List | 
| <a name="autoscaling-DescribeLaunchConfigurations"></a>[DescribeLaunchConfigurations](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeLaunchConfigurations.html) | Describe one or more launch configurations. If you omit the list of names, then the call describes all launch configurations | List | 
| <a name="autoscaling-DescribeLifecycleHookTypes"></a>[DescribeLifecycleHookTypes](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeLifecycleHookTypes.html) | Describe the available types of lifecycle hooks | List | 
| <a name="autoscaling-DescribeLifecycleHooks"></a>[DescribeLifecycleHooks](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeLifecycleHooks.html) | Describe the lifecycle hooks for the specified Auto Scaling group | List | 
| <a name="autoscaling-DescribeLoadBalancerTargetGroups"></a>[DescribeLoadBalancerTargetGroups](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeLoadBalancerTargetGroups.html) | Describe the target groups for the specified Auto Scaling group | List | 
| <a name="autoscaling-DescribeLoadBalancers"></a>[DescribeLoadBalancers](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeLoadBalancers.html) | Describe the load balancers for the specified Auto Scaling group | List | 
| <a name="autoscaling-DescribeMetricCollectionTypes"></a>[DescribeMetricCollectionTypes](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeMetricCollectionTypes.html) | Describe the available CloudWatch metrics for Auto Scaling | List | 
| <a name="autoscaling-DescribeNotificationConfigurations"></a>[DescribeNotificationConfigurations](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeNotificationConfigurations.html) | Describe the notification actions associated with the specified Auto Scaling group | List | 
| <a name="autoscaling-DescribePolicies"></a>[DescribePolicies](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribePolicies.html) | Describe the policies for the specified Auto Scaling group | List | 
| <a name="autoscaling-DescribeScalingActivities"></a>[DescribeScalingActivities](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeScalingActivities.html) | Describe one or more scaling activities for the specified Auto Scaling group | List | 
| <a name="autoscaling-DescribeScalingProcessTypes"></a>[DescribeScalingProcessTypes](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeScalingProcessTypes.html) | Describe the scaling process types for use with ResumeProcesses and SuspendProcesses | List | 
| <a name="autoscaling-DescribeScheduledActions"></a>[DescribeScheduledActions](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeScheduledActions.html) | Describe the actions scheduled for your Auto Scaling group that haven't run | List | 
| <a name="autoscaling-DescribeTags"></a>[DescribeTags](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeTags.html) | Describe the specified tags | Read | 
| <a name="autoscaling-DescribeTerminationPolicyTypes"></a>[DescribeTerminationPolicyTypes](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeTerminationPolicyTypes.html) | Describe the termination policies supported by Auto Scaling | List | 
| <a name="autoscaling-DescribeTrafficSources"></a>[DescribeTrafficSources](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeTrafficSources.html) | Describe the target groups for the specified Auto Scaling group | List | 
| <a name="autoscaling-DescribeWarmPool"></a>[DescribeWarmPool](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_DescribeWarmPool.html) | Describe the warm pool associated with the Auto Scaling group | List | 
| <a name="autoscaling-GetPredictiveScalingForecast"></a>[GetPredictiveScalingForecast](https://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_GetPredictiveScalingForecast.html) | Retrieve the forecast data for a predictive scaling policy | List | 