# CPU options for Amazon EC2 instances

Many Amazon EC2 instances support simultaneous multithreading (SMT), which enables multiple
threads to run concurrently on a single CPU core. Each thread is represented as a virtual
CPU (vCPU) on the instance. An instance has a default number of CPU cores, which varies
according to instance type. For example, an `m5.xlarge` instance type has two CPU
cores and two threads per core by default—four vCPUs in total.

In most cases, there is an Amazon EC2 instance type that has a combination of memory and number
of vCPUs to suit your workloads. However, to optimize your instance for specific workloads
or business needs, you can specify the following CPU options during and after instance
launch:

- Number of CPU cores: You can customize the number
  of CPU cores for the instance. You might do this to potentially optimize the
  licensing costs of your software with an instance that has sufficient amounts of RAM
  for memory-intensive workloads but fewer CPU cores.
- Threads per core: You can disable SMT by specifying
  a single thread per CPU core. You might do this for certain workloads, such as high
  performance computing (HPC) workloads.

###### Considerations

- You can't modify the number of threads per core for T2, C7a, M7a, R7a, and Apple
  silicon Mac instances, and instances based on the AWS Graviton processor.
- The [number of instances that you can run](../../../ec2/latest/instancetypes/ec2-instance-quotas.md "../../../ec2/latest/instancetypes/ec2-instance-quotas.md")
  is based on the default vCPUs for the instance types used. How we calculate the
  vCPUs consumed by an instance is not affected by changing its CPU options.

###### Pricing

There is no additional charge for specifying CPU options. For EC2 instances that are
launched from license-included Windows and SQL Server AMIs, you can customize the CPU
options to take advantage of the EC2 Optimize CPUs feature to pay licensing fees based
on the number of vCPUs that are configured for your instance. For other EC2 instances,
you're charged the same as instances that are launched with the default CPU options.

###### Contents

- [Rules for specifying CPU options](instance-cpu-options-rules.md "instance-cpu-options-rules.md")
- [Supported CPU options](cpu-options-supported-instances-values.md "cpu-options-supported-instances-values.md")
- [Specify CPU options](instance-specify-cpu-options.md "instance-specify-cpu-options.md")
- [View CPU options](view-cpu-options.md "view-cpu-options.md")
- [Optimize CPUs](optimize-cpu.md "optimize-cpu.md")
