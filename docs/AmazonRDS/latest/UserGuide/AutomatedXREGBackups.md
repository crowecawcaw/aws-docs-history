# Troubleshooting stopped cross-Region automated backups

Amazon RDS automatically stops cross-Region automated backup replication under specific
circumstances to protect your data and maintain compliance with AWS operational requirements.

## Account suspension

If your AWS account is suspended, Amazon RDS automatically stops cross-Region automated backup replication for all DB instances in that account. The replicated backups that already exist in the destination AWS Region are kept up to your specified retention period.

After your account suspension is resolved, you must manually re-enable cross-Region automated backup replication to resume replicating backups to the destination AWS Region.

## Opt-in Region changes

Cross-Region automated backup replication stops automatically when you opt out of either the source AWS Region (where the primary DB instance is located) or the destination AWS Region (where backups are being replicated). For more information about opt-in Regions, see [Managing AWS Regions](../../../general/latest/gr/rande-manage.md "../../../general/latest/gr/rande-manage.md").

The replicated backups that already exist in the destination AWS Region are kept up to your specified retention period. To resume replication, opt back into the required AWS Region and manually re-enable cross-Region automated backup replication.

## AWS KMS key issues

For encrypted DB instances, Amazon RDS requires access to AWS KMS keys in both the source and destination AWS Region
to replicate backups. If you disable or delete the AWS KMS key in either AWS Region, cross-Region automated backup
replication stops automatically. The replicated backups that already exist in the destination AWS Region are kept up to your specified retention period.

To resume cross-Region automated backup replication:

1. Re-enable the disabled AWS KMS key, or create a new AWS KMS key if the original was deleted
2. If using a new AWS KMS key, delete existing replicated backup in the destination AWS Region that was encrypted with the previous key.
3. Re-enable cross-Region automated backup replication for the instance

For more information about managing AWS KMS keys, see [AWS Key Management Service documentation](../../../kms/latest/developerguide.md "../../../kms/latest/developerguide.md").

###### Note

You cannot restore from previously replicated backups in the destination AWS Region unless the previous AWS KMS key is re-enabled. The backups remain encrypted and inaccessible without a valid AWS KMS key.

## Monitoring backup replication status

You can monitor the status of your cross-Region automated backups using the Amazon RDS console, AWS CLI, or RDS API. For more information, see [Finding information about replicated backups for Amazon RDS](AutomatedBackups.Replicating.md "AutomatedBackups.Replicating.md").
