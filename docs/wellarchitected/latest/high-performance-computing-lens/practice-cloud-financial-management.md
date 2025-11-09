# Practice Cloud Financial Management

| HPCCOST01: How do you keep track of<br>expenditure used for HPC? |
| ---------------------------------------------------------------- |
|                                                                  |

HPC workloads can use a large number of resources in a short space of time. Use of cloud
compute changes the way users decide what to run, where decisions on what jobs will be run are
budget based. Using the following best practices, on-going expenditure can be tracked.

## HPCCOST01-BP01 Use the right tools to collect and analyze the data you need.

There are many ways to keep track of costs using the standard
AWS tools, which will vary depending on the chosen architecture.
Please refer to the
[Cost Optimization Pillar - AWS Well-Architected Framework](../cost-optimization-pillar/welcome.md "../cost-optimization-pillar/welcome.md").

### Implementation guidance

- For HPC applications, it is very common to use tagging.
  Resources used for jobs can be tagged with project names,
  user ids or any other attributes you choose. Once
  resources are tagged with tags activated for cost
  allocation, you can generate reports based on the
  attributes chosen earlier.
- If a queuing system, such as
  [Slurm](https://slurm.schedmd.com/documentation.html "https://slurm.schedmd.com/documentation.html")
  or
  [IBM
  Spectrum LSF Suites](https://www.ibm.com/products/hpc-workload-management "https://www.ibm.com/products/hpc-workload-management") is in use, they typically have
  ways to log the usage of resources, such as Slurm
  Accounting or LSF Analytics. Details vary depending on the
  system in use.

## Key AWS services

- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/ "https://aws.amazon.com/aws-cost-management/aws-cost-explorer/")
- [Slurm
  accounting with AWS ParallelCluster](../../../parallelcluster/latest/ug/slurm-accounting-v3.md "../../../parallelcluster/latest/ug/slurm-accounting-v3.md")
- [Metrics
  in Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md")
