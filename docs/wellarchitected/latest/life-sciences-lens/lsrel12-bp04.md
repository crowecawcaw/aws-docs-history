# LSREL12-BP04 Implement cyber resilience for GxP-regulated

backup data

Implement cyber resilience strategies for your backup data to
protect against ransomware and other cyber threats, with specific
considerations for GxP-regulated systems. Cyber resilience goes
beyond traditional backup approaches by keeping backups immutable,
isolated, and recoverable even during sophisticated cyber attacks
while maintaining data integrity in accordance with ALCOA+
principles.

**Desired outcome:** A robust backup
strategy that protects GxP-regulated data from cyber threats, which
recovers clean, unaltered data following an attack while maintaining
regulatory adherence and data integrity.

**Common anti-patterns:**

- Relying solely on encryption without implementing immutability,
  leaving GxP data backups vulnerable to deletion.
- Using the same security domain for production and backup
  systems, allowing credential compromise to affect both
  environments.
- Assuming backups are valid without regular validation testing,
  potentially discovering issues only during actual recovery.
- Allowing single-person authorization for critical recovery
  operations, reducing segregation of duties required for
  regulated systems.
- Failing to document backup immutability controls as part of the
  quality management system.

**Benefits of establishing this best
practice:**

- Enhanced protection against ransomware and other cyber threats
  that specifically target backup infrastructure.
- Maintained data integrity for GxP-regulated information during
  recovery.
- Improved confidence in recovery capabilities during security
  incidents.
- Enhanced adherence to regulatory requirements for data
  protection and recovery.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Traditional backup approaches for GxP systems focus on data
availability and integrity but may not adequately address
sophisticated cyber threats that specifically target backup
infrastructure. Life sciences organizations must implement
cyber-resilient backup strategies that maintain regulatory
adherence while protecting against evolving threats.

Implement a comprehensive cyber resilience strategy for your
GxP-regulated backups that includes four fundamental pillars:

- **Immutability:** Stop backup
  data from being altered or deleted during its retention
  period, maintaining the ALCOA+ principle of originality
- **Logical isolation:** Separate
  backup storage from production environments with distinct
  security controls to avoid compromise of both systems
- **Integrity validation:**
  Regularly verify backup data remains uncorrupted and can be
  successfully restored, improving ongoing adherence to data
  integrity requirements
- **Access controls:** Implement
  multi-party approval for critical recovery operations to
  maintain appropriate segregation of duties for regulated
  systems

For GxP-regulated systems, document your cyber-resilient backup
strategy within your quality management system, including
validation of backup immutability controls and recovery processes.
This documentation should address how your backup strategy adheres
data integrity requirements and should be sufficient to
demonstrate regulatory adherence during inspections or audits.

### Implementation steps

1. Assess your GxP backup strategy for cyber resilience gaps:

- Evaluate current backup solutions for immutability
  capabilities and potential vulnerabilities.
- Identify potential attack vectors that could compromise both
  production and backup systems.
- Determine appropriate retention periods based on data
  criticality, regulatory requirements, and threat models.
- Document recovery time objectives (RTOs) and recovery point
  objectives (RPOs) for cyber recovery scenarios.
- Classify backup data based on GxP relevance and criticality.

1. Implement immutable backup storage for GxP data:

- Configure AWS Backup Vault Lock or S3 Object Lock for GxP
  data with appropriate retention periods.
- Define immutability settings based on data classification
  and regulatory requirements.
- Implement technical controls to avoid override of
  immutability settings.
- Document immutability configurations in your data protection
  policies and Quality Management System.
- Test immutability by attempting to delete or modify
  protected backups.

1. Establish logical isolation for GxP backup storage:

- Create dedicated AWS accounts for GxP backup storage with
  separate administrative controls.
- Implement AWS Backup logically air-gapped vault for critical
  GxP systems requiring enhanced protection.
- Configure strict cross-account access controls using IAM and
  service control policies (SCPs).
- Establish network isolation between production and backup
  environments.
- Implement separate authentication mechanisms for backup
  administration.
- Document isolation controls in your Quality Management
  System.

1. Implement multi-party approval for GxP system recovery:

- Configure AWS Backup multi-party approval workflows for GxP
  systems.
- Define approver roles and responsibilities with appropriate
  separation of duties.
- Document escalation procedures for emergency scenarios
  requiring expedited recovery.
- Implement comprehensive audit trails for approval actions.
- Align your approval workflows with your quality management
  system requirements.
- Regularly test approval workflows to verify effectiveness
  during actual incidents.

1. Validate GxP backup integrity and recovery processes:

- Implement AWS Backup restore testing with automated
  validation of restored resources.
- Schedule regular recovery exercises in isolated environments
  for critical GxP systems.
- Document validation procedures and success criteria for
  different resource types.
- Test recovery from various cyber attack scenarios including
  ransomware and data corruption.
- Validate data integrity after restoration to improve
  consistency and completeness.
- Maintain validation documentation as part of your quality
  management system.

1. Monitor and audit GxP backup protection:

- Configure AWS CloudTrail logging for backup and recovery
  operations.
- Implement Amazon CloudWatch alarms for unauthorized access
  attempts or policy violations.
- Regularly review backup protection controls through
  automated checks.
- Conduct periodic security assessments of backup
  infrastructure.
- Maintain comprehensive documentation of cyber resilience
  controls for audits and regulatory inspections.

## Resources

**Related best practices:**

- LSREL13-BP01
- LSOPS03-BP01

**Related documents:**

- [GxP
  Systems on AWS](../../../whitepapers/latest/gxp-systems-on-aws/gxp-systems-on-aws.md "../../../whitepapers/latest/gxp-systems-on-aws/gxp-systems-on-aws.md")
- [Building
  cyber resiliency with AWS Backup logically air-gapped
  vault](https://aws.amazon.com/blogs/storage/building-cyber-resiliency-with-aws-backup-logically-air-gapped-vault/ "https://aws.amazon.com/blogs/storage/building-cyber-resiliency-with-aws-backup-logically-air-gapped-vault/")
- [Validate
  recovery readiness with AWS Backup restore testing](https://aws.amazon.com/blogs/storage/validate-recovery-readiness-with-aws-backup-restore-testing/ "https://aws.amazon.com/blogs/storage/validate-recovery-readiness-with-aws-backup-restore-testing/")
- [Ransomware
  Risk Management on AWS Using the NIST Cyber Security
  Framework](../../../whitepapers/latest/ransomware-risk-management-on-aws-using-nist-csf/ransomware-risk-management-on-aws-using-nist-csf.md "../../../whitepapers/latest/ransomware-risk-management-on-aws-using-nist-csf/ransomware-risk-management-on-aws-using-nist-csf.md")

**Related examples:**

- [Building
  cyber resiliency with AWS Backup logically air-gapped
  vault](https://aws.amazon.com/blogs/storage/building-cyber-resiliency-with-aws-backup-logically-air-gapped-vault/ "https://aws.amazon.com/blogs/storage/building-cyber-resiliency-with-aws-backup-logically-air-gapped-vault/")
- [Validate
  recovery readiness with AWS Backup restore testing](https://aws.amazon.com/blogs/storage/validate-recovery-readiness-with-aws-backup-restore-testing/ "https://aws.amazon.com/blogs/storage/validate-recovery-readiness-with-aws-backup-restore-testing/")
- [Improve
  recovery resilience with AWS Backup support for Multi-party
  approval](https://aws.amazon.com/blogs/storage/improve-recovery-resilience-with-aws-backup-support-for-multi-party-approval/ "https://aws.amazon.com/blogs/storage/improve-recovery-resilience-with-aws-backup-support-for-multi-party-approval/")

**Related tools:**

- AWS Backup
- AWS Backup Vault Lock
- Amazon S3 Object Lock
- AWS CloudTrail
- Amazon CloudWatch
- AWS IAM
