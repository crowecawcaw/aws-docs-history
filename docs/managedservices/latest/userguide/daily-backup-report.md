End of support notice: On June 30, 2027, AWS
will end support for AMS Advanced. After June 30, 2027, you will
no longer be able to access the AMS Advanced console or AMS Advanced resources.
For more information, see [AMS Advanced end of support](SunsetPlan.md "SunsetPlan.md").

# Backup report (daily)

The backup report covers primary and secondary (when applicable) regions. It covers the
status of backups (success/failure), and data on snapshots taken.

**This report provides:**

- Backup status
- Number of snapshots taken
- Recovery point
- Backup plan and vault information

| **Field Name**                                 | **Dataset Field Name**                                | **Definition**                                                                        |
| ---------------------------------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Report Datetime                                | dataset\_datetime                                     | The date and time the report was generated.                                           |
| Account Id                                     | aws\_account\_id                                      | AWS Account ID to which the instance ID belongs                                       |
| Admin Account Id                               | aws\_admin\_account\_id                               | Trusted AWS Organizations account enabled by you.                                     |
| Account Name                                   | account\_name                                         | AWS account name                                                                      |
| Account SLA                                    | account\_sla                                          | AMS account service commitment                                                        |
|                                                | malz\_flag                                            | Flag for MALZ-related account                                                         |
|                                                | malz\_role                                            | MALZ role                                                                             |
|                                                | access\_restrictions                                  | Regions to which access is restricted                                                 |
| Backup snapshot scheduled start datetime       | start\_by\_dt\_utc                                    | Timestamp when snapshot is scheduled to begin                                         |
| Backup snapshot actual start datetime          | creation\_dt\_utc                                     | Timestamp when snapshot actually begins                                               |
| Backup snapshot completion datetime            | completion\_dt\_utc                                   | Timestamp when snapshot is completed                                                  |
| Backup snapshot expiration datetime            | expiration\_dt\_utc                                   | Timestamp when snapshot expires                                                       |
| Backup Job status                              | backup\_job\_status                                   | State of the snapshot                                                                 |
| Backup Type                                    | backup\_type                                          | Type of backup                                                                        |
| Backup Job Id                                  | backup\_job\_id                                       | The unique identifier of the backup job                                               |
| Backup Size In Bytes                           | backup\_size\_in\_bytes                               | The backup size in bytes                                                              |
| Backup Plan ARN                                | backup\_plan\_arn                                     | The backup plan ARN                                                                   |
| Backup Plan Id                                 | backup\_plan\_id                                      | Backup plan unique identifier                                                         |
| Backup Plan Name                               | backup\_plan\_name                                    | The Backup Plan name                                                                  |
| Backup Plan Version                            | backup\_plan\_version                                 | The backup plan version                                                               |
| Backup Rule Id                                 | backup\_rule\_id                                      | The backup rule id                                                                    |
| Backup Vault ARN                               | backup\_vault\_arn                                    | Backup vault ARN                                                                      |
| Backup Vault Name                              | backup\_vault\_name                                   | The backup vault name                                                                 |
| IAM Role ARN                                   | iam\_role\_arn                                        | The IAM role ARN                                                                      |
| Instance Id                                    | instance\_id                                          | Unique instance Id                                                                    |
| Instance State                                 | instance\_state                                       | Instance state                                                                        |
| Instance Tags                                  | ec2\_tags                                             | The tags associated with the EC2 Instance ID                                          |
| Resource ARN                                   | resource\_arn                                         | The Amazon resource name                                                              |
| Resource Id                                    | resource\_id                                          | The unique resource identifier                                                        |
| Resource Region                                | resource\_region                                      | The resource's primary (and secondary, when applicable) regions.                      |
| Resource Type                                  | resource\_type                                        | The type of resource                                                                  |
| Recovery Point ARN                             | recovery\_point\_arn                                  | The ARN of the recovery point                                                         |
| Recovery Point Id                              | recovery\_point\_id                                   | The unique identifier of the recovery point                                           |
| Recovery Point Status                          | recovery\_point\_status                               | Recovery point status                                                                 |
| Recovery Point Delete After Days               | recovery\_point\_delete\_after\_days                  | Recovery point delete after days                                                      |
| Recovery point move to cold storage after days | recovery\_point\_move\_to\_cold\_storage\_after\_days | Number of days after completion date when backup<br>snapshot is moved to cold storage |
| Recovery Point Encryption Status               | recovery\_point\_is\_encrypted                        | Recovery point encryption status                                                      |
| Recovery Point Encryption Key ARN              | recovery\_point\_encryption\_key\_arn                 | Recovery point encryption key ARN                                                     |
| Stack Id                                       | stack\_id                                             | Cloudformation stack unique identifier                                                |
| Stack Name                                     | stack\_name                                           | Stack Name                                                                            |
| Tag: AMS Default Patch Group                   | tag\_ams\_default\_patch\_group                       | Tag Value: AMS Default Patch Group                                                    |
| Tag: App Id                                    | tag\_app\_id                                          | Tag Value: App ID                                                                     |
| Tag: App Name                                  | tag\_app\_name                                        | Tag Value: App Name                                                                   |
| Tag: Backup                                    | tag\_backup                                           | Tag Value: Backup                                                                     |
| Tag: Compliance Framework                      | tag\_compliance\_framework                            | Tag Value: Compliance Framework                                                       |
| Tag: Cost Center                               | tag\_cost\_center                                     | Tag Value: Cost Center                                                                |
| Tag: Customer                                  | tag\_customer                                         | Tag Value: Customer                                                                   |
| Tag: Data Classification                       | tag\_data\_classification                             | Tag Value: Data Classification                                                        |
| Tag: Environment Type                          | tag\_environment\_type                                | Tag Value: Environment Type                                                           |
| Tag: Hours of Operation                        | tag\_hours\_of\_operation                             | Tag Value: Hours of Operation                                                         |
| Tag: Owner Team                                | tag\_owner\_team                                      | Tag Value: Owner Team                                                                 |
| Tag: Owner Team Email                          | tag\_owner\_team\_email                               | Tag Value: Owner Team Email                                                           |
| Tag: Patch Group                               | tag\_patch\_group                                     | Tag Value: Patch Group                                                                |
| Tag: Support Priority                          | tag\_support\_priority                                | Tag Value: Support Priority                                                           |
| Volume State                                   | volume\_state                                         | Volume State                                                                          |
