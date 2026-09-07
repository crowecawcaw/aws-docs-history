

# Practice Cloud Financial Management
<a name="practice-cloud-financial-management"></a>


| HPCCOST01: How do you keep track of expenditure used for HPC? | 
| --- | 
|   | 

 HPC workloads can use a large number of resources in a short space of time. Use of cloud compute changes the way users decide what to run, where decisions on what jobs will be run are budget based. Using the following best practices, on-going expenditure can be tracked. 

## HPCCOST01-BP01 Use the right tools to collect and analyze the data you need.
<a name="hpccost01-bp01"></a>

 There are many ways to keep track of costs using the standard AWS tools, which will vary depending on the chosen architecture. Please refer to the [Cost Optimization Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html). 

### Implementation guidance
<a name="implementation-guidance-20"></a>
+  For HPC applications, it is very common to use tagging. Resources used for jobs can be tagged with project names, user ids or any other attributes you choose. Once resources are tagged with tags activated for cost allocation, you can generate reports based on the attributes chosen earlier. 
+  If a queuing system, such as [Slurm](https://slurm.schedmd.com/documentation.html) or [IBM Spectrum LSF Suites](https://www.ibm.com/products/hpc-workload-management) is in use, they typically have ways to log the usage of resources, such as Slurm Accounting or LSF Analytics. Details vary depending on the system in use. 

## Key AWS services
<a name="key-aws-services-7"></a>
+  [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) 
+  [Slurm accounting with AWS ParallelCluster](https://docs.aws.amazon.com/parallelcluster/latest/ug/slurm-accounting-v3.html) 
+  [Metrics in Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) 