

# Document history

The following table describes the important changes to the documentation since the last release of EMR Serverless. For more information about updates to this documentation, you can subscribe to an RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [New feature](doc-history.md) | [Using Scaling Profiles](scaling-profiles.md) | November 18, 2026 | 
| [Lake Formation-governed user-defined functions](doc-history.md) | [Using user-defined functions with Lake Formation fine-grained access control](emr-serverless-lf-udf.md) | November 18, 2026 | 
| [Update to an existing policy.](doc-history.md) | Added `ec2:CreateNetworkInterfacePermission` and `ec2:DeleteNetworkInterfacePermission` to the [AmazonEMRServerlessServiceRolePolicy policy](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/using-service-linked-roles.html#slr-permissions) to support Flex execution. | November 17, 2026 | 
| [New feature](doc-history.md) | [Running EMR Serverless jobs on spare capacity with Flex](jobs-flex-execution.md) | November 17, 2026 | 
| [New feature](doc-history.md) | [Fine-grained access control with AWS Lake Formation for Spark Connect sessions](spark-connect.md#spark-connect-fgac) | September 22, 2026 | 
| [New GA release](doc-history.md) | [`AWS runtime for Apache Spark` (emr-spark-8.0.0)](release-version-emr-spark-8.0.0.md) | May 21, 2026 | 
| [New feature](doc-history.md) | [Run interactive sessions with Spark Connect](spark-connect.md) | April 23, 2026 | 
| [New preview release](doc-history.md) | [`AWS runtime for Apache Spark` (emr-spark-8.0-preview)](release-version-emr-spark-8.0-preview.md) | November 21, 2025 | 
| [New release](doc-history.md) | [EMR Serverless 7.2.0](release-version-720.md) | July 25, 2024 | 
| [New release](doc-history.md) | [EMR Serverless 7.1.0](release-version-710.md) | April 17, 2024 | 
| [Update to an existing policy.](doc-history.md) | Added the new `Sid` `CloudWatchPolicyStatement` and `EC2PolicyStatement` to the [AmazonEMRServerlessServiceRolePolicy policy](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/using-service-linked-roles.html#slr-permissions). | January 25, 2024 | 
| [New release](doc-history.md) | [EMR Serverless 7.0.0](release-version-700.md) | December 29, 2023 | 
| [New release](doc-history.md) | [EMR Serverless 6.15.0](release-version-6150.md) | November 17, 2023 | 
| [New feature](doc-history.md) | [Configure multiple IAM roles to assume when you access Amazon S3 buckets in different accounts from EMR Serverless](jobs-s3-access.md#jobs-s3-access-how-to-assumed-role-multiple) (6.11 and higher) | October 18, 2023 | 
| [New release](doc-history.md) | [EMR Serverless 6.14.0](release-version-6140.md) | October 17, 2023 | 
| [New feature](doc-history.md) | [Default application configuration for EMR Serverless](default-configs.md) | September 25, 2023 | 
| [Update to default Hive properties](doc-history.md) | Updated the default values for `hive.driver.disk`, `hive.tez.disk.size`, `hive.tez.auto.reducer.parallelism`, and `tez.grouping.min-size` [Hive job properties](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/jobs-hive.html#hive-defaults). | September 12, 2023 | 
| [New release](doc-history.md) | [EMR Serverless 6.13.0](release-version-6130.md) | September 11, 2023 | 
| [New release](doc-history.md) | [EMR Serverless 6.12.0](release-version-6120.md) | July 21, 2023 | 
| [New release](doc-history.md) | [EMR Serverless 6.11.0](release-version-6110.md) | June 8, 2023 | 
| [Update to service-linked role policy](doc-history.md) | Updated the [`AmazonEMRServerlessServiceRolePolicy`](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/using-service-linked-roles.html#slr-permissions) SLR role to publish account-level usage in `"AWS/Usage"` namespace. | April 20, 2023 | 
| [EMR Serverless general availability (GA)](doc-history.md) | This is the first public release of EMR Serverless. | June 1, 2022 | 