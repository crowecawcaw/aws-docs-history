

# How the security agent connects to GuardDuty
<a name="runtime-monitoring-agent-connectivity"></a>

The Runtime Monitoring security agent delivers runtime events to GuardDuty over one of two connectivity methods: a link-local address or an Amazon VPC endpoint. Both keep data within the AWS network. There is no additional cost for GuardDuty connectivity.

## Link-local connectivity
<a name="runtime-monitoring-connectivity-link-local"></a>

The agent connects to the GuardDuty backend over a link-local address, at `guardduty-data-v2.{{us-east-1}}.amazonaws.com`. Link-local connectivity doesn't use private DNS. Replace {{us-east-1}} with your AWS Region.

## Amazon VPC endpoint connectivity
<a name="runtime-monitoring-connectivity-vpc-endpoint"></a>

The agent connects to the GuardDuty backend through an Amazon VPC endpoint. It resolves and connects to the endpoint's private DNS name. For a non-FIPS endpoint, this is `guardduty-data.{{us-east-1}}.amazonaws.com`. Replace {{us-east-1}} with your AWS Region.

The resource must have a valid network path to an active `guardduty-data` Amazon VPC endpoint. GuardDuty selects the subnet based on IP availability, so for advanced network topologies, validate that a valid network path exists.

If you delete an Amazon VPC endpoint that an agent is using and the Amazon VPC has no link-local path, Runtime Monitoring stops for that resource.

## Prerequisites
<a name="runtime-monitoring-connectivity-prerequisites"></a>

For prerequisites, see [Prerequisites to enabling Runtime Monitoring](runtime-monitoring-prerequisites.md).

## Considerations
<a name="runtime-monitoring-connectivity-considerations"></a>
+ **Automated agent configuration** – GuardDuty establishes connectivity automatically. For new Runtime Monitoring enablements, the agent connects to GuardDuty over a link-local address. If you manage the agent manually, you need to create an Amazon VPC endpoint for the agent to connect through.
+ **Region availability** – Link-local connectivity is not supported in all AWS Regions. In Regions where it is not supported, the agent connects through an Amazon VPC endpoint.
+ **Minimum agent version** – Link-local connectivity requires security agent version `v1.17.3` or later for Amazon EC2 instances, Amazon ECS (including AWS Fargate), and Amazon EKS clusters. For security agent version history, see [GuardDuty security agent release versions](runtime-monitoring-agent-release-history.md).
+ **All VPCs** – With automated agent configuration, GuardDuty sets up connectivity across all your VPCs, including centralized and spoke VPCs. For more information about centralized VPCs, see [Interface VPC endpoints](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/centralized-access-to-vpc-private-endpoints.html#interface-vpc-endpoints) in the *AWS Whitepaper - Building a Scalable and Secure Multi-VPC AWS Network Infrastructure*.
+ **Shared VPC** – If you use a shared VPC, GuardDuty uses that shared VPC to receive runtime events from your resources after the prerequisites are met. See [Using shared VPC with Runtime Monitoring](runtime-monitoring-shared-vpc.md).
+ **Existing Amazon VPC endpoints** – An Amazon VPC that GuardDuty already set up with an Amazon VPC endpoint keeps using it. GuardDuty doesn't add link-local connectivity to that Amazon VPC until you turn Runtime Monitoring off and then on again.
+ **Endpoint policies and security groups on the endpoint** – On the link-local path, the agent's traffic does not go through an Amazon VPC endpoint, so an endpoint policy or a security group on the `guardduty-data` endpoint does not apply to it.
+ **Host-level controls** – On the link-local path, if you run host-level controls that inspect or filter the agent's traffic, or apply security group outbound rules on your hosts, allow the link-local ranges `169.254.170.248/29` (IPv4) and `fd00:ec2:6d00::/64` (IPv6).

## Related topics
<a name="runtime-monitoring-connectivity-related"></a>
+ [Deploying the security agent to Amazon EC2](how-runtime-monitoring-works-ec2.md)
+ [Deploying the security agent to Amazon EKS](how-runtime-monitoring-works-eks.md)
+ [Deploying the security agent to Amazon ECS on Fargate](how-runtime-monitoring-works-ecs-fargate.md)
+ [Reviewing runtime coverage statistics and troubleshooting issues](runtime-monitoring-assessing-coverage.md)