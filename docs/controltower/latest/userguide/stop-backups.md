# Turn off backups

You can turn off backups for your resources in accounts that are enrolled in AWS Control Tower,
either during landing zone setup, or when you update your landing zone.

Two main steps are required to turn off backups: first, turn off the AWS Backup baseline on
each OU that has backups enabled, _then_, turn off backups for your
landing zone.

## First step: Turn off backups on OUs

If AWS Backup is enabled, you must disable the AWS Backup baseline from all OUs before you
can turn off AWS Backup for your landing zone.

To disable the AWS Backup baseline on an OU, you can call the
`DisableBaseline` API. The nested OUs inherit this status, so that
the AWS Backup baseline baseline is disabled for them also.

_Example command:_

```
aws controltower disable-baseline --enabled-baseline-identifier `Enabled-baseline-ARN`
```

When you disable the the AWS Backup baseline, AWS Control Tower cleans up the following
resources:

- All stacksets related to AWS Backup
- All controls related to AWS Backup

###### Note

The local vault is retained even though the stacksets are deleted, because the
retention policy on the local vault is set to `Retain`. It preserves
your data.

## Next step: Turn off AWS Backup for your landing zone

After the prerequisite is met by turning off backups to your OUs, to turn off
backups from the AWS Control Tower console, navigate to the **Landing zone
settings** page. Choose **Disable backup**.

When you turn off AWS Backup, AWS Control Tower changes the following resources:

- Removes all stacksets related to AWS Backup
- Deactivates all controls related to AWS Backup in the Security OU
- De-registers the **Delegated admin** account for AWS Backup
  administration
- Removes AWS Control Tower governance (for CloudTrail, AWS Config, and so forth) from the AWS Backup
  Administrator and Central Backup accounts
- AWS Control Tower retains the AWS Backup vaults and Amazon S3 bucket resources
  containing your data

After you disable backups, no new backups are created, but existing backups are
not removed.
