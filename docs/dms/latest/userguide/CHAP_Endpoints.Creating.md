# Using IAM authentication for Amazon RDS

endpoint in AWS DMS

AWS Identity and Access Management (IAM) database authentication provides
enhanced security for your Amazon RDS databases by managing database access through AWS
IAM credentials. Instead of using traditional database passwords, IAM authentication
generates short-lived authentication tokens, valid for 15 minutes, using AWS
credentials. This approach significantly improves security by eliminating the need
to store database passwords in application code, reducing the risk of credential
exposure, and providing centralized access management through IAM. It also
simplifies access management by leveraging existing AWS IAM roles and policies,
enabling you to control database access using the same IAM framework you use for
other AWS services.

AWS DMS now supports IAM authentication for replication instances running DMS
version 3.6.1 or later when connecting to MySQL, PostgreSQL, Aurora PostgreSQL,
Aurora MySQL, or MariaDB endpoints on Amazon RDS. When creating a new endpoint for
these engines, you can select IAM authentication and specify an IAM role instead of
providing database credentials. This integration enhances security by eliminating
the need to manage and store database passwords for your migration tasks.

## Configuring IAM

authentication for Amazon RDS endpoint in AWS DMS

When creating an endpoint you can configure IAM authentication for your Amazon RDS
database. To configure IAM authentication, do the following:

1. Ensure the Amazon RDS and the database user has IAM authentication
   enabled. For more information, see [Enabling and disabling IAM database
   authentication](../../../AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.md "../../../AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.md") in the _Amazon
   Relational Database Service user guide_.
2. Navigate to the IAM Console, create an IAM role with the below
   policies:

Policy

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "rds-db:connect"
 ],
 "Resource": "*"
 }
 ]
}`

```

Trust policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "dms.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

3. During the endpoint configuration in the [AWS DMS console](https://console.aws.amazon.com/dms/v2 "https://console.aws.amazon.com/dms/v2"), navigate to the **Access to endpoint database** section and select **IAM authentication**.
4. In the **IAM role for RDS database authentication** dropdown menu, select the IAM role with appropriate permissions to access the database.

For more information, see [Creating source and target endpoints](CHAP_Endpoints.md "CHAP_Endpoints.md").

1. Ensure the Amazon RDS and the database user has IAM authentication
   enabled. For more information, see [Enabling and disabling IAM database
   authentication](../../../AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.md "../../../AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.md") in the _Amazon
   Relational Database Service user guide_.
2. Navigate to the AWS CLI, create an IAM role, and allow DMS
   to assume the role:

Policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "rds-db:connect"
 ],
 "Resource": "*"
 }
 ]
}`

```

Trust policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "dms.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

3. Run the following command to import the certificate and
   download the PEM file. For more information, see [Download certificate bundles for Amazon
   RDS](../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md#UsingWithRDS.SSL.CertificatesDownload "../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md#UsingWithRDS.SSL.CertificatesDownload") in the _Amazon Relational
   Database Service user guide_.

```
aws dms import-certificate --certificate-identifier rdsglobal --certificate-pem file://~/global-bundle.pem
```

4. Run the following commands to create an IAM endpoint:
   - For PostgreSQL/Aurora PostgreSQL endpoints (When
     `sslmode` is set to
     `required`, `--certificate-arn`
     flag is not required):

   ```
   aws dms create-endpoint --endpoint-identifier <endpoint-name> --endpoint-type <source/target> --engine-name <postgres/aurora-postgres> --username <db username with iam auth privileges> --server-name <db server name> --port <port number> --ssl-mode <required/verify-ca/verify-full> --postgre-sql-settings "{\"ServiceAccessRoleArn\": \"role arn created from step 2 providing permissions for iam authentication\", \"AuthenticationMethod\": \"iam\", \"DatabaseName\": \"database name\"}" --certificate-arn <if sslmode is verify-ca/verify full use cert arn generated in step 3, otherwise this parameter is not required>
   ```

   - For MySQL, MariaDB, or Aurora MySQL endpoints:

   ```
   aws dms create-endpoint --endpoint-identifier <endpoint-name> --endpoint-type <source/target> --engine-name <mysql/mariadb/aurora> --username <db username with iam auth privileges> --server-name <db server name> --port <port number> --ssl-mode <verify-ca/verify-full> --my-sql-settings "{\"ServiceAccessRoleArn\": \"role arn created from step 2 providing permissions for iam authentication\", \"AuthenticationMethod\": \"iam\", \"DatabaseName\": \"database name\"}" --certificate-arn <cert arn from previously imported cert in step 3>
   ```

5. Run a test connection against your desired replication
   instance to create the instance endpoint association and verify
   everything is set up correctly:

```
aws dms test-connection --replication-instance-arn <replication instance arn> --endpoint-arn <endpoint arn from previously created endpoint in step 4>
```

###### Note

When using IAM authentication, the replication instance
provided in test-connection must be on AWS DMS version 3.6.1
or later.

## Limitations

AWS DMS has following limitations when using IAM authentication with Amazon RDS
endpoint:

- Currently Amazon RDS PostgreSQL and Amazon Aurora PostgreSQL instances do
  not support CDC connections with IAM authentication. For more
  information, see [Limitations for IAM database authentication](../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md#UsingWithRDS.IAMDBAuth.Limitations "../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md#UsingWithRDS.IAMDBAuth.Limitations") in the
  _Amazon Relational Database Service User
  Guide_.
