# Title 21 CFR Part 11

AWS Audit Manager provides a prebuilt standard framework that supports Title 21 of the Code of
Federal Regulations (CFR) Part 11, Electronic records; Electronic Signatures - Scope and
Application 24 May 2023.

###### Topics

- [What is Title 21 of the CFR Part 11?](#what-is-GxP "#what-is-GxP")
- [Using this framework](#framework-GxP "#framework-GxP")
- [Next steps](#next-steps-GxP "#next-steps-GxP")
- [Additional resources](#resources-gxp-21-cfr-part-11 "#resources-gxp-21-cfr-part-11")

## What is Title 21 of the CFR Part 11?

GxP refers to the regulations and guidelines that are applicable to life sciences
organizations that make food and medical products. Medical products that fall under this
include medicines, medical devices, and medical software applications. The overall intent
of GxP requirements is to ensure that food and medical products are safe for consumers.
It's also to ensure the integrity of data that's used to make product-related safety
decisions.

In the United States, GxP regulations are enforced by the US Food and Drug
Administration (FDA), and are contained in Title 21 of the Code of Federal Regulations (21
CFR). Within 21 CFR, Part 11 contains the requirements for computer systems that create,
modify, maintain, archive, retrieve, or distribute electronic records and electronic
signatures in support of GxP-regulated activities. Part 11 was created to permit the
adoption of new information technologies by FDA-regulated life sciences organizations,
while simultaneously providing a framework to ensure that the electronic GxP data is
trustworthy and reliable.

For a comprehensive approach to using the AWS Cloud for GxP systems, see the [Considerations for Using AWS Products in GxP Systems](https://d1.awsstatic.com/whitepapers/compliance/Using_AWS_in_GxP_Systems.pdf "https://d1.awsstatic.com/whitepapers/compliance/Using_AWS_in_GxP_Systems.pdf") whitepaper.

## Using this framework

You can use the Title 21 CFR Part 11 framework to help you prepare for audits. This
framework includes a prebuilt collection of controls with descriptions and testing
procedures. These controls are grouped into control sets according to CFR requirements.
You can also customize this framework and its controls to support internal audits with
specific requirements.

Using the framework as a starting point, you can create an Audit Manager assessment and start
collecting evidence that’s relevant for your audit. After you create an assessment, Audit Manager
starts to assess your AWS resources. It does this based on the controls that are defined
in the Title 21 CFR Part 11 framework. When it's time for an audit, you—or a
delegate of your choice—can review the evidence that Audit Manager collected. Either, you
can browse the evidence folders in your assessment and choose which evidence you want to
include in your assessment report. Or, if you enabled evidence finder, you can search for
specific evidence and export it in CSV format, or create an assessment report from your
search results. Either way, you can use this assessment report to show that your controls
are working as intended.

The framework details are as follows:

| Framework name in AWS Audit Manager                                                                                                     | Number of automated controls | Number of manual controls | Number of control sets |
| --------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- | ------------------------- | ---------------------- |
| Title 21 Code of Federal Regulations (CFR) Part 11, Electronic records;<br>Electronic Signatures<br>• Scope and Application 24 May 2023 | 6                            | 19                        | 2                      |

###### Important

To ensure that this framework collects the intended evidence from AWS Security Hub CSPM, make sure
that you enabled all standards in Security Hub CSPM.

To ensure that this framework collects the intended evidence from AWS Config, make sure
that you enable the necessary AWS Config rules. To review the AWS Config rules that are used
as data source mappings in this standard framework, download the [AuditManager_ConfigDataSourceMappings_Title-21-CFR-Part-11.zip](samples/AuditManager_ConfigDataSourceMappings_Title-21-CFR-Part-11.md "samples/AuditManager_ConfigDataSourceMappings_Title-21-CFR-Part-11.md") file.

The controls in this AWS Audit Manager framework aren't intended to verify if your systems are
compliant with GxP regulations. Moreover, they can't guarantee that you'll pass an audit.
AWS Audit Manager doesn't automatically check procedural controls that require manual evidence
collection.

## Next steps

For instructions on how to view detailed information about this framework, including the
list of standard controls that it contains, see [Reviewing a framework in AWS Audit Manager](review-frameworks.md "review-frameworks.md").

For instructions on how to create an assessment using this framework, see [Creating an assessment in AWS Audit Manager](create-assessments.md "create-assessments.md").

For instructions on how to customize this framework to support your specific
requirements, see [Making an editable copy of an
existing framework in AWS Audit Manager](create-custom-frameworks-from-existing.md "create-custom-frameworks-from-existing.md").

## Additional resources

- [AWS Compliance
  page for GxP](https://aws.amazon.com/compliance/gxp-part-11-annex-11/ "https://aws.amazon.com/compliance/gxp-part-11-annex-11/")
- [Considerations for Using AWS Products in GxP Systems](https://d1.awsstatic.com/whitepapers/compliance/Using_AWS_in_GxP_Systems.pdf "https://d1.awsstatic.com/whitepapers/compliance/Using_AWS_in_GxP_Systems.pdf")
