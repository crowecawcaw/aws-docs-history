# PCI DSS V4.0

AWS Audit Manager provides a prebuilt framework that supports the Payment Card Industry Data
Security Standard (PCI DSS) v4.0.

###### Note

For information about PCI DSS v3.2.1 and the Audit Manager framework that supports it, see
[PCI DSS V3.2.1](PCI.md "PCI.md").

###### Topics

- [What is PCI DSS?](#what-is-PCI-v4 "#what-is-PCI-v4")
- [Using this framework](#framework-PCI-v4 "#framework-PCI-v4")
- [Next steps](#next-steps-PCI-v4 "#next-steps-PCI-v4")
- [Additional resources](#resources-PCI-v4 "#resources-PCI-v4")

## What is PCI DSS?

The Payment Card Industry Data Security Standard (PCI DSS) is a global standard that
provides a baseline of technical and operational requirements for protecting payment data.
PCI DSS v4.0 is the next evolution of the standard.

PCI DSS was developed to encourage and enhance payment card account data security. It
also facilitates the broad adoption of consistent data security measures globally. It
provides a baseline of technical and operational requirements that are designed to protect
account data. Although it’s specifically designed to focus on environments with payment
card account data, you can also use PCI DSS to protect against threats and secure other
elements in the payment ecosystem.

The PCI Security Standards Council (PCI SSC) introduced many changes between PCI DSS
v3.2.1 and v4.0. These updates are broken into three categories:

1. **Evolving requirement** – Changes to ensure
   that the standard is up to date with emerging threats and technologies, and changes in
   the payment industry. Examples include new or modified requirements or testing
   procedures, or the removal of a requirement.
2. **Clarification or guidance** – Updates to
   wording, explanation, definition, additional guidance, or instruction to increase
   understanding or provide further information or guidance on a particular topic.
3. **Structure or format** – Reorganization of
   content, including combining, separating, and renumbering of requirements to align
   content.

## Using this framework to support your audit preparation

###### Note

This standard framework uses consolidated controls from Security Hub CSPM as a data source. To
successfully collect evidence from consolidated controls, make sure that you [turned on the consolidated control findings setting in Security Hub CSPM](../../../securityhub/latest/userguide/controls-findings-create-update.md#turn-on-consolidated-control-findings "../../../securityhub/latest/userguide/controls-findings-create-update.md#turn-on-consolidated-control-findings"). For more
information about using Security Hub as a data source type, see [AWS Security Hub CSPM controls
supported by AWS Audit Manager](control-data-sources-ash.md "control-data-sources-ash.md").

You can use the PCI DSS V4.0 framework to help you prepare for audits. This framework
includes a prebuilt collection of controls with descriptions and testing procedures. These
controls are grouped into control sets according to PCI DSS V4.0 requirements. You can
also customize this framework and its controls to support internal audits with specific
requirements.

Using the framework as a starting point, you can create an Audit Manager assessment and start
collecting evidence that’s relevant for your audit. After you create an assessment, Audit Manager
starts to assess your AWS resources. It does this based on the controls that are defined
in the PCI DSS V4.0 framework. When it's time for an audit, you—or a delegate
of your choice—can review the evidence that Audit Manager collected. Either, you can browse
the evidence folders in your assessment and choose which evidence you want to include in
your assessment report. Or, if you enabled evidence finder, you can search for specific
evidence and export it in CSV format, or create an assessment report from your search
results. Either way, you can use this assessment report to show that your controls are
working as intended.

The framework details are as follows:

| Framework name in AWS Audit Manager                         | Number of automated controls | Number of manual controls | Number of control sets |
| ----------------------------------------------------------- | ---------------------------- | ------------------------- | ---------------------- |
| Payment Card Industry Data Security Standard (PCI DSS) v4.0 | 40                           | 240                       | 15                     |

###### Important

To ensure that this framework collects the intended evidence from AWS Security Hub CSPM, make sure
that you enabled all standards in Security Hub CSPM.

To ensure that this framework collects the intended evidence from AWS Config, make sure
that you enable the necessary AWS Config rules. To review the AWS Config rules that are used
as data source mappings in this standard framework, download the [AuditManager_ConfigDataSourceMappings_PCI-DSS-v4.0.zip](samples/AuditManager_ConfigDataSourceMappings_PCI-DSS-v4.0.md "samples/AuditManager_ConfigDataSourceMappings_PCI-DSS-v4.0.md") file.

The controls in this AWS Audit Manager framework aren't intended to verify if your systems are
compliant with the PCI DSS standard. Moreover, they can't guarantee that you'll pass a PCI
DSS audit. AWS Audit Manager doesn't automatically check procedural controls that require manual
evidence collection.

## Next steps

For instructions on how to view detailed information about this framework, including the
list of standard controls that it contains, see [Reviewing a framework in AWS Audit Manager](review-frameworks.md "review-frameworks.md").

For instructions on how to create an assessment using this framework, see [Creating an assessment in AWS Audit Manager](create-assessments.md "create-assessments.md").

For instructions on how to customize this framework to support your specific
requirements, see [Making an editable copy of an existing framework in AWS Audit Manager](create-custom-frameworks-from-existing.md "create-custom-frameworks-from-existing.md").

## Additional resources

- [PCI
  DSS v4.0 Resource Hub](https://blog.pcisecuritystandards.org/pci-dss-v4-0-resource-hub "https://blog.pcisecuritystandards.org/pci-dss-v4-0-resource-hub")
- [PCI Security Standards
  Council](https://www.pcisecuritystandards.org/ "https://www.pcisecuritystandards.org/")
- [PCI Security Standards Council Document Library](https://www.pcisecuritystandards.org/document_library?category=pcidss&document=pci_dss "https://www.pcisecuritystandards.org/document_library?category=pcidss&document=pci_dss").
- [AWS Compliance
  page for PCI DSS](https://aws.amazon.com/compliance/pci-dss-level-1-faqs/ "https://aws.amazon.com/compliance/pci-dss-level-1-faqs/")
- [Payment Card Industry Data Security Standard (PCI DSS) v4.0 on AWS Compliance
  Guide](https://d1.awsstatic.com/whitepapers/compliance/pci-dss-compliance-on-aws-v4-102023.pdf "https://d1.awsstatic.com/whitepapers/compliance/pci-dss-compliance-on-aws-v4-102023.pdf")
