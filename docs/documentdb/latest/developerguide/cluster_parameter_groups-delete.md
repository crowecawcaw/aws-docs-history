# Deleting Amazon DocumentDB cluster parameter groups

You can delete a custom Amazon DocumentDB cluster parameter group using the AWS Management Console or the
AWS Command Line Interface (AWS CLI). You can't delete the `default.docdb4.0` cluster parameter
group.

Using the AWS Management Console

###### To delete a cluster parameter group

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. In the navigation pane, choose **Parameter groups**.

###### Tip

If you don't see the navigation pane on the left side of your screen, choose the menu icon
(![Hamburger menu icon with three horizontal lines.](images/docdb-menu-icon.png))
in the upper-left corner of the page. 3. In the **Parameter groups** pane, choose the radio button to the left of the cluster parameter group that you want to
delete. 4. Choose **Actions**, and then choose
**Delete**. 5. In the **Delete** confirmation pane, choose
**Delete** to delete the cluster parameter group. To keep
the cluster parameter group, choose **Cancel**.

Using the AWS CLI
To delete a cluster parameter group, use the `delete-db-cluster-parameter-group` operation with the following parameter.

- `--db-cluster-parameter-group-name`
  — Required. The name of the cluster parameter group to delete. This must
  be an existing cluster parameter group. _You cannot delete the
  `default.docdb4.0` cluster parameter group._

###### Example - Deleting a cluster parameter group

The following example walks you through the three steps for deleting a cluster
parameter group:

1. Finding the name of the cluster parameter group that you want to
   delete.
2. Deleting the specified cluster parameter group.
3. Verifying that the cluster parameter group was deleted.

###### 1. Find the name of the cluster parameter group that you want to

delete.

The following code lists the names of all cluster parameter groups.

For Linux, macOS, or Unix:

```
aws docdb describe-db-cluster-parameter-groups \
       --query 'DBClusterParameterGroups[*].[DBClusterParameterGroupName]'
```

For Windows:

```
aws docdb describe-db-cluster-parameter-groups ^
       --query 'DBClusterParameterGroups[*].[DBClusterParameterGroupName]'
```

The output of the preceding operation is a list the names of cluster parameter
groups similar to the following (JSON format).

```
[
       [
           "default.docdb4.0"
       ],
       [
           "sample-parameter-group"
       ],
       [
           "sample-parameter-group-copy"
       ]
   ]
```

###### 2. Delete a specific cluster parameter group.

The following code deletes the cluster parameter group
`sample-parameter-group-copy`.

For Linux, macOS, or Unix:

```
aws docdb delete-db-cluster-parameter-group \
       --db-cluster-parameter-group-name `sample-parameter-group-copy`
```

For Windows:

```
aws docdb delete-db-cluster-parameter-group ^
       --db-cluster-parameter-group-name `sample-parameter-group-copy`
```

There is no output from this operation.

###### 3. Verify that the specified cluster parameter group was deleted.

The following code lists the names of all remaining cluster parameter
groups.

For Linux, macOS, or Unix:

```
aws docdb describe-db-cluster-parameter-groups \
       --query 'DBClusterParameterGroups[*].[DBClusterParameterGroupName]'
```

For Windows:

```
aws docdb describe-db-cluster-parameter-groups ^
       --query 'DBClusterParameterGroups[*].[DBClusterParameterGroupName]'
```

The output of the preceding operation is a list of cluster parameter groups
similar to the following (JSON format). The cluster parameter group that you just
deleted should not be in the list.

Output from this operation looks something like the following (JSON format).

```
[
       [
           "default.docdb4.0"
       ],
       [
           "sample-parameter-group"
       ]
   ]
```
