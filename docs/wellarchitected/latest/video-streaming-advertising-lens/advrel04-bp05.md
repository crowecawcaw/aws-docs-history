

# ADVREL04-BP05 Back up data in multiple locations with consideration for regulatory requirements
<a name="advrel04-bp05"></a>

 Select geographic regions for backup locations that satisfy your legal and business requirements. Consumer privacy laws might restrict where you can replicate data that contains personal data. Countries where your workload operates might also regulate advertising and related data. 

 **Desired outcome:** 
+  Advertising data is backed up in multiple locations to protect against regional failures. 
+  Backup location choices comply with data residency regulations. EU audience data isn't replicated to non-EU regions without explicit compliance review. 
+  Data handling agreements with advertising partners are reflected in backup and replication configurations. 

 **Common anti-patterns:** 
+  Replicating backups to whatever region is cheapest or nearest without checking data residency obligations. 
+  Replicating EU personal data to non-EU regions without an adequacy decision or compliance review. 
+  Transferring KMS key material between regions to enable cross-region restore instead of using Multi-Region keys. 
+  Ignoring partner data handling agreements when configuring backup and replication of shared audience or measurement data. 

 **Benefits of establishing this best practice:** 
+  Data is recoverable from multiple locations, protecting against regional failures. 
+  Backup topology respects data residency law, avoiding regulatory exposure from noncompliant replication. 
+  Multi-region KMS keys enable cross-region restoration without insecure key material transfer. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 The fastest or cheapest backup Region might be legally off-limits for the data you protect. Advertising systems process personal identifiers such as device IDs, hashed emails, location signals, and bid-stream metadata. Privacy frameworks like GDPR treat any copy of that data, including backups, as processing activity. The transfer restrictions on the live dataset apply to those copies. For example, an architect who selects a backup Region on latency or cost grounds may inadvertently create an unlawful data transfer when replication begins. Have legal counsel validate Region choices before you configure replication. 

 If a regulator orders deletion of unlawfully transferred data, backups in the noncompliant Region become unrestorable. Consent and purpose limitations follow the data into every replica. A segment collected under one lawful basis can't be backed up, or later restored for use, in a Region where that basis doesn't apply. Think of backup topology as a privacy-engineering decision, not only an infrastructure-availability decision, because legal constraints that prohibit restoration can render a backup unusable. 

 Demand-side platforms, data-management platforms, and measurement vendors each impose contractual limits on where their data can reside and how long copies persist. Replicating partner audience segments into regions or retention windows not covered by the data-handling agreement can trigger contract breach and loss of data-sharing access. Treat partner agreements as a hard constraint on your backup design to avoid blocking business recoverability. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Create a backup topology that addresses data residency requirements:** For each data category, document the permitted backup regions based on regulatory requirements, cross-Region replication configuration, and encryption key management for cross-region access. Create a decision matrix that maps (data type × user geography) to permitted backup Regions. 

1.  **Configure KMS Multi-Region keys for cross-region backup encryption:** Create KMS Multi-Region primary keys in your primary region and replica keys in your backup regions. Use these keys for encrypting backups that must be restorable in multiple regions. This removes the need to transfer key material while maintaining encryption protection in all backup locations. 

1.  **Document and periodically review partner data handling agreements:** For advertising data shared with partners (audience segments from DMPs, measurement data from third-party vendors), review data handling agreements to understand what backup and replication rights you have. Update backup configurations when agreements change. Include partner data handling terms in annual compliance reviews. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL03-BP02 Choose AWS Regions that meet your legal and disaster recovery requirements](advrel03-bp02.md) 
+  [ADVREL07-BP03 Implement secure and privacy-preserving recovery mechanisms for collaboration workloads](advrel07-bp03.md) 

 **Related documents:** 
+  [AWS Key Management Service multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) 
+  [Amazon DynamoDB backup features](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BackupRestore.html) 

 **Related services:** 
+  [AWS KMS](https://aws.amazon.com/kms/) 
+  [AWS Backup](https://aws.amazon.com/backup/) 