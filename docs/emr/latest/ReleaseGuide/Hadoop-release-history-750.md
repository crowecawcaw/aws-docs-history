# Amazon EMR 7.5.0 - Hadoop release notes

## Amazon EMR 7.5.0 - Hadoop changes

| Type        | Description                                                                                                                                                                             |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bug Fix     | Commented out fs.file.impl to empty value.                                                                                                                                              |
| Backport    | [HADOOP-19286](https://issues.apache.org/jira/browse/HADOOP-19286 "https://issues.apache.org/jira/browse/HADOOP-19286"): Support S3A cross region access when S3 region/endpoint is set |
| Improvement | Automatic S3 region configuration setting for S3A connector on EMR-EC2                                                                                                                  |
| Improvement | Reduce the number of HeadObject calls in S3A                                                                                                                                            |

With the release of Amazon EMR 7.5, Spark's S3A connector demonstrates read performance comparable to EMRFS, as evidenced by benchmarks using a 3TB TPC-DS parquet dataset.

## Amazon EMR 7.5.0 - Hadoop features

- S3 region configuration `fs.s3a.endpoint.region` is automatically set to the region where the EMR cluster is launched with S3A connector for EMR-EC2 deployment.
- Amazon S3 cross-bucket region access is enabled by default for the S3A connector. It can be modified by
  setting `fs.s3a.cross.region.access.enabled=`true or false``.
