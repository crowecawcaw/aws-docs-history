# Managing security agent manually for

Amazon EKS cluster

This section describes how you can manage your Amazon EKS add-on agent (GuardDuty agent) after you
enable Runtime Monitoring (or EKS Runtime Monitoring). To use Runtime Monitoring, you must enable Runtime Monitoring and configure
the Amazon EKS add-on, `aws-guardduty-agent`. You require to perform both the steps
for GuardDuty to detect potential threats and generate [GuardDuty Runtime Monitoring finding types](findings-runtime-monitoring.md "findings-runtime-monitoring.md").

For managing the agent manually, you need to create a VPC endpoint as a prerequisite. This
helps GuardDuty receive the runtime events. After
this, you can install the security agent so that GuardDuty will start
receiving the runtime events from the Amazon EKS resources. When
GuardDuty releases a new agent version for this resource, you can update the agent version in
your account.

###### Topics

- [Prerequisite – Creating
  an Amazon VPC endpoint](eksrunmon-prereq-deploy-security-agent.md "eksrunmon-prereq-deploy-security-agent.md")
- [Installing GuardDuty security agent
  manually on Amazon EKS resources](eksrunmon-deploy-security-agent.md "eksrunmon-deploy-security-agent.md")
- [Updating security agent
  manually for Amazon EKS resources](eksrunmon-update-security-agent.md "eksrunmon-update-security-agent.md")
