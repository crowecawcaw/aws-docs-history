# Compliance validation for IAM Identity Center

Third-party auditors assess the security and compliance of AWS services such as
 AWS IAM Identity Center as part of multiple AWS compliance programs.

To learn whether an AWS service is within the scope of specific compliance programs, see [AWS services in Scope by Compliance
 Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/") and choose the compliance program that you are interested in. For general information, see [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/").

You can download third-party audit reports using AWS Artifact. For more information, see [Downloading Reports in AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/downloading-documents.html "https://docs.aws.amazon.com/artifact/latest/ug/downloading-documents.html").

Your compliance responsibility when using AWS services is determined by the sensitivity
 of your data, your company's compliance objectives, and applicable laws and regulations. AWS provides the following resources to help with compliance:


* [Security Compliance & Governance](https://aws.amazon.com/solutions/security/security-compliance-governance/ "https://aws.amazon.com/solutions/security/security-compliance-governance/") – These solution implementation guides discuss architectural
 considerations and provide steps for deploying security and compliance features.
* [HIPAA Eligible Services Reference](https://aws.amazon.com/compliance/hipaa-eligible-services-reference/ "https://aws.amazon.com/compliance/hipaa-eligible-services-reference/") –
 Lists HIPAA eligible services. Not all AWS services are HIPAA eligible.
* [AWS Compliance
 Resources](https://aws.amazon.com/compliance/resources/ "https://aws.amazon.com/compliance/resources/") – This collection of workbooks and guides might apply to your industry and
 location.
* [AWS Customer Compliance Guides](https://d1.awsstatic.com/whitepapers/compliance/AWS_Customer_Compliance_Guides.pdf "https://d1.awsstatic.com/whitepapers/compliance/AWS_Customer_Compliance_Guides.pdf") – 
 Understand the shared responsibility model through the lens of compliance.
 The guides summarize the best practices for securing AWS services and map the
 guidance to security controls across multiple frameworks (including National Institute of Standards and Technology (NIST), Payment Card Industry Security Standards Council (PCI), and International Organization for Standardization (ISO)).
* [Evaluating
 Resources with Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html "https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html") in the *AWS Config Developer
 Guide* – The AWS Config service assesses how well your resource
 configurations comply with internal practices, industry guidelines, and
 regulations.
* [AWS Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html "https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html") – 
 This AWS service provides a comprehensive view of your security state within AWS. Security Hub uses security controls to evaluate your AWS 
 resources and to check your compliance against security industry standards and best practices. For a list of supported services and 
 controls, see [Security Hub controls reference](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-controls-reference.html "https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-controls-reference.html").
* [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html "https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html") – 
 This AWS service detects potential threats to your AWS accounts, workloads, containers, and data by monitoring your environment for suspicious and malicious activities. GuardDuty can help you address various compliance requirements, like PCI DSS, by meeting intrusion detection requirements mandated by certain compliance frameworks.
* [AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html "https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html") – This AWS service helps you continuously audit your AWS usage to simplify how you manage risk and compliance with regulations and industry standards.

## Supported compliance standards


IAM Identity Center has undergone auditing for the following standards and is eligible for use as
 part of solutions for which you need to obtain compliance certification. 




|  |  |
| --- | --- |
| Health Insurance Portability and Accountability Act (HIPAA) image | AWS has expanded its Health Insurance Portability and Accountability Act (HIPAA) compliance program to include IAM Identity Center as a [HIPAA eligible service](https://aws.amazon.com/compliance/hipaa-eligible-services-reference/ "https://aws.amazon.com/compliance/hipaa-eligible-services-reference/"). AWS offers a [HIPAA-focused whitepaper](https://docs.aws.amazon.com/whitepapers/latest/architecting-hipaa-security-and-compliance-on-aws/architecting-hipaa-security-and-compliance-on-aws.pdf "https://docs.aws.amazon.com/whitepapers/latest/architecting-hipaa-security-and-compliance-on-aws/architecting-hipaa-security-and-compliance-on-aws.pdf") for customers who want to learn more about how they can use AWS services to process and store health information. For more information, see [HIPAA compliance](https://aws.amazon.com/compliance/hipaa-compliance/ "https://aws.amazon.com/compliance/hipaa-compliance/"). |
| Information Security Registered Assessors Program (IRAP) image | The Information Security Registered Assessors Program (IRAP) enables Australian Government customers to ensure that appropriate compliance controls are in place and determine the appropriate responsibility model for addressing the requirements of the Australian Government Information Security Manual (ISM) produced by the Australian Cyber Security Centre (ACSC). For more information, see  [IRAP Resources](https://aws.amazon.com/compliance/irap/ "https://aws.amazon.com/compliance/irap/"). |
| Attestation of Compliance for Payment Card Industry (PCI) image | IAM Identity Center has an Attestation of Compliance for Payment Card Industry (PCI) Data Security Standard (DSS) version 3.2 at Service Provider Level 1. Customers who use AWS products and services to store, process, or transmit cardholder data can use the following identity sources in IAM Identity Center to manage their own PCI DSS compliance certification: <br>• Active Directory <br>• External identity provider The IAM Identity Center identity source is currently not compliant with PCI DSS. For more information about PCI DSS, including how to request a copy of the AWS PCI Compliance Package, see [PCI DSS level 1](http://aws.amazon.com/compliance/pci-dss-level-1-faqs/ "http://aws.amazon.com/compliance/pci-dss-level-1-faqs/").  |
| System and Organization Control (SOC) image | System & Organization Control (SOC) Reports are independent, third-party examination reports that demonstrate how IAM Identity Center achieves key compliance controls and objectives. These reports help you and your auditors to understand how controls support operations and compliance. There are three types of SOC reports: <br>• AWS SOC 1 Report - [Download with AWS Artifact](https://console.aws.amazon.com/artifact/home "https://console.aws.amazon.com/artifact/home") <br>• AWS SOC 2: Security, Availability, & Confidentiality Report - [Download with AWS Artifact](https://console.aws.amazon.com/artifact/home "https://console.aws.amazon.com/artifact/home") <br>• [AWS SOC 3: Security, Availability, & Confidentiality Report](https://d1.awsstatic.com/whitepapers/compliance/AWS_SOC3.pdf "https://d1.awsstatic.com/whitepapers/compliance/AWS_SOC3.pdf") IAM Identity Center is in scope for AWS SOC 1, SOC 2, and SOC 3 reports. For more information, see [SOC Compliance](https://aws.amazon.com/compliance/soc-faqs/ "https://aws.amazon.com/compliance/soc-faqs/"). |
