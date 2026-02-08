# Setting up Oracle Database@AWS integrations with Amazon Redshift

To set up zero-ETL integration between your Oracle database and Amazon Redshift, complete the following
steps:

1. Enable Zero-ETL on your ODB network.
2. Configure Oracle database prerequisites.
3. Set up AWS Secrets Manager and AWS Key Management Service.
4. Configure IAM permissions.
5. Set up Amazon Redshift resource policies.
6. Create the zero-ETL integration.
7. Create the target database in Amazon Redshift.

## Step 1: Enable Zero-ETL for your ODB network

You can enable the zero-ETL integration for the ODB network associated with your source VM cluster. By
default, this integration is disabled.

###### To enable zero-ETL integration

1. Open the Oracle Database@AWS console at [https://console.aws.amazon.com/odb/](https://console.aws.amazon.com/odb/ "https://console.aws.amazon.com/odb/").
2. In the navigation pane, choose **ODB networks**.
3. Select the ODB network for which you want to enable the zero-ETL integration.
4. Choose **Modify**.
5. Select **Zero-ETL**.
6. Choose **Continue** and then **Modify**.
   To enable the zero-ETL integration, use the `update-odb-network` command with
   the `--zero-etl-access` parameter:

```
aws odb update-odb-network \
  --odb-network-id `odb-network-id` \
  --zero-etl-access ENABLED
```

To enable zero-ETL integration for the ODB network associated with your source VM cluster, use the
`update-odb-network` command. This command configures the network infrastructure
required for zero-ETL integration.

```
aws odb update-odb-network \
  --odb-network-id `your-odb-network-id` \
  --zero-etl-access ENABLED
```

## Step 2: Configure your Oracle database

Complete the Oracle database configuration as described in the [Prerequisites](zero-etl-prerequisites.md "zero-etl-prerequisites.md"):

- Create replication users and grant necessary permissions.
- Enable archived redo logs.
- Configure SSL (Oracle Exadata only).
- Set up ASM users if applicable (Oracle Exadata only).

## Step 3: Set up AWS Secrets Manager and AWS Key Management Service

Create a Customer Managed Key (CMK) and store your database credentials.

1. Create a CMK in AWS Key Management Service using the `create-key` command.

```
aws kms create-key \
  --description "ODB Zero-ETL Integration Key" \
  --key-usage ENCRYPT_DECRYPT \
  --key-spec SYMMETRIC_DEFAULT
```

2. Store your database credentials in AWS Secrets Manager.

```
aws secretsmanager create-secret \
  --name "ODBZeroETLCredentials" \
  --description "Credentials for Oracle Database@AWS Zero-ETL integration" \
  --kms-key-id `your-cmk-key-arn` \
  --secret-string file://secret-content.json
```

3. Attach a resource policy to the secret to allow Oracle Database@AWS access.

```
aws secretsmanager put-resource-policy \
  --secret-id "ODBZeroETLCredentials" \
  --resource-policy file://secret-resource-policy.json
```

In the preceding command, `secret-resource-policy.json` contains the
following JSON.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "zetl.odb.amazonaws.com"
 },
 "Action": [
 "secretsmanager:GetSecretValue",
 "secretsmanager:DescribeSecret"
 ],
 "Resource": "*"
 }
 ]
}`

```

4. Attach a resource policy to the CMK. The CMK resource policy must include permissions
   for both the Oracle Database@AWS service principal and the Amazon Redshift service principal to support encrypted
   Zero-ETL integration.

```
aws kms put-key-policy \
  --key-id `your-cmk-key-arn` \
  --policy-name default \
  --policy file://cmk-resource-policy.json
```

The `cmk-resource-policy.json` file should include the following policy
statements. The first statement allows Oracle Database@AWS service access, and the second statement
allows Amazon Redshift to create grants on the KMS key for encrypted data operations.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow ODB service access",
 "Effect": "Allow",
 "Principal": {
 "Service": "zetl.odb.amazonaws.com"
 },
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey",
 "kms:CreateGrant"
 ],
 "Resource": "*"
 },
 {
 "Sid": "Allows the Redshift service principal to add a grant to a KMS key",
 "Effect": "Allow",
 "Principal": {
 "Service": "redshift.amazonaws.com"
 },
 "Action": "kms:CreateGrant",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:EncryptionContext:{context-key}": "{context-value}"
 },
 "ForAllValues:StringEquals": {
 "kms:GrantOperations": [
 "Decrypt",
 "GenerateDataKey",
 "CreateGrant"
 ]
 }
 }
 }
 ]
}`

```

## Step 4: Configure IAM permissions

Create and attach IAM policies that allow zero-ETL integration operations.

```
aws iam create-policy \
  --policy-name "ODBZeroETLIntegrationPolicy" \
  --policy-document file://odb-zetl-iam-policy.json

aws iam attach-user-policy \
  --user-name `your-iam-username` \
  --policy-arn `policy-arn`
```

The following policy grants the necessary permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ODBGlueIntegrationAccess",
 "Effect": "Allow",
 "Action": [
 "glue:CreateIntegration",
 "glue:ModifyIntegration",
 "glue:DeleteIntegration",
 "glue:DescribeIntegrations",
 "glue:DescribeInboundIntegrations"
 ],
 "Resource": "*"
 },
 {
 "Sid": "ODBZetlOperations",
 "Effect": "Allow",
 "Action": "odb:CreateOutboundIntegration",
 "Resource": "*"
 },
 {
 "Sid": "ODBRedshiftFullAccess",
 "Effect": "Allow",
 "Action": [
 "redshift:*",
 "redshift-serverless:*",
 "ec2:DescribeAccountAttributes",
 "ec2:DescribeAddresses",
 "ec2:DescribeAvailabilityZones",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs",
 "ec2:DescribeInternetGateways",
 "sns:CreateTopic",
 "sns:Get*",
 "sns:List*",
 "cloudwatch:Describe*",
 "cloudwatch:Get*",
 "cloudwatch:List*",
 "cloudwatch:PutMetricAlarm",
 "cloudwatch:EnableAlarmActions",
 "cloudwatch:DisableAlarmActions",
 "tag:GetResources",
 "tag:UntagResources",
 "tag:GetTagValues",
 "tag:GetTagKeys",
 "tag:TagResources"
 ],
 "Resource": "*"
 },
 {
 "Sid": "ODBRedshiftDataAPI",
 "Effect": "Allow",
 "Action": [
 "redshift-data:ExecuteStatement",
 "redshift-data:CancelStatement",
 "redshift-data:ListStatements",
 "redshift-data:GetStatementResult",
 "redshift-data:DescribeStatement",
 "redshift-data:ListDatabases",
 "redshift-data:ListSchemas",
 "redshift-data:ListTables",
 "redshift-data:DescribeTable"
 ],
 "Resource": "*"
 },
 {
 "Sid": "ODBKMSAccess",
 "Effect": "Allow",
 "Action": [
 "kms:CreateKey",
 "kms:DescribeKey",
 "kms:Encrypt",
 "kms:Decrypt",
 "kms:GenerateDataKey",
 "kms:ListKeys",
 "kms:CreateAlias",
 "kms:ListAliases"
 ],
 "Resource": "*"
 },
 {
 "Sid": "ODBSecretsManagerAccess",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue",
 "secretsmanager:PutSecretValue",
 "secretsmanager:CreateSecret",
 "secretsmanager:UpdateSecret",
 "secretsmanager:DeleteSecret",
 "secretsmanager:DescribeSecret",
 "secretsmanager:ListSecrets",
 "secretsmanager:GetResourcePolicy",
 "secretsmanager:PutResourcePolicy",
 "secretsmanager:ValidateResourcePolicy"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Step 5: Configure Amazon Redshift resource policies

Set up resource policies on your Amazon Redshift cluster to authorize inbound integrations.

```
aws redshift put-resource-policy \
  --no-verify-ssl \
  --resource-arn "`your-redshift-cluster-arn`" \
  --policy '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
          "Service": "redshift.amazonaws.com"
        },
        "Action": [
          "redshift:AuthorizeInboundIntegration"
        ],
        "Condition": {
          "StringEquals": {
            "aws:SourceArn": "`your-vm-cluster-arn`"
          }
        }
      },
      {
        "Effect": "Allow",
        "Principal": {
          "AWS": "`your-account-id`"
        },
        "Action": [
          "redshift:CreateInboundIntegration"
        ]
      }
    ]
  }' \
  --region us-west-2
```

###### Tip

Alternatively, you can use the **Fix it for me** option in the AWS
console. This option automatically configures the required Amazon Redshift policies without your
needing to do it manually.

## Step 6: Create the zero-ETL integration using

AWS Glue

Create the zero-ETL integration using the AWS Glue `create-integration`
command. In this command, you specify the source VM cluster and the target Amazon Redshift
namespace.

The following example creates an integration with a PDB named `pdb1` running in
an Exadata VM cluster. You can also create an Autonomous VM cluster by replacing `cloud-vm-cluster`
with `cloud-autonomous-vm-cluster` in the source ARN. Specifying a KMS key is
optional. If you specify a key, it can be different from the one that you created in [Step 3: Set up AWS Secrets Manager and AWS Key Management Service](#zero-etl-setup-secrets "#zero-etl-setup-secrets").

```
aws glue create-integration \
  --integration-name "MyODBZeroETLIntegration" \
  --source-arn "arn:aws:odb:`region`:`account`:cloud-vm-cluster/`cluster-id`" \
  --target-arn "arn:aws:redshift:`region:account`:namespace/`namespace-id`" \
  --data-filter "include: `pdb1`.*.*" \
  --integration-config '{
      "RefreshInterval": "10",
      "IntegrationMode": "DEFAULT",
      "SourcePropertiesMap": {
        "secret-arn": "arn:aws:secretsmanager:`region`:`account`:secret:`secret-name`"
      }
    }' \
  --description "Zero-ETL integration for Oracle to Amazon Redshift" \
  --kms-key-id "arn:aws:kms:`region:account`:key/`key-id`"
```

The command returns an integration ARN and sets the status to `creating`. You
can monitor the integration status using the `describe-integrations`
command.

```
aws glue describe-integrations \
  --integration-identifier `integration-id`
```

###### Important

Only one PDB per integration is supported. The data filter must specify a single PDB,
for example, `include: pdb1.*.*`. The source must be in the same AWS Region and
account in which the integration is being created.

## Step 7: Create a target database in

Amazon Redshift

After the integration is active, create a target database in your Amazon Redshift cluster.

```
-- Connect to your Amazon Redshift cluster
psql -h `your-redshift-endpoint` -U `username` -d `database`

-- Create database from integration
CREATE DATABASE `target_database_name`
FROM INTEGRATION '`integration-id`'
DATABASE "`source_pdb_name`";
```

After creating the target database, you can query the replicated data.

```
-- List databases to verify creation
\l

-- Connect to the new database
\c `target_database_name`

-- List tables to see replicated data
\dt
```

## Verify the zero-ETL integration

Verify that the integration works by querying the integration status in AWS Glue and making
sure that your Oracle changes are being replicated to Amazon Redshift.

###### To verify that your zero-ETL integration is working correctly

1. Check the integration status.

```
aws glue describe-integrations \
  --integration-identifier `integration-id`
```

The status should be `ACTIVE` or `REPLICATING`. 2. Verify data replication by making changes in your Oracle database and checking that
they appear in Amazon Redshift. 3. Monitor replication metrics in Amazon CloudWatch (if available).
