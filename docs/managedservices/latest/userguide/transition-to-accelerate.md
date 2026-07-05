End of support notice: On June 30, 2027, AWS
will end support for AMS Advanced. After June 30, 2027, you will
no longer be able to access the AMS Advanced console or AMS Advanced resources.
For more information, see [AMS Advanced end of support](SunsetPlan.md "SunsetPlan.md").

# Transitioning from AMS Advanced to AMS Accelerate

AMS Advanced reaches end of support on June 30, 2027. After this date, AMS Advanced operational
capabilities will no longer function and all customers will be offboarded from the service.
Your underlying AWS infrastructure and workloads aren't affected - only the AMS Advanced
management layer is removed.

This guide helps you understand what is changing during the transition and what actions you
need to take. AMS Accelerate continues to provide incident management, patch management,
backup management, and security monitoring directly in your existing AWS accounts. Your
workloads remain in place with no migration required.

###### Topics

- [How AMS Advanced and Accelerate differ](#transition-how-differ "#transition-how-differ")
- [How the transition works](#transition-how-works "#transition-how-works")
- [How we support you through the transition](#transition-support "#transition-support")
- [What changes at a glance](#transition-changes-glance "#transition-changes-glance")
- [EC2 instance access](#transition-ec2-access "#transition-ec2-access")
- [AMS Amazon Machine Images (AMIs)](#transition-amis "#transition-amis")
- [Endpoint security](#transition-endpoint-security "#transition-endpoint-security")
- [Monitoring and alarms](#transition-monitoring "#transition-monitoring")
- [Backup management](#transition-backup "#transition-backup")
- [Change management and configuration compliance](#transition-change-mgmt "#transition-change-mgmt")
- [Patch management](#transition-patching "#transition-patching")
- [Timeline and support](#transition-timeline "#transition-timeline")
- [Related resources](#transition-related-resources "#transition-related-resources")

## How AMS Advanced and Accelerate differ

AMS Advanced uses a preventive model: you make changes to your environment exclusively
through a library of pre-vetted automated changes (change types) or by requesting manual
changes run by AMS engineers. This approach prevents risky changes from reaching
your infrastructure, but it also means you can't use your own tools (like Terraform,
AWS CloudFormation, or the AWS Management Console) to make changes directly.

AMS Accelerate uses a detect-and-respond model: you make changes directly using your
preferred tools and workflows. Rather than blocking changes upfront, Accelerate
monitors your environment and responds to risky configurations—automatically
remediating, notifying you, or reporting findings depending on how you've configured
each control. This gives you the speed and autonomy to operate at your own pace while
AMS continues to protect your environment.

Both plans share the same core operational services: monitoring, incident management,
patch management, backup management, cost optimization, reporting, and dedicated CSDM
and CA support. Some capabilities that are unique to AMS Advanced (such as the RFC system,
managed access, and endpoint security) don't carry over directly—the table in the
following section explains what's available in Accelerate and what you manage yourself.

It's also important to understand how AMS Operations engineers access your instances.
In AMS Advanced, AMS Ops connect through the same bastion infrastructure using internal
credentials. In Accelerate, AMS Ops use AWS Systems Manager Session Manager to access your instances when
needed for incident response, patching, or operational tasks. This requires the SSM agent
to be running on your instances and an IAM instance profile that authorizes communication
with the AWS Systems Manager service. AMS Accelerate provides automated instance configuration that
installs and maintains the SSM agent (and CloudWatch agent) on your EC2 instances—your CA
helps you enable this during onboarding. If you already have the SSM agent deployed and a
compatible instance profile, no additional setup is needed.

## How the transition works

We don't migrate your workloads. Your applications, data, and infrastructure stay
exactly where they are. What we do is offboard your accounts from AMS Advanced and onboard
them into Accelerate. This is an operational transition, not a workload migration.

The transition runs per account and can proceed on multiple accounts in parallel. Your
CSDM and CA coordinate the scheduling with you, selecting dates and times that work for
your operations. During the transition, the AMS Accelerate console and APIs are enabled
first, and the AMS Advanced console and APIs stop working before they're fully removed. You
should begin using the Accelerate console and APIs as soon as they're enabled. The
removal of AMS Advanced resources takes approximately two hours per account, during which the
old AMS Advanced interfaces are no longer functional. Your workloads continue running normally
throughout.

## How we support you through the transition

For the features that AMS continues to manage in Accelerate (monitoring, patching,
backup, incident management), AMS handles the migration on your behalf. This includes
deploying new configurations, applying tags, translating your alarm settings, and migrating
your maintenance windows. You also have access to AMS engineers throughout the process
for questions or issues that come up.

Your CSDM and CA are your primary contacts throughout. They help you understand what's
involved for your specific accounts, coordinate migration dates, and connect you with the
right teams when needed. We recommend completing the transition by March 31, 2027 to allow
buffer before June 30, 2027.

If you need additional hands-on help making changes, Operations on Demand gives you
access to skilled AMS engineers who can work alongside your team in 20-hour monthly
blocks. We also check in with you quarterly (September 2026, December 2026, March 2027)
to review progress, address any blockers, and adjust the plan if your timeline or
priorities shift.

## What changes at a glance

AMS Accelerate includes several capabilities not available in AMS Advanced, including
monitoring for 13+ resource types (Amazon RDS, Elastic Load Balancing, Amazon EFS, Amazon EKS, OpenSearch Service, Amazon FSx, NAT
Gateway, VPN), automated resource tagging (Resource Tagger), automated resource
scheduling for cost optimization (Resource Scheduler), and automated instance
configuration for agent deployment. These are available to you immediately after
onboarding.

The following table summarizes what's available in Accelerate and what's different
from AMS Advanced.

| Capability                                        | Available in Accelerate? | What's different                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Incident management**                           | Yes, same coverage       | AMS continues to detect, investigate, and respond to operational and security incidents on your behalf. No change to how incidents are handled.                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Monitoring**                                    | Yes, expanded coverage   | AMS monitors your resources and responds to alerts, same as today. In Accelerate, monitoring expands from EC2 and Redshift to 13+ resource types. You can also customize alarm thresholds directly in your account without submitting service requests. No action required during migration—AMS configures monitoring automatically.                                                                                                                                                                                                                      |
| **Security monitoring (GuardDuty)**               | Yes, same coverage       | AMS continues to monitor and respond to GuardDuty findings and providing help in case of security incidents. No action required.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Patch management**                              | Yes, same coverage       | Your maintenance windows, schedules, and baselines are preserved. To create or modify maintenance windows, you can self-service directly through AWS Systems Manager (changes apply immediately) or submit a service request through the Accelerate console.                                                                                                                                                                                                                                                                                              |
| **Backup management**                             | Yes, same coverage       | Your recovery points and backup history are preserved. AMS Accelerate continues to manage backups with no gap in coverage. You can configure backup policies, retention periods, and vault settings directly through AWS Backup.                                                                                                                                                                                                                                                                                                                          |
| **Cost optimization**                             | Yes, same coverage       | No change to coverage. You manage optimization actions directly instead of through RFCs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Reporting**                                     | Yes, same coverage       | Reports transition to the Accelerate reporting framework. Historical data is retained.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Configuration compliance (detective controls)** | Yes, expanded coverage   | Replaces the AMS Advanced change management preventive model with continuous compliance monitoring. AMS deploys a library of AWS Config rules aligned to CIS and NIST standards that continuously evaluate your resource configurations. You configure how AMS responds to each finding: auto-remediate, notify, or report. Accelerate includes approximately 87 rules with broader coverage than AMS Advanced, including net-new checks for IAM, networking, storage, database, serverless, and encryption. Additional controls will be added over time. |
| **CSDM and CA support**                           | Yes, same coverage       | No change. Your CSDM and CA remain your primary contacts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **EC2 instance access**                           | Customer-managed         | You connect directly using your AD credentials over your existing network. AMS-managed bastion hosts are decommissioned. You can deploy your own bastions or use Session Manager.                                                                                                                                                                                                                                                                                                                                                                         |
| **Endpoint security**                             | Customer-managed         | You choose your own endpoint security vendor (including Trend Micro Vision One) and manage agent lifecycle. Customers who want AMS to monitor third-party security alerts can onboard to AWS Security Incident Response (SIR) at no additional cost—it's included for AMS customers.                                                                                                                                                                                                                                                                      |
| **Change management (RFC system)**                | Not available            | The RFC system is not part of Accelerate. You use your preferred tools (Console, CLI, Terraform, AWS CloudFormation) directly. Configuration compliance monitors for risky changes after the fact. Operations on Demand is available if you need assisted change management.                                                                                                                                                                                                                                                                              |
| **Landing zone management**                       | Customer-managed         | For MALZ customers, core accounts (Management, Shared Services, Networking, Security, Logging) are handed over to you. AMS removes AMS-managed infrastructure from these accounts during offboarding. Your VPCs, subnets, and network configurations remain in place and are yours to manage.                                                                                                                                                                                                                                                             |
| **AMS AMIs**                                      | Not available            | AMS no longer produces monthly AMIs. Use standard AWS AMIs and EC2 Image Builder for your own pipelines. Operations on Demand offers managed AMI building if you have custom needs.                                                                                                                                                                                                                                                                                                                                                                       |

## EC2 instance access

In AMS Advanced, instance access follows a prescriptive model: you connect through
AMS-managed bastion hosts, use AMS-managed Active Directory for authentication, and
request access through RFCs. AMS controls who can reach which instances and for how long.

In AMS Accelerate, you choose your own access method. There's no prescribed path—you
can use AWS Systems Manager Session Manager, direct RDP/SSH over your corporate network, or any other approach that
fits your security requirements.

As part of the transition, we remove the AMS bastion hosts and hand over the Active
Directory infrastructure to you. Your existing instances remain domain-joined and accessible
with your AD credentials—we've validated this with zero access downtime. You can
continue using AD as your long-term access method if it works for your organization, or you
can use it temporarily while you configure a different approach. Either way, the AD trust,
network connectivity, and domain configuration are yours to keep.

###### What you need to do

For existing instances, you need to add your corporate users or groups to the AMS AD
access groups so that they have persistent access. In AMS Advanced, the RFC process granted
temporary 8-hour access windows. Post-transition, that automation is no longer
available—instead, you add your users as permanent members of the access groups.
We provide guidance on which groups to add your users to and the tools to do so.

After users are provisioned, they connect directly over your existing network path (Direct
Connect, VPN, or Transit Gateway) using their AD credentials.

For new instances, the AMS bootstrap script no longer runs on boot, so two things that
were previously automatic now need configuration:

- **Domain join** – New instances don't
  automatically join the domain. We recommend configuring automated domain join using
  AWS Directory Service seamless join or SSM State Manager. See
  [Joining
  an instance to your directory](../../../directoryservice/latest/admin-guide/ms_ad_join_instance.md "../../../directoryservice/latest/admin-guide/ms_ad_join_instance.md") in the _AWS Directory Service Administration Guide_.
- **Local group configuration** – New
  instances need the AD access groups added to the local administrator groups so that
  group members get admin access. We provide guidance on configuring this using GPO or
  SSM State Manager—both apply automatically to new instances without per-instance
  setup.

**Access administration:** You take ownership of who has
access to your instances. We provide you with an AD admin account, an admin workstation,
and automation tools for user provisioning. You decide your access policy—whether
that's permanent group membership, time-limited access through your own governance
tooling, or Session Manager IAM policies.

## AMS Amazon Machine Images (AMIs)

In AMS Advanced, AMS produces updated AMIs every month for supported operating systems,
pre-configured with management software, security agents, and domain-join scripts. These
AMIs are shared to your accounts and used when launching new EC2 instances through the
change management system.

AMS AMI production is not part of AMS Accelerate. After the transition, AMS no longer
produces or shares monthly AMIs to your accounts. For new instance launches and Auto Scaling
group (ASG) launch configurations, use the standard AWS-provided AMIs for your operating
system (available in the EC2 console or through the
[AWS AMI catalog](../../../AWSEC2/latest/UserGuide/finding-an-ami.md "../../../AWSEC2/latest/UserGuide/finding-an-ami.md")).
These are maintained by AWS with regular security updates and are the recommended base for
all new instances. If you use ASGs that reference AMS AMIs in their launch templates, update
those references to standard AWS AMIs or your own custom AMIs to ensure new instances
launched by scaling events use a supported image.

Existing AMS AMIs that have already been shared are not immediately unshared during
offboarding. However, AMIs created before June 30, 2026 will be deprecated on June 30, 2027.
AMIs created between June 30, 2026 and June 30, 2027 will continue to be shared for one year
after June 30, 2027.

If you have custom AMI requirements beyond what standard AWS AMIs provide (for example,
pre-baked applications, hardened configurations, or organization-specific tooling), you can
build your own pipeline using
[EC2 Image Builder](../../../imagebuilder/latest/userguide/what-is-image-builder.md "../../../imagebuilder/latest/userguide/what-is-image-builder.md").
If you'd prefer AMS to manage this for you, the Operations on Demand catalog includes an
AMI Building and Vending offering. Talk to your CSDM to explore this option.

## Endpoint security

In AMS Advanced, AMS deploys and manages Trend Micro endpoint security on your EC2
instances. This includes agent installation (automated through boot scripts on every
instance launch), agent activation, event monitoring, and incident creation. AMS manages
this infrastructure through the Deep Security Manager (DSM), Cloud One, or Vision One
platform depending on your account configuration.

As part of the transition, you choose your endpoint security path: continue with Trend
Micro by moving to Vision One (a fully SaaS platform hosted by Trend Micro that eliminates
the on-premises DSM infrastructure), or move to a different security vendor of your choice.
Either way, you take ownership of the agent lifecycle with your chosen vendor—deploying
agents, managing licenses, and configuring activation. This must be completed before the
transition to Accelerate, because AMS offboards the EPS stack during migration and
the boot scripts will no longer install or activate the Trend Micro agent on instance launch.

###### Option 1: Continue with Trend Micro Vision One (SaaS)

Vision One is the cloud-native Trend Micro platform that integrates with AWS Security Hub.
AMS assists with migrating you from your current platform (DSM or Cloud One) to Vision
One before offboarding. Once on Vision One, you work directly with Trend Micro for agent
lifecycle management. If you currently use DSM, the migration path is sequential: DSM to
Cloud One, then Cloud One to Vision One. With Vision One, security alerts are sent to
AWS Security Hub. Customers who also onboard to AWS Security Incident Response (SIR) get continued event
monitoring and incident response through AWS.

###### Option 2: Use a different endpoint security solution

You select, deploy, and manage an endpoint security solution of your choice. AMS
removes the Trend Micro agents from your instances and offboards the EPS stack. You're
responsible for standing up and running your chosen vendor. You can optionally integrate
your chosen solution with AWS Security Hub for SIR coverage.

With either option, you take ownership of the full agent lifecycle going forward:
deploying agents to your instances (using your own automation, SSM State Manager, custom
AMIs, or a configuration management tool), maintaining your vendor license and activation
credentials, and configuring event monitoring through your vendor's dashboard or
AWS Security Hub.

###### Note

If you currently use DSM and want to continue with Trend Micro, start planning
early. The migration path (DSM to Cloud One to Vision One) is sequential and takes the
most lead time.

## Monitoring and alarms

In AMS Advanced, the alarm manager creates CloudWatch alarms for all managed EC2 instances
automatically, and you submit service requests to change thresholds. In AMS Accelerate,
AMS continues to create and manage alarms on your behalf, but the model is
tag-driven—AMS monitors instances that have a monitoring tag applied—and you
customize thresholds directly in your account through AWS AppConfig without submitting service
requests. The coverage also expands from EC2 and Redshift to 13+ resource types including
Amazon RDS, Elastic Load Balancing, Amazon EFS, Amazon EKS, OpenSearch Service, Amazon FSx, NAT Gateway, and VPN.

###### What you need to do

No manual action is required for monitoring continuity. AMS applies monitoring
tags to your existing EC2 instances during migration and translates your current alarm
customizations into the Accelerate configuration format. Your CA reviews the
translated configuration with you before migration begins.

###### What changes

Alarm names and default thresholds differ between AMS Advanced and Accelerate
(AMS Advanced defaults at ~85%, Accelerate at ~95% to reduce alert noise). If you have
dashboards, runbooks, or alert routing that reference specific alarm names, update them
after migration. Three AMS Advanced-specific alarms (Log Agent Hard Failure, Root Volume
Inode Usage, Broken Secure Channel) that monitor AMS Advanced-specific infrastructure are
removed and not carried over to Accelerate. After the transition, new EC2 instances
need to be tagged to receive monitoring coverage—use AMS Resource Tagger to
apply tags automatically based on rules you define, or apply them manually.

## Backup management

Your existing recovery points remain intact and accessible throughout the
transition—there is no gap in backup coverage and no data is deleted. You can
continue to restore from any existing recovery point as needed.

After the transition, AMS Accelerate protects your resources through AWS Backup with
managed plans, schedules, and vaults. Your backup schedules and retention periods remain
consistent with your current configuration. Depending on your account's existing backup
configuration, Accelerate may create new vaults with updated names rather than reusing
existing ones—in that case, your historical recovery points remain available in the
original vaults while new backups are written to the new ones.

You can configure retention periods, schedules, vault settings, and encryption keys
directly through the AWS Backup console or your preferred infrastructure-as-code tooling.
If any of your vaults have Vault Lock enabled, locked recovery points are retained
according to their configured retention period.

###### What you need to do

No action is required to maintain backup continuity.

## Change management and configuration compliance

In AMS Advanced, the change management system controls what happens in your environment. You
submit requests for change (RFCs) from a library of pre-vetted change types, and AMS
runs them on your behalf. For changes that aren't automated, AMS engineers review and
perform them manually. This preventive model ensures that only approved, tested changes reach
your infrastructure, but it also means you can't use native AWS tools (Console, CLI,
Terraform, AWS CloudFormation) to make changes directly.

In AMS Accelerate, you make changes directly using whatever tools and workflows you prefer.
The RFC system doesn't exist in Accelerate. Instead, AMS protects your environment
through configuration compliance—a library of AWS Config rules that continuously evaluates
your resource configurations against security and operational best practices. This is the
detect-and-respond model: rather than blocking changes before they happen, AMS detects
risky configurations after they're applied and responds according to rules you control.

###### How configuration compliance works in Accelerate

You configure response levels with your CA during onboarding, and you can adjust them
at any time:

- _Auto-remediate_ – AMS automatically corrects the
  non-compliant configuration (for example, re-enabling VPC Flow Logs if they're
  disabled).
- _Notify_ – AMS alerts you of the finding so you
  can investigate and decide how to respond.
- _Report_ – AMS records the finding and includes it
  in your monthly business review for visibility without immediate action.

###### What's covered

Accelerate includes approximately 87 AWS Config rules covering IAM and access controls,
network and VPC security, encryption (EBS, Amazon RDS, Amazon S3), logging and audit trail
integrity, database and storage configurations, and serverless resources. This is
broader coverage than AMS Advanced, which deployed approximately 24-27 rules (depending on
SALZ or MALZ) with many tied to enforcing AMS-internal service behavior rather than
customer security posture. Additional controls are added over time as new AWS services
and compliance standards are supported.

###### What you need to do

No action is required for the transition. AMS deploys the AWS Config rules during
Accelerate onboarding. Your CA walks you through the available rules and helps you
configure the response level for each one. If you currently have custom AWS Config rules
deployed in your AMS Advanced accounts, those are retained—they aren't removed during
offboarding.

###### What changes for customers who relied on the RFC system for governance

If your organization used the RFC system as a governance control (for example,
requiring approval workflows before changes are made), you need to implement equivalent
controls using your own tooling. Common approaches include AWS Service Control
Policies (SCPs) to enforce permission boundaries, AWS CloudTrail with alerting for sensitive
API calls, and approval workflows in your CI/CD pipeline or change management tool
(ServiceNow, Jira, etc.). Your CA can help you identify which governance patterns map
to your current RFC-based workflows.

For customers who need hands-on help making changes, Operations on Demand provides
curated change support through skilled AMS engineers in 20-hour monthly blocks. This is
useful during the transition period while you build familiarity with direct access, or on an
ongoing basis for complex changes where you want expert support.

## Patch management

In AMS Advanced, patch management uses the AMS Patch Orchestrator with maintenance windows
configured through the RFC system. AMS manages patch baselines, scheduling, notifications,
and the default maintenance window. Custom maintenance windows are created and updated through
change types.

In AMS Accelerate, your patching schedule, baselines, and maintenance windows are preserved
through the transition. The same tag-based patching model applies, and your instances continue
to be patched on the same schedule. Some operational details change (notification delivery, how
the default maintenance window is managed, and the change process), but your patching behavior
remains consistent.

###### What you need to do

Before the migration begins, your CSDM and CA confirm your notification email addresses
for patch events, since notifications transition from the AMS Advanced delivery model to the
Accelerate notification framework and we need to ensure you continue receiving them at
the right addresses. They also confirm whether you want to retain your existing patch
compliance reporting history.

###### What happens during migration

The migration is scheduled outside any active maintenance window run. No patches
run during the transition window. Your existing maintenance windows, patch baselines,
schedules, and per-OS configurations are migrated to the Accelerate infrastructure.
The maintenance window names and behavior are preserved so your operational processes
remain consistent.

###### What changes

The following operational details change after migration:

- **Maintenance window notifications** –
  Patch event notifications transition from the AMS Advanced SNS-based notification model to
  the Accelerate notification framework. Your notification email addresses are
  preserved.
- **Default maintenance window** – If you use
  the AMS default maintenance window, it's migrated to a standalone configuration that
  you own. Instances tagged `AMSDefaultPatchGroup: True` continue to be patched
  on the same schedule.
- **Auto-tagging** – The automatic patch
  group tagging maintenance window (which tags new instances with
  `AMSDefaultPatchGroup: True`) is deprecated. If you need automatic tagging
  for new instances, AMS Resource Tagger is the self-service replacement.
- **Patch reporting** – Your patch compliance
  reports transition to the Accelerate reporting model. Historical patch data is
  retained.
- **Change process** – You no longer use the
  RFC system to create or modify maintenance windows. In Accelerate, you manage
  maintenance windows directly through the AWS Systems Manager console, API, or
  infrastructure-as-code.

**Continuity:** Your patching doesn't stop during the
transition. The migration is sequenced so that your maintenance windows and baselines are
functional on the Accelerate side before the AMS Advanced infrastructure is removed. If any
issue is detected, the migration can be reversed to restore AMS Advanced patching.

## Timeline and support

We recommend completing your transition by March 31, 2027 to allow buffer before the
June 30, 2027 shutdown. Your CSDM and CA are your primary points of contact throughout
the transition and will help you create a plan tailored to your environment.

For customers who need assistance making changes during the transition period,
Operations on Demand provides curated change support in monthly blocks.

AMS conducts quarterly checkpoints (September 2026, December 2026, March 2027)
to monitor migration progress and provide additional support where needed.

## Related resources

- [AMS Accelerate operations plan](../accelerate-guide/what-is-acc.md "../accelerate-guide/what-is-acc.md")
- [AWS Systems Manager Session Manager](../../../systems-manager/latest/userguide/session-manager.md "../../../systems-manager/latest/userguide/session-manager.md")
- [Offboard from multi-account landing zone](offboarding-malz.md "offboarding-malz.md")
- [Offboard from single-account landing zone](offboarding-salz.md "offboarding-salz.md")
- [Operations on Demand](ops-on-demand.md "ops-on-demand.md")
