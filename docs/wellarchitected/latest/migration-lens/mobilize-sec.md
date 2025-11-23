# Mobilize

During the mobilize phase of the migration, you plan for your
authentication and authorization systems to ensure secure access
to your migrated workloads. This phase also involves building your
AWS environment in alignment with AWS security foundations.
Establishing a secure connection between on-premises and AWS is
essential for safely migrating workloads to AWS. This includes
establishing policies and tools for data encryption at rest and in
transit. Furthermore, it's important to consider any third-party
integrations and align them with the overall security strategy.
These steps collectively enhance the security resilience of the
migration process and prepare the infrastructure for a successful
transition to AWS.

| MIG-SEC-04: Do you have an established standard for authentication and authorization? |
| ------------------------------------------------------------------------------------- |
|                                                                                       |

AWS Identity and Access Management (IAM) provides fine-grained
access control across the entire AWS platform. You can use IAM
to specify who or what can access which services and resources,
and under which conditions. IAM policies let you manage
permissions to your workforce and systems to ensure least
privilege permissions.

[Least privilege](../framework/sec-design.md "../framework/sec-design.md") is an AWS Well-Architected Framework best
practice for building securely in the cloud. 

## MIG-SEC-BP-4.1 Implement strong identity and least privilege principles

This BP applies to the following best practice areas: Identity
and access management

### Implementation guidance

**Suggestion
4.1.1:** Protect
and limit the use of the AWS account root user.

It's vital to ensure strong security measures for your AWS account's root user, treating its credentials with the
utmost confidentiality and limitation.  You should regard
your root user credentials with the same seriousness as
vital personal information, deploying them only when
required.

For a comprehensive guide on the best practices surrounding
the AWS root account, see
[Root user best practices for your AWS account](../../../accounts/latest/reference/best-practices-root-user.md "../../../accounts/latest/reference/best-practices-root-user.md").

**Suggestion 4.1.2:**
Assess how user identities are managed and authenticated in
AWS.

In the migration process, the selection of a suitable
identity provider (IDP) is essential. This choice determines
how smoothly and securely you can connect to the cloud. When
migrating to AWS, it's crucial to evaluate and optimize how
user identities are managed and authenticated to pick the
most appropriate option based on your long-term
authentication and authorization requirements:

- **AWS Identity and Access Management (IAM):** Define distinct user roles
  and permissions tailored to AWS resources. Consider the
  enhanced security of AWS multi-factor authentication for
  high-priority accounts. IAM's federated capabilities
  integrate effortlessly with established identity
  systems, like Microsoft Active Directory. Federation
  should be leveraged in place of IAM users whenever
  feasible. This allows users to authenticate using their
  existing credentials, streamlining the authentication
  process and simplifying the account management
  provisioning and de-provisioning processes.
- **Directory Service:**Facilitate your migration by
  integrating with corporate directories, enhancing user
  experience and reducing operational burdens.
- **AWS IAM Identity Center:**Centrally coordinate workforce
  access, a pivotal asset during the migration phase. AWS
  IAM Identity Center is the preferred method for
  organizations to federate existing workforce identity
  stores.
- **Amazon Cognito:**
  Provides customer identity and access management to
  applications and workloads.
- **External identity
  providers**: While adopting AWS, integrate with
  existing IDPs to establish connections. External
  identity providers can easily integrate directly with
  AWS IAM, AWS IAM Identity Center, and Amazon Cognito.
  Manual configuration may be required to provide optimal
  connectivity. Regularly synchronize identities to
  maintain accurate access controls.

For more detail, see the following: 

- [Identity and Access Control](../../../whitepapers/latest/introduction-aws-security/identity-and-access-control.md "../../../whitepapers/latest/introduction-aws-security/identity-and-access-control.md")
- [Require human users to use federation with an identity provider to access AWS using temporary credentials](../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp "../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp")
- [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md")

**Suggestion
4.1.3:** Implement
a strong privileged access management program and controls.

A key security consideration for the enterprise is
monitoring and administrating elevated access, often known
as privileged access, for business-critical applications
that are running in the AWS Cloud. You need to have a
process to request, fulfill, certify, and govern privileged
assets in the cloud to maintain privileged access management
(PAM). Based on your compliance requirements, you may need
to limit the privileged access to a certain group of
resources or for a specific period of time.

For more detail, see the following: 

- [AWS Marketplace for PAM solutions](https://aws.amazon.com/marketplace/search/results?searchTerms=PAM "https://aws.amazon.com/marketplace/search/results?searchTerms=PAM")
- [Temporary elevated access management with IAM Identity Center](https://aws.amazon.com/blogs/security/temporary-elevated-access-management-with-iam-identity-center/ "https://aws.amazon.com/blogs/security/temporary-elevated-access-management-with-iam-identity-center/")

| MIG-SEC-05: Have you built your AWS environment following the AWS recommended security foundations? |
| --------------------------------------------------------------------------------------------------- |
|                                                                                                     |

As you move into the mobilize phase of the migration journey,
you build the foundational components, such as AWS accounts and
networking and security, before the workloads move to AWS. We
refer to this as building a
[landing zone](../../../prescriptive-guidance/latest/migration-aws-environment/understanding-landing-zones.md "../../../prescriptive-guidance/latest/migration-aws-environment/understanding-landing-zones.md") (not to be confused with AWS Landing Zone Service,
which is part of

[AWS Control Tower](https://aws.amazon.com/controltower/ "https://aws.amazon.com/controltower/")).

## MIG-SEC-BP-5.1 Implement AWS multi-account structure

This BP applies to the following best practice areas: Security
foundations

### Implementation guidance

**Suggestion
5.1.1:** Understand
and design AWS multi-account structure for isolation
boundaries at the AWS account, VPC, business unit, and
environment levels.

As you adopt AWS, we recommend that you determine how your
business, governance, security, and operational requirements
can be met in AWS. Use of multiple AWS accounts plays an
important role in how you meet those requirements. The use
of multiple accounts allows for benefits like group
workloads based on business purpose and ownership.

Apply distinct security controls by environment, constrain
access to sensitive data, and limit scope of impact from
adverse events.

For more detail, see the following: 

- [Building
  a landing zone](../../../prescriptive-guidance/latest/migration-aws-environment/building-landing-zones.md "../../../prescriptive-guidance/latest/migration-aws-environment/building-landing-zones.md")
- [The
  AWS Security Reference Architecture](../../../prescriptive-guidance/latest/security-reference-architecture/architecture.md "../../../prescriptive-guidance/latest/security-reference-architecture/architecture.md")
- [Best
  practices for AWS Control Tower administrators](../../../controltower/latest/userguide/best-practices.md "../../../controltower/latest/userguide/best-practices.md")
- [Security
  in AWS Control Tower](../../../controltower/latest/userguide/security.md "../../../controltower/latest/userguide/security.md")

**Suggestion 5.1.2:** Take
note of AWS service quotas per AWS account.

Your AWS account has

[default
quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md"), formerly referred to as limits, for each AWS
service. Unless otherwise noted, each quota is
Region-specific. You can request increases for some quotas,
and other quotas cannot be increased. As you scale, AWS
multi-account strategy quotas play an important role in
designing multi-account strategy and workload grouping
strategy.

| MIG-SEC-06: Have you established secure connectivity in preparation for migrating workloads to AWS? |
| --------------------------------------------------------------------------------------------------- |
|                                                                                                     |

There are many different mechanisms available for connectivity
between a customer's data center and AWS. Which solution you
choose is dependent on your use case and requirements. For all
solutions, secure connectivity between your on-premises
infrastructure and AWS is paramount during the migration
process. This involves the use of robust strategies for
maintaining data confidentiality and integrity in transit.

## MIG-SEC-BP-6.1 Establish secure connectivity to AWS

This BP applies to the following best practice areas: Data
protection

### Implementation guidance

**Suggestion 6.1.1:** Establish secure data transmission capabilities between on-premise networks and AWS

Create secure data transmission utilizing virtual private networks (VPNs) or dedicated private connections to establish secure network connections for your migration. These connections keep the data confidential and maintain its integrity as it moves between your on-premises environment and AWS. If your organization has compliance requirements for encryption in transit, implement VPN or encryption for connectivity between your data center and AWS. This provides secure transmission of data during the migration process. You might consider using AWS Transit Gateway in conjunction with a VPN to securely connect your on-premise datacenters to your VPCs.

For more detail, see the following:

- [Site-to-Site VPN](https://aws.amazon.com/vpn/ "https://aws.amazon.com/vpn/")
- [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/ "https://aws.amazon.com/transit-gateway/")

**Suggestion 6.1.2:** Use
AWS Direct Connect for large bandwidth and dedicated
connectivity

Use
[AWS Direct Connect](https://aws.amazon.com/directconnect/ "https://aws.amazon.com/directconnect/") for stable connectivity for large data
movement with stable bandwidth and low latency network
connectivity. It provides a dedicated, private network
connection from your premises to AWS, which is crucial for
large workload migrations.

**Suggestion 6.1.3:** Use AWS PrivateLink to limit exposure between VPCs and AWS services.

Establish connectivity between VPCs and AWS services without exposing data to the internet using [AWS PrivateLink](https://aws.amazon.com/privatelink/ "https://aws.amazon.com/privatelink/").  [AWS Application Migration Service](../../../mgn/latest/ug/AWS-Related-FAQ.md#mgn-and-vpc "../../../mgn/latest/ug/AWS-Related-FAQ.md#mgn-and-vpc") interacts with interface [VPC endpoints](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") to establish a private connection between your VPC and AWS Application Migration Service.

## MIG-SEC-BP-6.2: Establish network security controls

This BP applies to the following best practice areas:
Infrastructure protection and Data protection

During the migration process to AWS, it's important to ensure
robust network protection, including the implementation of
intrusion detection and prevention systems (IDS/IPS), as well
as OSI layer 4 to layer 7 security. AWS and the Amazon Partner
Network offer a variety of services that can support these
requirements.

### Implementation guidance

**Suggestion
6.2.1**: Enable
layer 7 Security with AWS Web Application Firewall (WAF) to
protect your web applications from common web exploits. 

[AWS WAF](https://aws.amazon.com/waf/ "https://aws.amazon.com/waf/") allows you to control how traffic reaches your
applications by creating security rules that block common
attack patterns, such as SQL injection or cross-site
scripting (XSS).  Use

[AWS Shield](https://aws.amazon.com/shield/ "https://aws.amazon.com/shield/") for managed Distributed Denial of Service
(DDoS) protection. AWS Shield Advanced provides additional
DDoS protections and capabilities.

**Suggestion 6.2.2:** Use
VPCs and network segmentation.

Use the appropriate network controls to isolate your
applications appropriately. [Virtual Private Clouds (VPCs)](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") allow you to create logically
isolated virtual networks. Within a VPC, you can use [security groups (SGs)](../../../vpc/latest/userguide/vpc-security-groups.md "../../../vpc/latest/userguide/vpc-security-groups.md") and [network access control lists (NACLS)](../../../vpc/latest/userguide/vpc-network-acls.md "../../../vpc/latest/userguide/vpc-network-acls.md") that implement inbound
and outbound traffic rules and ensure appropriate
segmentation. For more detail, see [Zero Trust](https://aws.amazon.com/security/zero-trust/ "https://aws.amazon.com/security/zero-trust/").

**Suggestion
6.2.3**: Explore
IDS/IPS solutions in the AWS Marketplace.

Explore third-party IDS/IPS solutions offered in the [AWS Marketplace](https://aws.amazon.com/marketplace/search/results?searchTerms=ids+and+ips "https://aws.amazon.com/marketplace/search/results?searchTerms=ids+and+ips"). Many of these solutions offer additional
security features and capabilities that can complement those
provided by AWS services. For more detail, see [AWS Network Firewall](../../../network-firewall/latest/developerguide/what-is-aws-network-firewall.md "../../../network-firewall/latest/developerguide/what-is-aws-network-firewall.md").

**Suggestion
6.2.4**:
Identify anomalous network behavior from migrated workloads
using Amazon GuardDuty.

[Amazon GuardDuty](https://aws.amazon.com/guardduty/ "https://aws.amazon.com/guardduty/") monitors your accounts and various
workloads to identify malicious and anomalous behaviors,
including monitoring network and DNS traffic. When migrating
workloads such as virtual machines and containers, Amazon GuardDuty can detect and alert you if those workloads are
attempting to use your network for potentially malicious or
unauthorized activities.

| MIG-SEC-07: Do you have policies and tools defined for data encryption at rest during and after migration? |
| ---------------------------------------------------------------------------------------------------------- |
|                                                                                                            |

Data at rest represents any data that you persist in
non-volatile storage for any duration in your workload. This
includes block storage, object storage, databases, archives, IoT
devices, and any other storage medium on which data is
persisted. Protecting your data at rest reduces the risk of
unauthorized access, when encryption and appropriate access
controls are implemented. AWS provides robust and scalable
encryption solutions for both data at rest and in transit to
help you meet your data security requirements and compliance
needs.

## MIG-SEC-BP-7.1 Establish security controls for protecting data at rest

This BP applies to the following best practice areas: Data
protection

### Implementation guidance

**Suggestion
7.1.1**:
Classify your data based on its sensitivity

Understand what data is sensitive, confidential, or public.
This helps in applying appropriate security controls. To
effectively manage risk, organizations should consider
[classifying data](../../../whitepapers/latest/data-classification/data-classification-overview.md "../../../whitepapers/latest/data-classification/data-classification-overview.md") by working backward from the contextual use of
the data, and creating a [categorization scheme](../../../whitepapers/latest/data-classification/using-aws-cloud-to-support-data-classification.md "../../../whitepapers/latest/data-classification/using-aws-cloud-to-support-data-classification.md") that takes into account whether a given use
case results in significant impact to an organization's
operations (for example, if data is confidential, it needs
to have integrity, and it needs to be available). Customers
also need to take into account their regulatory and
compliance requirements for protection of data like GDPR.

**Suggestion 7.1.2:** Use
AWS Key Management Service (KMS) for protecting data at
rest.

Protect data at rest by using [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/") to create and control the
cryptographic keys used to encrypt your data. Additionally,
use the built-in encryption capabilities of services like [Amazon S3](../../../AmazonS3/latest/userguide/UsingEncryption.md "../../../AmazonS3/latest/userguide/UsingEncryption.md"), [Amazon EBS](../../../AWSEC2/latest/UserGuide/EBSEncryption.md "../../../AWSEC2/latest/UserGuide/EBSEncryption.md"), [Amazon RDS](../../../AmazonRDS/latest/UserGuide/Overview.md "../../../AmazonRDS/latest/UserGuide/Overview.md"), and [AWS Lambda](../../../lambda/latest/dg/security-dataprotection.md#security-privacy-atrest "../../../lambda/latest/dg/security-dataprotection.md#security-privacy-atrest") for protecting data at rest.

**Suggestion 7.1.3:** Use
AWS CloudHSM when compliance dictates.

If compliance requirements dictate the need for
hardware-based cryptographic key storage, commonly referred
to as hardware security models (HSMs), consider

[AWS CloudHSM](https://aws.amazon.com/cloudhsm/ "https://aws.amazon.com/cloudhsm/"). HSMs provided by CloudHSM are FIPS 140-2
level 3 certified.

**Suggestion 7.1.4**: Use
strong IAM policies for key management.

Establish granular IAM policies that explicitly delineate
permissions for activities related to data encryption at
rest. Verify that only trusted roles or users can decrypt
the data or manage encryption keys, further bolstering the
security of your data during and after migration.

For more detail, see the following:

- [AWS IAM Policy Best Practices](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md")
- [AWS Key Management Service (KMS) Best Practices](../../../kms/latest/developerguide/best-practices.md "../../../kms/latest/developerguide/best-practices.md")

| MIG-SEC-08: Have you identified and applied application security controls? |
| -------------------------------------------------------------------------- |
|                                                                            |

Protecting applications, hosting environments, and detecting
irregular behavior is critical to a secure cloud environment.
Customers transitioning to AWS have the advantage of tapping
into a comprehensive array of AWS cloud-native application
security services and work on existing applications to match the
overall security posture. 

## MIG-SEC-BP-8.1: Establish application layer security controls

This BP applies to the following best practice areas:
Application security

### Implementation guidance

**Suggestion
8.1.1**:
Implement application layer vulnerability scanning.

AWS emphasizes the importance of application security
through comprehensive practices such as regular updates,
vulnerability scanning, penetration testing, and secure
coding principles. Conduct regular scanning and testing to
identify weaknesses within AWS applications and
infrastructure. Use AWS tools like [Amazon Inspector](https://aws.amazon.com/inspector/ "https://aws.amazon.com/inspector/") for streamlined security assessments.

**Suggestion 8.1.2:**
Implement full-lifecycle secure coding practices and
supporting tools.

Implement secure coding practices for applications within
AWS, leveraging code review and proper methodologies. Use
AWS services such as [AWS CodeGuru](https://aws.amazon.com/codeguru/ "https://aws.amazon.com/codeguru/") for enhanced code quality insights and
security. Use [Amazon CodeWhisperer](../../../codewhisperer/latest/userguide/security-scans.md "../../../codewhisperer/latest/userguide/security-scans.md") to provide additional security context
and recommendations within your IDE as you write your
application code. For more detail, see [Building a secure CICD pipeline](https://aws.amazon.com/blogs/devops/building-end-to-end-aws-devsecops-ci-cd-pipeline-with-open-source-sca-sast-and-dast-tools/ "https://aws.amazon.com/blogs/devops/building-end-to-end-aws-devsecops-ci-cd-pipeline-with-open-source-sca-sast-and-dast-tools/").

**Suggestion 8.1.3**:
Perform threat modeling.

Identify and prioritize risks using a [threat model](https://aws.amazon.com/blogs/security/how-to-approach-threat-modeling/ "https://aws.amazon.com/blogs/security/how-to-approach-threat-modeling/"). Use a threat model to identify and maintain an
up-to-date register of potential threats. Prioritize your
threats and adapt your security controls to prevent, detect,
and respond. Revisit on a recurring basis and maintain this
in the context of the evolving security landscape.

**Suggestion
8.1.4**:
Implement customer identity and access management for your
applications that target non-workforce users.

Implement a customer identity and access management (CIAM)
solution that allows your customers and end-users (like
non-employee accounts) to access your application securely.
Use
[Amazon Cognito](https://aws.amazon.com/cognito/ "https://aws.amazon.com/cognito/"), which is designed to handle the scale and
full lifecyle of CIAM account management, or consider
various partner CIAM solutions in the [AWS Marketplace](https://aws.amazon.com/marketplace "https://aws.amazon.com/marketplace"). Additionally, use [Amazon Verified Permissions (AVP)](../../../verifiedpermissions/latest/userguide/what-is-avp.md "../../../verifiedpermissions/latest/userguide/what-is-avp.md") for scalable, fine-grained
permissions management and authorization service for custom
applications built by you.

## MIG-SEC-BP-8.2: Optimize application security with AWS Application Migration Service

This BP applies to the following best practice areas: 
Application security

### Implementation guidance

**Suggestion
8.2.1**:
Automate the migration and conversion processes using
AWS-provided services.

Use the
[AWS Application Migration Service](https://aws.amazon.com/application-migration-service/ "https://aws.amazon.com/application-migration-service/") (MGN) to convert source
servers to run natively on AWS, streamlining the conversion
and migration processes and minimizing manual errors. This
provides a seamless transition through a tested
non-interactive and secure conversion, introduces automation
for post-migration configurations, and optimizes
applications to benefit from robust AWS infrastructure.

**Suggestion
8.2.2**:
Modernize and enhance your application.

During migration, take advantage of the service's in-built
options such as disaster recovery, OS or license conversion,
and cloud-native capabilities. This ensures applications are
not just migrated but also modernized to meet contemporary
security and operational standards.

| MIG-SEC-9: Do you have a data backup and disaster recovery strategy during migration? |
| ------------------------------------------------------------------------------------- |
|                                                                                       |

Data backups are an essential element of data security. In the
context of migration to AWS, planning for data backup and
disaster recovery is critical to assure business continuity and
protect against data loss. These concepts are covered in more
details in the Reliability pillar of this document. AWS provides
several services that can help with data backup and restoration,
as well as managing and testing disaster recovery plans.

## MIG-SEC-BP-9.1: Establish a data backup and restore strategy

This BP applies to the following best practice areas: Data
protection

### Implementation guidance

**Suggestion
9.1.1:** Implement
and test backup and recovery capabilities.

Use [AWS Backup](https://aws.amazon.com/backup/ "https://aws.amazon.com/backup/") to create backup plans, which define when and
how often backups are created and how long they're stored.
Regularly test backup restoration to test that your backup
strategy is effective and backups are usable in case of data
loss or system failure.

**Suggestion
9.1.2:** Audit
and validate your backup requirements.

Use [AWS Backup Audit Manager](../../../aws-backup/latest/devguide/aws-backup-audit-manager.md "../../../aws-backup/latest/devguide/aws-backup-audit-manager.md") to audit the compliance of your
AWS Backup policies against controls you define. Audit and
identify issues regarding backup schedules, which resources
are being backed up, and any non-compliance against the
controls you set up can be reported and leveraged for
remediation.

## MIG-SEC-BP-9.2: Establish a Disaster recovery plan

This BP applies to the following best practice areas: Data
protection and Infrastructure protection

### Implementation guidance

**Suggestion
9.2.1:** Develop
and test a disaster recovery plan and capabilities.

Leverage [AWS Elastic Disaster Recovery](https://aws.amazon.com/disaster-recovery/?nc2=type_a "https://aws.amazon.com/disaster-recovery/?nc2=type_a") to minimize downtime and
data loss with fast, reliable recovery of physical, virtual,
and cloud-based servers into AWS. Use the [AWS Well-Architected Framework Reliability Pillar](../reliability-pillar/welcome.md "../reliability-pillar/welcome.md") to
design, deploy, and manage workloads and align them with
disaster recovery strategies and requirements.

| MIG-SEC-10: Have you established monitoring controls with the right set of tools? |
| --------------------------------------------------------------------------------- |
|                                                                                   |

Establishing robust monitoring controls for security is
essential to detect and respond to potential security threats in
your AWS environment. By implementing comprehensive monitoring
controls, you can gain visibility into activities, monitor for
unusual behavior, and proactively identify security incidents. 

## MIG-SEC-BP-10.1: Validate and use AWS native monitoring tools.

This BP applies to the following best practice areas: Incident
response

### Implementation guidance

**Suggestion
10.1.1:** Develop
and deploy a comprehensive logging strategy

An effective logging strategy is a cornerstone of any
successful migration to AWS. By leveraging the right
combination of AWS and third-party tools, you can maintain
full visibility into your infrastructure and ensure your
operations are running smoothly.

For more detail, see the following:

- [Getting started with AWS CloudTrail tutorials](../../../awscloudtrail/latest/userguide/cloudtrail-tutorial.md "../../../awscloudtrail/latest/userguide/cloudtrail-tutorial.md")
- [Setting Up AWS Config with the Console](../../../config/latest/developerguide/gs-console.md "../../../config/latest/developerguide/gs-console.md")
- [Getting set up (Amazon CloudWatch)](../../../AmazonCloudWatch/latest/monitoring/GettingSetup.md "../../../AmazonCloudWatch/latest/monitoring/GettingSetup.md")
- [Analyze Network Traffic of Amazon Virtual Private Cloud (VPC) by CIDR blocks](https://aws.amazon.com/blogs/networking-and-content-delivery/analyze-network-traffic-of-amazon-virtual-private-cloud-vpc-by-cidr-blocks/ "https://aws.amazon.com/blogs/networking-and-content-delivery/analyze-network-traffic-of-amazon-virtual-private-cloud-vpc-by-cidr-blocks/")
- [Considerations for the security operations center in the cloud: deployment using AWS security services](https://aws.amazon.com/blogs/security/considerations-for-the-security-operations-center-in-the-cloud-deployment-using-aws-security-services/ "https://aws.amazon.com/blogs/security/considerations-for-the-security-operations-center-in-the-cloud-deployment-using-aws-security-services/")
- [Logging strategies for security incident response](https://aws.amazon.com/blogs/security/logging-strategies-for-security-incident-response/ "https://aws.amazon.com/blogs/security/logging-strategies-for-security-incident-response/")

## MIG-SEC-BP-10.2: Explore cloud native AWS partner monitoring tools

This BP applies to the following best practice areas: Incident
response

### Implementation guidance

**Suggestion
10.2.1:** Deploy
application monitoring capabilities.

Alongside AWS tools such as
[AWS X-Ray](https://aws.amazon.com/xray/ "https://aws.amazon.com/xray/"), consider [third-party
partner tools](https://aws.amazon.com/marketplace/ "https://aws.amazon.com/marketplace/") which provide application-level
insights and monitoring on AWS. They can supplement AWS
services and help create a more holistic monitoring strategy
tailored to your business needs.

| MIG-SEC-11: Do you have any third-party integrations? |
| ----------------------------------------------------- |
|                                                       |

When integrating third-party services into your AWS migration,
it's crucial to review the security features, permissions, and
data handling practices of these services to maintain a secure
and compliant migration process. Review their security practices
and verify that they align with your organization's security
requirements. 

## MIG-SEC-BP-11.1: Perform third-party integration due diligence

This BP applies to the following best practice areas: Security
foundations

### Implementation guidance

**Suggestion 11.1.1:**
Review third-party integration patterns and security
practices.

When reviewing third-party integration patterns, conduct
thorough due diligence and consider engaging with the vendor
directly to discuss their security practices and address any
specific security concerns you may have. Additionally,
consult the AWS Shared Responsibility Model to understand
the division of security responsibilities between AWS and
third-party service providers. 

Review the following checklist in regard to third-party
integrations:

1. **Authentication and
   authorization:** The third-party should
   supports secure mechanisms like multi-factor
   authentication (MFA) and role-based access control
   (RBAC).
2. **Data encryption**:
   Confirm encryption both in transit (using TLS) and at
   rest with robust algorithms.
3. **Compliance and
   certifications**: Assess adherence to standards
   like SOC 2, ISO 27001, and other relevant industry
   certifications.
4. **Data privacy and
   residency**: Verify that data handling aligns
   with organizational privacy policies and legal
   regulations.
5. **Logging and
   monitoring:** Review capabilities for security
   analysis and incident response visibility.
6. **Security incident
   response:** Understand incident management,
   customer communication, and resolution speed.
7. **Third-party audits and
   assessments:** Request information on security
   tests and independent reviews undergone.
8. **Data backup and
   recovery**: Check mechanisms against data loss.
9. **Service-level agreements
   (SLAs):** Check that they fulfill
   organizational needs in terms of availability,
   performance, and security.
10. **Integration with AWS
    services:** Verify that AWS integration adheres
    to security best practices.
11. **Vendor reputation and
    support:** Research vendor credibility,
    reviews, and their support effectiveness.
12. **Continual security
    updates:** Confirm timely vulnerability
    addressing and update provision.
