# Migrating from Amazon EC2 manual agent to

automated agent

This section applies to your AWS account if you were previously managing the security agent
manually and now want to use the GuardDuty automated agent configuration. If this doesn't apply to
you, continue with configuring the security agent for your account.

When you enable GuardDuty automated agent, GuardDuty manages the security agent on your behalf. For
information about what steps does GuardDuty take, see [Use automated agent configuration
(recommended)](how-runtime-monitoring-works-ec2.md#use-automated-agent-config-ec2 "how-runtime-monitoring-works-ec2.md#use-automated-agent-config-ec2").

## Clean up resources

**Delete SSM association**

- Delete any SSM association that you may have created when you were managing the
  security agent for Amazon EC2 manually. For more information, see [Deleting associations](../../../systems-manager/latest/userguide/systems-manager-state-manager-delete-association.md "../../../systems-manager/latest/userguide/systems-manager-state-manager-delete-association.md").
- This is done so that GuardDuty can take over the management of SSM actions whether you use
  automated agents at the account level or instance level (by using inclusion or exclusion
  tags). For more information about what SSM actions can GuardDuty take, see [Service-linked role permissions for GuardDuty](slr-permissions.md "slr-permissions.md").
- When you delete an SSM association that was previously created for managing the
  security agent manually, there might be a brief period of overlap when GuardDuty creates an SSM
  association for managing the security agent automatically. During this period, you could
  experience conflicts based on SSM scheduling. For more information, see [Amazon EC2 SSM scheduling](../../../systems-manager/latest/userguide/quick-setup-scheduler.md "../../../systems-manager/latest/userguide/quick-setup-scheduler.md").

**Manage inclusion and exclusion tags for your Amazon EC2
instances**

- **Inclusion tags** – When you don't enable GuardDuty
  automated agent configuration but tag any of your Amazon EC2 instances with an inclusion tag
  (`GuardDutyManaged`:`true`), GuardDuty creates an SSM association that
  will install and manage the security agent on the selected EC2 instances. This is an
  expected behavior that helps you manage the security agent on selected EC2 instances only.
  For more information, see [How Runtime Monitoring works with Amazon EC2
  instances](how-runtime-monitoring-works-ec2.md "how-runtime-monitoring-works-ec2.md").

To prevent GuardDuty from installing and managing the security agent, remove the inclusion
tag from these EC2 instances. For more information, see [Add and delete
tags](../../../AWSEC2/latest/UserGuide/Using_Tags.md#adding-or-deleting-tags "../../../AWSEC2/latest/UserGuide/Using_Tags.md#adding-or-deleting-tags") in the _Amazon EC2 User Guide_.

- **Exclusion tags** – When you want to enable GuardDuty
  automated agent configuration for all the EC2 instances in your account, make sure that no
  EC2 instance is tagged with an exclusion tag
  (`GuardDutyManaged`:`false`).
