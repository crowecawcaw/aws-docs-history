# AWS Audit Manager Sample Framework

If you’re new to Audit Manager, you can use the AWS Audit Manager Sample Framework to get to know how Audit Manager
works. It provides a simple environment where you can explore Audit Manager functionality without
getting overwhelmed by excessive evidence or exceeding your AWS Free Tier limits. After
you've tried out the sample framework, you'll be ready to start using the rest of the
frameworks that Audit Manager provides.

###### Topics

- [What is the AWS Audit Manager sample framework?](#what-is-Sample "#what-is-Sample")
- [Using this framework](#framework-sample "#framework-sample")
- [Next steps](#next-steps-sample "#next-steps-sample")

## What is the AWS Audit Manager Sample Framework?

The sample framework provides a streamlined, beginner-friendly way to explore the core
functionality of Audit Manager – collecting evidence and attaching it to controls.

In the framework, you’ll find sample controls that show you the different data sources
that Audit Manager uses to automatically collect evidence. These data sources include an AWS CloudTrail
event, an AWS Config rule, an AWS Security Hub control, and an AWS API call. By using these data
sources in an test assessment, you can see how Audit Manager works with different AWS services to
gather evidence. In addition to demonstrating automated evidence collection, the sample
framework shows how you can manually add your own evidence. It also has a manual control
that allows you to upload files as evidence. By trying out both automated and manual
controls, you can develop a well-rounded understanding of the different ways in which
evidence can be added to your assessments.

###### Note

This framework is different from other standard frameworks. The sample framework isn’t
intended for managing actual compliance assessments or audits. Its purpose is to help you
learn how to use Audit Manager. It provides a controlled environment where you can collect enough
evidence to experience Audit Manager's capabilities, while keeping the scope manageable for
beginners.

## Using this framework

Using the AWS Audit Manager Sample Framework lets you practice navigating the Audit Manager interface,
collecting evidence, and seeing how that evidence is attached to your assessment
controls.

To get started, use the sample framework to create an assessment. This action starts the
ongoing collection of evidence for each of the automated controls in the sample framework.
Based on the control definitions, Audit Manager assesses your AWS resources, collects the relevant
evidence, and then attaches it to the controls in your assessment. At this time, you can
explore the evidence that Audit Manager has collected. You can also try adding your own evidence to
the manual controls.

You can find this framework under the **Standard frameworks** tab of
the framework library in Audit Manager.

The framework details are as follows:

| Framework name in AWS Audit Manager                      | Number of automated controls | Number of manual controls | Number of control sets |
| -------------------------------------------------------- | ---------------------------- | ------------------------- | ---------------------- |
| Amazon Web Services (AWS) Audit Manager Sample Framework | 4                            | 1                         | 2                      |

###### Important

To ensure that this framework collects the intended evidence from AWS Security Hub, make sure
that you enabled all standards in Security Hub.

To ensure that this framework collects the intended evidence from AWS Config, make sure
that you enable the necessary AWS Config rules. To review the AWS Config rules that are used
as data source mappings in this standard framework, download the [AuditManager_ConfigDataSourceMappings_AWS-Audit-Manager-Sample-Framework.zip](samples/AuditManager_ConfigDataSourceMappings_AWS-Audit-Manager-Sample-Framework.md "samples/AuditManager_ConfigDataSourceMappings_AWS-Audit-Manager-Sample-Framework.md")
file.

## Next steps

For instructions on how to view detailed information about this framework, including the
list of standard controls that it contains, see [Reviewing a framework in AWS Audit Manager](review-frameworks.md "review-frameworks.md").

For instructions on how to create an assessment using this framework, see [Creating an assessment in AWS Audit Manager](create-assessments.md "create-assessments.md").

For instructions on how to customize this framework to support your specific
requirements, see [Making an editable copy of an
existing framework in AWS Audit Manager](create-custom-frameworks-from-existing.md "create-custom-frameworks-from-existing.md").
