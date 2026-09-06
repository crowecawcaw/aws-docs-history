

# AWS zero-ETL integration for self-managed database sources
<a name="zero-etl"></a>

AWS zero-ETL integration is a fully managed solution that makes transactional and operational data available in Amazon Redshift, Amazon S3, and Amazon S3 Tables from multiple operational and transactional database sources. Using zero-ETL, you can replicate data from your self-managed source databases such as MySQL, PostgreSQL, SQL Server, and Oracle to Amazon Redshift through existing AWS Database Migration Service (AWS DMS) source endpoints. The automatic synchronization avoids the traditional extract, transform, and load (ETL) process. It also enables real-time analytics and AI workloads. For more information, see [zero-ETL integrations](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.html) in the *Amazon Redshift Management Guide*. 

Zero-ETL integration provides the following benefits:
+  **Real-time data replication** – Continuous data synchronization from Oracle databases to Amazon Redshift with minimal latency. 
+  **Elimination of complex ETL pipelines** – No need to build and maintain custom data integration solutions. 
+  **Reduced operational overhead** – Automated setup and management through AWS APIs. 
+  **Simplified data integration architecture** – Seamless integration between self-managed databases and AWS analytics services. 
+  **Enhanced security** – Built-in encryption and IAM access controls. 

## How zero-ETL integration works for self-managed database sources
<a name="zero-etl.how-it-works"></a>

You can use existing AWS DMS endpoints previously created for self-managed databases or create new ones.
+ Use the AWS Glue console or [CLI](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-integrations.html) to create the zero-ETL integration with Amazon Redshift as a target in the AWS Glue catalog. You can specify schema and table filter when creating zero-ETL integrations. 
+ Additional read-only resources related to the integrations are automatically created within the AWS DMS service. These resources including the zero-ETL engine are used to initiate full load and continuous data change processes, to sync up data with the Amazon Redshift target database. 
+ You control the encryption of your data when you create the integration source, when you create the zero-ETL integration, and when you create the Amazon Redshift data warehouse. 
+ The integration monitors the health of the data pipeline and recovers from issues when possible. 
+ You can create integrations from sources of the same type into a single Amazon Redshift data warehouse to derive holistic insights across multiple applications. 

Once the data is replicated you can use the analytics capabilities of Amazon Redshift. For example, built-in machine learning (ML), materialized views, data sharing, and direct access to multiple data stores and data lakes. For data engineers, zero-ETL integrations provide access to time-sensitive data that otherwise can get delayed by intermittent errors in complex data pipelines. You can run analytical queries and ML models on transactional data to derive timely insights for time-sensitive events and business decisions. 

You can create an Amazon Redshift event notification subscriptions to be automatically notified when issues occur for any zero-ETL integration. To view the list of integration-related event notifications, see [Zero-ETL integration event notifications with Amazon EventBridge](https://docs.aws.amazon.com/redshift/latest/mgmt/integration-event-notifications.html). The simplest way to create a subscription is with the Amazon Simple Notification Service console. For information on creating an Amazon SNS topic and subscribing to it, see [Getting started with Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html) in the *Amazon Simple Notification Service Developer Guide*. 

## Source database configuration before creating integration
<a name="zero-etl.source-database-configuration"></a>

Before configuring zero-ETL integrations, you must properly configure your source database according to the requirements for your database engine. Each engine has specific configuration requirements and limitations. 

SQL Server
+ For configuration requirements, see [Using a Microsoft SQL Server database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html). 
+ For change data capture (CDC) requirements, see [Capturing data changes for ongoing replication from SQL Server](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.CDC.html). 

**Note**  
RDS SQL Server and Azure SQL Server cannot be used as sources for self-managed zero-ETL integrations.

Oracle
+ For configuration requirements and limitations, see [Using an Oracle database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html). 

MySQL
+ For configuration requirements and limitations, see [Using a MySQL-compatible database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html). 

PostgreSQL
+ For configuration requirements and limitations, see [Using a PostgreSQL database as an AWS DMS source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html). 

## Setting up IAM permissions and encryption for zero-ETL integration
<a name="zero-etl.iam-setup"></a>

To create and manage zero-ETL integrations, you need to configure appropriate IAM permissions, AWS Key Management Service (AWS KMS) encryption keys, and resource policies. This section provides guidance on setting up the required security components. 

### Prerequisites
<a name="zero-etl.iam-setup.prerequisites"></a>

Before creating a zero-ETL integration, ensure you have the following:
+ An IAM user or role with appropriate permissions to create and manage integrations
+ Configure AWS DMS source endpoints for your self-managed databases. For more information, see [Source database configuration before creating integration](#zero-etl.source-database-configuration).
+ An Amazon Redshift provisioned cluster as the target
**Note**  
Amazon Redshift Serverless cannot be used as a target for zero-ETL integrations from self-managed sources.
+ Network configuration including VPC subnets and security groups

### Creating a KMS key
<a name="zero-etl.iam-setup.kms-key"></a>

First, create a customer managed AWS KMS key to encrypt data in your zero-ETL integration. The following example creates a symmetric encryption key: 

```
aws kms create-key \
  --description "On-prem Zero-ETL Integration Encryption Key" \
  --key-usage ENCRYPT_DECRYPT \
  --key-spec SYMMETRIC_DEFAULT \
  --region {{region}}
```

Note the `KeyId` and `Arn` from the response, as you will need them when configuring the key policy and creating the integration. 

Example output:

```
{
    "KeyMetadata": {
        "AWSAccountId": "{{account-id}}",
        "KeyId": "4e2c14f8-7abe-4aec-851a-379f6ed973a8",
        "Arn": "arn:aws:kms:{{region}}:{{account-id}}:key/4e2c14f8-7abe-4aec-851a-379f6ed973a8",
        "CreationDate": 1763155061.148,
        "Enabled": true,
        "Description": "Zero-ETL Integration Encryption Key",
        "KeyUsage": "ENCRYPT_DECRYPT",
        "KeyState": "Enabled",
        "Origin": "AWS_KMS",
        "KeyManager": "CUSTOMER",
        "CustomerMasterKeySpec": "SYMMETRIC_DEFAULT",
        "KeySpec": "SYMMETRIC_DEFAULT",
        "EncryptionAlgorithms": [
            "SYMMETRIC_DEFAULT"
        ],
        "MultiRegion": false
    }
}
```

### Configuring the KMS key policy
<a name="zero-etl.iam-setup.kms-policy"></a>

After creating the KMS key, configure the key policy to allow Amazon Redshift and AWS Glue services to use the key for encryption and decryption operations. The key policy must grant the necessary permissions to the service principals and include the encryption context that will be used during integration creation. 

The following example shows a key policy for zero-ETL integrations:

```
{
    "Version": "2012-10-17",		 	 	 
    "Id": "key-default-1",
    "Statement": [
        {
            "Sid": "Enable IAM User Permissions",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{111122223333}}:root"
            },
            "Action": "kms:*",
            "Resource": "*"
        },
        {
            "Sid": "Allows the Redshift and glue service principal to add a grant to a KMS key",
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "redshift.amazonaws.com",
                    "glue.amazonaws.com"
                ]
            },
            "Action": "kms:CreateGrant",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
	              "kms:EncryptionContext:{{context-key}}": "{{context-value}}"
                },
                "ForAllValues:StringEquals": {
                    "kms:GrantOperations": [
                        "Decrypt",
                        "GenerateDataKey",
                        "CreateGrant",
                        "GenerateDataKeyWithoutPlaintext",
                        "ReEncryptTo"
                    ]
                }
            }
        }
    ]
}
```

The `kms:EncryptionContext` condition must match the additional encryption context you specify when creating the integration. You can update the key policy using the AWS KMS console or the following CLI command: 

```
aws kms put-key-policy \
  --key-id {{key-id}} \
  --policy-name default \
  --policy file://kms-key-policy.json
```

### Creating an IAM user and configuring AWS CLI
<a name="zero-etl.iam-setup.user-setup"></a>

Create an IAM user that will be used to manage zero-ETL integrations and configure the AWS CLI with appropriate credentials. 

1. Create an IAM user:

   ```
   aws iam create-user --user-name {{cli-user}}
   ```

1. Create access keys for the user:

   ```
   aws iam create-access-key --user-name {{cli-user}}
   ```

   Save the `AccessKeyId` and `SecretAccessKey` from the output, as you will need them to configure the AWS CLI. 

### Creating and attaching an IAM policy
<a name="zero-etl.iam-setup.iam-policy"></a>

Create an IAM policy that grants permissions for zero-ETL integration operations. The policy should include permissions for AWS Glue, AWS DMS, Amazon Redshift, AWS KMS, and . 

Save the following policy to a file (for example, `/tmp/zetl-policy.json`):

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "ZetlGlueIntegrationAccess",
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
            "Sid": "DMSIntegrationAccess",
            "Effect": "Allow",
            "Action": [
                "dms:CreateOutboundIntegration",
                "dms:ModifyOutboundIntegration",
                "dms:CreateEndpoint",
                "dms:DescribeEndpoints",
                "dms:ModifyEndpoint",
                "dms:DeleteEndpoint",
                "dms:TestConnection"
            ],
            "Resource": "*"
        },
        {
            "Sid": "ZetlRedshiftFullAccess",
            "Effect": "Allow",
            "Action": [
                "redshift:*",
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
            "Sid": "ZetlRedshiftDataAPI",
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
            "Sid": "ZetlKMSAccess",
            "Effect": "Allow",
            "Action": [
                "kms:CreateKey",
                "kms:DescribeKey",
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:GenerateDataKey",
                "kms:ListKeys",
                "kms:CreateAlias",
                "kms:ListAliases",
                "kms:CreateGrant"
            ],
            "Resource": "*"
        },
        {
            "Sid": "ZetlSecretsManagerAccess",
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
}
```

Create the policy and attach it to the IAM user:

```
aws iam create-policy \
  --policy-name ZetlCustomPolicy \
  --policy-document file:///tmp/zetl-policy.json

aws iam attach-user-policy \
  --policy-arn arn:aws:iam::{{account-id}}:policy/ZetlCustomPolicy \
  --user-name {{cli-user}}
```

### Configuring the AWS CLI profile
<a name="zero-etl.iam-setup.cli-config"></a>

Configure an AWS CLI profile with the user credentials created in the previous steps:

```
aws configure set aws_access_key_id {{ACCESS_KEY_ID}} --profile {{cli-user}}
aws configure set aws_secret_access_key {{SECRET_ACCESS_KEY}} --profile {{cli-user}}
aws configure set region {{region}} --profile {{cli-user}}
aws configure set output json --profile {{cli-user}}
```

Test the profile configuration:

```
aws sts get-caller-identity --profile {{cli-user}}
```

The output should display the user's account ID, user ID, and ARN, confirming that the profile is configured correctly. 

### Creating a Redshift resource policy
<a name="zero-etl.iam-setup.resource-policy"></a>

Create an Amazon Redshift resource policy to authorize the AWS DMS source endpoint to create inbound integrations with your Amazon Redshift namespace. This policy is attached to the Amazon Redshift namespace and controls which sources can replicate data into it. 

The following example shows how to create a resource policy for an Amazon Redshift namespace:

```
aws redshift put-resource-policy \
  --policy '{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
          "Service": ["redshift.amazonaws.com"]
        },
        "Action": ["redshift:AuthorizeInboundIntegration"],
        "Resource": "arn:aws:redshift:{{region}}:{{account-id}}:namespace:{{namespace-id}}",
        "Condition": {
          "StringEquals": {
            "aws:SourceArn": "arn:aws:dms:{{region}}:{{account-id}}:endpoint:{{endpoint-id}}"
          }
        }
      },
      {
        "Effect": "Allow",
        "Principal": {
          "AWS": "{{account-id}}"
        },
        "Action": [
          "redshift:CreateInboundIntegration",
          "redshift:ModifyInboundIntegration"
        ],
        "Resource": "arn:aws:redshift:{{region}}:{{account-id}}:namespace:{{namespace-id}}"
      }
    ]
  }' \
  --resource-arn arn:aws:redshift:{{region}}:{{account-id}}:namespace:{{namespace-id}} \
  --region {{region}}
```

Replace the following placeholders:
+  {{region}} – The AWS region where your resources are located 
+  {{account-id}} – Your AWS account ID 
+  {{endpoint-id}} – The ID of your AWS DMS source endpoint 
+  {{namespace-id}} – The ID of your Amazon Redshift namespace 

### Example: Creating a zero-ETL integration with encryption
<a name="zero-etl.iam-setup.example"></a>

After setting up the necessary permissions and encryption keys, you can create a zero-ETL integration using the AWS Glue API. The following example demonstrates creating an integration from a MySQL source to an Amazon Redshift target with KMS encryption: 

```
aws glue create-integration \
  --integration-name {{mysql-onprem-integration}} \
  --source-arn arn:aws:dms:{{region}}:{{account-id}}:endpoint:{{source-endpoint-id}} \
  --target-arn arn:aws:redshift:{{region}}:{{account-id}}:namespace:{{namespace-id}} \
  --description "MySQL to Redshift integration" \
  --integration-config '{"SourceProperties":{"SubnetIds":"{{subnet-id1,subnet-id2,subnet-id3}}","VpcSecurityGroupIds":"{{sg-id}}"}}' \
  --data-filter "include: {{mysql}}.*" \
  --kms-key-id arn:aws:kms:{{region}}:{{account-id}}:key/{{key-id}} \
  --additional-encryption-context '{"{{context-key}}": "{{context-value}}"}' \
  --profile {{cli-user}} \
  --region {{region}}
```

The command includes the following key parameters:
+  `--integration-name` – A unique name for your integration 
+  `--source-arn` – The ARN of your AWS DMS source endpoint 
+  `--target-arn` – The ARN of your Amazon Redshift namespace 
+  `--integration-config` – Network configuration including subnet IDs and security groups 
+  `--data-filter` – Specifies which schemas and tables to replicate 
+  `--kms-key-id` – The ARN of the AWS KMS key for encryption 
+  `--additional-encryption-context` – Encryption context key-value pairs that must match the KMS key policy (e.g., `{"{{context-key}}": "{{context-value}}"}`) 
+  `--profile` – The AWS CLI profile to use (the cli-user profile created earlier) 

Upon successful creation, the command returns the integration details including the integration ARN, status, and configuration parameters. Example output: 

```
{
    "SourceArn": "arn:aws:dms:{{region}}:{{account-id}}:endpoint:{{endpoint-id}}",
    "TargetArn": "arn:aws:redshift:{{region}}:{{account-id}}:namespace:{{namespace-id}}",
    "IntegrationName": "mysql-onprem-integration",
    "IntegrationArn": "arn:aws:glue:{{region}}:{{account-id}}:integration:{{integration-id}}",
    "KmsKeyId": "arn:aws:kms:{{region}}:{{account-id}}:key/{{key-id}}",
    "AdditionalEncryptionContext": {
	  "{{context-key}}": "{{context-value}}"
    },
    "Status": "CREATED",
    "CreateTime": 1763234086.001,
    "DataFilter": "include: mysql.*",
    "IntegrationConfig": {
        "SourceProperties": {
            "SubnetIds": "subnet-id1,subnet-id2,subnet-id3",
            "VpcSecurityGroupIds": "sg-id"
        }
    }
}
```

### Security best practices
<a name="zero-etl.iam-setup.best-practices"></a>

Follow these security best practices when setting up zero-ETL integrations:
+  **Use least privilege access** – Grant only the minimum permissions required for creating and managing integrations. Consider using resource-level permissions where possible. 
+  **Enable encryption** – Always use customer managed AWS KMS keys to encrypt integration data. Specify encryption context for additional security. 
+  **Rotate credentials regularly** – If using IAM user access keys, rotate them regularly. Consider using IAM roles with temporary credentials instead. 
+  **Monitor access** – Use AWS CloudTrail to monitor API calls related to integration creation and management. 
+  **Restrict network access** – Configure VPC security groups to limit network access to only required resources. 
+  **Use resource policies** – Implement Amazon Redshift resource policies to control which sources can create integrations with your data warehouse. 
+  **Tag resources** – Apply tags to integrations and related resources for better organization and cost tracking. 