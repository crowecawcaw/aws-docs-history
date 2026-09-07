

# Mobilize
<a name="mobilize-sec"></a>

 During the mobilize phase of the migration, you plan for your authentication and authorization systems to ensure secure access to your migrated workloads. This phase also involves building your AWS environment in alignment with AWS security foundations. Establishing a secure connection between on-premises and AWS is essential for safely migrating workloads to AWS. This includes establishing policies and tools for data encryption at rest and in transit. Furthermore, it's important to consider any third-party integrations and align them with the overall security strategy. These steps collectively enhance the security resilience of the migration process and prepare the infrastructure for a successful transition to AWS. 


| MIG-SEC-04: Do you have an established standard for authentication and authorization? | 
| --- | 
|   | 

 AWS Identity and Access Management (IAM) provides fine-grained access control across the entire AWS platform. You can use IAM to specify who or what can access which services and resources, and under which conditions. IAM policies let you manage permissions to your workforce and systems to ensure least privilege permissions. [Least privilege](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-design.html) is an AWS Well-Architected Framework best practice for building securely in the cloud.  

## MIG-SEC-BP-4.1 Implement strong identity and least privilege principles
<a name="mig-sec-bp-4.1-implement-strong-identity-and-least-privilege-principles"></a>

 This BP applies to the following best practice areas: Identity and access management 

### Implementation guidance
<a name="implementation-guidance-17"></a>

 **Suggestion 4.1.1:** Protect and limit the use of the AWS account root user. 

 It's vital to ensure strong security measures for your AWS account's root user, treating its credentials with the utmost confidentiality and limitation.  You should regard your root user credentials with the same seriousness as vital personal information, deploying them only when required. 

 For a comprehensive guide on the best practices surrounding the AWS root account, see [Root user best practices for your AWS account](https://docs.aws.amazon.com/accounts/latest/reference/best-practices-root-user.html). 

 **Suggestion 4.1.2:** Assess how user identities are managed and authenticated in AWS. 

 In the migration process, the selection of a suitable identity provider (IDP) is essential. This choice determines how smoothly and securely you can connect to the cloud. When migrating to AWS, it's crucial to evaluate and optimize how user identities are managed and authenticated to pick the most appropriate option based on your long-term authentication and authorization requirements: 
+  **AWS Identity and Access Management (IAM):** Define distinct user roles and permissions tailored to AWS resources. Consider the enhanced security of AWS multi-factor authentication for high-priority accounts. IAM's federated capabilities integrate effortlessly with established identity systems, like Microsoft Active Directory. Federation should be leveraged in place of IAM users whenever feasible. This allows users to authenticate using their existing credentials, streamlining the authentication process and simplifying the account management provisioning and de-provisioning processes. 
+  **Directory Service: **Facilitate your migration by integrating with corporate directories, enhancing user experience and reducing operational burdens. 
+  **AWS IAM Identity Center: **Centrally coordinate workforce access, a pivotal asset during the migration phase. AWS IAM Identity Center is the preferred method for organizations to federate existing workforce identity stores. 
+  **Amazon Cognito:** Provides customer identity and access management to applications and workloads. 
+  **External identity providers**: While adopting AWS, integrate with existing IDPs to establish connections. External identity providers can easily integrate directly with AWS IAM, AWS IAM Identity Center, and Amazon Cognito. Manual configuration may be required to provide optimal connectivity. Regularly synchronize identities to maintain accurate access controls. 

 For more detail, see the following:  
+  [Identity and Access Control](https://docs.aws.amazon.com/whitepapers/latest/introduction-aws-security/identity-and-access-control.html) 
+  [Require human users to use federation with an identity provider to access AWS using temporary credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-users-federation-idp) 
+  [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) 

 **Suggestion 4.1.3:** Implement a strong privileged access management program and controls. 

 A key security consideration for the enterprise is monitoring and administrating elevated access, often known as privileged access, for business-critical applications that are running in the AWS Cloud. You need to have a process to request, fulfill, certify, and govern privileged assets in the cloud to maintain privileged access management (PAM). Based on your compliance requirements, you may need to limit the privileged access to a certain group of resources or for a specific period of time. 

 For more detail, see the following:  
+  [AWS Marketplace for PAM solutions](https://aws.amazon.com/marketplace/search/results?searchTerms=PAM) 
+  [Temporary elevated access management with IAM Identity Center](https://aws.amazon.com/blogs/security/temporary-elevated-access-management-with-iam-identity-center/) 


| MIG-SEC-05: Have you built your AWS environment following the AWS recommended security foundations? | 
| --- | 
|   | 

 As you move into the mobilize phase of the migration journey, you build the foundational components, such as AWS accounts and networking and security, before the workloads move to AWS. We refer to this as building a [landing zone](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-aws-environment/understanding-landing-zones.html) (not to be confused with AWS Landing Zone Service, which is part of [AWS Control Tower](https://aws.amazon.com/controltower/)). 

## MIG-SEC-BP-5.1 Implement AWS multi-account structure
<a name="mig-sec-bp-5.1-implement-multi-account-structure"></a>

 This BP applies to the following best practice areas: Security foundations 

### Implementation guidance
<a name="implementation-guidance-18"></a>

 **Suggestion 5.1.1:** Understand and design AWS multi-account structure for isolation boundaries at the AWS account, VPC, business unit, and environment levels. 

 As you adopt AWS, we recommend that you determine how your business, governance, security, and operational requirements can be met in AWS. Use of multiple AWS accounts plays an important role in how you meet those requirements. The use of multiple accounts allows for benefits like group workloads based on business purpose and ownership. 

 Apply distinct security controls by environment, constrain access to sensitive data, and limit scope of impact from adverse events. 

 For more detail, see the following:  
+  [Building a landing zone](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-aws-environment/building-landing-zones.html) 
+  [The AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/architecture.html) 
+  [Best practices for AWS Control Tower administrators](https://docs.aws.amazon.com/controltower/latest/userguide/best-practices.html) 
+  [Security in AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/security.html) 

 **Suggestion 5.1.2:** Take note of AWS service quotas per AWS account. 

 Your AWS account has [default quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html), formerly referred to as limits, for each AWS service. Unless otherwise noted, each quota is Region-specific. You can request increases for some quotas, and other quotas cannot be increased. As you scale, AWS multi-account strategy quotas play an important role in designing multi-account strategy and workload grouping strategy. 


| MIG-SEC-06: Have you established secure connectivity in preparation for migrating workloads to AWS? | 
| --- | 
|   | 

 There are many different mechanisms available for connectivity between a customer's data center and AWS. Which solution you choose is dependent on your use case and requirements. For all solutions, secure connectivity between your on-premises infrastructure and AWS is paramount during the migration process. This involves the use of robust strategies for maintaining data confidentiality and integrity in transit. 

## MIG-SEC-BP-6.1 Establish secure connectivity to AWS 
<a name="mig-sec-bp-6.1-establish-secure-connectivity"></a>

 This BP applies to the following best practice areas: Data protection 

### Implementation guidance
<a name="implementation-guidance-19"></a>

**Suggestion 6.1.1:** Establish secure data transmission capabilities between on-premise networks and AWS

Create secure data transmission utilizing virtual private networks (VPNs) or dedicated private connections to establish secure network connections for your migration. These connections keep the data confidential and maintain its integrity as it moves between your on-premises environment and AWS. If your organization has compliance requirements for encryption in transit, implement VPN or encryption for connectivity between your data center and AWS. This provides secure transmission of data during the migration process. You might consider using AWS Transit Gateway in conjunction with a VPN to securely connect your on-premise datacenters to your VPCs.

 For more detail, see the following: 
+  [Site-to-Site VPN](https://aws.amazon.com/vpn/) 
+  [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/) 

 **Suggestion 6.1.2:** Use AWS Direct Connect for large bandwidth and dedicated connectivity 

 Use [AWS Direct Connect](https://aws.amazon.com/directconnect/) for stable connectivity for large data movement with stable bandwidth and low latency network connectivity. It provides a dedicated, private network connection from your premises to AWS, which is crucial for large workload migrations. 

**Suggestion 6.1.3:** Use AWS PrivateLink to limit exposure between VPCs and AWS services. Establish connectivity between VPCs and AWS services without exposing data to the internet using [AWS PrivateLink](https://aws.amazon.com/privatelink/).  [AWS Application Migration Service](https://docs.aws.amazon.com/mgn/latest/ug/AWS-Related-FAQ.html#mgn-and-vpc) interacts with interface [VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) to establish a private connection between your VPC and AWS Application Migration Service.

## MIG-SEC-BP-6.2: Establish network security controls 
<a name="mig-sec-bp-6.2-establish-network-security-controls"></a>

 This BP applies to the following best practice areas: Infrastructure protection and Data protection 

 During the migration process to AWS, it's important to ensure robust network protection, including the implementation of intrusion detection and prevention systems (IDS/IPS), as well as OSI layer 4 to layer 7 security. AWS and the Amazon Partner Network offer a variety of services that can support these requirements. 

### Implementation guidance
<a name="implementation-guidance-20"></a>

 **Suggestion 6.2.1**: Enable layer 7 Security with AWS Web Application Firewall (WAF) to protect your web applications from common web exploits.  

 [AWS WAF](https://aws.amazon.com/waf/) allows you to control how traffic reaches your applications by creating security rules that block common attack patterns, such as SQL injection or cross-site scripting (XSS).  Use [AWS Shield](https://aws.amazon.com/shield/) for managed Distributed Denial of Service (DDoS) protection. AWS Shield Advanced provides additional DDoS protections and capabilities. 

 **Suggestion 6.2.2:** Use VPCs and network segmentation. 

 Use the appropriate network controls to isolate your applications appropriately. [Virtual Private Clouds (VPCs)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) allow you to create logically isolated virtual networks. Within a VPC, you can use [security groups (SGs)](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) and [network access control lists (NACLS)](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) that implement inbound and outbound traffic rules and ensure appropriate segmentation. For more detail, see [Zero Trust](https://aws.amazon.com/security/zero-trust/). 

 **Suggestion 6.2.3**: Explore IDS/IPS solutions in the AWS Marketplace. 

 Explore third-party IDS/IPS solutions offered in the [AWS Marketplace](https://aws.amazon.com/marketplace/search/results?searchTerms=ids+and+ips). Many of these solutions offer additional security features and capabilities that can complement those provided by AWS services. For more detail, see [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html). 

 **Suggestion 6.2.4**: Identify anomalous network behavior from migrated workloads using Amazon GuardDuty. 

 [Amazon GuardDuty](https://aws.amazon.com/guardduty/) monitors your accounts and various workloads to identify malicious and anomalous behaviors, including monitoring network and DNS traffic. When migrating workloads such as virtual machines and containers, Amazon GuardDuty can detect and alert you if those workloads are attempting to use your network for potentially malicious or unauthorized activities. 


| MIG-SEC-07: Do you have policies and tools defined for data encryption at rest during and after migration? | 
| --- | 
|   | 

 Data at rest represents any data that you persist in non-volatile storage for any duration in your workload. This includes block storage, object storage, databases, archives, IoT devices, and any other storage medium on which data is persisted. Protecting your data at rest reduces the risk of unauthorized access, when encryption and appropriate access controls are implemented. AWS provides robust and scalable encryption solutions for both data at rest and in transit to help you meet your data security requirements and compliance needs. 

## MIG-SEC-BP-7.1 Establish security controls for protecting data at rest
<a name="mig-sec-bp-7.1-establish-security-controls-for-protecting-data-at-rest"></a>

 This BP applies to the following best practice areas: Data protection 

### Implementation guidance
<a name="implementation-guidance-21"></a>

 **Suggestion 7.1.1**: Classify your data based on its sensitivity 

 Understand what data is sensitive, confidential, or public. This helps in applying appropriate security controls. To effectively manage risk, organizations should consider [classifying data](https://docs.aws.amazon.com/whitepapers/latest/data-classification/data-classification-overview.html) by working backward from the contextual use of the data, and creating a [categorization scheme](https://docs.aws.amazon.com/whitepapers/latest/data-classification/using-aws-cloud-to-support-data-classification.html) that takes into account whether a given use case results in significant impact to an organization's operations (for example, if data is confidential, it needs to have integrity, and it needs to be available). Customers also need to take into account their regulatory and compliance requirements for protection of data like GDPR. 

 **Suggestion 7.1.2:** Use AWS Key Management Service (KMS) for protecting data at rest. 

 Protect data at rest by using [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/) to create and control the cryptographic keys used to encrypt your data. Additionally, use the built-in encryption capabilities of services like [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingEncryption.html), [Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html), [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html), and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/security-dataprotection.html#security-privacy-atrest) for protecting data at rest. 

 **Suggestion 7.1.3:** Use AWS CloudHSM when compliance dictates. 

 If compliance requirements dictate the need for hardware-based cryptographic key storage, commonly referred to as hardware security models (HSMs), consider [AWS CloudHSM](https://aws.amazon.com/cloudhsm/). HSMs provided by CloudHSM are FIPS 140-2 level 3 certified. 

 **Suggestion 7.1.4**: Use strong IAM policies for key management. 

 Establish granular IAM policies that explicitly delineate permissions for activities related to data encryption at rest. Verify that only trusted roles or users can decrypt the data or manage encryption keys, further bolstering the security of your data during and after migration. 

 For more detail, see the following: 
+  [AWS IAM Policy Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) 
+  [AWS Key Management Service (KMS) Best Practices](https://docs.aws.amazon.com/kms/latest/developerguide/best-practices.html) 


| MIG-SEC-08: Have you identified and applied application security controls? | 
| --- | 
|   | 

 Protecting applications, hosting environments, and detecting irregular behavior is critical to a secure cloud environment. Customers transitioning to AWS have the advantage of tapping into a comprehensive array of AWS cloud-native application security services and work on existing applications to match the overall security posture.  

## MIG-SEC-BP-8.1: Establish application layer security controls
<a name="mig-sec-bp-8.1-establish-application-layer-security-controls"></a>

 This BP applies to the following best practice areas: Application security 

### Implementation guidance
<a name="implementation-guidance-22"></a>

 **Suggestion 8.1.1**: Implement application layer vulnerability scanning. 

 AWS emphasizes the importance of application security through comprehensive practices such as regular updates, vulnerability scanning, penetration testing, and secure coding principles. Conduct regular scanning and testing to identify weaknesses within AWS applications and infrastructure. Use AWS tools like [Amazon Inspector](https://aws.amazon.com/inspector/) for streamlined security assessments. 

 **Suggestion 8.1.2:** Implement full-lifecycle secure coding practices and supporting tools. 

 Implement secure coding practices for applications within AWS, leveraging code review and proper methodologies. Use AWS services such as [AWS CodeGuru](https://aws.amazon.com/codeguru/) for enhanced code quality insights and security. Use [Amazon CodeWhisperer](https://docs.aws.amazon.com/codewhisperer/latest/userguide/security-scans.html) to provide additional security context and recommendations within your IDE as you write your application code. For more detail, see [Building a secure CICD pipeline](https://aws.amazon.com/blogs/devops/building-end-to-end-aws-devsecops-ci-cd-pipeline-with-open-source-sca-sast-and-dast-tools/). 

 **Suggestion 8.1.3**: Perform threat modeling. 

 Identify and prioritize risks using a [threat model](https://aws.amazon.com/blogs/security/how-to-approach-threat-modeling/). Use a threat model to identify and maintain an up-to-date register of potential threats. Prioritize your threats and adapt your security controls to prevent, detect, and respond. Revisit on a recurring basis and maintain this in the context of the evolving security landscape. 

 **Suggestion 8.1.4**: Implement customer identity and access management for your applications that target non-workforce users. 

 Implement a customer identity and access management (CIAM) solution that allows your customers and end-users (like non-employee accounts) to access your application securely. Use [Amazon Cognito](https://aws.amazon.com/cognito/), which is designed to handle the scale and full lifecyle of CIAM account management, or consider various partner CIAM solutions in the [AWS Marketplace](https://aws.amazon.com/marketplace). Additionally, use [Amazon Verified Permissions (AVP)](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/what-is-avp.html) for scalable, fine-grained permissions management and authorization service for custom applications built by you. 

## MIG-SEC-BP-8.2: Optimize application security with AWS Application Migration Service
<a name="mig-sec-bp-8.2-optimize-application-security"></a>

 This BP applies to the following best practice areas:  Application security 

### Implementation guidance
<a name="implementation-guidance-23"></a>

 **Suggestion 8.2.1**: Automate the migration and conversion processes using AWS-provided services. 

 Use the [AWS Application Migration Service](https://aws.amazon.com/application-migration-service/) (MGN) to convert source servers to run natively on AWS, streamlining the conversion and migration processes and minimizing manual errors. This provides a seamless transition through a tested non-interactive and secure conversion, introduces automation for post-migration configurations, and optimizes applications to benefit from robust AWS infrastructure. 

 **Suggestion 8.2.2**: Modernize and enhance your application. 

 During migration, take advantage of the service's in-built options such as disaster recovery, OS or license conversion, and cloud-native capabilities. This ensures applications are not just migrated but also modernized to meet contemporary security and operational standards. 


| MIG-SEC-9: Do you have a data backup and disaster recovery strategy during migration? | 
| --- | 
|   | 

 Data backups are an essential element of data security. In the context of migration to AWS, planning for data backup and disaster recovery is critical to assure business continuity and protect against data loss. These concepts are covered in more details in the Reliability pillar of this document. AWS provides several services that can help with data backup and restoration, as well as managing and testing disaster recovery plans. 

## MIG-SEC-BP-9.1: Establish a data backup and restore strategy
<a name="mig-sec-bp-9.1-establish-a-data-backup-and-restore-strategy"></a>

 This BP applies to the following best practice areas: Data protection 

### Implementation guidance
<a name="implementation-guidance-24"></a>

 **Suggestion 9.1.1:** Implement and test backup and recovery capabilities. 

 Use [AWS Backup](https://aws.amazon.com/backup/) to create backup plans, which define when and how often backups are created and how long they're stored. Regularly test backup restoration to test that your backup strategy is effective and backups are usable in case of data loss or system failure. 

 **Suggestion 9.1.2:** Audit and validate your backup requirements. 

 Use [AWS Backup Audit Manager](https://docs.aws.amazon.com/aws-backup/latest/devguide/aws-backup-audit-manager.html) to audit the compliance of your AWS Backup policies against controls you define. Audit and identify issues regarding backup schedules, which resources are being backed up, and any non-compliance against the controls you set up can be reported and leveraged for remediation. 

## MIG-SEC-BP-9.2: Establish a Disaster recovery plan
<a name="mig-sec-bp-9.2-establish-a-disaster-recovery-plan"></a>

 This BP applies to the following best practice areas: Data protection and Infrastructure protection 

### Implementation guidance
<a name="implementation-guidance-25"></a>

 **Suggestion 9.2.1:** Develop and test a disaster recovery plan and capabilities. 

 Leverage [AWS Elastic Disaster Recovery](https://aws.amazon.com/disaster-recovery/?nc2=type_a) to minimize downtime and data loss with fast, reliable recovery of physical, virtual, and cloud-based servers into AWS. Use the [AWS Well-Architected Framework Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) to design, deploy, and manage workloads and align them with disaster recovery strategies and requirements. 


| MIG-SEC-10: Have you established monitoring controls with the right set of tools? | 
| --- | 
|   | 

 Establishing robust monitoring controls for security is essential to detect and respond to potential security threats in your AWS environment. By implementing comprehensive monitoring controls, you can gain visibility into activities, monitor for unusual behavior, and proactively identify security incidents.  

## MIG-SEC-BP-10.1: Validate and use AWS native monitoring tools.
<a name="mig-sec-bp-10.1-validate-and-use-monitoring-tools"></a>

 This BP applies to the following best practice areas: Incident response 

### Implementation guidance
<a name="implementation-guidance-26"></a>

 **Suggestion 10.1.1:** Develop and deploy a comprehensive logging strategy 

 An effective logging strategy is a cornerstone of any successful migration to AWS. By leveraging the right combination of AWS and third-party tools, you can maintain full visibility into your infrastructure and ensure your operations are running smoothly. 

 For more detail, see the following: 
+  [Getting started with AWS CloudTrail tutorials](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-tutorial.html) 
+  [Setting Up AWS Config with the Console](https://docs.aws.amazon.com/config/latest/developerguide/gs-console.html) 
+  [Getting set up (Amazon CloudWatch)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GettingSetup.html) 
+  [Analyze Network Traffic of Amazon Virtual Private Cloud (VPC) by CIDR blocks](https://aws.amazon.com/blogs/networking-and-content-delivery/analyze-network-traffic-of-amazon-virtual-private-cloud-vpc-by-cidr-blocks/) 
+  [Considerations for the security operations center in the cloud: deployment using AWS security services](https://aws.amazon.com/blogs/security/considerations-for-the-security-operations-center-in-the-cloud-deployment-using-aws-security-services/) 
+  [Logging strategies for security incident response](https://aws.amazon.com/blogs/security/logging-strategies-for-security-incident-response/) 

## MIG-SEC-BP-10.2: Explore cloud native AWS partner monitoring tools
<a name="mig-sec-bp-10.2-explore-cloud-native-partner-monitoring-tools"></a>

 This BP applies to the following best practice areas: Incident response 

### Implementation guidance
<a name="implementation-guidance-27"></a>

 **Suggestion 10.2.1:** Deploy application monitoring capabilities. 

 Alongside AWS tools such as [AWS X-Ray](https://aws.amazon.com/xray/), consider [third-party partner tools](https://aws.amazon.com/marketplace/) which provide application-level insights and monitoring on AWS. They can supplement AWS services and help create a more holistic monitoring strategy tailored to your business needs. 


| MIG-SEC-11: Do you have any third-party integrations? | 
| --- | 
|   | 

 When integrating third-party services into your AWS migration, it's crucial to review the security features, permissions, and data handling practices of these services to maintain a secure and compliant migration process. Review their security practices and verify that they align with your organization's security requirements.  

## MIG-SEC-BP-11.1: Perform third-party integration due diligence
<a name="mig-sec-bp-11.1-perform-third-party-integration-due-diligence"></a>

 This BP applies to the following best practice areas: Security foundations 

### Implementation guidance
<a name="implementation-guidance-28"></a>

 **Suggestion 11.1.1:** Review third-party integration patterns and security practices. 

 When reviewing third-party integration patterns, conduct thorough due diligence and consider engaging with the vendor directly to discuss their security practices and address any specific security concerns you may have. Additionally, consult the AWS Shared Responsibility Model to understand the division of security responsibilities between AWS and third-party service providers.  

 Review the following checklist in regard to third-party integrations: 

1.  **Authentication and authorization:** The third-party should supports secure mechanisms like multi-factor authentication (MFA) and role-based access control (RBAC). 

1.  **Data encryption**: Confirm encryption both in transit (using TLS) and at rest with robust algorithms. 

1.  **Compliance and certifications**: Assess adherence to standards like SOC 2, ISO 27001, and other relevant industry certifications. 

1.  **Data privacy and residency**: Verify that data handling aligns with organizational privacy policies and legal regulations. 

1.  **Logging and monitoring:** Review capabilities for security analysis and incident response visibility. 

1.  **Security incident response:** Understand incident management, customer communication, and resolution speed. 

1.  **Third-party audits and assessments:** Request information on security tests and independent reviews undergone. 

1.  **Data backup and recovery**: Check mechanisms against data loss. 

1.  **Service-level agreements (SLAs):** Check that they fulfill organizational needs in terms of availability, performance, and security. 

1.  **Integration with AWS services:** Verify that AWS integration adheres to security best practices. 

1.  **Vendor reputation and support:** Research vendor credibility, reviews, and their support effectiveness. 

1.  **Continual security updates:** Confirm timely vulnerability addressing and update provision. 