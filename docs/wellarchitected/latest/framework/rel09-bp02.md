

# REL09-BP02 Secure and encrypt backups

 Backups often hold the same sensitive data as production, yet they receive less protection. Anyone who gains unauthorized access to your backups can read or destroy the one copy you rely on to recover. Protecting backups means controlling who can access them, detecting that access, and encrypting the data so an accidental exposure does not become a breach. 

 **Desired outcome:** 
+  Access to backups and restoration tooling is separated from access to the production data itself. 
+  All backups are encrypted at rest and in transit. 
+  You can detect and audit who accessed, or attempted to access, backups. 
+  Encryption keys for backups are governed by policies that limit who can use them. 

 **Common anti-patterns:** 
+  Teams grant the same access to backups and restore automation that they grant to production data. 
+  Teams store backups without encryption. 
+  Teams share one set of credentials across production and backup environments. 
+  Teams leave key policies unmanaged, so any identity with account access can decrypt backups. 

 **Benefits of establishing this best practice:** 
+  Exposed production credentials do not automatically expose backups. 
+  Accidental exposure of a backup reveals no readable data because it is encrypted. 
+  Unauthorized access attempts are detected and audited. 
+  Key policies give you fine-grained control over who can decrypt recovered data. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Give backups their own security boundary. If the credentials that manage production also manage backups, a single breached identity puts both the primary data and its only copy at risk. Separate the roles that can restore or delete backups from those with day-to-day access to production data. Apply least privilege to backups, snapshots, and replicas so that the ability to recover is not bundled with the ability to operate. 

 Encryption protects backups when access controls fail. With server-side encryption at rest, the storage service encrypts data as it arrives. With client-side encryption, your application encrypts data before it leaves, which keeps the service from ever seeing plaintext but shifts key handling to you. Most workloads use server-side encryption with a managed key service, reserving client-side encryption for data with the strictest confidentiality requirements. 

 A service-owned or account-managed key is convenient but gives you limited control over who can decrypt. A customer-managed key lets you write policies that govern exactly which principals can use it, and you can revoke that access at the cost of managing the key's lifecycle yourself. On AWS, [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) stores keys and enforces those policies through IAM. 

 When a source data store is encrypted, its snapshots and backups inherit that encryption. [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html) backups are encrypted when the database is, [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EncryptionAtRest.html) encrypts all data at rest by default, and [AWS Elastic Disaster Recovery](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html) encrypts data in transit and at rest. For cross-Region backups, KMS keys are Region-specific, so a replicated backup needs a key in the destination Region. Set the destination key when you configure replication, or the copy can fail or use a key you did not intend. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Encrypt each data store so backups inherit encryption:** Turn on encryption at rest for every source. Configure [Amazon RDS encryption](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html) at instance creation, [Amazon EBS encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html) by default or per volume, [DynamoDB encryption](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EncryptionAtRest.html) with your chosen key, and [Amazon EFS encryption](https://docs.aws.amazon.com/efs/latest/ug/encryption.html) at file system creation. 

1.  **Govern encryption keys and their access policies:** Use [AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) to create and store keys, and choose customer-managed keys where you need to control and revoke who can decrypt. Write key policies that grant decrypt permission only to the roles that legitimately restore data. 

1.  **Configure encryption across source and destination Regions:** For replicated backups, set the destination-Region key when you configure replication, because KMS keys do not cross Regions. See [replicating objects created with server-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) and [Amazon EBS encryption for Elastic Disaster Recovery](https://docs.aws.amazon.com/drs/latest/userguide/volumes-drs.html#ebs-encryption). 

1.  **Apply least-privilege permissions to backups:** Limit access to backups, snapshots, and replicas separately from production data access, following the [security best practices in the Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/security.html). Grant restore and delete permissions only to the roles that require them. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL09-BP01 Identify and back up all data that needs to be backed up, or reproduce the data from sources](rel09-bp01.md) 
+  [REL09-BP04 Perform periodic recovery of the data to verify backup integrity and processes](rel09-bp04.md) 
+  [REL09-BP05 Implement cyber resilience for backup data](rel09-bp05.md) 

 **Related documents:** 
+  [Encryption for backups in AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/encryption.html) 
+  [Amazon EBS encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html) 
+  [Protecting data with encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingEncryption.html) 
+  [DynamoDB encryption at rest](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EncryptionAtRest.html) 
+  [Encrypting Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html) 
+  [Data encryption in Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/encryption.html) 
+  [Managing encrypted tables in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/encryption.tutorial.html) 
+  [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) 
+  [Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/security.html) 
+  [What is Elastic Disaster Recovery?](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html) 