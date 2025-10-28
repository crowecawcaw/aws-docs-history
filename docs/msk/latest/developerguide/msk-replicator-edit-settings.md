# Edit MSK Replicator settings

You can’t change the source cluster, target cluster, Replicator starting
position, or topic name replication configuration once the MSK Replicator has been created. You need to create a new replicator to use Identical topic name replication configuration. However, you can edit other Replicator settings, such as topics and consumer groups to replicate.

1. Sign in to the AWS Management Console, and open the Amazon MSK console at [https://console.aws.amazon.com/msk/home?region=us-east-1#/home/](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/ "https://console.aws.amazon.com/msk/home?region=us-east-1#/home/").
2. In the left navigation pane, choose **Replicators** to display the list of Replicators in the account and select the MSK Replicator you want to edit.
3. Choose the **Properties** tab.
4. In the **Replicator settings** section, choose **Edit replicator**.
5. You can edit the MSK Replicator settings by changing any of these settings.
   - Specify the topics you want to replicate using regular expressions in the allow and deny
     lists. By default, MSK Replicator copies all metadata including topic
     configurations, Access Control Lists (ACLs) and consumer group offsets
     for seamless failover. If you are not creating the Replicator for
     failover, you can optionally choose to turn off one or more of these
     settings available in the **Additional settings**
     section.

   ###### Note

   MSK Replicator does not replicate write ACLs since your producers should not be writing directly to the replicated topic in the target cluster. Your producers should write to the local topic in the target cluster after failover. See [Perform a planned failover to the
   secondary AWS Region](msk-replicator-perform-planned-failover.md "msk-replicator-perform-planned-failover.md") for details.
   - For **Consumer group replication**, you can specify the consumer groups you want to replicate using regular expressions in the allow and deny lists. By default, all consumer groups are replicated. If allow and deny lists are empty, consumer group replication is turned off.
   - Under **Target compression type**, you can choose whether to compress the data written to the target cluster. If you’re going to use compression, we recommend that you use the same compression method as the data in your source cluster.

6. Save your changes.

It takes approximately 30 minutes for the MSK Replicator to be
successfully created and transitioned to running state. If your MSK Replicator
has transitioned to a FAILED status, refer to the troubleshooting section [Troubleshoot MSK Replicator](msk-replicator-troubleshooting.md "msk-replicator-troubleshooting.md").
