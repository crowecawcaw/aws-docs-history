# Customize an Amazon GameLift Servers container fleet

The topics in this section describe some of the optional features for Amazon GameLift Servers managed
containers. You can choose to use any or all of these features.

###### Topics

- [Set resource limits](#containers-design-fleet-limits "#containers-design-fleet-limits")
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

## Configuring NVMe Drive Access

On d-type instances, the NVMe drive automatically mounts to the `/data` directory during host startup. To enable containers to access the SSD storage, set the following `ContainerGroupDefinition` property `MountPoints`:

- `InstancePath` – Set to `/data` to reference the auto-mounted NVMe drive on the host instance.
- `AccessLevel` – Choose the appropriate access level for your container's needs (e.g., READ_ONLY or READ_WRITE).
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
the correct process on the instance.

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

      + Minimum: **21 ports** [1 game server container
       ports \* 20 game server container groups per instance + 1 per-instance container
       port]
      + Best practice: **42 ports** [minimum ports \*
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
