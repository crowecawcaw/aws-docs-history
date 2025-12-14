# Security Hub CSPM controls for Systems Manager

These AWS Security Hub CSPM controls evaluate the AWS Systems Manager (SSM) service and resources. The
controls might not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [SSM.1] Amazon EC2 instances should be managed by AWS Systems Manager

**Related requirements:** PCI DSS v3.2.1/2.4,
NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2, NIST.800-53.r5 CM-2(2), NIST.800-53.r5
CM-8, NIST.800-53.r5 CM-8(1), NIST.800-53.r5 CM-8(2), NIST.800-53.r5 CM-8(3),
NIST.800-53.r5 SA-15(2), NIST.800-53.r5 SA-15(8), NIST.800-53.r5 SA-3, NIST.800-53.r5
SI-2(3)

**Category:** Identify > Inventory

**Severity:** Medium

**Evaluated resource:**
`AWS::EC2::Instance`

**Required AWS Config recording resources:**
`AWS::EC2::Instance`,
`AWS::SSM::ManagedInstanceInventory`

**AWS Config rule:**
[ec2-instance-managed-by-systems-manager](../../../config/latest/developerguide/ec2-instance-managed-by-systems-manager.md "../../../config/latest/developerguide/ec2-instance-managed-by-systems-manager.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether the stopped and running EC2 instances in your account are
managed by AWS Systems Manager. Systems Manager is an AWS service that you can use to view and control
your AWS infrastructure.

To help you maintain security and compliance, Systems Manager scans your stopped and running
managed instances. A managed instance is a machine that's configured for use with Systems Manager.
Systems Manager then reports or takes corrective action on any policy violations that it detects.
Systems Manager also helps you configure and maintain your managed instances. To learn more, see
the [AWS Systems Manager User Guide](../../../systems-manager/latest/userguide/what-is-systems-manager.md "../../../systems-manager/latest/userguide/what-is-systems-manager.md").

###### Note

This control generates `FAILED` findings for EC2 instances that are
AWS Elastic Disaster Recovery Replication Server instances managed by AWS. A Replication Server
instance is an EC2 Instance that’s automatically launched by AWS Elastic Disaster Recovery to support
continuous data replication from source servers. AWS intentionally removes the
Systems Manager (SSM) Agent from these instances to maintain isolation and help prevent
potential unintended access paths.

### Remediation

For information about managing EC2 instances with AWS Systems Manager, see [Amazon EC2
host management](../../../systems-manager/latest/userguide/quick-setup-host-management.md "../../../systems-manager/latest/userguide/quick-setup-host-management.md") in the _AWS Systems Manager User Guide_. In the **Configuration options**
section on the AWS Systems Manager console, you can keep the default settings or change them
as necessary for your preferred configuration.

## [SSM.2] Amazon EC2 instances managed by Systems Manager should have a patch

compliance status of COMPLIANT after a patch installation

**Related requirements:** NIST.800-53.r5 CM-8(3),
NIST.800-53.r5 SI-2, NIST.800-53.r5 SI-2(2), NIST.800-53.r5 SI-2(3), NIST.800-53.r5
SI-2(4), NIST.800-53.r5 SI-2(5), NIST.800-171.r2 3.7.1, PCI DSS v3.2.1/6.2,
PCI DSS v4.0.1/2.2.1, PCI DSS v4.0.1/6.3.3

**Category:** Detect > Detection services

**Severity:** High

**Resource type:**
`AWS::SSM::PatchCompliance`

**AWS Config rule:**
[ec2-managedinstance-patch-compliance-status-check](../../../config/latest/developerguide/ec2-managedinstance-patch-compliance-status-check.md "../../../config/latest/developerguide/ec2-managedinstance-patch-compliance-status-check.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether the compliance status of Systems Manager patch compliance is
`COMPLIANT` or `NON_COMPLIANT` after the patch installation on
the instance. The control fails if the compliance status is `NON_COMPLIANT`.
The control only checks instances that are managed by Systems Manager Patch Manager.

Patching your EC2 instances as required by your organization reduces the attack
surface of your AWS accounts.

### Remediation

Systems Manager recommends using [patch
policies](../../../systems-manager/latest/userguide/patch-manager-policies.md "../../../systems-manager/latest/userguide/patch-manager-policies.md") to configure patching for your managed instances. You can also
use [Systems Manager
documents](../../../systems-manager/latest/userguide/patch-manager-ssm-documents.md "../../../systems-manager/latest/userguide/patch-manager-ssm-documents.md"), as described in the following procedure, to patch an
instance.

###### To remediate noncompliant patches

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. For **Node Management**, choose **Run
   Command**, and then choose **Run
   command**.
3. Choose the option for **AWS-RunPatchBaseline**.
4. Change the **Operation** to
   **Install**.
5. Choose **Choose instances manually**, and then choose the
   noncompliant instances.
6. Choose **Run**.
7. After the command is complete, to monitor the new compliance status of
   your patched instances, choose **Compliance** in the
   navigation pane.

## [SSM.3] Amazon EC2 instances managed by Systems Manager should have an

association compliance status of COMPLIANT

**Related requirements:** NIST.800-53.r5 CA-9(1),
NIST.800-53.r5 CM-2, NIST.800-53.r5 CM-2(2), NIST.800-53.r5 CM-8, NIST.800-53.r5
CM-8(1), NIST.800-53.r5 CM-8(3), NIST.800-53.r5 SI-2(3), PCI DSS v3.2.1/2.4,
PCI DSS v4.0.1/2.2.1, PCI DSS v4.0.1/6.3.3

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:**
`AWS::SSM::AssociationCompliance`

**AWS Config rule:**
[ec2-managedinstance-association-compliance-status-check](../../../config/latest/developerguide/ec2-managedinstance-association-compliance-status-check.md "../../../config/latest/developerguide/ec2-managedinstance-association-compliance-status-check.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether the status of the AWS Systems Manager association compliance is
`COMPLIANT` or `NON_COMPLIANT` after the association is run on
an instance. The control fails if the association compliance status is
`NON_COMPLIANT`.

A State Manager association is a configuration that is assigned to your managed
instances. The configuration defines the state that you want to maintain on your
instances. For example, an association can specify that antivirus software must be
installed and running on your instances or that certain ports must be closed.

After you create one or more State Manager associations, compliance status information
is immediately available to you. You can view the compliance status in the console or in
response to AWS CLI commands or corresponding Systems Manager API actions. For associations,
Configuration Compliance shows the compliance status (`Compliant` or
`Non-compliant`). It also shows the severity level assigned to the
association, such as `Critical` or `Medium`.

To learn more about State Manager association compliance, see [About State Manager association compliance](../../../systems-manager/latest/userguide/sysman-compliance-about.md#sysman-compliance-about-association "../../../systems-manager/latest/userguide/sysman-compliance-about.md#sysman-compliance-about-association") in the _AWS Systems Manager User Guide_.

### Remediation

A failed association can be related to different things, including targets and
Systems Manager document names. To remediate this issue, you must first identify and
investigate the association by viewing association history. For instructions on
viewing association history, see [Viewing association histories](../../../systems-manager/latest/userguide/state-manager-associations-history.md "../../../systems-manager/latest/userguide/state-manager-associations-history.md") in the
_AWS Systems Manager User Guide_.

After investigating, you can edit the association to correct the identified issue.
You can edit an association to specify a new name, schedule, severity level, or
targets. After you edit an association, AWS Systems Manager creates a new version. For
instructions on editing an association, see [Editing and creating a new version of an association](../../../systems-manager/latest/userguide/state-manager-associations-edit.md "../../../systems-manager/latest/userguide/state-manager-associations-edit.md") in the
_AWS Systems Manager User Guide_.

## [SSM.4] SSM documents should not be public

**Related requirements:** NIST.800-53.r5 AC-21,
NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-4, NIST.800-53.r5
AC-4(21), NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11),
NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(20), NIST.800-53.r5 SC-7(21),
NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-7(9)

**Category:** Protect > Secure network configuration > Resources not publicly accessible

**Severity:** Critical

**Resource type:**
`AWS::SSM::Document`

**AWS Config rule:**
[ssm-document-not-public](../../../config/latest/developerguide/ssm-document-not-public.md "../../../config/latest/developerguide/ssm-document-not-public.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether AWS Systems Manager documents that are owned by an account are
public. The control fails if Systems Manager documents that have `Self` as the owner
are public.

Systems Manager documents that are public might allow unintended access to your documents. A
public Systems Manager document can expose valuable information about your account, resources, and
internal processes.

Unless your use case requires public sharing, we recommend that you block public
sharing for Systems Manager documents that have `Self` as the owner.

### Remediation

For information about configuring sharing for Systems Manager documents, see [Share an SSM document](../../../systems-manager/latest/userguide/documents-ssm-sharing.md#ssm-how-to-share "../../../systems-manager/latest/userguide/documents-ssm-sharing.md#ssm-how-to-share") in the _AWS Systems Manager User Guide_.

## [SSM.5] SSM documents should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::SSM::Document`

**AWS Config rule:**
[ssm-document-tagged](../../../config/latest/developerguide/ssm-document-tagged.md "../../../config/latest/developerguide/ssm-document-tagged.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                                | Type                            | Allowed custom values                                                                                                                                                         | Security Hub CSPM default value |
| ----------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `requiredKeyTags` | A list of non-system tag keys that must be assigned to an evaluated resource. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value                |

This control checks whether an AWS Systems Manager document has the tag keys specified by the
`requiredKeyTags` parameter. The control fails if the document
doesn't have any tag keys, or it doesn't have all the keys specified by the
`requiredKeyTags` parameter. If you don't specify any values for
the `requiredKeyTags` parameter, the control checks only for the
existence of a tag key and fails if the document doesn't have any tag keys. The control
ignores system tags, which are applied automatically and have the `aws:`
prefix. The control doesn't evaluate Systems Manager documents that are owned by Amazon.

A tag is a label that you create and assign to an AWS resource. Each tag consists of
a required tag key and an optional tag value. You can use tags to categorize resources
by purpose, owner, environment, or other criteria. They can help you identify, organize,
search for, and filter resources. They can also help you track resource owners for
actions and notifications. You can also use tags to implement attribute-based access
control (ABAC) as an authorization strategy. For more information about ABAC strategies,
see [Define
permissions based on attributes with ABAC authorization](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_. For more information about tags, see the
[Tagging AWS Resources and Tag Editor User
Guide](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md").

###### Note

Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are
accessible from many AWS services. They aren't intended to be used for private or sensitive data.

### Remediation

To add tags to an AWS Systems Manager document, you can use the [AddTagsToResource](../../../systems-manager/latest/APIReference/API_AddTagsToResource.md "../../../systems-manager/latest/APIReference/API_AddTagsToResource.md") operation of the AWS Systems Manager API or, if you're using
the AWS CLI, run the [add-tags-to-resource](../../../cli/latest/reference/ssm/add-tags-to-resource.md "../../../cli/latest/reference/ssm/add-tags-to-resource.md") command. You can also use the AWS Systems Manager
console.

## [SSM.6] SSM Automation should have CloudWatch logging

enabled

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::::Account`

**AWS Config rule:**
[ssm-automation-logging-enabled](../../../config/latest/developerguide/ssm-automation-logging-enabled.md "../../../config/latest/developerguide/ssm-automation-logging-enabled.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether Amazon CloudWatch logging is enabled for AWS Systems Manager (SSM)
Automation. The control fails if CloudWatch logging isn't enabled for SSM Automation.

SSM Automation is an AWS Systems Manager tool that helps you build automated solutions to
deploy, configure, and manage AWS resources at scale using predefined or custom
runbooks. To meet operational or security requirements for your organization, you might
need to provide a record of the scripts that it runs. You can configure SSM Automation
to send the output from `aws:executeScript` actions in your runbooks to an
Amazon CloudWatch Logs log group that you specify. With CloudWatch Logs, you can monitor, store, and access log
files from various AWS services.

### Remediation

For information about enabling CloudWatch logging for SSM Automation, see [Logging
Automation action output with CloudWatch Logs](../../../systems-manager/latest/userguide/automation-action-logging.md "../../../systems-manager/latest/userguide/automation-action-logging.md") in the _AWS Systems Manager User Guide_.

## [SSM.7] SSM documents should have the block public sharing

setting enabled

**Category:** Protect > Secure access management > Resource not publicly accessible

**Severity:** Critical

**Resource type:**
`AWS::::Account`

**AWS Config rule:**
[ssm-automation-block-public-sharing](../../../config/latest/developerguide/ssm-automation-block-public-sharing.md "../../../config/latest/developerguide/ssm-automation-block-public-sharing.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether the block public sharing setting is enabled for AWS Systems Manager
documents. The control fails if the block public sharing setting is disabled for Systems Manager
documents.

The block public sharing setting for AWS Systems Manager (SSM) documents is an account-level
setting. Enabling this setting can prevent unwanted access to your SSM documents. If
you enable this setting, your change doesn't affect any SSM documents that you're
currently sharing with the public. Unless your use case requires you to share SSM
documents with the public, we recommend that you enable the block public sharing
setting. The setting can differ for each AWS Region.

### Remediation

For information about enabling the block public sharing setting for AWS Systems Manager
(SSM) documents, see [Block
public sharing for SSM documents](../../../systems-manager/latest/userguide/documents-ssm-sharing.md#block-public-access "../../../systems-manager/latest/userguide/documents-ssm-sharing.md#block-public-access") in the _AWS Systems Manager User Guide_.
