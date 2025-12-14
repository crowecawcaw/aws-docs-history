# ACSC ISM 02 March 2023

AWS Audit Manager provides a prebuilt standard framework that supports the Australian Cyber
Security Center (ACSC) Information Security Manual (ISM).

###### Topics

- [What is the ACSC ISM?](#what-is-acsc-information-security-manual "#what-is-acsc-information-security-manual")
- [Using this framework](#framework-acsc-information-security-manual "#framework-acsc-information-security-manual")
- [Next steps](#next-steps-acsc-information-security-manual "#next-steps-acsc-information-security-manual")
- [Additional resources](#resources-acsc-information-security-manual "#resources-acsc-information-security-manual")

## What is the ACSC ISM?

The ACSC is the Australian government's lead agency for cyber security. The ACSC
produces the ISM, which functions as a set of cyber security principles. The purpose of
these principles is to provide strategic guidance on how an organization can protect their
systems and data from cyber threats. These cyber security principles are grouped into four
key activities: govern, protect, detect and respond. An organization should be able to
demonstrate that the cyber security principles are being adhered to within their
organization. The ISM is intended for Chief Information Security Officers, Chief
Information Officers, cyber security professionals, and information technology
managers.

The ISM framework is provided by the ACSC under a [Creative Commons Attribution 4.0
International License](https://creativecommons.org/licenses/by/4.0/ "https://creativecommons.org/licenses/by/4.0/"), and copyright information can be found at [ACSC | Copyright](https://www.cyber.gov.au/acsc/copyright "https://www.cyber.gov.au/acsc/copyright"). © Commonwealth
of Australia 2022.

## Using this framework

You can use the ACSC ISM standard framework in AWS Audit Manager to help you prepare for
audits. This framework includes a prebuilt collection of controls with descriptions and
testing procedures. These controls are grouped into control sets according to ACSC ISM
requirements. You can also customize this framework and its controls to support internal
audits with specific requirements.

Using the framework as a starting point, you can create an Audit Manager assessment and start
collecting evidence that’s relevant for your audit. After you create an assessment, Audit Manager
starts to assess your AWS resources. It does this based on the controls that are defined
in the ACSC ISM framework. When it's time for an audit, you—or a delegate of
your choice—can review the evidence that Audit Manager collected. Either, you can browse the
evidence folders in your assessment and choose which evidence you want to include in your
assessment report. Or, if you enabled evidence finder, you can search for specific
evidence and export it in CSV format, or create an assessment report from your search
results. Either way, you can use this assessment report to show that your controls are
working as intended.

The framework details are as follows:

| Framework name in AWS Audit Manager                                                        | Number of automated controls | Number of manual controls | Number of control sets |
| ------------------------------------------------------------------------------------------ | ---------------------------- | ------------------------- | ---------------------- |
| Australian Cyber Security Center (ACSC) Information Security Manual (ISM) 02<br>March 2023 | 88                           | 789                       | 22                     |

###### Important

To ensure that this framework collects the intended evidence from AWS Security Hub CSPM, make sure
that you enabled all standards in Security Hub CSPM.

To ensure that this framework collects the intended evidence from AWS Config, make sure
that you enable the necessary AWS Config rules. To review the AWS Config rules that are used
as data source mappings in this standard framework, download the [AuditManager_ConfigDataSourceMappings_Australian-Cyber-Security-Center-(ACSC)-Information-Security-Manual-(ISM)-02-March-2023.zip](<samples/AuditManager_ConfigDataSourceMappings_Australian-Cyber-Security-Center-(ACSC)-Information-Security-Manual-(ISM)-02-March-2023.md> "samples/AuditManager_ConfigDataSourceMappings_Australian-Cyber-Security-Center-(ACSC)-Information-Security-Manual-(ISM)-02-March-2023.md")
file.

The controls in this AWS Audit Manager framework aren't intended to verify if your systems are
compliant with the ACSC Information Security Manual controls. Moreover, they can't
guarantee that you'll pass an ACSC audit. AWS Audit Manager doesn't automatically check procedural
controls that require manual evidence collection.

## Next steps

For instructions on how to view detailed information about this framework, including the
list of standard controls that it contains, see [Reviewing a framework in AWS Audit Manager](review-frameworks.md "review-frameworks.md").

For instructions on how to create an assessment using this framework, see [Creating an assessment in AWS Audit Manager](create-assessments.md "create-assessments.md").

For instructions on how to customize this framework to support your specific
requirements, see [Making an editable copy of an
existing framework in AWS Audit Manager](create-custom-frameworks-from-existing.md "create-custom-frameworks-from-existing.md").

## Additional resources

- [ACSC Information
  Security Manual](https://www.cyber.gov.au/acsc/view-all-content/ism "https://www.cyber.gov.au/acsc/view-all-content/ism")
