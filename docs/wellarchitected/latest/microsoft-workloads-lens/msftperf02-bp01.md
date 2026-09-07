

# MSFTPERF02-BP01 Choose the Amazon EC2 instance families that best fit the Microsoft workload
<a name="msftperf02-bp01"></a>

 Amazon EC2 provides different instance family types, addressing different purposes. For example, General purpose instances, such as m7i and m7a can be used for most production applications running on Windows Server. For non-production or less critical environments, t3 burstable instances may also be a fit. Memory optimized instances, such as r7i, r7a, and x2iedn provide greater ratio of memory to vCPU and are ideal for memory-intensive workloads, such as Microsoft SQL Server. 

 **Desired outcome:** Optimize performance and cost efficiency by selecting the most appropriate EC2 instance families that align with your Microsoft workload's specific compute, memory, and I/O requirements, ensuring optimal resource utilization while maintaining application performance and scalability. 

 **Common anti-patterns:** 
+  Choosing instance types based solely on cost without considering performance requirements, leading to under-provisioned resources that impact application performance and user experience. 
+  Using the same instance family for all workloads without evaluating specific requirements, missing opportunities to optimize performance for memory-intensive applications like SQL Server or compute-intensive .NET applications. 
+  Over-provisioning instances with excessive resources "just in case" without analyzing actual workload patterns, resulting in unnecessary costs and inefficient resource utilization. 

 **Benefits of establishing this best practice:** 
+  Optimized performance through instance families specifically designed for different workload characteristics, ensuring Microsoft applications receive appropriate compute, memory, and I/O resources. 
+  Improved cost efficiency by matching instance capabilities to actual workload requirements, avoiding over-provisioning while maintaining performance standards. 
+  Enhanced scalability and flexibility through understanding of instance family characteristics, enabling better architectural decisions for different Microsoft workload components. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Selecting appropriate EC2 instance families for Microsoft workloads requires understanding both your application requirements and the characteristics of different instance types. Begin by analyzing your workload patterns, then match them to instance families that provide optimal price-performance ratios for your specific use cases. 

### Implementation steps
<a name="implementation-steps"></a>

1.  Analyze your Microsoft workload requirements including CPU utilization patterns, memory requirements, storage I/O needs, and network performance requirements. 

1.  Evaluate different EC2 instance families based on your workload characteristics: 
   +  General purpose (m7i, m7a, m6i) for balanced workloads 
   +  Memory optimized (r7i, r7a, x2iedn) for SQL Server and memory-intensive applications 
   +  Compute optimized (c7i, c7a) for CPU-intensive .NET applications 
   +  Burstable (t3, t4g1) for variable or low-utilization workloads 

1.  Consider processor architecture options including Intel, AMD, and AWS Graviton processors based on application compatibility and performance requirements. 

1.  Evaluate instance sizes within families to match vCPU and memory requirements without over-provisioning resources. 

1.  Test different instance types in non-production environments to validate performance and cost characteristics. 

1.  Implement monitoring using Amazon CloudWatch and AWS Compute Optimizer to track instance utilization and receive rightsizing recommendations. 

1.  Establish regular review processes to evaluate instance performance and adjust selections based on changing workload patterns. 

1.  Document instance selection criteria and rationale for different Microsoft workload components to guide future decisions. 

 Windows Server OS does not support ARM based processors. Consider using AWS Graviton based instances can be used to run [cross-platform .NET on Linux](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/net-graviton.html). 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/) 

 **Related tools:** 
+  [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html) 