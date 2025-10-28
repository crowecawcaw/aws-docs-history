For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Quota and limits

AWS Backup limits the backups to one concurrent backup per resource. Therefore, additional
scheduled or on-demand backup requests for the resource are queued and will start only after the
existing backup job is completed. If the backup job is not started or completed within the backup
window, the request fails. For more information about AWS Backup limits, see [AWS Backup
Limits](../../../aws-backup/latest/devguide/aws-backup-limits.md "../../../aws-backup/latest/devguide/aws-backup-limits.md") in the AWS Backup Developer Guide.

When creating a backup, you can execute up to four concurrent backups per account.
Similarly, you can execute one concurrent restore per account. When you initiate more than four
backup jobs simultaneously, only four backup jobs are initiated and the remaining jobs will be
periodically retried. Once initiated, if the backup job is not completed within the configured
backup window duration, the backup job fails. If the failed backup job is an on-demand backup,
you can retry the backup and for scheduled backups, the job is attempted in the following
schedule.
