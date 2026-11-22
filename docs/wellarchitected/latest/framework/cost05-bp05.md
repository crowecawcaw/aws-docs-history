

# COST05-BP05 Select components for business-value-driven cost optimization

 Managed and serverless options remove idle capacity and operational overhead, event-driven designs do work only when required, and open-source software avoids license fees. Weigh these choices against the business value each component delivers. 

 **Desired outcome:** 
+  Your workload architecture is cost-optimized and aligned with business objectives. 
+  You use managed services, serverless, and containers where each fits best. 
+  You reduce licensing costs through open-source alternatives where they meet requirements. 
+  Your event-driven designs improve scalability and cost efficiency. 

 **Common anti-patterns:** 
+  Components are selected on familiarity without weighing cost. 
+  Capacity is overprovisioned instead of using services that scale with demand. 
+  Long-term cost implications of a component choice go unexamined. 
+  Component costs are never measured against business metrics and outcomes. 

 **Benefits of establishing this best practice:** 
+  Infrastructure and operational costs fall. 
+  Cost tracks actual resource usage more closely. 
+  The architecture scales and adapts more readily. 
+  Managed services cut management overhead. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Managed and serverless services charge for what you consume and scale with demand, removing the idle capacity of fixed provisioning. They also handle operations for you, so both cost and management overhead fall. 

 In event-driven designs, components act only when an event arrives, so nothing runs while the system is idle. Continuous polling spends compute, network bandwidth, and connection setup checking for work that may not exist. For workloads with uneven or bursty demand, moving from polling to events cuts the cost of idle polling. 

 Component choice also includes licensing. Choosing open-source software or engines without license fees removes a recurring cost that scales with each instance. An open-source database on a managed service avoids both license fees and administrative effort. 

 Lower-cost components are only better if they serve the business. A serverless function that meets demand at low cost is the right call unless it fails a latency requirement. Measure each component's cost against the business metric it supports, and make the trade-off explicit when the lowest-cost option falls short. Without that measurement, teams either overprovision out of caution or cut cost until the workload no longer meets its goals. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Select each component to optimize cost:** Use your prioritized list and analysis to choose the option that best matches your organizational priorities. Instead of adding capacity to meet demand, consider options that deliver better performance at lower cost. For example, review instance sizing and CPU architecture recommendations in [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/), and migrate open-source [Amazon RDS](https://aws.amazon.com/rds/) databases to [AWS Graviton](https://aws.amazon.com/ec2/graviton/) for lower cost and improved energy efficiency. 

1.  **Apply serverless and event-driven patterns:** Use serverless services such as [AWS Lambda](https://aws.amazon.com/lambda/), [Amazon SQS](https://aws.amazon.com/sqs/), [Amazon SNS](https://aws.amazon.com/sns/), and [Amazon SES](https://aws.amazon.com/ses/) to remove resource management. Build [event-driven architecture](https://aws.amazon.com/what-is/eda/) for distributed, microservice-based applications to gain scalable, resilient, and cost-effective solutions. 

1.  **Review and re-evaluate regularly:** Review workload performance and cost on a schedule, and assess newly released features or services that could improve the current profile. Re-evaluation keeps component choices aligned as usage and available options change. 

1.  **Implement component-level cost allocation:** Develop [tagging strategies](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) and [cost allocation mechanisms](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) that tracks cost at the component level. This visibility lets teams see the financial impact of their component selections and creates accountability for ongoing optimization. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [COST05-BP03 Analyze the total cost of ownership of each component](cost05-bp03.md) 
+  [COST05-BP04 Select software with cost-effective licensing](cost05-bp04.md) 
+  [COST06-BP01 Perform cost modeling](cost06-bp01.md) 

 **Related documents:** 
+  [AWS Serverless](https://aws.amazon.com/serverless/) 
+  [What is event-driven architecture?](https://aws.amazon.com/what-is/eda/) 
+  [Serverless Applications Lens](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html) 

 **Related examples:** 
+  [Event-driven architecture](https://aws.amazon.com/event-driven-architecture/) 
+  [Best practices for working with AWS Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html) 