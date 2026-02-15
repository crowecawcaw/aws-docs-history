# Compute resource memory management

When the Amazon ECS container agent registers a compute resource into a compute environment, the agent must determine
how much memory the compute resource has available to reserve for your jobs. Because of platform memory overhead and
memory occupied by the system kernel, this number is different than the installed memory amount for Amazon EC2 instances.
For example, an `m4.large` instance has 8 GiB of installed memory. However, this doesn't always translate
to exactly 8192 MiB of memory available for jobs when the compute resource registers.

Suppose that you specify 8192 MiB for the job, and none of your compute resources have 8192 MiB or greater of
memory available to satisfy this requirement. Then, the job can't be placed in your compute environment. If you're
using a managed compute environment, AWS Batch must launch a larger instance type to accommodate the request.

The default AWS Batch compute resource AMI also reserves 32 MiB of memory for the Amazon ECS container agent and other
critical system processes. This memory isn't available for job allocation. For more information, see [Reserve system memory](ecs-reserved-memory.md "ecs-reserved-memory.md").

The Amazon ECS container agent uses the Docker `ReadMemInfo()` function to query the total memory available
to the operating system. Linux provides command line utilities to determine the total memory.

###### Example- Determine Linux total memory

The **free** command returns the total memory that's recognized by the operating system.

```
`$` `free -b`
```

The following is example output for an `m4.large` instance that's running the Amazon ECS-optimized Amazon Linux AMI.

```
             total       used       free     shared    buffers     cached
Mem:    `8373026816`  348180480 8024846336      90112   25534464  205418496
-/+ buffers/cache:  117227520 8255799296
```

This instance has 8373026816 bytes of total memory. This means that there's 7985 MiB available for tasks.

###### Topics

- [Reserve system memory](ecs-reserved-memory.md "ecs-reserved-memory.md")
- [Tutorial: View compute resource memory](viewing-memory.md "viewing-memory.md")
- [Memory and vCPU considerations for AWS Batch on Amazon EKS](memory-cpu-batch-eks.md "memory-cpu-batch-eks.md")
