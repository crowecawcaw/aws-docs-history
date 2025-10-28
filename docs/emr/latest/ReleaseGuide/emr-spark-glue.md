# Use AWS Glue Data Catalog catalog with Spark on Amazon EMR

Using Amazon EMR release 5.8.0 or later, you can configure Spark to use the AWS Glue Data Catalog
as its Apache Hive metastore. We recommend this configuration when you require a persistent
Hive metastore or a Hive metastore shared by different clusters, services, applications, or AWS
accounts.

Using Amazon EMR release 6.5.0 or later, you can configure Spark to use the AWS Glue Data Catalog with Apache Iceberg.

Using Amazon EMR release 7.5.0 or later, you can configure Spark to use the AWS Glue Data Catalog
as its Iceberg REST catalog.

AWS Glue is a fully managed extract, transform, and load (ETL) service that makes it simple and cost-effective to categorize your data, clean it, enrich it, and move it reliably between various data stores. The AWS Glue Data Catalog provides a unified metadata repository across a variety of data sources and data formats, integrating with Amazon EMR as well as Amazon RDS, Amazon Redshift, Redshift Spectrum, Athena, and any application compatible with the Apache Hive metastore. AWS Glue crawlers can automatically infer schema from source data in Amazon S3 and store the associated metadata in the Data Catalog. For more information about the Data Catalog, see [Populating the AWS Glue Data Catalog](../../../glue/latest/dg/populate-data-catalog.md "../../../glue/latest/dg/populate-data-catalog.md") in the _AWS Glue Developer Guide_.

Separate charges apply for AWS Glue. There is a monthly rate for storing and accessing the metadata in the Data Catalog, an hourly rate billed per minute for AWS Glue ETL jobs and crawler runtime, and an hourly rate billed per minute for each provisioned development endpoint. The Data Catalog allows you to store up to a million objects at no charge. If you store more than a million objects, you are charged USD$1 for each 100,000 objects over a million. An object in the Data Catalog is a table, partition, or database. For more information, see [Glue Pricing](https://aws.amazon.com/glue/pricing "https://aws.amazon.com/glue/pricing").

###### Important

If you created tables using Amazon Athena or Amazon Redshift Spectrum before August 14, 2017, databases and tables are stored in an Athena-managed catalog, which is separate from the AWS Glue Data Catalog. To integrate Amazon EMR with these tables, you must upgrade to the AWS Glue Data Catalog. For more information, see [Upgrading to the AWS Glue Data Catalog](../../../athena/latest/ug/glue-upgrade.md "../../../athena/latest/ug/glue-upgrade.md") in the _Amazon Athena User Guide_.

## Specifying AWS Glue Data Catalog as the

Apache Hive metastore

You can specify the AWS Glue Data Catalog as the metastore using the AWS Management Console, AWS CLI, or Amazon EMR API. When you use the CLI or API, you use the configuration classification for Spark to specify the Data Catalog. In addition, with Amazon EMR 5.16.0 and later, you can use the configuration classification to specify a Data Catalog in a different AWS account. When you use the console, you can specify the Data Catalog using **Advanced Options** or **Quick Options**.

###### Note

The option to use AWS Glue Data Catalog is also available with Zeppelin because Zeppelin
is installed with Spark components.

Console

###### To specify AWS Glue Data Catalog as the Apache Hive metastore with the new

console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **Amazon EMR on EC2** in the left navigation
   pane, choose **Clusters**, and then choose
   **Create cluster**.
3. Under **Application bundle**, choose
   **Spark** or **Custom**.
   If you customize your cluster, make sure that you select
   Zeppelin or Spark as one of your applications.
4. Under **AWS Glue Data Catalog settings**, select the
   **Use for Spark table metadata** check
   box.
5. Choose any other options that apply to your cluster.
6. To launch your cluster, choose **Create
   cluster**.

AWS CLI

###### To specify the AWS Glue Data Catalog as the Apache Hive metastore with the

AWS CLI

For more information about specifying a configuration
classification using the AWS CLI and Amazon EMR API, see [Configure applications](emr-configure-apps.md "emr-configure-apps.md").

- Specify the value for
  `hive.metastore.client.factory.class` using the
  `spark-hive-site` classification as shown in the
  following example:

```
[
  {
    "Classification": "spark-hive-site",
    "Properties": {
      "hive.metastore.client.factory.class": "com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory"
    }
  }
]

```

To specify a Data Catalog in a different AWS account, add the
`hive.metastore.glue.catalogid` property as shown
in the following example. Replace
`acct-id` with the
AWS account of the Data Catalog.

```
[
  {
    "Classification": "spark-hive-site",
    "Properties": {
      "hive.metastore.client.factory.class": "com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory",
      "hive.metastore.glue.catalogid": "`acct-id`"
    }
  }
]

```

## Specifying AWS Glue Data Catalog as the Apache Iceberg catalog

You can specify the AWS Glue Data Catalog as the Apache Iceberg catalog implementation, or the Apache Iceberg REST catalog
endpoint, using the AWS Management Console, the AWS CLI, or the Amazon EMR API, or at Spark session runtime configuration. When you use the CLI or API, you
use the configuration classification for Spark to specify the Data Catalog. For more details,
see [Specifying AWS Glue Data Catalog as the Apache Iceberg catalog](emr-spark-glue.md#emr-spark-glue-configure-iceberg "emr-spark-glue.md#emr-spark-glue-configure-iceberg").

## IAM permissions

The EC2 instance profile for a cluster must have IAM permissions for AWS Glue actions. In
addition, if you enable encryption for AWS Glue Data Catalog objects, the role must also be allowed to
encrypt, decrypt and generate the AWS KMS key used for encryption.

### Permissions for AWS Glue actions

If you use the default EC2 instance profile for Amazon EMR, no action is required. The
`AmazonElasticMapReduceforEC2Role` managed policy that is attached to the
`EMR_EC2_DefaultRole` allows all necessary AWS Glue actions. However, if you
specify a custom EC2 instance profile and permissions, you must configure the
appropriate AWS Glue actions. Use the `AmazonElasticMapReduceforEC2Role` managed
policy as a starting point. For more information, see [Service role for cluster EC2 instances
(EC2 instance profile)](../ManagementGuide/emr-iam-role-for-ec2.md "../ManagementGuide/emr-iam-role-for-ec2.md") in the _Amazon EMR Management Guide_.

### Permissions for encrypting and decrypting AWS Glue Data Catalog

Your instance profile needs permission to encrypt and decrypt data using your key. You
do _not_ need to configure these permissions if both of
the following statements apply:

- You enable encryption for AWS Glue Data Catalog objects using managed keys for
  AWS Glue.
- You use a cluster that's in the same AWS account as the AWS Glue Data Catalog.

Otherwise, you must add the following statement to the permissions policy attached to
your EC2 instance profile.

For more information
about AWS Glue Data Catalog encryption, see [Encrypting your data
catalog](../../../glue/latest/dg/encrypt-glue-data-catalog.md "../../../glue/latest/dg/encrypt-glue-data-catalog.md") in the _AWS Glue Developer Guide_.

### Resource-based permissions

If you use AWS Glue in conjunction with Hive, Spark, or Presto in Amazon EMR, AWS Glue supports resource-based policies to control access to Data Catalog resources. These resources include databases, tables, connections, and user-defined functions. For more information, see [AWS Glue Resource Policies](../../../glue/latest/dg/glue-resource-policies.md "../../../glue/latest/dg/glue-resource-policies.md") in the _AWS Glue Developer Guide_.

When using resource-based policies to limit access to AWS Glue from within Amazon EMR, the principal that you specify in the permissions policy must be the role ARN associated with the EC2 instance profile that is specified when a cluster is created. For example, for a resource-based policy attached to a catalog, you can specify the role ARN for the default service role for cluster EC2 instances, `EMR_EC2_DefaultRole` as the `Principal`, using the format shown in the following example:

```
arn:aws:iam::`acct-id`:role/`EMR_EC2_DefaultRole`
```

The `acct-id` can be different from the AWS Glue account ID. This enables access from EMR clusters in different accounts. You can specify multiple principals, each from a different account.

## Considerations when using

AWS Glue Data Catalog

Consider the following items when using AWS Glue Data Catalog as an Apache Hive metastore with
Spark:

- Having a default database without a location URI causes failures when you
  create a table. As a workaround, use the `LOCATION` clause to
  specify a bucket location, such as
  `s3://`amzn-s3-demo-bucket1``,
when you use `CREATE TABLE`. Alternatively create tables within a
  database other than the default database.
- Renaming tables from within AWS Glue is not supported.
- When you create a Hive table without specifying a `LOCATION`, the table data is stored in the location specified by the `hive.metastore.warehouse.dir` property. By default, this is a location in HDFS. If another cluster needs to access the table, it fails unless it has adequate permissions to the cluster that created the table. Furthermore, because HDFS storage is transient, if the cluster terminates, the table data is lost, and the table must be recreated. We recommend that you specify a `LOCATION` in Amazon S3 when you create a Hive table using AWS Glue. Alternatively, you can use the `hive-site` configuration classification to specify a location in Amazon S3 for `hive.metastore.warehouse.dir`, which applies to all Hive tables. If a table is created in an HDFS location and the cluster that created it is still running, you can update the table location to Amazon S3 from within AWS Glue. For more information, see [Working with Tables on the AWS Glue Console](../../../glue/latest/dg/console-tables.md "../../../glue/latest/dg/console-tables.md") in the _AWS Glue Developer Guide_.
- Partition values containing quotes and apostrophes are not supported, for example, `PARTITION (owner="Doe's").`
- [Column statistics](https://cwiki.apache.org/confluence/display/Hive/StatsDev#StatsDev-ColumnStatistics "https://cwiki.apache.org/confluence/display/Hive/StatsDev#StatsDev-ColumnStatistics") are supported for emr-5.31.0 and later.
- Using [Hive authorization](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Authorization "https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Authorization") is not supported. As an alternative, consider using [AWS Glue Resource-Based Policies](../../../glue/latest/dg/glue-resource-policies.md "../../../glue/latest/dg/glue-resource-policies.md"). For more information, see [Use Resource-Based Policies for Amazon EMR Access to AWS Glue Data Catalog](../ManagementGuide/emr-iam-roles-glue.md "../ManagementGuide/emr-iam-roles-glue.md").

Consider the following when using AWS Glue Data Catalog as Apache Iceberg REST Catalog with Spark:

- If you use the Spark session catalog with Iceberg, which is described in [Configuration differences when you use Iceberg SparkCatalog versus SparkSessionCatalog](emr-iceberg-use-spark-cluster.md#emr-iceberg-spark-catalog "emr-iceberg-use-spark-cluster.md#emr-iceberg-spark-catalog"), you must configure the AWS Glue Data Catalog as the Apache Hive metastore, in addition to configuring the AWS Glue Data Catalog as
  the Apache Iceberg REST catalog.
- The AWS Glue Data Catalog IRC endpoint supports only the Amazon SigV4 authentication scheme. OAuth is not supported. For OAuth users, please use IAM Identity Center to
  configure access. See [Connecting Lake Formation with IAM Identity Center](../../../lake-formation/latest/dg/connect-lf-identity-center.md "../../../lake-formation/latest/dg/connect-lf-identity-center.md").
- The AWS Glue Iceberg REST catalog does not support all operations in open source.
