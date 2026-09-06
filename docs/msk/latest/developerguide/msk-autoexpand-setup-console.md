

# Set up automatic scaling using the Amazon MSK AWS Management Console
<a name="msk-autoexpand-setup-console"></a>

This process describes how to use the Amazon MSK console to implement automatic scaling for storage.

1. Sign in to the AWS Management Console, and open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1\#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/).

1. In the list of clusters, choose your cluster. This takes you to a page that lists details about the cluster.

1. In the **Auto scaling for storage** section, choose **Configure**.

1. Create and name an auto-scaling policy. Specify the storage utilization target, the maximum storage capacity, and the target metric.

1. Choose `Save changes`.

When you save and enable the new policy, the policy becomes active for the cluster. Amazon MSK then expands the cluster's storage when the storage utilization target is reached.