# Amazon ECS Managed Instances auto scaling and task placement

Amazon ECS Managed Instances use intelligent algorithms to automatically scale your cluster capacity
and place tasks efficiently across your infrastructure. Understanding how these algorithms
work helps you optimize your service configurations and troubleshoot placement
behaviors.

## Task placement algorithm

Amazon ECS Managed Instances use a sophisticated placement algorithm that balances availability,
resource utilization, and network requirements when scheduling tasks.

### Availability Zone spread

By default, Amazon ECS Managed Instances prioritize availability by spreading tasks across
multiple Availability Zones:

- For services with multiple tasks, Amazon ECS Managed Instances ensure distribution
  across at least 3 instances in different Availability Zones when
  possible
- This behavior provides fault tolerance but may result in lower resource
  utilization per instance
- Availability Zone spread takes precedence over bin packing
  optimization

### Bin packing behavior

While Amazon ECS Managed Instances can perform bin packing to maximize resource utilization,
this behavior is influenced by your network configuration:

- To achieve bin packing, configure your service to use a single
  subnet
- Multi-subnet configurations prioritize Availability Zone distribution over
  resource density
- Bin packing is more likely during initial service launch than during
  scaling events

### ENI density considerations

For services using the `awsvpc` network mode, Amazon ECS Managed Instances
consider Elastic Network Interface (ENI) density when making placement
decisions:

- Each task in `awsvpc` mode requires a dedicated ENI
- Instance types have different ENI limits that affect task density
- Amazon ECS Managed Instances account for ENI availability when selecting target
  instances

###### Note

Improvements to ENI density calculations are continuously being made to
optimize placement decisions.

## Capacity provider decision logic

Amazon ECS Managed Instances capacity providers make scaling and placement decisions based on
multiple factors:

Resource requirements

CPU, memory, and network requirements of pending tasks

Instance availability

Current capacity and utilization across existing instances

Network constraints

Subnet configuration and ENI availability

Availability Zone distribution

Maintaining fault tolerance across multiple Availability Zones

## Configuration options

### Subnet selection strategy

Your subnet configuration significantly impacts task placement behavior:

Multiple subnets (default)

Prioritizes Availability Zone spread for high availability

May result in lower resource utilization per instance

Recommended for production workloads requiring fault tolerance

Single subnet

Enables bin packing for higher resource utilization

Reduces fault tolerance by concentrating tasks in one Availability
Zone

Suitable for development or cost-optimized workloads

### Network mode considerations

The network mode you choose affects placement decisions:

- `awsvpc` mode – Each task requires a dedicated ENI, limiting
  task density per instance
- `host` mode – Tasks use the host's network directly, with
  placement primarily driven by resource availability

### CPU architecture considerations

The `cpuArchitecture` that you specify in your task definition is used
for placing tasks on a specific architecture. If you don't specify a
`cpuArchitecture`, Amazon ECS will try to place tasks on any available CPU
architecture based on the capacity provider configuration. You can specify either
`X86_64` or `ARM64`.

## Troubleshooting task placement

### Common placement patterns

Understanding expected placement patterns helps distinguish normal behavior from
potential issues:

Spread distribution

Tasks distributed across multiple instances with partial
utilization

Normal behavior when using multiple subnets

Indicates prioritization of availability over resource
efficiency

Concentrated placement

Multiple tasks placed on fewer instances with higher
utilization

Expected when using single subnet configuration

May occur during initial service launch

Uneven distribution

Some instances heavily utilized while others remain
underutilized

May indicate ENI limits or resource constraints

Consider reviewing instance types and network configuration

### Optimizing placement behavior

To optimize task placement for your specific requirements:

1. Evaluate your availability requirements versus cost optimization
   needs
2. Choose appropriate subnet configuration based on your priorities
3. Select instance types with adequate ENI capacity for your network
   mode
4. Monitor placement patterns and adjust configuration as needed

## Best practices

- **For production workloads** – Use multiple
  subnets across different Availability Zones to ensure high availability,
  accepting the trade-off in resource utilization
- **For development or testing** – Consider single
  subnet configuration to maximize resource utilization and reduce costs
- **For `awsvpc` mode** – Choose
  instance types with sufficient ENI capacity to avoid placement
  constraints
- **For cost optimization** – Monitor utilization
  patterns and adjust service configuration to balance availability and
  efficiency
- **For troubleshooting** – Review subnet
  configuration and network mode when investigating unexpected placement
  patterns
