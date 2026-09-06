

# Pricing
<a name="msk-replicator-pricing"></a>

MSK Replicator pricing is based on the amount of data replicated. You pay for the data processed by the Replicator. For cross-region replication, you also pay for cross-region data transfer.

If you use Identical topic name replication for active-active setups, each Replicator will process twice the usual amount of data (once for replication and again to filter data to prevent infinite loops). You can track the total data processed by each replicator using the `ReplicatorBytesInPerSec` metric. See [Metrics reference](msk-replicator-metrics-ref.md).

For current pricing information, see [Amazon MSK Pricing](https://aws.amazon.com/msk/pricing/).

For MSK Replicator service quotas and limits, see [MSK Replicator quotas](limits.md) in the Amazon MSK quota page.