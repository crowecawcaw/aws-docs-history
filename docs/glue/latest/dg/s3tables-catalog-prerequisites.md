

# Prerequisites
<a name="s3tables-catalog-prerequisites"></a>

Before you create a federated catalog for S3 Tables in the AWS Glue Data Catalog, ensure your IAM principal (user or role) has the required permissions.

## Required IAM permissions
<a name="s3tables-required-iam-permissions"></a>

Your IAM principal needs the following permissions to enable S3 Tables integration:

**AWS Glue permissions**:
+ `glue:CreateCatalog` – Required to create the `s3tablescatalog` federated catalog
+ `glue:GetCatalog` – Required to view catalog details
+ `glue:GetDatabase` – Required to view S3 namespaces as databases
+ `glue:GetTable` – Required to view S3 tables
+ `glue:passConnection` – Grants the calling principal the right to delegate the `aws:s3tables` connection to the AWS Glue service

**S3 Tables permissions** (for IAM access control):
+ `s3tables:CreateTableBucket`
+ `s3tables:GetTableBucket`
+ `s3tables:CreateNamespace`
+ `s3tables:GetNamespace`
+ `s3tables:ListNamespaces`
+ `s3tables:CreateTable`
+ `s3tables:GetTable`
+ `s3tables:ListTables`
+ `s3tables:UpdateTableMetadataLocation`
+ `s3tables:GetTableMetadataLocation`
+ `s3tables:GetTableData`
+ `s3tables:PutTableData`

## IAM policy example
<a name="s3tables-iam-policy-example"></a>

The following IAM policy provides the minimum permissions required to enable S3 Tables integration with the Data Catalog in IAM mode:

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "GlueDataCatalogPermissions",
      "Effect": "Allow",
      "Action": [
        "glue:CreateCatalog",
        "glue:GetCatalog",
        "glue:GetDatabase",
        "glue:GetTable"
      ],
      "Resource": [
        "arn:aws:glue:{{us-east-1}}:{{123456789012}}:catalog/s3tablescatalog",
        "arn:aws:glue:{{us-east-1}}:{{123456789012}}:database/s3tablescatalog/*/*",
        "arn:aws:glue:{{us-east-1}}:{{123456789012}}:table/s3tablescatalog/*/*/*"
      ]
    },
    {
      "Sid": "S3TablesDataAccessPermissions",
      "Effect": "Allow",
      "Action": [
        "s3tables:GetTableBucket",
        "s3tables:GetNamespace",
        "s3tables:GetTable",
        "s3tables:GetTableMetadataLocation",
        "s3tables:GetTableData"
      ],
      "Resource": [
        "arn:aws:s3tables:{{us-east-1}}:{{123456789012}}:bucket/*",
        "arn:aws:s3tables:{{us-east-1}}:{{123456789012}}:bucket/*/table/*"
      ]
    }
  ]
}
```