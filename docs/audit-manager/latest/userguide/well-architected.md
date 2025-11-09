# AWS Well Architected Framework WAF v10

AWS Audit Manager provides a prebuilt standard framework that supports the AWS Well-Architected
Framework v10.

###### Topics

- [What is the AWS Well-Architected
  Framework?](#what-is-well-architected "#what-is-well-architected")
- [Using this framework](#framework-well-architected "#framework-well-architected")
- [Next steps](#next-steps-well-architected "#next-steps-well-architected")
- [Additional resources](#resources-aws-foundational-security-best-practices "#resources-aws-foundational-security-best-practices")

## What is the AWS Well-Architected

Framework?

[AWS
Well-Architected](https://aws.amazon.com/architecture/well-architected/ "https://aws.amazon.com/architecture/well-architected/") is a framework that can help you to build secure,
high-performing, resilient, and efficient infrastructure for your applications and
workloads. Based on six pillars—operational excellence, security, reliability,
performance efficiency, cost optimization, and sustainability—AWS
Well-Architected provides a consistent approach for you and your partners to evaluate
architectures and implement designs that can scale over time.

## Using this framework

You can use the AWS Well-Architected Framework to help you prepare for audits. This
framework describes the key concepts, design principles, and architectural best practices
for designing and running workloads in the cloud. Out of the six pillars that AWS
Well-Architected is based on, the security and reliability pillars are the pillars that
AWS Audit Manager offers a prebuilt framework and controls for. You can also customize this
framework and its controls to support internal audits with specific requirements.

Using the framework as a starting point, you can create an Audit Manager assessment and start
collecting evidence that’s relevant for your audit. After you create an assessment, Audit Manager
starts to assess your AWS resources. It does this based on the controls that are defined
in the AWS Well-Architected Framework. When it's time for an audit, you—or a
delegate of your choice—can review the evidence that Audit Manager collected. Either, you
can browse the evidence folders in your assessment and choose which evidence you want to
include in your assessment report. Or, if you enabled evidence finder, you can search for
specific evidence and export it in CSV format, or create an assessment report from your
search results. Either way, you can use this assessment report to show that your controls
are working as intended.

The framework details are as follows:

| Framework name in AWS Audit Manager                            | Number of automated controls | Number of manual controls | Number of control sets |
| -------------------------------------------------------------- | ---------------------------- | ------------------------- | ---------------------- |
| Amazon Web Services (AWS) Well Architected Framework (WAF) v10 | 43                           | 291                       | 6                      |

###### Important

To ensure that this framework collects the intended evidence from AWS Security Hub, make sure
that you enabled all standards in Security Hub.

To ensure that this framework collects the intended evidence from AWS Config, make sure
that you enable the necessary AWS Config rules. To review the AWS Config rules that are used
as data source mappings in this standard framework, download the [AuditManager_ConfigDataSourceMappings_AWS-Well-Architected-Framework-WAF-v10.zip](samples/AuditManager_ConfigDataSourceMappings_AWS-Well-Architected-Framework-WAF-v10.md "samples/AuditManager_ConfigDataSourceMappings_AWS-Well-Architected-Framework-WAF-v10.md")
file.

The controls in this framework aren't intended to verify if your systems are
compliant. Moreover, they can't guarantee that you'll pass an audit.

## Next steps

For instructions on how to view detailed information about this framework, including the
list of standard controls that it contains, see [Reviewing a framework in AWS Audit Manager](review-frameworks.md "review-frameworks.md").

For instructions on how to create an assessment using this framework, see [Creating an assessment in AWS Audit Manager](create-assessments.md "create-assessments.md").

For instructions on how to customize this framework to support your specific
requirements, see [Making an editable copy of an
existing framework in AWS Audit Manager](create-custom-frameworks-from-existing.md "create-custom-frameworks-from-existing.md").

## Additional resources

- [AWS
  Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")
- [AWS Well-Architected Framework documentation](../../../wellarchitected/latest/framework/welcome.md "../../../wellarchitected/latest/framework/welcome.md")
