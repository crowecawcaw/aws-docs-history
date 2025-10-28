# Remove tags from an Amazon EMR cluster

If you no longer need a tag, you can remove it from the cluster.

Console

###### To remove tags on a cluster with the new

console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left navigation pane, choose
   **Clusters**, and select the cluster that
   you want to update.
3. On the **Tags** tab on the cluster details page, select
   **Manage tags**.
4. Choose **Remove** for each key-value pair that
   you want to remove.
5. Choose **Save changes**.

AWS CLI

###### To remove tags on a cluster with the AWS CLI

Type the `remove-tags`
subcommand with the `--tag-keys` parameter. When removing a tag, only the
key name is required.

- To remove a tag from a cluster, type the following command and replace
  `j-KT4XXXXXXXX1NM` with your cluster ID.

```
aws emr remove-tags --resource-id `j-KT4XXXXXX1NM` --tag-keys `"costCenter"`
```

###### Note

You cannot currently remove multiple tags using a single
command.

For more information on using Amazon EMR commands in the AWS CLI, see [https://docs.aws.amazon.com/cli/latest/reference/emr](../../../cli/latest/reference/emr.md "../../../cli/latest/reference/emr.md").
