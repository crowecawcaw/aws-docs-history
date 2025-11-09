AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Create AWS resources for a migrated

application

In order to run your migrated application in AWS, you must create some AWS resources
with other AWS services. The resources you must create include the following:

- An S3 bucket to hold application code, configuration, data files, and other required
  artifacts.
- An Amazon RDS or Amazon Aurora database to hold the data that the application requires.
- An AWS KMS key, which is required by AWS Secrets Manager to create and store secrets.
- A Secrets Manager secret to hold the database credentials.

###### Note

Each migrated application requires its own set of these resources. This is a minimum set.
Your application might also require additional resources, such as Amazon Cognito secrets or MQ
queues.

## Required permissions

Make sure that you have the following permissions:

- `s3:CreateBucket`, `s3:PutObject`
- `rds:CreateDBInstance`
- `kms:CreateKey`
- `secretsmanager:CreateSecret`

## Amazon S3 bucket

Both refactored and replatformed applications require an Amazon S3 bucket that you configure as
follows:

```
bucket-name/root-folder-name/application-name
```

**bucket-name**

Any name within the constraints of Amazon S3 naming. We recommend that you include the
AWS Region name as part of your bucket name. Make sure that you create the bucket in the
same Region where you plan to deploy the migrated application.

**root-folder-name**

Name required to satisfy constraints in the application definition, which you create as
part of the AWS Mainframe Modernization application. You can use the `root-folder-name` to distinguish
between different versions of an application, for example, V1 and V2.

**application-name**

The name of your migrated application, for example, PlanetsDemo or BankDemo.

## Database

Both refactored and replatformed applications might require a database. You must create,
configure, and manage the database according to specific requirements for each runtime engine.
AWS Mainframe Modernization supports encryption in transit on this database. If you enable SSL on your database, make
sure that you specify `sslMode` in the database secret along with the connection
details of the database. For more information, see [AWS Secrets Manager secret](#applications-m2-other-resources-secret "#applications-m2-other-resources-secret").

If you use the AWS Blu Age refactoring pattern, and you need a Blusam database, the AWS Blu Age runtime
engine expects an Amazon Aurora PostgreSQL database, which you must create, configure, and manage. The
Blusam database is optional. Create this database only if your application requires it. To
create the database, follow the steps in [Creating an Amazon Aurora DB
cluster](../../../AmazonRDS/latest/AuroraUserGuide/Aurora.md "../../../AmazonRDS/latest/AuroraUserGuide/Aurora.md") in the _Amazon Aurora User Guide_.

If you are using the Rocket Software replatforming pattern, you can create either an Amazon RDS or an
Amazon Aurora PostgreSQL database. To create the database, follow the steps in [Creating an
Amazon RDS DB instance](../../../AmazonRDS/latest/UserGuide/USER_CreateDBInstance.md "../../../AmazonRDS/latest/UserGuide/USER_CreateDBInstance.md") in the _Amazon RDS User Guide_ or in [Creating
an Amazon Aurora DB cluster](../../../AmazonRDS/latest/AuroraUserGuide/Aurora.md "../../../AmazonRDS/latest/AuroraUserGuide/Aurora.md") in the _Amazon Aurora User Guide_.

For both runtime engines, you must store the database credentials in AWS Secrets Manager using an
AWS KMS key to encrypt them.

## AWS Key Management Service key

You must store the credentials for the application database securely in AWS Secrets Manager. To
create a secret in Secrets Manager, you must create an AWS KMS key. To create an KMS key, follow the
steps in [Creating
keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the _AWS Key Management Service Developer Guide_.

After you create the key, you must update the key policy to grant AWS Mainframe Modernization decrypt permissions.
Add the following policy statements:

```
{
   "Effect" : "Allow",
   "Principal" : {
   "Service" : "m2.amazonaws.com"
   },
   "Action" : "kms:Decrypt",
   "Resource" : "*"
   }
```

## AWS Secrets Manager secret

You must store the credentials for the application database securely in AWS Secrets Manager. To
create a secret follow the steps in [Create a database
secret](../../../secretsmanager/latest/userguide/create_database_secret.md "../../../secretsmanager/latest/userguide/create_database_secret.md") in the _AWS Secrets Manager User Guide_.

AWS Mainframe Modernization supports encryption in transit on this database. If you enable SSL on your database,
make sure that you specify `sslMode` in the database secret along with the connection
details of the database. You can specify one of the following values for `sslMode`:
`verify-full`, `verify-ca`, or `disable`.

During the key creation process, choose **Resource permissions -
optional**, and then choose **Edit permissions**. In the policy
editor, add a resource-based policy, such as the following, to retrieve the content of the
encrypted fields.

```
{
   "Effect" : "Allow",
   "Principal" : {
   "Service" : "m2.amazonaws.com"
   },
   "Action" : "secretsmanager:GetSecretValue",
   "Resource" : "*"
   }
```
