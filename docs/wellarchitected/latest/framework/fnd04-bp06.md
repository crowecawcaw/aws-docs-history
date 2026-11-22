

# FND04-BP06 Establish centralized backup standards and mechanisms

 Backups are a foundation capability every workload depends on, but without central standards each team builds its own approach. The result is inconsistent coverage, mixed retention periods, untested restore procedures, and vaults that might not survive the incident they were meant to recover from. A central backup foundation gives workload teams reliable backup and restore primitives so they do not have to design backup from scratch. 

 **Desired outcome:** 
+  Your foundation team provides a central backup service that workload teams consume, covering the resource types used across the organization. 
+  Your backup policies are applied organization-wide through AWS Backup and AWS Organizations, with coverage verified through reporting. 
+  Your backups are stored in accounts and Regions separate from the workloads they protect, with vault lock in place for retention-critical data. 
+  Your backup plans align to data classification tiers so critical workloads have longer retention and more frequent backups than non-critical ones. 
+  Your restore procedures are documented and exercised regularly so workload teams know how to recover before they need to. 

 **Common anti-patterns:** 
+  Each workload team configuring backups on its own, with no central record of which workloads are covered or what retention they use. 
+  Storing backups in the same account as the workloads they protect, so unauthorized access at the workload account level also reaches the recovery path. 
+  Relying on service-specific snapshots (EBS, RDS) without cross-account copy, so account deletion takes the backups with it. 
+  Setting uniform retention across all data regardless of classification, either paying for long retention of ephemeral data or losing regulated data too soon. 
+  Treating backups as write-only: configuring them but never restoring, so the first real restore is the one that has to work during an incident. 
+  Deploying backup policies without vault lock or immutability, leaving the door open for a ransomware actor to delete the backups before encrypting the data. 

 **Benefits of establishing this best practice:** 
+  Consistent backup coverage across the organization because every in-scope resource is backed up through the same central service. 
+  Stronger protection against unauthorized account-level access and ransomware because backups are stored in separate, isolated vaults with immutability controls. 
+  Lower operational effort for workload teams because backup configuration is inherited from central policies rather than built per workload. 
+  Reliable recovery because restore procedures are documented, exercised, and understood by teams before an incident forces them. 
+  Clear compliance evidence because central reporting shows which resources are covered, how often they are backed up, and how long they are retained. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Most organizations have backups in the sense that some teams have configured snapshots for some resources, but they struggle to accurately determine which workloads are covered, where the backups are stored, whether the backups would survive unauthorized access in the source account, and whether the restore procedure has ever been tested in its entirety. Ransomware encrypts data and the backup vault along with it, an account is deleted and the snapshots go with it, or a restore attempt reveals the last successful backup was weeks old. 

 A central backup foundation solves this problem by moving backup from a per-workload concern to a foundation-provided capability. The foundation team owns the backup service, the storage destinations, and the policy framework. Workload teams consume the service by tagging resources for backup or by inheriting backup plans through account membership, and the foundation team provides restore runbooks and exercises that keep the recovery path working. 

 [AWS Backup](https://aws.amazon.com/backup/) is the natural central service. It supports most AWS compute, storage, database, and file service resource types with a single policy framework, and it integrates with [AWS Organizations](https://docs.aws.amazon.com/aws-backup/latest/devguide/manage-cross-account.html) so policies can be applied across all accounts. [Backup plans](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup-plan.html) define the schedule, retention, and backup vault. [Resource assignment](https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html) uses tags or resource types to decide what each plan covers. With this combination, the foundation team can publish tier-based backup plans (critical, standard, low-value), and workload teams opt in by tagging resources with the appropriate tier. [Backup policies in AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_backup.html) distribute these plans to accounts or OUs based on the organizational structure. Production OUs get the standard production backup plan automatically, and DR or compliance-scoped OUs get stricter versions layered on top. 

 [Cross-account backup copies](https://docs.aws.amazon.com/aws-backup/latest/devguide/create-cross-account-backup.html) replicate backups to a dedicated backup account, which survives unauthorized access to or deletion of the source account. A workload account where unauthorized access has occurred must not be able to reach into the backup account and delete what is stored there. Pair cross-account copies with [AWS Backup Vault Lock](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html) to enforce retention on the backup vault. After vault lock is in compliance mode, even administrators cannot shorten retention or delete backups before they expire. [Cross-Region backup copies](https://docs.aws.amazon.com/aws-backup/latest/devguide/cross-region-backup.html) protect against Region-level events and provide the primitive that workload-level DR plans build on. Not every workload needs cross-Region backup, so this is usually reserved for the critical tier. 

 Backups are encrypted at rest using KMS keys, and those keys need to be accessible during restore. Multi-Region keys or cross-account key sharing is often required. If the backup vault uses a key that exists only in the source account, and the source account is unavailable or lost, the backups become unrecoverable. Refer to your organization's encryption and key management standards for how backup keys fit into the broader key ownership model. 

 Backups that have never been restored are untested. Build recovery exercises into the foundation team's calendar, rotate which workload teams are exercised, and document the results. When an exercise reveals a gap (missing permissions, outdated runbooks, a service type not covered by the backup plan), fix it before the next exercise. 

**Important**  
 Vault Lock in compliance mode is irreversible within the defined retention period. Even the root user cannot shorten retention or delete a locked vault. Validate your retention requirements in a non-production vault before enabling compliance mode in production. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Designate a delegated administrator for AWS Backup:** From the management account, [register a delegated administrator](https://docs.aws.amazon.com/aws-backup/latest/devguide/manage-cross-account.html) for AWS Backup, typically your central operations or infrastructure account. Create a dedicated backup account separate from workload accounts to receive cross-account backup copies. 

1.  **Define backup tiers aligned to data classification:** Publish standard backup tiers (for example, critical, standard, archive) and document the frequency, retention, and destination for each tier. Critical data might be backed up daily with 90-day retention plus monthly archives for 7 years, and low-value data might use service snapshots with short retention. Align tiers to the data classification scheme already in use by the organization. 

1.  **Publish organization-wide backup plans through backup policies:** Create [AWS Backup plans](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup-plan.html) for each tier and distribute them through [AWS Organizations backup policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_backup.html). Apply policies to OUs so accounts inherit backup configuration based on their role. Production accounts get the production plan automatically, and sandbox accounts get a lightweight plan or none at all. 

1.  **Configure cross-account backup copies:** Set up [cross-account backup copies](https://docs.aws.amazon.com/aws-backup/latest/devguide/create-cross-account-backup.html) so that each backup created in a workload account is copied into the dedicated backup account. Key the cross-account vault policy to the principal types that need to read the backups during recovery (the workload account role, the backup account restore role), not to the source account as a whole. 

1.  **Enable AWS Backup Vault Lock on retention-critical vaults:** Enable [Vault Lock](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html) on vaults that hold backups with regulated retention requirements. Test vault lock behavior in a non-production vault first to confirm the minimum and maximum retention periods fit your requirements before applying compliance mode in production. 

1.  **Add cross-Region copies for the critical tier:** Configure [cross-Region backup copies](https://docs.aws.amazon.com/aws-backup/latest/devguide/cross-region-backup.html) from the primary backup Region to a secondary Region for the critical tier. Size the secondary Region's service quotas for the expected backup storage and restore capacity so that a cross-Region restore does not hit quota limits mid-recovery. 

1.  **Automate resource assignment through tagging:** Require workload teams to tag resources with their backup tier (for example, BackupTier: critical). Use [AWS Backup resource assignment by tag](https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html#assigning-resources-by-tag) so that tagged resources are picked up automatically by the appropriate plan. Enforce the tagging requirement through AWS Config rules or tag policies so that resources without a backup tag are surfaced for remediation. 

1.  **Monitor backup coverage and compliance:** Use [AWS Backup Audit Manager](https://docs.aws.amazon.com/aws-backup/latest/devguide/aws-backup-audit-manager.html) to report on backup coverage, retention compliance, and restore testing activity across the organization. Route compliance findings to the foundation team for triage and to workload teams for the resources they own. Integrate the coverage view into your central operations dashboards so gaps surface quickly. 

1.  **Exercise restores regularly:** Schedule regular restore exercises with rotating workload teams. Each exercise covers the full path: identify the backup, approve the restore, perform the restore into a test environment, validate the restored data, and document any gaps. Include cross-account and cross-Region restore scenarios so that the paths that matter during a real incident are the ones that have been tested. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND04-BP01 Implement standardized attribution policies](fnd04-bp01.md) 
+  [FND04-BP02 Establish an organization view of cloud inventory and dependencies](fnd04-bp02.md) 
+  [FND05-BP10 Prepare forensic capabilities](fnd05-bp10.md) 
+  [REL09-BP01 Identify and back up all data that needs to be backed up, or reproduce the data from sources](rel09-bp01.md) 
+  [REL09-BP03 Perform data backup automatically](rel09-bp03.md) 

 **Related documents:** 
+  [AWS Backup Developer Guide](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) 
+  [Manage AWS Backup resources across multiple AWS accounts](https://docs.aws.amazon.com/aws-backup/latest/devguide/manage-cross-account.html) 
+  [Backup policies in AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_backup.html) 
+  [AWS Backup Vault Lock](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html) 
+  [AWS Prescriptive Guidance - Backup and Recovery](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/storageandbackup-pattern-list.html) 
+  [Resilience by design: Building an effective ransomware recovery strategy](https://aws.amazon.com/blogs/storage/resilience-by-design-building-an-effective-ransomware-recovery-strategy/) 

 **Related examples:** 
+  [Use backups to recover from security incidents](https://aws.amazon.com/blogs/security/use-backups-to-recover-from-security-incidents/) 

 **Related services:** 
+  [AWS Backup](https://aws.amazon.com/backup/) 
+  [AWS Backup Audit Manager](https://docs.aws.amazon.com/aws-backup/latest/devguide/aws-backup-audit-manager.html) 