

# SUS04-BP03 Implement distributed systems appropriately

 Designing efficient distributed systems requires careful consideration of both what components should be distributed and where they should be located. Properly architected distributed systems can significantly reduce resource consumption by placing processing close to data, minimizing data movement, and optimizing communication patterns between components. 

 **Desired outcome:** 
+  You design distributed systems that minimize resource consumption while meeting performance and availability requirements. 
+  You place components strategically to reduce data movement, optimize network traffic, and maximize local processing efficiency, lowering overall energy consumption and environmental impact. 

 **Common anti-patterns:** 
+  Moving large data volumes to centralized processing instead of placing computation close to the data, including failing to process at the edge or aggregate deltas locally where appropriate. 
+  Using synchronous, overly frequent, or unnecessarily verbose communication patterns where asynchronous or batched approaches would reduce idle resources and network overhead. 
+  Implementing distributed architectures more complex than the workload justifies, or tightly coupling components in chains that amplify resource usage and propagate inefficiencies. 
+  Designing system topology without considering data flow patterns, resulting in avoidable cross-zone or cross-Region traffic. 

 **Benefits of establishing this best practice:** 
+  Reduction of network traffic lowers the required share on hardware related impacts for networking, from raw material extraction to end of life treatment (Scope 3 emissions), and share on energy for operating the infrastructure (Scope 2 emissions). 
+  Increases overall system efficiency through improved resource utilization. 
+  Often reduces costs associated with data transfer and processing. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Designing efficient distributed systems requires understanding your workload's data flows, processing and resource requirements, and access patterns. By mapping these elements and optimizing component placement and communication patterns, you can create architectures that minimize resource consumption while maintaining performance. Evaluate if a [distributed architecture](https://aws.amazon.com/what-is/distributed-computing/) fits your scale and team needs. 

 If distributed systems fit your use case, consider using [domain-driven design (DDD)](https://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/overview.html#ddd) to break down a system. In DDD, architects decompose the solution into bounded contexts by using business logic-based decomposition instead of technical decomposition. 

### Implementation steps
<a name="implementation-steps"></a>

1.  Analyze your workload's data flows and access patterns: 
   +  Break down systems into domains using DDD principles, carefully evaluating trade-offs of different distribution strategies. 
   +  Map data sources, processing components, and consumers in your architecture. 
   +  Analyze the geographic distribution of your users and data sources. 
   +  Analyze read or write rate and cost of staleness of data to determine viability for caching. 

1.  Evaluate architecture patterns for sustainability: 
   +  Consider trade-offs when choosing architectures that minimize unnecessary distribution when simpler patterns would be more efficient. Assess [monolithic and microservice](https://aws.amazon.com/compare/the-difference-between-monolithic-and-microservices-architecture/) approaches based on what would be the best fit for your workload characteristics. 
   +  Identify high-volume data transfers and frequent communication paths, and consider a [hexagonal architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/overview.html#hexagonal) to implement distributed systems. 
   +  Use [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html) or [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) for efficient distributed data processing. 

1.  Optimize data processing location: 
   +  Move computation closer to the user when possible using services such as [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) at edge locations. This requires making trade-offs regarding where data resides. 
   +  Use location-based method (LBM) data about electricity grids to inform optimal Region selection for workload placement. For more detail, see [SUS01-BP03 Select Regions that align to your sustainability goals](sus01-bp03.md). 

1.  Implement appropriate communication patterns: 
   +  Use asynchronous communication where possible with services such as Amazon SQS and Amazon SNS. 
   +  Adopt an [event-driven architecture](https://aws.amazon.com/event-driven-architecture/) where components react to events rather than calling each other directly. Use Amazon EventBridge to route and filter events at the router so consumers are invoked only for events they act on. This removes the idle waiting inherent in synchronous chains and scales each component to its own demand. For the provisioning side of this pattern, see [SUS02-BP01 Implement elasticity for variable workloads](sus02-bp01.md). 
   +  Publish events carrying only the fields consumers need, or a reference to the payload rather than the payload itself, so routing a high-volume event stream does not become its own source of data movement. 
   +  Implement caching with Amazon CloudFront or Amazon ElastiCache. 
   +  Use [connection pooling](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.howitworks.html) and persistent connections to reduce setup and decommissioning overhead where relevant (for example, there are many clients that reuse the connection many times). 
   +  Transmit only the data actually needed (for example, transmitting sub-sections of a larger document). 
   +  Implement data compression and efficient serialization formats, and verify that you transmit only data needed for a given operation. 

1.  Optimize network topology: 
   +  Use Amazon VPC design to minimize cross-AZ and cross-Region traffic. 
   +  Consider AWS Global Accelerator for optimized global traffic routing. 

1.  Monitor and continuously optimize: 
   +  Track network transfer [metrics](https://aws.amazon.com/cloudwatch/features/infrastructure-observability/) and identify optimization opportunities. 
   +  Monitor component utilization and latency across your distributed system. 
   +  Regularly review architecture as usage patterns and AWS capabilities evolve. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SUS01-BP03 Select Regions that align to your sustainability goals](sus01-bp03.md) 
+  [SUS02-BP01 Implement elasticity for variable workloads](sus02-bp01.md) 
+  [SUS02-BP03 Match resource use to business need](sus02-bp03.md) 
+  [SUS03-BP01 Optimize workloads for high resource usage efficiency](sus03-bp01.md) 
+  [SUS03-BP02 Flatten demand peaks for consistently high resource utilization](sus03-bp02.md) 
+  [SUS04-BP02 Select appropriate file formats, compression, and software implementation](sus04-bp02.md) 

 **Related documents:** 
+  [Optimizing your AWS Infrastructure for Sustainability, Part III: Networking](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-iii-networking/) 
+  [Amazon ElastiCache Documentation](https://docs.aws.amazon.com/elasticache/) 
+  [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/) 
+  [Domain-driven design (DDD)](https://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/overview.html#ddd) 
+  [Building hexagonal architectures on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/introduction.html) 
+  [What's the Difference Between Monolithic and Microservices Architecture?](https://aws.amazon.com/compare/the-difference-between-monolithic-and-microservices-architecture/) 
+  [What is an Event-Driven Architecture?](https://aws.amazon.com/event-driven-architecture/) 
+  [RDS Proxy concepts and terminology](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.howitworks.html) 

 **Related videos:** 
+  [AWS re:Invent 2023 - Navigating the journey to serverless event-driven architecture (API303)](https://www.youtube.com/watch?v=hvGuqHp051c) 
+  [AWS re:Invent 2023 - Advanced integration patterns & trade-offs for loosely coupled systems (API309)](https://www.youtube.com/watch?v=FGKGdUiZKto) 
+  [AWS TV - Optimizing Enterprise Software with Domain-Driven Design: From Composable Architectures to Efficient DynamoDB Implementation](https://aws.amazon.com/video/watch/07104c7732d/) 

 **Related examples:** 
+  [AWS Networking Workshops](https://catalog.workshops.aws/networking/en-US) 
+  [Architecting for sustainability - Minimize data movement across networks](https://catalog.us-east-1.prod.workshops.aws/workshops/7c4f8394-8081-4737-aa1b-6ae811d46e0a/en-US) 