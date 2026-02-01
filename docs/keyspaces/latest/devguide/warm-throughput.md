# Configure pre-warming for tables in Amazon Keyspaces

Amazon Keyspaces automatically scales storage partitions based on on-demand or provisioned throughput, but for new tables or
sudden throughput peaks, it can take longer to allocate the required storage partitions. To insure that a new or existing table
has enough capacity to support anticipated peak throughput, you can
manually set specific _warm throughput_ values to _pre-warm_ your table.

_Warm throughput_ refers to the number of read and write operations
your Amazon Keyspaces table can instantaneously support. These values are available by default for
all new and existing tables. If you are using on-demand mode, or if you update your
provisioned throughput, Amazon Keyspaces ensures that your application is able to issue requests
up to those values instantly.

Amazon Keyspaces automatically adjusts warm throughput values as your usage increases.
To adjust throughput capacity for upcoming peak events, for example when you're migrating data
from another database, which may require loading terabytes of data in a short period of time, you can manually
increase your tables warm throughput values. This is useful for planned peak events
where request rates might increase by 10x, 100x, or more. First, assess whether the current warm throughput is sufficient
to handle the expected traffic. Then, if you need to pre-warm the table for the planned peak workload, you can increase
the warm throughput value manually without changing your
throughput settings or [capacity mode](ReadWriteCapacityMode.md "ReadWriteCapacityMode.md").

You can pre-warm tables for read operations, write operations, or
both. You can increase this value for new and existing single-Region tables and multi-Region tables and the warm throughput
settings you set apply automatically to all replicas of the multi-Region tables.
There is no limit to the number of Amazon Keyspaces tables you can pre-warm at any time. The time
to complete pre-warming depends on the values you set and the size of the table.
You can submit simultaneous pre-warm requests and these requests don't
interfere with any table operations. You can pre-warm your table up to the table quota limit for your account in that Region. Use the [Service Quotas console](https://console.aws.amazon.com/servicequotas "https://console.aws.amazon.com/servicequotas") to
check your current quotas and increase them if needed.

The warm throughput values that Amazon Keyspaces adjusts based on your on-demand usage or provisioned capacity are available by
default for all tables without additional charges.
However, if you manually increase the default warm throughput values to
pre-warm tables for peak traffic events, additional charges apply. For more information, see
[Amazon Keyspaces
pricing](https://aws.amazon.com/keyspaces/pricing/ "https://aws.amazon.com/keyspaces/pricing/").

Here are some different scenarios and best practices you might consider when pre-warming Amazon Keyspaces tables.

## Warm throughput and uneven

access patterns

A table might have a warm throughput of 30,000 read units per second and
10,000 write units per second, but you could still experience capacity exceeded events on
reads or writes before hitting those values. This is likely due to a hot
partition. While Amazon Keyspaces can keep scaling to support virtually unlimited
throughput, each individual partition is limited to 1,000 write units per second
and 3,000 read units per second. If your application drives too much traffic to
a small portion of the table’s partitions, capacity exceeded events can occur even before you
reach the table's warm throughput values. We recommend following [Amazon Keyspaces best practices](bp-partition-key-design.md "bp-partition-key-design.md") to ensure
seamless scalability and avoid hot partitions.

## Warm throughput for a

provisioned table

Consider a provisioned table that has a warm throughput of 30,000 read units
per second and 10,000 write units per second but currently has a provisioned
throughput of 4,000 RCUs and 8,000 WCUs. You can instantly scale the table's
provisioned throughput up to 30,000 RCUs or 10,000 WCUs by updating your
provisioned throughput settings. As you increase the provisioned throughput
beyond these values, the warm throughput adjusts automatically to the new
higher values, because you have established a new peak throughput. For example,
if you set the provisioned throughput to 50,000 RCU, the warm throughput
increases to 50,000 read units per second.

```
"ProvisionedThroughput":
    {
        "ReadCapacityUnits": 4000,
        "WriteCapacityUnits": 8000
    }
"WarmThroughput":
    {
        "ReadUnitsPerSecond": 30000,
        "WriteUnitsPerSecond": 10000
    }

```

## Warm throughput for an

on-demand table

A new on-demand table starts with a warm throughput of 12,000 read units per
second and 4,000 write units per second. Your table can instantly accommodate
sustained traffic up to these levels. When your requests exceed 12,000 read
units per second or 4,000 write units per second, the warm throughput adjusts
automatically to the higher values.

```
"WarmThroughput":
    {
        "ReadUnitsPerSecond": 12000,
        "WriteUnitsPerSecond": 4000
    }
```

## Best practices for pre-warming Amazon Keyspaces tables

Follow these best practices when implementing pre-warming for your Amazon Keyspaces tables:

Accurately estimate the required capacity

Because pre-warming incurs a one-time cost, carefully calculate the throughput needed based on expected workload to avoid
over-provisioning.

Consider the table's schema

Tables with larger rows may require more partitions for the same throughput. Factor in your average row size when estimating
pre-warming requirements.

Monitor table performance

After pre-warming, use CloudWatch metrics to verify that your table is handling the load as expected.
For more information, see [Monitor the performance of a pre-warmed table using Amazon CloudWatch](monitor-prewarming-cloudwatch.md "monitor-prewarming-cloudwatch.md").

Manage quotas

If your application requires higher throughput than the default quotas allow (40,000 RCUs/WCUs or 2,000 partitions),
request quota increases well in advance of your high-traffic event. To request a quota increase,
use the [Service Quotas console](https://console.aws.amazon.com/servicequotas "https://console.aws.amazon.com/servicequotas").

Optimize costs

For temporary high-traffic events, consider using pre-warming instead of switching to provisioned mode with high
capacity, as it may be more cost-effective for short duration events. For more information about pricing,
see [Amazon Keyspaces pricing](https://aws.amazon.com/keyspaces/pricing/ "https://aws.amazon.com/keyspaces/pricing/").

###### Note

Monitor your application's performance metrics during the test phase to validate that your pre-warming configuration
adequately supports your workload requirements.

###### Topics

- [Create a new Amazon Keyspaces table with higher
  warm throughput](create-table-warm-throughput.md "create-table-warm-throughput.md")
- [Increase your existing Amazon Keyspaces table's warm
  throughput](update-warm-throughput.md "update-warm-throughput.md")
- [View warm throughput of an Amazon Keyspaces table](view-warm-throughput.md "view-warm-throughput.md")
- [Monitor the performance of a pre-warmed table using Amazon CloudWatch](monitor-prewarming-cloudwatch.md "monitor-prewarming-cloudwatch.md")
