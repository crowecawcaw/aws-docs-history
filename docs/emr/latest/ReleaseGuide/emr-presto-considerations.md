# Considerations with Presto on

Amazon EMR

Consider the following limitations when you run [Presto](https://aws.amazon.com/big-data/what-is-presto/ "https://aws.amazon.com/big-data/what-is-presto/") on
Amazon EMR.

## Presto command line executable

In Amazon EMR, PrestoDB and Trino both use the same command line executable,
`presto-cli`, as in the following example.

```
presto-cli --catalog hive
```

## Non-configurable Presto deployment

properties

The version of Amazon EMR that you use determines the Presto deployment configurations
that are available. For more information about these configuration properties, see
[Deploying Presto](https://prestodb.io/docs/current/installation/deployment.html "https://prestodb.io/docs/current/installation/deployment.html") in the Presto documentation. The following table shows
the different configuration options for Presto `properties` files.

| File                | Configurable                                                                                                                       |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `log.properties`    | PrestoDB: Configurable in Amazon EMR versions 4.0.0 and later. Use<br>the `presto-log` configuration classification.               |
| `config.properties` | PrestoDB: Configurable in Amazon EMR versions 4.0.0 and later. Use<br>the `presto-config` configuration<br>classification.         |
| `hive.properties`   | PrestoDB: Configurable in Amazon EMR versions 4.1.0 and later. Use<br>the `presto-connector-hive` configuration<br>classification. |
| `node.properties`   | PrestoDB: Configurable in Amazon EMR version 5.6.0 and later. Use<br>the `presto-node` configuration<br>classification.            |
| `jvm.config`        | Not configurable.                                                                                                                  |

## PrestoDB installation

The application name _Presto_ continues to be used to install
PrestoDB on clusters.

You can install either PrestoDB or Trino, but you can't install both on a single
cluster. If you specify both PrestoDB and Trino when you attempt to create a
cluster, a validation error occurs and the cluster creation request fails.

## EMRFS and PrestoS3FileSystem

configuration

With Amazon EMR versions 5.12.0 and later, PrestoDB can use EMRFS. For more information, see [EMR File System (EMRFS)](emr-fs.md "emr-fs.md") in the
_Amazon EMR Management Guide_. With earlier versions of Amazon EMR,
PrestoS3FileSystem is the only configuration option.

You can use a security configuration to set up encryption for EMRFS data in Amazon S3.
You can also use IAM roles for EMRFS requests to Amazon S3. For more information, see
[Understanding
encryption options](../ManagementGuide/emr-data-encryption-options.md "../ManagementGuide/emr-data-encryption-options.md") and [Configure IAM roles for EMRFS
requests to Amazon S3](../ManagementGuide/emr-emrfs-iam-roles.md "../ManagementGuide/emr-emrfs-iam-roles.md") in the _Amazon EMR Management Guide_.

###### Note

If you query underlying data in Amazon S3 with Amazon EMR version 5.12.0, Presto errors
can occur. This is because Presto fails to pick up configuration classification
values from `emrfs-site.xml`. As a workaround, create an
`emrfs` subdirectory under
`usr/lib/presto/plugin/hive-hadoop2/` and create a symlink in
`usr/lib/presto/plugin/hive-hadoop2/emrfs` to the existing
`/usr/share/aws/emr/emrfs/conf/emrfs-site.xml` file. Then restart
the presto-server process (`sudo presto-server stop` followed by
`sudo presto-server start`).

You can override the EMRFS default and use the PrestoS3FileSystem instead. To do
this, use the `presto-connector-hive` configuration classification to set
`hive.s3-file-system-type` to `PRESTO` as shown in the
following example. For more information, see [Configure applications](emr-configure-apps.md "emr-configure-apps.md").

```
[
   {
      "Classification": "presto-connector-hive",
      "Properties": {
         "hive.s3-file-system-type": "PRESTO"
      }
   }
]
```

If you use PrestoS3FileSystem, use the `presto-connector-hive`
configuration classification to
configure PrestoS3FileSystem properties. For more information about available
properties, see [Amazon S3 configuration](https://prestodb.io/docs/current/connector/hive.html#amazon-s3-configuration "https://prestodb.io/docs/current/connector/hive.html#amazon-s3-configuration") in the Hive Connector section of the Presto
documentation. These settings do not apply to EMRFS.

## Default setting for end user

impersonation

By default, Amazon EMR versions 5.12.0 and later enable end user impersonation for
access to HDFS. For more information, see [End user impersonation](https://prestodb.io/docs/current/connector/hive-security.html#end-user-impersonation "https://prestodb.io/docs/current/connector/hive-security.html#end-user-impersonation") in the Presto documentation. To change this
setting with the `presto-config` configuration classification, set the
`hive.hdfs.impersonation.enabled` property to
`false`.

## Default port for Presto web

interface

By default, Amazon EMR configures the Presto web interface on the Presto coordinator to
use port 8889 (for PrestoDB and Trino). To change the port, use the
`presto-config` configuration classification to set the
`http-server.http.port` property. For more information, see [Config properties](https://prestodb.io/docs/current/installation/deployment.html#config-properties "https://prestodb.io/docs/current/installation/deployment.html#config-properties") in the _Deploying Presto_ section
of Presto Documentation.

## Issue with Hive Bucket execution in

some releases

Presto version 152.3 has an issue with Hive bucket execution that causes
significantly slower Presto query performance in some circumstances. Amazon EMR versions
5.0.3, 5.1.0, and 5.2.0 include this version of Presto. To mitigate this issue, use
the `presto-connector-hive` configuration classification to set the
`hive.bucket-execution` property to `false`, as shown in
the following example.

```
[
   {
      "Classification": "presto-connector-hive",
      "Properties": {
         "hive.bucket-execution": "false"
      }
   }
]
```
