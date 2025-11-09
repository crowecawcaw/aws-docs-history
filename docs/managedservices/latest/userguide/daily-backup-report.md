# Backup report (daily)

The backup report covers primary and secondary (when applicable) regions. It covers the
status of backups (success/failure), and data on snapshots taken.

**This report provides:**

- Backup status
- Number of snapshots taken
- Recovery point
- Backup plan and vault information

| **Field Name**                                 | **Dataset Field Name**                         | **Definition**                                                                        |
| ---------------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------- |
| Report Datetime                                | dataset_datetime                               | The date and time the report was generated.                                           |
| Account Id                                     | aws_account_id                                 | AWS Account ID to which the instance ID belongs                                       |
| Admin Account Id                               | aws_admin_account_id                           | Trusted AWS Organizations account enabled by you.                                     |
| Account Name                                   | account_name                                   | AWS account name                                                                      |
| Account SLA                                    | account_sla                                    | AMS account service commitment                                                        |
|                                                | malz_flag                                      | Flag for MALZ-related account                                                         |
|                                                | malz_role                                      | MALZ role                                                                             |
|                                                | access_restrictions                            | Regions to which access is restricted                                                 |
| Backup snapshot scheduled start datetime       | start_by_dt_utc                                | Timestamp when snapshot is scheduled to begin                                         |
| Backup snapshot actual start datetime          | creation_dt_utc                                | Timestamp when snapshot actually begins                                               |
| Backup snapshot completion datetime            | completion_dt_utc                              | Timestamp when snapshot is completed                                                  |
| Backup snapshot expiration datetime            | expiration_dt_utc                              | Timestamp when snapshot expires                                                       |
| Backup Job status                              | backup_job_status                              | State of the snapshot                                                                 |
| Backup Type                                    | backup_type                                    | Type of backup                                                                        |
| Backup Job Id                                  | backup_job_id                                  | The unique identifier of the backup job                                               |
| Backup Size In Bytes                           | backup_size_in_bytes                           | The backup size in bytes                                                              |
| Backup Plan ARN                                | backup_plan_arn                                | The backup plan ARN                                                                   |
| Backup Plan Id                                 | backup_plan_id                                 | Backup plan unique identifier                                                         |
| Backup Plan Name                               | backup_plan_name                               | The Backup Plan name                                                                  |
| Backup Plan Version                            | backup_plan_version                            | The backup plan version                                                               |
| Backup Rule Id                                 | backup_rule_id                                 | The backup rule id                                                                    |
| Backup Vault ARN                               | backup_vault_arn                               | Backup vault ARN                                                                      |
| Backup Vault Name                              | backup_vault_name                              | The backup vault name                                                                 |
| IAM Role ARN                                   | iam_role_arn                                   | The IAM role ARN                                                                      |
| Instance Id                                    | instance_id                                    | Unique instance Id                                                                    |
| Instance State                                 | instance_state                                 | Instance state                                                                        |
| Instance Tags                                  | ec2_tags                                       | The tags associated with the EC2 Instance ID                                          |
| Resource ARN                                   | resource_arn                                   | The Amazon resource name                                                              |
| Resource Id                                    | resource_id                                    | The unique resource identifier                                                        |
| Resource Region                                | resource_region                                | The resource's primary (and secondary, when applicable) regions.                      |
| Resource Type                                  | resource_type                                  | The type of resource                                                                  |
| Recovery Point ARN                             | recovery_point_arn                             | The ARN of the recovery point                                                         |
| Recovery Point Id                              | recovery_point_id                              | The unique identifier of the recovery point                                           |
| Recovery Point Status                          | recovery_point_status                          | Recovery point status                                                                 |
| Recovery Point Delete After Days               | recovery_point_delete_after_days               | Recovery point delete after days                                                      |
| Recovery point move to cold storage after days | recovery_point_move_to_cold_storage_after_days | Number of days after completion date when backup<br>snapshot is moved to cold storage |
| Recovery Point Encryption Status               | recovery_point_is_encrypted                    | Recovery point encryption status                                                      |
| Recovery Point Encryption Key ARN              | recovery_point_encryption_key_arn              | Recovery point encryption key ARN                                                     |
| Stack Id                                       | stack_id                                       | Cloudformation stack unique identifier                                                |
| Stack Name                                     | stack_name                                     | Stack Name                                                                            |
| Tag: AMS Default Patch Group                   | tag_ams_default_patch_group                    | Tag Value: AMS Default Patch Group                                                    |
| Tag: App Id                                    | tag_app_id                                     | Tag Value: App ID                                                                     |
| Tag: App Name                                  | tag_app_name                                   | Tag Value: App Name                                                                   |
| Tag: Backup                                    | tag_backup                                     | Tag Value: Backup                                                                     |
| Tag: Compliance Framework                      | tag_compliance_framework                       | Tag Value: Compliance Framework                                                       |
| Tag: Cost Center                               | tag_cost_center                                | Tag Value: Cost Center                                                                |
| Tag: Customer                                  | tag_customer                                   | Tag Value: Customer                                                                   |
| Tag: Data Classification                       | tag_data_classification                        | Tag Value: Data Classification                                                        |
| Tag: Environment Type                          | tag_environment_type                           | Tag Value: Environment Type                                                           |
| Tag: Hours of Operation                        | tag_hours_of_operation                         | Tag Value: Hours of Operation                                                         |
| Tag: Owner Team                                | tag_owner_team                                 | Tag Value: Owner Team                                                                 |
| Tag: Owner Team Email                          | tag_owner_team_email                           | Tag Value: Owner Team Email                                                           |
| Tag: Patch Group                               | tag_patch_group                                | Tag Value: Patch Group                                                                |
| Tag: Support Priority                          | tag_support_priority                           | Tag Value: Support Priority                                                           |
| Volume State                                   | volume_state                                   | Volume State                                                                          |
