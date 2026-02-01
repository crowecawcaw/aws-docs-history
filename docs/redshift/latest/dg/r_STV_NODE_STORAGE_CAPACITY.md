Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STV_NODE_STORAGE_CAPACITY

The STV_NODE_STORAGE_CAPACITY table shows details of total storage capacity and total used capacity for each node in a cluster.
It contains a row for each node.

STV_NODE_STORAGE_CAPACITY is visible only to superusers. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name | Data type | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| node        | integer   | The node number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| used        | integer   | The number of 1 MB disk blocks currently in use on<br>the node. For RA3 node types, used blocks include both locally<br>cached blocks and blocks persisted in Amazon S3.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| capacity    | integer   | The total storage capacity provisioned for the node in 1 MB blocks.<br>The capacity includes space that is reserved by Amazon Redshift on<br>DC2 node types for internal use.<br>The capacity is larger than the nominal node capacity, which is the amount of node space available for user data.<br>For RA3 node types, this capacity is the same as the total managed storage quota for the cluster.<br>For more information about capacity by node type, see<br>[Node type details](../mgmt/working-with-clusters.md#working-with-clusters-overview "../mgmt/working-with-clusters.md#working-with-clusters-overview") in the _Amazon Redshift Management Guide_. |

## Sample queries

###### Note

The results of the following examples vary based on the node specifications of your cluster.
Add column `capacity` to your SQL SELECT to retrieve the capacity of your cluster.

The following query returns used space and total capacity in 1 MB disk blocks.
This example ran on a two-node dc2.8xlarge cluster.

```
select node, used from stv_node_storage_capacity order by node;
```

This query returns the following sample output.

```

 node | used
------+-------
    0 | 30597
    1 | 27089

```

The following query returns used space and total capacity in 1 MB disk blocks.
This example ran on a two-node ra3.16xlarge cluster.

```
select node, used from stv_node_storage_capacity order by node;
```

This query returns the following sample output.

```

 node | used
------+-------
    0 | 30591
    1 | 27103

```
