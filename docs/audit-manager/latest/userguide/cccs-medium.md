# CCCS Medium Cloud Control

AWS Audit Manager provides a prebuilt standard framework that supports the Canadian Centre for
Cyber Security (CCCS) Medium Cloud Control.

###### Topics

- [What is the CCCS?](#what-is-cccs-medium "#what-is-cccs-medium")
- [Using this framework](#framework-cccs-medium "#framework-cccs-medium")
- [Next steps](#next-steps-cccs-medium "#next-steps-cccs-medium")

## What is the CCCS?

The CCCS is Canada’s authoritative source of cybersecurity expert guidance, services,
and support. CCCS provides this expertise to Canadian governments, industry, and the
general public. Their rigorous assessments of cloud service providers are relied on by
Canadian public sector organizations across the country to make informed cloud procurement
decisions.

The CCCS Medium Cloud Control Profile replaced the government of Canada's PROTECTED B
/ Medium Integrity / Medium Availability (PBMM) profile in May 2020. The CCCS Medium Cloud
Security Control Profile is suitable if your organization uses public cloud services to
support business activities with medium confidentiality, integrity, and availability (AIC)
requirements. Workloads with medium AIC requirements mean that unauthorized disclosure,
modification, or loss of access to the information or services that are used by the
business activity can reasonably be expected to cause serious injury to an individual or
organization or limited injury to a group of individuals. Examples of these levels of
injury include the following:

- Significant effect on annual profit
- Loss of major accounts
- Loss of goodwill
- Clear compliance violation
- Privacy violation for hundreds or thousands of people
- Affects program performance
- Causing mental disorder or illness
- Sabotage
- Damage to reputation
- Individual financial hardship

## Using this framework

You can use the AWS Audit Manager framework for CCCS Medium Cloud Control to help you prepare
for audits. This framework includes a prebuilt collection of controls with descriptions
and testing procedures. These controls are grouped into control sets according to CCCS
requirements. You can also customize this framework and its controls to support internal
audits with specific requirements.

Using the framework as a starting point, you can create an Audit Manager assessment and start
collecting evidence that’s relevant for a CCCS Medium Cloud Control audit. In your
assessment, you can specify the AWS accounts that you want to include in the scope of
your audit. After you create an assessment, Audit Manager starts to assess your AWS resources. It
does this based on the controls that are defined in the CCCS Medium Cloud Control
framework. When it's time for an audit, you—or a delegate of your
choice—can review the evidence that Audit Manager collected. Either, you can browse the
evidence folders in your assessment and choose which evidence you want to include in your
assessment report. Or, if you enabled evidence finder, you can search for specific
evidence and export it in CSV format, or create an assessment report from your search
results. Either way, you can use this assessment report to show that your controls are
working as intended.

The framework details are as follows:

| Framework name in AWS Audit Manager                            | Number of automated controls | Number of manual controls | Number of control sets |
| -------------------------------------------------------------- | ---------------------------- | ------------------------- | ---------------------- |
| Canadian Centre for Cyber Security (CCCS) Medium Cloud Control | 71                           | 282                       | 175                    |

###### Important

To ensure that this framework collects the intended evidence from AWS Security Hub CSPM, make sure
that you enabled all standards in Security Hub CSPM.

To ensure that this framework collects the intended evidence from AWS Config, make sure
that you enable the necessary AWS Config rules. To review the AWS Config rules that are used
as data source mappings in this standard framework, download the [AuditManager_AuditManager_ConfigDataSourceMappings_CCCS-Medium-Cloud-Control.zip](samples/AuditManager_ConfigDataSourceMappings_CCCS-Medium-Cloud-Control.md "samples/AuditManager_ConfigDataSourceMappings_CCCS-Medium-Cloud-Control.md")
file.

The controls in this AWS Audit Manager framework aren't intended to verify if your systems are
compliant with the CCCS Medium Cloud Control requirements. Moreover, they can't guarantee
that you'll pass an CCCS audit. AWS Audit Manager doesn't automatically check procedural controls
that require manual evidence collection.

## Next steps

For instructions on how to view detailed information about this framework, including the
list of standard controls that it contains, see [Reviewing a framework in AWS Audit Manager](review-frameworks.md "review-frameworks.md").

For instructions on how to create an assessment using this framework, see [Creating an assessment in AWS Audit Manager](create-assessments.md "create-assessments.md").

For instructions on how to customize this framework to support your specific
requirements, see [Making an editable copy of an
existing framework in AWS Audit Manager](create-custom-frameworks-from-existing.md "create-custom-frameworks-from-existing.md").
