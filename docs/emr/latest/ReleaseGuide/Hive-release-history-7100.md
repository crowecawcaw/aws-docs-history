

# Amazon EMR 7.10.0 - Hive release notes
<a name="Hive-release-history-7100"></a>

## Amazon EMR 7.10.0 - Hive changes
<a name="Hive-release-history-changes-7100"></a>



| Type | Description | 
| --- | --- | 
| Bug Fix | Hive side fix for [TEZ-4595](https://issues.apache.org/jira/browse/TEZ-4595). | 

**Known issues**
+ AWS EMR from EMR-7.10.0 now uses S3A as the default filesystem (replacing EMRFS), which means Hive operations will no longer create `_$folder$` marker objects in S3, and the intermediate manifest files used in Hive write queries are now stored in S3 as compared to EMRFS’s HDFS. For considerations while using S3A, please refer to the [migration guide](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-s3a-migrate.html).
+ From EMR-7.3.0 to EMR-7.10.0, there is a Bug due to Hive Iceberg integration which causes HBase table creation in Hive to fail when AWS Glue Data Catalog is used as the metastore. Please reach out to the AWS support team if you encounter this issue. 