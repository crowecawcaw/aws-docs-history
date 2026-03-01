# AWS Foundational Security Best Practices

AWS Audit Manager provides a prebuilt standard framework that supports the AWS Foundational
Security Best Practices.

###### Topics

- [What is the AWS Foundational Security Best Practices standard?](#what-is-aws-foundational-security-best-practices "#what-is-aws-foundational-security-best-practices")
- [Using this framework](#framework-aws-foundational-security-best-practices "#framework-aws-foundational-security-best-practices")
- [Next steps](#next-steps-aws-foundational-security-best-practices "#next-steps-aws-foundational-security-best-practices")
- [Additional resources](#resources-aws-foundational-security-best-practices "#resources-aws-foundational-security-best-practices")

## What is the AWS Foundational Security Best Practices standard?

The AWS Foundational Security Best Practices standard is a set of controls that
detect when your deployed accounts and resources deviate from security best
practices.

You can use this standard to continually evaluate all of your AWS accounts and
workloads and quickly identify areas of deviation from best practices. The standard
provides actionable and prescriptive guidance on how to improve and maintain your
organization’s security posture.

The controls include best practices from across multiple AWS services. Each control
is assigned a category that reflects the security function that it applies to. For more
information, see [Control categories](../../../securityhub/latest/userguide/control-categories.md "../../../securityhub/latest/userguide/control-categories.md") in the _AWS Security Hub CSPM
User Guide_.

## Using this framework

You can use the AWS Foundational Security Best Practices framework to help you
prepare for audits. This framework includes a prebuilt collection of controls with
descriptions and testing procedures. These controls are grouped into control sets
according to AWS Foundational Security Best Practices requirements. You can also
customize this framework and its controls to support internal audits with specific
requirements.

Using the framework as a starting point, you can create an Audit Manager assessment and start
collecting evidence that’s relevant for your audit. After you create an assessment, Audit Manager
starts to assess resources in your AWS accounts and services. It does this based on the
controls that are defined in the AWS Foundational Security Best Practices framework.
When it's time for an audit, you—or a delegate of your choice—can
review the evidence that Audit Manager collected. Either, you can browse the evidence folders in
your assessment and choose which evidence you want to include in your assessment report.
Or, if you enabled evidence finder, you can search for specific evidence and export it in
CSV format, or create an assessment report from your search results. Either way, you can
use this assessment report to show that your controls are working as intended.

The AWS Foundational Security Best Practices framework details are as
follows:

| Framework name in AWS Audit Manager      | Number of automated controls | Number of manual controls | Number of control sets |
| ---------------------------------------- | ---------------------------- | ------------------------- | ---------------------- |
| AWS Foundational Security Best Practices | 146                          | 0                         | 31                     |

###### Important

To ensure that this framework collects the intended evidence from AWS Security Hub CSPM, make sure
that you enabled all standards in Security Hub CSPM.

The controls in this AWS Audit Manager framework aren't intended to verify if your systems are
compliant with AWS Foundational Security Best Practices. Moreover, they can't guarantee
that you'll pass an AWS Foundational Security Best Practices audit.

## Next steps

For instructions on how to view detailed information about this framework, including the
list of standard controls that it contains, see [Reviewing a framework in AWS Audit Manager](review-frameworks.md "review-frameworks.md").

For instructions on how to create an assessment using this framework, see [Creating an assessment in AWS Audit Manager](create-assessments.md "create-assessments.md").

For instructions on how to customize this framework to support your specific
requirements, see [Making an editable copy of an existing framework in AWS Audit Manager](create-custom-frameworks-from-existing.md "create-custom-frameworks-from-existing.md").

## Additional resources

- [AWS Foundational Security Best Practices standard](../../../securityhub/latest/userguide/securityhub-standards-fsbp.md "../../../securityhub/latest/userguide/securityhub-standards-fsbp.md") in
  the _AWS Security Hub CSPM User Guide_
- [Control categories](../../../securityhub/latest/userguide/control-categories.md "../../../securityhub/latest/userguide/control-categories.md") in the _AWS Security Hub CSPM User Guide_
