# Enabling cross-Region automated backups for Amazon RDS

You can enable backup replication on new or existing DB instances using the Amazon RDS
console. You can also use the `start-db-instance-automated-backups-replication` AWS CLI command or the
`StartDBInstanceAutomatedBackupsReplication` RDS API operation. You can replicate up to 20 backups to each
destination AWS Region for each AWS account.

###### Note

To be able to replicate automated backups, make sure to enable them. For more
information, see [Enabling automated backups](USER_WorkingWithAutomatedBackups.md "USER_WorkingWithAutomatedBackups.md").

You can enable backup replication for a new or existing DB instance:

- For a new DB instance, enable it when you launch the instance. For more information, see [Settings for DB instances](USER_CreateDBInstance.md "USER_CreateDBInstance.md").
- For an existing DB instance, use the following procedure.

###### To enable backup replication for an existing DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Automated backups**.
3. On the **Current Region** tab, choose the DB instance for which you want to enable backup
   replication.
4. For **Actions**, choose **Manage cross-Region replication**.
5. Under **Backup replication**, choose **Enable replication to another AWS Region**.
6. Choose the **Destination Region**.
7. Choose the **Replicated backup retention period**.
8. If you've enabled encryption on the source DB instance, choose the **AWS KMS key**
   for encrypting the backups or enter a key ARN.
9. Choose **Save**.
   In the source Region, replicated backups are listed on the **Current Region** tab of the
   **Automated backups** page. In the destination Region, replicated backups are listed on the
   **Replicated backups** tab of the **Automated backups** page.

Enable backup replication by using the [`start-db-instance-automated-backups-replication`](../../../cli/latest/reference/rds/start-db-instance-automated-backups-replication.md "../../../cli/latest/reference/rds/start-db-instance-automated-backups-replication.md") AWS CLI
command.

The following CLI example replicates automated backups from a DB instance in the US West (Oregon) Region to the US East (N. Virginia) Region.
It also encrypts the replicated backups, using an AWS KMS key in the destination Region.

###### To enable backup replication

- Run one of the following commands.

For Linux, macOS, or Unix:

```
aws rds start-db-instance-automated-backups-replication \
--region us-east-1 \
--source-db-instance-arn "arn:aws:rds:us-west-2:`123456789012`:db:`mydatabase`" \
--kms-key-id "arn:aws:kms:us-east-1:`123456789012`:key/`AKIAIOSFODNN7EXAMPLE`" \
--backup-retention-period `7`
```

For Windows:

```
aws rds start-db-instance-automated-backups-replication ^
--region us-east-1 ^
--source-db-instance-arn "arn:aws:rds:us-west-2:`123456789012`:db:`mydatabase`" ^
--kms-key-id "arn:aws:kms:us-east-1:`123456789012`:key/`AKIAIOSFODNN7EXAMPLE`" ^
--backup-retention-period `7`
```

The `--source-region` option is required when you encrypt
backups between the AWS GovCloud (US-East) and AWS GovCloud (US-West)
Regions. For `--source-region`, specify the
AWS Region of the source DB instance.

If `--source-region` isn't specified, make sure to
specify a `--pre-signed-url` value. A _presigned URL_ is a URL that contains a Signature Version
4 signed request for the
`start-db-instance-automated-backups-replication` command
that is called in the source AWS Region. To learn more about the
`pre-signed-url` option, see [start-db-instance-automated-backups-replication](../../../cli/latest/reference/rds/start-db-instance-automated-backups-replication.md "../../../cli/latest/reference/rds/start-db-instance-automated-backups-replication.md") in the _AWS CLI Command Reference_.
Enable backup replication by using the [`StartDBInstanceAutomatedBackupsReplication`](../APIReference/API_StartDBInstanceAutomatedBackupsReplication.md "../APIReference/API_StartDBInstanceAutomatedBackupsReplication.md") RDS API
operation with the following parameters:

- `Region` (if you aren't calling the API operation from the destination Region)
- `SourceDBInstanceArn`
- `BackupRetentionPeriod`
- `KmsKeyId` (optional)
- `PreSignedUrl` (required if you use `KmsKeyId`)

###### Note

If you encrypt the backups, you must also include a presigned URL. For more information on presigned URLs, see
[Authenticating Requests: Using Query Parameters (AWS
Signature Version 4)](../../../AmazonS3/latest/API/sigv4-query-string-auth.md "../../../AmazonS3/latest/API/sigv4-query-string-auth.md") in the _Amazon Simple Storage Service API Reference_ and [Signature Version 4 signing process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md") in the _AWS
General Reference_.
