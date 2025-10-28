# Copying continuous backups

If a continuous backup rule also specifies a cross-account or cross-Region copy and
AWS Backup supports the operation for the resource type, AWS Backup takes a snapshot of the resource
and copies the snapshot to the destination vault. To learn more about copying your recovery
points across accounts and Regions, see [Copying a backup](recov-point-create-a-copy.md "recov-point-create-a-copy.md") .

Continuous backups create a periodic backups in accordance with the frequency set in the
backup plan rule in the destination account and/or Region.

AWS Backup does not support on-demand copies of continuous backups.
