For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Working with AWS Backup

The data protection functionality in Amazon Timestream for LiveAnalytics is a fully managed solution to help you meet
your regulatory compliance and business continuity requirements. The functionality is enabled
through native integration with AWS Backup, a unified backup service designed to simplify the creation,
migration, restoration, and deletion of backups, while providing improved reporting and auditing.
Through integration with AWS Backup, you can use a fully managed, policy-driven centralized data
protection solution to create immutable backups and centrally manage data protection of your
application data spanning Timestream and other AWS services supported by AWS Backup.

To use the functionality, you must [opt-in](../../../aws-backup/latest/devguide/service-opt-in.md "../../../aws-backup/latest/devguide/service-opt-in.md") to allow AWS Backup to protect
your Timestream resources. Opt-in choices apply to the specific account and AWS Region, so you
might have to opt in to multiple Regions using the same account. For more information on AWS
Backup, see the [AWS Backup Developer Guide](../../../aws-backup/latest/devguide/whatisbackup.md "../../../aws-backup/latest/devguide/whatisbackup.md").

Data Protection functionality available through AWS Backup includes the following.

**Scheduled backups**—You can set up regularly scheduled
backups of your Timestream for LiveAnalytics tables using backup plans.

**Cross-account and cross-Region copying**—You can
automatically copy your backups to another backup vault in a different AWS Region or account,
which allows you to support your data protection requirements.

**Cold storage tiering**—You can configure your backups
to implement life cycle rules to delete or transition backups to colder storage. This can help you
optimize your backup costs.

**Tags**—You can automatically tag your backups for
billing and cost allocation purposes.

**Encryption**—Your backup data is stored in the AWS Backup
vault. This allows you to encrypt and secure your backups by using an AWS KMS key that is
independent from your Timestream for LiveAnalytics table encryption key.

**Secure backups using the WORM model**—You can use AWS Backup
Vault Lock to enable a write-once-read-many (WORM) setting for your backups. With AWS Backup Vault
Lock, you can add an additional layer of defense that protects backups from inadvertent or
malicious delete operations, changes to backup retention periods, and updates to lifecycle
settings. To learn more, see [AWS Backup Vault Lock](../../../aws-backup/latest/devguide/vault-lock.md "../../../aws-backup/latest/devguide/vault-lock.md").

The data protection functionality is available in all regions To learn more about the
functionality, see the [AWS Backup Developer Guide](../../../aws-backup/latest/devguide/whatisbackup.md "../../../aws-backup/latest/devguide/whatisbackup.md").
