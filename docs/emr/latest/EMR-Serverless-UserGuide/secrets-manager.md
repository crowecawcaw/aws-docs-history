# Secrets Manager for data protection with EMR Serverless

AWS Secrets Manager is a secret storage service for protecting database credentials, API
keys, and other secret information. Then in your code, replace hardcoded credentials
with an API call to Secrets Manager. This helps ensure that the secret can't be compromised by someone
examining your code, because the secret isn't there. For an overview, refer to the [AWS Secrets Manager User
Guide](../../../secretsmanager/latest/userguide.md "../../../secretsmanager/latest/userguide.md").

Secrets Manager encrypts secrets using AWS Key Management Service keys. For more information, refer to [Secret
encryption and decryption](../../../secretsmanager/latest/userguide/security-encryption.md "../../../secretsmanager/latest/userguide/security-encryption.md") in the _AWS Secrets Manager User Guide_.

You can configure Secrets Manager to automatically rotate secrets for you according to a schedule that
you specify. This enables you to replace long-term secrets with short-term ones, which helps to
significantly reduce the risk of compromise. For more information, refer to [Rotate
AWS Secrets Manager secrets](../../../secretsmanager/latest/userguide/rotating-secrets.md "../../../secretsmanager/latest/userguide/rotating-secrets.md") in the _AWS Secrets Manager User Guide_.

Amazon EMR Serverless integrates with AWS Secrets Manager so that you can store your data in Secrets Manager and
use the secret ID in your configurations.

## How EMR Serverless uses secrets

When you store your data in Secrets Manager and use the secret ID in your configurations for
EMR Serverless, you don't pass sensitive configuration data to EMR Serverless in plain text and expose
it to external APIs. If you indicate that a key-value pair contains a secret ID for a secret
that you stored in Secrets Manager, EMR Serverless retrieves the secret when it sends configuration data to
workers for running jobs.

To indicate that a key-value pair for a configuration contains a reference to a secret
stored in Secrets Manager, add the `EMR.secret@` annotation to the configuration value. For
any configuration property with secret Id annotation, EMR Serverless calls Secrets Manager and resolves the
secret at the time of job execution.

## How to create a secret

To create a secret, follow the steps in [Create an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md")
in the _AWS Secrets Manager User Guide_. In **Step 3**,
choose the **Plaintext** field to enter your sensitive
value.

## Provide a secret in a configuration

classification

The following examples demonstrate how to provide a secret in a configuration classification at `StartJobRun`. If you want to configure classifications for Secrets Manager at the application level, refer to [Default application configuration for EMR Serverless](default-configs.md "default-configs.md").

In the examples, replace `SecretName` with the name of the secret to
retrieve.
. For more information, refer to [How to create a secret](#secrets-manager-create "#secrets-manager-create").

###### In this section

- [Specify secret references - Spark](#secrets-manager-examples-spark "#secrets-manager-examples-spark")
- [Specify secret references - Hive](#secrets-manager-examples-hive "#secrets-manager-examples-hive")

### Specify secret references - Spark

###### Example – Specify secret references in the external Hive metastore configuration for

Spark

```
aws emr-serverless start-job-run \
  --application-id "`application-id`" \
  --execution-role-arn "`job-role-arn`" \
  --job-driver '{
        "sparkSubmit": {
            "entryPoint": "s3://`amzn-s3-demo-bucket`/scripts/spark-jdbc.py",
            "sparkSubmitParameters": "--jars s3://`amzn-s3-demo-bucket`/mariadb-connector-java.jar
            --conf spark.hadoop.javax.jdo.option.ConnectionDriverName=org.mariadb.jdbc.Driver
            --conf spark.hadoop.javax.jdo.option.ConnectionUserName=`connection-user-name`
            --conf spark.hadoop.javax.jdo.option.ConnectionPassword=EMR.secret@`SecretName`
            --conf spark.hadoop.javax.jdo.option.ConnectionURL=jdbc:mysql://`db-host:db-port/db-name`
            --conf spark.driver.cores=2
            --conf spark.executor.memory=10G
            --conf spark.driver.memory=6G
            --conf spark.executor.cores=4"
        }
    }' \
    --configuration-overrides '{
        "monitoringConfiguration": {
        "s3MonitoringConfiguration": {
            "logUri": "s3://`amzn-s3-demo-bucket`/spark/logs/"
        }
    }
}'
```

###### Example – Specify secret references for the external Hive metastore configuration in

the `spark-defaults` classification

```
{
        "classification": "spark-defaults",
        "properties": {
            "spark.hadoop.javax.jdo.option.ConnectionDriverName":"org.mariadb.jdbc.Driver"
            "spark.hadoop.javax.jdo.option.ConnectionURL":"jdbc:mysql://`db-host:db-port/db-name`"
            "spark.hadoop.javax.jdo.option.ConnectionUserName":"`connection-user-name`"
            "spark.hadoop.javax.jdo.option.ConnectionPassword": "EMR.secret@`SecretName`",
        }
    }
```

### Specify secret references - Hive

###### Example – Specify secret references in the external Hive metastore configuration for

Hive

```
aws emr-serverless start-job-run \
  --application-id "`application-id`" \
  --execution-role-arn "`job-role-arn`" \
    --job-driver '{
        "hive": {
        "query": "s3://`amzn-s3-demo-bucket`/emr-serverless-hive/query/hive-query.ql",
        "parameters": "--hiveconf hive.exec.scratchdir=s3://`amzn-s3-demo-bucket`/emr-serverless-hive/hive/scratch
                    --hiveconf hive.metastore.warehouse.dir=s3://`amzn-s3-demo-bucket`/emr-serverless-hive/hive/warehouse
                    --hiveconf javax.jdo.option.ConnectionUserName=`username`
                    --hiveconf javax.jdo.option.ConnectionPassword=EMR.secret@`SecretName`
                    --hiveconf hive.metastore.client.factory.class=org.apache.hadoop.hive.ql.metadata.SessionHiveMetaStoreClientFactory
                    --hiveconf javax.jdo.option.ConnectionDriverName=org.mariadb.jdbc.Driver
                    --hiveconf javax.jdo.option.ConnectionURL=jdbc:mysql://`db-host:db-port/db-name`"
        }
    }' \
    --configuration-overrides '{
        "monitoringConfiguration": {
        "s3MonitoringConfiguration": {
            "logUri": "s3://`amzn-s3-demo-bucket`"
        }
    }
}'
```

###### Example – Specify secret references for the external Hive metastore configuration in

the `hive-site` classification

```
{
    "classification": "hive-site",
    "properties": {
        "hive.metastore.client.factory.class": "org.apache.hadoop.hive.ql.metadata.SessionHiveMetaStoreClientFactory",
        "javax.jdo.option.ConnectionDriverName": "org.mariadb.jdbc.Driver",
        "javax.jdo.option.ConnectionURL": "jdbc:mysql://`db-host:db-port/db-name`",
        "javax.jdo.option.ConnectionUserName": "username",
        "javax.jdo.option.ConnectionPassword": "EMR.secret@`SecretName`"
    }
}
```

## Grant access for EMR Serverless to retrieve the

secret

To allow EMR Serverless to retrieve the secret value from Secrets Manager, add the following policy
statement to your secret when you create it. You must create your secret with the
customer-managed KMS key for EMR Serverless to read the secret value. For more information, refer to
[Permissions for the KMS key](../../../secretsmanager/latest/userguide/security-encryption.md#security-encryption-authz "../../../secretsmanager/latest/userguide/security-encryption.md#security-encryption-authz") in the _AWS Secrets Manager User
Guide_.

In the following policy, replace `applicationId`
with the ID for your application.

**Resource policy for the secret**

You must include the following permissions in the resource policy for the secret in
AWS Secrets Manager to allow EMR Serverless to retrieve secret values. To ensure that only a specific
application can retrieve this secret, you can optionally specify the EMR Serverless application ID
as a condition in the policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue",
 "secretsmanager:DescribeSecret"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:SourceArn": "arn:aws:emr-serverless:*:123456789012:/applications/*"
 }
 },
 "Sid": "AllowSECRETSMANAGERGetsecretvalue"
 }
 ]
}`

```

Create your secret with the following policy for the customer-managed AWS Key Management Service (AWS KMS)
key:

**Policy for customer-managed AWS KMS key**

```
{
    "Sid": "Allow EMR Serverless to use the key for decrypting secrets",
    "Effect": "Allow",
    "Principal": {
        "Service": [
            "emr-serverless.amazonaws.com"
        ]
    },
    "Action": [
        "kms:Decrypt",
        "kms:DescribeKey"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "kms:ViaService": "secretsmanager.`AWS Region`.amazonaws.com"
        }
    }
}

```

## Rotating the secret

_Rotation_ is when you periodically update a secret. You can configure
AWS Secrets Manager to automatically rotate the secret for you on a schedule that you specify. This way,
you can replace long-term secrets with short-term ones. This helps to reduce the risk of
compromise. EMR Serverless retrieves the secret value from an annotated configuration when the job
transitions to a running state. If you or a process updates the secret value in Secrets Manager, you
must submit a new job so that the job can fetch the updated value.

###### Note

Jobs that are already in a running state can't fetch an updated secret value. This might
result in job failure.
