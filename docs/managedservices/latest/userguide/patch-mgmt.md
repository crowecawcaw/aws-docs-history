# Patch management in AMS

###### Topics

- [AMS Patch Orchestrator: a tag-based patching model](patch-orchestrator.md "patch-orchestrator.md")
- [Using Patch Orchestrator](patch-orchestrator-using.md "patch-orchestrator-using.md")
- [On-demand patching](#patching-on-demand "#patching-on-demand")
- [AMS standard patching](patch-overview.md "patch-overview.md")
- [Patching service commitments](patching-service-commitments.md "patching-service-commitments.md")
  In AMS, patch management is a service that helps you maintain OS vendor updates on your
  Amazon Elastic Compute Cloud (Amazon EC2) instances. You have the freedom to customize the
  frequency and process of patching your Amazon EC2 instances.

You configure patch management during onboarding, and you can update it by using the RFC
process. Stacks created using the change management system and a patch-compatible template
(for Amazon EC2, Auto Scaling group, HA one-tier or two-tier stack) are subscribed to patch management automatically.

AMS provides a feature, Patch Orchestrator – tag-based patching, for configuring patching.

For definitions of patching terms, see [AMS key terms](key-terms.md "key-terms.md").

###### Important

- It's not possible for stacks or a stack's constituent instances to opt out of
  patch management, if the AMS template from which the stack is created is
  compatible with patch management. Currently, patching is compatible with the following stack templates:
  - Amazon EC2 stack | Create, and Amazon EC2 stack | Create (with additional volumes)
  - Amazon EC2 instance launched with CloudFormation ingest
  - Auto Scaling group | Create (the Amazon EC2 instances in the group are patched)
  - High Availability One-Tier stack | Create, and High Availability Two-Tier stack | Create

- If there is an ongoing incident that affects a stack, AMS operators can reschedule or cancel scheduled patching.
- By default, all instances within a particular patch-compatible stack are
  patched in-place. To patch Auto Scaling groups with an Amazon Machine Image
  (AMI) replacement using the latest/patched AMS AMI, submit a service request.
  Updated AMIs are shared to accounts every month.

###### Important

You can specify alternative patch repositories for managed nodes. While AMS
implements your requested patch configurations, you are responsible for selecting and
validating the security of your chosen repositories. You must also accept any risks from
using these repositories, such as supply chain risks.

The following are best practices for the security of your patch management process:

- Use only trusted, verified repository sources
- Default to standard OS vendor repositories when possible
- Regularly audit custom repository configurations

###### Tip

AMS recommends that you enable backups for instances that have valuable applications
or services. For information about enabling backups,
see [Continuity management in AMS Advanced](continuity-mgmt.md "continuity-mgmt.md").

## On-demand patching

AMS has a change type that works with your patch baseline, to enable you to run a
patch on instances on demand. This can be either the default baseline you set at on
boarding, or the Patch Orchestrator Systems Manager patch baseline that you set with the Patch
Baseline change type (CT ID varies per operating system).

You can use the on-demand patching change type with or without Patch
Orchestrator.

For information about using this change type, see
[On Demand Patching | Run](../ctref/management-patching-on-demand-patching-run.md "../ctref/management-patching-on-demand-patching-run.md").

###### Note

You can't use instances that are part of an Auto Scaling group in an on-demand patching change type.
