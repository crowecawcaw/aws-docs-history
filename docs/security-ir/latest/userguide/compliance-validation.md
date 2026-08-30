# Compliance validation

Third-party auditors assess the security and compliance of AWS Security Incident Response as part of
multiple AWS compliance programs. These include SOC, PCI, FedRAMP, and others.

AWS Security Incident Response is currently in scope for the following compliance programs.

###### Topics

- [AWS services in scope](#compliance-validation-services-in-scope "#compliance-validation-services-in-scope")
- [Healthcare compliance (HITRUST CSF)](#compliance-validation-hitrust "#compliance-validation-hitrust")
- [HIPAA eligibility](#compliance-validation-hipaa "#compliance-validation-hipaa")

## AWS services in scope

| Compliance program                                                                                                                                          | Description                                                                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [SOC 1, 2, 3](https://aws.amazon.com/compliance/services-in-scope/SOC/ "https://aws.amazon.com/compliance/services-in-scope/SOC/")                          | System and Organization Controls — independent audit reports covering<br>security, availability, processing integrity, confidentiality, and privacy<br>controls.                                                |
| [ISO 27001, 27017, 27018, 27701, 22301, 20000-1, 9001](https://aws.amazon.com/compliance/iso-certified/ "https://aws.amazon.com/compliance/iso-certified/") | International standards for information security management, cloud<br>security controls, PII protection, privacy information management, business<br>continuity, IT service management, and quality management. |
| [CSA STAR CCM v4.0](https://aws.amazon.com/compliance/iso-certified/ "https://aws.amazon.com/compliance/iso-certified/")                                    | Cloud Security Alliance Security Trust Assurance and Risk — third-party<br>assessment of cloud-specific security controls.                                                                                      |
| [C5 (Germany)](https://aws.amazon.com/compliance/services-in-scope/C5/ "https://aws.amazon.com/compliance/services-in-scope/C5/")                           | Cloud Computing Compliance Criteria Catalogue — German Federal Office<br>for Information Security (BSI) baseline security standard.                                                                             |
| [FedRAMP Moderate](https://aws.amazon.com/compliance/services-in-scope/FedRAMP/ "https://aws.amazon.com/compliance/services-in-scope/FedRAMP/")             | Federal Risk and Authorization Management Program — Class C (formerly<br>Moderate baseline). Authorized in US East/West commercial Regions.                                                                     |
| [DoD CC SRG](https://aws.amazon.com/compliance/services-in-scope/DoD-CC-SRG/ "https://aws.amazon.com/compliance/services-in-scope/DoD-CC-SRG/")             | Department of Defense Cloud Computing Security Requirements Guide —<br>Impact Level 2 (IL2). Baselined with FedRAMP Moderate authorization in US East/West<br>commercial Regions.                               |
| [HITRUST CSF](https://aws.amazon.com/compliance/services-in-scope/HITRUST-CSF/ "https://aws.amazon.com/compliance/services-in-scope/HITRUST-CSF/")          | Health Information Trust Alliance Common Security Framework —<br>certifiable framework harmonizing healthcare, privacy, and security<br>requirements.                                                           |
| [PCI DSS](https://aws.amazon.com/compliance/services-in-scope/PCI/ "https://aws.amazon.com/compliance/services-in-scope/PCI/")                              | Payment Card Industry Data Security Standard — security requirements for<br>organizations handling cardholder data.                                                                                             |
| [MTCS (Singapore)](https://aws.amazon.com/compliance/services-in-scope/MTCS/ "https://aws.amazon.com/compliance/services-in-scope/MTCS/")                   | Multi-Tier Cloud Security — Singapore's national cloud security<br>certification standard (SS 584).                                                                                                             |
| [PiTuKri (Finland)](https://aws.amazon.com/compliance/services-in-scope/PiTuKri/ "https://aws.amazon.com/compliance/services-in-scope/PiTuKri/")            | Criteria for Assessing the Information Security of Cloud Services —<br>Finnish Traficom criteria for government cloud use.                                                                                      |
| [FINMA (Switzerland)](https://aws.amazon.com/compliance/services-in-scope/FINMA/ "https://aws.amazon.com/compliance/services-in-scope/FINMA/")              | Swiss Financial Market Supervisory Authority — regulatory workload<br>guidance for cloud providers in Switzerland's financial sector.                                                                           |

For a complete list of AWS services in scope of specific compliance programs, see
[AWS services in scope by
compliance program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/"). For general information, see
[AWS compliance programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/").

You can download third-party audit reports using AWS Artifact. For more information,
see [Downloading
reports in AWS Artifact](../../../artifact/latest/ug/downloading-documents.md "../../../artifact/latest/ug/downloading-documents.md").

## Healthcare compliance (HITRUST CSF)

AWS Security Incident Response is
[HITRUST CSF
certified](https://aws.amazon.com/compliance/services-in-scope/HITRUST-CSF/ "https://aws.amazon.com/compliance/services-in-scope/HITRUST-CSF/"). The HITRUST Common Security Framework harmonizes healthcare, privacy,
and security requirements into a single certifiable standard, and is widely recognized by
healthcare organizations as an assurance that a service meets rigorous healthcare security
control requirements. This certification demonstrates that AWS Security Incident Response aligns with the
security controls expected for use in healthcare environments.

## HIPAA eligibility

You can use AWS Security Incident Response to monitor and respond to security events in accounts and
environments that handle electronic protected health information (ePHI), including
HIPAA-designated environments. By design, AWS Security Incident Response doesn't create, receive, process,
store, or transmit customer data, including ePHI, in the course of performing its function.
For this reason, it isn't a
[HIPAA Eligible
Service](https://aws.amazon.com/compliance/hipaa-eligible-services-reference/ "https://aws.amazon.com/compliance/hipaa-eligible-services-reference/") and isn't covered under the AWS Business Associate Agreement (BAA), and it
doesn't need to be to be used alongside these workloads.
