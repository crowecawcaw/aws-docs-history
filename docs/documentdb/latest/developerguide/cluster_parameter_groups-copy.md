# Copying Amazon DocumentDB cluster parameter groups

You can make a copy of a cluster parameter group in Amazon DocumentDB using the AWS Management Console or the
AWS Command Line Interface (AWS CLI).

Using the AWS Management Console
The following procedure guides you through making a new cluster parameter group by making a copy of an existing cluster parameter group.

###### To copy a cluster parameter group

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. In the navigation pane, choose **Parameter groups**.
3. In the **Cluster parameter groups** pane, choose the name of the cluster
   parameter group that you want to copy.
4. Choose **Actions**, and then choose **Copy** to copy that
   parameter group.
5. Under **Copy options**, enter a name and description for the new cluster
   parameter group. Then choose **Copy** to save your
   changes.

Using the AWS CLI
To make a copy of a cluster parameter group, use the `copy-db-cluster-parameter-group` operation with the following parameters.

- `--source-db-cluster-parameter-group-identifier` — Required. The name or Amazon Resource Name
  (ARN) of the cluster parameter group that you want to make a copy of.

If the source and target cluster parameter groups are in the same AWS Region, the identifier can be either a name or an ARN.

If the source and target cluster parameter groups are in different AWS Regions, the identifier must be an ARN.

- `--target-db-cluster-parameter-group-identifier` — Required. The name or ARN of the cluster
  parameter group copy.

Constraints:

    + Cannot be null, empty, or blank.
    + Must contain 1–255 letters, numbers, or hyphens.
    + First character must be a letter.
    + Cannot end with a hyphen or contain two consecutive hyphens.

- `--target-db-cluster-parameter-group-description` — Required. A user-supplied description for
  the cluster parameter group copy.

###### Example

The following code makes a copy of `sample-parameter-group`, naming the copy `sample-parameter-group-copy`.

For Linux, macOS, or Unix:

```
aws docdb copy-db-cluster-parameter-group \
    --source-db-cluster-parameter-group-identifier `sample-parameter-group` \
    --target-db-cluster-parameter-group-identifier `sample-parameter-group-copy` \
    --target-db-cluster-parameter-group-description "`Copy of sample-parameter-group`"
```

For Windows:

```
aws docdb copy-db-cluster-parameter-group ^
    --source-db-cluster-parameter-group-identifier `sample-parameter-group` ^
    --target-db-cluster-parameter-group-identifier `sample-parameter-group-copy` ^
    --target-db-cluster-parameter-group-description "`Copy of sample-parameter-group`"
```

Output from this operation looks something like the following (JSON format).

```
{
    "DBClusterParameterGroup": {
        "DBClusterParameterGroupArn": "arn:aws:rds:us-east-1:123456789012:cluster-pg:sample-parameter-group-copy",
        "DBClusterParameterGroupName": "sample-parameter-group-copy",
        "DBParameterGroupFamily": "docdb4.0",
        "Description": "Copy of sample-parameter-group"
    }
}
```
