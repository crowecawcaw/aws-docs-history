# CIS Controls v7.1, IG1

AWS Audit Manager provides a prebuilt standard framework that supports Center for Internet
Security (CIS) v7.1 Implementation Group 1.

###### Note

For information about CIS v8 IG1and the AWS Audit Manager framework that supports this
standard, see [CIS Critical Security Controls version 8.0, IG1](CIS-controls-v8.md "CIS-controls-v8.md") .

###### Topics

- [What are CIS Controls?](#what-is-CIS-controls "#what-is-CIS-controls")
- [Using this framework](#framework-CIS-controls "#framework-CIS-controls")
- [Next steps](#next-steps-CIS-controls "#next-steps-CIS-controls")
- [Additional resources](#resources-CIS-controls "#resources-CIS-controls")

## What are CIS Controls?

The CIS Controls are a prioritized set of actions that collectively form a
defense-in-depth set of best practices. These best practices mitigate the most common
attacks against systems and networks. _Implementation Group
1_ is generally defined for an organization with limited resources and
cybersecurity expertise that are available to implement Sub-Controls.

###### Difference between CIS Controls and CIS Benchmarks

The CIS Controls are foundational best practice guidelines that an organization can
follow to have protection from known cyberattack vectors. The CIS Benchmarks are
security best practice guidelines specific to vendor products. Ranging from operating
systems to cloud services and network devices, the settings that are applied from a
Benchmark protect the systems that are being used.

###### Examples

- _CIS Benchmarks_ are prescriptive. They typically
  reference a specific setting that can be reviewed and set in the vendor product.
  - **Example**: CIS AWS Benchmark v1.2.0 - Ensure
    MFA is enabled for the "root user" account
  - This recommendation provides prescriptive guidance on how to check for this
    and how to set this on the root account for the AWS environment.

- _CIS Controls_ are for your organization as a
  whole and aren't specific to only one vendor product.
  - **Example**: CIS v7.1 - Use Multi-Factor
    Authentication for All Administrative Access
  - This control describes what's expected to be applied within your organization.
    However, it doesn't tell you how you should apply it for the systems and workloads
    that you're running (regardless of where they are).

## Using this framework

You can use the _CIS Controls v7.1 IG1_ framework to
help you prepare for audits. This framework includes a prebuilt collection of controls
with descriptions and testing procedures. These controls are grouped into control sets
according to CIS requirements. You can also customize this framework and its controls to
support internal audits with specific requirements.

Using the framework as a starting point, you can create an Audit Manager assessment and start
collecting evidence that’s relevant for your audit. After you create an assessment, Audit Manager
starts to assess your AWS resources. It does this based on the controls that are defined
in the CIS Controls v7.1 IG1 framework. When it's time for an audit, you—or a
delegate of your choice—can review the evidence that Audit Manager collected. Either, you
can browse the evidence folders in your assessment and choose which evidence you want to
include in your assessment report. Or, if you enabled evidence finder, you can search for
specific evidence and export it in CSV format, or create an assessment report from your
search results. Either way, you can use this assessment report to show that your controls
are working as intended.

The CIS Controls v7.1 IG1 framework details are as follows:

| Framework name in AWS Audit Manager          | Number of automated controls | Number of manual controls | Number of control sets |
| -------------------------------------------- | ---------------------------- | ------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Center for Internet Security (CIS) v7.1, IG1 | 8                            | 35                        | 18                     | ###### Important To ensure that this framework collects the intended evidence from AWS Security Hub, make sure that you enabled all standards in Security Hub. To ensure that this framework collects the intended evidence from AWS Config, make sure that you enable the necessary AWS Config rules. To review the AWS Config rules that are used as data source mappings in this standard framework, download the [AuditManager_ConfigDataSourceMappings_Center-for-Internet-Security-(CIS)-v7.1,-IG1.zip](<samples/AuditManager_ConfigDataSourceMappings_Center-for-Internet-Security-(CIS)-v7.1,-IG1.md> "samples/AuditManager_ConfigDataSourceMappings_Center-for-Internet-Security-(CIS)-v7.1,-IG1.md") file. The controls in this framework aren't intended to verify if your systems are compliant with CIS Controls. Moreover, they can't guarantee that you'll pass a CIS audit. AWS Audit Manager doesn't automatically check procedural controls that require manual evidence collection. ## Next steps For instructions on how to view detailed information about this framework, including the list of standard controls that it contains, see [Reviewing a framework in AWS Audit Manager](review-frameworks.md "review-frameworks.md"). For instructions on how to create an assessment using this framework, see [Creating an assessment in AWS Audit Manager](create-assessments.md "create-assessments.md"). For instructions on how to customize this framework to support your specific requirements, see [Making an editable copy of an existing framework in AWS Audit Manager](create-custom-frameworks-from-existing.md "create-custom-frameworks-from-existing.md"). ## Additional resources <br>• [CIS Controls v7.1 IG1](https://www.cisecurity.org/controls/v7-1 "https://www.cisecurity.org/controls/v7-1") |
