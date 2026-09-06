

# Configuring a target for a zero-ETL integration
<a name="zero-etl-target"></a>

There are several options offered by AWS Glue when configuring a target for a zero-ETL integration. The target may be an encrypted Amazon Redshift data warehouse or a Lakehouse architecture of Amazon SageMaker.

Before selecting the target for the zero-ETL integration, you need to configure one of the following target resources. The configuration options for a target in a zero-ETL integration include:
+ A general purpose Amazon S3 bucket using the lakehouse architecture of Amazon SageMaker. See [Configuring a general purpose S3 bucket target](#zero-etl-config-target-regular-s3).
+ An Amazon S3 Tables bucket using the lakehouse architecture of Amazon SageMaker. See [Configuring an Amazon S3 Tables bucket target](#zero-etl-config-target-s3-tables).
+ An Amazon Redshift Managed Storage using the lakehouse architecture of Amazon SageMaker. See [Configuring an Amazon Redshift Managed Storage target](#zero-etl-config-target-redshift-managed-storage).
+ An Amazon Redshift data warehouse identified by a Redshift namespace. See [Configuring an Amazon Redshift data warehouse target](#zero-etl-config-target-redshift-data-warehouse).

**Note**  
You cannot modify the target of a zero-ETL integration after creation.

## Configuring a general purpose S3 bucket target
<a name="zero-etl-config-target-regular-s3"></a>

This section describes the prerequisites and setup steps for configuring a general purpose S3 bucket as storage for your target in a zero-ETL integration, using the Lakehouse architecture of Amazon SageMaker.

Before creating a zero-ETL integration with the Lakehouse architecture of Amazon SageMaker using general purpose S3 storage, you need to complete the following setup tasks:
+ Set up an AWS Glue database
+ Provide Catalog RBAC policy
+ Create target IAM role
+ Associate target role, KMS (optional) and Connection (optional) with target resource
+ (Optional) Configure target table properties

### Setting up an AWS Glue database
<a name="zero-etl-config-target-s3-glue-database"></a>

To set up a target database in the Data Catalog with an Amazon S3 general purpose bucket location:

1. In the AWS Glue console home page, select **Database** under Data Catalog.

1. Choose **Add database** in the top right corner. If you have already created a database, make sure that the location with Amazon S3 URI is set for the database.

1. Enter a name and **Location** (Amazon S3 URI). Note that the location is required for the zero-ETL integration. Click **Create database** when done.

**Note**  
The general purpose Amazon S3 bucket must be in the same region as the AWS Glue database.

For information on creating a new database in AWS Glue, see [Getting started with the Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/start-data-catalog.html).

You can also use the [`create-database`](https://docs.aws.amazon.com/cli/latest/reference/glue/create-database.html) CLI to create the database in AWS Glue. Note that the `LocationUri` in `--database-input` is required.

#### Optimizing Iceberg tables
<a name="zero-etl-config-target-s3-iceberg-optimization"></a>

Once a table is created by AWS Glue in the target database, you can enable the compaction to speed up queries in Amazon Athena. For information on setting up the resources (IAM Role) for compaction, see [Table optimization prerequisites](https://docs.aws.amazon.com/glue/latest/dg/optimization-prerequisites.html).

For more information on setting up compaction on the AWS Glue table created by the integration, see [Optimizing Iceberg tables](https://docs.aws.amazon.com/glue/latest/dg/table-optimizers.html).

### Providing a catalog Resource Based Access (RBAC) policy
<a name="zero-etl-config-target-s3-rbac-policy"></a>

For integrations that use an AWS Glue database, add the following permissions to the catalog RBAC Policy to allow for integrations between source and target.

**Note**  
For cross-account integrations, both the user creating the integration role policy and catalog resource policy need to allow `glue:CreateInboundIntegration` on the resource. For same-account, either a resource policy or role policy allowing `glue:CreateInboundIntegration` on the resource is sufficient. Both scenarios do still need to allow `glue.amazonaws.com` to `glue:AuthorizeInboundIntegration`.

You can access the **Catalog settings** under **Data Catalog**. Then provide the following permissions and fill in the missing information.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Principal": {
        "AWS": [
            "arn:aws:iam::123456789012:user/{{Alice}}"
        ]
      },
      "Effect": "Allow",
      "Action": [
        "glue:CreateInboundIntegration"
      ],
      "Resource": [
          "arn:aws:glue:us-east-1:111122223333:catalog",
          "arn:aws:glue:us-east-1:111122223333:database/{{database-name}}"
      ],
      "Condition": {
        "StringLike": {
        "aws:SourceArn": "arn:aws:dynamodb:us-east-1:444455556666:table/{{table-name}}"
        }
      }
    },
    {
      "Principal": {
        "Service": [
          "glue.amazonaws.com"
        ]
      },
      "Effect": "Allow",
      "Action": [
        "glue:AuthorizeInboundIntegration"
      ],
      "Resource": [
          "arn:aws:glue:us-east-1:111122223333:catalog",
          "arn:aws:glue:us-east-1:111122223333:database/{{database-name}}"
      ],
      "Condition": {
        "StringEquals": {
        "aws:SourceArn": "arn:aws:dynamodb:us-east-1:444455556666:table/{{table-name}}"
        }
      }
    }
  ]
}
```

### Creating a target IAM role
<a name="zero-etl-config-target-s3-iam-role"></a>

Create a target IAM role with the following permissions and trust relationships:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::{{amzn-s3-bucket}}",
            "Effect": "Allow"
        },
        {
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject"
            ],
            "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}/prefix/*",
            "Effect": "Allow"
        },
        {
            "Action": [
                "glue:GetDatabase"
            ],
            "Resource": [
                "arn:aws:glue:us-east-1:111122223333:catalog",
                "arn:aws:glue:us-east-1:111122223333:database/{{database-name}}"
            ],
            "Effect": "Allow"
        },
        {
            "Action": [
                "glue:CreateTable",
                "glue:GetTable",
                "glue:GetTables",
                "glue:DeleteTable",
                "glue:UpdateTable",
                "glue:GetTableVersion",
                "glue:GetTableVersions",
                "glue:GetResourcePolicy"
            ],
            "Resource": [
                "arn:aws:glue:us-east-1:111122223333:catalog",
                "arn:aws:glue:us-east-1:111122223333:database/{{database-name}}",
                "arn:aws:glue:us-east-1:111122223333:table/{{database-name}}/*"
            ],
            "Effect": "Allow"
        },
        {
            "Action": [
                "cloudwatch:PutMetricData"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "cloudwatch:namespace": "AWS/Glue/ZeroETL"
                }
            },
            "Effect": "Allow"
        },
        {
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "*",
            "Effect": "Allow"
        }
    ]
}
```

Add the following trust policy to allow the AWS Glue service to assume the role:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "glue.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

### Associate target role, KMS (optional) and Connection (optional) with target resource
<a name="zero-etl-config-target-s3-associate-role"></a>

Associate the above target role with the target resource i.e. AWS Glue Database. Optionally, KMS for encrypting the data before storing in target iceberg table and Connection ARN for accessing the S3 bucket can be configured for the target AWS Glue database. This will allow AWS Glue to access data on the target S3 location using the provided role and optionally encrypt using the provided KMS key. If the target S3 bucket is configured to be accessible using a certain VPC, the connection ARN can be associated to allow AWS Glue to run the processing inside that VPC. For more information on setting up a VPC, see [Create a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html).

![The screenshot shows configuring a target in a zero-ETL integration.](http://docs.aws.amazon.com/glue/latest/dg/images/zero-etl-target-selection.png)


Or using the AWS Glue CLI / API:

```
aws glue create-integration-resource-property \
--resource-arn arn:aws:glue:us-east-1:123456789012:database/{{database-name}} \
--target-processing-properties '{"RoleArn": "arn:aws:iam::123456789012:role/{{gmi_target_role}}"}' \
--region us-east-1
```

### (Optional) Configure target table properties
<a name="zero-etl-config-target-s3-table-properties"></a>

Optionally, target table properties can be configured for the target tables that are going to be synced to the target.

You can configure these settings in the **Output settings** section of the integration creation workflow in the AWS Glue console:

![The screenshot shows the Output settings section with schema unnesting options, data partitioning options, and target table name configuration.](http://docs.aws.amazon.com/glue/latest/dg/images/zero-etl-output-settings-unnesting.png)


When you select **Specify custom partition keys**, you can configure partition keys and their function and conversion specs:

![The screenshot shows the Output settings with custom partition keys configuration and Partition Spec Configuration table.](http://docs.aws.amazon.com/glue/latest/dg/images/zero-etl-output-settings-partitioning.png)


If the source and target are in the same account, then this configuration can be done as part of integration creation workflow from the AWS Glue console UI. But if the target is in different account, then this configuration is required to be complete before creating the integration. When using the CLI or API, this should be done before invoking the Create-Integration API even when both source and target are in the same account. AWS Glue console UI just encapsulates this API call for the same account scenario.

If this is not configured, then default values will be used when syncing the table. This configuration can also be changed anytime after the integration creation as well.

**Note**  
If this property is updated after the integration is created, then it could trigger a full table resync when the updated configuration conflicts with the existing configuration. For example, updating the table "un-nesting" from 'No-Unnest' to 'Full-Unnest', or changing the partition column.

Using CLI or API:

```
aws glue create-integration-table-properties \
--resource-arn arn:aws:glue:us-east-1:123456789012:database/{{database-name}} \
--table-name {{table-name}} \
--target-table-config '{
        "UnnestSpec":"TOPLEVEL"|"FULL"|"NOUNNEST",
        "PartitionSpec":
            [
                {
                    "FieldName":"string",
                    "FunctionSpec":"string",
                    "ConversionSpec":"string"}
                    ...
             ],
         "TargetTableName":"string"
     }' \
--region us-east-1
```

After configuring the Lakehouse architecture of Amazon SageMaker with general purpose Amazon S3 bucket storage, you can proceed to [Configuring the integration with your target](#zero-etl-config-target-configuring-the-integration) to complete the integration setup.

## Configuring an Amazon S3 Tables bucket target
<a name="zero-etl-config-target-s3-tables"></a>

This section describes the prerequisites and setup steps for configuring Amazon S3 Tables as a target for your zero-ETL integration, using the lakehouse architecture of Amazon SageMaker.

Before creating a zero-ETL integration with Amazon S3 Tables as a target, you need to complete the following setup tasks:
+ Setup Amazon S3 tables bucket (and analytics services integration)
+ Provide Catalog RBAC policy
+ Create target IAM role
+ Associate target role, KMS (optional) and Connection (optional) with target resource
+ (Optional) Configure target table properties

### Setup Amazon S3 tables bucket (with analytics services integration)
<a name="zero-etl-config-target-s3-tables-setup"></a>

1. Create an S3 table bucket in your account by following the instructions at [Getting started with Amazon S3 Tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-getting-started.html).

1. Enable Analytics integrations with your S3-Table bucket by following these instructions: [Integrating AWS services with Amazon S3 Tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-aws.html).

1. This will create a new S3-Table Catalog in AWS Lake Formation.

### Provide Catalog RBAC Policy
<a name="zero-etl-config-target-s3-tables-rbac"></a>

The following permissions must be added to the Catalog RBAC Policy to allow for integrations between source and Amazon S3 tables catalog target.

Target AWS Glue Catalog resource policy needs to include AWS Glue Service permissions to `AuthorizeInboundIntegration`. Additionally, `CreateInboundIntegration` permission is required either on the source principal creating the integration or in the target AWS Glue resource policy.

**Note**  
For cross-account scenario, both source principal as well as target AWS Glue Catalog resource policy need to include `glue:CreateInboundIntegration` permissions on the resource.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Principal": {
        "AWS": [
            "arn:aws:iam::123456789012:user/Alice"
        ]
      },
      "Effect": "Allow",
      "Action": [
        "glue:CreateInboundIntegration"
      ],
      "Resource": [
          "arn:aws:glue:us-east-1:111122223333:catalog/{{s3tablescatalog}}/*"
      ],
      "Condition": {
        "StringLike": {
        "aws:SourceArn": "arn:aws:dynamodb:us-east-1:444455556666:table/{{table-name}}"
        }
      }
    },
    {
      "Principal": {
        "Service": [
          "glue.amazonaws.com"
        ]
      },
      "Effect": "Allow",
      "Action": [
        "glue:AuthorizeInboundIntegration"
      ],
      "Resource": [
      "arn:aws:glue:us-east-1:111122223333:catalog/{{s3tablescatalog}}/*"
      ],
      "Condition": {
        "StringEquals": {
        "aws:SourceArn": "arn:aws:dynamodb:us-east-1:444455556666:table/{{table-name}}"
        }
      }
    }
  ]
}
```

**Note**  
Replace `{{s3tablescatalog}}` with the parent catalog name of your S3 tables (if different). Default value (when hosting S3-Table Catalog in the same account) for this is `s3tablescatalog`.

### Create target IAM Role
<a name="zero-etl-config-target-s3-tables-iam-role"></a>

Create a target IAM role with the following permissions and trust relationships:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "s3tables:ListTableBuckets",
        "s3tables:GetTableBucket",
        "s3tables:GetTableBucketEncryption",
        "s3tables:GetNamespace",
        "s3tables:CreateNamespace",
        "s3tables:ListNamespaces",
        "s3tables:CreateTable",
        "s3tables:DeleteTable",
        "s3tables:GetTable",
        "s3tables:GetTableEncryption",
        "s3tables:ListTables",
        "s3tables:GetTableMetadataLocation",
        "s3tables:UpdateTableMetadataLocation",
        "s3tables:GetTableData",
        "s3tables:PutTableData"
      ],
      "Resource": "arn:aws:s3tables:us-east-1:111122223333:bucket/{{s3-table-bucket}}",
      "Effect": "Allow"
    },
    {
      "Action": [
        "cloudwatch:PutMetricData"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "cloudwatch:namespace": "AWS/Glue/ZeroETL"
        }
      },
      "Effect": "Allow"
    },
    {
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "*",
      "Effect": "Allow"
    }
  ]
}
```

Add the following trust policy in the target IAM role to allow AWS Glue Service to assume it:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "glue.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

**Note**  
Make sure there is no explicit DENY statement for this target IAM role in the S3-Tables bucket resource policy. An explicit DENY would override any ALLOW permissions and prevent the integration from working properly.

### Associate target role, KMS (optional) and Connection (optional) with target resource
<a name="zero-etl-config-target-s3-tables-associate-role"></a>

Associate the above target role with the target resource. Optionally, KMS for encrypting the data before storing in target iceberg table and Connection ARN for accessing target S3 bucket can be configured. If the target S3 bucket is configured to be accessible using a certain VPC, the connection ARN can be associated to allow AWS Glue to run the processing inside that VPC. For more information on setting up a VPC, see [Create a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html).

Using the AWS Glue CLI / API:

```
aws glue create-integration-resource-property \
--resource-arn arn:aws:glue:us-east-1:123456789012:catalog/s3tablescatalog/{{S3 table bucket name}} \
--target-processing-properties '{
                    "RoleArn": "arn:aws:iam::123456789012:role/{{target_role}}"
                }' \
--region us-east-1
```

### (Optional) Configure target table properties
<a name="zero-etl-config-target-s3-tables-table-properties"></a>

Optionally, target table properties can be configured for the target tables that are going to be synced to the target. The same rules apply as described in the general purpose S3 target section.

Using CLI or API:

```
aws glue create-integration-table-properties \
--resource-arn arn:aws:glue:us-east-1:123456789012:catalog/s3tablescatalog/{{S3 table bucket name}} \
--table-name {{table-name}} \
--target-table-config '' \
--region us-east-1
```

After configuring the Amazon S3-Tables storage using Lakehouse architecture of Amazon SageMaker, you can proceed to [Configuring the integration with your target](#zero-etl-config-target-configuring-the-integration) to complete the integration setup.

## Configuring an Amazon Redshift Managed Storage target
<a name="zero-etl-config-target-redshift-managed-storage"></a>

This section describes the prerequisites and setup steps for configuring an Amazon Redshift managed storage (RMS) as a target for your zero-ETL integration, using the lakehouse architecture of Amazon SageMaker.

Before creating a zero-ETL integration with a Lakehouse architecture of Amazon SageMaker using Redshift managed storage, you need to complete the following setup tasks:
+ Set up an Amazon Redshift cluster or Serverless workgroup
+ Register the Amazon Redshift integration with Lake Formation
+ Create a managed catalog in Lake Formation
+ Configure IAM permissions

### Setting up Amazon Redshift managed storage
<a name="zero-etl-config-target-rms-setup"></a>

To set up Amazon Redshift managed storage for your zero-ETL integration:
+ Create or use an existing Amazon Redshift cluster or Serverless workgroup. Make sure the target Amazon Redshift workgroup or cluster has the `enable_case_sensitive_identifier` parameter turned on for the integration to be successful. For more information on enabling case sensitivity, see [Turn on case sensitivity for your data warehouse](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-setting-up.case-sensitivity.html) in the Amazon Redshift management guide.
+ Register an integration from Redshift into the catalog in AWS Lake Formation. See [Registering Amazon Redshift clusters and namespaces to the Data Catalog](https://docs.aws.amazon.com/redshift/latest/dg/iceberg-integration-register.html).
+ Create a federated or managed catalog in AWS Lake Formation. For more information, see: 
  + [Bringing Amazon Redshift data into the Data Catalog](https://docs.aws.amazon.com/lake-formation/latest/dg/managing-namespaces-datacatalog.html)
  + [Creating an Amazon Redshift managed catalog in the Data Catalog](https://docs.aws.amazon.com/lake-formation/latest/dg/create-rms-catalog.html)
+ Configure IAM permissions for the target role. The role needs permissions to access both Redshift and Lake Formation resources. At minimum, the role should have: 
  + Permissions to access the Redshift cluster or workgroup
  + Permissions to access the Lake Formation catalog
  + Permissions to create and manage tables in the catalog
  + CloudWatch and CloudWatch Logs permissions for monitoring

After configuring the Amazon SageMaker Lakehouse catalog with Amazon Redshift managed storage, you can proceed to [Configuring the integration with your target](#zero-etl-config-target-configuring-the-integration) to complete the integration setup.

## Configuring an Amazon Redshift data warehouse target
<a name="zero-etl-config-target-redshift-data-warehouse"></a>

This section describes the prerequisites and setup steps for configuring an Amazon Redshift data warehouse as a target for your zero-ETL integration.

Before creating a zero-ETL integration with an Amazon Redshift data warehouse target, you need to complete the following setup tasks:
+ Set up an Amazon Redshift cluster or Serverless workgroup
+ Configure case sensitivity
+ Configure IAM permissions

### Setting up the Amazon Redshift data warehouse
<a name="zero-etl-config-target-redshift-setup"></a>

To set up an Amazon Redshift data warehouse for your zero-ETL integration:

1. Navigate to the [Amazon Redshift console](https://console.aws.amazon.com/redshiftv2/home) and click **Create cluster** or use an existing cluster. To create an Amazon Redshift cluster, see [Creating a cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/create-cluster.html). For Amazon Redshift Serverless, click **Create workgroup**. To create an Amazon Redshift Serverless workgroup, see [Creating a workgroup with a namespace](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-console-workgroups-create-workgroup-wizard.html).

1. If creating a new cluster, choose an appropriate cluster size and ensure your cluster is encrypted. For Serverless, configure the workgroup settings according to your requirements.

1. Make sure the target Amazon Redshift workgroup or cluster has the `enable_case_sensitive_identifier` parameter turned on for the integration to be successful. For more information on enabling case sensitivity, see [Turn on case sensitivity for your data warehouse](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-setting-up.case-sensitivity.html) in the Amazon Redshift management guide.

1. Configure IAM permissions to allow the zero-ETL integration to access your Amazon Redshift data warehouse. You'll need to create an IAM role with the following permissions: 
   + Permissions to access the Amazon Redshift cluster or workgroup
   + Permissions to create and manage databases and tables in Amazon Redshift
   + CloudWatch and CloudWatch Logs permissions for monitoring

1. After the Amazon Redshift workgroup or cluster setup is complete, you need to configure your data warehouse for zero-ETL integrations. See [Getting started with zero-ETL integrations](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.setting-up.html) in the Amazon Redshift Management Guide for more information.

**Note**  
When using a Amazon Redshift data warehouse as a target, the integration creates a schema in the specified database to store the replicated data. The schema name is derived from the integration name.

**Note**  
The target Amazon Redshift workgroup or cluster must have the `enable_case_sensitive_identifier` parameter turned on for the integration to be successful.

After configuring the Amazon Redshift data warehouse, you can proceed to [Configuring the integration with your target](#zero-etl-config-target-configuring-the-integration) to complete the integration setup.

## Configuring the integration with your target
<a name="zero-etl-config-target-configuring-the-integration"></a>

After configuring the source and target resources, follow these steps to complete the integration setup:

1. Navigate to "Zero-ETL integrations" page and start the integration creation workflow.

1. Select the source resource configured in the previous steps.

1. Select or specify the target resource (same account or cross account) configured in the previous steps.

1. Select the target IAM role configured previously.

1. Select the **Fix it for me** option (only available when the target is in same account). 
   + For the regular Amazon S3 (AWS Glue Database) and S3-Table (Catalog) target, this will: 
     + Apply an authorized service principal on the target Catalog resource policy.
     + Apply an authorized AWS Glue source Principal ARN to the target Catalog resource policy.
   + For the Amazon Redshift target, this will: 
     + Apply an authorized service principal on the Amazon Redshift cluster or Serverless workgroup.
     + Apply an authorized AWS Glue source ARN to the Amazon Redshift cluster or Serverless workgroup.
     + Associate a new parameter group with `enable_case_sensitive_identifier = true`.

Use the following to create the integration via API or CLI: [CreateIntegration API](https://docs.aws.amazon.com/glue/latest/webapi/API_CreateIntegration.html).