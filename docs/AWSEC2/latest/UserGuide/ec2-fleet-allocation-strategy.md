# Use allocation strategies to determine

how EC2 Fleet or Spot Fleet fulfills Spot and On-Demand capacity

When you use multiple capacity pools (each comprising an instance type and Availability
Zone) in an EC2 Fleet or Spot Fleet, you can use an _allocation
strategy_ to manage how Amazon EC2 fulfills your Spot and On-Demand capacities
from these pools. The allocation strategies can optimize for available capacity, price,
and the instance types to use. There are different allocation strategies for Spot Instances and
On-Demand Instances.

###### Topics

- [Allocation
  strategies for Spot Instances](#ec2-fleet-allocation-strategies-for-spot-instances "#ec2-fleet-allocation-strategies-for-spot-instances")
- [Allocation
  strategies for On-Demand Instances](#ec2-fleet-allocation-strategies-for-on-demand-instances "#ec2-fleet-allocation-strategies-for-on-demand-instances")
- [Choose the appropriate Spot
  allocation strategy](#ec2-fleet-allocation-use-cases "#ec2-fleet-allocation-use-cases")
- [Maintain target capacity for
  Spot Instances](#ec2-fleet-maintain-fleet-capacity "#ec2-fleet-maintain-fleet-capacity")
- [Prioritize instance types for
  On-Demand capacity](#ec2-fleet-on-demand-priority "#ec2-fleet-on-demand-priority")

## Allocation

strategies for Spot Instances

Your launch configuration determines all the possible Spot capacity pools
(instance types and Availability Zones) from which EC2 Fleet or Spot Fleet can launch Spot Instances.
However, when launching instances, the fleet uses the allocation strategy that you
specify to pick the specific pools from all your possible pools.

###### Note

(Linux instances only) If you configure your Spot Instance to launch with [AMD SEV-SNP](sev-snp.md "sev-snp.md") turned on, you are charged an
additional hourly usage fee that is equivalent to 10% of the [On-Demand hourly rate](https://aws.amazon.com/ec2/pricing/on-demand/ "https://aws.amazon.com/ec2/pricing/on-demand/")
for the selected instance type. If the allocation strategy uses price as an
input, the fleet does not include this additional fee; only the Spot price is
used.

You can specify one of the following allocation strategies for Spot Instances:

**Price capacity optimized** (recommended)

The fleet identifies the pools with the highest capacity availability
for the number of instances that are launching. This means that we will
request Spot Instances from the pools that we believe have the lowest chance of
interruption in the near term. The fleet then requests Spot Instances from the
lowest priced of these pools.

The **price capacity optimized** allocation strategy
is the best choice for most Spot workloads, such as stateless
containerized applications, microservices, web applications, data and
analytics jobs, and batch processing.

If you're using the AWS CLI, the parameter name is
`price-capacity-optimized` for EC2 Fleet and
`priceCapacityOptimized` for Spot Fleet.

**Capacity optimized**

The fleet identifies the pools with the highest capacity availability
for the number of instances that are launching. This means that we will
request Spot Instances from the pools that we believe have the lowest chance of
interruption in the near term. You can optionally set a priority for
each instance type in your fleet, where the fleet optimizes for capacity
first, but honors instance type priorities on a best-effort
basis.

With Spot Instances, pricing changes slowly over time based on long-term trends
in supply and demand, but capacity fluctuates in real time. The
**capacity optimized** strategy automatically
launches Spot Instances into the most available pools by looking at real-time
capacity data and predicting which are the most available. This works
well for workloads that may have a higher cost of interruption
associated with restarting work, such as long Continuous Integration
(CI), image and media rendering, Deep Learning, and High Performance
Compute (HPC) workloads that may have a higher cost of interruption
associated with restarting work. By offering the possibility of fewer
interruptions, the **capacity optimized** strategy can
lower the overall cost of your workload.

Alternatively, you can use the **capacity optimized
prioritized** allocation strategy with a priority parameter
to order instance types from highest to lowest priority. You can set the
same priority for different instance types. The fleet will optimize for
capacity first, but will honor instance type priorities on a best-effort
basis (for example, if honoring the priorities will not significantly
affect the fleet's ability to provision optimal capacity). This is a
good option for workloads where the possibility of disruption must be
minimized and the preference for certain instance types matters. Note
that when you set the priority for instance types for your Spot
capacity, the same priority is also applied to your On-Demand Instances
if the On-Demand allocation strategy is set to
**prioritized**. For Spot Fleet, using priorities is
supported only if your fleet uses a launch template.

If you're using the AWS CLI, the parameter names are
`capacity-optimized` and
`capacity-optimized-prioritized` for EC2 Fleet and
`capacityOptimized` and
`capacityOptimizedPrioritized` for Spot Fleet.

**Diversified**

The Spot Instances are distributed across all Spot capacity pools. If you're
using the AWS CLI, the parameter name is `diversified` for both
EC2 Fleet and Spot Fleet.

**Lowest price** (not recommended)

###### Warning

We don't recommend the **lowest price**
allocation strategy because it has the highest risk of interruption
for your Spot Instances.

The Spot Instances come from the lowest priced pool that has available
capacity. When using the AWS CLI, this is the default strategy. However,
we recommend that you override the default by specifying the
**price capacity optimized** allocation
strategy.

With the lowest price strategy, if the lowest priced pool doesn't have
available capacity, the Spot Instances come from the next lowest priced pool that
has available capacity. If a pool runs out of capacity before fulfilling
your desired capacity, the fleet will continue to fulfill your request
by drawing from the next lowest priced pool. To ensure that your desired
capacity is met, you might receive Spot Instances from several pools.

Because this strategy only considers instance price and not capacity
availability, it might lead to high interruption rates.

The lowest price allocation strategy is only available when using the
AWS CLI. The parameter name is `lowest-price` for EC2 Fleet and
`lowestPrice` for Spot Fleet.

**Number of pools to use**

The number of Spot pools across which to allocate your target Spot
capacity. Valid only when the allocation strategy is set to
**lowest price**. The fleet selects the lowest
priced Spot pools and evenly allocates your target Spot capacity across
the number of Spot pools that you specify.

Note that the fleet attempts to draw Spot Instances from the number of pools
that you specify on a best effort basis. If a pool runs out of Spot
capacity before fulfilling your target capacity, the fleet will continue
to fulfill your request by drawing from the next lowest priced pool. To
ensure that your target capacity is met, you might receive Spot Instances from
more than the number of pools that you specified. Similarly, if most of
the pools have no Spot capacity, you might receive your full target
capacity from fewer than the number of pools that you specified.

This parameter is only available when specifying the **lowest
price** allocation strategy and only when using the AWS CLI.
The parameter name is `InstancePoolsToUseCount` for both EC2 Fleet
and Spot Fleet.

## Allocation

strategies for On-Demand Instances

Your launch configuration determines all the possible capacity pools (instance
types and Availability Zones) from which EC2 Fleet or Spot Fleet can launch On-Demand Instances. However,
when launching instances, the fleet uses the allocation strategy that you specify to
pick the specific pools from all your possible pools.

You can specify one of the following allocation strategies for On-Demand Instances:

**Lowest price**

The On-Demand Instances come from the lowest priced pool that has available
capacity. This is the default strategy.

If the lowest priced pool doesn't have available capacity, the On-Demand Instances
come from the next lowest priced pool that has available
capacity.

If a pool runs out of capacity before fulfilling your desired
capacity, the fleet will continue to fulfill your request by drawing
from the next lowest priced pool. To ensure that your desired capacity
is met, you might receive On-Demand Instances from several pools.

**Prioritized**

The fleet uses the priority that you assigned to each launch template
override, launching instance types in order of the highest priority
first. This strategy can't be used with attribute-based instance type
selection. For an example of how to use this allocation strategy, see
[Prioritize instance types for
On-Demand capacity](#ec2-fleet-on-demand-priority "#ec2-fleet-on-demand-priority").

## Choose the appropriate Spot

allocation strategy

You can optimize your fleet for your use case by choosing the appropriate Spot
allocation strategy.

### Balance lowest price and capacity availability

To balance the trade-offs between the lowest priced Spot capacity pools and
the Spot capacity pools with the highest capacity availability, we recommend
that you use the **price capacity optimized** allocation
strategy. This strategy makes decisions about which pools to request Spot Instances from
based on both the price of the pools and the capacity availability of Spot Instances in
those pools. This means that we will request Spot Instances from the pools that we
believe have the lowest chance of interruption in the near term, while still
taking price into consideration.

If your fleet runs resilient and stateless workloads, including containerized
applications, microservices, web applications, data and analytics jobs, and
batch processing, then use the **price capacity optimized**
allocation strategy for optimal cost savings and capacity availability.

If your fleet runs workloads that might have a higher cost of interruption
associated with restarting work, then you should implement checkpointing so that
applications can restart from that point if they're interrupted. By using
checkpointing, you make the **price capacity optimized**
allocation strategy a good fit for these workloads because it allocates capacity
from the lowest priced pools that also offer a low Spot Instance interruption
rate.

For example JSON configurations that use the **price capacity
optimized** allocation strategy, see the following:

- EC2 Fleet – [Example 10: Launch Spot Instances in a
  price-capacity-optimized fleet](ec2-fleet-examples.md#ec2-fleet-config11 "ec2-fleet-examples.md#ec2-fleet-config11")
- Spot Fleet – [Example 11: Launch Spot Instances in a
  priceCapacityOptimized fleet](spot-fleet-examples.md#fleet-config11 "spot-fleet-examples.md#fleet-config11")

### When workloads have a

high cost of interruption

You can optionally use the **capacity optimized** strategy if
you run workloads that either use similarly priced instance types, or where the
cost of interruption is so significant that any cost saving is inadequate in
comparison to a marginal increase in interruptions. This strategy allocates
capacity from the most available Spot capacity pools that offer the possibility
of fewer interruptions, which can lower the overall cost of your
workload.

When the possibility of interruptions must be minimized but the preference for
certain instance types matters, you can express your pool priorities by using
the **capacity optimized prioritized** allocation strategy and
then setting the order of instance types to use from highest to lowest
priority.

Note that when you set priorities for **capacity optimized
prioritized**, the same priorities are also applied to your On-Demand Instances
if the On-Demand allocation strategy is set to **prioritized**.
Also note that, for Spot Fleet, using priorities is supported only if your fleet uses
a launch template.

For example JSON configurations that use the **capacity
optimized** allocation strategy, see the following:

- EC2 Fleet – [Example 8: Launch Spot Instances in a
  capacity-optimized fleet](ec2-fleet-examples.md#ec2-fleet-config9 "ec2-fleet-examples.md#ec2-fleet-config9")
- Spot Fleet – [Example 9: Launch Spot Instances in a
  capacity-optimized fleet](spot-fleet-examples.md#fleet-config9 "spot-fleet-examples.md#fleet-config9")

For example JSON configurations that use the **capacity optimized
prioritized** allocation strategy, see the following:

- EC2 Fleet – [Example 9: Launch Spot Instances in a
  capacity-optimized fleet with priorities](ec2-fleet-examples.md#ec2-fleet-config10 "ec2-fleet-examples.md#ec2-fleet-config10")
- Spot Fleet – [Example 10: Launch Spot Instances in a
  capacity-optimized fleet with priorities](spot-fleet-examples.md#fleet-config10 "spot-fleet-examples.md#fleet-config10")

### When your workload

is time flexible and capacity availability is not a factor

If your fleet is small or runs for a short time, you can use **price
capacity optimized** to maximize cost savings while still
considering capacity availability.

### When your fleet is

large or runs for a long time

If your fleet is large or runs for a long time, you can improve the
availability of your fleet by distributing the Spot Instances across multiple pools using
the **diversified** strategy. For example, if your fleet
specifies 10 pools and a target capacity of 100 instances, the fleet launches 10
Spot Instances in each pool. If the Spot price for one pool exceeds your maximum price
for this pool, only 10% of your fleet is affected. Using this strategy also
makes your fleet less sensitive to increases in the Spot price in any one pool
over time. With the **diversified** strategy, the fleet does
not launch Spot Instances into any pools with a Spot price that is equal to or higher
than the [On-Demand
price](https://aws.amazon.com/ec2/pricing/ "https://aws.amazon.com/ec2/pricing/").

## Maintain target capacity for

Spot Instances

After Spot Instances are terminated due to a change in the Spot price or available capacity
of a Spot capacity pool, a fleet of type `maintain` launches replacement
Spot Instances. The allocation strategy determines the pools from which the replacement
instances are launched, as follows:

- If the allocation strategy is **price capacity
  optimized**, the fleet launches replacement instances in the
  pools that have the most Spot Instance capacity availability while also taking price
  into consideration and identifying lowest priced pools with high capacity
  availability.
- If the allocation strategy is **capacity optimized**, the
  fleet launches replacement instances in the pools that have the most Spot Instance
  capacity availability.
- If the allocation strategy is **diversified**, the fleet
  distributes the replacement Spot Instances across the remaining pools.

## Prioritize instance types for

On-Demand capacity

When an EC2 Fleet or Spot Fleet attempts to fulfill your On-Demand capacity, it defaults to
launching the lowest priced instance type first. If the On-Demand allocation
strategy is set to **prioritized**, the fleet uses priority to
determine which instance type to use first when fulfilling On-Demand capacity. The
priority is assigned to the launch template override, and the highest priority is
launched first.

**Example: Prioritize instance types**

In this example, you configure three launch template overrides, each with a
different instance type.

The On-Demand price for the instance types range in price. The following are the
instance types used in this example, listed in order of price, starting with the
least expensive instance type:

- `m4.large` – least expensive
- `m5.large`
- `m5a.large`

If you do not use priority to determine the order, the fleet fulfills the
On-Demand capacity by starting with the least expensive instance type.

However, say you have unused `m5.large` Reserved Instances that you want to use
first. You can set the launch template override priority so that the instance types
are used in the order of priority, as follows:

- `m5.large` – priority 1
- `m4.large` – priority 2
- `m5a.large` – priority 3
