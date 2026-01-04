# LSREL02-BP02 Maintain continuous data availability and

integrity

Implement real-time or near-real-time data replication strategies
across Availability Zones or AWS Regions to protect against system
failures or maintenance interruptions. Use warm standby environments
with synchronized datasets to enable quick failover and avoid data
loss or research disruption.

**Desired outcome:**

- Continuous data access during maintenance and outages.
- Minimal risk of data loss or corruption across failure events.
- Trust in the accuracy, completeness, and reproducibility of
  research datasets.

**Common anti-patterns:**

- Relying on manual backups without automated validation or
  recovery testing.
- Replicating data without maintaining consistency or integrity
  verification.
- Treating replication as optional for intermediate or temporary
  data sources unless cost/time-effective to reproduce.

**Benefits of establishing this best
practice:**

- Enables uninterrupted access to experimental results and
  research datasets.
- Reduces risk of losing critical data from unique or costly
  experiments.
- Supports reproducibility and regulatory adherence (like audit
  trails and traceability).
- Strengthens collaboration by making shared datasets available
  globally.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Data availability must be preserved even when system components
undergo maintenance or fail unexpectedly. Structured research
data, such as LIMS transactions, should use multi-zone replication
to maintain availability, while unstructured research datasets
should be replicated across independent storage domains.
Monitoring replication lag and validating dataset consistency are
critical to avoid silent data corruption. Automated recovery
validation and regular restore drills build trust that data can be
recovered accurately and within defined RPO and RTO objectives.

### Implementation steps

1. Configure Amazon RDS Multi-AZ deployments for LIMS databases
   to achieve transactional durability.
2. Use Amazon S3 Cross-Region Replication (CRR) for
   uninterrupted access to critical datasets, and protect
   large-scale file-based research workloads with Amazon FSx for Lustre combined with snapshot policies managed by AWS Backup.
3. Define automated recovery validation policies in AWS Backup
   for audit tracking.
4. Continuously monitor replication lag and recovery objectives
   through Amazon CloudWatch, aligning recovery metrics with
   the needs of research workflows.

## Resources

**Related best practices:**

- Data lifecycle management for research datasets
- Data integrity and reproducibility controls
- Governance documentation for GxP-relevant systems
