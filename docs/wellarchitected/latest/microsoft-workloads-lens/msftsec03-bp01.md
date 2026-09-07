

# MSFTSEC03-BP01 Encrypt data stored in Microsoft workloads
<a name="msftsec03-bp01"></a>

 Data at rest encompasses the entirety of your digitally stored information. Encryption is crucial to verify that this data remains visible only to authorized users and stays protected, even if storage or database access is compromised independently of the application. For Microsoft SQL Server environments, consider implementing Transparent Data Encryption (TDE). This technology provides robust encryption at rest solution specifically designed for Microsoft databases, offering strong protection for sensitive data without significant changes to your application architecture. 

 By employing these encryption methods, you enhance the security of your stored data, mitigating risks associated with unauthorized access and potential data breaches in your Microsoft SQL Server deployments. 

 **Desired outcome:** Implement comprehensive encryption at rest for sensitive data stored in Microsoft workloads, protecting data even if underlying storage systems are compromised while maintaining application performance and operational efficiency. 

 **Common anti-patterns:** 
+  Storing sensitive data in plaintext without any encryption protection, leaving it vulnerable to unauthorized access if storage systems or database files are compromised. 
+  Implementing encryption inconsistently across different data stores or only encrypting some sensitive data while leaving other critical information unprotected. 
+  Using weak encryption algorithms or poor key management practices that could be compromised, effectively negating the security benefits of encryption. 

 **Benefits of establishing this best practice:** 
+  Enhanced data protection through strong encryption that renders data unreadable to unauthorized users even if they gain access to storage systems or database files. 
+  Improved regulatory posture by meeting regulatory requirements for data protection that mandate encryption of sensitive information at rest. 
+  Reduced impact of security incidents through encryption that limits the value of stolen data and reduces the scope of potential data breaches. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 When encrypting Microsoft workloads at rest, start with Windows-based solutions like SQL Server TDE to protect databases and files. Establish a secure key management process and monitor performance metrics to maintain application responsiveness. 

### Implementation steps
<a name="implementation-steps"></a>

1.  Identify each data store containing sensitive information in your Microsoft workload, including SQL Server databases, file systems, and application data repositories. 

1.  Enable Transparent Data Encryption (TDE) on SQL Server databases to encrypt data files, log files, and backup files at the database level. 

1.  Configure AWS Key Management Service (KMS) or SQL Server key management to securely store and manage encryption keys with proper access controls. 

1.  Implement file system encryption using Amazon EBS encryption for EC2 instance storage volumes. 

1.  Enable encryption for backup files and verify that database backups maintain encryption protection during storage and transfer operations. 

1.  Configure application-level encryption for sensitive data fields that require additional protection beyond database-level encryption. 

1.  Establish key rotation policies and procedures to regularly update encryption keys while maintaining data accessibility and system availability. 

1.  Monitor encryption status and key usage through logging and alerting mechanisms to maintain continuous protection and detect any encryption failures. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Best Practices for Deploying Microsoft SQL Server on Amazon EC2 - Encryption at Rest](https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-microsoft-sql-server/security-optimization.html#encryption-at-rest) 
+  [SQL Server Transparent Data Encryption](https://docs.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption) 

 **Related tools:** 
+  [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/) 
+  [Amazon EBS Encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html) 
+  [BitLocker Drive Encryption](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview) 