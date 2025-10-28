# Copy tags onto backups

In general, AWS Backup copies tags from the resources it protects to your _recovery
points_. For more information on how to copy tags during a restore, see [Copy tags during
a restore](restoring-a-backup.md#tag-on-restore "restoring-a-backup.md#tag-on-restore").

For example, when you back up an Amazon EC2 volume, AWS Backup copies its group and individual
resource tags to the resulting snapshot, subject to the following:

- For a list of resource-specific permissions that are required to save metadata tags
  on backups, see [Permissions required to
  assign tags to backups](access-control.md#backup-tags-required-permissions "access-control.md#backup-tags-required-permissions").
- Tags that are originally associated with a resource and tags that are assigned
  during backup are assigned to recovery points stored in a backup vault, up to a maximum
  of 50 (this is an AWS limitation). Tags that are assigned during backup have priority,
  and both sets of tags are copied in alphabetical order.
- DynamoDB does not support assigning tags to backups unless you first enable [Advanced DynamoDB backup](advanced-ddb-backup.md "advanced-ddb-backup.md").
- Amazon EBS volumes that are attached to Amazon EC2 instances are nested resources. Tags on the
  Amazon EBS volumes that are attached to Amazon EC2 instances are nested tags. If AWS Backup can't
  copy nested tags, the backup job fails.
- When an Amazon EC2 backup creates an image recovery point and a set of snapshots, AWS Backup
  copies tags to the resulting AMI. If AWS Backup can't copy the tags from the volumes associated
  with the Amazon EC2 instance to the resulting snapshots, the backup job fails.
  If you copy your backup to another AWS Region, AWS Backup copies all tags of the original
  backup to the destination AWS Region.
