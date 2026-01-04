# LSREL09-BP03 Verify data integrity and point-in-time

recovery

Protect application and data state so that you can restore to a
precise point-in-time prior to a failed change. Backups must be
consistent, validated, and aligned with organizational RTO and RPO
targets. Include configuration and metadata in backups so restored
environments are audit-complete.

**Desired outcome:** Data and
application state can be restored to the exact state prior to the
failed change, preserving adherence and operational continuity.

**Common anti-patterns:**

- Infrequent or unplanned backups without restore validation.
- Omitting metadata or configuration in backup sets.
- Not aligning backup frequency to defined RTO and RPO needs of
  regulated systems.

**Benefits of establishing this best
practice:**

- Avoids loss of experiment data, patient records, or audit
  evidence during failed changes.
- Shortens recovery time, preserving study timelines and sample
  integrity.
- Demonstrates recoverability to auditors and stakeholders.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Define RTO and RPO aligned to the criticality of datasets and
regulated processes. Implement automated, policy-driven backups
that include application-level snapshots, database backups
(including transaction logs for point-in-time recovery), and
configuration exports. Regularly perform restore drills and
document restoration time and fidelity as part of validation
evidence. Store backups in tamper-evident, redundant storage and
that retention policies meet regulatory retention requirements.

### Implementation steps

1. Implement policy-driven backups using AWS Backup for
   supported services.
2. Enable automated backups and snapshots for databases (for
   example, automated backups for Amazon RDS and snapshot
   schedules for Amazon EC2 or Amazon EBS).
3. Configure point-in-time recovery for services that support
   it, such as enabling PITR for Amazon DynamoDB.
4. Store and catalog backup artifacts in Amazon S3 with
   appropriate lifecycle and retention rules, and use AWS Backup's recovery testing features to validate restores.

## Resources

**Related best practices:**

- Long-term storage and reliable recovery of trial data
- Observability and monitoring of pipelines
- Automated validation in deployments
