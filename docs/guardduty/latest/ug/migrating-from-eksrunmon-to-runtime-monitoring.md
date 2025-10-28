# Migrating from EKS Runtime Monitoring to

Runtime Monitoring

With the launch of GuardDuty Runtime Monitoring, the threat detection coverage has been expanded to Amazon ECS
containers and Amazon EC2 instances. EKS Runtime Monitoring experience has now been consolidated into Runtime Monitoring.
You can enable Runtime Monitoring and manage individual GuardDuty security agents for each resource type
(Amazon EC2 instance, Amazon ECS cluster, and Amazon EKS cluster) for which you want to monitor the runtime
behavior.

GuardDuty has consolidated the console experience for EKS Runtime Monitoring into Runtime Monitoring.
GuardDuty recommends [Checking EKS Runtime Monitoring configuration
status](checking-eks-runtime-monitoring-enable-status.md "checking-eks-runtime-monitoring-enable-status.md") and
Migrating from EKS Runtime Monitoring to
Runtime Monitoring.

As a part of migrating to Runtime Monitoring, ensure to [Disable
EKS Runtime Monitoring](disabling-eks-runtime-monitoring.md "disabling-eks-runtime-monitoring.md"). This is important
because if you later choose to disable Runtime Monitoring and you do not disable EKS Runtime Monitoring,
you will continue incurring usage cost for EKS Runtime Monitoring.

###### To migrate from EKS Runtime Monitoring to Runtime Monitoring

1. The GuardDuty console supports EKS Runtime Monitoring as a part of Runtime Monitoring.

You can start using Runtime Monitoring by [Checking EKS Runtime Monitoring configuration
status](checking-eks-runtime-monitoring-enable-status.md "checking-eks-runtime-monitoring-enable-status.md") of your organization and
accounts.

Make sure to not disable EKS Runtime Monitoring before enabling Runtime Monitoring. If you disable
EKS Runtime Monitoring, the Amazon EKS add-on management will also get disabled. Continue with the following
steps in the listed order. 2. Make sure you meet all the [Prerequisites to enabling Runtime Monitoring](runtime-monitoring-prerequisites.md "runtime-monitoring-prerequisites.md"). 3. Enable Runtime Monitoring by replicating the same organization configuration settings for Runtime Monitoring
as you have for EKS Runtime Monitoring. For more information, see [Enabling
Runtime Monitoring](runtime-monitoring-configuration.md "runtime-monitoring-configuration.md").

    * If you have a standalone account, you need to enable Runtime Monitoring.


    If your GuardDuty security agent is deployed already, the corresponding settings are
     replicated automatically and you don't need to configure the settings again.
    * If you have an organization with auto-enablement settings, make sure to replicate
     the same auto-enablement settings for Runtime Monitoring.
    * If you have an organization with settings configured for existing active member
     accounts individually, make sure to enable Runtime Monitoring and configure the GuardDuty security
     agent for these members individually.

4. After you have ensured that the Runtime Monitoring and GuardDuty security agent settings are correct,
   [disable EKS Runtime Monitoring](disabling-eks-runtime-monitoring.md "disabling-eks-runtime-monitoring.md")
   by using either the API or the AWS CLI command.
5. (Optional) if you want to clean any resource associated with the GuardDuty security agent,
   see [Disabling, uninstalling, and
   cleaning up resources in Runtime Monitoring](runtime-monitoring-agent-resource-clean-up.md "runtime-monitoring-agent-resource-clean-up.md").
   If you want to continue using EKS Runtime Monitoring without enabling Runtime Monitoring, see [EKS Runtime Monitoring in GuardDuty](eks-runtime-monitoring-guardduty.md "eks-runtime-monitoring-guardduty.md").
   Based on your use case, choose the steps to configure EKS Runtime Monitoring for a standalone account or
   for multiple member accounts.
