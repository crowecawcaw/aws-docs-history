# Backup policy syntax and

examples

This page describes backup policy syntax and provides examples.

## Syntax for backup policies

A backup policy is a plaintext file that is structured according to the rules of
[JSON](http://json.org "http://json.org"). The syntax for backup policies follows
the syntax for all management policy types. For more information, see [Policy syntax and inheritance for management policy types](orgs_manage_policies_inheritance_mgmt.md "orgs_manage_policies_inheritance_mgmt.md"). This topic
focuses on applying that general syntax to the specific requirements of the backup
policy type.

For more information about AWS Backup plans, see [CreateBackupPlan](../../../aws-backup/latest/devguide/API_CreateBackupPlan.md "../../../aws-backup/latest/devguide/API_CreateBackupPlan.md")
in the _AWS Backup Developer Guide_.

## Considerations

**Policy syntax**

Duplicate key names will be rejected in JSON.

Policies must specify the AWS Regions and resources to be backed up.

Policies must specify the IAM role that AWS Backup assumes.

Using `@@assign` operator at the same level can overwrite existing
settings. For more information, see [A child
policy overrides settings in a parent policy](#backup-policy-example-5 "#backup-policy-example-5").

Inheritance operators control how inherited policies and account policies merge into
the account's effective policy. These operators include value-setting operators and
child control operators.

For more information, see [Inheritance
operators](policy-operators.md "policy-operators.md") and [Backup policy
examples](#backup-policy-examples "#backup-policy-examples").

**IAM roles**

The IAM role must exist when creating a backup plan for the first time.

The IAM role must have permission to access resources identified by tag
query.

The IAM role must have permission to perform the backup.

**Backup vaults**

Vaults must exist in each specified AWS Regions before a backup plan can run.

Vaults must exist for each AWS account that receives the effective policy. For more
information, see [Backup vault creation and
deletion](../../../aws-backup/latest/devguide/create-a-vault.md "../../../aws-backup/latest/devguide/create-a-vault.md") in the _AWS Backup Developer
Guide_.

We recommend that you use AWS CloudFormation stack sets and its integration with Organizations to
automatically create and configure backup vaults and IAM roles for each member account
in the organization. For more information, see [Create a stack set with self-managed permissions](../../../AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.md#create-stack-set-service-managed-permissions "../../../AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.md#create-stack-set-service-managed-permissions") in the _AWS CloudFormation User Guide_.

**Quotas**

For a list of quotas see, [AWS Backup quotas](../../../aws-backup/latest/devguide/aws-backup-limits.md#aws-backup-policies-quotas-table "../../../aws-backup/latest/devguide/aws-backup-limits.md#aws-backup-policies-quotas-table") in the _AWS Backup Developer
Guide_.

## Backup syntax: Overview

Backup policy syntax includes the following components:

```
{
    "plans": {
        "PlanName": {
            "rules": { ... },
            "regions": { ... },
            "selections": { ... },
            "advanced_backup_settings": { ... },
            "backup_plan_tags": { ... },
            "scan_settings": { ... }
        }
    }
}
```

| Backup policy elements                                                            | Element                                                                                                                                                                                                                                                 | Description | Required |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | -------- |
| [rules](#backup-policy-rules "#backup-policy-rules")                              | List of backup rules. Each rule defines when backups start and the<br>execution window for the resources specified in the `regions`<br>and `selections` elements.                                                                                       | Yes         |
| [regions](#backup-plan-regions "#backup-plan-regions")                            | List of AWS Regions where a backup policy can protect<br>resources.                                                                                                                                                                                     | Yes         |
| [selections](#backup-plan-selections "#backup-plan-selections")                   | One or more resource types within the specified `regions`<br>that the backup `rules` protect.                                                                                                                                                           | Yes         |
| [advanced_backup_settings](#advanced-backup-settings "#advanced-backup-settings") | Configuration options for specific backup scenarios.<br>Currently, the only advanced backup setting that is supported is<br>enabling Microsoft Volume Shadow Copy Service (VSS) backups for<br>Windows or SQL Server running on an Amazon EC2 instance. | No          |
| [backup_plan_tags](#backup-plan-tags "#backup-plan-tags")                         | Tags you want to associate with a backup plan. Each tag is a<br>label consisting of a user-defined key and value.<br>Tags can help you manage, identify, organize, search for, and<br>filter your backup plans.                                         | No          |
| [scan_settings](#scan-settings "#scan-settings")                                  | Configuration options for scan settings. Currently the only scan settings that<br>is support is enable Amazon GuardDuty Malware Protection for AWS Backup.                                                                                              | No          |

## Backup syntax: rules

The `rules` policy key specifies the scheduled backup tasks that AWS Backup
performs on the selected resources.

| Backup rule elements                           | Element                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Description | Required |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | -------- |
| `schedule_expression`                          | Cron expression in UTC that specifies when AWS Backup initiates a<br>backup job.<br>For information about cron expression, see [Using cron and rate expressions to schedule rules](../../../eventbridge/latest/userguide/eb-scheduled-rule-pattern.md "../../../eventbridge/latest/userguide/eb-scheduled-rule-pattern.md") in<br>the _Amazon EventBridge User Guide_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Yes         |
| `target_backup_vault_name`                     | Backup vault where backups are stored.<br>Backup vaults are identified by names that are unique to the<br>account used to create them and the AWS Region where they are<br>created.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Yes         |
| `target_logically_air_gapped_backup_vault_arn` | Logically air-gapped vault ARN where backups are stored.<br>If provided, supported fully managed resources back up directly to logically air-gapped vault,<br>while other supported resources create a temporary (billable) snapshot in backup vault,<br>then copy it to logically air-gapped vault. Unsupported resources only back up to the specified<br>backup vault.<br>The ARN must use the special placeholders `$region` and `$account`.<br>For example, for a vault named `AirGappedVault` the correct value is<br>`arn:aws:backup:$region:$account:backup-vault:AirGappedVault`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | No          |
| `start_backup_window_minutes`                  | Number of minutes to wait before canceling a backup job will be<br>canceled if it doesn't start successfully.<br>If this value is included, it must be at least 60 minutes to avoid<br>errors.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | No          |
| `complete_backup_window_minutes`               | Nnumber of minutes after a backup job is successfully started before<br>it must be completed or it will be canceled by AWS Backup.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | No          |
| `enable_continuous_backup`                     | Specifies whether AWS Backup creates continuous backups.<br>`True` causes AWS Backup to create continuous backups<br>capable of point-in-time restore (PITR). `False` (or not<br>specified) causes AWS Backup to create snapshot backups.<br>For more information about continuous backups, see [Point-in-time<br>recovery](../../../aws-backup/latest/devguide/point-in-time-recovery.md "../../../aws-backup/latest/devguide/point-in-time-recovery.md") in the _AWS Backup Developer Guide_.<br>\*_Note:_<br>• PITR-enabled backups have<br>35-day maximum retention.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | No          |
| `lifecycle`                                    | Specifies when AWS Backup transitions a backup to cold storage and<br>when it expires.<br>Resource types that can transition to cold storage are listed in<br>the Feature availability by resource table [Feature availability by resources](../../../aws-backup/latest/devguide/backup-feature-availability.md#features-by-resource "../../../aws-backup/latest/devguide/backup-feature-availability.md#features-by-resource") in the _AWS Backup Developer Guide_.<br>Each lifecycle contains the following elements:<br>• `move_to_cold_storage_after_days`: Number of<br>days after the backup occurs before AWS Backup moves the recovery<br>point to cold storage.<br>• `delete_after_days`: Number of days after a<br>backup occurs before AWS Backup deletes the recovery<br>point.<br>• `opt_in_to_archive_for_supported_resources`: If<br>this value is assigned as `true`, a backup plan<br>transitions supported resources to archive (cold) storage<br>tier in accordance with your lifecycle settings.<br>**Note**: Backups transitioned to<br>cold storage must be stored in cold storage for a minimum of 90<br>days.<br>This means that the `delete_after_days` must be 90 days<br>greater than `move_to_cold_storage_after_days`. | No          |
| `copy_actions`                                 | Specifies whether AWS Backup copies a backup to one or more<br>additional locations.<br>Each copy action contains the following elements:<br>• `target_backup_vault_arn`: Vault where AWS Backup<br>stores an additional copy of the backup.<br>+ Use `$account` for same-account<br>copies<br>+ Use actual account ID for cross-account<br>copies<br>• `lifecycle`: Specifies when AWS Backup transitions a<br>backup to cold storage and when it expires.<br>Each lifecycle contains the following elements:<br>+ `move_to_cold_storage_after_days`:<br>Number of days after the backup occurs before AWS Backup<br>moves the recovery point to cold storage.<br>+ `delete_after_days`: Number of days<br>after s backup occurs before AWS Backup deletes the<br>recovery point.<br>**Note**: Backups transitioned to<br>cold storage must be stored in cold storage for a minimum of 90<br>days.<br>This means that the `delete_after_days` must be 90 days<br>greater than `move_to_cold_storage_after_days`.                                                                                                                                                                                                                                   | No          |
| `recovery_point_tags`                          | Tags that you want to assigned to resources that are restored<br>from backup.<br>Each tag contains the following elements:<br>• `tag_key`: Tag name (case-sensitive)<br>• `tag_value`: Tag value (case-sensitive)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | No          |
| `index_actions`                                | Specifies whether AWS Backup creates a backup index of your Amazon EBS<br>snapshots and/or Amazon S3 backups. Backup indexes are created in order to<br>search the metadata of your backups. For more information about<br>backup index creation and backup search, see [Backup search](../../../aws-backup/latest/devguide/backup-search.md#backup-search-overview "../../../aws-backup/latest/devguide/backup-search.md#backup-search-overview").<br>\*_Note:_<br>• Additional [IAM role permissions](../../../aws-backup/latest/devguide/backup-search.md#backup-search-access "../../../aws-backup/latest/devguide/backup-search.md#backup-search-access") are required for Amazon EBS snapshot<br>backup index creation.<br>Each index action contains the following element:<br>`resource_types` where resource types supported for<br>indexing are Amazon EBS and Amazon S3. This parameter specifies which resource<br>type will be opted into indexing.                                                                                                                                                                                                                                                                                    | No          |
| `scan_actions`                                 | Specifies whether a scanning action is enabled for a given rule.<br>You must specify a `Malwarescanner` and `ScanMode`.<br>You must use `scan_settings` in the backup policy elements in<br>conjunction with `scan_actions` in order for scanning jobs to start successfully.<br>Please also ensure you have the right [IAM role permissions](../../../aws-backup/latest/devguide/malware-protection.md#malware-access "../../../aws-backup/latest/devguide/malware-protection.md#malware-access").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | No          |

## Backup syntax: regions

The `regions` policy key specifies which AWS Regions that AWS Backup looks in
to find the resources that match the conditions in the `selections`
key.

| Backup regions elements | Element                                                                        | Description | Required |
| ----------------------- | ------------------------------------------------------------------------------ | ----------- | -------- |
| `regions`               | Specifies the AWS Region codes. For example:<br>`["us-east-1", "eu-north-1"]`. | Yes         |

## Backup syntax: selections

The `selections` policy key specifies the resources that are backed up by
the rules in a backup policy.

There are two mutually exclusive elements: `tags` and
`resources`. An effective policy **must**
`have` either tags or `resources` in the selection to be
valid.

If you want a selection with both tag conditions and resource conditions, use the
`resources` keys.

| Backup selection elements: Tags | Element                                                                                                                                                                                                                                                                                                                                        | Description | Required |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | -------- |
| `iam_role_arn`                  | IAM role that AWS Backup assumes to query, discover, and backup<br>resources across the specified Regions. The role must have<br>sufficient permissions to query resources based on tag conditions<br>and perform backup operations on the matched resources.                                                                                  | Yes         |
| `tag_key`                       | Tag key name to search for.                                                                                                                                                                                                                                                                                                                    | Yes         |
| `tag_value`                     | Value that must be associated with the matching tag_key. AWS Backup<br>includes the resource only if both tag_key and tag_value match (case<br>sensitive).                                                                                                                                                                                     | Yes         |
| `conditions`                    | Tag keys and values you want to include or exclude<br>Use string_equals or<br>string_not_equals to include or exclude tags of<br>an exact match.<br>Use string_like and<br>string_not_like to include or exclude tags that<br>contains or do not contain specific characters<br>\*_Note:_<br>• Limited to 30 conditions<br>for each selection. | No          |

| Backup selection elements: Resources | Element                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Description | Required |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | -------- |
| `iam_role_arn`                       | IAM role that AWS Backup assumes to query, discover, and backup<br>resources across the specified Regions. The role must have<br>sufficient permissions to query resources based on tag conditions<br>and perform backup operations on the matched resources.<br>\*_Note:_<br>• In AWS GovCloud (US) Regions,<br>you must add the name of the partition to the ARN.<br>For example, "`arn:aws:ec2:*:*:volume/*`" must be<br>"`arn:aws-us-gov:ec2:*:*:volume/*`". | Yes         |
| `resource_types`                     | Resource types to include in a backup plan.                                                                                                                                                                                                                                                                                                                                                                                                                      | Yes         |
| `not_resource_types`                 | Resource types to exclude from a backup plan.                                                                                                                                                                                                                                                                                                                                                                                                                    | No          |
| `conditions`                         | Tag keys and values you want to include or exclude<br>Use string_equals or<br>string_not_equals to include or exclude tags of<br>an exact match.<br>Use string_like and<br>string_not_like to include or exclude tags that<br>contains or do not contain specific characters<br>\*_Note:_<br>• Limited to 30 conditions<br>for each selection.                                                                                                                   | No          |

**Supported resource types**

Organizations supports the following resource types for the `resource_types` and
`not_resource_types` elements:

- AWS Backup gateway virtual machines: `"arn:aws:backup-gateway:*:*:vm/*"`
- AWS CloudFormation stacks: `"arn:aws:cloudformation:*:*:stack/*"`
- Amazon DynamoDB tables: `"arn:aws:dynamodb:*:*:table/*"`
- Amazon EC2 instances: `"arn:aws:ec2:*:*:instance/*"`
- Amazon EBS volumes: `"arn:aws:ec2:*:*:volume/*"`
- Amazon EFS file systems: `"arn:aws:elasticfilesystem:*:*:file-system/*"`
- Amazon Aurora/Amazon DocumentDB/Amazon Neptune clusters:
  `"arn:aws:rds:*:*:cluster:*"`
- Amazon RDS databases: `"arn:aws:rds:*:*:db:*"`
- Amazon Redshift clusters: `"arn:aws:redshift:*:*:cluster:*"`
- Amazon S3: `"arn:aws:s3:::*"`
- AWS Systems Manager for SAP HANA databases: `"arn:aws:ssm-sap:*:*:HANA/*"`
- AWS Storage Gateway gateways: `"arn:aws:storagegateway:*:*:gateway/*"`
- Amazon Timestream databases: `"arn:aws:timestream:*:*:database/*"`
- Amazon FSx file systems: `"arn:aws:fsx:*:*:file-system/*"`
- Amazon FSx volumes: `"arn:aws:fsx:*:*:volume/*"`

**Code examples**

For more information, see [Specifying resources
with the tags block](#backup-policy-example-6 "#backup-policy-example-6") and [Specifying
resources with the resources block](#backup-policy-example-7 "#backup-policy-example-7").

## Backup syntax: advanced backup

settings

The `advanced_backup_settings` key specifies the configuration options for
specific backup scenarios. Each setting contains the following elements:

| Advanced backup settings elements | Element                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description | Required |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | -------- |
| `advanced_backup_settings`        | Specifies settings for specific backup scenarios. This key contains<br>one or more settings. Each setting is a JSON object string with the<br>following elements: Currently the only advanced backup setting<br>that is supported is enabling Microsoft Volume Shadow Copy Service<br>(VSS) backups for Windows or SQL Server running on an Amazon EC2<br>instance.<br>Each advanced backup setting the following elements:<br>• `Object key name`: String that specifies the<br>type of resource to which the following advanced settings<br>apply.<br>The key name must be the `"ec2"` resource<br>type<br>• `Object value`: Dtring that contains one or<br>more backup settings specific to the associated resource<br>type.<br>The value specifies that `"windows_vss"`<br>support is either `enabled` or<br>`disabled` for backups performed on the Amazon EC2<br>instances. | No          |

**Example:**

```

"advanced_backup_settings": {
    "ec2": {
        "windows_vss": {
            "@@assign": "enabled"
        }
    }
},
```

## Backup syntax: backup plan tags

The `backup_plan_tags` policy key specifies the tags that are attached to a
backup plan itself. This does not impact the tags specified for `rules` or
`selections`.

| Backup plan tag elements | Element                                                                                                                                                                                                                                                                       | Description | Required |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | -------- |
| `backup_plan_tags`       | Each tag is a label consisting of a user-defined key and value:<br>• `tag_key`: Tag key name to search for. The<br>value is case sensitive.<br>• `tag_value`: Value that is attached to the<br>backup plan and associated with the `tag_key`.<br>The value is case sensitive. | No          |

## Backup syntax: scan settings

The `scan_settings` policy key specifies the tags that are attached to a
backup plan itself. This does not impact the tags specified for `rules` or
`selections`.

| Backup plan tag elements | Element                                                                                                                                                                                                                                                                                                        | Description | Required |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | -------- |
| `scan_settings`          | Each tag is a label consisting of a user-defined key and value:<br>Configuration options for scan settings. Currently the only scan settings that is<br>support is enable Amazon GuardDuty Malware Protection for AWS Backup.<br>You must specify the `Malwarescanner`, `ResourceTypes`, and `ScannerRoleArn`. | No          |

## Backup policy examples

The example backup policies that follow are for information purposes only. In some of
the following examples, the JSON whitespace formatting might be compressed to save
space.

- [Example 1: Policy assigned to a parent
  node](#backup-policy-example-1 "#backup-policy-example-1")
- [Example 2: A parent policy is merged
  with a child policy](#backup-policy-example-2 "#backup-policy-example-2")
- [Example 3: A parent policy prevents
  any changes by a child policy](#backup-policy-example-3 "#backup-policy-example-3")
- [Example 4: A parent policy prevents
  changes to one backup plan by a child policy](#backup-policy-example-4 "#backup-policy-example-4")
- [Example 5: A child policy overrides
  settings in a parent policy](#backup-policy-example-5 "#backup-policy-example-5")
- [Example 6: Specifying resources with
  the tags block](#backup-policy-example-6 "#backup-policy-example-6")
- [Example 7: Specifying resources with
  the resources block](#backup-policy-example-7 "#backup-policy-example-7")

### Example 1: Policy assigned to a parent

node

The following example shows a backup policy that is assigned to one of the parent
nodes of an account.

**Parent policy** – This policy can be
attached to the organization's root, or to any OU that is a parent of all of the
intended accounts.

```
{
    "plans": {
        "PII_Backup_Plan": {
            "regions": {
                "@@assign": [
                    "ap-northeast-2",
                    "us-east-1",
                    "eu-north-1"
                ]
            },
            "rules": {
                "Hourly": {
                    "schedule_expression": {
                        "@@assign": "cron(0 5/1 ? * * *)"
                    },
                    "start_backup_window_minutes": {
                        "@@assign": "480"
                    },
                    "complete_backup_window_minutes": {
                        "@@assign": "10080"
                    },
                    "lifecycle": {
                        "move_to_cold_storage_after_days": {
                            "@@assign": "180"
                        },
                        "delete_after_days": {
                            "@@assign": "270"
                        },
                        "opt_in_to_archive_for_supported_resources": {
                            "@@assign": "false"
                        }
                    },
                    "target_backup_vault_name": {
                        "@@assign": "FortKnox"
                    },
                    "target_logically_air_gapped_backup_vault_arn": {
                        "@@assign": "arn:aws:backup:$region:$account:backup-vault:AirGappedVault"
                    },
                    "index_actions": {
                        "resource_types": {
                            "@@assign": [
                                "EBS",
                                "S3"
                            ]
                        }
                     },
                    "copy_actions": {
                        "arn:aws:backup:us-east-1:$account:backup-vault:secondary_vault": {
                            "target_backup_vault_arn": {
                                "@@assign": "arn:aws:backup:us-east-1:$account:backup-vault:secondary_vault"
                            },
                            "lifecycle": {
                                "move_to_cold_storage_after_days": {
                                    "@@assign": "30"
                                },
                                "delete_after_days": {
                                    "@@assign": "120"
                                },
                                "opt_in_to_archive_for_supported_resources": {
                                    "@@assign": "false"
                                }
                            }
                        },
                        "arn:aws:backup:us-west-1:111111111111:backup-vault:tertiary_vault": {
                            "target_backup_vault_arn": {
                                "@@assign": "arn:aws:backup:us-west-1:111111111111:backup-vault:tertiary_vault"
                            },
                            "lifecycle": {
                                "move_to_cold_storage_after_days": {
                                    "@@assign": "30"
                                },
                                "delete_after_days": {
                                    "@@assign": "120"
                                },
                                "opt_in_to_archive_for_supported_resources": {
                                    "@@assign": "false"
                                }
                            }
                        }
                    }
                }
            },
            "selections": {
                "tags": {
                    "datatype": {
                        "iam_role_arn": {
                            "@@assign": "arn:aws:iam::$account:role/MyIamRole"
                        },
                        "tag_key": {
                            "@@assign": "dataType"
                        },
                        "tag_value": {
                            "@@assign": [
                                "PII",
                                "RED"
                            ]
                        }
                    }
                }
            },
            "advanced_backup_settings": {
                "ec2": {
                    "windows_vss": {
                        "@@assign": "enabled"
                    }
                }
            }
        }
    }
}
```

If no other policies are inherited or attached to the accounts, the effective
policy rendered in each applicable AWS account looks like the following example.
The CRON expression causes the backup to run once an hour on the hour. The account
ID 123456789012 will be the actual account ID for each account.

```
{
    "plans": {
        "PII_Backup_Plan": {
            "regions": [
                "us-east-1",
                "ap-northeast-3",
                "eu-north-1"
            ],
            "rules": {
                "hourly": {
                    "schedule_expression": "cron(0 0/1 ? * * *)",
                    "start_backup_window_minutes": "60",
                    "target_backup_vault_name": "FortKnox",
                    "target_logically_air_gapped_backup_vault_arn": "arn:aws:backup:$region:$account:backup-vault:AirGappedVault",
                    "index_actions": {
                        "resource_types": {
                            "@@assign": [
                                "EBS",
                                "S3"
                            ]
                        }
                     },
                    "lifecycle": {
                        "delete_after_days": "2",
                        "move_to_cold_storage_after_days": "180",
                        "opt_in_to_archive_for_supported_resources": "false"
                    },
                    "copy_actions": {
                        "arn:aws:backup:us-east-1:$account:backup-vault:secondary_vault": {
                            "target_backup_vault_arn": {
                                "@@assign": "arn:aws:backup:us-east-1:$account:backup-vault:secondary_vault"
                            },
                            "lifecycle": {
                                "delete_after_days": "28",
                                "move_to_cold_storage_after_days": "180",
                                "opt_in_to_archive_for_supported_resources": "false"
                            }
                        },
                        "arn:aws:backup:us-west-1:111111111111:backup-vault:tertiary_vault": {
                            "target_backup_vault_arn": {
                                "@@assign": "arn:aws:backup:us-west-1:111111111111:backup-vault:tertiary_vault"
                            },
                            "lifecycle": {
                                "delete_after_days": "28",
                                "move_to_cold_storage_after_days": "180",
                                "opt_in_to_archive_for_supported_resources": "false"
                            }
                        }
                    }
                }
            },
            "selections": {
                "tags": {
                    "datatype": {
                        "iam_role_arn": "arn:aws:iam::123456789012:role/MyIamRole",
                        "tag_key": "dataType",
                        "tag_value": [
                            "PII",
                            "RED"
                        ]
                    }
                }
            },
            "advanced_backup_settings": {
                "ec2": {
                    "windows_vss": "enabled"
                }
            }
        }
    }
}
```

### Example 2: A parent policy is merged with

a child policy

In the following example, an inherited parent policy and a child policy either
inherited or directly attached to an AWS account merge to form the effective
policy.

**Parent policy** – This policy can be
attached to the organization's root or to any parent OU.

```
{
    "plans": {
       "PII_Backup_Plan": {
            "regions": { "@@append":[ "us-east-1", "ap-northeast-3", "eu-north-1" ] },
            "rules": {
                "Hourly": {
                    "schedule_expression": { "@@assign": "cron(0 0/1 ? * * *)" },
                    "start_backup_window_minutes": { "@@assign": "60" },
                    "target_backup_vault_name": { "@@assign": "FortKnox" },
                    "index_actions": {
                        "resource_types": {
                            "@@assign": [
                                "EBS",
                                "S3"
                            ]
                        }
                     },
                    "lifecycle": {
                        "move_to_cold_storage_after_days": { "@@assign": "28" },
                        "delete_after_days": { "@@assign": "180" },
                        "opt_in_to_archive_for_supported_resources": { "@@assign": "false" }
                    },
                    "copy_actions": {
                        "arn:aws:backup:us-east-1:$account:backup-vault:secondary_vault" : {
                            "target_backup_vault_arn" : {
                                "@@assign" : "arn:aws:backup:us-east-1:$account:backup-vault:secondary_vault"
                            },
                            "lifecycle": {
                                "move_to_cold_storage_after_days": { "@@assign": "28" },
                                "delete_after_days": { "@@assign": "180" },
                                "opt_in_to_archive_for_supported_resources": { "@@assign": "false" }
                            }
                        }
                    }
                }
            },
            "selections": {
                "tags": {
                    "datatype": {
                        "iam_role_arn": { "@@assign": "arn:aws:iam::$account:role/MyIamRole" },
                        "tag_key": { "@@assign": "dataType" },
                        "tag_value": { "@@assign": [ "PII", "RED" ] }
                    }
                }
            }
        }
    }
}
```

**Child policy** – This policy can be attached
directly to the account or to an OU any level below the one the parent policy is
attached to.

```
{
    "plans": {
       "Monthly_Backup_Plan": {
            "regions": {
                "@@append":[ "us-east-1", "eu-central-1" ] },
            "rules": {
                "Monthly": {
                    "schedule_expression": { "@@assign": "cron(0 5 1 * ? *)" },
                    "start_backup_window_minutes": { "@@assign": "480" },
                    "target_backup_vault_name": { "@@assign": "Default" },
                    "lifecycle": {
                        "move_to_cold_storage_after_days": { "@@assign": "30" },
                        "delete_after_days": { "@@assign": "365" },
                        "opt_in_to_archive_for_supported_resources": { "@@assign": "false" }
                    },
                    "copy_actions": {
                        "arn:aws:backup:us-east-1:$account:backup-vault:Default" : {
                            "target_backup_vault_arn" : {
                                "@@assign" : "arn:aws:backup:us-east-1:$account:backup-vault:Default"
                            },
                            "lifecycle": {
                                "move_to_cold_storage_after_days": { "@@assign": "30" },
                                "delete_after_days": { "@@assign": "365" },
                                "opt_in_to_archive_for_supported_resources": { "@@assign": "false" }
                            }
                        }
                    }
                }
            },
            "selections": {
                "tags": {
                    "MonthlyDatatype": {
                        "iam_role_arn": { "@@assign": "arn:aws:iam::$account:role/MyMonthlyBackupIamRole" },
                        "tag_key": { "@@assign": "BackupType" },
                        "tag_value": { "@@assign": [ "MONTHLY", "RED" ] }
                    }
                }
            }
        }
    }
}
```

**Resulting effective policy** – The effective
policy applied to the accounts contains two plans, each with its own set of rules
and set of resources to apply the rules to.

```
{
    "plans": {
       "PII_Backup_Plan": {
            "regions": [ "us-east-1", "ap-northeast-3", "eu-north-1" ],
            "rules": {
                "hourly": {
                    "schedule_expression": "cron(0 0/1 ? * * *)",
                    "start_backup_window_minutes": "60",
                    "target_backup_vault_name": "FortKnox",
                    "index_actions": {
                        "resource_types": {
                            "@@assign": [
                                "EBS",
                                "S3"
                            ]
                        }
                     },
                    "lifecycle": {
                        "delete_after_days": "2",
                        "move_to_cold_storage_after_days": "180",
                        "opt_in_to_archive_for_supported_resources": { "@@assign": "false" }
                    },
                    "copy_actions": {
                        "arn:aws:backup:us-east-1:$account:backup-vault:secondary_vault" : {
                            "target_backup_vault_arn" : {
                                "@@assign" : "arn:aws:backup:us-east-1:$account:backup-vault:secondary_vault"
                            },
                            "lifecycle": {
                                "move_to_cold_storage_after_days": "28",
                                "delete_after_days": "180",
                                "opt_in_to_archive_for_supported_resources": { "@@assign": "false" }
                            }
                        }
                    }
                }
            },
            "selections": {
                "tags": {
                    "datatype": {
                        "iam_role_arn": "arn:aws:iam::$account:role/MyIamRole",
                        "tag_key": "dataType",
                        "tag_value": [ "PII", "RED" ]
                    }
                }
            }
        },
        "Monthly_Backup_Plan": {
            "regions": [ "us-east-1", "eu-central-1" ],
            "rules": {
                "monthly": {
                    "schedule_expression": "cron(0 5 1 * ? *)",
                    "start_backup_window_minutes": "480",
                    "target_backup_vault_name": "Default",
                    "lifecycle": {
                        "delete_after_days": "365",
                        "move_to_cold_storage_after_days": "30",
                        "opt_in_to_archive_for_supported_resources": { "@@assign": "false" }
                    },
                    "copy_actions": {
                        "arn:aws:backup:us-east-1:$account:backup-vault:Default" : {
                            "target_backup_vault_arn": {
                                "@@assign" : "arn:aws:backup:us-east-1:$account:backup-vault:Default"
                            },
                            "lifecycle": {
                                "move_to_cold_storage_after_days": "30",
                                "delete_after_days": "365",
                                "opt_in_to_archive_for_supported_resources": { "@@assign": "false" }
                            }
                        }
                    }
                }
            },
            "selections": {
                "tags": {
                    "monthlydatatype": {
                        "iam_role_arn": "arn:aws:iam::&ExampleAWSAccountNo3;:role/MyMonthlyBackupIamRole",
                        "tag_key": "BackupType",
                        "tag_value": [ "MONTHLY", "RED" ]
                    }
                }
            }
        }
    }
}
```

### Example 3: A parent policy prevents any

changes by a child policy

In the following example, an inherited parent policy uses the [child control operators](policy-operators.md#child-control-operators "policy-operators.md#child-control-operators") to enforce all
settings and prevents them from being changed or overridden by a child policy.

**Parent policy** – This policy can be
attached to the organization's root or to any parent OU. The presence of
`"@@operators_allowed_for_child_policies": ["@@none"]` at every node
of the policy means that a child policy can't make changes of any kind to the plan.
Nor can a child policy add additional plans to the effective policy. This policy
becomes the effective policy for every OU and account under the OU to which it is
attached.

```
{
    "plans": {
        "@@operators_allowed_for_child_policies": ["@@none"],
        "PII_Backup_Plan": {
            "@@operators_allowed_for_child_policies": ["@@none"],
            "regions": {
                "@@operators_allowed_for_child_policies": ["@@none"],
                "@@append": [
                    "us-east-1",
                    "ap-northeast-3",
                    "eu-north-1"
                ]
            },
            "rules": {
                "@@operators_allowed_for_child_policies": ["@@none"],
                "Hourly": {
                    "@@operators_allowed_for_child_policies": ["@@none"],
                    "schedule_expression": {
                        "@@operators_allowed_for_child_policies": ["@@none"],
                        "@@assign": "cron(0 0/1 ? * * *)"
                    },
                    "start_backup_window_minutes": {
                        "@@operators_allowed_for_child_policies": ["@@none"],
                        "@@assign": "60"
                    },
                    "target_backup_vault_name": {
                        "@@operators_allowed_for_child_policies": ["@@none"],
                        "@@assign": "FortKnox"
                    },
                    "index_actions": {
                       "@@operators_allowed_for_child_policies": ["@@none"],
                        "resource_types": {
                            "@@assign": [
                                "EBS",
                                "S3"
                            ]
                        }
                     },
                    "lifecycle": {
                        "@@operators_allowed_for_child_policies": ["@@none"],
                        "move_to_cold_storage_after_days": {
                            "@@operators_allowed_for_child_policies": ["@@none"],
                            "@@assign": "28"
                        },
                        "delete_after_days": {
                            "@@operators_allowed_for_child_policies": ["@@none"],
                            "@@assign": "180"
                        },
                        "opt_in_to_archive_for_supported_resources": {
                            "@@operators_allowed_for_child_policies": ["@@none"],
                            "@@assign": "false"
                        }
                    },
                    "copy_actions": {
                        "@@operators_allowed_for_child_policies": ["@@none"],
                        "arn:aws:backup:us-east-1:$account:backup-vault:secondary_vault": {
                            "@@operators_allowed_for_child_policies": ["@@none"],
                            "target_backup_vault_arn": {
                                "@@assign": "arn:aws:backup:us-east-1:$account:backup-vault:secondary_vault",
                                "@@operators_allowed_for_child_policies": ["@@none"]
                            },
                            "lifecycle": {
                                "@@operators_allowed_for_child_policies": ["@@none"],
                                "delete_after_days": {
                                    "@@operators_allowed_for_child_policies": ["@@none"],
                                    "@@assign": "28"
                                },
                                "move_to_cold_storage_after_days": {
                                    "@@operators_allowed_for_child_policies": ["@@none"],
                                    "@@assign": "180"
                                },
                                 "opt_in_to_archive_for_supported_resources": {
                                    "@@operators_allowed_for_child_policies": ["@@none"],
                                    "@@assign": "false"
                                }
                            }
                        }
                    }
                }
            },
            "selections": {
                "@@operators_allowed_for_child_policies": ["@@none"],
                "tags": {
                    "@@operators_allowed_for_child_policies": ["@@none"],
                    "datatype": {
                        "@@operators_allowed_for_child_policies": ["@@none"],
                        "iam_role_arn": {
                            "@@operators_allowed_for_child_policies": ["@@none"],
                            "@@assign": "arn:aws:iam::$account:role/MyIamRole"
                        },
                        "tag_key": {
                            "@@operators_allowed_for_child_policies": ["@@none"],
                            "@@assign": "dataType"
                        },
                        "tag_value": {
                            "@@operators_allowed_for_child_policies": ["@@none"],
                            "@@assign": [
                                "PII",
                                "RED"
                            ]
                        }
                    }
                }
            },
            "advanced_backup_settings": {
                "@@operators_allowed_for_child_policies": ["@@none"],
                "ec2": {
                    "@@operators_allowed_for_child_policies": ["@@none"],
                    "windows_vss": {
                        "@@assign": "enabled",
                        "@@operators_allowed_for_child_policies": ["@@none"]
                    }
                }
            }
        }
    }
}
```

**Resulting effective policy** – If any child
backup policies exist, they are ignored and the parent policy becomes the effective
policy.

```
{
    "plans": {
        "PII_Backup_Plan": {
            "regions": [
                "us-east-1",
                "ap-northeast-3",
                "eu-north-1"
            ],
            "rules": {
                "hourly": {
                    "schedule_expression": "cron(0 0/1 ? * * *)",
                    "start_backup_window_minutes": "60",
                    "target_backup_vault_name": "FortKnox",
                    "index_actions": {
                        "resource_types": {
                            "@@assign": [
                                "EBS",
                                "S3"
                            ]
                        }
                     },
                    "lifecycle": {
                        "delete_after_days": "2",
                        "move_to_cold_storage_after_days": "180",
                        "opt_in_to_archive_for_supported_resources": "false"
                    },
                    "copy_actions": {
                        "target_backup_vault_arn": "arn:aws:backup:us-east-1:123456789012:backup-vault:secondary_vault",
                        "lifecycle": {
                            "move_to_cold_storage_after_days": "28",
                            "delete_after_days": "180",
                            "opt_in_to_archive_for_supported_resources": "false"
                        }
                    }
                }
            },
            "selections": {
                "tags": {
                    "datatype": {
                        "iam_role_arn": "arn:aws:iam::123456789012:role/MyIamRole",
                        "tag_key": "dataType",
                        "tag_value": [
                            "PII",
                            "RED"
                        ]
                    }
                }
            },
            "advanced_backup_settings": {
                "ec2": {"windows_vss": "enabled"}
            }
        }
    }
}
```

### Example 4: A parent policy prevents

changes to one backup plan by a child policy

In the following example, an inherited parent policy uses the [child control operators](policy-operators.md#child-control-operators "policy-operators.md#child-control-operators") to enforce the
settings for a single plan and prevents them from being changed or overridden by a
child policy. The child policy can still add additional plans.

**Parent policy** – This policy can be
attached to the organization's root or to any parent OU. This example is similar to
the previous example with all child inheritance operators blocked, except at the
`plans` top level. The `@@append` setting at that level
enables child policies to add other plans to the collection in the effective policy.
Any changes to the inherited plan are still blocked.

The sections in the plan are truncated for clarity.

```
{
    "plans": {
        "@@operators_allowed_for_child_policies": ["@@append"],
        "PII_Backup_Plan": {
            "@@operators_allowed_for_child_policies": ["@@none"],
            "regions": { ... },
            "rules": { ... },
            "selections": { ... }
        }
    }
}
```

**Child policy** – This policy can be attached
directly to the account or to an OU any level below the one the parent policy is
attached to. This child policy defines a new plan.

The sections in the plan are truncated for clarity.

```
{
    "plans": {
        "MonthlyBackupPlan": {
            "regions": { ... },
            "rules": { ... },
            "selections": { … }
        }
    }
}
```

**Resulting effective policy** – The effective
policy includes both plans.

```
{
    "plans": {
        "PII_Backup_Plan": {
            "regions": { ... },
            "rules": { ... },
            "selections": { ... }
        },
        "MonthlyBackupPlan": {
            "regions": { ... },
            "rules": { ... },
            "selections": { … }
        }
    }
}
```

### Example 5: A child policy overrides

settings in a parent policy

In the following example, a child policy uses [value-setting operators](policy-operators.md#value-setting-operators "policy-operators.md#value-setting-operators") to override
some of the settings inherited from a parent policy.

**Parent policy** – This policy can be
attached to the organization's root or to any parent OU. Any of the settings can be
overridden by a child policy because the default behavior, in the absence of a [child-control operator](policy-operators.md#child-control-operators "policy-operators.md#child-control-operators") that prevents
it, is to allow the child policy to `@@assign`, `@@append`, or
`@@remove`. The parent policy contains all of the required elements
for a valid backup plan, so it backs up your resources successfully if it is
inherited as is.

```
{
    "plans": {
        "PII_Backup_Plan": {
            "regions": {
                "@@append": [
                    "us-east-1",
                    "ap-northeast-3",
                    "eu-north-1"
                ]
            },
            "rules": {
                "Hourly": {
                    "schedule_expression": {"@@assign": "cron(0 0/1 ? * * *)"},
                    "start_backup_window_minutes": {"@@assign": "60"},
                    "target_backup_vault_name": {"@@assign": "FortKnox"},
                    "index_actions": {
                        "resource_types": {
                            "@@assign": [
                                "EBS",
                                "S3"
                            ]
                        }
                     },
                    "lifecycle": {
                        "delete_after_days": {"@@assign": "2"},
                        "move_to_cold_storage_after_days": {"@@assign": "180"},
                        "opt_in_to_archive_for_supported_resources": {"@@assign": false}
                    },
                    "copy_actions": {
                        "arn:aws:backup:us-east-1:$account:backup-vault:t2": {
                            "target_backup_vault_arn": {"@@assign": "arn:aws:backup:us-east-1:$account:backup-vault:t2"},
                            "lifecycle": {
                                "move_to_cold_storage_after_days": {"@@assign": "28"},
                                "delete_after_days": {"@@assign": "180"},
                                "opt_in_to_archive_for_supported_resources": {"@@assign": false}
                            }
                        }
                    }
                }
            },
            "selections": {
                "tags": {
                    "datatype": {
                        "iam_role_arn": {"@@assign": "arn:aws:iam::$account:role/MyIamRole"},
                        "tag_key": {"@@assign": "dataType"},
                        "tag_value": {
                            "@@assign": [
                                "PII",
                                "RED"
                            ]
                        }
                    }
                }
            }
        }
    }
}
```

**Child policy** – The child policy includes
only the settings that need to be different from the inherited parent policy. There
must be an inherited parent policy that provides the other required settings when
merged into an effective policy. Otherwise, the effective backup policy contains a
backup plan that is not valid and doesn't back up your resources as expected.

```
{
    "plans": {
        "PII_Backup_Plan": {
            "regions": {
                "@@assign": [
                    "us-west-2",
                    "eu-central-1"
                ]
            },
            "rules": {
                "Hourly": {
                    "schedule_expression": {"@@assign": "cron(0 0/2 ? * * *)"},
                    "start_backup_window_minutes": {"@@assign": "80"},
                    "target_backup_vault_name": {"@@assign": "Default"},
                    "lifecycle": {
                        "move_to_cold_storage_after_days": {"@@assign": "30"},
                        "delete_after_days": {"@@assign": "365"},
                        "opt_in_to_archive_for_supported_resources": {"@@assign": false}
                    }
                }
            }
        }
    }
}
```

**Resulting effective policy** – The effective
policy includes settings from both policies, with the settings provided by the child
policy overriding the settings inherited from the parent. In this example, the
following changes occur:

- The list of Regions is replaced with a completely different list. If you
  wanted to add a Region to the inherited list, use `@@append`
  instead of `@@assign` in the child policy.
- AWS Backup performs every other hour instead of hourly.
- AWS Backup allows 80 minutes for the backup to start instead of 60 minutes.
- AWS Backup uses the `Default` vault instead of
  `FortKnox`.
- The lifecycle is extended for both the transfer to cold storage and the
  eventual deletion of the backup.

```
{
    "plans": {
        "PII_Backup_Plan": {
            "regions": [
                "us-west-2",
                "eu-central-1"
            ],
            "rules": {
                "hourly": {
                    "schedule_expression": "cron(0 0/2 ? * * *)",
                    "start_backup_window_minutes": "80",
                    "target_backup_vault_name": "Default",
                     "index_actions": {
                        "resource_types": {
                            "@@assign": [
                                "EBS",
                                "S3"
                            ]
                        }
                     },
                    "lifecycle": {
                        "delete_after_days": "365",
                        "move_to_cold_storage_after_days": "30",
                        "opt_in_to_archive_for_supported_resources": "false"

                    },
                    "copy_actions": {
                        "arn:aws:backup:us-east-1:$account:backup-vault:secondary_vault": {
                            "target_backup_vault_arn": {"@@assign": "arn:aws:backup:us-east-1:$account:backup-vault:secondary_vault"},
                            "lifecycle": {
                                "move_to_cold_storage_after_days": "28",
                                "delete_after_days": "180",
                                "opt_in_to_archive_for_supported_resources": "false"
                            }
                        }
                    }
                }
            },
            "selections": {
                "tags": {
                    "datatype": {
                        "iam_role_arn": "arn:aws:iam::$account:role/MyIamRole",
                        "tag_key": "dataType",
                        "tag_value": [
                            "PII",
                            "RED"
                        ]
                    }
                }
            }
        }
    }
}
```

### Example 6: Specifying resources with the

`tags` block

The following example includes all resources with the `tag_key` =
`“env”` and and `tag_value` = `"prod"` and
`"gamma"`. This example excludes resources with the
`tag_key` = `"backup"` and the `tag_value` =
`"false"`.

```
...
"selections":{
    "tags":{
        "`selection_name`":{
            "iam_role_arn": {"@@assign": "arn:aws:iam::$account:role/IAMRole"},
            "tag_key":{"@@assign": "env"},
            "tag_value":{"@@assign": ["prod", "gamma"]},
            "conditions":{
                "string_not_equals":{
                    "`condition_name1`":{
                        "condition_key": { "@@assign": "aws:ResourceTag/backup"  },
                        "condition_value": {  "@@assign": "false" }
                    }
                }
            }
        }
    }
},
...
```

### Example 7: Specifying resources with the

`resources` block

The following are examples of using the `resources` block to specify
resources.

Example: Select all resources in my account
The Boolean logic is similar to what you might use in IAM policies.
The `"resource_types"` block uses a Boolean `AND`
to combine the resource types.

```
...
"resources":{
    "`resource_selection_name`":{
        "iam_role_arn":{"@@assign": "arn:aws:iam::$account:role/IAMRole"},
        "resource_types":{
            "@@assign": [
                "*"
            ]
        }
    }
},
...
```

Example: Select all resources in my account, but exclude Amazon EBS
volumes
The Boolean logic is similar to what you might use in IAM policies.
The `"resource_types"` and `"not_resource_types"`
blocks use a Boolean `AND` to combine the resource
types.

```
...
"resources":{
    "`resource_selection_name`":{
        "iam_role_arn":{"@@assign": "arn:aws:iam::$account:role/IAMRole"},
        "resource_types":{
            "@@assign": [
                "*"
            ]
        },
        "not_resource_types":{
            "@@assign": [
                "arn:aws:ec2:*:*:volume/*"
            ]
        }
    }
},
...
```

Example: Select all resources tagged with "backup" : "true", but
exclude Amazon EBS volumes
The Boolean logic is similar to what you might use in IAM policies.
The `"resource_types"` and `"not_resource_types"`
blocks use a Boolean `AND` to combine the resource types. The
`"conditions"` block uses a Boolean `AND`.

```
...
"resources":{
    "`resource_selection_name`":{
        "iam_role_arn":{"@@assign": "arn:aws:iam::$account:role/IAMRole"},
        "resource_types":{
            "@@assign": [
                "*"
            ]
        },
        "not_resource_types":{
            "@@assign": [
                "arn:aws:ec2:*:*:volume/*"
            ]
        },
        "conditions":{
            "string_equals":{
                "`condition_name1`":{
                    "condition_key": { "@@assign":"aws:ResourceTag/backup"},
                    "condition_value": {  "@@assign":"true" }
                }
            }
        }
    }
},
...
```

Example: Select all Amazon EBS volumes and Amazon RDS DB instances tagged with
both "backup" : "true" and "stage" : "prod"
The Boolean logic is similar to what you might use in IAM policies.
The `"resource_types"` block uses a Boolean `AND`
to combine the resource types. The `"conditions"` block uses
a Boolean `AND` to combine resource types and tag
conditions.

```
...
"resources":{
    "`resource_selection_name`":{
        "iam_role_arn":{"@@assign": "arn:aws:iam::$account:role/IAMRole"},
        "resource_types":{
            "@@assign": [
                "arn:aws:ec2:*:*:volume/*",
                "arn:aws:rds:*:*:db:*"
            ]
        },
        "conditions":{
            "string_equals":{
                "`condition_name1`":{
                    "condition_key":{"@@assign":"aws:ResourceTag/backup"},
                    "condition_value":{"@@assign":"true"}
                },
                "`condition_name2`":{
                    "condition_key":{"@@assign":"aws:ResourceTag/stage"},
                    "condition_value":{"@@assign":"prod"}
                }
            }
        }
    }
},
...
```

Example: Select all Amazon EBS volumes and Amazon RDS instances tagged with
"backup" : "true" but not "stage" : "test"
The Boolean logic is similar to what you might use in IAM policies.
The `"resource_types"` block uses a Boolean `AND`
to combine the resource types. The `"conditions"` block uses
a Boolean `AND` to combine resource types and tag
conditions.

```
...
"resources":{
    "`resource_selection_name`":{
        "iam_role_arn":{"@@assign": "arn:aws:iam::$account:role/IAMRole"},
        "resource_types":{
            "@@assign": [
                "arn:aws:ec2:*:*:volume/*",
                "arn:aws:rds:*:*:db:*"
            ]
        },
        "conditions":{
            "string_equals":{
                "`condition_name1`":{
                    "condition_key":{"@@assign":"aws:ResourceTag/backup"},
                    "condition_value":{"@@assign":"true"}
                  }
            },
            "string_not_equals":{
                "`condition_name2`":{
                    "condition_key":{"@@assign":"aws:ResourceTag/stage"},
                    "condition_value":{"@@assign":"test"}
                }
            }
        }
    }
},
...
```

Example: Select all resources tagged with "key1" and a value which
begins with "include" but not with "key2" and value that contains the word
"exclude"
The Boolean logic is similar to what you might use in IAM policies.
The `"resource_types"` block uses a Boolean `AND`
to combine the resource types. The `"conditions"` block uses
a Boolean `AND` to combine resource types and tag
conditions.

In this example, note the use of the wildcard character
`(*)` in `include*`, `*exclude*`,
and `arn:aws:rds:*:*:db:*`. You can use the wildcard
character `(*)` at the start, end, and middle of a
string.

```
...
"resources":{
    "`resource_selection_name`":{
        "iam_role_arn":{"@@assign": "arn:aws:iam::$account:role/IAMRole"},
        "resource_types":{
            "@@assign": [
                "*"
            ]
        },
        "conditions":{
            "string_like":{
                "`condition_name1`":{
                    "condition_key":{"@@assign":"aws:ResourceTag/key1"},
                    "condition_value":{"@@assign":"include*"}
                }
            },
            "string_not_like":{
                "`condition_name2`":{
                    "condition_key":{"@@assign":"aws:ResourceTag/key2"},
                    "condition_value":{"@@assign":"*exclude*"}
                }
            }
        }
    }
},
...
```

Example: Select all resources tagged with "backup" : "true" except
Amazon FSx file systems and Amazon RDS resources
The Boolean logic is similar to what you might use in IAM policies.
The `"resource_types"` and `"not_resource_types"`
blocks use a Boolean `AND` to combine the resource types. The
`"conditions"` block uses a Boolean `AND` to
combine resource types and tag conditions.

```
...
"resources":{
    "`resource_selection_name`":{
        "iam_role_arn":{"@@assign": "arn:aws:iam::$account:role/IAMRole"},
            "resource_types":{
                "@@assign": [
                    "*"
               ]
            },
            "not_resource_types":{
                "@@assign":[
                    "arn:aws:fsx:*:*:file-system/*",
                    "arn:aws:rds:*:*:db:*"
                ]
            },
        "conditions":{
            "string_equals":{
                "`condition_name1`":{
                    "condition_key":{"@@assign":"aws:ResourceTag/backup"},
                    "condition_value":{"@@assign":"true"}
                }
            }
        }
    }
},
...
```
