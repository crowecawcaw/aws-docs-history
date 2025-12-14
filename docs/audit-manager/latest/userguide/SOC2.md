# SSAE-18 SOC 2

AWS Audit Manager provides a prebuilt standard framework that supports the Statement on Standards
for Attestations Engagement (SSAE) No. 18, Service Organizations Controls (SOC) Report 2.

###### Topics

- [What is SOC 2?](#what-is-SOC2 "#what-is-SOC2")
- [Using this framework](#framework-SOC2 "#framework-SOC2")
- [Next steps](#next-steps-SOC2 "#next-steps-SOC2")
- [Additional resources](#resources-SOC2 "#resources-SOC2")

## What is SOC 2?

SOC 2, defined by the [American Institute of Certified Public Accountants](https://en.wikipedia.org/wiki/American_Institute_of_Certified_Public_Accountants "https://en.wikipedia.org/wiki/American_Institute_of_Certified_Public_Accountants") (AICPA), is the name of a
set of reports that's produced during an audit. It's intended for use by service
organizations (organizations that provide information systems as a service to other
organizations) to issue validated reports of [internal controls](https://en.wikipedia.org/wiki/Internal_controls "https://en.wikipedia.org/wiki/Internal_controls") over
those information systems to the users of those services. The reports focus on controls
grouped into five categories known as _Trust Service
Principles_.

AWS SOC reports are independent third-party examination reports that demonstrate how
AWS achieves key compliance controls and objectives. The purpose of these reports is to
help you and your auditors understand the AWS controls established to support operations
and compliance. There are five AWS SOC reports:

- AWS SOC 1 Report, available to AWS customers from [AWS Artifact](https://aws.amazon.com/artifact/getting-started/ "https://aws.amazon.com/artifact/getting-started/").
- AWS SOC 2 Security, Availability & Confidentiality Report, available to
  AWS customers from [AWS Artifact](https://aws.amazon.com/artifact/getting-started/ "https://aws.amazon.com/artifact/getting-started/").
- AWS SOC 2 Security, Availability & Confidentiality Report available to AWS
  customers from [AWS Artifact](https://aws.amazon.com/artifact/getting-started/ "https://aws.amazon.com/artifact/getting-started/")
  (scope includes Amazon DocumentDB only).
- AWS SOC 2 Privacy Type I Report, available to AWS customers from [AWS Artifact](https://aws.amazon.com/artifact/getting-started/ "https://aws.amazon.com/artifact/getting-started/").
- AWS SOC 3 Security, Availability & Confidentiality Report, [publicly
  available as a whitepaper](https://d1.awsstatic.com/whitepapers/compliance/AWS_SOC3.pdf "https://d1.awsstatic.com/whitepapers/compliance/AWS_SOC3.pdf").

## Using this framework to support your audit

preparation

You can use this framework to help you prepare for audits. This framework includes a
prebuilt collection of controls with descriptions and testing procedures. These controls
are grouped into control sets according to SOC 2 requirements. You can also customize this
framework and its controls to support internal audits with specific requirements.

Using the framework as a starting point, you can create an Audit Manager assessment and start
collecting evidence that’s relevant for your audit. After you create an assessment, Audit Manager
starts to assess your AWS resources. It does this based on the controls that are defined
in the framework. When it's time for an audit, you—or a delegate of your
choice—can review the evidence that Audit Manager collected. Either, you can browse the
evidence folders in your assessment and choose which evidence you want to include in your
assessment report. Or, if you enabled evidence finder, you can search for specific
evidence and export it in CSV format, or create an assessment report from your search
results. Either way, you can use this assessment report to show that your controls are
working as intended.

The framework details are as follows:

| Framework name in AWS Audit Manager                                                                                | Number of automated controls | Number of manual controls | Number of control sets |
| ------------------------------------------------------------------------------------------------------------------ | ---------------------------- | ------------------------- | ---------------------- |
| Statement on Standards for Attestations Engagement (SSAE) No. 18, Service<br>Organizations Controls (SOC) Report 2 | 15                           | 46                        | 20                     |

###### Important

To ensure that this framework collects the intended evidence from AWS Security Hub CSPM, make sure
that you enabled all standards in Security Hub CSPM.

To ensure that this framework collects the intended evidence from AWS Config, make sure
that you enable the necessary AWS Config rules. To review the AWS Config rules that are used
as data source mappings in this standard framework, download the [AuditManager_ConfigDataSourceMappings_SSAE-No.-18-SOC-Report-2.zip](samples/AuditManager_ConfigDataSourceMappings_SSAE-No.-18-SOC-Report-2.md "samples/AuditManager_ConfigDataSourceMappings_SSAE-No.-18-SOC-Report-2.md") file.

The controls in this AWS Audit Manager framework aren't intended to verify if your systems are
compliant. Moreover, they can't guarantee that you'll pass an audit. AWS Audit Manager doesn't
automatically check procedural controls that require manual evidence collection.

## Next steps

For instructions on how to view detailed information about this framework, including the
list of standard controls that it contains, see [Reviewing a framework in AWS Audit Manager](review-frameworks.md "review-frameworks.md").

For instructions on how to create an assessment using this framework, see [Creating an assessment in AWS Audit Manager](create-assessments.md "create-assessments.md").

For instructions on how to customize this framework to support your specific
requirements, see [Making an editable copy of an
existing framework in AWS Audit Manager](create-custom-frameworks-from-existing.md "create-custom-frameworks-from-existing.md").

## Additional resources

- [AWS Compliance page for
  SOC](https://aws.amazon.com/compliance/soc-faqs/ "https://aws.amazon.com/compliance/soc-faqs/")
