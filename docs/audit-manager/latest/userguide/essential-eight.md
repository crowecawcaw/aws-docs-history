# ACSC Essential Eight

AWS Audit Manager provides a prebuilt standard framework that supports the Australian Cyber
Security Center (ACSC) Essential Eight.

###### Topics

- [What is the ACSC Essential Eight?](#what-is-essential-eight "#what-is-essential-eight")
- [Using this framework](#framework-essential-eight "#framework-essential-eight")
- [Next steps](#next-steps-essential-eight "#next-steps-essential-eight")
- [Additional resources](#resources-essential-eight "#resources-essential-eight")

## What is the ACSC Essential Eight?

The ACSC is the Australian government's lead agency for cyber security. To protect
against cyber threats, the ACSC recommends that organizations implement eight essential
mitigation strategies from the ACSC’s _Strategies to Mitigate Cyber
Security Incidents_ as a baseline. This baseline, known as the Essential
Eight, makes it much harder for adversaries to compromise systems.

As the Essential Eight outlines a minimum set of preventative measures, your
organization needs to implement additional measures where it is warranted by your
environment. Further, while the Essential Eight can help to mitigate the majority of cyber
threats, it will not mitigate all cyber threats. As such, additional mitigation strategies
and security controls need to be considered, including those from the _Strategies to Mitigate Cyber Security Incidents_ and the
_Information Security Manual_ (ISM).

The [Essential Eight](https://www.cyber.gov.au/acsc/view-all-content/essential-eight "https://www.cyber.gov.au/acsc/view-all-content/essential-eight") by the [ACSC](https://www.cyber.gov.au/ "https://www.cyber.gov.au/") is
licensed under a [Creative
Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/ "https://creativecommons.org/licenses/by/4.0/") and copyright information can be
found at [ACSC | Copyright](https://www.cyber.gov.au/acsc/copyright "https://www.cyber.gov.au/acsc/copyright"). ©
Commonwealth of Australia 2022.

## Using this framework

You can use the Essential Eight standard framework in AWS Audit Manager to help you prepare for
audits. This framework includes a prebuilt collection of controls with descriptions and
testing procedures. These controls are grouped into control sets according to Essential
Eight requirements. You can also customize this framework and its controls to support
internal audits with specific requirements.

Using the framework as a starting point, you can create an Audit Manager assessment and start
collecting evidence that’s relevant for your audit. After you create an assessment, Audit Manager
starts to assess your AWS resources. It does this based on the controls that are defined
in the Essential Eight framework. When it's time for an audit, you—or a
delegate of your choice—can review the evidence that Audit Manager collected. Either, you
can browse the evidence folders in your assessment and choose which evidence you want to
include in your assessment report. Or, if you enabled evidence finder, you can search for
specific evidence and export it in CSV format, or create an assessment report from your
search results. Either way, you can use this assessment report to show that your controls
are working as intended.

The framework details are as follows:

| Framework name in AWS Audit Manager                     | Number of automated controls | Number of manual controls | Number of control sets |
| ------------------------------------------------------- | ---------------------------- | ------------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Australian Cyber Security Center (ACSC) Essential Eight | 61                           | 132                       | 3                      | ###### Important To ensure that this framework collects the intended evidence from AWS Security Hub, make sure that you enabled all standards in Security Hub. To ensure that this framework collects the intended evidence from AWS Config, make sure that you enable the necessary AWS Config rules. To review the AWS Config rules that are used as data source mappings in this standard framework, download the [AuditManager_ConfigDataSourceMappings_Australian-Cyber-Security-Center-(ACSC)-Essential-Eight.zip](<samples/AuditManager_ConfigDataSourceMappings_Australian-Cyber-Security-Center-(ACSC)-Essential-Eight.md> "samples/AuditManager_ConfigDataSourceMappings_Australian-Cyber-Security-Center-(ACSC)-Essential-Eight.md") file. The controls in this AWS Audit Manager framework aren't intended to verify if your systems are compliant with the Essential Eight controls. Moreover, they can't guarantee that you'll pass an ACSC audit. AWS Audit Manager doesn't automatically check procedural controls that require manual evidence collection. ## Next steps For instructions on how to view detailed information about this framework, including the list of standard controls that it contains, see [Reviewing a framework in AWS Audit Manager](review-frameworks.md "review-frameworks.md"). For instructions on how to create an assessment using this framework, see [Creating an assessment in AWS Audit Manager](create-assessments.md "create-assessments.md"). For instructions on how to customize this framework to support your specific requirements, see [Making an editable copy of an existing framework in AWS Audit Manager](create-custom-frameworks-from-existing.md "create-custom-frameworks-from-existing.md"). ## Additional resources <br>• [ACSC Essential Eight](https://www.cyber.gov.au/acsc/view-all-content/essential-eight "https://www.cyber.gov.au/acsc/view-all-content/essential-eight") |
