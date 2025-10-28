# View tags on an Amazon EMR cluster

If you want to see all tags associated with a cluster, you can view them with
the console or the AWS CLI.

Console

###### To view tags on a cluster with the new

console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left navigation pane, choose
   **Clusters**, and select the cluster that
   you want to update.
3. To view all of your tags, select the **Tags** tab
   on the cluster details page.

AWS CLI

###### To view tags on a cluster with the AWS CLI

To view the tags on a cluster using the AWS CLI, type the
`describe-cluster` subcommand with the
`--query` parameter.

- To view a cluster's tags, type the following command and replace
  `j-KT4XXXXXXXX1NM` with your cluster
  ID.

```
aws emr describe-cluster --cluster-id `j-KT4XXXXXX1NM` --query Cluster.Tags
```

The output displays all the tag information about the cluster
similar to the following:

```
Value: accounting     Value: marketing
Key: other            Key: costCenter
```

For more information on using Amazon EMR commands in the AWS CLI, see
[https://docs.aws.amazon.com/cli/latest/reference/emr](../../../cli/latest/reference/emr.md "../../../cli/latest/reference/emr.md").
