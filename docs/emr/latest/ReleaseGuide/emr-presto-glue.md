# Using Presto with the AWS Glue Data Catalog

Using Amazon EMR release version 5.10.0 and later, you can specify the AWS Glue Data Catalog as the
default Hive metastore for Presto. We recommend this configuration when you require a
persistent metastore or a metastore shared by different clusters, services,
applications, or AWS accounts.

AWS Glue is a fully managed extract, transform, and load (ETL) service that makes it simple and cost-effective to categorize your data, clean it, enrich it, and move it reliably between various data stores. The AWS Glue Data Catalog provides a unified metadata repository across a variety of data sources and data formats, integrating with Amazon EMR as well as Amazon RDS, Amazon Redshift, Redshift Spectrum, Athena, and any application compatible with the Apache Hive metastore. AWS Glue crawlers can automatically infer schema from source data in Amazon S3 and store the associated metadata in the Data Catalog. For more information about the Data Catalog, see [Populating the AWS Glue Data Catalog](../../../glue/latest/dg/populate-data-catalog.md "../../../glue/latest/dg/populate-data-catalog.md") in the _AWS Glue Developer Guide_.

Separate charges apply for AWS Glue. There is a monthly rate for storing and accessing the metadata in the Data Catalog, an hourly rate billed per minute for AWS Glue ETL jobs and crawler runtime, and an hourly rate billed per minute for each provisioned development endpoint. The Data Catalog allows you to store up to a million objects at no charge. If you store more than a million objects, you are charged USD$1 for each 100,000 objects over a million. An object in the Data Catalog is a table, partition, or database. For more information, see [Glue Pricing](https://aws.amazon.com/glue/pricing "https://aws.amazon.com/glue/pricing").

###### Important

If you created tables using Amazon Athena or Amazon Redshift Spectrum before August 14, 2017, databases and tables are stored in an Athena-managed catalog, which is separate from the AWS Glue Data Catalog. To integrate Amazon EMR with these tables, you must upgrade to the AWS Glue Data Catalog. For more information, see [Upgrading to the AWS Glue Data Catalog](../../../athena/latest/ug/glue-upgrade.md "../../../athena/latest/ug/glue-upgrade.md") in the _Amazon Athena User Guide_.

## Specifying AWS Glue Data Catalog as the

metastore

You can specify the AWS Glue Data Catalog as the metastore using the AWS Management Console, AWS CLI, or Amazon EMR API. When you use the CLI or API, you use the configuration classification for Presto to specify the Data Catalog. In addition, with Amazon EMR 5.16.0 and later, you can use the configuration classification to specify a Data Catalog in a different AWS account. When you use the console, you can specify the Data Catalog using **Advanced Options** or **Quick Options**.

Console

###### To specify AWS Glue Data Catalog as the Hive metastore with the new

console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left navigation
   pane, choose **Clusters**, and then choose
   **Create cluster**.
3. Under **Application bundle**, choose
   **Presto**.
4. Under **AWS Glue Data Catalog settings**, select the
   **Use for Presto table metadata** check
   box.
5. Choose any other options that apply to your cluster.
6. To launch your cluster, choose **Create
   cluster**.

CLI

###### To specify the AWS Glue Data Catalog as the default Hive metastore using

the AWS CLI

For examples of how to specify the following configuration
classifications when you create a cluster, see [Configure applications](emr-configure-apps.md "emr-configure-apps.md").

**Amazon EMR 5.16.0 and later**

- Set the `hive.metastore` property to
  `glue` as shown in the following JSON
  example.

```
[
  {
    "Classification": "presto-connector-hive",
    "Properties": {
      "hive.metastore": "glue"
    }
  }
]
```

To specify a Data Catalog in a different AWS account, add the
`hive.metastore.glue.catalogid` property as shown
in the following JSON example. Replace
`acct-id` with the
AWS account of the Data Catalog. Using a Data Catalog in another
AWS account is not available using Amazon EMR version 5.15.0 and
earlier.

```
[
  {
    "Classification": "presto-connector-hive",
    "Properties": {
      "hive.metastore": "glue",
      "hive.metastore.glue.catalogid": "`acct-id`"
    }
  }
]
```

**Amazon EMR 5.10.0 through
5.15.0**

Set the `hive.metastore.glue.datacatalog.enabled`
property to `true`, as shown in the following JSON
example:

```
[
  {
    "Classification": "presto-connector-hive",
    "Properties": {
      "hive.metastore.glue.datacatalog.enabled": "true"
    }
  }
]
```

**Amazon EMR 6.1.0 and later using PrestoSQL
(Trino)**

Starting with EMR version 6.1.0, PrestoSQL also supports Glue
as the default Hive metastore. Use the
`prestosql-connector-hive` configuration
classification and set the `hive.metastore` property
to `glue`, as shown in the following JSON
example.

Amazon EMR versions 6.4.0 and later use the new name Trino instead
of PrestoSQL. If you use Trino, replace
`prestosql-connector-hive`
in the following configuration classification with
`trino-connector-hive`.

```
[
  {
    "Classification": "`prestosql-connector-hive`",
    "Properties": {
      "hive.metastore": "glue"
    }
  }
]
```

To switch metastores on a long-running cluster, you can manually set
these values as appropriate for your release version by connecting to
the master node, editing the property values in the
`/etc/presto/conf/catalog/hive.properties` file directly,
and restarting the Presto server (`sudo restart
 presto-server`). If you use this method with Amazon EMR 5.15.0 and
earlier, make sure that `hive.table-statistics-enabled` is
set to `false`. This setting is not required when using
release versions 5.16.0 and later; nevertheless, table and partition
statistics are not supported.

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

Consider the following items when using AWS Glue Data Catalog as a metastore with
Presto:

- Renaming tables from within AWS Glue is not supported.
- When you create a Hive table without specifying a `LOCATION`, the table data is stored in the location specified by the `hive.metastore.warehouse.dir` property. By default, this is a location in HDFS. If another cluster needs to access the table, it fails unless it has adequate permissions to the cluster that created the table. Furthermore, because HDFS storage is transient, if the cluster terminates, the table data is lost, and the table must be recreated. We recommend that you specify a `LOCATION` in Amazon S3 when you create a Hive table using AWS Glue. Alternatively, you can use the `hive-site` configuration classification to specify a location in Amazon S3 for `hive.metastore.warehouse.dir`, which applies to all Hive tables. If a table is created in an HDFS location and the cluster that created it is still running, you can update the table location to Amazon S3 from within AWS Glue. For more information, see [Working with Tables on the AWS Glue Console](../../../glue/latest/dg/console-tables.md "../../../glue/latest/dg/console-tables.md") in the _AWS Glue Developer Guide_.
- Partition values containing quotes and apostrophes are not supported, for example, `PARTITION (owner="Doe's").`
- [Column statistics](https://cwiki.apache.org/confluence/display/Hive/StatsDev#StatsDev-ColumnStatistics "https://cwiki.apache.org/confluence/display/Hive/StatsDev#StatsDev-ColumnStatistics") are supported for emr-5.31.0 and later.
- Using [Hive authorization](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Authorization "https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Authorization") is not supported. As an alternative, consider using [AWS Glue Resource-Based Policies](../../../glue/latest/dg/glue-resource-policies.md "../../../glue/latest/dg/glue-resource-policies.md"). For more information, see [Use Resource-Based Policies for Amazon EMR Access to AWS Glue Data Catalog](../ManagementGuide/emr-iam-roles-glue.md "../ManagementGuide/emr-iam-roles-glue.md").
