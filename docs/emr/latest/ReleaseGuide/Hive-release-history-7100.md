# Amazon EMR 7.10.0 - Hive

release notes

## Amazon EMR 7.10.0 -

Hive changes

| Type    | Description                                                                                                                    |
| ------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bug Fix | Hive side fix for [TEZ-4595](https://issues.apache.org/jira/browse/TEZ-4595 "https://issues.apache.org/jira/browse/TEZ-4595"). | **Known issues** <br>• AWS EMR from EMR-7.10.0 now uses S3A as the default filesystem (replacing EMRFS), which means Hive operations will no longer create `_$folder$` marker objects in S3, and the intermediate manifest files used in Hive write queries are now stored in S3 as compared to EMRFS’s HDFS. For considerations while using S3A, please refer to the [migration guide](emr-s3a-migrate.md "emr-s3a-migrate.md"). <br>• From EMR-7.3.0 to EMR-7.10.0, there is a Bug due to Hive Iceberg integration which causes HBase table creation in Hive to fail when AWS Glue Data Catalog is used as the metastore. Please reach out to the AWS support team if you encounter this issue. |
