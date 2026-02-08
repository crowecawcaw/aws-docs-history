# MSFTSEC01-BP02 Secure the Microsoft application and

database

Maintaining strong security at both the database and application
layers is crucial, as even read-only access by malicious actors
could compromise critical business data. To protect your Microsoft
environment, implement security best practices including the least
access principle, least privilege model, encryption at rest, and
encryption in transit. These measures help safeguard your Microsoft
application and database against unauthorized access and potential
data breaches, maintaining the confidentiality and integrity of your
business-critical information.

**Desired outcome:** Establish
comprehensive security controls for Microsoft applications and
databases that implement defense in depth strategies, proper access
controls, and encryption mechanisms to protect sensitive data and
block unauthorized access at the application and database layers.

**Common anti-patterns:**

- Using default database and application configurations without
  implementing security hardening, leaving systems vulnerable to
  common attack vectors such as SQL injection, privilege
  escalation, and unauthorized data access.
- Implementing overly permissive database and application access
  controls that grant excessive privileges to users or
  applications, violating the principle of least privilege and
  increasing the risk of data breaches.
- Storing sensitive data in plaintext or using weak encryption
  methods, making it vulnerable to exposure if the database or
  application is compromised or if data is intercepted during
  transmission.

**Benefits of establishing this best
practice:**

- Enhanced data protection through comprehensive encryption
  strategies that secure sensitive information both at rest and in
  transit, reducing the risk of data exposure even if systems are
  compromised.
- Improved access control and audit capabilities through
  implementation of least privilege principles and detailed
  logging, enabling better monitoring of data access patterns and
  potential security incidents.
- Reduced attack surface through application and database
  hardening measures that eliminate common vulnerabilities and
  implement security best practices specific to Microsoft
  technologies.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Securing Microsoft applications and databases requires a
multi-layered approach that addresses authentication,
authorization, encryption, and monitoring. Focus on implementing
Microsoft SQL Server security features alongside AWS security
services to create a comprehensive protection strategy. This
includes configuring proper access controls, enabling encryption
mechanisms, and establishing monitoring capabilities that provide
visibility into application and database activities.

### Implementation steps

1. Configure SQL Server authentication using Windows
   Authentication mode or mixed mode with strong password
   policies and account management practices.
2. Implement database-level security through proper user roles,
   schema permissions, and row-level security where appropriate
   for your Microsoft SQL Server environment.
3. Enable SQL Server audit logging to track database access,
   data modifications, and administrative activities for
   compliance and security monitoring.
4. Configure application-level security controls including
   input validation, output encoding, and secure session
   management for .NET applications.
5. Implement database connection security using encrypted
   connections (SSL/TLS) and connection string protection
   mechanisms.
6. Enable SQL Server security features such as dynamic data
   masking for sensitive data protection and Always Encrypted
   for client-side encryption.
7. Configure network security controls including database
   firewall rules and network segmentation to limit database
   access to authorized sources.
8. Establish regular security assessments and vulnerability
   scanning for both applications and databases using AWS and
   Microsoft security tools.

## Resources

**Related documents:**

- [Security
  best practices for Microsoft SQL Server on AWS](../../../sql-server-ec2/latest/userguide/security-sql-server-on-ec2.md "../../../sql-server-ec2/latest/userguide/security-sql-server-on-ec2.md")
- [Security
  Best Practices for Modernizing .NET Framework Applications on
  AWS](../../../prescriptive-guidance/latest/modernization-net-applications-security.md "../../../prescriptive-guidance/latest/modernization-net-applications-security.md")

**Related tools:**

- [SQL
  Server Management Studio](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms "https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms")
- [AWS Database Migration Service](https://aws.amazon.com/dms/ "https://aws.amazon.com/dms/")
- [Amazon RDS for SQL Server](https://aws.amazon.com/rds/sqlserver/ "https://aws.amazon.com/rds/sqlserver/")
