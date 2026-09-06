

# Configure GuardDuty security agent (add-on) parameters for Amazon EKS
<a name="guardduty-configure-security-agent-eks-addon"></a>

You can configure specific parameters of your GuardDuty security agent for Amazon EKS. This support is available for GuardDuty security agent version 1.5.0 and above. For information about latest add-on versions, see [GuardDuty security agent versions for Amazon EKS resources](runtime-monitoring-agent-release-history.md#eks-runtime-monitoring-agent-release-history).

**Why should I update the security agent configuration schema**  
Configuration schema for the GuardDuty security agent is the same across all containers within your Amazon EKS clusters. When the default values do not align with the associated workloads and instance size, consider configuring the CPU settings, memory settings, `PriorityClass`, and `dnsPolicy` settings. Regardless of how you manage the GuardDuty agent for your Amazon EKS clusters, you can configure or update the existing configuration of these parameters.

## Automated agent configuration behavior with configured parameters
<a name="preserve-config-param-eks-addon-auto-managed"></a>

When GuardDuty manages the security agent (EKS add-on) on your behalf, it updates the add-on, as needed. GuardDuty will set the value of the configurable parameters to a default value. However, you can still update the parameters to a desired value. If this leads to a conflict, the default option to [resolveConflicts](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateAddon.html#AmazonEKS-UpdateAddon-request-resolveConflicts) is `None`.

## Configurable parameters and values
<a name="gdu-eks-addon-configure-parameters-values"></a>

For information about the steps to configure the add-on parameters, see:
+ [Installing GuardDuty security agent manually on Amazon EKS resources](eksrunmon-deploy-security-agent.md) or
+ [Updating security agent manually for Amazon EKS resources](eksrunmon-update-security-agent.md)

The following tables provide the ranges and values that you can use to deploy the Amazon EKS add-on manually or update the existing add-on settings.

**CPU settings**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/guardduty-configure-security-agent-eks-addon.html)
The `disableCpuLimits` parameter is available for GuardDuty security agent version 1.12.1-eksbuild.3 and later. On earlier versions, the add-on does not support this parameter, and the Amazon EKS add-on APIs (`CreateAddon`, `UpdateAddon`) return a validation error if you specify it.  
When you set `disableCpuLimits` to `true`, the security agent pod does not enforce a CPU limit. Other resource settings are unaffected.  
To disable CPU limits, use the following configuration:  

```
{"resources":{"disableCpuLimits":true}}
```

**Memory settings**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/guardduty-configure-security-agent-eks-addon.html)

**`PriorityClass` settings**  
When GuardDuty creates an Amazon EKS add-on for you, the assigned `PriorityClass` is `aws-guardduty-agent.priorityclass`. This means that no action will be taken based on the priority of the agent pod. You can configure this add-on parameter by choosing one of the following `PriorityClass` options:      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/guardduty-configure-security-agent-eks-addon.html)
**1** Kubernetes provides these two `PriorityClass` options – `system-cluster-critical` and `system-node-critical`. For more information, see [PriorityClass](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#how-to-use-priority-and-preemption) in the *Kubernetes documentation*.

**`dnsPolicy` settings**  
Choose one of the following DNS policy options that Kubernetes supports. When no configuration is specified, `ClusterFirst` is used as the default value.  
+ `ClusterFirst`
+ `ClusterFirstWithHostNet`
+ `Default`
For information about these policies, see [Pod's DNS Policy](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/#pod-s-dns-policy) in the *Kubernetes documentation*.

## Verifying configuration schema updates
<a name="gdu-verify-eks-add-on-configuration-param"></a>

After you have configured the parameters, perform the following steps to verify that the configuration schema has been updated:

1. Open the Amazon EKS console at [https://console.aws.amazon.com/eks/home\#/clusters](https://console.aws.amazon.com/eks/home#/clusters).

1. In the navigation pane, choose **Clusters**.

1. On the **Clusters** page, select the **Cluster name** for which you want to verify the updates.

1. Choose the **Resources** tab.

1. From the **Resource types** pane, under **Workloads**, choose **DaemonSets**.

1. Select **aws-guardduty-agent**.

1. On the **aws-guardduty-agent** page, choose **Raw view** to view the unformatted JSON response. Verify that the configurable parameters display the value that you provided.

After you verify, switch to the GuardDuty console. Select the corresponding AWS Region and view the coverage status for your Amazon EKS clusters. For more information, see [Runtime coverage and troubleshooting for Amazon EKS clusters](eks-runtime-monitoring-coverage.md).