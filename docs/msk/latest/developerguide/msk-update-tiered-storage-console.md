# Update tiered storage on an existing Amazon MSK cluster using the console

This process describes how to updated a tiered storage Amazon MSK cluster using the AWS Management Console.

Make sure the current Apache Kafka version of your MSK cluster is
2.8.2.tiered. Refer to [updating the Apache Kafka version](version-upgrades.md "version-upgrades.md") if you need to upgrade
your MSK cluster to 2.8.2.tiered version.

###### Note

You can enable tiered storage only if your cluster's log.cleanup.policy is set to `delete`, as compacted topics are not supported on tiered storage. Later, you can configure an individual topic's log.cleanup.policy to `compact` if tiered storage is not enabled on that particular topic. See [Topic-level configuration](msk-configuration-properties.md#msk-topic-confinguration "msk-configuration-properties.md#msk-topic-confinguration") for more details on supported
configuration attributes.

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/](https://console.aws.amazon.com/msk/ "https://console.aws.amazon.com/msk/").
2. Go to the cluster summary page and choose **Properties**.
3. Go to the **Storage** section and choose **Edit cluster storage mode**.
4. Choose **Tiered storage and EBS storage** and **Save
   changes**.
