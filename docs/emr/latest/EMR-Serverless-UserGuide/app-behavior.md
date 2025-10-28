# Understanding application behavior in EMR Serverless

This section describes job submission behavior, capacity configuration for scaling, and worker configuration
settings for EMR Serverless.

## Default application behavior

**Auto-start** — An application by default is configured to
auto-start on job submission. You can turn this feature off.

**Auto-stop** — An application by default is configured to
auto-stop when idle for 15 minutes. When an application changes to the
`STOPPED` state, it releases any configured pre-initialized capacity. You can
modify the amount of idle time before an application auto-stops, or you can turn this
feature off.

## Maximum capacity

You can configure the maximum capacity that an application can scale up to. You can
specify your maximum capacity in terms of CPU, memory (GB), and disk (GB).

###### Note

It is best practice to configure your maximum capacity to be proportional to your supported
worker sizes by multiplying the number of workers by their sizes. For example, if you want
to limit your application to 50 workers with 2 vCPUs, 16 GB for memory, and
20 GB for disk, set your maximum capacity to 100 vCPUs, 800 GB for memory,
and 1000 GB for disk.

## Supported worker configurations

The following table lists supported worker configurations and sizes that can be specified
for EMR Serverless. Configure different sizes for drivers and executors based on
the need of your workload.

| Worker configurations and sizes | CPU                                               | Memory         | Default ephemeral storage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------- | ------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 vCPU                          | Minimum 2 GB, maximum 8 GB, in 1 GB increments    | 20 GB - 200 GB |
| 2 vCPU                          | Minimum 4 GB, maximum 16 GB, in 1 GB increments   | 20 GB - 200 GB |
| 4 vCPU                          | Minimum 8 GB, maximum 30 GB, in 1 GB increments   | 20 GB - 200 GB |
| 8 vCPU                          | Minimum 16 GB, maximum 60 GB, in 4 GB increments  | 20 GB - 200 GB |
| 16 vCPU                         | Minimum 32 GB, maximum 120 GB, in 8 GB increments | 20 GB - 200 GB | **CPU** — Each worker can have 1, 2, 4, 8, or 16 vCPUs. **Memory** — Each worker has memory, specified in GB, within the limits listed in the earlier table. Spark jobs have a memory overhead, meaning that the memory they use is more than the specified container sizes. This overhead is specified with the properties `spark.driver.memoryOverhead` and `spark.executor.memoryOverhead`. The overhead has a default value of 10% of container memory, with a minimum of 384 MB. You should consider this overhead when you choose worker sizes. For example, If you choose 4 vCPUs for your worker instance, and a pre-initialized storage capacity of 30 GB, then set a value of approximately 27 GB as executor memory for your Spark job. This maximizes the utilization of your pre-initialized capacity. Usable memory is 27 GB, plus 10% of 27 GB (2.7 GB), for a total of 29.7 GB. **Disk** — You can configure each worker with temporary storage disks with a minimum size of 20 GB and a maximum of 200 GB. You only pay for additional storage beyond 20 GB that you configure per worker. |
