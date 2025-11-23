# Amazon EMR 2.x and 3.x AMI versions

###### Note

AWS is updating the TLS configuration for all AWS API endpoints to a minimum
version of TLS 1.2. Amazon EMR releases 3.10 and lower only support TLS 1.0/1.1 connections.
After December 4, 2023, you won't be able to create clusters with Amazon EMR 3.10 and
lower.

If you use Amazon EMR 3.10 or lower, we recommend that you immediately test and migrate
your workloads to the latest Amazon EMR release. For more information, see the [AWS Security Blog](https://aws.amazon.com/blogs//security/tls-1-2-required-for-aws-endpoints/ "https://aws.amazon.com/blogs//security/tls-1-2-required-for-aws-endpoints/").

Amazon EMR 2.x and 3.x releases, called _AMI versions_, are made available
for pre-existing solutions that require them for compatibility reasons. We do not recommend
creating new clusters or new solutions with these release versions. They lack features of
newer releases and include outdated application packages.

We recommend that you build solutions using the most recent Amazon EMR release version.

The scope of differences between the 2.x and 3.x series release versions and recent Amazon EMR
release versions is significant. Those differences range from how you create and configure a
cluster to the ports and directory structure of applications on the cluster.

This section attempts to cover the most significant differences for Amazon EMR, as well as
specific application configuration and management differences. It is not comprehensive. If
you create and use clusters in the 2.x or 3.x series, you may encounter differences not
covered in this section.

###### Topics

- [Creating a cluster with earlier AMI versions of
  Amazon EMR](emr-3x-create.md "emr-3x-create.md")
- [Installing applications with earlier AMI versions
  of Amazon EMR](emr-3x-install-apps.md "emr-3x-install-apps.md")
- [Customizing cluster and application
  configuration with earlier AMI versions of Amazon EMR](emr-3x-customizeappconfig.md "emr-3x-customizeappconfig.md")
- [Hive application specifics for earlier AMI versions of
  Amazon EMR](emr-3x-hive.md "emr-3x-hive.md")
- [HBase application specifics for earlier AMI versions of
  Amazon EMR](emr-3x-hbase.md "emr-3x-hbase.md")
- [Pig application specifics for earlier AMI versions of
  Amazon EMR](emr-3x-pig.md "emr-3x-pig.md")
- [Spark application specifics with earlier AMI versions of
  Amazon EMR](emr-3x-spark.md "emr-3x-spark.md")
- [S3DistCp utility differences with earlier AMI versions of
  Amazon EMR](emr-3x-s3distcp.md "emr-3x-s3distcp.md")
