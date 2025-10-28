# Supported applications with Amazon EMR

Within an EMR cluster, Kerberos principals are the big data application services
and subsystems that run on all cluster nodes. Amazon EMR can configure the applications
and components listed below to use Kerberos. Each application has a Kerberos user
principal associated with it.

Amazon EMR does not support cross-realm trusts with
AWS Directory Service for Microsoft Active Directory.

Amazon EMR only configures the open-source Kerberos authentication features for the
applications and components listed below. Any other applications installed are not
Kerberized, which can result in an inability to communicate with Kerberized
components and cause application errors. Applications and components that are not
Kerberized do not have authentication enabled. Supported applications and components
may vary for different Amazon EMR releases.

The Livy user interface is the only web user interface hosted on the cluster that
is Kerberized.

- **Hadoop MapReduce**
- **Hbase**
- **HCatalog**
- **HDFS**
- **Hive**
  - Do not enable Hive with LDAP authentication. This may cause issues
    communicating with Kerberized YARN.

- **Hue**
  - Hue user authentication isn't set automatically and can be
    configured using the configuration API.
  - Hue server is Kerberized. The Hue front-end (UI) is not configured
    for authentication. LDAP authentication can be configured for the
    Hue UI.

- **Livy**
  - Livy impersonation with Kerberized clusters is supported in Amazon EMR
    releases 5.22.0 and higher.

- **Oozie**
- **Phoenix**
- **Presto**
  - Presto supports Kerberos authentication in Amazon EMR releases 6.9.0
    and higher.
  - To use Kerberos authentication for Presto, you must enable
    [in-transit encryption](emr-data-encryption-options.md#emr-encryption-intransit "emr-data-encryption-options.md#emr-encryption-intransit").

- **Spark**
- **Tez**
- **Trino**
  - Trino supports Kerberos authentication in Amazon EMR releases 6.11.0
    and higher.
  - To use Kerberos authentication for Trino, you must enable
    [in-transit encryption](emr-data-encryption-options.md#emr-encryption-intransit "emr-data-encryption-options.md#emr-encryption-intransit").

- **YARN**
- **Zeppelin**
  - Zeppelin is only configured to use Kerberos with the Spark
    interpreter. It is not configured for other interpreters.
  - User impersonation is not supported for Kerberized Zeppelin
    interpreters other than Spark.

- **Zookeeper**
  - Zookeeper client is not supported.
