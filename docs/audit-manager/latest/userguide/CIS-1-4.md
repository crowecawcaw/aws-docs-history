# CIS AWS Benchmark v1.4.0

AWS Audit Manager provides two prebuilt standard frameworks that support the Center for Internet
Security (CIS) AWS Foundations Benchmark v1.4.0.

###### Note

- For information about the Audit Manager frameworks that support v1.2.0, see [CIS AWS Benchmark v1.2.0](CIS-1-2.md "CIS-1-2.md").
- For information about the Audit Manager frameworks that support v1.3.0, see [CIS AWS Benchmark v1.3.0](CIS-1-3.md "CIS-1-3.md").

###### Topics

- [What is the CIS AWS Benchmark?](#what-is-CIS-1-4 "#what-is-CIS-1-4")
- [Using these frameworks](#framework-CIS-1-4 "#framework-CIS-1-4")
- [Next steps](#next-steps-CIS-1-4 "#next-steps-CIS-1-4")
- [Additional resources](#resources-CIS-1-4 "#resources-CIS-1-4")

## What is the CIS AWS Benchmark?

The CIS AWS Benchmark v1.4.0 provides prescriptive guidance for configuring security
options for a subset of Amazon Web Services. It has an emphasis on foundational, testable, and
architecture agnostic settings. Some of the specific Amazon Web Services in scope for this document
include the following:

- AWS Identity and Access Management (IAM)
- IAM Access Analyzer
- AWS Config
- AWS CloudTrail
- Amazon CloudWatch
- Amazon Simple Notification Service (Amazon SNS)
- Amazon Simple Storage Service (Amazon S3)
- Amazon Elastic Compute Cloud (Amazon EC2)
- Amazon Relational Database Service (Amazon RDS)
- Amazon Virtual Private Cloud

###### Difference between CIS Benchmarks and CIS Controls

The _CIS Benchmarks_ are security best practice
guidelines that are specific to vendor products. Ranging from operating systems to cloud
services and networks devices, the settings that are applied from a benchmark protect
the systems that are being used. The _CIS Controls_ are
foundational best practice guidelines for your organization to follow to help protect
from known cyberattack vectors.

###### Examples

- CIS Benchmarks are prescriptive. They typically reference a specific setting that
  can be reviewed and set in the vendor product.

**Example:** CIS AWS Benchmark v1.3.0 - Ensure MFA
is enabled for the "root user" account

This recommendation provides prescriptive guidance on how to check for this and
how to set this on the root account for the AWS environment.

- CIS Controls are for your organization as a whole, and aren't specific to only one
  vendor product.

**Example:** CIS v7.1 - Use Multi-Factor
Authentication for All Administrative Access

This control describes what's expected to be applied within your organization.
However, it doesn't describe how to apply it for the systems and workloads that you're
running, regardless of where they are.

## Using these frameworks to support your audit preparation

You can use the CIS AWS Benchmark v1.4.0 frameworks in AWS Audit Manager to help you prepare
for CIS audits. You can also customize these frameworks and their controls to support
internal audits with specific requirements.

Using the frameworks as a starting point, you can create an Audit Manager assessment and start
collecting evidence that’s relevant for your audit. After you create an assessment, Audit Manager
starts to assess your AWS resources. It does this based on the controls that are defined
in the CIS framework. When it's time for an audit, you—or a delegate of your
choice—can review the evidence that Audit Manager collected. Either, you can browse the
evidence folders in your assessment and choose which evidence you want to include in your
assessment report. Or, if you enabled evidence finder, you can search for specific
evidence and export it in CSV format, or create an assessment report from your search
results. Either way, you can use this assessment report to show that your controls are
working as intended.

The framework details are as follows:

| Framework name in AWS Audit Manager                                                             | Number of automated controls | Number of manual controls | Number of control sets |
| ----------------------------------------------------------------------------------------------- | ---------------------------- | ------------------------- | ---------------------- |
| Center for Internet Security (CIS) Amazon Web Services (AWS) Benchmark<br>v1.4.0, Level 1       | 32                           | 6                         | 5                      |
| Center for Internet Security (CIS) Amazon Web Services (AWS) Benchmark<br>v1.4.0, Level 1 and 2 | 50                           | 8                         | 5                      |

###### Important

To ensure that these frameworks collect the intended evidence from AWS Security Hub CSPM, make
sure that you enabled all standards in Security Hub CSPM.

To ensure that these frameworks collect the intended evidence from AWS Config, make sure
that you enable the necessary AWS Config rules. To review a list of the AWS Config rules that
are used as data source mappings for these standard frameworks, download the following
files:

1. [AuditManager_ConfigDataSourceMappings_CIS-AWS-Benchmark-v1.4.0,-Level-1.zip](samples/AuditManager_ConfigDataSourceMappings_CIS-AWS-Benchmark-v1.4.0,-Level-1.md "samples/AuditManager_ConfigDataSourceMappings_CIS-AWS-Benchmark-v1.4.0,-Level-1.md")
2. [AuditManager_ConfigDataSourceMappings_CIS-AWS-Benchmark-v1.4.0,-Level-1-and-2.zip](samples/AuditManager_ConfigDataSourceMappings_CIS-AWS-Benchmark-v1.4.0,-Level-1-and-2.md "samples/AuditManager_ConfigDataSourceMappings_CIS-AWS-Benchmark-v1.4.0,-Level-1-and-2.md")

The controls in these frameworks aren't intended to verify if your systems are
compliant with the CIS AWS Benchmark v1.4.0. Moreover, they can't guarantee that you'll
pass a CIS audit. AWS Audit Manager doesn't automatically check procedural controls that require
manual evidence collection.

## Next steps

For instructions on how to view detailed information about these framework, including
the list of standard controls that they contain, see [Reviewing a framework in AWS Audit Manager](review-frameworks.md "review-frameworks.md").

For instructions on how to create an assessment using these frameworks, see [Creating an assessment in AWS Audit Manager](create-assessments.md "create-assessments.md").

For instructions on how to customize these frameworks to support your specific
requirements, see [Making an editable copy of an existing framework in AWS Audit Manager](create-custom-frameworks-from-existing.md "create-custom-frameworks-from-existing.md").

## Additional resources

- [CIS Benchmarks](https://benchmarks.cisecurity.org "https://benchmarks.cisecurity.org") from the
  _Center for Internet Security_
- [CIS AWS
  Foundations Benchmark blog posts](https://aws.amazon.com/blogs/security/tag/cis-aws-foundations-benchmark/ "https://aws.amazon.com/blogs/security/tag/cis-aws-foundations-benchmark/") on the _AWS
  Security Blog_
