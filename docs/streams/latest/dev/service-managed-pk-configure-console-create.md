

# Choose a record distribution strategy when you create a stream
<a name="service-managed-pk-configure-console-create"></a>

1. Open the Kinesis Data Streams console at [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis).

1. Choose **Create data stream**.

1. Enter a name for your data stream.

1. Under **Data stream capacity**, choose **On-demand** capacity mode. The **Record distribution strategy** panel appears below the capacity panel. This panel is hidden when **Provisioned** mode is selected.

1. In the **Record distribution strategy** panel, choose one of the following:
   + **Auto** – Kinesis Data Streams distributes records evenly across shards and ignores any partition key that producers supply. Choose this option for stateless workloads that do not require partition-key ordering.
   + **User set** – Producers must supply a partition key, and Kinesis Data Streams uses it to determine shard placement. This is the default.

1. Choose **Create data stream**.