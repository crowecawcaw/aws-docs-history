

# IAM policies reference
<a name="aurora-analytics-iam-policies-reference"></a>

Aurora PostgreSQL requires IAM permissions to access your Iceberg and Parquet data in Amazon S3 and, optionally, AWS Glue Data Catalog or Amazon S3 Tables. The specific permissions depend on your data format and how the data is registered. This section presents examples of typical IAM policies for Aurora PostgreSQL.

**Topics**
+ [Summary of required permissions](#aurora-analytics-iam-summary)
+ [Example policies](#aurora-analytics-iam-examples)
+ [Server-side encryption with AWS KMS](#aurora-analytics-iam-kms)
+ [Cross-account access](#aurora-analytics-iam-cross-account)
+ [IAM role trust policy](#aurora-analytics-iam-trust-policy)
+ [Best practices for IAM policies](#aurora-analytics-iam-best-practices)

## Summary of required permissions
<a name="aurora-analytics-iam-summary"></a>

The following table summarizes the permissions that Aurora PostgreSQL requires for each access path. Grant only the row that matches your configuration.


**Required permissions by data format and access path**  

| Data format and access path | Service | Required permissions | Resources | 
| --- | --- | --- | --- | 
| Apache Parquet, single file | Amazon S3 | s3:GetObject | Object key | 
| Apache Parquet, folder or wildcard path | Amazon S3 | s3:GetObject, s3:ListBucket | Bucket, prefix condition, object keys | 
| Apache Iceberg, AWS Glue Data Catalog | AWS Glue \+ Amazon S3 | glue:GetTable, s3:GetObject | Catalog, database, table, object keys | 
| Apache Iceberg, AWS Glue federated catalog (remote catalogs such as Snowflake and Databricks) | AWS Lake Formation \+ AWS Glue \+ Amazon S3 | lakeformation:GetDataAccess, glue:GetTable, s3:GetObject | Catalog, database, table, object keys | 
| Apache Parquet, AWS Glue Data Catalog (crawler-registered) | AWS Glue \+ Amazon S3 | glue:GetTable, s3:GetObject, s3:ListBucket | Catalog, database, table, bucket, object keys | 
| Apache Iceberg, Amazon S3 Tables through AWS Glue | AWS Glue \+ Amazon S3 Tables | glue:GetTable, s3tables:GetTable, s3tables:GetTableBucket, s3tables:GetTableData, s3tables:GetNamespace | Catalog, database, table, table bucket, table | 
| Apache Iceberg, Amazon S3 Tables by table ARN | Amazon S3 Tables | s3tables:GetTable, s3tables:GetTableBucket, s3tables:GetTableData, s3tables:GetNamespace | Table bucket, table | 
| Any of the preceding, with SSE-KMS encryption | \+ AWS KMS | kms:Decrypt | KMS key | 

Three points affect how much you need to grant:
+ `s3:ListBucket` is required only when Aurora PostgreSQL must discover files. A location that names an exact object key needs no listing. Iceberg tables need no listing either, because Iceberg manifests carry the exact key of every data file. Crawler-registered Parquet tables in AWS Glue store a folder path rather than a manifest, which means listing is required for those.
+ Amazon S3 Tables requires four `s3tables` actions, not one. Resolving a table is a multi-step operation in the Amazon S3 Tables service: the table bucket, the namespace, the table metadata, and the table data are each authorized separately. Granting only `s3tables:GetTableData` results in an access denied error naming `s3tables:GetTableBucket`.
+ Cross-account access requires permissions on both sides. The examples in this section are same-account. When another account owns the data, the resource policy in the data owner's account and the IAM policy in your account must both allow the action.

## Example policies
<a name="aurora-analytics-iam-examples"></a>

These example policies use `amzn-s3-demo-bucket` as the bucket name, `amzn-s3-demo-table-bucket` as the Amazon S3 Tables table bucket name, and `123456789012` as the AWS account ID. To use these policies, replace the {{user input placeholders}} with your own information, and scope each `Resource` element to only the data that your foreign tables reference.

### Example: Parquet files in Amazon S3
<a name="aurora-analytics-iam-parquet"></a>

The following example policy grants permission to read Parquet files directly from an Amazon S3 bucket. AWS Glue Data Catalog isn't required for Parquet.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "S3ListBucket",
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::amzn-s3-demo-bucket",
            "Condition": {
                "StringLike": {
                    "s3:prefix": [
                        "data/orders",
                        "data/orders/*",
                        "data/customers",
                        "data/customers/*"
                    ]
                }
            }
        },
        {
            "Sid": "S3ReadObjects",
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket/data/orders/*",
                "arn:aws:s3:::amzn-s3-demo-bucket/data/customers/*"
            ]
        }
    ]
}
```

This policy consists of two `Allow` statements:

`S3ListBucket`  
Grants permission to list files in the Amazon S3 bucket, restricted to specific folder prefixes. Include this statement when a foreign table location names a folder or wildcard path, such as `s3://amzn-s3-demo-bucket/data/orders/`. Omit it when every foreign table names an exact object key. The `Condition` element restricts listing to the specified prefixes. Each prefix is listed both with and without a trailing slash so that the condition matches regardless of how the prefix is expressed.

`S3ReadObjects`  
Grants permission to read Parquet file contents. The resource ARNs are scoped to specific object key prefixes for least-privilege access.

### Example: Iceberg tables through AWS Glue Data Catalog and Amazon S3
<a name="aurora-analytics-iam-iceberg-glue"></a>

The following example policy grants permission to query Iceberg tables that are registered in AWS Glue Data Catalog.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "GlueCatalogAccess",
            "Effect": "Allow",
            "Action": "glue:GetTable",
            "Resource": [
                "arn:aws:glue:us-east-1:123456789012:catalog",
                "arn:aws:glue:us-east-1:123456789012:database/analytics_db",
                "arn:aws:glue:us-east-1:123456789012:table/analytics_db/orders",
                "arn:aws:glue:us-east-1:123456789012:table/analytics_db/customers"
            ]
        },
        {
            "Sid": "S3ReadObjects",
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket/data/iceberg/orders/*",
                "arn:aws:s3:::amzn-s3-demo-bucket/data/iceberg/customers/*"
            ]
        }
    ]
}
```

This policy consists of two `Allow` statements:

`GlueCatalogAccess`  
Grants permission to read table metadata from AWS Glue Data Catalog. The `glue:GetTable` action requires permissions at three resource levels: the root AWS Glue catalog, the database that contains the table, and each table that you want to query. When you reference an AWS Glue table ARN in a foreign table, Aurora PostgreSQL calls the AWS Glue API to retrieve table metadata, including the Amazon S3 location, format, and schema.

`S3ReadObjects`  
Grants permission to read the Iceberg metadata files and the Parquet data files from Amazon S3.

This policy doesn't grant `s3:ListBucket`, which Iceberg tables don't require. If the AWS Glue table is a crawler-registered Parquet table rather than an Iceberg table, add the `S3ListBucket` statement that is shown in the preceding Parquet example.

### Example: Iceberg tables in Amazon S3 Tables
<a name="aurora-analytics-iam-s3tables"></a>

Amazon S3 Tables supports two access paths, and each requires a different set of permissions. Use the example that matches your foreign table definition.

#### Access through AWS Glue Data Catalog
<a name="aurora-analytics-iam-s3tables-glue"></a>

The following example policy grants permission to query an Amazon S3 Tables table through an AWS Glue ARN under the `s3tablescatalog` federated catalog, such as `arn:aws:glue:us-east-1:123456789012:table/s3tablescatalog/amzn-s3-demo-table-bucket/my_namespace/orders`.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "GlueCatalogAccess",
            "Effect": "Allow",
            "Action": "glue:GetTable",
            "Resource": [
                "arn:aws:glue:us-east-1:123456789012:catalog/s3tablescatalog/amzn-s3-demo-table-bucket",
                "arn:aws:glue:us-east-1:123456789012:database/s3tablescatalog/amzn-s3-demo-table-bucket/my_namespace",
                "arn:aws:glue:us-east-1:123456789012:table/s3tablescatalog/amzn-s3-demo-table-bucket/my_namespace/orders"
            ]
        },
        {
            "Sid": "S3TablesAccess",
            "Effect": "Allow",
            "Action": [
                "s3tables:GetTable",
                "s3tables:GetTableBucket",
                "s3tables:GetTableData",
                "s3tables:GetNamespace"
            ],
            "Resource": [
                "arn:aws:s3tables:us-east-1:123456789012:bucket/amzn-s3-demo-table-bucket",
                "arn:aws:s3tables:us-east-1:123456789012:bucket/amzn-s3-demo-table-bucket/table/*"
            ]
        }
    ]
}
```

#### Access by table ARN
<a name="aurora-analytics-iam-s3tables-arn"></a>

The following example policy grants permission to query an Amazon S3 Tables table by its table ARN, such as `arn:aws:s3tables:us-east-1:123456789012:bucket/amzn-s3-demo-table-bucket/table/1234abcd-12ab-34cd-56ef-1234567890ab`. This access path doesn't involve AWS Glue, and no AWS Glue permissions are required.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "S3TablesAccess",
            "Effect": "Allow",
            "Action": [
                "s3tables:GetTable",
                "s3tables:GetTableBucket",
                "s3tables:GetTableData",
                "s3tables:GetNamespace"
            ],
            "Resource": [
                "arn:aws:s3tables:us-east-1:123456789012:bucket/amzn-s3-demo-table-bucket",
                "arn:aws:s3tables:us-east-1:123456789012:bucket/amzn-s3-demo-table-bucket/table/*"
            ]
        }
    ]
}
```

The statements in the preceding examples grant the following permissions:

`GlueCatalogAccess`  
Grants permission to resolve the table through AWS Glue Data Catalog. Amazon S3 Tables table buckets appear in AWS Glue under the `s3tablescatalog` federated catalog, so the resource ARNs include the table bucket name in the catalog, database, and table paths. This statement is required only when you access the table through AWS Glue Data Catalog.

`S3TablesAccess`  
Grants permission to resolve and read the table through Amazon S3 Tables. All four actions are required, and each one authorizes a distinct step of table resolution:  


**Amazon S3 Tables actions and the steps they authorize**  

<table>
<thead>
  <tr><th>Action</th><th>Authorizes</th></tr>
</thead>
<tbody>
  <tr><td><code>s3tables:GetTableBucket</code></td><td>Resolving the table bucket</td></tr>
  <tr><td><code>s3tables:GetNamespace</code></td><td>Resolving the namespace that contains the table</td></tr>
  <tr><td><code>s3tables:GetTable</code></td><td>Retrieving table metadata</td></tr>
  <tr><td><code>s3tables:GetTableData</code></td><td>Reading the underlying Iceberg data</td></tr>
</tbody>
</table>


When you access the table through AWS Glue Data Catalog, AWS Glue resolves the table bucket and the namespace on your behalf as part of resolving the federated catalog.

Standard Amazon S3 permissions such as `s3:GetObject` and `s3:ListBucket` aren't required for either access path.

For cross-account access, you can grant `s3tables:GetTableBucket` and `s3tables:GetNamespace` in the table bucket policy in the data owner's account instead of in your IAM policy. In that configuration, your IAM policy requires only `s3tables:GetTable` and `s3tables:GetTableData`.

## Server-side encryption with AWS KMS
<a name="aurora-analytics-iam-kms"></a>

If your data is encrypted with server-side encryption using AWS KMS keys (SSE-KMS), add a statement like the following to the policy for your access path. Data that is encrypted with SSE-S3 doesn't require additional permissions.

```
{
    "Sid": "KMSDecrypt",
    "Effect": "Allow",
    "Action": "kms:Decrypt",
    "Resource": "arn:aws:kms:us-east-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab"
}
```

For a KMS key that is owned by another account, the key policy in the owning account must grant `kms:Decrypt` to your role *and* your role's IAM policy must allow `kms:Decrypt` on that key. Neither policy alone is sufficient.

## Cross-account access
<a name="aurora-analytics-iam-cross-account"></a>

When another account owns your data, both accounts must allow the action. In the following examples, a cluster role in account `123456789012` reads Parquet files from a bucket that is owned by account `111122223333`.

The following example bucket policy, in the data owner's account, grants the cluster role permission to read objects from the bucket.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowAuroraAnalyticsRole",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::123456789012:role/amzn-analytics-demo-role"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/data/orders/*"
        }
    ]
}
```

The following example identity-based policy, attached to the cluster role in your account, grants the same permission on the same resource.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "S3ReadCrossAccount",
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/data/orders/*"
        }
    ]
}
```

If either policy omits the action, the request is denied. Cross-account denials from Amazon S3 don't identify which side is missing the permission, so check both policies.

The same requirement applies to AWS Glue resources and AWS KMS keys that are owned by another account. If your foreign table location names a folder rather than an exact object key, add `s3:ListBucket` on the bucket ARN to both policies.

## IAM role trust policy
<a name="aurora-analytics-iam-trust-policy"></a>

Whichever permissions policy you use, attach it to an IAM role whose trust policy allows Amazon RDS to assume the role on behalf of your Aurora DB cluster, as in the following example. The `aws:SourceAccount` and `aws:SourceArn` condition keys restrict the role so that it can be assumed only on behalf of your own cluster.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "rds.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "123456789012"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:rds:us-east-1:123456789012:cluster:amzn-rds-demo-cluster"
                }
            }
        }
    ]
}
```

## Best practices for IAM policies
<a name="aurora-analytics-iam-best-practices"></a>

When you create these IAM policies, follow these best practices:
+ **Use least privilege**: Grant only the specific Amazon S3 prefixes, AWS Glue resources, and Amazon S3 Tables resources that your foreign tables require. Avoid wildcard (`*`) resource ARNs.
+ **Grant `s3:ListBucket` only where it is needed**: See the summary table for which access paths require it.
+ **Use prefix conditions**: Apply `s3:prefix` conditions to `s3:ListBucket` actions to restrict which folders can be listed.
+ **Separate roles for separate concerns**: If different databases or users access different Amazon S3 data, consider using separate IAM roles for each scope.
+ **Audit regularly**: Review policy permissions periodically to confirm that they match your current foreign table definitions.