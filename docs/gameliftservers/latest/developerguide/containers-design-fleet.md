# Customize an Amazon GameLift Servers container fleet

The topics in this section describe some of the optional features for Amazon GameLift Servers managed
containers. You can choose to use any or all of these features.

###### Topics

- [Set resource limits](#containers-design-fleet-limits "#containers-design-fleet-limits")
- [Understand container fleet memory allocation](#containers-design-fleet-memory-allocation "#containers-design-fleet-memory-allocation")
- [Configuring NVMe Drive Access](#containers-design-fleet-nvme "#containers-design-fleet-nvme")
- [Designate essential containers](#containers-design-fleet-essential "#containers-design-fleet-essential")
- [Configure network connections](#containers-custom-network "#containers-custom-network")
- [Set up health checks for containers](#containers-design-fleet-health "#containers-design-fleet-health")
- [Set container dependencies](#containers-design-fleet-dependencies "#containers-design-fleet-dependencies")
- [Configure a container fleet](#containers-design-fleet-config "#containers-design-fleet-config")

## Set resource limits

For each container group, you can determine how much memory and computing power the
container group needs to run its software. Amazon GameLift Servers relies on this information to manage
resources across the container group. It also uses this information to calculate how many game
server container groups a fleet image can hold. You can also set limits for individual
containers.

You can set a maximum limit on memory and computing power for a container group. By
default, these resources are shared by all containers in the group. You can further customize
resource management by setting limits for individual containers.

**Set optional limits for individual containers**

Setting container-specific resource limits allows you to exert greater control over how
individual containers can use the group’s resources. If you don’t set container-specific
limits, all containers in the group share the group resources. Sharing offers greater
flexibility to use resources where they're needed. It also increases the potential for
processes to compete with each other and result in container failure.

Set any of the following `ContainerDefinition` properties for any
container.

- `MemoryHardLimitMebibytes` – Set a maximum memory limit for
  the container. If the container exceeds this limit, it results in a restart.
- `Vcpu` limit – Reserve a minimum amount of vCPU resources for
  the container's exclusive use. The container always has the reserved amount
  available to it. It can exceed this minimum at any time, if additional resources are
  available. (1024 CPU units is the equivalent of 1 vCPU.)

**Set total resource limits for a container group**

If you set limits for individual containers, you might need to modify how much memory
and vCPU resources the container group needs. The goal is to allocate enough resources
to optimize game server performance. Amazon GameLift Servers uses these limits to calculate how to pack
game server container groups on a fleet instance. You’ll also use them when choosing an
instance type for a container fleet.

Calculate the total memory and vCPU needed for a container group. Consider the
following:

- What are all the processes that run across all containers in the container group?
  Add up the resources required for these processes. Take note of any
  container-specific limits.
- How many concurrent game server processes do you plan to run in each container
  group? You determine this in your game server container image.

Based on your estimate of container group requirements, set the following
`ContainerGroupDefinition` properties:

- `TotalMemoryLimitMebibytes` – Set a maximum memory limit for the
  container group. All containers in the group share allocated memory. If you set
  individual container limits, the total memory limit must be equal to or greater than
  the highest container-specific memory limit.
- `TotalVcpuLimit` – Set a maximum vCPU limit for the container
  group. All containers in the group share allocated CPU resources. If you set
  individual container limits, the total CPU limit must be equal to or greater than
  the sum of all container-specific CPU limits. As a best practice, consider setting
  this value to double the sum of the container CPU limits.

**Example scenario**

Let’s say we’re defining a game server container group with the following three
containers:

- Container A is our game server container. We estimate the resource requirements
  for one game server at 512 MiB and 1024 CPU. We plan to have the container run 1
  server process. Because this container runs our most critical software, we set no
  memory limit or vCPU reserve limit.
- Container B is a support container with resource requirements estimated at
  1024 MiB and 1536 CPU. We set a memory limit of 2048 MiB, and a CPU reserve limit of
  1024 CPU.
- Container C is another support container. We set a hard memory limit of 512 MiB
  and a CPU reserve limit of 512 CPU.

Using this information, we set the following total limits for the container
group:

- Total memory limit: 7680 MiB. This value exceeds the highest memory limit (1024
  MiB).
- Total CPU limit: 13312 CPU. This value exceeds the sum of the CPU limit (1024+512
  CPU).

## Understand container fleet memory allocation

When Amazon GameLift Servers deploys container groups on a fleet instance, not all of the instance's memory
is available for your containers. Amazon GameLift Servers reserves a portion of the instance memory for the
operating system, the Amazon ECS agent, and other supporting services. The amount of reserved
memory varies based on the instance type's total memory. Understanding this overhead helps you
configure your container group definitions to fully utilize the available resources.

### Memory overhead formula

Amazon GameLift Servers calculates the memory available for your container groups using the following
steps:

1. **Determine the memory buffer percentage.** Amazon GameLift Servers
   reserves a percentage of the instance's total memory based on the following
   tiers:

| Instance memory (MiB) | Reserved percentage |
| --------------------- | ------------------- |
| Less than 5,000       | 8%                  |
| 5,000 to 9,999        | 6%                  |
| 10,000 to 89,999      | 5%                  |
| 90,000 to 199,999     | 4%                  |
| 200,000 or more       | 3%                  |

2. **Calculate available memory.** Subtract the reserved
   memory from the total instance memory:

`AvailableMemory = InstanceMemory - round(InstanceMemory × BufferPercentage)` 3. **Subtract per-instance container group memory.** If
your fleet uses a per-instance container group, subtract its
`TotalMemoryLimitMebibytes` from the available memory. One per-instance
container group runs on each fleet instance.

`AvailableMemory = AvailableMemory - PerInstanceCGD.TotalMemoryLimitMebibytes` 4. **Account for log router overhead.** If logging is
enabled for the fleet, Amazon GameLift Servers reserves an additional 50 MiB per game server container
group for the log router. 5. **Calculate maximum game server container groups.** The
maximum number of game server container groups that fit on the instance by memory
is:

`MaxGroupsByMemory = floor(AvailableMemory / (GameServerCGD.TotalMemoryLimitMebibytes + LogRouterMemory))`

Where `LogRouterMemory` is 50 MiB if logging is enabled, or 0 if logging
is disabled.

###### Note

Memory is only one factor that determines how many game server container groups fit on
an instance. Amazon GameLift Servers also considers vCPU capacity and available connection ports, and uses
the minimum of all three calculations.

### Example memory calculation

Consider a fleet using a `c5.xlarge` instance (8,192 MiB total memory) with
logging enabled:

1. Instance memory is 8,192 MiB, which falls in the 5,000–9,999 tier (6% buffer)
2. Reserved memory = round(8,192 × 0.06) = 492 MiB
3. Available memory = 8,192 - 492 = 7,700 MiB
4. If using a per-instance container group with `TotalMemoryLimitMebibytes`
   of 512: Available memory = 7,700 - 512 = 7,188 MiB
5. If each game server container group has `TotalMemoryLimitMebibytes` of
   1,024: MaxGroupsByMemory = floor(7,188 / (1,024 + 50)) = floor(7,188 / 1,074) =
   6

### Available memory by instance type

The following table shows the total memory and available memory (after the Amazon GameLift Servers buffer)
for commonly used instance types. Use these values as a starting point when configuring your
container group definitions. The _Available memory_ column
shows the memory available for all container groups on the instance, before subtracting any
per-instance container group or log router overhead.

| Instance type  | Total memory (MiB) | Buffer percentage | Available memory (MiB) |
| -------------- | ------------------ | ----------------- | ---------------------- |
| `c5.large`     | 4,096              | 8%                | 3,768                  |
| `c5.xlarge`    | 8,192              | 6%                | 7,700                  |
| `c5.2xlarge`   | 16,384             | 5%                | 15,565                 |
| `c5.4xlarge`   | 32,768             | 5%                | 31,130                 |
| `c5.9xlarge`   | 73,728             | 5%                | 70,042                 |
| `c5.12xlarge`  | 98,304             | 4%                | 94,372                 |
| `c5.18xlarge`  | 147,456            | 4%                | 141,558                |
| `c5.24xlarge`  | 196,608            | 4%                | 188,744                |
| `m5.large`     | 8,192              | 6%                | 7,700                  |
| `m5.xlarge`    | 16,384             | 5%                | 15,565                 |
| `m5.2xlarge`   | 32,768             | 5%                | 31,130                 |
| `m5.4xlarge`   | 65,536             | 5%                | 62,259                 |
| `m5.8xlarge`   | 131,072            | 4%                | 125,829                |
| `m5.12xlarge`  | 196,608            | 4%                | 188,744                |
| `r5.large`     | 16,384             | 5%                | 15,565                 |
| `r5.xlarge`    | 32,768             | 5%                | 31,130                 |
| `r5.2xlarge`   | 65,536             | 5%                | 62,259                 |
| `r5.4xlarge`   | 131,072            | 4%                | 125,829                |
| `c6i.large`    | 4,096              | 8%                | 3,768                  |
| `c6i.xlarge`   | 8,192              | 6%                | 7,700                  |
| `c6i.2xlarge`  | 16,384             | 5%                | 15,565                 |
| `c6i.4xlarge`  | 32,768             | 5%                | 31,130                 |
| `c6i.8xlarge`  | 65,536             | 5%                | 62,259                 |
| `c7i.large`    | 4,096              | 8%                | 3,768                  |
| `c7i.xlarge`   | 8,192              | 6%                | 7,700                  |
| `c7i.2xlarge`  | 16,384             | 5%                | 15,565                 |
| `c7i.4xlarge`  | 32,768             | 5%                | 31,130                 |
| `c7i.8xlarge`  | 65,536             | 5%                | 62,259                 |
| `m7i.large`    | 8,192              | 6%                | 7,700                  |
| `m7i.xlarge`   | 16,384             | 5%                | 15,565                 |
| `m7i.2xlarge`  | 32,768             | 5%                | 31,130                 |
| `m7i.4xlarge`  | 65,536             | 5%                | 62,259                 |
| `m7i.8xlarge`  | 131,072            | 4%                | 125,829                |
| `m7i.12xlarge` | 196,608            | 4%                | 188,744                |
| `r7i.large`    | 16,384             | 5%                | 15,565                 |
| `r7i.xlarge`   | 32,768             | 5%                | 31,130                 |
| `r7i.2xlarge`  | 65,536             | 5%                | 62,259                 |
| `r7i.4xlarge`  | 131,072            | 4%                | 125,829                |
| `c8a.medium`   | 2,048              | 8%                | 1,884                  |
| `c8a.large`    | 4,096              | 8%                | 3,768                  |
| `c8a.xlarge`   | 8,192              | 6%                | 7,700                  |
| `c8a.2xlarge`  | 16,384             | 5%                | 15,565                 |
| `c8i.large`    | 4,096              | 8%                | 3,768                  |
| `c8i.xlarge`   | 8,192              | 6%                | 7,700                  |
| `c8i.2xlarge`  | 16,384             | 5%                | 15,565                 |
| `m8a.medium`   | 4,096              | 8%                | 3,768                  |
| `m8a.large`    | 8,192              | 6%                | 7,700                  |
| `m8a.xlarge`   | 16,384             | 5%                | 15,565                 |
| `m8a.2xlarge`  | 32,768             | 5%                | 31,130                 |
| `m8i.large`    | 8,192              | 6%                | 7,700                  |
| `m8i.xlarge`   | 16,384             | 5%                | 15,565                 |
| `m8i.2xlarge`  | 32,768             | 5%                | 31,130                 |
| `c9g.medium`   | 2,048              | 8%                | 1,884                  |
| `c9g.large`    | 4,096              | 8%                | 3,768                  |
| `c9g.xlarge`   | 8,192              | 6%                | 7,700                  |
| `c9g.2xlarge`  | 16,384             | 5%                | 15,565                 |
| `m9g.large`    | 8,192              | 6%                | 7,700                  |
| `m9g.xlarge`   | 16,384             | 5%                | 15,565                 |
| `m9g.2xlarge`  | 32,768             | 5%                | 31,130                 |

For instance types not listed here, you can calculate the available memory using the
formula described above. Check the [Amazon EC2 instance types documentation](../../../ec2/latest/instancetypes/ec2-instance-type-specifications.md "../../../ec2/latest/instancetypes/ec2-instance-type-specifications.md") for the total memory of your chosen
instance type.

## Configuring NVMe Drive Access

On d-type instances, the NVMe drive automatically mounts to the `/data` directory during host startup. To enable containers to access the SSD storage, set the following `ContainerGroupDefinition` property `MountPoints`:

- `InstancePath` – Set to `/data` to reference the auto-mounted NVMe drive on the host instance.
- `AccessLevel` – Choose the appropriate access level for your container's needs (e.g., READ\_ONLY or READ\_WRITE).
- `ContainerPath` – (Optional) Specify the path where the instance path will be mounted inside the container. If not specified, it defaults to the instance path.

For more information about mount points, see [ContainerMountPoint](../apireference/API_ContainerMountPoint.md "../apireference/API_ContainerMountPoint.md") in the Amazon GameLift Servers API Reference.

## Designate essential containers

For a per-instance container group, designate each container as essential or
non-essential. Per-instance container groups must have at least one essential support
container. The essential container does the critical work of the container group. The
essential container is always expected to be running. If it fails, the entire container group
restarts.

Set the `ContainerDefinition` property `Essential` to either true or
false for each container.

## Configure network connections

You can customize network access to allow external traffic connect to any container in a
container fleet. For example, you must establish network connections to the container that
runs your game server processes, so that game clients can join and play your game. Game
clients connect to game servers using ports and IP addresses.

In a container fleet, the connection between a client and server is not direct.
Internally, a process in a container listens on a _container
port_. Externally, incoming traffic connects to a fleet instance using a _connection port_. Amazon GameLift Servers maintains the mappings between internal
container ports and external-facing connection ports, so that incoming traffic gets routed to
the correct process on the instance. To retrieve the current port mappings for a specific container group, call the [DescribeContainerGroupPortMappings](../apireference/API_DescribeContainerGroupPortMappings.md "../apireference/API_DescribeContainerGroupPortMappings.md") operation. For more information about viewing
port mappings, see [View container port mappings](containers-remote-access.md#containers-remote-access-port-mappings "containers-remote-access.md#containers-remote-access-port-mappings").

Amazon GameLift Servers provides an extra layer of control for your network connections. Each container
fleet has an _inbound permissions_ setting, which allows you to
control access to each external-facing connection port. For example, you could remove
permissions for all connection ports to shut off all access to the fleet's containers.

You can update a fleet's inbound permissions, connection ports, and container
ports.

###### Warning

If you provide a custom InstanceConnectionPortRange or InstanceInboundPermissions, Amazon GameLift Servers will no longer manage either value for your fleet. You must set both fields to avoid undefined behavior.

**Set container port ranges**

Configure container port ranges as part of each container definition. This is a
required parameter for a container group definition. You need to configure enough ports
to accommodate all concurrently running processes that need external access. Some
containers will not need any ports.

Your game server container, which runs your game servers, needs a port for every
concurrently running game server process. The game server process listens on the
assigned port and reports it to Amazon GameLift Servers.

**Set connection port ranges**

Configure your container fleet with a set of connection ports. Connection ports
provide external access to the fleet instances that are running your containers. Amazon GameLift Servers
assigns connection ports and maps them to container ports as needed.

By default, Amazon GameLift Servers calculates the number of ports required for all container groups
and sets a port range to accommodate them. We highly recommend you use Amazon GameLift Servers calculated
values, which are updated when you deploy updates to a container group definition. If
you do need to customize connection port ranges, use the following guidance.

When you create a container fleet, define a connection port range (see [ContainerFleet:InstanceConnectionPortRange](../apireference/API_ContainerFleet.md "../apireference/API_ContainerFleet.md")). Make sure that the range has
enough ports to map to every container port that's defined across all containers in both
container groups in the fleet. To calculate the minimum connection ports needed, use the
following formula:

`[Total number of container ports defined for containers in the game server
 container group] * [Number of game server container groups per instance] + [Total
 number of container ports defined for containers in the per-instance container
 group]`

As a best practice, double the minimum number of connection ports.

###### Note

The number of connection ports can potentially limit the number of game server
container groups per instance. If a fleet has only enough connection ports for one
game server container group per instance, Amazon GameLift Servers will deploy only one game server
container group, even if the instances have enough compute power for multiple game
server container groups.

**Set inbound permissions**
Inbound permissions control external access to a container fleet by specifying which
connection ports to open for incoming traffic. You can use this setting to turn a
fleet's network access on and off as needed.

By default, Amazon GameLift Servers calculates the number of ports required for all container groups
and sets a port range to accommodate them. We highly recommend you use Amazon GameLift Servers calculated
values, which are updated when you deploy updates to a container group definition. If
you do need to customize connection port ranges, use the following guidance.

When you create a container fleet, define a set of inbound permissions (see [ContainerFleet:InstanceInboundPermissions](../apireference/API_ContainerFleet.md "../apireference/API_ContainerFleet.md")). Inbound permission ports should
match with the fleet's connection port ranges.

###### Note

Since container ports are selected randomly from the InstanceConnectionPortRange, in order to guarantee that session connections can be made, all ports in InstanceConnectionPortRange should be covered by ports in InstanceInboundPermissions

**Example scenario**
This example illustrates how to set all three network connection properties.

- Our fleet's game server container group has 1 container, which runs 1 game
  server process.

In the game server container group definition, we set the
`PortConfiguration` parameter for this container as follows:

```
"PortConfiguration": {
  "ContainerPortRanges": [ { "FromPort": 10, "ToPort": 20, "Protocol": "TCP"} ]  }
```

- Our fleet also has a per-instance container group with 1 container. It has 1
  process that needs network access. In the per-instance container definition, we set
  the `PortConfiguration` parameter for this container as follows:

```
"PortConfiguration": {
  "ContainerPortRanges": [ { "FromPort": 25, "ToPort": 25, "Protocol": "TCP"} ]  }
```

- Our fleet is configured with 20 game server container groups per fleet instance.
  Given this information, we can use the formula to calculate the number of connection
  ports we need:

  - Minimum: **21 ports** [1 game server container
    ports \* 20 game server container groups per instance + 1 per-instance container
    port]
  - Best practice: **42 ports** [minimum ports \*
    2]
    When creating the container fleet, we set the `InstanceConnectionPortRange`
    parameter as follows:

```
"InstanceConnectionPortRange": { "FromPort": 1010, "ToPort": 1071 }
```

- We want to allow access to all available connection ports. When creating the
  container fleet, we set the `InstanceInboundPermissions` parameter as
  follows:

```
"InstanceInboundPermissions": [
  {"FromPort": 1010, "ToPort": 1071, "IpRange": "10.24.34.0/23", "Protocol": "TCP"} ]
```

## Set up health checks for containers

A container automatically restarts if it experiences a terminal failure and stops running.
If a container is considered essential, it prompts the entire container group to restart.

All game server containers are automatically considered essential. Support containers can
be designated essential, but they need to have a mechanism to report health. You can set
health checks for non-essential support containers as well.

You can define additional custom criteria to measure container health and use a health
check to test that criteria. To set up a container health check, you can define it in a Docker
container image or in your container definition. If you set a health check in the container
definition, it overrides any settings in the container image.

Set the following `SupportContainerDefinition` properties for a container
health check:

- `Command` — Provide a command that checks some aspect of the container’s
  health. You decide what criteria to use to measure health. The command must result in an
  exit value of 1 (unhealthy) or 0 (healthy).
- `StartPeriod` — Specify an initial delay before health check failures start
  counting. This delay gives the container time to bootstrap its processes.
- `Interval` — Decide how often to run the health check command. How quickly
  do you want to detect and resolve a container failure?
- `Timeout` — Decide how long to wait for success or failure before retrying
  the health check command. How long should the health check command take to
  complete?
- `Retries` — How many times should the health check command be retried
  before registering a failure?

## Set container dependencies

Within each container group you can set dependencies between containers based on container
status. A dependency impacts when the dependent container can start or shut down based the
status of another container.

A key use case for dependencies is to create startup and shutdown sequences for the
container group.

For example, you might want Container A to start first and complete successfully before
Containers B and C start. To achieve this, first create a dependency for Container B on
Container A, with the condition that Container A must complete successfully. Then create a
dependency for Container C on Container A with the same condition. Startup sequences occur in
reverse order for shutdown.

## Configure a container fleet

When you create a container fleet, consider the following decision points. Most of these
points are dependent on your container architecture and configuration.

**Decide where you want to deploy your fleet**

In general, you want to deploy your fleets geographically near your players to minimize
latency. You can deploy your container fleet to any AWS Region that Amazon GameLift Servers
supports. If you want to deploy the same game server to additional geographic locations,
you can add remote locations to the fleet including AWS Regions and Local Zones. For a
multi-location fleet, you can adjust capacity independently in each fleet location. For
more information about supported fleet locations, see [Amazon GameLift Servers service locations](gamelift-regions.md "gamelift-regions.md").

Consider using [UDP ping beacons](reference-udp-ping-beacons.md "reference-udp-ping-beacons.md") to collect network latency data
in various geographical locations to anticipate the latency between player devices and
potential fleet locations. These special endpoints accept UDP messages instead of
traditional ICMP pings, providing accurate latency measurements to help you select
optimal fleet locations.

**Choose an instance type and size for your fleet**

Amazon GameLift Servers supports a wide range of Amazon EC2 instances types, all of which are available for use
with a container fleet. Instance type availability and price varies by location. You can view
a list of supported instance types, filtered by location, in the Amazon GameLift Servers console (under
**Resources, Instance and service quotas**).

When choosing an instance type, first consider the instance family. Instance
families offer various combinations of CPU, memory, storage, and networking
capabilities. Get more information on [EC2 instance families](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/"). Within each family you have a range of instance sizes
to choose from. Consider the following issues when selecting an instance size:

- What's the minimum instance size that can support your workload? Use this
  information to eliminate any instance types that are too small.
- What instance type sizes are a good fit for your container architecture?
  Ideally, you want to choose a size that can accommodate multiple copies of your game
  server container group with minimal wasted space.
- What scaling granularity makes sense for your game? Scale fleet capacity
  involves adding or removing instances, and each instance represents the ability to
  host a specific number of game sessions. Consider how much capacity you want to add
  or remove with each instance. If player demand varies by thousands from minute to
  minute, then it might make sense to use very large instances that can host hundreds
  or thousands of game sessions. By contrast, you might prefer more fine-grained
  scaling control with smaller instance types.
- Are there cost savings available based on size? You might find that the cost of
  certain instance types vary by location due to availability.

**Set other optional fleet settings**
You can use the following optional features when configuring a container fleet:

- Set up your game servers to access other AWS resources. See [Connect your Amazon GameLift Servers hosted game server to other AWS resources](gamelift-sdk-server-resources.md "gamelift-sdk-server-resources.md").
- Protect game sessions with active players from terminating prematurely during a
  scale-down event.
- Limit the number of game sessions that one individual can create on the fleet
  within a limited span of time.
