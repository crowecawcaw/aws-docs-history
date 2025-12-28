# Creating Amazon DocumentDB cluster parameter groups

Default cluster parameter groups such as `default.docdb5.0`, `default.docdb4.0`, or `default.docdb3.6`, are created when you create a cluster with a new engine version and in a new region.
Subsequent clusters created in this region and with the same engine version inherit the `default` cluster parameter group.
Once created, the `default` parameter groups cannot be deleted or renamed.
You can modify the engine behavior of cluster instances by creating a custom parameter group with preferred parameter values and attaching it to your Amazon DocumentDB cluster.

The following procedure guides you through creating a custom cluster parameter group.
You can then [modify the parameters within that parameter group](cluster_parameter_groups-modify.md "cluster_parameter_groups-modify.md").

###### Note

After you create a cluster parameter group, you should wait at least 5 minutes before using that particular parameter group.
This allows Amazon DocumentDB to fully complete the `create` action before the cluster parameter group is used for a new cluster. You can use the AWS Management Console or the `describe-db-cluster-parameter-groups` AWS CLI operation to verify that your cluster parameter group has been created. For more information, see [Describing Amazon DocumentDB cluster parameter groups](cluster_parameter_groups-describe.md "cluster_parameter_groups-describe.md").

Using the AWS Management Console

###### To create a cluster parameter group

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. In the navigation pane, choose **Parameter groups**.

###### Tip

If you don't see the navigation pane on the left side of your screen, choose the menu icon
(![Hamburger menu icon with three horizontal lines.](/images/documentdb/latest/developerguide/images/docdb-menu-icon.png))
in the upper-left corner of the page. 3. In the **Cluster parameter groups** pane, choose **Create**. 4. In the **Create cluster parameter group** pane, enter the following:

    1. **New cluster parameter group name** — Enter a name for the cluster parameter group. For example, `sample-parameter-group`. Cluster parameter groups have the following naming constraints:




    	* Length is [1–255] alphanumeric characters.
    	* First character must be a letter.
    	* Cannot end with a hyphen or contain two consecutive hyphens.
    2. **Family** — Choose a DocumentDB version you intend to use for your cluster.
    3. **Description** — Provide a description for this cluster parameter
     group.

5. To create the cluster parameter group, choose **Create**. To cancel the operation, choose **Cancel**.
6. After you choose **Create**, the following text appears at the top of the page to verify that your cluster parameter group has been successfully created:

```
Successfully created cluster parameter group 'sample-parameter-group'.
```

Using the AWS CLI
To create a new cluster parameter group for Amazon DocumentDB 4.0 clusters, use the AWS CLI `create-db-cluster-parameter-group` operation with the following parameters:

- `--db-cluster-parameter-group-name`
  — The name of the custom cluster parameter group. For example, `sample-parameter-group`.
- `--db-cluster-parameter-group-family`
  — The cluster parameter group family that is used as the template for the custom cluster parameter group.
- `--description` — The user-provided
  description for this cluster parameter group. The following example uses
  "`Custom docdb4.0 parameter group`".

For Linux, macOS, or Unix:

```
aws docdb create-db-cluster-parameter-group \
 --db-cluster-parameter-group-name `sample-parameter-group` \
 --db-parameter-group-family docdb5.0 \
 --description "`Custom docdb5.0 parameter group`"
```

For Windows:

```
aws docdb create-db-cluster-parameter-group ^
 --db-cluster-parameter-group-name `sample-parameter-group` ^
 --db-parameter-group-family docdb5.0 ^
 --description "`Custom docdb5.0 parameter group`"
```

Output from this operation looks something like the following (JSON format).

```
{
    "DBClusterParameterGroup": {
        "DBClusterParameterGroupName": "`sample-parameter-group`",
        "DBParameterGroupFamily": "docdb5.0",
        "Description": "`Custom docdb4.0 parameter group`",
        "DBClusterParameterGroupArn": "`sample-parameter-group-arn`"
    }
}
```
