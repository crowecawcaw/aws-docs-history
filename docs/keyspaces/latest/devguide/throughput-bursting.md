# Use burst

capacity effectively in Amazon Keyspaces

Amazon Keyspaces provides some flexibility in your per-partition throughput provisioning by providing
_burst capacity_. Whenever you're not fully using a partition's
throughput, Amazon Keyspaces reserves a portion of that unused capacity for later
_bursts_ of throughput to handle usage spikes.

Amazon Keyspaces currently retains up to 5 minutes (300 seconds) of unused read and write
capacity. During an occasional burst of read or write activity, these extra capacity units can
be consumed quickly—even faster than the per-second provisioned throughput capacity that
you've defined for your table.

Amazon Keyspaces can also consume burst capacity
for background maintenance and other tasks without prior notice.

Note that these burst capacity details might change in the future.
