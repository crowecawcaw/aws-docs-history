# Managing a DB instance in a Domain

You can use the console, AWS CLI, or the Amazon RDS API to manage your DB instance and its
relationship with your domain. For example, you can move the DB instance into, out of,
or between domains.

For example, using the Amazon RDS API, you can do the following:

- To reattempt a domain join for a failed membership, use the [ModifyDBInstance](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md") API
  operation and specify the current membership's directory ID.
- To update the IAM role name for membership, use the `ModifyDBInstance` API operation and
  specify the current membership's directory ID and the new IAM role.
- To remove a DB instance from a domain, use the `ModifyDBInstance` API operation and specify
  `none` as the domain parameter.
- To move a DB instance from one domain to another, use the `ModifyDBInstance` API operation
  and specify the domain identifier of the new domain as the domain parameter.
- To list membership for each DB instance, use the [DescribeDBInstances](../APIReference/DescribeDBInstances.md "../APIReference/DescribeDBInstances.md") API operation.

## Restoring a RDS Custom for SQL Server DB instance and adding it to an Active Directory domain

You can restore a DB snapshot or do point-in-time recovery (PITR) for a SQL Server DB instance and then add it to an Active Directory domain. Once
the DB instance is restored, modify the instance using the process explained in [Step 5: Create or modify a RDS Custom for SQL Server DB instance](custom-sqlserver-WinAuth.md#custom-sqlserver-WinAuth.settingUp.CreateDBInstance "custom-sqlserver-WinAuth.md#custom-sqlserver-WinAuth.settingUp.CreateDBInstance") to add
the DB instance to an AD domain.
