# Disabling RDS for SQL Server integration with S3

Following, you can find how to disable Amazon S3 integration with Amazon RDS for SQL Server. Files in
`D:\S3\` aren't deleted when disabling S3 integration.

###### Note

To remove an IAM role from a DB instance, the status of the DB instance must be
`available`.

###### To disassociate your IAM role from your DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Choose the RDS for SQL Server DB instance name to display its details.
3. On the **Connectivity & security** tab, in the **Manage
   IAM roles** section, choose the IAM role to remove.
4. Choose **Delete**.

###### To remove the IAM role from the RDS for SQL Server DB instance

- The following AWS CLI command removes the IAM role from a RDS for SQL Server DB instance
  named `mydbinstance`.

For Linux, macOS, or Unix:

```
aws rds remove-role-from-db-instance \
	   --db-instance-identifier `mydbinstance` \
	   --feature-name S3_INTEGRATION \
	   --role-arn `your-role-arn`
```

For Windows:

```
aws rds remove-role-from-db-instance ^
	   --db-instance-identifier `mydbinstance` ^
	   --feature-name S3_INTEGRATION ^
	   --role-arn `your-role-arn`
```

Replace `your-role-arn` with the appropriate IAM
role ARN for the `--feature-name` option.
