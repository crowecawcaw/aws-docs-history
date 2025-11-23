# Backup tiering

## Overview

AWS Backup offers a lower-cost warm storage tier for Amazon S3 backups that reduces long-term
storage costs by up to 30% while maintaining enterprise-grade protection and recovery capabilities.
The low-cost tier provides the same performance and features as the warm storage tier. You can
configure tiering to move S3 backup data to cost-optimized storage based on the age of objects
within your backup vaults.

AWS Backup tiering provides the ability to optimize storage costs for S3 backup data that is
retained for extended periods due to regulatory compliance, disaster readiness, and ransomware
protection strategies. You can configure tiering for all S3 backups for all vaults in an account,
or create targeted configurations for specific vaults and protected resources.

First, create a tiering configuration that specifies which S3 resources should be tiered and
after how many days (minimum 60 days). Tiering configurations can be automated to apply to all
backups or targeted to specific resources. When backup data reaches the specified age
threshold, it transitions to the lower-cost storage tier while maintaining identical restore
capabilities.

This document outlines the steps to create tiering configurations, manage tiered backup
data, monitor cost savings, and troubleshoot any issues with the tiering function in AWS Backup.

###### Important

Cost considerations for backup tiering:

- Backup tiering has three cost components: warm storage tier, low-cost warm
  storage tier, and transition costs. When backup data transitions to the lower-cost tier,
  you'll incur a one-time per-object transition fee based on the number of objects eligible
  for tiering.
- For large datasets with many objects, transition costs may be significant
  initially but are typically offset by ongoing storage savings for data retained beyond the
  minimum 60-day threshold.

## Tiering Configurations

S3 backup tiering involves creating a tiering configuration that specifies which resources
should be tiered and the number of days before transitioning (minimum 60 days) to the lower-cost
tier. To enable cost optimization, backup data must be covered by a tiering configuration.

Tiering configuration creation can be set up to apply broadly across backups of all S3
resources in your account, or targeted to specific vaults and resources. You can create multiple
configurations to handle different data retention and cost optimization requirements.

Tiering configurations apply to both existing backup data in vaults and new backups
created after the configuration is established.

S3 backup tiering configurations specify:

- **Resource scope:** All resources across all vaults, all
  resources in a specific vault, or selected individual resources. A tiering configuration
  that applies to all vaults and all resources is considered the default configuration.
- **Transition timing:** Minimum 60 days before data moves to
  the lower-cost tier
- **Vault assignment:** Which backup vaults the configuration
  applies to (for all vaults or specific vault name)
- **Resource selection:** Up to 5 different resource selection
  rules per configuration

Configuration constraints:

- **One configuration per vault:** Each vault can only have
  one tiering configuration apart from the default configuration
- **Maximum 5 resource selections:** Vault specific configuration
  supports up to 5 different resource group and corresponding tiering settings
- **Maximum 100 resources:** Up to 100 specific resources across
  all resource groups can be selected per configuration
- **Vault priority:** If both "all vaults" and specific vault
  configurations exist, the specific vault configuration takes priority

## Creating tiering configurations

**Creating tiering configurations**

Console

###### To create an all vaults tiering configuration (default)

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, choose **S3 backup tiering**.
3. Choose **Create configuration**.
4. For configuration name, enter a unique descriptive name.
5. Choose **All S3 resources in all vaults**.
6. For tiering down settings in days, enter the number of days (minimum 60)
   before data transitions to the lower-cost tier.
7. (Optional) Add tags.
8. Choose **Create configuration**.

###### To create a specific vault tiering configuration

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, choose **S3 backup tiering**.
3. Choose **Create configuration**.
4. For configuration name, enter a unique descriptive name.
5. Choose **S3 resources in a specific vault**.
6. For vault selection, select a specific backup vault from the dropdown.
7. For resource selection, choose either:
   1. **All S3 resources in this vault** to apply to all S3 resources in the vault
   2. **Specific S3 resources in this vault** to select individual S3 buckets

8. If selecting specific resources:
   1. Choose individual S3 resources (up to 100 total across resource groups in a configuration)
   2. Set tiering down settings in days for each resource group
   3. Choose **Add tiering setting** to create additional rules (up to 5 total)

9. (Optional) Add tags.
10. Choose **Create configuration**.

AWS CLI
To create an all vaults tiering configuration (default) using the AWS CLI

```
aws backup create-tiering-configuration \
--tiering-configuration '{
  "TieringConfigurationName":`"MyTieringConfig"`,
  "BackupVaultName":"*",
  "ResourceSelection":[{
    "Resources":["*"],
    "TieringDownSettingsInDays":60,
    "ResourceType":"S3"
  }]
}'
```

## Managing tiering configurations

**Viewing tiering configurations**

You can view existing tiering configurations through the AWS Backup console, AWS CLI, or REST API.

Console

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, choose **S3 backup tiering**.
3. View the list of configurations with their scope, transition settings, and status.

AWS CLI
To list all tiering configurations using the AWS CLI

```
aws backup list-tiering-configurations --max-results 50
```

To get specific tiering configuration details

```
aws backup get-tiering-configuration --tiering-configuration-name `"MyTieringConfig"`
```

**Modifying tiering configurations**

You can update existing tiering configurations to change transition timing, resource selection, or vault assignments.

Console

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, choose **S3 backup tiering**.
3. Select the configuration to modify.
4. Choose Edit.
5. Update the desired settings.
6. For Tiering down settings in days, enter the number of days (minimum 60)
   before data transitions to the lower-cost tier.
7. Choose Save changes.

AWS CLI
To update a tiering configuration using the AWS CLI

```
aws backup update-tiering-configuration \
--tiering-configuration-name `"MyTieringConfig"` \
--tiering-configuration '{
  "BackupVaultName":`"*"`,
  "ResourceSelection":[{
    "Resources":[`"*"`],
    "TieringDownSettingsInDays":`60`,
    "ResourceType":"S3"
  }]
}'
```

**Deleting tiering configurations**

You can delete tiering configurations when they are no longer needed.

Console

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, choose **S3 backup tiering**.
3. Select the configuration to delete.
4. Choose Delete.
5. Enter the tiering configuration name to confirm deletion.
6. Choose Delete tiering configuration.

AWS CLI
To delete a tiering configuration using the AWS CLI

```
aws backup delete-tiering-configuration \
--tiering-configuration-name `"MyTieringConfig"`
```

Note: Deleting a tiering configuration keeps existing data in the lower-cost
tier but prevents new data from tiering down.

## How S3 backup tiering configurations apply

AWS Backup evaluates objects within backups for tiering eligibility based on their age. The service
checks object age on a daily basis and transitions eligible objects to the lower-cost tier according
to your configuration settings. Tiering evaluation occurs automatically in the background. When objects
within a backup reach the specified age threshold (minimum 60 days), they become eligible for transition
during the next evaluation cycle.

Both objects in existing backups and newly created backup objects are subject to tiering configurations.
If you have multiple configurations that could apply to the same backup objects, vault-specific settings take
precedence over the configurations that applies to all vaults. The tiering process is irreversible - once
objects move to the lower-cost tier, they remain there until the backup is deleted according to your
retention policies.

## Cost structure and monitoring

**Pricing model**

S3 backup tiering uses a cost-optimized pricing structure:

- **Storage cost:** Lower /GB-month cost compared to standard warm tier
- **Transition fee:** One-time per-object fee when moving to lower-cost tier
- **Restore cost:** /GB charge when restoring data same as the warm tier restore
- **No retrieval fees:** There are no additional retrieval charges

**Cost monitoring**

Monitor your tiering cost savings through:

- **AWS Cost Explorer:** Separate usage types for each storage tier
- **AWS Cost and Usage Reports:** Detailed breakdown with cost allocation tags
- **AWS Backup console:** Configuration information

**Example cost savings**

For a 500TB S3 bucket with 1 billion objects where 60% are eligible for tiering:

- **Before tiering:** $25,600/month
- **After tiering:** $21,000/month
- **Monthly savings:** $4,600/month (18% reduction)
- **One-time transition fee:** $6,000

## Configuration Examples

**Example 1: Account-wide tiering**

Apply tiering to all S3 resources across all backup vaults:

```
{
  "TieringConfigurationName":"MyTieringConfig",
  "BackupVaultName":"*",
  "ResourceSelection":[
    {
      "Resources":["*"],
      "TieringDownSettingsInDays":60,
      "ResourceType":"S3"
    }
  ]
}
```

**Example 2:**

Tier all resources in a MyBackupVault4 vault:

```
{
  "TieringConfigurationName":"MyTieringConfig",
  "BackupVaultName":"MyBackupVault4",
  "ResourceSelection":[
    {
      "Resources":["*"],
      "TieringDownSettingsInDays":60,
      "ResourceType":"S3"
    }
  ]
}
```

**Example 3:**

Tier specific buckets with different rules:

```
{
  "TieringConfigurationName":"MyTieringConfig",
  "BackupVaultName":"MyBackupVault",
  "ResourceSelection":[
    {
      "Resources": ["arn:aws:s3:::mybucket1", "arn:aws:s3:::mybucket2"],
      "TieringDownSettingsInDays": 60,
      "ResourceType": "S3"
    },
    {
      "Resources": ["arn:aws:s3:::mybucket3"],
      "TieringDownSettingsInDays": 120,
      "ResourceType": "S3"
    }
  ]
}
```

**Example 4:**

Set the rule to not tier a bucket (set tiering to 36500):

```
{
  "TieringConfigurationName":"MyTieringConfig",
  "BackupVaultName":"*",
  "ResourceSelection":[
    {
      "Resources":["arn:aws:s3:::mybucket7", "arn:aws:s3:::mybucket8"],
      "TieringDownSettingsInDays":36500,
      "ResourceType":"S3"
    }
  ]
}
```

## Supported features and limitations

**Supported features**

- **Backup types:** Both continuous and periodic backups
- **Vault types:** Standard backup vaults and logically air-gapped vaults
- **Vault lock:** Full compatibility with locked backup vaults
- **Cross-region/account:** Copying tiered data (copies land in standard tier at destination)
- **Restore capabilities:** Point-in-time recovery and item-level restores
- **Search and indexing:** Full compatibility with backup search functionality
- **Compliance:** Maintains all compliance and audit capabilities

**Limitations**

- **Minimum transition time:** 60 days before data can be moved to lower-cost tier
- **Resource limit:** Up to 100 specific resources per configuration
- **Configuration limit:** Up to 5 different resource selection rules per configuration
- **One configuration per vault:** Each vault can only have one vault specific tiering configuration, apart from the default
- **One-way transition:** Data moved to lower-cost tier remains there until deletion

## Troubleshooting

**Common issues**

Configuration not applying to existing backups

- Verify that the configuration is properly assigned to the correct vaults
- Check that resources are correctly selected in targeted configurations
- Ensure backup data meets the minimum age requirement (60 days)

`AlreadyExistsException` when creating configuration

- Ensure the tiering configuration name is unique within your account
- Check if the target vault already has an active tiering configuration

`LimitExceededException` errors

- Verify you have not exceeded the maximum of 5 resource selection group per configuration
- Check that you have not selected more than 100 specific resources

Higher than expected transition costs

- Review the number of objects being transitioned
- Consider the transition fee impact for frequently changing data
- Evaluate whether the minimum threshold settings is appropriate for your use case
