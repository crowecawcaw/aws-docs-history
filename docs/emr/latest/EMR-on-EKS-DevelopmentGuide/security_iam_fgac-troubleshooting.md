# Troubleshooting

## Logging

EMR on EKS uses Spark resources profiles to split job execution. Amazon EMR on EKS uses the user profile to run the code you supplied, while the system profile
enforces Lake Formation policies. You can access the logs for the containers ran as the user profile by configuring the StartJobRun request with
[MonitoringConfiguration](emr-eks-jobs-s3.md "emr-eks-jobs-s3.md").

## Spark History Server

The Spark History Server have all Spark events generated from the user profile and redacted events generated from the system driver. You can see all of the
containers from both the user and system drivers in the **Executors** tab. However, log links are available only for the user profile.

## Job failed with insufficient Lake Formation permissions

Make sure that your job execution role has the permissions to run `SELECT` and `DESCRIBE` on the table that you are accessing.

## Job with RDD execution failed

EMR on EKS currently doesn't support resilient distributed dataset (RDD) operations on Lake Formation-enabled jobs.

## Unable to access data files in Amazon S3

Make sure you have registered the location of the data lake in Lake Formation.

## Security validation exception

EMR on EKS detected a security validation error. Contact AWS support for assistance.

## Sharing AWS Glue Data Catalog and tables across accounts

You can share databases and tables across accounts and still use Lake Formation. For more information, see [Cross-account data sharing in Lake Formation](../../../lake-formation/latest/dg/cross-account-permissions.md "../../../lake-formation/latest/dg/cross-account-permissions.md") and
[How do I share AWS Glue Data Catalog and tables cross-account
using AWS Lake Formation?](https://repost.aws/knowledge-center/glue-lake-formation-cross-account "https://repost.aws/knowledge-center/glue-lake-formation-cross-account").

## Iceberg Job throwing initialization error not setting the AWS region

Message is the following:

```
25/02/25 13:33:19 ERROR SparkFGACExceptionSanitizer: Client received error with id = b921f9e6-f655-491f-b8bd-b2842cdc20c7,
reason = IllegalArgumentException, message = Cannot initialize
LakeFormationAwsClientFactory, please set client.region to a valid aws region
```

Make sure the Spark configuration `spark.sql.catalog.`catalog_name`.client.region` is set
to a valid region.

## Iceberg Job throwing SparkUnsupportedOperationException

Message is the following:

```
25/02/25 13:53:15 ERROR SparkFGACExceptionSanitizer: Client received error with id = 921fef42-0800-448b-bef5-d283d1278ce0,
reason = SparkUnsupportedOperationException, message = Either glue.id or glue.account-id is set with non-default account.
Cross account access with fine-grained access control is only supported with AWS Resource Access Manager.
```

Make sure the Spark Configuration `spark.sql.catalog.`catalog_name`.glue.account-id` is set to a valid account id.

## Iceberg Job fail with "403 Access Denied" during MERGE operation

Message is the following:

```
software.amazon.awssdk.services.s3.model.S3Exception: Access Denied (Service: S3, Status Code: 403,
...
	at software.amazon.awssdk.services.s3.DefaultS3Client.deleteObject(DefaultS3Client.java:3365)
	at org.apache.iceberg.aws.s3.S3FileIO.deleteFile(S3FileIO.java:162)
	at org.apache.iceberg.io.FileIO.deleteFile(FileIO.java:86)
	at org.apache.iceberg.io.RollingFileWriter.closeCurrentWriter(RollingFileWriter.java:129)
```

Disable S3 Delete operations in Spark by adding the following property. `--conf spark.sql.catalog.`s3-table-name`.s3.delete-enabled=false`.
