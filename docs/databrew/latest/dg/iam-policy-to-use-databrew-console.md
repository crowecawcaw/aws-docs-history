# AwsGlueDataBrewCustomUserPolicy

The `AwsGlueDataBrewCustomUserPolicy` policy grants most of the
permissions required to use the DataBrew console. Some of the resources that are
specified in this policy refer to services that are used by DataBrew. These include
names for AWS Glue Data Catalog, Amazon S3 buckets, Amazon CloudWatch Logs, and AWS KMS
resources. It is similar to the AWS-managed policy named
`AwsGlueDataBrewFullAccessPolicy`.

The following table describes the permissions granted by this policy.

| **Action**                                                                                                                                                                           | **Resource**                                               | **Description**                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `"databrew:*"`                                                                                                                                                                       | `"*"`                                                      | Grants permission to run all DataBrew API operations.                                                    |
| `"glue:GetDatabases"` `"glue:GetPartitions"` `"glue:GetTable"` `"glue:GetTables"` `"glue:GetDataCatalogEncryptionSettings"`                                                          | `"*"`                                                      | Allows listing of AWS Glue databases and tables.                                                         |
| `"dataexchange:ListDataSets"` `"dataexchange:ListDataSetRevisions"` `"dataexchange:ListRevisionAssets"` `"dataexchange:CreateJob"` `"dataexchange:StartJob"` `"dataexchange:GetJob"` | `"*"`                                                      | Allows listing of AWS Data Exchange resources in datasets.                                               |
| `"kms:DescribeKey"` `"kms:ListKeys"` `"kms:ListAliases"`                                                                                                                             | `"*"`                                                      | Allows listing of AWS KMS keys to use for encryption of job output.                                      |
| `"kms:GenerateDataKey"`                                                                                                                                                              | `"arn:aws:kms:::key/key_ids"`                              | Allows encrypting of job output.                                                                         |
| `"s3:ListAllMyBuckets"` `"s3:GetBucketCORS"` `"s3:GetBucketLocation"` `"s3:GetEncryptionConfiguration"`                                                                              | `"arn:aws:s3:::bucket_name/*", "arn:aws:s3:::bucket_name"` | Allows listing of Amazon S3 buckets for projects, datasets, and jobs. Allows sending output files to S3. |
| `"sts:GetCallerIdentity"`                                                                                                                                                            | `"*"`                                                      | Get information about the current caller.                                                                |
| `"cloudtrail:LookupEvents",`                                                                                                                                                         | `"*"`                                                      | Allow listing AWS CloudTrail events for datasets (data lineage).                                         |
| `"iam:ListRoles"` `"iam:GetRole"`                                                                                                                                                    | `"*"`                                                      | Allows listing IAM roles to use for projects and jobs.                                                   |
