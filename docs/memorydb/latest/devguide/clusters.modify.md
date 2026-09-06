

# Modifying a MemoryDB cluster
<a name="clusters.modify"></a>

In addition to adding or removing nodes from a cluster, there can be times where you need to make other changes to an existing cluster, such as adding a security group, changing the maintenance window or a parameter group.

We recommend that you have your maintenance window fall at the time of lowest usage. Thus it might need modification from time to time.

When you change a cluster's parameters, the change is applied to the cluster immediately. This is true whether you change the cluster's parameter group itself or a parameter value within the cluster's parameter group.

You can also update your clusters' engine version. For example, you can select a new engine minor version and MemoryDB will start updating your cluster immediately. 

## Using the AWS Management Console
<a name="clusters.modifyclusters.viewdetails"></a>

**To modify a cluster**

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/).

1. From the list in the upper-right corner, choose the AWS Region where the cluster that you want to modify is located.

1. From the left navigation, go to **Clusters**. From **Clusters detail**, select the cluster using the radio button and go to **Actions** and then **Modify**. 

1. The **Modify** page appears.

1. In the **Modify** window, make the modifications that you want. Options include:
   + Description
   + Subnet groups
   + VPC Security Group(s)
   + Node type
**Note**  
If the cluster is using a node type from the r6gd family, you can only choose a different node size from within that family. If you choose a node type from the r6gd family, data tiering will automatically be enabled. For more information, see [Data tiering](data-tiering.md).
   + Valkey or Redis OSS version compatibility
   + Enable Automatic snapshots
   + Snapshot Retention Period
   + Snapshot Window
   + Maintenance window
   + Topic for SNS Notification

1. Choose **Save changes**.

You can also go to the **Cluster details** page and click on **modify** to make modifications to the cluster. If you want to modify specific sections of the cluster, you can go to the respective tab in the **Cluster details** page and click **Modify**. 

## Using the AWS CLI
<a name="clusters.modify.cli"></a>

You can modify an existing cluster using the AWS CLI `update-cluster` operation. To modify a cluster's configuration value, specify the cluster's ID, the parameter to change and the parameter's new value. The following example changes the maintenance window for a cluster named `my-cluster` and applies the change immediately.

For Linux, macOS, or Unix:

```
aws memorydb update-cluster \
    --cluster-name {{my-cluster}} \
    --preferred-maintenance-window {{sun:23:00-mon:02:00}}
```

For Windows:

```
aws memorydb update-cluster ^
    --cluster-name {{my-cluster}} ^
    --preferred-maintenance-window {{sun:23:00-mon:02:00}}
```

For more information, see [update-cluster](https://docs.aws.amazon.com/cli/latest/reference/memorydb/update-cluster.html) in the AWS CLI Command Reference.

## Using the MemoryDB API
<a name="clusters.modify.api"></a>

You can modify an existing cluster using the MemoryDB API [UpdateCluster](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UpdateCluster.html) operation. To modify a cluster's configuration value, specify the cluster's ID, the parameter to change and the parameter's new value. The following example changes the maintenance window for a cluster named `my-cluster` and applies the change immediately.

```
https://memory-db.us-east-1.amazonaws.com/
    ?Action=UpdateCluster
    &ClusterName=my-cluster
    &PreferredMaintenanceWindow=sun:23:00-mon:02:00
    &SignatureVersion=4
    &SignatureMethod=HmacSHA256
    &Timestamp=20210801T220302Z
    &X-Amz-Algorithm=Amazon4-HMAC-SHA256
    &X-Amz-Date=20210802T220302Z
    &X-Amz-SignedHeaders=Host
    &X-Amz-Expires=20210801T220302Z
    &X-Amz-Credential=<credential>
    &X-Amz-Signature=<signature>
```

## How to trigger a cross-engine upgrade from Redis OSS to Valkey
<a name="clusters.modifyclusters.cross-engine"></a>

You can upgrade an existing Redis OSS cluster to the Valkey engine using Console, API or CLI. 

If you have an existing Redis OSS cluster that is using the default parameter group, you can upgrade to Valkey by specifying the new engine and engine version with update-cluster API.

For Linux, macOS, or Unix:

```
aws memorydb update-cluster \
   --cluster-name myCluster \
   --engine valkey \
   --engine-version 7.2
```

For Windows:

```
aws memorydb update-cluster ^
   --cluster-name myCluster ^
   --engine valkey ^
   --engine-version 7.2
```

If you have a custom parameter group applied to the existing Redis OSS cluster you wish to upgrade, you will need to pass a custom Valkey parameter group in the request as well. The input Valkey custom parameter group must have the same Redis OSS static parameter values as the existing Redis OSS custom parameter group.

For Linux, macOS, or Unix:

```
aws memorydb update-cluster \
   --cluster-name myCluster \
   --engine valkey \
   --engine-version 7.2 \
   --parameter-group-name myParamGroup
```

For Windows:

```
aws memorydb update-cluster ^
   --cluster-name myCluster ^
   --engine valkey ^
   --engine-version 7.2 ^
   --parameter-group-name myParamGroup
```