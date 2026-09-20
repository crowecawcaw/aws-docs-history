

# Turn off backups
<a name="stop-backups"></a>

You can turn off backups for your resources in accounts that are enrolled in AWS Control Tower, either during landing zone setup, or when you update your landing zone.

Two main steps are required to turn off backups: first, turn off the AWS Backup baseline on each OU that has backups enabled, *then*, turn off backups for your landing zone.

## First step: Turn off backups on OUs
<a name="turn-off-ou-backup"></a>

If AWS Backup is enabled, you must disable the AWS Backup baseline from all OUs before you can turn off AWS Backup for your landing zone.

If you have nested OUs, disable the AWS Backup baseline on the child OUs before the parent OU. While the AWS Backup baseline is still enabled on a child OU, AWS Control Tower cannot disable it on the parent OU.

You can disable the AWS Backup baseline on an OU by using the AWS Control Tower APIs or the AWS Control Tower console.

**To disable the AWS Backup baseline (API)**

First, find the ARN of the AWS Backup baseline. Call the `ListBaselines` API and query for the baseline whose `name` is `BackupBaseline` to get its ARN.

```
aws controltower list-baselines --query 'baselines[?name==`BackupBaseline`]'
```

Then, using that ARN, identify which OUs have the AWS Backup baseline enabled. Call the `ListEnabledBaselines` API, filtering on the `BackupBaseline` baseline identifier, to find each enabled baseline and its `enabledBaselineIdentifier` ARN to disable.

```
aws controltower list-enabled-baselines --filter baselineIdentifiers={{BackupBaseline-ARN}}
```

To disable the AWS Backup baseline on an OU, you can call the `DisableBaseline` API.

*Example command:*

```
aws controltower disable-baseline --enabled-baseline-identifier {{Enabled-baseline-ARN}}
```

**To disable the AWS Backup baseline (console)**

1. Sign in to the AWS Control Tower console and navigate to the **Organization** page.

1. Choose the OU whose **AWS Backup baseline status** is **Enabled** to open the OU detail page.

1. In the **Integrations on this OU - optional** section, under **AWS Backup**, choose **Edit**.

1. In the dialog that appears, select **Disable**, and then choose **Confirm**.

When you disable the the AWS Backup baseline, AWS Control Tower cleans up the following resources:
+ All stacksets related to AWS Backup
+ All controls related to AWS Backup 

**Note**  
The local vault is retained even though the stacksets are deleted, because the retention policy on the local vault is set to `Retain`. It preserves your data.

## Next step: Turn off AWS Backup for your landing zone
<a name="turn-off-lz-backup"></a>

After the prerequisite is met by turning off backups to your OUs, to turn off backups from the AWS Control Tower console, navigate to the **Landing zone settings** page. Choose **Disable backup**.

When you turn off AWS Backup, AWS Control Tower changes the following resources:
+ Removes all stacksets related to AWS Backup
+ Deactivates all controls related to AWS Backup in the Security OU
+ De-registers the **Delegated admin** account for AWS Backup administration
+ Removes AWS Control Tower governance (for CloudTrail, AWS Config, and so forth) from the AWS Backup Administrator and Central Backup accounts
+ AWS Control Tower retains the AWS Backup vaults and Amazon S3 bucket resources containing your data

After you disable backups, no new backups are created, but existing backups are not removed.