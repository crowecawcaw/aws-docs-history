

# SUS02-BP03 Match resource use to business need

 Designing customer experience with sustainability in mind involves making intentional trade-offs that can significantly reduce resource consumption while maintaining acceptable service levels. Align service-level objectives (SLOs) with your real business requirements to produce an efficient system. 

 **Desired outcome:** 
+  You design the customer experience to optimize resource consumption while still meeting user expectations. 
+  You apply deliberate trade-offs in quality, responsiveness, and processing to minimize environmental impact without compromising essential functionality or user satisfaction. 

 **Common anti-patterns:** 
+  Implementing unnecessarily high precision for all operations regardless of user needs. 
+  Defaulting to synchronous processing for all operations, even when immediate user feedback is not required. 
+  Precomputing all possible results rather than generating them on demand. 
+  Having uptime SLAs that imply high availability when it is not required for the business case. 
+  Maintaining capacity for theoretical peak performance instead of actual user requirements. 

 **Benefits of establishing this best practice:** 
+  Lowers the share of hardware related impacts from raw material extraction to end of life treatment (Scope 3 emissions). 
+  Lowers the share of required energy for operating infrastructure (Scope 2 emissions). 
+  Reduces resource consumption through appropriate quality vs resource trade-offs. 
+  Lowers environmental impact by eliminating unnecessary processing. 
+  Can improve overall system scalability and resilience. 
+  Creates flexible architectures that can adapt to varying demands. 
+  Often reduces operational costs alongside environmental impact. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Implementing sustainable customer experience design involves analyzing user needs, identifying appropriate trade-offs, and implementing architectural patterns that minimize resource consumption while maintaining acceptable service level agreement or requirements. This requires a nuanced understanding of both technical capabilities and user expectations. The process should be iterative so it can adapt to changes on business requirements or advancements. 

### Implementation steps
<a name="implementation-steps"></a>

1.  Analyze user needs and expectations: 
   +  Conduct regular user research to understand requirements as business need changes. 
   +  Identify features where lower precision or slower responses would be acceptable. 
   +  Prioritize workload functionality based on user importance. 

1.  Implement quality of results optimizations: 
   +  Use approximate calculations when exact precision is not necessary. 
   +  Implement tiered accuracy levels based on user needs and resource implications. 
   +  Optimize content delivery through summaries, data projection, and paging. 
   +  Optimize data streams based on device type by resizing [images](https://aws.amazon.com/blogs/compute/resize-images-on-the-fly-with-amazon-s3-aws-lambda-and-amazon-api-gateway/) and video content. For example, deliver smaller image sizes to mobile devices to reduce data transfer and processing costs. 

1.  Design appropriate service levels: 
   +  Define differentiated SLOs for various features based on their importance for key stakeholders. 
   +  Implement circuit breakers and graceful degradation for non-critical components to minimize resource waste during failures. For example, temporarily replace a malfunctioning dynamic element with a static image until the issue is resolved. This approach reduces unnecessary resource consumption from retries, logging, and exception handling. 
   +  Use [Amazon CloudWatch Service Level Objectives](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html) to monitor adherence to targets. 
   +  Consider speed of delivery requirements carefully, instant responses might not be needed for all operations, allowing for more efficient resource allocation. For example processing an order that is due to delivery next week. 

1.  Adopt asynchronous processing patterns: 
   +  Convert appropriate synchronous operations to asynchronous as detailed in [SUS04-BP01 Eliminate unnecessary data](sus04-bp01.md). 
   +  Implement notification mechanisms to alert users when processing is complete. For example, notify users rather than making them wait on a webpage, or refreshing a webpage. 

1.  Implement data processing only when needed: 
   +  Replace pre-computation with on-demand generation where appropriate. For example, don't run a report on a daily basis when the report can be generated when accessed. 
   +  Use managed compute services. For example, AWS Lambda for efficient serverless on-demand processing as this can increase resource utilization and therefore efficiency. 
   +  Implement caching strategies to balance responsiveness and resource usage. 
   +  Evaluate if a preloaded cache or a cache populated as on first need fit a data access pattern best. This is often based on technology constraints, data volume, and customer location requests to optimize resource usage. 

1.  Define and monitor appropriate key metrics: 
   +  Define a resource usage efficiency (RUE) metric for the workload by dividing its core resource provisioned metric by the unit of business value delivered, as described in [SUS01-BP01 Understand your resource usage efficiency](sus01-bp01.md). Expressing efficiency this way keeps service-level trade-offs anchored to business objectives rather than judged in isolation. 
   +  Use the [AWS Sustainability console](https://aws.amazon.com/sustainability/tools/console/) as the source of your measured environmental data, broken down by AWS Region, service, and usage account, and retrieve it programmatically through the AWS Sustainability API or a monthly data export. Carbon emissions data is published monthly for the previous usage month, so treat it as a reporting and trend signal rather than an operational one. 
   +  Use the [Sustainability Proxy Metrics and Carbon Emissions Dashboard](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/sustainability-proxy-metrics-dashboard.html) to track the resource metrics that form the numerator of your RUE, such as vCPU hours, storage usage, and data transfer, and to set workload-level targets against them. These resource metrics move with your usage, so they are what you monitor between emissions publications. 
   +  Regularly evaluate the balance between user experience and resource consumption. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SUS01-BP01 Understand your resource usage efficiency](sus01-bp01.md) 
+  [SUS03-BP02 Flatten demand peaks for consistently high resource utilization](sus03-bp02.md) 
+  [SUS04-BP01 Eliminate unnecessary data](sus04-bp01.md) 

 **Related documents:** 
+  [Availability and Beyond: Understanding and Improving the Resilience of Distributed Systems on AWS](https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/availability-and-beyond-improving-resilience.html) 
+  [What is Step Functions?](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) 
+  [Getting started with AWS Sustainability](https://docs.aws.amazon.com/sustainability/latest/userguide/getting-started.html) 
+  [Cloud Intelligence Dashboards on AWS](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/) 
+  [Sustainability Proxy Metrics and Carbon Emissions Dashboard](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/sustainability-proxy-metrics-dashboard.html) 
+  [Measure and track cloud efficiency with sustainability proxy metrics, Part I: What are proxy metrics?](https://aws.amazon.com/blogs/aws-cloud-financial-management/measure-and-track-cloud-efficiency-with-sustainability-proxy-metrics-part-i-what-are-proxy-metrics/) 
+  [Measure and track cloud efficiency with sustainability proxy metrics, Part II: Establish a metrics pipeline](https://aws.amazon.com/blogs/aws-cloud-financial-management/measure-and-track-cloud-efficiency-with-sustainability-proxy-metrics-part-ii-establish-a-metrics-pipeline/) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Integration patterns for distributed systems (API315)](https://www.youtube.com/watch?v=xc9P6wbhLwE) 
+  [AWS re:Invent 2024 - Try again: The tools and techniques behind resilient systems (ARC403)](https://www.youtube.com/watch?v=rvHd4Y76-fs) 
+  [AWS re:Invent 2025 - Optimizing generative AI workloads for sustainability and cost (AIM253)](https://www.youtube.com/watch?v=9SV_rIFrFh8) 

 **Related examples:** 
+  [Event-driven architecture with AWS Graviton Processors and Amazon EC2 Spot Instances](https://catalog.workshops.aws/well-architected-sustainability/en-US/2-software-and-architecture/event-driven-architecture-with-graviton-spot) 