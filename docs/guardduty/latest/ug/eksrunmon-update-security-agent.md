# Updating security agent

manually for Amazon EKS resources

When you manage the GuardDuty security agent manually, you are responsible to update it
for your account. For notification about new agent versions, you can subscribe to an RSS
feed to [GuardDuty security agent release
versions](runtime-monitoring-agent-release-history.md "runtime-monitoring-agent-release-history.md").

You can update the security agent to the latest version to benefit from the added
support and improvements. If your current agent version is reaching an end of standard
support, then to continue using Runtime Monitoring (or EKS Runtime Monitoring), you must update to a next
available or the latest agent version.

**Prerequisite**

Before you update the security agent version, make sure that the agent
version that you're planning to use now, is compatible with your Kubernetes
version. For more information, see [Kubernetes versions supported by GuardDuty security
agent](prereq-runtime-monitoring-eks-support.md#gdu-agent-supported-k8-version "prereq-runtime-monitoring-eks-support.md#gdu-agent-supported-k8-version").

Console

1. Open the Amazon EKS console at [https://console.aws.amazon.com/eks/home#/clusters](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
2. Choose your **Cluster name**.
3. Under the **Cluster info**, choose the
   **Add-ons** tab.
4. Under the **Add-ons** tab, select **GuardDuty
   EKS Runtime Monitoring**.
5. Choose **Edit** to update the agent
   details.
6. On the **Configure GuardDuty EKS Runtime Monitoring** page, update
   the details.
7. ###### (Optional) Updating Optional configuration settings

If your EKS add-on **Version** is _1.5.0_
or above, you can also update the add-on configuration schema.

    1. Expand **Optional configuration
     settings** to view the configuration
     schema.
    2. Update the parameter values based on the range provided in
     [Configure EKS add-on
     parameters](guardduty-configure-security-agent-eks-addon.md "guardduty-configure-security-agent-eks-addon.md").
    3. Choose **Save changes** to start the
     update.
    4. For **Conflict resolution method**, the option that you choose will
     be used to resolve a conflict when you update the value of a parameter to a non-default value. For more
     information about the listed options, see [resolveConflicts](../../../eks/latest/APIReference/API_UpdateAddon.md#AmazonEKS-UpdateAddon-request-resolveConflicts "../../../eks/latest/APIReference/API_UpdateAddon.md#AmazonEKS-UpdateAddon-request-resolveConflicts")
     in the *Amazon EKS API Reference*.

API/CLI
To update the GuardDuty security agent for your Amazon EKS clusters, see [Updating an add-on](../../../eks/latest/userguide/managing-add-ons.md#updating-an-add-on "../../../eks/latest/userguide/managing-add-ons.md#updating-an-add-on").

###### Note

For the add-on `version`, if you choose **1.5.0 or above**, Runtime Monitoring supports
configuring specific parameters of the GuardDuty agent. For information
about parameter ranges, see [Configure EKS add-on
parameters](guardduty-configure-security-agent-eks-addon.md "guardduty-configure-security-agent-eks-addon.md").

You can use the following AWS CLI example when using configurable values
supported for add-on versions _1.5.0 and above_. Make sure to replace the
placeholder values highlighted in red and the associated
`Example.json` with the configured values.

```
aws eks update-addon --region `us-east-1` --cluster-name `myClusterName` --addon-name aws-guardduty-agent --addon-version `v1.12.1-eksbuild.2` --configuration-values `'file://example.json'`
```

###### Example.json

```
{
	"priorityClassName": "aws-guardduty-agent.priorityclass-high",
	"dnsPolicy": "Default",
	"resources": {
		"requests": {
			"cpu": "237m",
			"memory": "512Mi"
		},
		"limits": {
			"cpu": "2000m",
			"memory": "2048Mi"
		}
	}
}
```

If your Amazon EKS add-on version is 1.5.0 or above, and you have configured the add-on
schema, you can verify whether or not the values appear correctly for your cluster. For
more information, see [Verifying configuration schema
updates](guardduty-configure-security-agent-eks-addon.md#gdu-verify-eks-add-on-configuration-param "guardduty-configure-security-agent-eks-addon.md#gdu-verify-eks-add-on-configuration-param").
