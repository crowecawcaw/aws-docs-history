

# Compliance validation for AWS HealthOmics
<a name="compliance-validation"></a>

Third-party auditors assess the security and compliance of AWS HealthOmics as part of multiple AWS compliance programs. This includes HIPAA, FedRAMP, and others. The following table shows compliance certifications for the HealthOmics service.


| Certification | Link | 
| --- | --- | 
| HIPAA | [ HIPAA Eligible Services Reference](https://aws.amazon.com/compliance/hipaa-eligible-services-reference) | 
| HiTrust-CSF | [ Health Information Trust Alliance Common Security Framework ](https://aws.amazon.com/compliance/services-in-scope/HITRUST-CSF/) | 
| FedRAMP Moderate (East/West) | [ Federal Risk and Authorization Management Program](https://aws.amazon.com/compliance/services-in-scope/FedRAMP) | 
| ISO/CSA STAR | [ ISO and CSA STAR Certified](https://aws.amazon.com/compliance/iso-certified/) | 
| C5 | [ Cloud Computing Compliance Controls Catalog](https://aws.amazon.com/compliance/services-in-scope/C5) | 
| DoD CC SRG IL2 | [ Department of Defense Cloud Computing Security Requirements Guide](https://aws.amazon.com/compliance/services-in-scope/DoD_CC_SRG) | 
| ENS High | [ Esquema Nacional de Seguridad](https://aws.amazon.com/compliance/services-in-scope//ENS-High) | 
| FINMA | [ Swiss Financial Market Supervisory Authority](https://aws.amazon.com/compliance/services-in-scope/FINMA) | 
| ISMAP | [ Information System Security Management and Assessment Program](https://aws.amazon.com/compliance/services-in-scope/ISMAP/) | 
| OSPAR | [ Outsourced Service Provider’s Audit Report](https://aws.amazon.com/compliance/services-in-scope/OSPAR/) | 
| PCI | [ Payment Card Industry Data Security Standard](https://aws.amazon.com/compliance/services-in-scope/PCI/) | 
| Pinakes | [ Banking association CCI - Third Party Qualification](https://aws.amazon.com/compliance/services-in-scope/pinakes/) | 
| PiTuKri | [ Criteria for Assessing the Information Security of Cloud Services](https://aws.amazon.com/compliance/services-in-scope/PiTuKri/) | 
| SOC 1,2,3 | [ System and Organization Controls](https://aws.amazon.com/compliance/services-in-scope/SOC/) | 

For a list of all AWS services in scope for specific compliance programs, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/). For general information, see [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/).

You can download third-party audit reports using AWS Artifact. For more information, see [Downloading Reports in AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/downloading-documents.html).

HealthOmics data stores use the sample ID for internal file naming and for tagging resources. Before you ingest data, check whether the sample ID contains any PHI data. If it does, change the sample ID before you ingest the data. For more information, see guidance on the AWS [ HIPAA compliance](https://aws.amazon.com/compliance/hipaa-compliance) web page.

Your compliance responsibility when using AWS HealthOmics is determined by the sensitivity of your data, your company's compliance objectives, and applicable laws and regulations. AWS provides the following resources to help with compliance:
+ [Security and Compliance Quick Start Guides](https://aws.amazon.com/quickstart/?awsf.quickstart-homepage-filter=categories%23security-identity-compliance) – These deployment guides discuss architectural considerations and provide steps for deploying security- and compliance-focused baseline environments on AWS.
+ [Architecting for HIPAA Security and Compliance Whitepaper ](https://docs.aws.amazon.com/whitepapers/latest/architecting-hipaa-security-and-compliance-on-aws/architecting-hipaa-security-and-compliance-on-aws.html) – This whitepaper describes how companies can use AWS to create HIPAA-compliant applications.
+ [AWS Compliance Resources](https://aws.amazon.com/compliance/resources/) – This collection of workbooks and guides might apply to your industry and location.
+ [Evaluating Resources with Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) in the *AWS Config Developer Guide* – AWS Config; assesses how well your resource configurations comply with internal practices, industry guidelines, and regulations.
+ [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) – This AWS service provides a comprehensive view of your security state within AWS that helps you check your compliance with security industry standards and best practices.