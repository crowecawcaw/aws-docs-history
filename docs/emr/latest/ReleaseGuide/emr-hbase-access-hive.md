# Access HBase tables with Hive

HBase and [Apache Hive](emr-hive.md "emr-hive.md") are tightly
integrated, allowing you run massively parallel processing workloads directly on data
stored in HBase. To use Hive with HBase, you can usually launch them on the same
cluster. You can, however, launch Hive and HBase on separate clusters. Running HBase and
Hive separately on different clusters can improve performance because this allows each
application to use cluster resources more efficiently.

The following procedures show how to connect to HBase on a cluster using Hive.

###### Note

You can only connect a Hive cluster to a single HBase cluster.

###### To connect Hive to HBase

1. Create separate clusters with Hive and HBase installed or create a single cluster with
   both HBase and Hive installed.
2. If you are using separate clusters, modify your security groups so that HBase and Hive
   ports are open between these two primary nodes.
3. Use SSH to connect to the primary node for the cluster with Hive installed. For
   more information, see [Connect to the primary node using SSH](../ManagementGuide/emr-connect-master-node-ssh.md "../ManagementGuide/emr-connect-master-node-ssh.md") in the _Amazon EMR Management Guide_.
4. Launch the Hive shell with the following command.

```

hive
```

5. (Optional) You do not need to do this if HBase and Hive are located on the same cluster.
   Connect the HBase client on your Hive cluster to the HBase cluster that contains
   your data. In the following example, `public-DNS-name`
   is replaced by the public DNS name of the primary node of the HBase cluster, for
   example: `ec2-50-19-76-67.compute-1.amazonaws.com`.

```

set hbase.zookeeper.quorum=`public-DNS-name`;

```

6. Proceed to run Hive queries on your HBase data as desired or see the next
   procedure.

###### To access HBase data from Hive

- After the connection between the Hive and HBase clusters has been made (as
  shown in the previous procedure), you can access the data stored on the HBase
  cluster by creating an external table in Hive.

The following example, when run from the Hive prompt on the primary node, creates an external
table that references data stored in an HBase table called
`inputTable`. You can then reference `inputTable` in
Hive statements to query and modify data stored in the HBase cluster.

```

set hbase.zookeeper.quorum=ec2-107-21-163-157.compute-1.amazonaws.com;

create external table inputTable (key string, value string)
     stored by 'org.apache.hadoop.hive.hbase.HBaseStorageHandler'
      with serdeproperties ("hbase.columns.mapping" = ":key,f1:col1")
      tblproperties ("hbase.table.name" = "t1");

select count(key) from inputTable ;
```

For a more advanced use case and example combining HBase and Hive, see the AWS Big
Data Blog post, [Combine NoSQL and massively parallel analytics using Apache HBase and Apache Hive
on Amazon EMR](https://aws.amazon.com/blogs/big-data/combine-nosql-and-massively-parallel-analytics-using-apache-hbase-and-apache-hive-on-amazon-emr "https://aws.amazon.com/blogs/big-data/combine-nosql-and-massively-parallel-analytics-using-apache-hbase-and-apache-hive-on-amazon-emr").
