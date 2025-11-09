# NIST Cybersecurity Framework

v1.1

AWS Audit Manager provides a prebuilt framework that supports the NIST Cybersecurity Framework
(CSF) v1.1.

###### Note

- For information about the Audit Manager framework that supports NIST SP 800-53, see [NIST SP 800-53 Rev 5](NIST800-53r5.md "NIST800-53r5.md").
- For information about the Audit Manager framework that supports NIST SP 800-171, see [NIST SP 800-171 Rev 2](NIST-800-171-r2-1.md "NIST-800-171-r2-1.md").

###### Topics

- [What is the NIST Cybersecurity
  Framework?](#what-is-NIST-Cybersecurity-Framework-v1-1 "#what-is-NIST-Cybersecurity-Framework-v1-1")
- [Using this framework](#framework-NIST-Cybersecurity-Framework-v1-1 "#framework-NIST-Cybersecurity-Framework-v1-1")
- [Next steps](#next-steps-NIST-Cybersecurity-Framework-v1-1 "#next-steps-NIST-Cybersecurity-Framework-v1-1")
- [Additional resources](#resources-NIST-Cybersecurity-Framework-v1-1 "#resources-NIST-Cybersecurity-Framework-v1-1")

## What is the NIST Cybersecurity

Framework?

The [National Institute of Standards and Technology
(NIST)](https://www.nist.gov/ "https://www.nist.gov/") was founded in 1901 and is now part of the U.S. Department of Commerce.
NIST is one of the oldest physical science laboratories in the United States. The U.S.
Congress established the agency to improve what was at the time a second-rate measurement
infrastructure. The infrastructure was a major challenge to U.S. industrial
competitiveness, having lagged behind other economic powers like the U.K. and
Germany.

The United States depends on the reliable functioning of critical infrastructure.
Cybersecurity threats exploit the increased complexity and interconnectedness of critical
infrastructure systems. They put the security, economy, and public safety and health of
the United States at risk. Similar to financial and reputational risks, cybersecurity risk
affects a company’s bottom line. It can drive up costs and affect revenue. It can harm an
organization’s ability to innovate and to gain and maintain customers. Ultimately,
cybersecurity can amplify the overall risk management of an organization.

The NIST Cybersecurity Framework (CSF) is supported by governments and industries
worldwide as a recommended baseline for use by any organization, regardless of sector or
size. The NIST Cybersecurity Framework consists of three primary components: the framework
core, the profiles, and the implementation tiers. The framework core contains desired
cybersecurity activities and outcomes organized into 23 categories that cover the breadth
of cybersecurity objectives for an organization. The profiles contain an organization's
unique alignment of their organizational requirements and objectives, risk appetite, and
resources using the desired outcomes of the framework core. The implementation tiers
describe the degree to which an organization’s cybersecurity risk management practices
exhibit the characteristics defined in the framework core.

## Using this framework

You can use the NIST CSF v1.1 to help you prepare for audits. This framework includes
a prebuilt collection of controls with descriptions and testing procedures. These controls
are grouped into control sets according to NIST CSF requirements. Audit Manager currently supports
the framework core component. Audit Manager doesn't support the profile and implementation
components in this framework.

Using the framework as a starting point, you can create an Audit Manager assessment and start
collecting evidence that’s relevant for your audit. After you create an assessment, Audit Manager
starts to assess your AWS resources. It does this based on the controls that are defined
in the NIST CSF When it's time for an audit, you—or a delegate of your
choice—can review the evidence that Audit Manager collected. Either, you can browse the
evidence folders in your assessment and choose which evidence you want to include in your
assessment report. Or, if you enabled evidence finder, you can search for specific
evidence and export it in CSV format, or create an assessment report from your search
results. Either way, you can use this assessment report to show that your controls are
working as intended.

The framework details are as follows:

| Framework name in AWS Audit Manager     | Number of automated controls | Number of manual controls | Number of control sets |
| --------------------------------------- | ---------------------------- | ------------------------- | ---------------------- |
| NIST Cybersecurity Framework (CSF) v1.1 | 14                           | 94                        | 22                     |

###### Important

To ensure that this framework collects the intended evidence from AWS Security Hub, make sure
that you enabled all standards in Security Hub.

To ensure that this framework collects the intended evidence from AWS Config, make sure
that you enable the necessary AWS Config rules. To review the AWS Config rules that are used
as data source mappings in this standard framework, download the [AuditManager_ConfigDataSourceMappings_NIST-CSF-v1.1.zip](samples/AuditManager_ConfigDataSourceMappings_NIST-CSF-v1.1.md "samples/AuditManager_ConfigDataSourceMappings_NIST-CSF-v1.1.md") file.

The controls that are offered by Audit Manager aren't intended to verify if your systems are
compliant with the NIST CSF. Moreover, they can't guarantee that you'll pass a NIST audit.
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

- [National Institute of Standards and Technology
  (NIST)](https://www.nist.gov/ "https://www.nist.gov/")
- [NIST Computer Security Resource
  Center](http://csrc.nist.gov "http://csrc.nist.gov")
- [AWS Compliance page for
  NIST](https://aws.amazon.com/compliance/nist/ "https://aws.amazon.com/compliance/nist/")
- [NIST Cybersecurity Framework - Aligning to the NIST CSF in the AWS Cloud](https://d1.awsstatic.com/whitepapers/compliance/NIST_Cybersecurity_Framework_CSF.pdf "https://d1.awsstatic.com/whitepapers/compliance/NIST_Cybersecurity_Framework_CSF.pdf")
