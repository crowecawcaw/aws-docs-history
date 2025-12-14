# PCI DSS V3.2.1

AWS Audit Manager provides a prebuilt standard framework that supports the Payment Card Industry
Data Security Standard (PCI DSS) v3.2.1.

###### Note

For information about PCI DSS v4 and the Audit Manager framework that supports it, see [PCI DSS V4.0](pci-v4.md "pci-v4.md").

###### Topics

- [What is PCI DSS?](#what-is-PCI "#what-is-PCI")
- [Using this framework](#framework-PCI "#framework-PCI")
- [Next steps](#next-steps-PCI "#next-steps-PCI")
- [Additional resources](#resources-PCI-DSS "#resources-PCI-DSS")

## What is PCI DSS?

PCI DSS is a proprietary information security standard. It's administered by the
[PCI Security Standards
Council](https://www.pcisecuritystandards.org/ "https://www.pcisecuritystandards.org/"), which was founded by American Express, Discover Financial Services, JCB
International, MasterCard Worldwide, and Visa Inc. PCI DSS applies to entities that store,
process, or transmit cardholder data (CHD) or sensitive authentication data (SAD). This
includes, but isn't limited to, merchants, processors, acquirers, issuers, and service
providers. The PCI DSS is mandated by the card brands and administered by the Payment Card
Industry Security Standards Council.

AWS is certified as a PCI DSS Level 1 Service Provider, which is the highest level
of assessment available. The compliance assessment was conducted by Coalfire Systems Inc.,
an independent Qualified Security Assessor (QSA). The PCI DSS Attestation of Compliance
(AOC) and Responsibility Summary are available to you through AWS Artifact. This is a
self-service portal for on-demand access to AWS compliance reports. Sign in to [AWS Artifact in the AWS Management Console](https://console.aws.amazon.com/artifact "https://console.aws.amazon.com/artifact"), or learn
more at [Getting Started with
AWS Artifact](https://aws.amazon.com/artifact/getting-started/ "https://aws.amazon.com/artifact/getting-started/").

You can download the PCI DSS standard from the [PCI Security Standards Council Document Library](https://www.pcisecuritystandards.org/document_library?category=pcidss&document=pci_dss "https://www.pcisecuritystandards.org/document_library?category=pcidss&document=pci_dss").

## Using this framework to support your audit

preparation

You can use the _PCI DSS V3.2.1_ framework to help
you prepare for audits. This framework includes a prebuilt collection of controls with
descriptions and testing procedures. These controls are grouped into control sets
according to PCI DSS requirements. You can also customize this framework and its controls
to support internal audits with specific requirements.

Using the framework as a starting point, you can create an Audit Manager assessment and start
collecting evidence that’s relevant for your audit. After you create an assessment, Audit Manager
starts to assess your AWS resources. It does this based on the controls that are defined
in the PCI DSS V3.2.1 framework. When it's time for an audit, you—or a
delegate of your choice—can review the evidence that Audit Manager collected. Either, you
can browse the evidence folders in your assessment and choose which evidence you want to
include in your assessment report. Or, if you enabled evidence finder, you can search for
specific evidence and export it in CSV format, or create an assessment report from your
search results. Either way, you can use this assessment report to show that your controls
are working as intended.

The framework details are as follows:

| Framework name in AWS Audit Manager                           | Number of automated controls | Number of manual controls | Number of control sets |
| ------------------------------------------------------------- | ---------------------------- | ------------------------- | ---------------------- |
| Payment Card Industry Data Security Standard (PCI DSS) v3.2.1 | 38                           | 246                       | 15                     |

###### Important

To ensure that this framework collects the intended evidence from AWS Security Hub CSPM, make sure
that you enabled all standards in Security Hub CSPM.

To ensure that this framework collects the intended evidence from AWS Config, make sure
that you enable the necessary AWS Config rules. To review the AWS Config rules that are used
as data source mappings in this standard framework, download the [AuditManager_ConfigDataSourceMappings_PCI-DSS-v3.2.1.zip](samples/AuditManager_ConfigDataSourceMappings_PCI-DSS-v3.2.1.md "samples/AuditManager_ConfigDataSourceMappings_PCI-DSS-v3.2.1.md") file.

The controls in this AWS Audit Manager framework aren't intended to verify if your systems are
compliant with the PCI DSS standard. Moreover, they can't guarantee that you'll pass a PCI
DSS audit. AWS Audit Manager doesn't automatically check procedural controls that require manual
evidence collection.

## Next steps

For instructions on how to view detailed information about this framework, including the
list of standard controls that it contains, see [Reviewing a framework in AWS Audit Manager](review-frameworks.md "review-frameworks.md").

For instructions on how to create an assessment using this framework, see [Creating an assessment in AWS Audit Manager](create-assessments.md "create-assessments.md").

For instructions on how to customize this framework to support your specific
requirements, see [Making an editable copy of an
existing framework in AWS Audit Manager](create-custom-frameworks-from-existing.md "create-custom-frameworks-from-existing.md").

## Additional resources

- [PCI Security Standards
  Council](https://www.pcisecuritystandards.org/ "https://www.pcisecuritystandards.org/")
- [PCI Security Standards Council Document Library](https://www.pcisecuritystandards.org/document_library?category=pcidss&document=pci_dss "https://www.pcisecuritystandards.org/document_library?category=pcidss&document=pci_dss").
- [AWS Compliance
  page for PCI DSS](https://aws.amazon.com/compliance/pci-dss-level-1-faqs/ "https://aws.amazon.com/compliance/pci-dss-level-1-faqs/")
