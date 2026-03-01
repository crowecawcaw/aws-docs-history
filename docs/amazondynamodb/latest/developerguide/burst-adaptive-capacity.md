# DynamoDB burst and adaptive capacity

To minimize throttling because of throughput exceptions, DynamoDB uses _burst
capacity_ to handle usage spikes. DynamoDB uses _adaptive
capacity_ to help accommodate uneven access patterns.

## Burst capacity

DynamoDB provides some flexibility for your throughput provisioning with
_burst capacity_. Whenever you aren't fully using your
available throughput, DynamoDB reserves a portion of that unused capacity for later
_bursts_ of throughput to handle usage spikes. With burst
capacity, unexpected read or write requests can succeed where they otherwise would
be throttled.

DynamoDB currently retains up to five minutes (300 seconds) of unused read and write
capacity. During an occasional burst of read or write activity, these extra capacity
units can be consumed quickly — even faster than the per-second provisioned
throughput capacity that you've defined for your table.

DynamoDB can also consume burst capacity for background maintenance and other tasks
without prior notice.

Note that these burst capacity details might change in the future.

## Adaptive capacity

DynamoDB automatically distributes your data across [partitions](HowItWorks.md "HowItWorks.md"), which are stored on multiple
servers in the AWS Cloud. It's not always possible to evenly distribute read and
write activity all the time. When data access is imbalanced, a "hot" partition can
receive a higher volume of read and write traffic compared to other partitions.
Because read and write operations on a partition are managed independently,
throttling will occur if a single partition receives more than 3000 read operation
or more than 1000 write operations. Adaptive capacity works by automatically
increasing throughput capacity for partitions that receive more traffic.

To better accommodate uneven access patterns, DynamoDB adaptive capacity enables
your application to continue reading and writing to hot partitions without being
throttled, provided that traffic does not exceed your table’s total provisioned
capacity or the partition maximum capacity. Adaptive capacity works by automatically
and instantly increasing throughput capacity for partitions that receive more
traffic.

The following diagram illustrates how adaptive capacity works. The example table
is provisioned with 400 WCUs evenly shared across four partitions, allowing each
partition to sustain up to 100 WCUs per second. Partitions 1, 2, and 3 each receives
write traffic of 50 WCU/sec. Partition 4 receives 150 WCU/sec. This hot partition
can accept write traffic while it still has unused burst capacity, but eventually it
throttles traffic that exceeds 100 WCU/sec.

DynamoDB adaptive capacity responds by increasing the capacity of partition 4 so that
it can sustain the higher workload of 150 WCU/sec without being throttled.

![Adaptive capacity automatically increases throughput for partition 4 with higher traffic to avoid throttling.](images/adaptive-capacity.png)

Adaptive capacity is enabled automatically for every DynamoDB table, at no additional
cost. You don't need to explicitly enable or disable it.

### Isolate frequently accessed items

If your application drives disproportionately high traffic to one or more
items, adaptive capacity rebalances your partitions such that frequently
accessed items don't reside on the same partition. This isolation of frequently
accessed items reduces the likelihood of request throttling due to your workload
exceeding the throughput quota on a single partition. You can also break up an
item collection into segments by sort key, as long as the item collection isn't
traffic that is tracked by a monotonic increase or decrease of the sort
key.

If your application drives consistently high traffic to a single item,
adaptive capacity might rebalance your data so that a partition contains only
that single, frequently accessed item. In this case, DynamoDB can deliver
throughput up to the partition maximum of 3,000 RCUs and 1,000 WCUs to that
single item’s primary key. Adaptive capacity will not split item collections
across multiple partitions of the table when there is a [local secondary index](LSI.md "LSI.md") on the table.
