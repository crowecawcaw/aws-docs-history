# Add tags to an Amazon EMR cluster

You can add tags to a cluster when you create it.

Console

###### To add tags when you create a cluster with the new

console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left navigation pane, choose
   **Clusters**, and then choose
   **Create cluster**.
3. Under **Tags**, choose **Add new
   tag**. Specify a tag in the **Key**
   field. Optionally, specify a tag in the **Value**
   field.
4. Choose any other options that apply to your cluster.
5. To launch your cluster, choose **Create
   cluster**.

AWS CLI

###### To add tags when you create a cluster with the the AWS CLI

The following example demonstrates how to add a tag to a new cluster using the
AWS CLI. To add tags when you create a cluster, type the `create-cluster`
subcommand with the `--tags` parameter.

- To add a tag named `costCenter` with key value
  `marketing` when you create a cluster, type the
  following command and replace `myKey` with the name of
  your EC2 key pair.

```
aws emr create-cluster --name `"Test cluster"` --release-label `emr-4.0.0` --applications Name=`Hadoop` Name=`Hive` Name=`Pig` --tags `"costCenter=marketing"` --use-default-roles --ec2-attributes KeyName=`myKey` --instance-type `m5.xlarge` --instance-count `3`
```

When you specify the instance count without using the
`--instance-groups` parameter, a single Master node is launched,
and the remaining instances are launched as core nodes. All nodes will use the
instance type specified in the command.

###### Note

If you have not previously created the default EMR service role and
EC2 instance profile, type aws `emr create-default-roles` to
create them before typing the `create-cluster`
subcommand.

For more information on using Amazon EMR commands in the AWS CLI, see [https://docs.aws.amazon.com/cli/latest/reference/emr](../../../cli/latest/reference/emr.md "../../../cli/latest/reference/emr.md").

You can also add tags to an existing cluster.

Console

###### To add tags to an existing cluster with the new

console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left navigation pane, choose
   **Clusters**, and select the cluster that
   you want to update.
3. On the **Tags** tab on the cluster details page,
   select **Manage tags**. Specify a tag in the
   **Key** field. Optionally, specify a tag in the
   **Value** field.
4. Select **Save changes**. The
   **Tags** tab updates with the new number of
   tags that you have on your cluster. For example, if you now have two
   tags, the label of your tab is **Tags (2)**.

AWS CLI

###### To add tags to a running cluster with the AWS CLI

- Enter the `add-tags` subcommand with the
  `--tag` parameter to assign tags to the cluster ID.
  You can find the cluster ID using the console or the
  `list-clusters` command. The `add-tags`
  subcommand currently accepts only one resource ID.

For example, to add two tags to a running cluster one with a key
named `costCenter` with a value of
`marketing` and another named
`other` with a value of
`accounting`, enter the following
command and replace `j-KT4XXXXXXXX1NM` with
your cluster ID.

```
aws emr add-tags --resource-id `j-KT4XXXXXXXX1NM` --tag `"costCenter=marketing"` --tag `"other=accounting"`
```

Note that when tags are added using the AWS CLI, there's no
output from the command. For more information on using Amazon EMR
commands in the AWS CLI, see [https://docs.aws.amazon.com/cli/latest/reference/emr](../../../cli/latest/reference/emr.md "../../../cli/latest/reference/emr.md").
