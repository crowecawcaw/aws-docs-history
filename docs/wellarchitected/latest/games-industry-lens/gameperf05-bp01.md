# GAMEPERF05-BP01 Benchmark your game performance across multiple

compute types

For game server workloads, there is no singular approach to
identifying the optimal compute solution for hosting your game
server. A common strategy for benchmarking game servers is to
start with compute-optimized EC2 'c' instances, because this
instance family provides high performance for workloads that are
computationally intensive. Alternatively, if your game requires a
significant amount of memory to implement specific features, the
memory-optimized instances may be most suitable.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

If your workload utilizes significant network resources, consider
implementing instances that are network-optimized which is
typically indicated using an 'n' in the instance name, avoid
burstable instance types 't' as after credits are exhausted
performance will decrease. Games are sensitive to latency and
dropped packets, so it is recommended to use EC2 enhanced
networking to help improve the network performance of your game
servers. Enhanced networking uses single root I/O virtualization
([SR-IOV](../../../whitepapers/latest/ec2-networking-for-telecom/overview-of-performance-optimization-options.md "../../../whitepapers/latest/ec2-networking-for-telecom/overview-of-performance-optimization-options.md"))
to provide high-performance networking capabilities on
[supported](../../../AWSEC2/latest/UserGuide/enhanced-networking.md#supported_instances "../../../AWSEC2/latest/UserGuide/enhanced-networking.md#supported_instances")
[instance
types](../../../AWSEC2/latest/UserGuide/enhanced-networking.md#supported_instances "../../../AWSEC2/latest/UserGuide/enhanced-networking.md#supported_instances") . SR-IOV is a method of device virtualization that
provides higher I/O performance and lower CPU utilization when
compared to traditional virtualized network interfaces. Enhanced
networking provides higher bandwidth, higher packet per second
(PPS) performance, and consistently lower inter-instance
latencies. Enhanced networking with Elastic Network Adapter is
available for most recent EC2 instance types and is important to
[regularly
update](https://github.com/amzn/amzn-drivers/tree/master "https://github.com/amzn/amzn-drivers/tree/master") to benefit from performance enhancements from newer
instances and improvements to the
[AWS Nitro hypervisor.](../../../ec2/latest/instancetypes/ec2-nitro-instances.md "../../../ec2/latest/instancetypes/ec2-nitro-instances.md")

If your game performs similarly across multiple EC2 instance
types, then you should consider using multiple instance types to
host your game servers. Monitor performance over time and perform
further optimization after you have hosted enough production game
sessions to be able to identify performance trends. Remember that
your compute requirements may change as you add new features into
your game that require different allocation of resources. You can
[configure
EC2 Auto Scaling groups](../../../autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.md "../../../autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.md") to use multiple instance types, or
you can use separate Auto Scaling groups to host game server
instances that run separate instance types which may make it
simpler to manage correlation and aggregation of metrics. 

Evaluate how your game performs on different types of processors
such as Intel-based instances, AMD-based instances, and ARM-based
Graviton instances. Unreal Engine 5.1.1 or
[newer
can compile game servers for Graviton](https://aws.amazon.com/blogs/gametech/compiling-unreal-engine-5-dedicated-servers-for-aws-graviton-ec2-instances/ "https://aws.amazon.com/blogs/gametech/compiling-unreal-engine-5-dedicated-servers-for-aws-graviton-ec2-instances/") and can improve price
performance for your game. Perform sweep and saturation testing at
various sizes within each family to determine the sweet spot where
utilization and performance are consistent.

You should also benchmark how your game performance is impacted
when it is hosted using containers and Lambda functions. For use
cases where long-lived game server processes are not required,
such as asynchronous games and for game backend services, consider
using a serverless architecture with Lambda which can simplify
management and operations for game operations teams, as well as
allow you to more quickly deploy your game globally to many AWS Regions. For serverless best practices, refer to
the [Serverless
Applications Lens - Well-Architected Framework](../serverless-applications-lens/welcome.md "../serverless-applications-lens/welcome.md").

### Implementation steps

- Benchmark game servers on compute-optimized 'c' instances
  for CPU intensive workloads, memory-optimized instances for
  memory heavy task, and network-optimized 'n' instances for
  high network throughput.
- Use enhanced networking with Elastic Network Adapter (ENA)
  on supported instances to improve network performance,
  reduce latency, and increase packet processing rates.
- Evaluate and test multiple instance types, processors
  (Intel, AMD, Graviton), and container or Lambda hosting
  options, adjusting compute solutions as game features
  evolve.

For more information, see
[Choose
the right compute strategy for your global game servers](https://aws.amazon.com/blogs/gametech/choose-the-right-compute-strategy-for-your-global-game-servers/ "https://aws.amazon.com/blogs/gametech/choose-the-right-compute-strategy-for-your-global-game-servers/").
