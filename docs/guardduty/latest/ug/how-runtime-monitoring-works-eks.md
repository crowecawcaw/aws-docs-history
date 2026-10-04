

# Deploying the security agent to Amazon EKS
<a name="how-runtime-monitoring-works-eks"></a>

GuardDuty Runtime Monitoring monitors your Amazon EKS clusters for threats by deploying the GuardDuty security agent to them. On Amazon EKS, GuardDuty deploys the agent as the [EKS add-on `aws-guardduty-agent`](https://docs.aws.amazon.com/eks/latest/userguide/eks-add-ons.html#workloads-add-ons-available-eks).

**Notes**  
Runtime Monitoring **supports** Amazon EKS clusters running on Amazon EC2 instances and Amazon EKS Auto Mode.  
Runtime Monitoring **doesn't support** Amazon EKS clusters with Amazon EKS Hybrid Nodes, and those running on AWS Fargate.  
For information about these Amazon EKS features, see [What is Amazon EKS?](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) in the **Amazon EKS User Guide**.

You can let GuardDuty manage the agent automatically (recommended) or manage it manually.

## Automated agent configuration (recommended)
<a name="eks-runtime-using-gdu-agent-management-auto"></a>

GuardDuty manages deployment and updates to the security agent for your EKS clusters. In the GuardDuty console, this configuration appears as *Runtime Monitoring (EKS)*.

For how the security agent connects to GuardDuty, see [How the security agent connects to GuardDuty](runtime-monitoring-agent-connectivity.md).

**Impact of enabling the security agent**

GuardDuty deploys the security agent to your EKS clusters, and Amazon Elastic Kubernetes Service (Amazon EKS) coordinates deploying it to the nodes.

**Monitoring scope**

By default, GuardDuty manages the security agent for all EKS clusters in your account, including new clusters you create. To stop GuardDuty from managing the agent on a specific cluster, add the tag `GuardDutyManaged`:`false` to that cluster.

For more information about tagging EKS clusters, see [Tagging your Amazon EKS resources](https://docs.aws.amazon.com/eks/latest/userguide/eks-using-tags.html) in the **Amazon EKS User Guide**.

**Considerations**
+ When automated agent configuration is off, GuardDuty manages the security agent only on the EKS clusters that you tag with `GuardDutyManaged`:`true`.
+ Adding the `GuardDutyManaged`:`false` tag stops GuardDuty from managing the security agent, but doesn't uninstall an agent that is already installed.
+ Protect the `GuardDutyManaged` tag by controlling who can modify it, using service control policies or IAM policies. For more information, see [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) in the *AWS Organizations User Guide* or [Control access to AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html) in the *IAM User Guide*.

## Manual agent configuration
<a name="eks-runtime-using-gdu-agent-manually"></a>

Use this approach when you want to manually deploy and manage the GuardDuty security agent on all your EKS clusters. Ensure Runtime Monitoring is enabled for your accounts. The GuardDuty security agent might not work as expected if Runtime Monitoring isn't enabled.

**Impact of using this approach**

You must coordinate deploying the GuardDuty security agent within your EKS clusters across all your accounts. To get the latest security features, you must also update the agent when GuardDuty releases a new version. For more information about agent versions for EKS, see [GuardDuty security agent versions for Amazon EKS resources](runtime-monitoring-agent-release-history.md#eks-runtime-monitoring-agent-release-history).

**Considerations**

You must support secure data flow while monitoring for and addressing coverage gaps as new clusters and workloads are continuously deployed.

## Related topics
<a name="eksrunmon-related"></a>
+ [How the security agent connects to GuardDuty](runtime-monitoring-agent-connectivity.md)
+ [Tracking Runtime Monitoring coverage](runtime-monitoring-after-configuration.md)