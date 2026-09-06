

# AWS FedRAMP Rev5 Secure Configuration Guidance
<a name="introduction"></a>

Comprehensive security configuration guidance for AWS accounts and services aligned with FedRAMP Revision 5 Secure Configuration Guidance (SCG) requirements. This site contains FedRAMP specific guidance for AWS services. These guidances are provided as a point in time reference to how to configure AWS services and AWS top-level administration accounts in a secure fashion to align with FedRAMP.

## Coverage
<a name="_coverage"></a>
+  **ALL** Administrative guidance requirements

## Requirements
<a name="_requirements"></a>
+  **All 4** SCG Cloud Service Offering (CSO) requirements
+  **All 5** SCG Enhanced Capabilities (ENH) recommendations

## About FedRAMP Rev5 SCG Requirements
<a name="_about_fedramp_rev5_scg_requirements"></a>

FedRAMP Revision 5 introduces Secure Configuration Guide requirements that cloud service providers must address to help federal agencies secure their cloud environments. AWS provides comprehensive guidance to align with these requirements.

### What AWS Provides:
<a name="_what_aws_provides"></a>
+  **Administrative Account Protection:** Specific guidance for securing top-level administrative accounts
+  **Machine-Readable Formats:** OSCAL-compliant exports automation
+  **API-Driven Configuration:** Documentation on security settings configurable via AWS CLI and APIs where applicable

## Complete SCG Coverage
<a name="_complete_scg_coverage"></a>

### Cloud Service Offering Requirements
<a name="_cloud_service_offering_requirements"></a>


| Requirement | Description | AWS Solution | 
| --- | --- | --- | 
| SCG-CSO-RSC | Providers MUST create, maintain, and make available recommendations for securely configuring their cloud services (the Secure Configuration Guide) that includes at least the following information:<br />Required: Instructions on how to securely access, configure, operate, and decommission top-level administrative accounts that control enterprise access to the entire cloud service offering.<br />Required: Explanations of security-related settings that can be operated only by top-level administrative accounts and their security implications.<br />Recommended: Explanations of security-related settings that can be operated only by privileged accounts and their security implications. | Create, maintain, and make available recommendations for securely configuring AWS services including: instructions for top-level administrative accounts (access, configure, operate, decommission), security-related settings operated by top-level administrative accounts, and privileged account security settings | 
| SCG-CSO-AUP | Providers MUST include instructions in the FedRAMP authorization package that explain how to obtain and use the Secure Configuration Guide. | Available | 
| SCG-CSO-PUB | Public Guidance Providers SHOULD make the Secure Configuration Guide available publicly. | AWS provides these secure configuration guidances available through the AWS documentation to the public for usage. | 
| SCG-CSO-SDF | Providers SHOULD set all settings to their recommended secure defaults for top-level administrative accounts and privileged accounts when initially provisioned. | AWS builds services with security in mind, we don’t enforce a minimum standard but provide security options to meet customer needs. | 

### Enhanced Capabilities
<a name="_enhanced_capabilities"></a>


| Recommendation | Description | AWS Solution | 
| --- | --- | --- | 
| SCG-ENH-CMP | Comparison Capability Providers SHOULD offer the capability to compare all current settings for top-level administrative accounts and privileged accounts to the recommended secure defaults. | Leverage AWS Config | 
| SCG-ENH-EXP | Export Capability Providers SHOULD offer the capability to export all security settings in a machine-readable format. | OSCAL Formats will be available in the future | 
| SCG-ENH-API | API Capability Providers SHOULD offer the capability to view and adjust security settings via an API or similar capability. | AWS provides API access to AWS services | 
| SCG-ENH-MRG | Machine-Readable Guidance Providers SHOULD also provide the Secure Configuration Guide in a machine-readable format that can be used by customers or third-party tools to compare against current settings. | AWS Will provide OSCAL formatted guides | 
| SCG-ENH-VRH | Versioning and Release History Providers SHOULD provide versioning and a release history for recommended secure default settings for top-level administrative accounts and privileged accounts as they are adjusted over time | Each guide includes versioning details | 

## Get Started
<a name="_get_started"></a>

### Review & Implement Guidance
<a name="_review_implement_guidance"></a>

Explore security configuration guidance for administrative accounts and all avaialble AWS services. Use the examples provided to help implement security configurations of your AWS accounts and AWS services.