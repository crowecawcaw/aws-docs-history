# Configuring an external metastore for

Hive

By default, Hive records metastore information in a MySQL database on the primary node's
file system. The metastore contains a description of the table and the underlying data on
which it is built, including the partition names, data types, and so on. When a cluster
terminates, all cluster nodes shut down, including the primary node. When this happens, local
data is lost because node file systems use ephemeral storage. If you need the metastore to
persist, you must create an _external metastore_ that exists outside the
cluster.

You have two options for an external metastore:

- AWS Glue Data Catalog (Amazon EMR release 5.8.0 or later only).

For more information, see [Using the AWS Glue Data Catalog as the metastore for
Hive](emr-hive-metastore-glue.md "emr-hive-metastore-glue.md").

- Amazon RDS or Amazon Aurora.

For more information, see [Using an external MySQL database or
Amazon Aurora](emr-hive-metastore-external.md "emr-hive-metastore-external.md").

###### Note

If you're using Hive 3 and encounter too many connections to Hive metastore, configure the
parameter `datanucleus.connectionPool.maxPoolSize` to have a smaller value or
increase the number of connection the database server can handle. The increased number
of connections is due to the way Hive computes the maximum number of JDBC connections.
To calculate the optimal value for performance, see [Hive Configuration Properties](https://cwiki.apache.org/confluence/display/Hive/Configuration+Properties#ConfigurationProperties-datanucleus.connectionPool.maxPoolSize.1 "https://cwiki.apache.org/confluence/display/Hive/Configuration+Properties#ConfigurationProperties-datanucleus.connectionPool.maxPoolSize.1").
