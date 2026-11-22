

# REL03-BP01 Choose how to segment your workload

 How you divide a workload (segmentation) sets the boundaries for where teams work and where faults are contained. Finer-grained segments improve agility and limit the blast radius of a failure, but they add the complexity of a distributed system. The right level depends on your reliability requirements, your team structure, and how much operational overhead you can absorb. 

 **Desired outcome:** 
+  Your workload is divided into components whose boundaries match reliability requirements and team ownership. 
+  Your components are as loosely coupled and stateless as their function allows, so they scale and recover independently. 
+  You choose a segmentation level deliberately, weighing agility and fault isolation against operational and latency costs. 
+  Your architecture can evolve toward finer segmentation as adoption grows, without a full rewrite. 

 **Common anti-patterns:** 
+  Teams build a monolith with no internal modularity, leaving no path to decompose it as the workload grows. 
+  Teams split a workload into services so interdependent that one failure cascades across all of them, recreating a monolith's fragility with added complexity. 
+  Teams adopt microservices for a product racing to first launch, paying distributed-system costs before they are needed. 
+  Teams decompose a monolith without checking whether its components can operate without shared state. 

 **Benefits of establishing this best practice:** 
+  Finer-grained segments increase agility, organizational flexibility, and scalability because small teams own well-defined pieces. 
+  A failure in one component affects a smaller share of the workload, which reduces the impact of service interruptions. 
+  Components with different availability requirements can be sized and operated independently. 
+  Team responsibilities become clearer because each service maps to a defined boundary. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Segmentation sits on a spectrum. For example: 
+  A monolith packages all functionality into one deployable unit. 
+  Service-oriented architecture (SOA) divides functionality into coarse services aligned to business functions. 
+  Microservices push those boundaries finer, so each service owns a single capability and its data. 

 Moving along this spectrum trades simplicity for autonomy. Smaller services deploy, scale, and fail on their own, but the workload as a whole becomes a distributed system with associated coordination costs. 

 The main cost of finer segmentation is distributed computing. Calls that were once in-process become network calls, which adds latency and new failure modes. A single user interaction now spans several services, so debugging is harder. Operating many independently deployed components raises the operational burden. A subtler failure mode is over-decomposition. When services grow so interdependent that one service's failure brings down the others, you have recreated a monolith's fragility while paying the full price of distribution. 

 A product racing to first launch benefits from the speed of a monolith or a few coarse services, whereas a workload expected to scale from the start justifies finer boundaries early. Statelessness makes fine segmentation practical because components that do not share state respond to demand and recover from faults on their own. When you refactor an existing monolith, assess how well its components tolerate separation before you commit. Even if you begin with a monolith, keep it modular so it can evolve toward SOA or microservices as adoption grows. 

![Comparison of three architecture styles: a monolithic application that does everything through a shared release pipeline with rigid scaling, a service-oriented architecture of some coupled services surfaced through a communication protocol, and microservices that each do one thing with independent deployment and scaling.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/monolith-soa-microservices-comparison.png)

*Monolithic, service-oriented, and microservices architectures compared*


 Several AWS services address the trade-offs of finer segmentation. [AWS X-Ray (part of Amazon CloudWatch)](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) traces requests across distributed services, which reduces the debugging cost of many moving parts. [Amazon VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-lattice.html) and [AWS Cloud Map](https://aws.amazon.com/cloud-map/) let distributed services discover and reach each other. [Amazon MQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html) can act as a service bus when you decouple a legacy application in stages. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Choose a target architecture:** Decide where to place your workload on the segmentation spectrum based on its reliability requirements, team structure, and tolerance for operational overhead. SOA offers smaller segments than a monolith while avoiding some microservices complexity, and microservices offer the finest boundaries and the most autonomy. For the decision criteria, see [Microservice trade-offs](https://martinfowler.com/articles/microservice-trade-offs.html). 

1.  **Refactor incrementally with the Strangler Fig pattern:** When you decompose an existing monolith, replace specific functions with new services one at a time rather than rewriting everything at once. For a worked approach, see [Seamlessly migrate on-premises legacy workloads using a strangler pattern](https://aws.amazon.com/blogs/architecture/seamlessly-migrate-on-premises-legacy-workloads-using-a-strangler-pattern/). 

1.  **Separate shared data along the new boundaries:** For a monolith with one shared database, split the data by business unit, access pattern, or data structure so it matches your service boundaries. Decide whether each segment fits a relational or non-relational store. For guidance on that choice, see [From SQL to NoSQL](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.html). 

1.  **Add service discovery for distributed components:** Distributed services need a way to find and reach each other as they scale and move. Use [AWS Cloud Map](https://aws.amazon.com/cloud-map/) for dynamic, DNS-based discovery. [Amazon VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-lattice.html) provides service-to-service connectivity with built-in traffic management across VPCs and accounts, and [Amazon ECS Service Connect](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html) simplifies service discovery and traffic handling for ECS workloads. 

1.  **Bridge legacy integration during migration:** When you move from a monolith to SOA, a managed message broker can decouple components while you redesign them. [Amazon MQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html) can serve as a service bus for applications that use standard messaging protocols. 

1.  **Instrument distributed tracing:** Once requests span multiple services, add tracing so you can follow one interaction across service boundaries and locate latency and failures. Use [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) to collect and visualize this data. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL03-BP02 Build services focused on specific business domains and functionality](rel03-bp02.md) 
+  [REL03-BP03 Provide service contracts per API](rel03-bp03.md) 
+  [REL04-BP02 Implement loosely coupled dependencies](rel04-bp02.md) 

 **Related documents:** 
+  [Implementing Microservices on AWS](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/) 
+  [What is SOA? - Service-Oriented Architecture Explained](https://aws.amazon.com/what-is/service-oriented-architecture/) 
+  [Bounded Context](https://martinfowler.com/bliki/BoundedContext.html) 
+  [Microservices](https://www.martinfowler.com/articles/microservices.html) 
+  [Develop REST APIs using OpenAPI in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api.html) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Circuit Breaker, Saga & Strangler Fig: Patterns for Transformation (MAM358)](https://www.youtube.com/watch?v=UJGbzjxfaw8) 

 **Related workshops:** 
+  [Iterative app modernization workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/f2c0706c-7192-495f-853c-fd3341db265a/en-US/intro) 

 **Related services:** 
+  [Microservices on AWS](https://aws.amazon.com/microservices/) 