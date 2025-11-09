AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Diagnosing and remediating

Using the unified Systems Manager console, you can identify problems across your fleet in a single
diagnosis operation. For organizations, you can then attempt remediation on all or only
select targets using a single Automation operation. For an organization, as a delegated
account administrator, you can select targets across all accounts and Regions. If you are
working in a single account, you can select targets in a single Region at a time.

Systems Manager can diagnose and help you remediate several types of deployment failures, as well as
drifted configurations. Systems Manager can also identify Amazon Elastic Compute Cloud (Amazon EC2) instances in your account
or organization that Systems Manager isn't able to treat as a _managed
node_. The EC2 instance diagnosis process can identify issues related to
misconfigurations for a virtual private cloud (VPC), in a Domain Name Service (DNS) setting,
or in an Amazon Elastic Compute Cloud (Amazon EC2) security group.

###### Note

Systems Manager supports both EC2 instances and other machine types in a [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types") environment
as _managed nodes_. To be a managed node, AWS Systems Manager
Agent (SSM Agent) must be installed on the machine, and Systems Manager must have permission to
perform actions on the machine.

For EC2 instances, this permission can be provided at the account level using an
AWS Identity and Access Management (IAM) role, or at the instance level using an instance profile. For more
information, see [Configure instance permissions required for
Systems Manager](setup-instance-permissions.md "setup-instance-permissions.md").

For non-EC2 machines, this permission is provided using an IAM service role. For
more information, see [Create the IAM service role required
for Systems Manager in hybrid and multicloud environments](hybrid-multicloud-service-role.md "hybrid-multicloud-service-role.md").

###### Before you begin

In order to use the **Diagnose and remediate** feature to detect
unmanaged EC2 instances, you must first onboard your organization or account to the
unified Systems Manager console. During this process, you must choose the option to create IAM
roles and managed policies required for these operations. For more information, see
[Setting up Systems Manager unified console
for an organization](systems-manager-setting-up-organizations.md "systems-manager-setting-up-organizations.md").

Use the following topics to help you identify and fix certain common types of failed
deployments, drifted configurations, and unmanaged EC2 instances.

###### Topics

- [Diagnosing and remediating failed
  deployments](remediating-deployment-issues.md "remediating-deployment-issues.md")
- [Diagnosing and remediating drifted
  configurations](remediating-configuration-drift.md "remediating-configuration-drift.md")
- [Diagnosing and remediating unmanaged
  Amazon EC2 instances in Systems Manager](remediating-unmanaged-instances.md "remediating-unmanaged-instances.md")
- [Remediation impact types of runbook
  actions](remediation-impact-type.md "remediation-impact-type.md")
- [Viewing execution progress
  and history for remediations in Systems Manager](diagnose-and-remediate-execution-history.md "diagnose-and-remediate-execution-history.md")
