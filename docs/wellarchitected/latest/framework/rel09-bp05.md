

# REL09-BP05 Implement cyber resilience for backup data

 A ransomware or destructive event can breach the production environment or its identities and then delete or tamper with the backup copies you rely on to recover. Cyber resilience keeps backup data protected from deletion and tampering, so you can still recover even when production itself is affected. 

 **Desired outcome:** 
+  Every critical data source has at least one recovery path whose backup data is protected by service-enforced deletion controls. 
+  Backup data is logically isolated from the production environment. 
+  Backup data is validated for safety before it is used in recovery. 
+  Backup retention exceeds the time between the initial breach and detection. 
+  Credentials are rotated after recovery. 

 **Common anti-patterns:** 
+  You manage backup governance with the same identities that administer production, leaving no trust boundary between them. 
+  You rely solely on snapshot immutability (cannot be modified) without deletion protection (can still be removed). 
+  You validate backup recoverability without validating backup safety, confirming that a restore works without confirming the restored data is free of threats and corruption. 
+  You restore the most recent backup without considering whether it was taken while the threat actor was active in the environment. 
+  You set backup retention based only on compliance requirements, without accounting for how long a threat could persist before detection. 
+  You return a recovered environment to production without rotating credentials that were active during the event window. 

 **Benefits of establishing this best practice:** 
+  Recovery points remain available regardless of the scope of an unauthorized access. 
+  Validating backups for safety before use reduces the risk of reintroducing the threat. 
+  Retention that accounts for detection latency keeps a clean recovery point available when needed. 
+  Rotating credentials after recovery removes persisting exposed secrets. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 This best practice extends [REL09-BP01 Identify and back up all data that needs to be backed up, or reproduce the data from sources](rel09-bp01.md) through [REL09-BP04 Perform periodic recovery of the data to verify backup integrity and processes](rel09-bp04.md), which verify that data is identified, secured, automated, and periodically tested for recoverability. It adds the properties needed when the threat model includes a threat actor who might target the backups themselves or has taken over identities with administrative access. 

 Three properties define cyber-resilient backup data: 

1.  **Deletion protection:** No principal can remove recovery points or shorten retention within the protection period. 

1.  **Logical isolation from the production environment:** A breached production administrator account cannot reach or govern the backup storage. 

1.  **Validated safety:** Recovery points are confirmed to be in a known-good state before use. A restorability check alone is insufficient. 

 AWS provides multiple mechanisms to achieve these properties, with varying coverage by resource type: 
+  [AWS Backup logically air-gapped vaults](https://docs.aws.amazon.com/aws-backup/latest/devguide/logicallyairgappedvault.html) deliver deletion protection and logical isolation for supported resource types. Vault Lock Compliance mode is built in with no grace period, and backups are stored in an AWS Backup service-owned account that is unreachable from your accounts. Not all resource types are supported, so check the [Feature availability by resource](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html#features-by-resource) matrix for current coverage. 
+  [AWS Backup Vault Lock in Compliance mode](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html) on a standard vault in a dedicated backup account delivers deletion protection and a degree of isolation through account separation. It suits resource types that logically air-gapped vaults do not support. A configurable grace period applies before the lock becomes irrevocable. 
+  [Amazon S3 Object Lock in Compliance mode](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) delivers deletion protection for Amazon S3 data. No user, including the root user, can delete or shorten retention. 
+  [Amazon GuardDuty Malware Protection for AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/malware-protection.html) provides automated threat scanning of recovery points for supported resource types (Amazon EC2 images, Amazon EBS snapshots, EBS recovery points, EC2 recovery points, and Amazon S3 recovery points). 
+  [AWS Backup multi-party approval](https://docs.aws.amazon.com/aws-backup/latest/devguide/multipartyapproval.html) helps protect your access to backup data when the vault-owning account itself becomes inaccessible, whether through unauthorized account access, lockout, or closure. A separate group of trusted individuals, managed in an independent AWS Organization, can authorize access to logically air-gapped vault contents without access to the affected account. 

 For most workloads, combine these mechanisms to cover every critical data source. 

 The effort to establish this practice is moderate to high. Creating vaults and configuring backup plans is straightforward, but the effort grows with the number of data sources that need alternative mechanisms because of coverage gaps, and with the complexity of your safety-validation and credential-rotation processes. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Inventory critical data sources:** Map each source to the strongest available protection mechanism based on current resource-type support: a logically air-gapped vault, then Vault Lock with a cross-account copy, then [Amazon S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html). 

1.  **Separate backup governance from production administration:** Use [service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) to control who can modify vault configurations and sharing settings. 

1.  **Set retention beyond your threat-detection window:** Configure retention periods that exceed how long a threat could realistically persist before your organization detects it. 

1.  **Point backup plans at protected vaults:** Configure your backup plans to target the protected vaults. 

1.  **Enable malware scanning where supported:** Turn on [Amazon GuardDuty Malware Protection for AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/malware-protection.html) for the resource types it supports. 

1.  **Validate backup safety, not only recoverability:** Extend your restore testing from [REL09-BP04 Perform periodic recovery of the data to verify backup integrity and processes](rel09-bp04.md) to confirm the restored data is in a known-good state, not just that a restore works. Malware scanning alone is not sufficient, because backups may contain data that was corrupted, encrypted, or tampered with in ways that do not match known malware signatures. 

1.  **Select recovery points against an event timeline:** Establish a process that evaluates candidate recovery points against an event timeline built from [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html), [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html), and [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) findings, rather than defaulting to the most recent backup. 

1.  **Rotate credentials after recovery:** Document and exercise a credential-rotation process, and rotate all credentials that were active during the event window before the environment returns to production. [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_managed.html) provides managed rotation for supported credential types. 

1.  **Add multi-party approval for account-level unauthorized access:** For critical workloads where account-level unauthorized access is in the threat model, integrate logically air-gapped vaults with [AWS Backup multi-party approval](https://docs.aws.amazon.com/aws-backup/latest/devguide/multipartyapproval.html), so recovery access is possible through a separate AWS Organization even when the vault-owning account is inaccessible. 

1.  **Exercise the full cyber-recovery capability periodically:** Test the end-to-end capability on a regular schedule, covering safety validation, recovery-point selection, and credential rotation, separate from the standard restore testing in [REL09-BP04 Perform periodic recovery of the data to verify backup integrity and processes](rel09-bp04.md). 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL09-BP01 Identify and back up all data that needs to be backed up, or reproduce the data from sources](rel09-bp01.md) 
+  [REL09-BP02 Secure and encrypt backups](rel09-bp02.md) 
+  [REL09-BP03 Perform data backup automatically](rel09-bp03.md) 
+  [REL09-BP04 Perform periodic recovery of the data to verify backup integrity and processes](rel09-bp04.md) 

 **Related documents:** 
+  [Logically air-gapped vault](https://docs.aws.amazon.com/aws-backup/latest/devguide/logicallyairgappedvault.html) 
+  [AWS Backup Vault Lock](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html) 
+  [What is AWS Backup?](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html#features-by-resource) 
+  [Primary backups to logically air-gapped vaults](https://docs.aws.amazon.com/aws-backup/latest/devguide/lag-vault-primary-backup.html) 
+  [Malware protection in AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/malware-protection.html) 
+  [Multi-party approval for logically air-gapped vaults](https://docs.aws.amazon.com/aws-backup/latest/devguide/multipartyapproval.html) 
+  [Locking objects with Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) 
+  [Managed rotation for AWS Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_managed.html) 