# Best Practice 8.3 – Secure your data

recovery mechanisms to protect against threats

To help protect against malicious activities, follow the guidelines set out within
your organization’s security framework. [Protecting against ransomware](https://aws.amazon.com/security/protecting-against-ransomware/ "https://aws.amazon.com/security/protecting-against-ransomware/")
provides an overview of the key items to
address before an incident and as part of an incident response including network controls,
patching, and least privilege permissions. For SAP systems, the threat is similar to other
applications, but the impact is potentially greater. If SAP is a system of record, or
required for mission critical transactions, consider the following suggestions to secure a
backup against a malicious attack.

- SAP Note: [2663467

* Tips to avoid a Ransomware situation](https://launchpad.support.sap.com/#/notes/2663467 "https://launchpad.support.sap.com/#/notes/2663467") [Requires SAP Portal Access]

- SAP Note: [2496239

* Ransomware / malware on Windows](https://launchpad.support.sap.com/#/notes/2496239 "https://launchpad.support.sap.com/#/notes/2496239") [Requires SAP Portal Access]

**Suggestion 8.3.1 – Secure backups in a separate account with
additional controls**

By securing backups in an account that is isolated from the primary copy of your data,
either directly or using replication, it’s possible to minimize the risk of a compromised
system also impacting your data recovery mechanisms.

The secondary account can be viewed as a “data bunker” with access requirements
aligned to the use case.

For backups using Amazon S3, additional controls might include S3 Object Lock to
store objects using a write-once-read-many (WORM) model or [multi-factor authentication delete](../../../AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.md "../../../AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.md").

If using replication, understand the different options available, including [delete marker replication](../../../AmazonS3/latest/userguide/delete-marker-replication.md "../../../AmazonS3/latest/userguide/delete-marker-replication.md") (by default deletion markers are not replicated) and
[S3 Replication Time Control](../../../AmazonS3/latest/userguide/replication-time-control.md "../../../AmazonS3/latest/userguide/replication-time-control.md"). To optimize costs, ensure that housekeeping is
performed on both the primary and secondary buckets.

Consider [AWS Backup Audit Manager](https://aws.amazon.com/about-aws/whats-new/2022/03/aws-backup-audit-manager-controls-compliance-backups-accounts/ "https://aws.amazon.com/about-aws/whats-new/2022/03/aws-backup-audit-manager-controls-compliance-backups-accounts/") to monitor and prove compliance for immutable backups
across Regions and accounts.

**Suggestion 8.3.2 – Validate your ability to recover**

Backups are the last line of defense when protecting your data from malicious
activities, but might prove worthless if recovery is not possible due to incomplete
backups or backups that are not valid. Recovery might not be possible if you are unable to
access or decrypt backups. Consider how you protect encryption keys and
credentials.

Perform recovery tests aligned with a malicious scenario, including a rebuild in an
alternate account.

- SAP Lens [Operational Excellence]: [Best
  Practice 4.3 - Regularly test business continuity plans and fault recovery](best-practice-4-3.md "best-practice-4-3.md")
