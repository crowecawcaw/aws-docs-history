

# Security Hub CSPM controls for Amazon Athena
<a name="athena-controls"></a>

These AWS Security Hub CSPM controls evaluate the Amazon Athena service and resources. The controls might not be available in all AWS Regions. For more information, see [Availability of controls by Region](securityhub-regions.md#securityhub-regions-control-support).

## [Athena.1] Athena workgroups should be encrypted at rest
<a name="athena-1"></a>

**Important**  
Security Hub CSPM retired this control in April 2024. For more information, see [Change log for Security Hub CSPM controls](controls-change-log.md).

**Category:** Protect > Data protection > Encryption of data at rest

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-3(6), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-28, NIST.800-53.r5 SC-28(1), NIST.800-53.r5 SC-7(10), NIST.800-53.r5 SI-7(6)

**Severity:** Medium

**Resource type:** `AWS::Athena::WorkGroup`

**AWS Config rule:** [athena-workgroup-encrypted-at-rest](https://docs.aws.amazon.com/config/latest/developerguide/athena-workgroup-encrypted-at-rest.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks if an Athena workgroup is encrypted at rest. The control fails if an Athena workgroup isn’t encrypted at rest.

In Athena, you can create workgroups for running queries for teams, applications, or different workloads. Each workgroup has a setting to enable encryption on all queries. You have the option to use server-side encryption with Amazon Simple Storage Service (Amazon S3) managed keys, server-side encryption with AWS Key Management Service (AWS KMS) keys, or client-side encryption with customer managed KMS keys. Data at rest refers to any data that's stored in persistent, non-volatile storage for any duration. Encryption helps you protect the confidentiality of such data, reducing the risk that an unauthorized user can access it.

### Remediation
<a name="athena-1-remediation"></a>

To enable encryption at rest for Athena workgroups, see [Edit a workgroup](https://docs.aws.amazon.com/athena/latest/ug/workgroups-create-update-delete.html#editing-workgroups) in the *Amazon Athena User Guide*. In the **Query Result Configuration** section, select **Encrypt query results**.

## [Athena.2] Athena data catalogs should be tagged
<a name="athena-2"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::Athena::DataCatalog`

**AWS Config rule:** `tagged-athena-datacatalog` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  |  No default value  | 

This control checks whether an Amazon Athena data catalog has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the data catalog doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the data catalog isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="athena-2-remediation"></a>

To add tags to an Athena data catalog, see [Tagging Athena resources](https://docs.aws.amazon.com/athena/latest/ug/tags.html) in the *Amazon Athena User Guide*.

## [Athena.3] Athena workgroups should be tagged
<a name="athena-3"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::Athena::WorkGroup`

**AWS Config rule:** `tagged-athena-workgroup` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  |  No default value  | 

This control checks whether an Amazon Athena workgroup has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the workgroup doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the workgroup isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="athena-3-remediation"></a>

To add tags to an Athena workgroup, see [Adding and deleting tags on an individual workgroup](https://docs.aws.amazon.com/athena/latest/ug/tags-console.html#tags-add-delete) in the *Amazon Athena User Guide*.

## [Athena.4] Athena workgroups should have logging enabled
<a name="athena-4"></a>

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:** `AWS::Athena::WorkGroup`

**AWS Config rule:** [athena-workgroup-logging-enabled](https://docs.aws.amazon.com/config/latest/developerguide/athena-workgroup-logging-enabled.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon Athena workgroup has logging enabled. The control fails if the workgroup doesn't have logging enabled.

Audit logs track and monitor system activities. They provide a record of events that can help you detect security breaches, investigate incidents, and comply with regulations. Audit logs also enhance the overall accountability and transparency of your organization.

### Remediation
<a name="athena-4-remediation"></a>

For information about enabling logging for an Athena workgroup, see [Enable CloudWatch query metrics in Athena](https://docs.aws.amazon.com/athena/latest/ug/athena-cloudwatch-metrics-enable.html) in the *Amazon Athena User Guide*.