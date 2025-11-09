# Security Hub controls for Amazon Athena

These AWS Security Hub controls evaluate the Amazon Athena service and resources. The controls might
not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [Athena.1] Athena workgroups should be encrypted at

rest

###### Important

Security Hub retired this control in April 2024.
For more information, see [Change log for Security Hub CSPM controls](controls-change-log.md "controls-change-log.md").

**Category:** Protect > Data protection > Encryption of
data at rest

**Related requirements:** NIST.800-53.r5 CA-9(1),
NIST.800-53.r5 CM-3(6), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-28, NIST.800-53.r5
SC-28(1), NIST.800-53.r5 SC-7(10), NIST.800-53.r5 SI-7(6)

**Severity:** Medium

**Resource type:**
`AWS::Athena::WorkGroup`

**AWS Config rule:**
[athena-workgroup-encrypted-at-rest](../../../config/latest/developerguide/athena-workgroup-encrypted-at-rest.md "../../../config/latest/developerguide/athena-workgroup-encrypted-at-rest.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks if an Athena workgroup is encrypted at rest. The control fails if
an Athena workgroup isn’t encrypted at rest.

In Athena, you can create workgroups for running queries for teams, applications, or
different workloads. Each workgroup has a setting to enable encryption on all queries.
You have the option to use server-side encryption with Amazon Simple Storage Service (Amazon S3) managed keys,
server-side encryption with AWS Key Management Service (AWS KMS) keys, or client-side encryption with
customer managed KMS keys. Data at rest refers to any data that's stored in
persistent, non-volatile storage for any duration. Encryption helps you protect the
confidentiality of such data, reducing the risk that an unauthorized user can access
it.

### Remediation

To enable encryption at rest for Athena workgroups, see [Edit a workgroup](../../../athena/latest/ug/workgroups-create-update-delete.md#editing-workgroups "../../../athena/latest/ug/workgroups-create-update-delete.md#editing-workgroups")
in the _Amazon Athena User Guide_. In the **Query Result Configuration**
section, select **Encrypt query results**.

## [Athena.2] Athena data catalogs should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::Athena::DataCatalog`

**AWS Config rule:**
`tagged-athena-datacatalog` (custom Security Hub rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | `No default value`         |

This control checks whether an Amazon Athena data catalog has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the data catalog doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the data catalog isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to
categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources.
Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based
access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles)
and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC
policies to allow operations when the principal's tag matches the resource tag. For more information, see
[What is ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_.

###### Note

Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible
to many AWS services, including AWS Billing. For more tagging best practices, see
[Tagging your AWS resources](../../../tag-editor/latest/userguide/tagging.md#tag-best-practices "../../../tag-editor/latest/userguide/tagging.md#tag-best-practices") in the
_AWS General Reference_.

### Remediation

To add tags to an Athena data catalog, see [Tagging Athena resources](../../../athena/latest/ug/tags.md "../../../athena/latest/ug/tags.md") in the _Amazon Athena User Guide_.

## [Athena.3] Athena workgroups should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::Athena::WorkGroup`

**AWS Config rule:**
`tagged-athena-workgroup` (custom Security Hub rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | `No default value`         |

This control checks whether an Amazon Athena workgroup has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the workgroup doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the workgroup isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to
categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources.
Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based
access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles)
and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC
policies to allow operations when the principal's tag matches the resource tag. For more information, see
[What is ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_.

###### Note

Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible
to many AWS services, including AWS Billing. For more tagging best practices, see
[Tagging your AWS resources](../../../tag-editor/latest/userguide/tagging.md#tag-best-practices "../../../tag-editor/latest/userguide/tagging.md#tag-best-practices") in the
_AWS General Reference_.

### Remediation

To add tags to an Athena workgroup, see [Adding and deleting tags on an individual workgroup](../../../athena/latest/ug/tags-console.md#tags-add-delete "../../../athena/latest/ug/tags-console.md#tags-add-delete") in the _Amazon Athena User Guide_.

## [Athena.4] Athena workgroups should have logging enabled

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::Athena::WorkGroup`

**AWS Config rule:**
[athena-workgroup-logging-enabled](../../../config/latest/developerguide/athena-workgroup-logging-enabled.md "../../../config/latest/developerguide/athena-workgroup-logging-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon Athena workgroup has logging enabled. The control
fails if the workgroup doesn't have logging enabled.

Audit logs track and monitor system activities. They provide a record of events that can help you detect security
breaches, investigate incidents, and comply with regulations. Audit logs also enhance the overall accountability and transparency
of your organization.

### Remediation

For information about enabling logging for an Athena workgroup, see [Enable CloudWatch query
metrics in Athena](../../../athena/latest/ug/athena-cloudwatch-metrics-enable.md "../../../athena/latest/ug/athena-cloudwatch-metrics-enable.md") in the _Amazon Athena User Guide_.
