

# Amazon DynamoDB incremental backups

With incremental backups, AWS Backup captures only the data in your DynamoDB table that changed since the previous backup, rather than taking a full snapshot every time. You can maintain frequent backup schedules to meet strict recovery point objectives (RPOs) without the cost of storing a full copy of your table on every backup. Your backup schedules, retention periods, and copy settings are unchanged — only the storage behavior changes.

Incremental backups are an extension of AWS Backup advanced features for DynamoDB. You need to enable advanced features before you can enable incremental backups.

**Availability** Amazon DynamoDB incremental backups are available in all commercial AWS Regions where AWS Backup supports DynamoDB, and in the China Regions.

**Topics**
+ [Benefits of incremental backups](#incremental-ddb-backups-benefits)
+ [How incremental backups work](#incremental-ddb-backups-how-it-works)
+ [Supported RPO range](#incremental-ddb-backups-rpo-range)
+ [Considerations](#incremental-ddb-backups-considerations)
+ [Enabling Amazon DynamoDB incremental backups using the console](#incremental-ddb-backups-enable-console)
+ [Enabling Amazon DynamoDB incremental backups programmatically](#incremental-ddb-backups-enable-cli)
+ [Opting out of incremental backups](#incremental-ddb-backups-opt-out)
+ [Understanding incremental backups and costs](#incremental-ddb-backups-costs)
+ [Copying incremental backups](#incremental-ddb-backups-copying)
+ [Restoring incremental backups](#incremental-ddb-backups-restoring)
+ [Incremental backups and Amazon DynamoDB point-in-time recovery (PITR)](#incremental-ddb-backups-pitr)

## Benefits of incremental backups
<a name="incremental-ddb-backups-benefits"></a>
+ **Lower backup storage** — after the first backup, each backup stores only changed data, which can substantially reduce the storage you consume for frequent schedules.
+ **Frequent, granular RPOs** — protect tables as often as every hour without paying to store a full table copy each time.
+ **No reconfiguration** — your existing backup plans, frequencies, retention periods, and copy settings continue to apply.
+ **Works across AWS Backup** — incremental backups support cross-Region and cross-account copy, logically air-gapped (LAG) vaults, cold storage transitions, restore testing, and AWS Backup Audit Manager.

## How incremental backups work
<a name="incremental-ddb-backups-how-it-works"></a>

When you enable incremental backups for a table, AWS Backup takes an initial full backup. Every backup after that captures only the changes since the previous backup, with periodic rebasing in between.

To keep restores fast and to limit how long shared data must be retained, AWS Backup periodically takes a new full backup of the table. This is called periodic rebasing. It resets the incremental chain so that any single restore depends on a shorter chain of backups. AWS Backup manages this automatically and it is not customer configurable. At this time, AWS Backup conducts a periodic rebase every 15 days across all incremental backup schedules.

Because every backup is self-describing and references a logical full backup, you can still perform a complete restore from a single recovery point even if earlier backups in the chain — including the initial full backup — have been deleted or have expired.

For instructions on enabling incremental backups, see [Enabling Amazon DynamoDB incremental backups using the console](#incremental-ddb-backups-enable-console).

## Supported RPO range
<a name="incremental-ddb-backups-rpo-range"></a>

Incremental backups support RPOs from one hour to seven days. If a backup rule has an RPO greater than seven days, backups for that rule remain full backups. You can bring such a schedule into incremental coverage by lowering its RPO to seven days or less. In most cases, this provides similar storage savings, because incremental change over a longer period is typically the sum of the changes over shorter periods.

## Considerations
<a name="incremental-ddb-backups-considerations"></a>
+ **Enablement order** You need to enable advanced features before you can enable the Incremental Backup setting.
+ **Manage through AWS Backup only** You manage incremental backups through the AWS Backup console, CLI, or API. You can still use the DynamoDB console or APIs to create on-demand full backups and to configure native DynamoDB point-in-time recovery (PITR).
+ **Restores create a new table** Incremental backups support non-destructive restores only. You restore an incremental backup (or a copy of one) into a new DynamoDB table, not over the original table. You choose the encryption key at restore time.
+ **Existing recovery points are unchanged** Recovery points created before you enable incremental remain full backups for the rest of their lifecycle. New recovery points are incremental.
+ **RPOs over seven days stay full** See [Supported RPO range](#incremental-ddb-backups-rpo-range).
+ **No separate PITR requirement** You do not need to enable DynamoDB PITR to use incremental backups.

## Enabling Amazon DynamoDB incremental backups using the console
<a name="incremental-ddb-backups-enable-console"></a>

**To enable Amazon DynamoDB incremental backups from the AWS Backup console:**

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup).

1. In the left navigation menu, choose **Settings**.

1. Under **Supported services**, verify that **Amazon DynamoDB** is **Enabled**. If it is not, choose **Opt-in** and enable DynamoDB.

1. Under **Advanced features for DynamoDB backups**, verify that advanced features are **Enabled**. If not, choose **Enable**, then **Enable features**.

1. In the **Advanced features for DynamoDB backups** section, select **Incremental Backups**.

After you enable incremental backups, the next backup for each assigned table is a full backup, and subsequent backups are incremental, with periodic rebasing in between.

## Enabling Amazon DynamoDB incremental backups programmatically
<a name="incremental-ddb-backups-enable-cli"></a>

You can also enable incremental backups using the AWS Command Line Interface. Advanced features for DynamoDB backups must already be enabled before these settings take effect. Incremental backups require all three of the following settings to be true for DynamoDB: `ResourceTypeManagementPreference`, `ResourceTypeOptInPreference`, and `ResourceTypeOptInIncremental`.

The `UpdateRegionSettings` operation accepts a new `ResourceTypeOptInIncremental` map, which enables or disables incremental backups for a resource type. Disabling it returns the resource type to full backups. Only the DynamoDB resource type is currently supported, and it requires `"DynamoDB":true` under both `ResourceTypeManagementPreference` and `ResourceTypeOptInPreference`.

The following AWS Command Line Interface command checks your current settings:

```sh
aws backup describe-region-settings
```

If `"DynamoDB":true` appears under all three of `ResourceTypeManagementPreference`, `ResourceTypeOptInPreference`, and `ResourceTypeOptInIncremental`, incremental backups are already enabled. If you see at least one `"DynamoDB":false`, continue to the next step.

The following example output shows DynamoDB opt-in for incremental backups set to false:

```JSON
{
    "ResourceTypeManagementPreference": {
        "DynamoDB": false,
        "EFS": true
    },
    "ResourceTypeOptInPreference": {
        "Aurora": true,
        "DocumentDB": false,
        "DynamoDB": false,
        "EBS": true,
        "EC2": true,
        "EFS": true,
        "FSx": true,
        "Neptune": false,
        "RDS": true,
        "Storage Gateway": true
    },
    "ResourceTypeOptInIncremental": {
        "DynamoDB": false
    }
}
```

Use `UpdateRegionSettings` to set all three preferences to `"DynamoDB":true`:

```sh
aws backup update-region-settings \
    --resource-type-opt-in-preference DynamoDB=true \
    --resource-type-management-preference DynamoDB=true \
    --resource-type-opt-in-incremental DynamoDB=true
```

To confirm the change, run `describe-region-settings` again. DynamoDB now appears as `true` under all three preferences:

```JSON
{
    "ResourceTypeManagementPreference": {
        "DynamoDB": true
    },
    "ResourceTypeOptInPreference": {
        "DynamoDB": true
    },
    "ResourceTypeOptInIncremental": {
        "DynamoDB": true
    }
}
```

For more information, see [UpdateRegionSettings](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_UpdateRegionSettings.html) in the *AWS Backup API Reference*.

## Opting out of incremental backups
<a name="incremental-ddb-backups-opt-out"></a>

You might opt out of incremental backups to return to full backups for workloads that change extensively between backups.

You can return to full backups at any time by disabling **Incremental Backup** in the console in AWS Backup settings, or by setting `--resource-type-opt-in-incremental DynamoDB=false`. After you opt out, new backups are full backups. If you later opt back in, AWS Backup starts a new incremental chain with a fresh initial full backup.

## Understanding incremental backups and costs
<a name="incremental-ddb-backups-costs"></a>

Each incremental backup references a chain of earlier backups going back to the most recent periodic full backup. Because backups in a chain share common data blocks:
+ You are not charged for backups that have expired or that you have deleted. However, data blocks referenced by a deleted or expired backup might still be referenced by other active backups in the chain; the cost of those shared blocks transitions to the next active backup in the chain.
+ Incremental backups support cold storage transitions. You incur cold storage charges for incremental backups immediately after they transition to cold tier.

## Copying incremental backups
<a name="incremental-ddb-backups-copying"></a>

You can copy incremental backups across AWS Regions and across accounts, and into LAG vaults. Copied backups remain incremental and are encrypted with the destination vault's encryption key. AWS Backup copies all data references the destination needs to perform an independent full restore, so each destination vault can restore on its own.

## Restoring incremental backups
<a name="incremental-ddb-backups-restoring"></a>

You restore an incremental backup the same way you restore a DynamoDB full backup using AWS Backup:
+ The restore target is always a new DynamoDB table (non-destructive restore).
+ You can choose the encryption key for the restored table. When you restore into a different Region than the original table, you must specify an encryption key.

For instructions on restoring incremental backups, see [Restore a Amazon DynamoDB table](restoring-dynamodb.md).

## Incremental backups and Amazon DynamoDB point-in-time recovery (PITR)
<a name="incremental-ddb-backups-pitr"></a>

Incremental backups and native DynamoDB PITR are complementary, and you can use them together, with separate charges.

The following table compares when to use incremental backups and DynamoDB PITR.


| Use case | Incremental | DynamoDB PITR | 
| --- | --- | --- | 
| Same-Region, same-account recovery with highly granular (sub-hour) RPO, typically for application recovery | No | Yes | 
| Policy-based backup management such as vaulting, immutability, and centralized compliance monitoring | Yes | No | 
| RPO lower than one hour, without compliance-driven cross-Region/cross-account needs | No | Yes | 
| RPO of one hour or more with compliance and DR needs — cross-account/cross-Region copy, long-term retention, ransomware protection through LAG vaults — under centralized AWS Backup management | Yes | No | 

You do not need to turn on DynamoDB PITR to use incremental backups. If you use AWS Backup incrementally for compliance-driven use cases and do not need sub-hour recovery, you can disable native PITR for those tables to avoid paying for both.