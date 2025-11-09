# Cost effective resources

| HPCCOST02: How have you evaluated the trade-offs between job completion time and<br>cost? |
| ----------------------------------------------------------------------------------------- |
|                                                                                           |

With greater resource availability there is greater capability to run jobs on faster – or
more – compute resources. Even though this may result in a faster turnaround of a job (based
on wall clock time), it could also result in a much greater cost of running that job if speed
up is non-linear. For every workload there is a sweet-spot for run time and cost.

## HPCCOST02-BP01 Use the most appropriate instances and resources

Using the appropriate instances and resources for your system is key to cost
management. The technology choice may increase or decrease the overall cost of running an
HPC workload.

### Implementation guidance

- For example, a tightly coupled HPC workload might take ten hours to run on one
  instance (X CPU cores), if the same job is run on 10 EC2 instances (10X CPU cores), it
  may take 2 hours (performance scaling can be but is typically not linear). The cost
  for EC2 will be higher, however the results of the calculation will be available much
  quicker. This could reduce the research and development time, and for example reduce
  time to market.
- Verify that instances have sufficient physical memory to complete jobs but not
  more, as unused memory will not improve compute performance. Depending on the
  methodology, increasing the number of nodes per job may distribute the computational
  problem and reduce the required memory per node.
- Choose the pricing model best suited for workload duration and criticality, such
  as using On Demand for high priority workloads, spot for flexible HPC workloads, and
  RI for consistent HPC workloads to help optimize cost.
- Reducing the runtime can also reduce costs for surrounding services, such as
  storage, since these resources will not be needed for as long.
- The choice of storage can also impact cost. Many HPC applications read and write
  significant amounts of data. If the time to read and write data can be reduced, then
  the compute will be needed for less time. There are many different types and
  performance settings for storage. Picking the optimum version for your application can
  improve efficiency and reduce cost overall.
- For some applications, the cost of licenses exceeds the cost of AWS resources.
  It may be worth spending a little more on AWS resources to achieve better
  performance and save money overall.
