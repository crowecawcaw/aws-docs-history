# Data tiering monitoring

MemoryDB offers metrics designed specifically to monitor the performance clusters that use data tiering.
To monitor the ratio of items in DRAM compared to SSD, you can use the `CurrItems` metric at [Metrics for MemoryDB](metrics.md "metrics.md").
You can calculate the percentage as: `(CurrItems with Dimension: Tier = Memory * 100) / (CurrItems with no dimension filter)`.

If the configured eviction policy allows, then MemoryDB will start evicting items
when the percentage of items in memory decreases below 5 percent.
On nodes configured with noeviction policy, write operations will receive an out of memory error.

It is still recommended that you consider [Scaling MemoryDB clusters](scaling-cluster.md "scaling-cluster.md") when the percentage of items in memory decreases below 5 percent.
For more information, see _Metrics for MemoryDB clusters that use data tiering_ at [Metrics for MemoryDB](metrics.md "metrics.md").
