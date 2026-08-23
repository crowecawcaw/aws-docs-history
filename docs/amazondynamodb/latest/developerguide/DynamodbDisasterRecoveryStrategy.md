# Choosing your disaster recovery strategy for Amazon DynamoDB workloads

Before selecting a DynamoDB DR strategy, you must define your business recovery requirements. This initial analysis prevents costly over-engineering while helping to ensure you meet critical business continuity needs. The optimal approach balances four key factors: recovery speed, data loss tolerance, implementation complexity, and operational costs.

Let's understand two key metrics that shape your DR strategy:

- **Recovery time objective (RTO)** – This is the maximum acceptable delay between the interruption of service and its restoration. RTO answers the question, How long can we afford to be down? This can range from zero (requiring continuous availability) to several hours, depending on business requirements.
- **Recovery point objective (RPO)** – This represents the maximum acceptable amount of time since the last data recovery point. RPO answers the question, How much data can we afford to lose? For example, if your RPO is 1 hour, your DR solution must make sure you can recover data to a point no more than 1 hour before an incident began.

![Recovery Objectives](images/recoveryobjectives.png)
Your choice of DynamoDB DR strategy should be based on the following factors:

- Business impact analysis of service disruption
- Risk assessment of different disaster scenarios
- Cost of implementing each DR option
- Regulatory requirements for data protection and availability

## Decision points for selecting a DynamoDB DR approach

When selecting the appropriate DynamoDB DR approach, you must evaluate your specific business requirements, risk tolerance, regulatory requirements, and budget constraints.

**For zero downtime** requirements where revenue loss during outages significantly exceeds the additional operational costs, [global tables](GlobalTables.md "GlobalTables.md"), including [multi-Region strong consistency](V2globaltables_HowItWorks.md#V2globaltables_HowItWorks.consistency-modes "V2globaltables_HowItWorks.md#V2globaltables_HowItWorks.consistency-modes") (MRSC) tables, architectures provide instant recovery capabilities. While these solutions carry higher operational costs, they deliver immediate failover and continuous availability, making them essential for mission-critical applications where downtime directly impacts revenue streams.

**Budget-conscious organizations with flexible recovery requirements** can use more cost-effective solutions when applications can tolerate hours of downtime during recovery scenarios. [On-demand backup](backuprestore_HowItWorks.md "backuprestore_HowItWorks.md"), [AWS Backup](backuprestore_HowItWorksAWS.md "backuprestore_HowItWorksAWS.md"), or [Amazon Simple Storage Service export](S3DataExport.HowItWorks.md "S3DataExport.HowItWorks.md") strategies offer significantly lower operational costs while accepting longer recovery timeframes. These approaches work well for applications where business continuity is important but immediate recovery isn't financially justified, providing the option to balance protection with cost optimization.

**Regulatory compliance** requirements need automated solutions that ensure audit readiness and proper data retention policies. [AWS Backup with cross-Region replication](../../../prescriptive-guidance/latest/patterns/copy-amazon-dynamodb-tables-across-accounts-using-aws-backup.md "../../../prescriptive-guidance/latest/patterns/copy-amazon-dynamodb-tables-across-accounts-using-aws-backup.md") provides comprehensive compliance automation while maintaining higher cost structures. This approach delivers the documentation, retention policies, and geographic distribution required by regulatory frameworks while reducing manual compliance overhead and helping to ensure consistent backup procedures across the organization.

**Protection against human-error** scenarios such as accidental deletions or data corruption, [point-in-time recovery](PointInTimeRecovery_Howitworks.md "PointInTimeRecovery_Howitworks.md") (PITR) combined with [deletion protection](WorkingWithTables.Basics.md#WorkingWithTables.Basics.DeletionProtection "WorkingWithTables.Basics.md#WorkingWithTables.Basics.DeletionProtection") offers continuous protection within a single Region. While this solution provides excellent protection against operational mistakes and maintains reasonable costs, you must accept the single-Region limitation and plan additional strategies for true DR scenarios involving regional outages or infrastructure failures.

## Disaster recovery options

DynamoDB offers options for backing up and restoring your table data, providing resilience against various failure scenarios. There are four main DR solutions that serve different needs:

- Point-in-time recovery (PITR) for continuous data protection
- On-demand backup and restore for flexible protection
- Scheduled backup and restore for automated regular protection
- Global tables for instant recovery of mission-critical workloads

| Backup type                                     | Backup option                                                                     | Feature                                                                                                                   | RPO     | RTO                                                                                 | Backup availability                                                                        | Monthly backup cost                               | One-time restoration cost |
| ----------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------- | ------------------------- |
| Continuous data protection                      | PITR                                                                              | Continuous backups retained for up to 35 days, enabling PITR within seconds of any moment in the configured backup window | Seconds | Minutes                                                                             | Single AWS Region only                                                                     | $0.20 per GB-month                                | $0.15 per GB              |
| On-demand protection                            | On-demand backup and restore                                                      | On-demand process                                                                                                         | Hours   | Minutes                                                                             | Single AWS Region                                                                          | $0.10 per GB-month                                | $0.15 per GB              |
| Scheduled backup and restore                    | AWS Backup                                                                        | Flexible scheduling options (hourly to monthly)                                                                           | Hours   | Minutes                                                                             | Cross-Region backup is supported                                                           | $0.10 per GB-month                                | $0.15 per GB              |
| Amazon S3 export and import (with PITR enabled) | Export full or incremental data within PITR windows to an bucket                  | Minutes                                                                                                                   | Hours   | Cross-Region backup to bucket possible                                              | $0.10 per GB                                                                               | $0.15 per GB                                      |
| Instant recovery for mission-critical workloads | Global tables                                                                     | Fully managed solution, multi-Region, multi-active tables                                                                 | Seconds | Zero                                                                                | Automated propagation of data changes from primary to secondary Region within milliseconds | $0.625 per million replicated write request units | 0                         |
| MRSC tables                                     | Fully managed solution, multi-Region, multi-active tables with strong consistency | Zero                                                                                                                      | Zero    | Automated propagation of data changes from primary to secondary Region in real time | $0.625 per million replicated write request units                                          | 0                                                 |

###### Note

Costs shown in the above table are based on N. Virginia Region prices from [DynamoDB pricing](https://aws.amazon.com/dynamodb/pricing/ "https://aws.amazon.com/dynamodb/pricing/") for on-demand capacity.

### Continuous data protection using PITR

Imagine an ecommerce retailer that uses DynamoDB for inventory management, product catalogs, and order processing. While preparing for a Black Friday event, the development team accidentally deletes their product catalog. Using PITR, they can restore thousands of records to the exact pre-incident moment in 30 minutes, preventing millions in potential revenue loss.

When you enable PITR, DynamoDB automatically backs up your table data with per-second granularity. You can restore your table to any given second within your configured recovery period, which ranges from 1–35 days. Notably, reducing the retention period does not decrease costs, making extended retention periods cost-neutral. The PITR feature provides granular recovery capabilities with minimal RPO (seconds) and reasonable RTO (minutes to hours), making it suitable for various DR requirements. Real-world scenarios demonstrate how PITR's minimal RPO and reasonable RTO transform potential business disasters into manageable recovery operations, whether protecting against human error, application failures, or meeting stringent regulatory requirements.

To learn more, see [Enable point-in-time recovery in DynamoDB](Point-in-time-recovery.md "Point-in-time-recovery.md"), which provides detailed instructions on how to configure PITR and restore tables using CloudFormation, AWS CLI, and the DynamoDB API.

### Flexible protection using on-demand backup and restore

Consider a healthcare provider planning a major electronic health record (EHR) system migration. Using milestone backups throughout the migration process would enable them to meet strict HIPAA requirements while providing their legal teams with immutable audit evidence. If compliance issues arose during migration, they could demonstrate exact data handling procedures and restore to any compliant checkpoint, ensuring patient data protection and regulatory adherence.

With the DynamoDB on-demand backup feature, you can create backups and restore tables as needed. On-demand backups operate asynchronously, capturing all changes up to the moment the backup request is made. On-demand backup capabilities give you precise control over your data protection strategy while supporting various operational and compliance requirements.

On-demand backup and restore offers flexible table restoration capabilities across both same-Region and cross-Region scenarios, providing you with versatile recovery options. For enhanced business continuity, DynamoDB delivers instantaneous backup completion regardless of table size, while same-region restorations provide optimal performance to minimize recovery time and maximize operational availability.

By implementing a daily backup strategy, you can achieve reliable RPO of 24 hours, complemented by predictable RTOs of minutes to hours. By using this structured approach to data protection, you can plan and execute your backup and recovery strategies effectively while maintaining business operations.

To learn more about DynamoDB backup and restore operations, see [Backing up a DynamoDB table](backuprestore_HowItWorks.md "backuprestore_HowItWorks.md") and [Restoring a DynamoDB table from a backup](Restore.Tutorial.md "Restore.Tutorial.md").

### Automated regular protection using scheduled backup and restore

DynamoDB provides multiple protection mechanisms that can be automated through scheduled workflows, including AWS Backup with customizable backup plans for operational recovery and Amazon S3 export capabilities for long-term archival, cross-Region data migration and continuous operations. By implementing these automated regular protection schedules, you can ensure consistent data protection without manual intervention while balancing recovery objectives with storage costs.

#### Backup and restore using AWS Backup and backup plans

Consider a multinational bank with operations spanning 15 countries that needed to add enterprise-grade protection to their Amazon DynamoDB based fraud detection system; protection that could adapt to diverse regulatory requirements across jurisdictions while ensuring continuous availability.

Using the multi-Region replication and cross-account capabilities of AWS Backup, the bank implemented a protection architecture that automatically replicated critical transaction data across Regions while maintaining strict access controls for different business units. When regulators in three countries simultaneously requested historical transaction data for compliance audits, the bank's standardized backup policies and detailed audit trails enabled them to provide complete documentation within hours instead of weeks.

With AWS Backup you can take regular backups of your data within a specific AWS account. With backup plans, you can copy these backups to different Regions either on demand or automatically as part of a scheduled backup plan. Backup plans offer flexible scheduling options, so you can choose a frequency that suits your needs: every hour, every 12 hours, daily, weekly, or monthly. DynamoDB backups will be copied across Regions based on the selected frequency.

[AWS Backup Vault Lock](../../../aws-backup/latest/devguide/vault-lock.md "../../../aws-backup/latest/devguide/vault-lock.md") enforces write-once, read-many (WORM) backups to help protect backups (recovery points) in your backup vaults from inadvertent or malicious actions and provides protection against ransomware attacks. You can achieve a RPO of 1 hour and an RTO ranging from a few minutes to hours, depending on the table size.

To understand how AWS Backup integrates with DynamoDB and learn about backup features, and best practices, see [Using AWS Backup with DynamoDB](backuprestore_HowItWorksAWS.md "backuprestore_HowItWorksAWS.md").

#### Amazon Simple Storage Service (Amazon S3) export and import

Imagine a global financial services firm that needs to meet regulatory requirements for transaction data across multiple jurisdictions while maintaining 99.99% availability. They could build their enterprise data strategy around the export and import capabilities of Amazon S3, implementing cross-Region data replication to comply with data sovereignty laws in 12 countries and establishing Regional failover mechanisms. Should a European outage occur, these systems would automatically execute failover procedures, helping to ensure zero trading disruption and continuous operations.

The company used the export/import to Amazon S3 feature to create daily full backups and hourly incremental exports to jurisdiction-specific Amazon S3 buckets across all 12 Regions, helping to ensure compliance with local data residency requirements. Each Regional table automatically exported transaction data to encrypted buckets within the same jurisdiction, while cross-Region replication provided additional redundancy for critical datasets. Exports don't consume read capacity units (RCUs) and have no impact on table performance or availability. If there's an impairment on one of the Regions where the company operates, automated recovery procedures can restore the most recent export to an alternate Region, enabling full trading operations to resume. This export/import strategy provides both regulatory compliance through immutable audit trails and robust DR capabilities. The firm can maintain continuous operations while preserving complete transaction histories that can be restored to new tables in any available Region, helping to minimize data loss and downtime during regional infrastructure failures.

With DynamoDB export to Amazon S3, you can export data from a DynamoDB table at a point within your PITR window. You can achieve an RPO of a few minutes and an RTO ranging from a few minutes to hours, depending on the table size.

For detailed implementation guidance on configuring exports, see [Requesting a table export in DynamoDB](S3DataExport.HowItWorks.md "S3DataExport.HowItWorks.md"). For restore operations and importing data from , see [Requesting a table import in DynamoDB](S3DataImport.HowItWorks.md "S3DataImport.HowItWorks.md").

### Instant recovery of mission-critical workloads using global tables

DynamoDB global tables provide robust failover capabilities during primary Region disruption; applications can immediately redirect traffic to healthy Regions and continue operations. Global tables have two options: multi-Region eventual consistency (MREC) and multi-Region strong consistency (MRSC).

#### Multi-Region eventual consistency

Imagine a multinational ecommerce service serving millions of customers across North America, Europe, and Asia-Pacific that could face significant operational challenges without proper global infrastructure. The company might struggle with slow checkout times for international customers, complex compliance requirements across multiple jurisdictions, and frequent disruptions during regional outages. By implementing DynamoDB global tables, they could transform their operations: customers in Tokyo would experience the same lightning-fast checkout times as those in New York through ultra-low latency local data access. Should a severe weather event disrupt their primary Region, their application could seamlessly fail over to another Region without customers noticing. This approach maintains high availability, improves global read and write latency, supports regulatory compliance across the Regions where they operate, and gives the company confidence to expand into new markets knowing their infrastructure can scale reliably worldwide while meeting local requirements.

DynamoDB global tables offer a fully managed, multi-Region, multi-active database solution designed to provide fast and localized read and write performance for massively scaled global applications. For DR purposes, you can specify the primary Region and the DR Region where you want the tables to be available. DynamoDB automatically propagates ongoing data changes from the primary Region to the DR replica. With MREC setup, you can achieve an RPO of a few seconds and an RTO of zero.

For guidance on creating and managing DynamoDB global tables, see [Global tables - multi-Region replication for DynamoDB](GlobalTables.md "GlobalTables.md").

#### Multi-Region strong consistency

Imagine a leading digital banking platform processing millions of transactions daily across three continents that could experience a significant regional outage during peak trading hours. Instead of scrambling with manual DR procedures and facing potential millions in losses, their architecture would activate DR within seconds, seamlessly redirecting traffic to healthy Regions without customers noticing a disruption. The bank's mobile app could continue processing loan applications in real-time, their trading platform would maintain millisecond response times for high-frequency transactions, and customer account balances would remain perfectly synchronized across all Regions.

With multi-Region strongly consistent global tables, you can build applications with zero RPO. An RPO of zero means your applications can read the most up-to-date version of DynamoDB data, even if an application interruption requires you to shift traffic to a different Region.

###### Note

For DR purposes, you can use two replicas and one witness Region.

For more information about creating MRSC global tables, see [How global tables work](V2globaltables_HowItWorks.md "V2globaltables_HowItWorks.md").
