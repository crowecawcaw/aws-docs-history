# AWS FedRAMP Rev5 Secure Configuration Guidance

Comprehensive security configuration guidance for AWS services aligned with FedRAMP Revision 5 Recommended Secure Configuration (FRR-RSC) requirements. This site contains FedRAMP specific guidance for AWS services as well as access to [OSCAL](https://csrc.nist.gov/Projects/Open-Security-Controls-Assessment-Language "https://csrc.nist.gov/Projects/Open-Security-Controls-Assessment-Language") formatted documents for consumption into your own tooling. These guidances are provided as a point in time reference to how to configure AWS services and AWS top-level administration accounts in a secure fashion to align with FedRAMP.

## Coverage

- **ALL** Administrative guidance requirements

## Requirements

- **All 10** FRR-RSC controls

## About FedRAMP Rev5 RSC Requirements

FedRAMP Revision 5 introduces 10 new Recommended Secure Configuration (FRR-RSC) requirements that cloud service providers must address to help federal agencies secure their cloud environments. AWS provides comprehensive guidance to align with these requirements.

### What AWS Provides:

- **Administrative Account Protection:** Specific guidance for securing top-level administrative accounts
- **Machine-Readable Formats:** OSCAL-compliant exports automation
- **API-Driven Configuration:** Docuemntation on security settings configurable via AWS CLI and APIs where applicable

## Complete FRR-RSC Coverage

| Requirement | Description                                | AWS Solution                                                           |
| ----------- | ------------------------------------------ | ---------------------------------------------------------------------- |
| FRR-RSC-01  | Top-Level Administrative Accounts Guidance | Detailed guidance for Root Account, Organizations, IAM Identity Center |
| FRR-RSC-02  | Administrative Security Settings           | Root-only security settings documentation with API commands            |
| FRR-RSC-03  | Privileged Accounts Security               | IAM best practices, MFA enforcement, least privilege guidance          |
| FRR-RSC-04  | Secure Defaults on Provisioning            | AWS Well-Architected Framework security baselines per service          |
| FRR-RSC-05  | Comparison Capability                      | AWS Config integration for drift detection and compliance comparison   |
| FRR-RSC-06  | Export Capability                          | JSON, OSCAL, and CloudFormation export formats                         |
| FRR-RSC-07  | API Capability                             | 100% of security settings configurable via AWS CLI/API                 |
| FRR-RSC-08  | Machine-Readable Guidance                  | OSCAL 1.1.2 component definitions for all services                     |
| FRR-RSC-09  | Publish Guidance                           | Publicly accessible web interface and downloadable artifacts           |
| FRR-RSC-10  | Versioning and Release History             | Version-controlled guidance with change tracking                       |

## Get Started

### 1. Review & Implement Guidance

Explore security configuration guidance for administrative accounts and all 161 AWS services, Implement gudiance from examples provided in each service guidance doc.

### 3. Export & Automate

Download OSCAL files to integrate with your compliance automation tools for continued usage

[Download Artifacts](samples/FRR-RSC.md "samples/FRR-RSC.md")
