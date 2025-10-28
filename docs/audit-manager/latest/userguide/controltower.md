# AWS Control Tower Guardrails

AWS Audit Manager provides a prebuilt AWS Control Tower Guardrails framework to assist you with your audit
preparation.

###### Topics

- [What is AWS Control Tower?](#what-is-controltower "#what-is-controltower")
- [Using this framework](#framework-controltower "#framework-controltower")
- [Next steps](#next-steps-controltower "#next-steps-controltower")
- [Additional resources](#resources-controltower "#resources-controltower")

## What is AWS Control Tower?

AWS Control Tower is a management and governance service that you can use to navigate through
the setup process and governance requirements that are involved in creating a
multi-account AWS environment.

With AWS Control Tower, you can provision new AWS accounts that conform to your company- or
organization-wide policies in a few clicks. AWS Control Tower creates an _orchestration_ layer on your behalf that combines and integrates the
capabilities of several other [AWS services](../../../controltower/latest/userguide/integrated-services.md "../../../controltower/latest/userguide/integrated-services.md"). These services include AWS Organizations, AWS IAM Identity Center, and AWS service
Catalog. This helps streamline the process of setting up and governing a multi-account
AWS environment that's both secure and compliant.

The AWS Control Tower Guardrails framework contains all of the AWS Config Rules that are based on
guardrails from AWS Control Tower.

## Using this framework

You can use the _AWS Control Tower Guardrails_ framework to
help you prepare for audits. This framework includes a prebuilt collection of controls
with descriptions and testing procedures. These controls are grouped according to the
AWS Config Rules that are based on guardrails from AWS Control Tower. You can also customize this framework
and its controls to support internal audits with specific requirements.

Using the framework as a starting point, you can create an Audit Manager assessment and start
collecting evidence that’s relevant for an AWS Control Tower audit. After you create an assessment,
Audit Manager starts to assess your AWS resources. It does this based on the controls that are
defined in the AWS Control Tower Guardrails framework. When it's time for an audit,
you—or a delegate of your choice—can review the evidence that Audit Manager
collected. Either, you can browse the evidence folders in your assessment and choose which
evidence you want to include in your assessment report. Or, if you enabled evidence
finder, you can search for specific evidence and export it in CSV format, or create an
assessment report from your search results. Either way, you can use this assessment report
to show that your controls are working as intended.

The AWS Control Tower Guardrails framework details are as follows:

| Framework name in AWS Audit Manager | Number of automated controls | Number of manual controls | Number of control sets |
| ----------------------------------- | ---------------------------- | ------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS Control Tower Guardrails        | 14                           | 0                         | 5                      | ###### Important To ensure that this framework collects the intended evidence from AWS Config, make sure that you enable the necessary AWS Config rules. To review the AWS Config rules that are used as data source mappings in this standard framework, download the [AuditManager_ConfigDataSourceMappings_AWS-Control-Tower-Guardrails.zip](samples/AuditManager_ConfigDataSourceMappings_AWS-Control-Tower-Guardrails.md "samples/AuditManager_ConfigDataSourceMappings_AWS-Control-Tower-Guardrails.md") file. The controls in this AWS Audit Manager framework aren't intended to verify if your systems are compliant with AWS Control Tower Guardrails. Moreover, they can't guarantee that you'll pass an audit. ## Next steps For instructions on how to view detailed information about this framework, including the list of standard controls that it contains, see [Reviewing a framework in AWS Audit Manager](review-frameworks.md "review-frameworks.md"). For instructions on how to create an assessment using this framework, see [Creating an assessment in AWS Audit Manager](create-assessments.md "create-assessments.md"). For instructions on how to customize this framework to support your specific requirements, see [Making an editable copy of an existing framework in AWS Audit Manager](create-custom-frameworks-from-existing.md "create-custom-frameworks-from-existing.md"). ## Additional resources <br>• [AWS Control Tower service page](https://aws.amazon.com/controltower "https://aws.amazon.com/controltower") <br>• [AWS Control Tower user guide](../../../controltower/latest/userguide/what-is-control-tower.md "../../../controltower/latest/userguide/what-is-control-tower.md") |
