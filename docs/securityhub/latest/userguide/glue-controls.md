# Security Hub controls for AWS Glue

These AWS Security Hub controls evaluate the AWS Glue service and resources. The controls might
not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [Glue.1] AWS Glue jobs should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::Glue::Job`

**AWS Config rule:**
`tagged-glue-job` (custom Security Hub rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value           |

This control checks whether an AWS Glue job has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the job doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the job isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
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

To add tags to a AWS Glue job, see [AWS tags in AWS Glue](../../../glue/latest/dg/monitor-tags.md "../../../glue/latest/dg/monitor-tags.md") in the _AWS Glue User Guide_.

## [Glue.3] AWS Glue machine learning transforms should be encrypted at rest

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:**
`AWS::Glue::MLTransform`

**AWS Config rule:**
[glue-ml-transform-encrypted-at-rest](../../../config/latest/developerguide/glue-ml-transform-encrypted-at-rest.md "../../../config/latest/developerguide/glue-ml-transform-encrypted-at-rest.md")

**Schedule type:** Change triggered

**Parameters:** No

This control checks whether an AWS Glue machine learning transform is encrypted at rest. The control fails if the machine learning transform isn't encrypted at rest.

Data at rest refers to data that's stored in persistent, non-volatile storage for any duration. Encrypting data at rest helps you protect its confidentiality, which reduces the risk that an unauthorized user can access it.

### Remediation

To configure encryption for AWS Glue machine learning transforms, see [Working with machine learning transforms](../../../glue/latest/dg/console-machine-learning-transforms.md "../../../glue/latest/dg/console-machine-learning-transforms.md") in the
_AWS Glue User Guide_.

## [Glue.4] AWS Glue Spark jobs should run on supported versions of AWS Glue

**Related requirements:** NIST.800-53.r5 CA-9(1),
NIST.800-53.r5 CM-2, NIST.800-53.r5 SI-2, NIST.800-53.r5 SI-2(2), NIST.800-53.r5
SI-2(4), NIST.800-53.r5 SI-2(5)

**Category:** Identify > Vulnerability, patch, and version management

**Severity:** Medium

**Resource type:** `AWS::Glue::Job`

**AWS Config rule:** [glue-spark-job-supported-version](../../../config/latest/developerguide/glue-spark-job-supported-version.md "../../../config/latest/developerguide/glue-spark-job-supported-version.md")

**Schedule type:** Change triggered

**Parameters:**
`minimumSupportedGlueVersion`: `3.0` (not customizable)

This control checks whether an AWS Glue for Spark job is configured to run on a supported
version of AWS Glue. The control fails if the Spark job is configured to run on a version
of AWS Glue that's earlier than the minimum supported version.

###### Note

This control also generates a `FAILED` finding for an AWS Glue for Spark
job if the AWS Glue version (`GlueVersion`) property doesn’t exist or is
null in the configuration item (CI) for the job. In such cases, the finding includes
the following annotation: `GlueVersion is null or missing in glueetl job
 configuration`. To address this type of `FAILED` finding, add
the `GlueVersion` property to the job’s configuration. For a list of
supported versions and runtime environments, see [AWS Glue
Versions](../../../glue/latest/dg/release-notes.md#release-notes-versions "../../../glue/latest/dg/release-notes.md#release-notes-versions") in the _AWS Glue User
Guide_.

Running AWS Glue Spark jobs on current versions of AWS Glue can optimize performance,
security, and access to the latest features of AWS Glue. It can also help safeguard against
security vulnerabilities. For example, a new version might be released to provide
security updates, address issues, or introduce new features.

### Remediation

For information about migrating a Spark job to a supported version of AWS Glue, see
[Migrating AWS Glue for Spark
jobs](../../../glue/latest/dg/migrating-version-40.md "../../../glue/latest/dg/migrating-version-40.md") in the _AWS Glue User
Guide_.
