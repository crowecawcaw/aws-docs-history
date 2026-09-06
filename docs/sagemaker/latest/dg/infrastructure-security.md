

# Infrastructure Security in Amazon SageMaker AI
<a name="infrastructure-security"></a>

As a managed service, Amazon SageMaker AI is protected by AWS global network security. For information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/). To design your AWS environment using the best practices for infrastructure security, see [Infrastructure Protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html) in *Security Pillar AWS Well‐Architected Framework*.

You use AWS published API calls to access Amazon SageMaker AI through the network. Clients must support the following:
+ Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
+ Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes.

**Topics**
+ [SageMaker AI Scans AWS Marketplace Training and Inference Containers for Security Vulnerabilities](#mkt-container-scan)
+ [Connect to Amazon SageMaker AI resources from within a VPC](infrastructure-connect-to-resources.md)
+ [Run Training and Inference Containers in Internet-Free Mode](mkt-algo-model-internet-free.md)
+ [Connect to SageMaker AI Within your VPC](interface-vpc-endpoint.md)
+ [Give SageMaker AI Access to Resources in your Amazon VPC](infrastructure-give-access.md)

## SageMaker AI Scans AWS Marketplace Training and Inference Containers for Security Vulnerabilities
<a name="mkt-container-scan"></a>

To meet our security requirements, all the [pre-built SageMaker images](https://docs.aws.amazon.com/sagemaker/latest/dg-ecr-paths/sagemaker-algo-docker-registry-paths.html), including AWS Deep Learning Containers, the SageMaker AI machine learning framework containers, and the SageMaker AI built-in algorithm containers, and algorithms and model packages listed in AWS Marketplace are scanned for Common Vulnerabilities and Exposures (CVE). CVE is a list of publicly known information about security vulnerability and exposure. The National Vulnerability Database (NVD) provides CVE details such as severity, impact rating, and fix information. Both CVE and NVD are available for public consumption and free for security tools and services to use. For more information, see [CVE Frequently Asked Questions (FAQs)](https://www.cve.org/ResourcesSupport/FAQs). 