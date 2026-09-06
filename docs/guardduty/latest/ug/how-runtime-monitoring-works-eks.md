

# How Runtime Monitoring works with Amazon EKS clusters
<a name="how-runtime-monitoring-works-eks"></a>

Runtime Monitoring uses an [EKS add-on `aws-guardduty-agent`](https://docs.aws.amazon.com/eks/latest/userguide/eks-add-ons.html#workloads-add-ons-available-eks), also known as the GuardDuty security agent. After GuardDuty security agent gets deployed on your EKS clusters, GuardDuty is able to receive runtime events for these EKS clusters. 

**Notes**  
Runtime Monitoring **supports** Amazon EKS clusters running on Amazon EC2 instances and Amazon EKS Auto Mode.  
Runtime Monitoring **doesn't support** Amazon EKS clusters with Amazon EKS Hybrid Nodes, and those running on AWS Fargate.  
For information about these Amazon EKS features, see [What is Amazon EKS?](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) in the **Amazon EKS User Guide**.

You can monitor the runtime events of your Amazon EKS clusters at either account or cluster level. You can manage the GuardDuty security agent for only those Amazon EKS clusters that you want to monitor for threat detection. You can manage the GuardDuty security agent either manually or by allowing GuardDuty to manage it on your behalf, by using Automated agent configuration.

When you use the automated agent configuration approach to allow GuardDuty to manage the deployment of the security agent on your behalf, it will automatically **create an Amazon Virtual Private Cloud (Amazon VPC) endpoint**. The security agent delivers the runtime events to GuardDuty by using this Amazon VPC endpoint. 

Along with the VPC endpoint, GuardDuty also creates a new security group. The inbound (ingress) rules control the traffic that's allowed to reach the resources, that are associated with the security group. GuardDuty adds inbound rules that match the VPC CIDR range for your resource, and also adapts to it when the CIDR range changes. For more information, see [VPC CIDR range](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cidr-blocks.html) in the *Amazon VPC User Guide*.

**Notes**  
There is no additional cost for the usage of the VPC endpoint.
Working with centralized VPC with automated agent – When you use GuardDuty automated agent configuration for a resource type, GuardDuty will create a VPC endpoint on your behalf for all the VPCs. This includes the centralized VPC and spoke VPCs. GuardDuty doesn't support creating a VPC endpoint only for the centralized VPC. For more information about how the centralized VPC works, see [Interface VPC endpoints](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/centralized-access-to-vpc-private-endpoints.html#interface-vpc-endpoints) in the *AWS Whitepaper - Building a Scalable and Secure Multi-VPC AWS Network Infrastructure*.

## Approaches to manage GuardDuty security agent in Amazon EKS clusters
<a name="eksrunmon-approach-to-monitor-eks-clusters"></a>

Prior to September 13, 2023, you could configure GuardDuty to manage the security agent at the account level. This behavior indicated that by default, GuardDuty manages the security agent on all the EKS clusters that belong to an AWS account. Now, GuardDuty provides a granular capability to help you choose the EKS clusters where you want GuardDuty to manage the security agent.

When you choose to [Manage GuardDuty security agent manually](#eks-runtime-using-gdu-agent-manually), you can still select the EKS clusters that you want to monitor. However, to manage the agent manually, creating a Amazon VPC endpoint for your AWS account is a prerequisite.

**Note**  
Regardless of the approach that you use to manage the GuardDuty security agent, EKS Runtime Monitoring is always enabled at the account level. 

**Topics**
+ [Manage security agent through GuardDuty](#eks-runtime-using-gdu-agent-management-auto)
+ [Manage GuardDuty security agent manually](#eks-runtime-using-gdu-agent-manually)

### Manage security agent through GuardDuty
<a name="eks-runtime-using-gdu-agent-management-auto"></a>

GuardDuty deploys and manages the security agent on your behalf. At any point in time, you can monitor the EKS clusters in your account by using one of the following approaches.

**Topics**
+ [Monitor all EKS clusters](#gdu-security-agent-all-eks-clusters)
+ [Exclude selective EKS clusters](#eks-runtime-using-exclusion-tags)
+ [Include selective EKS clusters](#eks-runtime-using-inclusion-tags)

#### Monitor all EKS clusters
<a name="gdu-security-agent-all-eks-clusters"></a>

Use this approach when you want GuardDuty to deploy and manage the security agent for all the EKS clusters in your account. By default, GuardDuty will also deploy the security agent on a potentially new EKS cluster created in your account.

**Impact of using this approach**  
+ GuardDuty creates an Amazon Virtual Private Cloud (Amazon VPC) endpoint through which the GuardDuty security agent delivers the runtime events to GuardDuty. There is no additional cost for the creation of the Amazon VPC endpoint when you manage the security agent through GuardDuty.
+ It is required that your worker node has a valid network path to an active `guardduty-data` VPC endpoint. GuardDuty deploys the security agent on your EKS clusters. Amazon Elastic Kubernetes Service (Amazon EKS) will coordinate the deployment of the security agent on the nodes within the EKS clusters.
+ On the basis of IP availability, GuardDuty selects the subnet to create a VPC endpoint. If you use advanced network topologies, you must validate that the connectivity is possible.

#### Exclude selective EKS clusters
<a name="eks-runtime-using-exclusion-tags"></a>

Use this approach when you want GuardDuty to manage the security agent for all EKS clusters in your account but exclude selective EKS clusters. This method uses a tag-based[1](#eks-runtime-inclusion-exclusion-tags) approach wherein you can tag the EKS clusters for which you don't want to receive the runtime events. The pre-defined tag must have `GuardDutyManaged`:`false` as the key-value pair.

**Impact of using this approach**  
This approach requires that you enable GuardDuty agent auto-management only after adding tags to the EKS clusters that you want to exclude from monitoring.  
Therefore, the impact when you [Manage security agent through GuardDuty](#eks-runtime-using-gdu-agent-management-auto) applies to this approach too. When you add tags prior to enabling GuardDuty agent auto-management, GuardDuty will neither deploy nor manage the security agent for the EKS clusters that are excluded from monitoring.

**Considerations**  
+ You must add the tag key-value pair as `GuardDutyManaged`:`false` for the selective EKS clusters before enabling Automated agent configuration otherwise, the GuardDuty security agent will be deployed on all the EKS clusters until you use the tag.
+ You must prevent the tags from being modified, except by trusted identities.
**Important**  
Manage permissions for modifying the value of the `GuardDutyManaged` tag for your EKS cluster by using service control policies or IAM policies. For more information, see [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) in the *AWS Organizations User Guide* or [Control access to AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html) in the *IAM User Guide*.
+ For a potentially new EKS cluster that you don't want to monitor, make sure to add the `GuardDutyManaged`:`false` key-value pair at the time of creating this EKS cluster.
+ This approach will also have the same consideration as specified for [Monitor all EKS clusters](#gdu-security-agent-all-eks-clusters).

#### Include selective EKS clusters
<a name="eks-runtime-using-inclusion-tags"></a>

Use this approach when you want GuardDuty to deploy and manage the updates to the security agent only for selective EKS clusters in your account. This method uses a tag-based[1](#eks-runtime-inclusion-exclusion-tags) approach wherein you can tag the EKS cluster for which you want to receive the runtime events.

**Impact of using this approach**  
+ By using inclusion tags, GuardDuty will automatically deploy and manage the security agent only for the selective EKS clusters that are tagged with `GuardDutyManaged`:`true` as the key-value pair.
+ Using this approach will also have the same impact as specified for [Monitor all EKS clusters](#gdu-security-agent-all-eks-clusters). 

**Considerations**  
+ If the value of the `GuardDutyManaged` tag is not set to `true`, the inclusion tag will not work as expected and this may impact monitoring your EKS cluster.
+ To ensure that your selective EKS clusters are being monitored, you need to prevent the tags from being modified, except by trusted identities.
**Important**  
Manage permissions for modifying the value of the `GuardDutyManaged` tag for your EKS cluster by using service control policies or IAM policies. For more information, see [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) in the *AWS Organizations User Guide* or [Control access to AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html) in the *IAM User Guide*.
+ For a potentially new EKS cluster that you don't want to monitor, make sure to add the `GuardDutyManaged`:`false` key-value pair at the time of creating this EKS cluster.
+ This approach will also have the same consideration as specified for [Monitor all EKS clusters](#gdu-security-agent-all-eks-clusters).<a name="eks-runtime-inclusion-exclusion-tags"></a>

1For more information about tagging selective EKS clusters, see [Tagging your Amazon EKS resources](https://docs.aws.amazon.com/eks/latest/userguide/eks-using-tags.html) in the **Amazon EKS User Guide**.

### Manage GuardDuty security agent manually
<a name="eks-runtime-using-gdu-agent-manually"></a>

Use this approach when you want to deploy and manage the GuardDuty security agent on all of your EKS clusters manually. Ensure that EKS Runtime Monitoring is enabled for your accounts. The GuardDuty security agent may not work as expected if you don't enable EKS Runtime Monitoring.

**Impact of using this approach**  
You will need to coordinate the deployment of the GuardDuty security agent within your EKS clusters across all accounts and AWS Regions where this feature is available. You will also need to update the agent version when GuardDuty releases it. For more information about agent versions for EKS, see [GuardDuty security agent versions for Amazon EKS resources](runtime-monitoring-agent-release-history.md#eks-runtime-monitoring-agent-release-history).

**Considerations**  
You must support secure data flow while monitoring for and addressing coverage gaps as new clusters and workloads are continuously deployed.