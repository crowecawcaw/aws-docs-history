# HIPAA Omnibus Final Rule

AWS Audit Manager provides a prebuilt standard framework that supports the Health Insurance
Portability and Accountability Act (HIPAA) Omnibus Final Rule.

###### Note

For information about the HIPAA Security Rule 2003 and the AWS Audit Manager framework that
supports this standard, see [HIPAA Security Rule: Feb 2003](HIPAA.md "HIPAA.md").

###### Topics

- [What is HIPAA and the HIPAA Final Omnibus
  Security Rule?](#what-is-HIPAA-omnibus-rule "#what-is-HIPAA-omnibus-rule")
- [Using this framework](#framework-HIPAA "#framework-HIPAA")
- [Next steps](#next-steps-HIPAA-omnibus-rule "#next-steps-HIPAA-omnibus-rule")
- [Additional resources](#resources-HIPAA-omnibus-rule "#resources-HIPAA-omnibus-rule")

## What is HIPAA and the HIPAA Final Omnibus

Security Rule?

HIPAA is legislation that helps US workers to retain health insurance coverage when
they change or lose jobs. The legislation also seeks to encourage electronic health
records to improve the efficiency and quality of the US healthcare system through improved
information sharing.

Along with increasing the use of electronic medical records, HIPAA includes provisions
to protect the security and privacy of protected health information (PHI). PHI includes a
very wide set of personally identifiable health and health-related data. This includes
insurance and billing information, diagnosis data, clinical care data, and lab results
such as images and test results.

The HIPAA Final Omnibus Security Rule, which became effective in 2013, implements a
number of updates to all of the previously passed rules. The modifications to the
Security, Privacy, Breach Notification, and Enforcement Rules were intended to enhance
confidentiality and security in data sharing.

HIPAA rules apply to covered entities. These include hospitals, medical services
providers, employer-sponsored health plans, research facilities, and insurance companies
that deal directly with patients and patient data. As part of the omnibus updates, many of
the HIPAA rules that apply to covered entities also now apply to business
associates.

For more information about how HIPAA and HITECH protect health information, see the
[Health Information
Privacy](https://www.hhs.gov/hipaa/for-professionals/index.html "https://www.hhs.gov/hipaa/for-professionals/index.html") webpage from the U.S. Department of Health and Human Services.

A growing number of healthcare providers, payers, and IT professionals are using AWS
utility-based cloud services to process, store, and transmit protected health information
(PHI). AWS enables covered entities and their business associates subject to HIPAA to
use the secure AWS environment to process, maintain, and store protected health
information. For instructions on how you can use AWS for the processing and storage of
health information, see the [Architecting for HIPAA Security and Compliance on Amazon Web Services](https://d1.awsstatic.com/whitepapers/compliance/AWS_HIPAA_Compliance_Whitepaper.pdf "https://d1.awsstatic.com/whitepapers/compliance/AWS_HIPAA_Compliance_Whitepaper.pdf") whitepaper.

## Using this framework

You can use the HIPAA Omnibus Final Rule framework to help you prepare for audits.
This framework includes a prebuilt collection of controls with descriptions and testing
procedures. These controls are grouped into control sets according to HIPAA requirements.
You can also customize this framework and its controls to support internal audits with
specific requirements.

Using the framework as a starting point, you can create an Audit Manager assessment and start
collecting evidence that’s relevant for your audit. After you create an assessment, Audit Manager
starts to assess your AWS resources. It does this based on the controls that are defined
in the HIPAA framework. When it's time for an audit, you—or a delegate of your
choice—can review the evidence that Audit Manager collected. Either, you can browse the
evidence folders in your assessment and choose which evidence you want to include in your
assessment report. Or, if you enabled evidence finder, you can search for specific
evidence and export it in CSV format, or create an assessment report from your search
results. Either way, you can use this assessment report to show that your controls are
working as intended.

The framework details are as follows:

| Framework name in AWS Audit Manager                                               | Number of automated controls | Number of manual controls | Number of control sets |
| --------------------------------------------------------------------------------- | ---------------------------- | ------------------------- | ---------------------- |
| Health Insurance Portability and Accountability Act (HIPAA) Omnibus Final<br>Rule | 21                           | 53                        | 5                      |

###### Important

To ensure that this framework collects the intended evidence from AWS Security Hub, make sure
that you enabled all standards in Security Hub.

To ensure that this framework collects the intended evidence from AWS Config, make sure
that you enable the necessary AWS Config rules. To review the AWS Config rules that are used
as data source mappings in this standard framework, download the [AuditManager_ConfigDataSourceMappings_HIPAA-Omnibus-Final-Rule.zip](samples/AuditManager_ConfigDataSourceMappings_HIPAA-Omnibus-Final-Rule.md "samples/AuditManager_ConfigDataSourceMappings_HIPAA-Omnibus-Final-Rule.md") file.

The controls in this AWS Audit Manager framework aren't intended to verify if your systems are
compliant with the HIPAA standard. Moreover, they can't guarantee that you'll pass a HIPAA
audit. AWS Audit Manager doesn't automatically check procedural controls that require manual
evidence collection.

## Next steps

For instructions on how to view detailed information about this framework, including the
list of standard controls that it contains, see [Reviewing a framework in AWS Audit Manager](review-frameworks.md "review-frameworks.md").

For instructions on how to create an assessment using this framework, see [Creating an assessment in AWS Audit Manager](create-assessments.md "create-assessments.md").

For instructions on how to customize this framework to support your specific
requirements, see [Making an editable copy of an
existing framework in AWS Audit Manager](create-custom-frameworks-from-existing.md "create-custom-frameworks-from-existing.md").

## Additional resources

- [Health
  Information Privacy](https://www.hhs.gov/hipaa/for-professionals/index.html "https://www.hhs.gov/hipaa/for-professionals/index.html") from the U.S. Department of Health and Human
  Service
- [Omnibus HIPAA Rulemaking](https://www.hhs.gov/hipaa/for-professionals/privacy/laws-regulations/combined-regulation-text/omnibus-hipaa-rulemaking/index.html "https://www.hhs.gov/hipaa/for-professionals/privacy/laws-regulations/combined-regulation-text/omnibus-hipaa-rulemaking/index.html") from the U.S. Department of Health and Human
  Service
- [Architecting for HIPAA Security and Compliance on Amazon Web Services](https://d1.awsstatic.com/whitepapers/compliance/AWS_HIPAA_Compliance_Whitepaper.pdf "https://d1.awsstatic.com/whitepapers/compliance/AWS_HIPAA_Compliance_Whitepaper.pdf")
- [AWS Compliance page
  for HIPAA](https://aws.amazon.com/compliance/hipaa-compliance/ "https://aws.amazon.com/compliance/hipaa-compliance/")
