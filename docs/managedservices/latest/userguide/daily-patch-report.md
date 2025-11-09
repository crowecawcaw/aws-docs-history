# Patch report (daily)

###### Available reports

-
- [Patch details](#patch-details "#patch-details")
- [Instances that missed patches](#instances-that-missed-patches "#instances-that-missed-patches")

This is an informational report that helps identify all
the instances onboarded to Patch Orchestrator (PO), account status, instance details,
maintenance window coverage, maintenance window execution time, stack details, and platform type.

**This dataset provides:**

- Data on the Production and Non-Production instances of an account. Production and Non-Production
  stage is derived from the account name and not from the instance tags.
- Data on the distribution of instances by platform type. The 'N/A' platform type occurs when
  AWS Systems Manager (SSM) can't get the platform information.
- Data on the distribution of state of instances, number of instances
  running, stopped, or terminating.

| **Console Field Name**                | **Dataset Field Name**         | **Definition**                                                                                                                               |
| ------------------------------------- | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Access Restrictions                   | access_restrictions            | Regions to which access is restricted                                                                                                        |
| Account Id                            | aws_account_id                 | AWS Account ID to which the instance ID belongs                                                                                              |
| Admin Account Id                      | aws_admin_account_id           | Trusted AWS Organizations account enabled by you.                                                                                            |
| Account Name                          | account_name                   | AWS account name                                                                                                                             |
| Account Status                        | account_status                 | AMS account status                                                                                                                           |
|                                       | account_sla                    | AMS account service commitment                                                                                                               |
| Account Type                          | malz_role                      | MALZ role                                                                                                                                    |
| Auto Scaling Group Name               | instance_asg_name              | Name of Auto Scaling Group (ASG) that contains the instance                                                                                  |
| Instance Id                           | instance_id                    | ID of EC2 instance                                                                                                                           |
| Instance Name                         | instance_name                  | Name of EC2 instance                                                                                                                         |
| Instance Patch Group                  | instance_patch_group           | Patch group name used to group instances together and apply the same maintenance window                                                      |
| Instance Patch Group Type             | instance_patch_group_type      | Patch group type                                                                                                                             |
| Instance Platform Type                | instance_platform_type         | Operating System (OS) type                                                                                                                   |
| Instance Platform Name                | instance_platform_name         | Operating System (OS) name                                                                                                                   |
| Instance State                        | instance_state                 | State within the EC2 instance lifecycle                                                                                                      |
| Instance Tags                         | ec2_tags                       | The tags associated with the Amazon EC2 instance ID                                                                                          |
| Landing Zone                          | malz_flag                      | Flag for MALZ-related account                                                                                                                |
| Maintenance Window Coverage           | mw_covered_flag                | If an instance has at least one enabled maintenance window with a future execution date, then it’s considered covered, otherwise not covered |
| Maintenance Window Execution Datetime | earliest_window_execution_time | Next time the maintenance window is expected to execute                                                                                      |
| Maintenance Window Execution Datetime | earliest_window_execution_time | Next time the maintenance window is expected to execute                                                                                      |
| Production Account                    | prod_account                   | Identifier of AMS prod, non-prod accounts, depending on whether account name include value 'PROD', 'NONPROD'.                                |
| Report Datetime                       | dataset_datetime               | The date and time the report was generated.                                                                                                  |
| Stack Name                            | instance_stack_name            | Name of stack that contains instance                                                                                                         |
| Stack Type                            | instance_stack_type            | AMS stack (AMS infrastructure within customer account) or Customer stack (AMS managed infrastructure that<br>supports customer applications) |

## Patch details

This report provides patch details and maintenance window coverage of various instances.

**This report provides:**

- Data on Patch groups and its types.
- Data on Maintenance Windows, duration, cutoff, future dates of maintenance window executions (schedule) and instances impacted in each window.
- Data on all the operating systems under the account and the number of instances that the operating system is installed.

| **Field Name**                             | **Dataset Field Name**          | **Definition**                                                                                                                                                                                             |
| ------------------------------------------ | ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Report Datetime                            | dataset_datetime                | The date and time the report was generated.                                                                                                                                                                |
| Account Id                                 | aws_account_id                  | AWS Account ID to which the instance ID belongs                                                                                                                                                            |
| Account Name                               | account_name                    | AWS account name                                                                                                                                                                                           |
| Account Status                             | account_status                  | AMS account status                                                                                                                                                                                         |
| Compliant<br>• Critical                    | compliant_critical              | Count of compliant patches with "critical" severity                                                                                                                                                        |
| Compliant<br>• High                        | compliant_high                  | Count of compliant patches with "high" severity                                                                                                                                                            |
| Compliant<br>• Medium                      | compliant_medium                | Count of compliant patches with "medium" severity                                                                                                                                                          |
| Compliant<br>• Low                         | compliant_low                   | Count of compliant patches with "low" severity                                                                                                                                                             |
| Compliant<br>• Informational               | compliant_informational         | Count of compliant patches with "informational" severity                                                                                                                                                   |
| Compliant<br>• Unspecified                 | compliant_unspecified           | Count of compliant patches with "unspecified" severity                                                                                                                                                     |
| Compliant<br>• Total                       | compliant_total                 | Count of compliant patches (all severities)                                                                                                                                                                |
| Instance Id                                | instance_id                     | ID of EC2 instance                                                                                                                                                                                         |
| Instance Name                              | instance_name                   | Name of EC2 instance                                                                                                                                                                                       |
|                                            | account_sla                     | AMS account service tier                                                                                                                                                                                   |
| Instance Platform Type                     | instance_platform_type          | Operating System (OS) type                                                                                                                                                                                 |
| Instance Platform Name                     | instance_platform_name          | Operating System (OS) name                                                                                                                                                                                 |
| Instance Patch Group Type                  | instance_patch_group_type       | DEFAULT: default patch group w/ default maintenance window, determined by AMSDefaultPatchGroup:True tag on the instance<br>CUSTOMER: customer created patch group<br>NOT_ASSIGNED: no patch group assigned |
| Instance Patch Group                       | instance_patch_group            | Patch group name used to group instances together and<br>apply the same maintenance window                                                                                                                 |
| Instance State                             | instance_state                  | State within the EC2 instance life cycle                                                                                                                                                                   |
| Instance Tags                              | ec2_tags                        | The tags associated with the Amazon EC2 instance ID                                                                                                                                                        |
| Last Execution Maintenance Window          | last_execution_window           | The latest time the maintenance window was executed                                                                                                                                                        |
| Maintenance Window Id                      | window_id                       | Maintenance window ID                                                                                                                                                                                      |
| Maintenance Window State                   | window_state                    | Maintenance window state                                                                                                                                                                                   |
| Maintenance Window Type                    | window_type                     | Maintenance window type                                                                                                                                                                                    |
| Maintenance Window Next Execution Datetime | window_next<br>execution_time   | Next time the maintenance window is expected to execute                                                                                                                                                    |
| Maintenance Window Duration (hrs)          | window_duration                 | The duration of the maintenance window in hours                                                                                                                                                            |
| Maintenance Window Coverage                | mw_covered_flag                 | If an instance has at least one enabled maintenance window with a future execution date, then it’s considered<br>covered, otherwise not covered                                                            |
| Noncompliant<br>• Critical                 | noncompliant_critical           | Count of noncompliant patches with "critical" severity                                                                                                                                                     |
| Noncompliant<br>• High                     | noncompliant_high               | Count of noncompliant patches with "high" severity                                                                                                                                                         |
| Noncompliant<br>• Medium                   | noncompliant_medium             | Count of noncompliant patches with "medium" severity                                                                                                                                                       |
| Noncompliant<br>• Low                      | noncompliant_low                | Count of noncompliant patches with "low" severity                                                                                                                                                          |
| Noncompliant<br>• Informational            | noncompliant<br>\_informational | Count of noncompliant patches with "informational" severity                                                                                                                                                |
| Noncompliant<br>• Unspecified              | noncompliant<br>\_unspecified   | Count of noncompliant patches with "unspecified" severity                                                                                                                                                  |
| Noncompliant<br>• Total                    | noncompliant_total              | Count of noncompliant patches (all severities)                                                                                                                                                             |
| Patch Baseline Id                          | patch_baseline_id               | Patch baseline currently attached to instance                                                                                                                                                              |
| Patch Status                               | patch_status                    | Overall patch compliance status. If there is at least one missing patch, instance is considered noncompliant, otherwise compliant.                                                                         |
| Production Account                         | prod_account                    | Identifier of AMS prod, non-prod accounts, depending on whether account name include value 'PROD', 'NONPROD'.                                                                                              |
| Stack Type                                 | instance_stack_type             | AMS stack (AMS infrastructure within customer account)<br>or Customer stack (AMS managed infrastructure that supports customer applications)                                                               |
|                                            | window_next_exec_yyyy           | Year part of window_next_execution_time                                                                                                                                                                    |
|                                            | window_next_exec_mm             | Month part of window_next_execution_time                                                                                                                                                                   |
|                                            | window_next_exec_D              | Day part of window_next_execution_time                                                                                                                                                                     |
|                                            | window_next<br>\_exec_HHMI      | Hour:Minute part of window_next_execution_time                                                                                                                                                             |

## Instances that missed patches

This report provides details on instances
that missed patches during the last maintenance window execution.

**This report provides:**

- Data on missing patches at the patch ID level.
- Data on all the instances that have at least one missing patch and attributes such as patch
  severity, unpatched days, range, and release date of the patch.

| **Field Name**               | **Dataset Field Name** | **Definition**                                                                                                                |
| ---------------------------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Report Datetime              | dataset_datetime       | The date and time the report was generated                                                                                    |
| Account Id                   | aws_account_id         | AWS Account ID that the instance ID belongs to                                                                                |
| Account Name                 | account_name           | AWS account name                                                                                                              |
| Customer Name Parent         | customer_name_parent   |                                                                                                                               |
| Customer Name                | customer_name          |                                                                                                                               |
| Production Account           | prod_account           | Identifier of AMS prod or non-prod accounts, depending on<br>whether the account name includes the value 'PROD' or 'NONPROD'. |
| Account Status               | account_status         | AMS account status                                                                                                            |
| Account Type                 | account_type           |                                                                                                                               |
|                              | account_sla            | AMS account service tier                                                                                                      |
| Instance Id                  | instance_id            | ID of your EC2 instance                                                                                                       |
| Instance Name                | instance_name          | Name of your EC2 instance                                                                                                     |
| Instance Platform Type       | instance_platform_type | Operating System (OS) type                                                                                                    |
| Instance State               | instance_state         | State within the EC2 instance life cycle                                                                                      |
| Instance Tags                | ec2_tags               | The tags associated with the Amazon EC2 instance ID                                                                           |
| Patch Id                     | patch_id               | ID of released patch                                                                                                          |
| Patch Severity               | patch_sev              | Severity of patch per publisher                                                                                               |
| Patch Classification         | patch_class            | Classification of patch per the patch publisher                                                                               |
| Patch Release Datetime (UTC) | release_dt_utc         | Release date of patch per publisher                                                                                           |
| Patch Install State          | install_state          | Install state of patch on instance per SSM                                                                                    |
| Days Unpatched               | days_unpatched         | Number of days instance unpatched since last SSM scanning                                                                     |
| Days Unpatched Range         | days_unpatched_bucket  | Bucketing of days unpatched                                                                                                   |
