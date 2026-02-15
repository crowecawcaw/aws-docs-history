# Reserving Amazon ECS Linux container instance memory

When the Amazon ECS container agent registers a container instance to a cluster, the agent must
determine how much memory the container instance has available to reserve for your tasks.
Because of platform memory overhead and memory occupied by the system kernel, this number is
different than the installed memory amount that is advertised for Amazon EC2 instances. For
example, an `m4.large` instance has 8 GiB of installed memory. However, this does
not always translate to exactly 8192 MiB of memory available for tasks when the container
instance registers.

## ECS Managed Instances memory resource determination

Amazon ECS Managed Instances uses a hierarchical approach to determine memory resource
requirements for tasks. Unlike ECS on EC2 which relies on Docker's memory introspection,
ECS Managed Instances calculates memory requirements directly from the task payload during
scheduling decisions.

When the ECS Managed Instances agent receives a task, it calculates the memory requirement
using the following priority order:

1. **Task-level memory (highest priority)** - If
   task-level memory is specified in the task definition, the agent uses this value
   directly. This takes precedence over all container-level memory settings.
2. **Container-level memory sum (fallback)** - If
   task-level memory is not specified (or is 0), the agent sums the memory requirements
   from all containers in the task. For each container, it uses:
   1. _Memory reservation (soft limit)_ - If a container
      specifies `memoryReservation` in its configuration, the agent
      uses this value.
   2. _Container memory (hard limit)_ - If
      `memoryReservation` is not specified, the agent uses the
      container's `memory` field.

###### Example Task-level memory specified

When task-level memory is specified, it takes precedence over container-level settings:

```
{
  "family": "my-task",
  "memory": "2048",
  "containerDefinitions": [
    {
      "name": "container1",
      "memory": 1024,
      "memoryReservation": 512
    }
  ]
}
```

The agent reserves 2048 MiB (task-level memory takes precedence).

###### Example Container-level memory with reservations

When task-level memory is not specified, the agent sums container memory requirements:

```
{
  "family": "my-task",
  "containerDefinitions": [
    {
      "name": "container1",
      "memory": 1024,
      "memoryReservation": 512
    },
    {
      "name": "container2",
      "memory": 512
    }
  ]
}
```

The agent reserves 512 MiB (container1 reservation) + 512 MiB (container2 memory) = 1024 MiB total.

The ECS Managed Instances agent performs memory calculation in three phases:

1. **Task reception** - When a task payload arrives
   from the ECS control plane, the agent immediately calculates the required memory.
2. **Resource storage** - The calculated memory
   requirement is stored in the task model for later use in resource accounting operations.
3. **Scheduling decision** - Before accepting a task,
   the agent checks if sufficient memory is available. If insufficient memory is available,
   the task is rejected and remains in the ECS service queue until resources become available.

###### Note

Unlike ECS on EC2, ECS Managed Instances does not use the `ECS_RESERVED_MEMORY`
configuration variable. Memory reservation for system processes is handled through the
underlying platform's resource management, and the agent performs accurate resource
accounting based on task definitions.

For ECS on EC2, the Amazon ECS container agent provides a configuration variable called
`ECS_RESERVED_MEMORY`, which you can use to remove a specified number of MiB
of memory from the pool that is allocated to your tasks. This effectively reserves that
memory for critical system processes.

If you occupy all of the memory on a container instance with your tasks, then it is
possible that your tasks will contend with critical system processes for memory and possibly
start a system failure.

For example, if you specify `ECS_RESERVED_MEMORY=256` in your container agent
configuration file, then the agent registers the total memory minus 256 MiB for that
instance, and 256 MiB of memory could not be allocated by ECS tasks. For more information
about agent configuration variables and how to set them, see [Amazon ECS container agent configuration](ecs-agent-config.md "ecs-agent-config.md") and [Bootstrapping Amazon ECS Linux container instances to pass data](bootstrap_container_instance.md "bootstrap_container_instance.md").

If you specify 8192 MiB for the task, and none of your container instances have 8192 MiB
or greater of memory available to satisfy this requirement, then the task cannot be placed
in your cluster. If you are using a managed compute environment, then AWS Batch must launch a
larger instance type to accommodate the request.

The Amazon ECS container agent uses the Docker `ReadMemInfo()` function to query the
total memory available to the operating system. Both Linux
and Windows provide command line utilities to determine the total memory.

###### Example- Determine Linux total memory

The **free** command returns the total memory that is recognized by the
operating system.

```
`$` `free -b`
```

Example output for an `m4.large` instance running the
Amazon ECS-optimized Amazon Linux AMI.

```
             total       used       free     shared    buffers     cached
Mem:    `8373026816`  348180480 8024846336      90112   25534464  205418496
-/+ buffers/cache:  117227520 8255799296
```

This instance has 8373026816 bytes of total memory, which translates to 7985 MiB
available for tasks.

###### Example- Determine Windows total memory

The **wmic** command returns the total memory that is recognized by the
operating system.

```
`C:\>` `wmic ComputerSystem get TotalPhysicalMemory`
```

Example output for an `m4.large` instance running the
Amazon ECS-optimized Windows Server AMI.

```
TotalPhysicalMemory
`8589524992`
```

This instance has 8589524992 bytes of total memory, which translates to 8191 MiB
available for tasks.

## Viewing container instance memory

You can view how much memory a container instance registers with in the Amazon ECS console (or
with the [DescribeContainerInstances](../APIReference/API_DescribeContainerInstances.md "../APIReference/API_DescribeContainerInstances.md") API operation). If you are trying to maximize
your resource utilization by providing your tasks as much memory as possible for a
particular instance type, you can observe the memory available for that container instance
and then assign your tasks that much memory.

###### To view container instance memory

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Clusters**, and then choose
   the cluster that hosts your container instance.
3. Choose **Infrastructure**, and then under Container
   instances, choose a container instance.
4. The **Resources** section shows the registered and available
   memory for the container instance.

The **Registered** memory value is what the container instance;
registered with Amazon ECS when it was first launched, and the
**Available** memory value is what has not already been
allocated to tasks.
