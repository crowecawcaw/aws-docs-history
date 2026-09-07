

# SCSUS04-BP01 Optimize your compute workloads for your supply chain sustainability
<a name="scsus04-bp01"></a>

 Consider configuring AWS Compute Optimizer to analyze and investigate supply chain sustainability related workloads, to support your analysis on how to optimize the usage of compute resources to sustain your supply chain workloads. 

 **Desired outcome:** Optimize the performance of compute workloads to reduce energy consumption and emissions while maintaining the reliability of supply chain operations. 

 **Benefits of establishing this best practice:** Enhances the efficiency of compute resource utilization, reduces operational costs, and aligns sustainability efforts with performance objectives. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance-59"></a>

 Before proceeding with scenarios simulation over your supply chains operations, to help you understand why and which set of operations are requiring more compute and memory resources, consider to setup and run AWS Compute Optimizer combined with Amazon CloudWatch metrics to analyze resource utilization patterns and identify optimization opportunities, leading as a direct consequence to sustainability's KPIs improvements. 

### Implementation steps
<a name="implementation-steps-60"></a>

1.  Configure AWS Compute Optimizer to analyze supply chains workload performance and resource utilization patterns. 

1.  Provision Amazon CloudWatch and configure metrics collection to gather detailed performance data across all supply chains compute resources. 

1.  Analyze compute utilization patterns to identify over-provisioned or under-utilized resources that can be optimized. 

1.  Right-size compute instances based on actual usage patterns and performance requirements. 

1.  Implement automated scaling policies to match compute resources with actual demand patterns. 

1.  Monitor and measure the impact of optimization efforts on both performance and sustainability metrics. 