# Rules for specifying CPU options for an

Amazon EC2 instance

To specify the CPU options for your instance, be aware of the following rules:

- You can't specify CPU options for bare metal instances.
- You can specify CPU options both during and after instance launch.
- To configure CPU options, you must specify both the number of CPU cores and
  threads per core in the request. For example requests, see [Specify CPU options for an Amazon EC2
  instance](instance-specify-cpu-options.md "instance-specify-cpu-options.md").
- The number of vCPUs for the instance is the number of CPU cores multiplied by
  the threads per core. To specify a custom number of vCPUs, you must specify a
  valid number of CPU cores and threads per core for the instance type. You cannot
  exceed the default number of vCPUs for the instance. For more information, see
  [Supported CPU options for Amazon EC2
  instance types](cpu-options-supported-instances-values.md "cpu-options-supported-instances-values.md").
- To disable simultaneous multithreading (SMT), also referred to as
  hyper-threading, specify one thread per core.
- In the console, when you [change the
  instance type](ec2-instance-resize.md "ec2-instance-resize.md") of an existing instance, Amazon EC2 applies the CPU option
  settings from the existing instance to the new instance, if possible. If the new
  instance type doesn't support those settings, the CPU options are reset to
  **Use default CPU options**. This option uses the default number
  of vCPUs for the new instance type.

To update settings for the new instance, select **Specify CPU
options** under **Advanced details** in the
**Change instance type** view.

- The specified CPU options persist after you stop, start, or reboot an
  instance.
- If you use Reserved Instances, discounts may not be applied when you configure Optimize CPUs
  for instances launched from license-included Windows AMIs in the same payer account. We recommend
  that you use Savings Plans to reduce vCPU-based licensing costs and provide comparable savings on
  your compute costs.
- To save on licensing costs for instances launched from Windows and SQL Server
  license-included AMIs, you must configure a minimum of four vCPUs. If you configure
  fewer than four vCPUs, default billing is applied.
- Optimize CPUs for License-Included instances is not supported on T3 instance types.
