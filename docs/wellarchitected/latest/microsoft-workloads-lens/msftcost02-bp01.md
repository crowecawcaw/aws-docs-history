

# MSFTCOST02-BP01 Right size Windows instances
<a name="msftcost02-bp01"></a>

 AWS Compute Optimizer uses machine learning to analyze the performance metrics and utilization patterns of Microsoft workloads running on AWS, including Windows Server instances and SQL Server deployments. By examining historical resource usage data across CPU, memory, and network dimensions, Compute Optimizer provides tailored recommendations for right-sizing EC2 instances running Microsoft applications, helping organizations optimize both performance and cost. The service can identify when Windows workloads are over-provisioned or under-provisioned, suggesting instance types that are aligned with actual resource requirements. This is valuable for Microsoft-heavy enterprises that have migrated to AWS, as Windows workloads often have different resource consumption patterns and proper sizing is crucial for managing the additional licensing costs associated with Windows Server and SQL Server instances. 

 **Desired outcome:** Optimize Microsoft workload deployments on AWS to substantially reduce compute costs while maintaining or improving application performance through right-sized instances, resulting in lower Windows licensing fees and improved resource utilization metrics across CPU, memory, and network resources as validated by AWS Compute Optimizer recommendations. 

 **Common anti-patterns:** 
+  Deploying Microsoft workloads on the largest available EC2 instance types as a precautionary measure regardless of actual resource requirements, leading to severe over-provisioning and unnecessary Windows licensing costs for unused capacity. 
+  Ignoring AWS Compute Optimizer's recommendations and maintaining static instance sizes based on initial deployment configurations, even when utilization metrics consistently show periods of low resource usage or performance bottlenecks that indicate the need for right-sizing. 

 **Benefits of establishing this best practice:** 
+  Cost Efficiency: Organizations can eliminate resource waste by precisely matching instance types to actual workload requirements, reducing both EC2 instance costs and associated Microsoft licensing fees which are typically tied to instance size and processor count. 
+  Performance Optimization: Workloads receive the right balance of compute resources, preventing both performance bottlenecks from under-provisioning and excess capacity from over-provisioning, leading to consistent and reliable application performance for end users. 
+  Data-Driven Decision Making: IT teams can make instance sizing decisions based on machine learning-analyzed historical performance data rather than guesswork, reducing the operational overhead of manual monitoring and enabling proactive capacity planning for Microsoft workloads. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 This implementation guide provides a high-level approach to leveraging AWS Compute Optimizer for Microsoft workload optimization on AWS. By following these best practices, organizations can establish a systematic process for analyzing and right-sizing their Windows-based instances while ensuring optimal performance and cost efficiency. The guide covers essential steps from initial Compute Optimizer activation and baseline assessment through to ongoing monitoring and adjustment phases. Whether you are running Windows Server applications, SQL Server databases, or other Microsoft workloads, these recommendations will help you implement a data-driven optimization strategy that aligns with both AWS architectural principles and Microsoft licensing considerations. 

### Implementation steps
<a name="implementation-steps"></a>

1.  Enable AWS Compute Optimizer and verify data collection across accounts 

1.  Create inventory of Microsoft workloads and licenses 

1.  Define performance baselines and thresholds for each workload type 

1.  Review initial optimization recommendations after 14-day analysis period 

1.  Create prioritized migration schedule for instance right-sizing 

1.  Execute instance changes during maintenance windows 

1.  Set up automated monitoring and reporting 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Right size Windows workloads](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/rightsize.html) 
+  [Reduce Microsoft SQL Server licensing costs with AWS Compute Optimizer](https://aws.amazon.com/blogs/modernizing-with-aws/reduce-microsoft-sql-server-licensing-costs-with-aws-compute-optimizer/) 
+  [Optimizing your cost with rightsizing recommendations](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-rightsizing.html) 

 **Related tools:** 
+  [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) 