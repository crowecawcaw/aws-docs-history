

# Monitoring an Amazon DocumentDB cluster's status
<a name="monitoring_docdb-cluster_status"></a>

The status of a cluster indicates the health of the cluster. You can view the status of a cluster by using the Amazon DocumentDB console or the AWS CLI `describe-db-clusters` command.

**Topics**
+ [Cluster status values](#monitoring_docdb-status_values)
+ [Monitoring a cluster's status](#monitor-cluster-status)

## Cluster status values
<a name="monitoring_docdb-status_values"></a>

The following table lists the valid values for a cluster's status.


| Cluster Status | Description | 
| --- | --- | 
| active | The cluster is active. This status applies to elastic clusters only. | 
| available | The cluster is healthy and available. This status applies to instance-based clusters only. | 
| backing-up | The cluster is currently being backed up. | 
| creating | The cluster is being created. It is inaccessible while it is being created. | 
| deleting | The cluster is being deleted. It is inaccessible while it is being deleted. | 
| failing-over | A failover from the primary instance to an Amazon DocumentDB replica is being performed. | 
| inaccessible-encryption-credentials | The AWS KMS key used to encrypt or decrypt the cluster can't be accessed. | 
| maintenance | A maintenance update is being applied to the cluster. This status is used for cluster-level maintenance that Amazon DocumentDB schedules well in advance. | 
| migrating | A cluster snapshot is being restored to a cluster. | 
| migration-failed | A migration failed. | 
| modifying | The cluster is being modified because of a customer request to modify the cluster. | 
| renaming | The cluster is being renamed because of a customer request to rename it. | 
| resetting-master-credentials | The master credentials for the cluster are being reset because of a customer request to reset them. | 
| upgrading | The cluster engine version is being upgraded. | 

## Monitoring a cluster's status
<a name="monitor-cluster-status"></a>

------
#### [ Using the AWS Management Console ]

When using the AWS Management Console to determine the status of a cluster, use the following procedure.

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb).

1. In the navigation pane, choose **Clusters**.

1. In the Clusters navigation box, you'll see the column **Cluster identifier**. Your instances are listed under clusters, similar to the following screenshot.  
![Clusters table showing how an instance is nested under a cluster.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/choose-clusters.png)

1. In the **Cluster identifier** column, find the name of the instance that you are interested in. Then, to find the status of the instance, read across that row to the **Status** column, as shown below.  
![Cluster instance showing available status.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/db-cluster-status-con.png)

------
#### [ Using the AWS CLI ]

When using the AWS CLI to determine the status of a cluster, use the `describe-db-clusters` operation. The following code finds the status of the cluster `sample-cluster`.

For Linux, macOS, or Unix:

```
aws docdb describe-db-clusters \
    --db-cluster-identifier sample-cluster  \
    --query 'DBClusters[*].[DBClusterIdentifier,Status]'
```

For Windows:

```
aws docdb describe-db-clusters ^
    --db-cluster-identifier sample-cluster  ^
    --query 'DBClusters[*].[DBClusterIdentifier,Status]'
```

Output from this operation looks something like the following.

```
[
    [
        "sample-cluster",
        "available"
    ]
]
```

------