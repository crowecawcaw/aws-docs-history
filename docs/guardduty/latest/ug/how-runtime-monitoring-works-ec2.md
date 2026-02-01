# How Runtime Monitoring works with Amazon EC2

instances

Your Amazon EC2 instances can run multiple types of applications and workloads in your AWS
environment. When you enable Runtime Monitoring and manage the GuardDuty security agent, GuardDuty helps you
detect threats in your existing Amazon EC2 instances and potentially new ones. This feature also
supports Amazon ECS managed Amazon EC2 instances. For more see [Managed Instances support in Guardduty](guardduty_managed-instances.md "guardduty_managed-instances.md").

###### Note

Runtime Monitoring doesn't support applications running on [Amazon ECS Managed Instances](../../../AmazonECS/latest/developerguide/ManagedInstances.md "../../../AmazonECS/latest/developerguide/ManagedInstances.md").

Enabling Runtime Monitoring makes GuardDuty ready to consume runtime events from currently running and
new processes within Amazon EC2 instances. GuardDuty requires a security agent to send runtime events
from your EC2 instance to GuardDuty.

For Amazon EC2 instances, GuardDuty security agent operates at the instance level. You can decide if
you want to monitor all or selective Amazon EC2 instances in your account. If you want to manage
selective instances, the security agent is required only for these instances.

GuardDuty can also consume runtime events from new tasks and existing tasks running in Amazon EC2
instances within Amazon ECS clusters.

To install the GuardDuty security agent, Runtime Monitoring provides the following two options:

- [Use automated agent configuration
  (recommended)](#use-automated-agent-config-ec2 "#use-automated-agent-config-ec2"), or
- [Manage security agent manually](#ec2-security-agent-option2-manual "#ec2-security-agent-option2-manual")

## Use automated agent configuration through

GuardDuty (recommended)

Use automated agent configuration that permits GuardDuty to install the security agent on your
Amazon EC2 instances on your behalf. GuardDuty also manages the updates to the security agent.

By default, GuardDuty installs the security agent on all the instances in your account. If
you'd want GuardDuty to install and manage the security agent for selected EC2 instances only, add
inclusion or exclusion tags to your EC2 instances, as needed.

Sometimes, you may not want to monitor runtime events for all the Amazon EC2 instances that
belong to your account. For cases when you want to monitor the runtime events for a limited
number of instances, add an inclusion tag as `GuardDutyManaged`:`true` to
these selected instances. Starting with the availability of automated agent configuration for
Amazon EC2, if your EC2 instance has an inclusion tag
(`GuardDutyManaged`:`true`), GuardDuty will honor the tag and manage the
security agent for the selected instances even when you do not explicitly enable automated
agent configuration.

On the other hand, if there are a limited number of EC2 instances for which you don't want
to monitor runtime events, add an exclusion tag
(`GuardDutyManaged`:`false`) to these selected instances. GuardDuty will
honor the exclusion tag by **neither** installing **nor** managing the security agent for these EC2 resources.

### Impact

When you use automated agent configuration in an AWS account or an organization, you
permit GuardDuty to take the following steps on your behalf:

- GuardDuty creates one SSM association for all your Amazon EC2 instances that are SSM managed
  and appear under **Fleet Manager** in the [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/") console.
- Using inclusion tags with automated agent configuration disabled – After
  enabling Runtime Monitoring, when you don't enable automated agent configuration but add inclusion tag
  to your Amazon EC2 instance, it means that you are permitting GuardDuty to manage the security agent
  on your behalf. SSM association will then install the security agent in each instance that
  has the inclusion tag (`GuardDutyManaged`:`true`).
- If you enable automated agent configuration – The SSM association will then
  install the security agent in all the EC2 instances that belong to your account.
- Using exclusion tags with automated agent configuration – Before you enable
  automated agent configuration, when you add exclusion tag to your Amazon EC2 instance, it means
  that you are permitting GuardDuty to prevent installing and managing the security agent for this
  selected instance.

Now, when you enable automated agent configuration, the SSM association will install
and manage the security agent in all the EC2 instances except the ones that are tagged with
the exclusion tag.

- GuardDuty creates VPC endpoints in all the VPCs, including shared VPCs, as long as there is
  at least one Linux EC2 instance in that VPC that are not in the terminated or shutting-down
  instance states. This includes the centralized VPC and spoke VPCs. GuardDuty doesn't
  support creating a VPC endpoint only for the centralized VPC. For more information about how
  the centralized VPC works, see [Interface VPC endpoints](../../../whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/centralized-access-to-vpc-private-endpoints.md#interface-vpc-endpoints "../../../whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/centralized-access-to-vpc-private-endpoints.md#interface-vpc-endpoints") in the _AWS Whitepaper - Building a Scalable
  and Secure Multi-VPC AWS Network Infrastructure_.

For information about different instance states, see [Instance lifecycle](../../../AWSEC2/latest/UserGuide/ec2-instance-lifecycle.md "../../../AWSEC2/latest/UserGuide/ec2-instance-lifecycle.md") in the
_Amazon EC2 User Guide_.

GuardDuty also supports [Using shared VPC with Runtime Monitoring](runtime-monitoring-shared-vpc.md "runtime-monitoring-shared-vpc.md"). When all the prerequisites are considered
for your organization and AWS account, GuardDuty will use the shared VPC to receive runtime
events.

###### Note

There is no additional cost for the usage of the VPC endpoint.

- Along with the VPC endpoint, GuardDuty also creates a new security group. The inbound
  (ingress) rules control the traffic that's allowed to reach the resources, that are
  associated with the security group. GuardDuty adds inbound rules that match the VPC CIDR range
  for your resource, and also adapts to it when the CIDR range changes. For more information,
  see [VPC CIDR
  range](../../../vpc/latest/userguide/vpc-cidr-blocks.md "../../../vpc/latest/userguide/vpc-cidr-blocks.md") in the _Amazon VPC User Guide_.

## Manage security agent manually

There are two ways to manage the security agent for Amazon EC2 manually:

- Use GuardDuty managed documents in AWS Systems Manager to install the security agent on your Amazon EC2
  instances that are already SSM managed.

Whenever you launch a new Amazon EC2 instance, ensure that it is SSM enabled.

- Use RPM package manager (RPM) scripts to install the security agent on your Amazon EC2
  instances, whether or not they are SSM managed.

## Next step

To get started with Runtime Monitoring configuration to monitor your Amazon EC2 instances, see [Prerequisites for Amazon EC2 instance
support](prereq-runtime-monitoring-ec2-support.md "prereq-runtime-monitoring-ec2-support.md").
