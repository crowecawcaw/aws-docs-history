# Best practice 9.1 – Identify critical performance criteria for your storage workload

In data analytics, throughput is often a constraining
factor to enable your workloads to run effectively.
Throughput is measured by the amount of information that has
successfully moved through the network, compute, or storage
layers. Improving throughput in each of these layers
generally results in better query performance.

## Suggestion 9.1.1 – Use performance monitoring tools to determine if the analytics system performance is limited by compute, storage, or networking

Use a metric collection and reporting system, such as
Amazon CloudWatch, to analyze the performance
characteristics of the analytics system. Evaluate the
measured performance metrics relative to system reference
documentation to characterize the system constraints for
the workload as a percentage of maximum performance.
