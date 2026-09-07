

# SCCOST01-BP02 Adopt a flexible and scalable cloud infrastructure
<a name="sccost01-bp02"></a>

 A typical supply chain landscape will include ERPs, warehouse management systems (WMS), and transportation management systems (TMS) running on a large infrastructure that needs to be reliable, scalable and optimized for cost and performance. 

 **Desired outcome:** Pay as you go cloud infrastructure configured with auto scaling to expand or shrink as per demand of the workload. Cloud service quotas configured for peak usage. 

 **Benefits of establishing this best practice:** Reduced cost and better resiliency. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance-47"></a>

 Use AWS' pay-as-you-go model to align costs with actual usage and demand fluctuations, while implementing auto scaling capabilities to automatically adjust resources based on workload demands. Configure service quotas to accommodate peak usage for respective services and use containerization and serverless technologies for improved resource utilization and cost optimization. 

### Implementation steps
<a name="implementation-steps-48"></a>

1.  Assess current infrastructure costs and identify opportunities for pay-as-you-go optimization. 

1.  Implement auto-scaling policies for compute, storage, and database resources based on demand patterns. 

1.  Configure appropriate service quotas to handle peak usage while avoiding unnecessary over-provisioning. 

1.  Deploy containerization technologies to improve resource utilization and reduce infrastructure costs. 

1.  Implement serverless architectures for event-driven workloads to minimize idle resource costs. 

1.  Establish cost monitoring and alerting mechanisms to track spending and identify optimization opportunities. 