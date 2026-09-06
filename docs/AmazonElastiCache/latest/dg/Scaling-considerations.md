

# Considerations
<a name="Scaling-considerations"></a>

## Potential impact on CPU utilization when scaling
<a name="Scaling-considerations-cpu"></a>

When scaling up or down between node types, be aware of the potential impact on CPU utilization related to enhanced I/O features. For [supported node types](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html#CacheNodes.CurrentGen), ElastiCache offloads network I/O and TLS operations to dedicated threads by default, which utilize the extra CPU cores available on the node. The availability of these features depends on your engine version and node types:
+ **Enhanced I/O (Redis 5.0.6\+):** Network I/O is handled on dedicated threads, leveraging additional CPU cores on supported node types.
+ **TLS offloading (Redis 6.2.5\+):** TLS operations are offloaded to the I/O threads, further utilizing available CPU cores.
+ **Enhanced I/O Multiplexing (Redis OSS 7.0.4\+ or Valkey 7.2.6\+):** Multiple client connections are multiplexed onto I/O threads, increasing throughput and optimizing CPU usage across available cores.

These features distribute processing across the extra CPU cores available on the node, which affects CPU metrics in the following ways:

**Impact on CPUUtilization metric**  
`CPUUtilization` reflects the aggregate CPU usage across all cores on the node, including the dedicated I/O threads. Because enhanced I/O features consume CPU on these additional cores, `CPUUtilization` is not a reliable indicator of your engine's actual capacity and loads.

**Impact on EngineCPUUtilization metric**  
`EngineCPUUtilization` measures only the main Redis or Valkey engine thread. When enhanced I/O features are active, operations such as network I/O and TLS processing are offloaded from the main thread to dedicated I/O threads. This means `EngineCPUUtilization` may decrease because the main thread is doing less work. `EngineCPUUtilization` accurately reflects your actual workload capacity and whether your instance is approaching its processing limits.

**Scaling scenarios**
+ **Scaling from a non-supported to a supported node type:** When enhanced I/O features become active on the new node type, `CPUUtilization` may increase as dedicated I/O threads begin utilizing additional CPU cores. At the same time, `EngineCPUUtilization` may decrease as operations are offloaded from the main engine thread.
+ **Scaling up within supported node types:** Additional CPU cores become available, which may reduce `CPUUtilization` as I/O operations are distributed across more resources.
+ **Scaling down within supported node types:** Fewer CPU cores are available to handle I/O operations, which may increase `CPUUtilization` as network I/O, TLS processing, and connection handling compete for limited resources.

**Recommended monitoring approach**

We recommend using `EngineCPUUtilization` rather than `CPUUtilization` for monitoring. `EngineCPUUtilization` measures the main engine thread's performance and accurately reflects whether your instance is approaching its processing limits. `CPUUtilization` may vary across engine versions and node types due to changes in how enhanced I/O features utilize available cores, making it an unreliable metric for capacity planning.