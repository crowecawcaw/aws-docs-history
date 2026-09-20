

# Compliance validation for Amazon Quick
<a name="sec-compliance"></a>

Third-party auditors assess the security and compliance of Amazon Quick as part of multiple AWS compliance programs. Amazon Quick, across its web, desktop, and mobile clients, is in scope for the following programs:
+ Federal Risk and Authorization Management Program (FedRAMP)
+ Health Insurance Portability and Accountability Act (HIPAA)
+ Payment Card Industry Data Security Standard (PCI DSS)
+ System and Organization Controls (SOC) 1, SOC 2, and SOC 3
+ International Organization for Standardization (ISO) 9001, ISO 27001, ISO 27018, and ISO 27019
+ Cloud Computing Compliance Criteria Catalogue (C5) from the German Federal Office for Information Security (BSI)
+ Health Information Trust Alliance Common Security Framework (HITRUST CSF)

When a program lists Quick as in scope, the audits and assessments for that program include the service. In-scope status does not make your own workloads compliant. Under the [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/), you configure Quick and manage your data to meet the requirements that apply to you.

## Compliance programs that include Quick
<a name="sec-compliance-programs"></a>

The following programs include Quick. For each program, use the linked AWS page to confirm the current status, the authorized AWS Regions, and any program details before you rely on the program for your own workloads.

FedRAMP  
Quick is in scope for the FedRAMP program. To confirm the current authorization status and the authorized AWS Regions, see [AWS services in scope for FedRAMP](https://aws.amazon.com/compliance/services-in-scope/FedRAMP/). You remain responsible for meeting the FedRAMP requirements that apply to your workloads.

HIPAA eligibility  
Quick is a HIPAA Eligible Service. This eligibility applies across the Quick web, desktop, and mobile clients, subject to the shared responsibility model and your configuration. To process, store, or transmit protected health information (PHI), you must have an AWS Business Associate Addendum (BAA) in place. You must also configure the service according to your obligations. To confirm current eligibility, see the [HIPAA Eligible Services Reference](https://aws.amazon.com/compliance/hipaa-eligible-services-reference/). For more information about using AWS to build HIPAA workloads, see [HIPAA Overview](https://aws.amazon.com/compliance/hipaa-compliance/).

PCI DSS  
Quick is in scope for the Payment Card Industry Data Security Standard (PCI DSS). To confirm the current status, see [AWS services in scope for PCI DSS](https://aws.amazon.com/compliance/services-in-scope/PCI/). You are responsible for the security of the cardholder data that you handle in the service.

SOC reports  
Quick is in scope for the AWS System and Organization Controls (SOC) reports, including SOC 1, SOC 2, and SOC 3. To confirm the current status and download the reports that describe the AWS controls, see [AWS services in scope for SOC](https://aws.amazon.com/compliance/services-in-scope/SOC/).

ISO 9001, ISO 27001, ISO 27018, and ISO 27019  
Quick is in scope for the ISO 9001, ISO 27001, ISO 27018, and ISO 27019 standards. ISO 27018 is the code of practice for protecting personal data in the cloud. To confirm the current status and review the certifications, see [ISO 27001 Overview](https://aws.amazon.com/compliance/iso-27001-faqs/) and the [AWS services in scope by compliance program](https://aws.amazon.com/compliance/services-in-scope/) page.

BSI C5  
Quick is in scope for the AWS Cloud Computing Compliance Criteria Catalogue (BSI C5). To confirm the current status, see [AWS services in scope for BSI C5](https://aws.amazon.com/compliance/services-in-scope/C5/).

HITRUST CSF  
Quick is in scope for the HITRUST Common Security Framework (CSF). To confirm the current status, see [AWS services in scope for HITRUST CSF](https://aws.amazon.com/compliance/services-in-scope/HITRUST-CSF/).

## Verifying current reports and scope
<a name="sec-compliance-verify"></a>

Program scope and audit reports change over time. To confirm the status that applies to you, use the following AWS resources.
+ To download third-party audit reports, use AWS Artifact. For more information, see [Downloading reports in AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/downloading-documents.html).
+ For the most current list of AWS services in scope of specific compliance programs, see [AWS services in scope by compliance program](https://aws.amazon.com/compliance/services-in-scope/). For general information, see [AWS compliance programs](https://aws.amazon.com/compliance/programs/).

## Your compliance responsibilities
<a name="sec-compliance-responsibility"></a>

Your compliance responsibility when you use Amazon Quick depends on the sensitivity of your data, your company's compliance objectives, and applicable laws and regulations. Use the following AWS resources to help you meet your obligations:
+ [Security and compliance quick start guides](https://aws.amazon.com/quickstart/?awsf.quickstart-homepage-filter=categories%23security-identity-compliance) – These deployment guides discuss architectural considerations and provide steps for deploying security- and compliance-focused baseline environments on AWS.
+ [AWS compliance resources](https://aws.amazon.com/compliance/resources/) – This collection of workbooks and guides might apply to your industry and location.
+ [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) – This AWS service assesses how well your resource configurations comply with internal practices, industry guidelines, and regulations.
+ [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) – This AWS service provides a comprehensive view of your security state within AWS that helps you check your compliance with security industry standards and best practices.