# MSFTSEC03-BP02 Enable Always Encrypted feature for SQL

Server

Microsoft SQL Server's _Always Encrypted_ feature
provides robust data protection using client-side encryption with
certificates. This technology creates a clear separation between
data owners who can view the information and data managers who
shouldn't have access. It effectively safeguards sensitive data by
encrypting it in the database, during transit, and even while being
processed. Always Encrypted is available not only in on-premises SQL
Server deployments but also in cloud environments, including Amazon RDS for SQL Server and SQL Server instances running on Amazon EC2.
By implementing Always Encrypted, organizations can enhance their
data security posture, particularly when handling sensitive
information in Microsoft SQL Server environments on AWS.

**Desired outcome:** Implement
client-side encryption capabilities that protect sensitive data
throughout its entire lifecycle, keeping data encrypted even during
processing and is only accessible to authorized applications and
users with proper decryption keys.

**Common anti-patterns:**

- Processing sensitive data in plaintext within applications or
  databases, exposing it to potential compromise during
  computation or memory access by unauthorized processes.
- Implementing encryption in use inconsistently across different
  data types or applications, leaving some sensitive information
  vulnerable during processing operations.
- Using client-side encryption without proper key management or
  secure key distribution mechanisms, potentially compromising the
  security benefits of the encryption implementation.

**Benefits of establishing this best
practice:**

- Maximum data protection through encryption that maintains data
  confidentiality even during processing operations, verifying
  that sensitive information is never exposed in plaintext to
  unauthorized systems or users.
- Enhanced separation of duties between data owners and data
  managers, allowing database administrators to manage systems
  without accessing sensitive business data.
- Improved regulatory capabilities for highly regulated industries
  that require the highest levels of data protection, including
  protection during data processing operations.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

When implementing Always Encrypted, first identify which sensitive
data elements truly need this protection layer. Then map out where
to apply based on your data flows and access patterns. Evaluate
feature limitations and potential performance impacts before
proceeding, as encryption/decryption operations can affect
response times and resource usage.

### Implementation steps

1. Identify highly sensitive data elements that require
   protection during processing, such as personally
   identifiable information (PII), financial data, or
   healthcare records.
2. Configure SQL Server Always Encrypted for identified
   sensitive columns, choosing appropriate encryption types
   (deterministic or randomized) based on query requirements.
3. Set up certificate-based key management for Always
   Encrypted, and properly store and distribute keys to
   authorized client applications.
4. Modify client applications to handle encrypted data
   operations, including proper connection string configuration
   and query modifications.
5. Implement secure key provisioning mechanisms that allow
   authorized applications to access encryption keys while
   blocking unauthorized access.
6. Configure column master keys and column encryption keys with
   appropriate permissions and access controls to maintain
   separation of duties.
7. Test application functionality with encrypted data for
   proper operation and performance while maintaining data
   protection.
8. Establish monitoring and auditing procedures to track key
   usage, encryption operations, and access to sensitive
   encrypted data.

## Resources

**Related documents:**

- [Best
  Practices for Deploying Microsoft SQL Server on Amazon EC2 -
  Encryption in Use](../../../whitepapers/latest/best-practices-for-deploying-microsoft-sql-server/security-optimization.md#encryption-in-use "../../../whitepapers/latest/best-practices-for-deploying-microsoft-sql-server/security-optimization.md#encryption-in-use")
- [SQL
  Server Always Encrypted](https://docs.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine "https://docs.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine")

**Related tools:**

- [SQL
  Server Management Studio](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms "https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms")
- [Always
  Encrypted Wizard](https://docs.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-wizard "https://docs.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-wizard")
- [Azure
  Key Vault](https://azure.microsoft.com/en-us/services/key-vault/ "https://azure.microsoft.com/en-us/services/key-vault/") (for hybrid scenarios)
