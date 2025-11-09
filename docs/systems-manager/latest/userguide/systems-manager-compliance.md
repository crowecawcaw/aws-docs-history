AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# AWS Systems Manager Compliance

You can use Compliance, a tool in AWS Systems Manager, to scan your fleet of managed nodes for patch
compliance and configuration inconsistencies. You can collect and aggregate data from
multiple AWS accounts and Regions, and then drill down into specific resources that aren’t
compliant. By default, Compliance displays current compliance data about patching in
Patch Manager and associations in State Manager. (Patch Manager and State Manager are also both tools in
AWS Systems Manager.) To get started with Compliance, open the [Systems Manager console](https://console.aws.amazon.com/systems-manager/compliance "https://console.aws.amazon.com/systems-manager/compliance"). In the navigation pane, choose
**Compliance**.

Patch compliance data from Patch Manager can be sent to AWS Security Hub. Security Hub gives you a
comprehensive view of your high-priority security alerts and compliance status. It also
monitors the patching status of your fleet. For more information, see [Integrating Patch Manager with
AWS Security Hub](patch-manager-security-hub-integration.md "patch-manager-security-hub-integration.md").

Compliance offers the following additional benefits and features:

- View compliance history and change tracking for Patch Manager patching data and
  State Manager associations by using AWS Config.
- Customize Compliance to create your own compliance types based on your IT or
  business requirements.
- Remediate issues by using Run Command, another tool in AWS Systems Manager, State Manager, or
  Amazon EventBridge.
- Port data to Amazon Athena and Amazon Quick Suite to generate fleet-wide reports.

###### EventBridge support

This Systems Manager tool is supported as an _event_ type in Amazon EventBridge rules.
For information, see [Monitoring Systems Manager events with
Amazon EventBridge](monitoring-eventbridge-events.md "monitoring-eventbridge-events.md") and [Reference: Amazon EventBridge event patterns and types
for Systems Manager](reference-eventbridge-events.md "reference-eventbridge-events.md").

###### Chef InSpec integration

Systems Manager integrates with [Chef
InSpec](https://www.chef.io/inspec/ "https://www.chef.io/inspec/"). InSpec is an open-source, runtime framework that allows
you to create human-readable profiles on GitHub or Amazon Simple Storage Service (Amazon S3). You
can then use Systems Manager to run compliance scans and view compliant and noncompliant managed
nodes. For more information, see [Using Chef InSpec profiles
with Systems Manager Compliance](integration-chef-inspec.md "integration-chef-inspec.md").

###### Pricing

Compliance is offered at no additional charge. You only pay for the AWS resources
that you use.

###### Contents

- [Getting started with Compliance](compliance-prerequisites.md "compliance-prerequisites.md")
- [Configuring permissions for Compliance](compliance-permissions.md "compliance-permissions.md")
- [Creating a resource data sync for
  Compliance](compliance-datasync-create.md "compliance-datasync-create.md")
- [Learn details about Compliance](compliance-about.md "compliance-about.md")
- [Deleting a resource data sync
  for Compliance](systems-manager-compliance-delete-RDS.md "systems-manager-compliance-delete-RDS.md")
- [Remediating compliance issues using EventBridge](compliance-fixing.md "compliance-fixing.md")
- [Assign custom compliance metadata using
  the AWS CLI](compliance-custom-metadata-cli.md "compliance-custom-metadata-cli.md")
