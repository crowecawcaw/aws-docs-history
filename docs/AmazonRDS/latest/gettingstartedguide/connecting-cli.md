# Using the AWS CLI to retrieve and validate connection information for Amazon RDS

While the AWS Command Line Interface (AWS CLI) doesn't directly connect to a database for querying or
interactive use, it provides tools to manage and test the connectivity of your Amazon RDS DB
instance. You can retrieve connection details, validate network configurations, and generate
authentication tokens if you're using IAM authentication. This section explains how to use the
AWS CLI to prepare to connect to your database using a client tool.

## Testing connectivity using the AWS CLI

Test connectivity with the AWS CLI to make sure you can reach your DB instance from your
local environment. The following steps guide you through retrieving and verifying connection
details.

###### To test connectivity using the CLI

1. Retrieve the endpoint and port. Use the following [describe-db-instances](../../../cli/latest/reference/rds/describe-db-instances.md "../../../cli/latest/reference/rds/describe-db-instances.md")
   command to retrieve connection information for your DB instance:

```
aws rds describe-db-instances \
  --db-instance-identifier `your-db-instance-id` \
  --query "DBInstances[0].[Endpoint.Address, Endpoint.Port]"
```

Replace `your-db-instance-id` with the identifier of your DB
instance.

The output should include the endpoint (hostname) and port, which you need in order
to configure your database client. 2. Verify the output. Make sure that the endpoint and port match the values in the
AWS Management Console. If there are any discrepancies, check the DB instance
configuration.

## Resolving network and authentication issues using the AWS CLI

Misconfigured network settings or incorrect authentication credentials are common causes
of connectivity issues. The AWS CLI provides commands to check and resolve these
problems.

1. Check network settings. Network issues often stem from incorrect security group or
   VPC configurations.
   - **Verify security group rules**. Make sure that the
     security group associated with your DB instance allows inbound traffic on the
     database port (for example, 3306 for MySQL or 5432 for PostgreSQL) from your IP
     address.

   ```
   aws ec2 describe-security-groups \
     --group-ids `security-group-id`
   ```

   Replace `security-group-id` with the ID of your security
   group.
   - **Check subnet configurations**. Confirm that your
     DB instance resides in a subnet that allows connectivity.

   ```
   aws ec2 describe-subnets \
     --subnet-ids `subnet-id`
   ```

   Replace `subnet-id` with the ID of the subnet for your DB
   instance.

2. Validate configuration details. Authentication errors can occur due to incorrect
   credentials or improper IAM configuration.
   - **Reset the master password**. If the master
     password is incorrect or you forgot it, reset it using the following [moidfy-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md")
     command:

   ```
   aws rds modify-db-instance \
     --db-instance-identifier `db-instance-id` \
     --master-user-password `new-password`
   ```

   Replace `db-instance-id` with your instance ID and
   `new-password` with the new password.
   - **Verify the master username**. Confirm the master
     username for your DB instance with the following [describe-db-instances](../../../cli/latest/reference/rds/describe-db-instances.md "../../../cli/latest/reference/rds/describe-db-instances.md")
     command:

   ```
   aws rds describe-db-instances \
     --db-instance-identifier `db-instance-id` \
     --query "DBInstances[0].MasterUsername"
   ```

   Make sure that the username matches what you’re using in your database
   client.
   - **Check IAM authentication**. If your DB instance
     uses IAM authentication, generate a temporary token for login with the following
     [generate-db-auth-token](../../../cli/latest/reference/rds/generate-db-auth-token.md "../../../cli/latest/reference/rds/generate-db-auth-token.md") command:

   ```
   aws rds generate-db-auth-token \
     --hostname `endpoint` \
     --port `port` \
     --username `iam-user`
   ```

   Replace `endpoint`, `port`, and `iam-user` with
   your DB instance endpoint, port, and IAM username. For more information, see [IAM database authentication for MariaDB, MySQL, and PostgreSQL](../UserGuide/UsingWithRDS.md "../UserGuide/UsingWithRDS.md") in the
   _Amazon RDS User Guide_.

By combining these CLI commands, you can verify that your DB instance is accessible and
correctly configured. If connection issues persist, see [Troubleshooting for Amazon
RDS](../UserGuide/CHAP_Troubleshooting.md "../UserGuide/CHAP_Troubleshooting.md") in the _Amazon RDS User Guide_.

## Next steps

Once you have the required connection details, including the instance endpoint and port,
you can use them to connect to the DB instance.

**Next step:** [Connecting to an Amazon RDS DB instance using a database client](connecting-client.md "connecting-client.md")
