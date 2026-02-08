# Security

The security pillar within the Microsoft Workloads Lens extends the foundational security
principles of the AWS Well-Architected Framework with specialized guidance tailored for
Microsoft-centric environments. Rather than replacing the core Well-Architected security
practices, this lens amplifies them by addressing the unique security considerations that arise
when running Microsoft technologies on AWS.

This extension provides targeted security strategies for protecting Windows Server
infrastructures, Active Directory implementations, SQL Server databases, Exchange Server
deployments, SharePoint environments, and .NET applications. The lens integrates Microsoft
security capabilities with AWS security services—including AWS IAM for identity
management, AWS KMS for encryption, Amazon GuardDuty for threat detection, AWS Security Hub CSPM for centralized
security posture management, and NitroTPM for hardware-based security—creating a comprehensive
defense-in-depth approach.

By building upon the Well-Architected Framework's security foundation, this lens assists
organizations in maintaining Microsoft workload security best practices while fully using
AWS Cloud security capabilities, resulting in a hybrid security model that addresses both
traditional Microsoft security requirements and modern cloud security paradigms. This includes
implementing defense in depth strategies for Windows Server environments, Active Directory
services, SQL Server databases, Exchange Server, SharePoint, and .NET applications, while using
with AWS security services (including IAM, KMS, GuardDuty, Security Hub CSPM, and NitroTPM).

Establish proper identity and access management through AWS IAM integration with Active
Directory, implement encryption at rest and in transit using AWS KMS and Microsoft TDE, and deploy
comprehensive monitoring capabilities through AWS CloudTrail, Amazon CloudWatch, and Microsoft security
logging. This strategy maintains strong security postures that protect against advanced
persistent threats, insider threats, and compliance violations while adhering to regulatory
requirements such as HIPAA, PCI DSS, SOX, and GDPR.

The pillar emphasizes the AWS shared responsibility model, where AWS secures the
underlying cloud infrastructure, hypervisor, and physical facilities while customers are
responsible for securing their Microsoft workloads within the cloud, including operating system
hardening, application security, data classification and protection, network configuration, and
identity management. This includes implementing security best practices such as least privilege
access, regular security assessments, automated patch management through AWS Systems Manager, and
incident response procedures tailored to Microsoft environments.

Key security considerations for Microsoft workloads include securing hybrid connectivity
between on-premises Active Directory and AWS through AWS Direct Connect or Site-to-Site VPN, implementing
proper network segmentation using VPCs and security groups, enabling comprehensive logging and
monitoring for Windows events and Microsoft application logs, and establishing disaster recovery
procedures that maintain security controls across Regions while maintaining business continuity
for mission-critical Microsoft applications.

###### Focus areas

- [Definitions](definitions-sec.md "definitions-sec.md")
- [Design principles](design-principles-sec.md "design-principles-sec.md")
- [Workload security](workload-security.md "workload-security.md")
- [Access management](access-management.md "access-management.md")
- [Data protection](data-protection.md "data-protection.md")
