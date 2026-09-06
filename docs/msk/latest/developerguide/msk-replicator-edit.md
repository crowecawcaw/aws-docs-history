

# Edit a replicator
<a name="msk-replicator-edit"></a>

You cannot change the source cluster, target cluster, Replicator starting position, or topic name replication configuration once the MSK Replicator has been created. You need to create a new replicator to change these settings. However, you can edit other Replicator settings, such as topics and consumer groups to replicate.

1. Sign in to the AWS Management Console, and open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1\#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/).

1. In the left navigation pane, choose **Replicators** and select the MSK Replicator you want to edit.

1. Choose the **Properties** tab.

1. In the **Replicator settings** section, choose **Edit replicator**.

1. You can edit the following settings:
   + Topics to replicate using regular expressions in the allow and deny lists.
   + Metadata replication settings (topic configurations, ACLs, consumer group offsets).
**Note**  
MSK Replicator does not replicate write ACLs since your producers should not be writing directly to the replicated topic in the target cluster. Your producers should write to the local topic in the target cluster after failover.
   + Consumer groups to replicate using regular expressions in the allow and deny lists. If both allow and deny lists are empty, consumer group replication is turned off.
   + Log delivery configurations (`logDelivery`) to forward operational logs to Amazon CloudWatch Logs, Amazon S3, or Amazon Data Firehose. See [MSK Replicator logs](msk-replicator-logs.md).
**Note**  
Log delivery configurations cannot be updated at the same time as consumer groups or topics configuration. These settings must be updated independently in separate update actions.

1. Save your changes. It takes approximately 30 minutes for the changes to take effect.