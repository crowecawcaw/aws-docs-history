

# How the security agent connects to GuardDuty
<a name="runtime-monitoring-agent-connectivity"></a>

The Runtime Monitoring security agent delivers runtime events to GuardDuty. The data remains within the AWS network. There is no additional cost for the connectivity that GuardDuty configures. To authenticate the agent, GuardDuty uses [Instance identity roles](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html#ec2-instance-identity-roles). For Amazon ECS on Fargate, GuardDuty uses the task execution role; see [Permissions requirements](prereq-runtime-monitoring-ecs-support.md#ecs-runtime-permissions-requirements).

GuardDuty supports two connectivity methods: link-local and Amazon VPC endpoint. The security agent attempts to connect using these methods to deliver runtime events to GuardDuty.

With automated agent configuration, GuardDuty establishes connectivity automatically. If you manage the agent manually, you need to create an Amazon VPC endpoint.

## Link-local connectivity
<a name="runtime-monitoring-connectivity-link-local"></a>

The agent connects to the GuardDuty backend over a link-local address, at `guardduty-data-v2.{{us-east-1}}.amazonaws.com`. Link-local connectivity doesn't use private DNS. The AWS Region ({{us-east-1}}) changes based on your Region.

## Amazon VPC endpoint connectivity
<a name="runtime-monitoring-connectivity-vpc-endpoint"></a>

The agent connects to the GuardDuty backend through an Amazon VPC endpoint. It resolves and connects to the endpoint's private DNS name. For a non-FIPS endpoint, this is `guardduty-data.{{us-east-1}}.amazonaws.com`. The AWS Region ({{us-east-1}}) changes based on your Region.

The resource must have a valid network path to an active `guardduty-data` Amazon VPC endpoint. GuardDuty selects the subnet based on IP availability, so for advanced network topologies, validate that connectivity is possible.

## Prerequisites
<a name="runtime-monitoring-connectivity-prerequisites"></a>

For prerequisites, see [Prerequisites to enabling Runtime Monitoring](runtime-monitoring-prerequisites.md).

## Considerations
<a name="runtime-monitoring-connectivity-considerations"></a>
+ **All VPCs** – With automated agent configuration, GuardDuty sets up connectivity across all your VPCs, including centralized and spoke VPCs. For more information about centralized VPCs, see [Interface VPC endpoints](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/centralized-access-to-vpc-private-endpoints.html#interface-vpc-endpoints) in the *AWS Whitepaper - Building a Scalable and Secure Multi-VPC AWS Network Infrastructure*.
+ **Shared VPC** – If you use a shared VPC, GuardDuty uses that shared VPC to receive runtime events from your resources after the prerequisites are met. See [Using shared VPC with Runtime Monitoring](runtime-monitoring-shared-vpc.md).

## Related topics
<a name="runtime-monitoring-connectivity-related"></a>
+ [Deploying the security agent to Amazon EC2](how-runtime-monitoring-works-ec2.md)
+ [Deploying the security agent to Amazon EKS](how-runtime-monitoring-works-eks.md)
+ [Deploying the security agent to Amazon ECS on Fargate](how-runtime-monitoring-works-ecs-fargate.md)
+ [Reviewing runtime coverage statistics and troubleshooting issues](runtime-monitoring-assessing-coverage.md)