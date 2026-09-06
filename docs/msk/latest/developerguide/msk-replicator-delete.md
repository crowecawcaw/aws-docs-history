

# Delete a replicator
<a name="msk-replicator-delete"></a>

You may need to delete an MSK Replicator if it fails to create (FAILED status). The source and target clusters assigned to an MSK Replicator cannot be changed once the MSK Replicator is created. You can delete an existing MSK Replicator and create a new one. If you create a new MSK Replicator to replace the deleted one, the new Replicator starts replication from the latest offset.

1. In the AWS Region where your target cluster is located, sign in to the AWS Management Console, and open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1\#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/).

1. In the navigation pane, select **Replicators**.

1. From the list of MSK Replicators, select the one you want to delete and choose **Delete**.