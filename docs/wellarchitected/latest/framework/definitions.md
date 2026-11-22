

# Definitions

 Every day, experts at AWS assist customers in architecting systems to take advantage of best practices in the cloud. We work with you on making architectural trade-offs as your designs evolve. As you deploy these systems into live environments, we learn how well these systems perform and the consequences of those trade-offs. 

 Based on what we have learned, we have created the AWS Well-Architected Framework, which provides a consistent set of best practices for customers and partners to evaluate architectures, and provides a set of questions you can use to evaluate how well an architecture is aligned to AWS best practices. 

## Pillars of the Framework
<a name="framework-pillars"></a>

 The AWS Well-Architected Framework is based on the following six pillars: 


|  **Name**  |  **Description**  | 
| --- | --- | 
|  [Operational excellence](operational-excellence.md)  |  The ability to support development and run workloads effectively, gain insight into their operations, and to continuously improve supporting processes and procedures to deliver business value.  | 
|  [Security](security.md)  |  The security pillar describes how to take advantage of cloud technologies to protect data, systems, and assets in a way that can improve your security posture.  | 
|  [Reliability](reliability.md)  |  The reliability pillar encompasses the ability of a workload to perform its intended function correctly and consistently when it's expected to. This includes the ability to operate and test the workload through its total lifecycle. This paper provides in-depth, best practice guidance for implementing reliable workloads on AWS.  | 
|  [Performance efficiency](performance-efficiency.md)  |  The ability to use computing resources efficiently to meet system requirements, and to maintain that efficiency as demand changes and technologies evolve.  | 
|  [Cost optimization](cost-optimization.md)  |  The ability to run systems to deliver business value at the lowest price point.  | 
|  [Sustainability](sustainability.md)  |  The ability to continually improve sustainability impacts by reducing energy consumption and increasing efficiency across all components of a workload by maximizing the benefits from the provisioned resources and minimizing the total resources required.  | 

## Definitions and terms
<a name="framework-definitions"></a>

 In the AWS Well-Architected Framework, we use the following terms: 
+  **Component:** The code, configuration, and AWS Resources that together deliver against a requirement. A component is often the unit of technical ownership, and is decoupled from other components. 
+  **Workload:** A set of components that together deliver business value. A workload is usually the level of detail that business and technology leaders communicate about. 
+  **Architecture:** Components work together in a workload. How components communicate and interact is often the focus of architecture diagrams. 
+  **Milestones:** Mark key changes in your architecture as it evolves throughout the product lifecycle (design, implementation, testing, go live, and in production). 
+  **Technology portfolio:** The collection of workloads that are required for the business to operate. 
+  **Best practice:** Approaches, processes, and methods that have been shown to lead to good outcomes. Best practices are identified by looking at sets of outcomes and finding common traits in those with successful outcomes, and reversing traits associated with failures. 
+  **Availability:** A measurement of a system's ability to provide its designed functionality at a given point in time. Highly available systems can withstand some measure of degradation while still remaining available. For more information, see [Availability](concepts.md#concept-availability). 
+  **Durability:** The ability of a system to remain functional over time, even when unexpected events occur. For example, a durable storage system reliably stores data without data loss. 
+  **Scalability:** A measurement of a system's ability to grow to accommodate an increase in demand. 
+  **Horizontal scaling:** Increasing capacity by adding more computers to a system, in contrast to vertical scaling (adding more resources to a single computer). Horizontally scalable systems can outperform vertically scalable systems by distributing workloads across many computers in parallel. 
+  **Elasticity:** The ability to acquire resources as you need them and release resources when you no longer need them. In the cloud, you can do this automatically. 
+  **Consistency:** The state where multiple systems storing a given piece of information return the same data when queried. A system is eventually consistent if there is a period of time during which different systems may return different answers. 
+  **Level of effort:** Categorizes the amount of time, effort, and complexity a task requires for implementation. Each organization needs to consider the size and expertise of the team and the complexity of the workload for additional context to properly categorize the level of effort for the organization. 
  +  **High:** The work might take multiple weeks or multiple months. This could be broken out into multiple stories, releases, and tasks. 
  +  **Medium:** The work might take multiple days or multiple weeks. This could be broken out into multiple releases and tasks. 
  +  **Low:** The work might take multiple hours or multiple days. This could be broken out into multiple tasks. 
+  **Level of risk:** The term *risk* in Well-Architected represents potential negative impact to a business, organization, or workload. In AWS Well-Architected, risks result from not performing certain architectural best practices, which raises *issues*, often referred to as *High risk issues (HRIs)* and *Medium risk issues (MRIs)*. 

 There are three levels of risk in Well-Architected best practices: 
+  **High risk:** Architectural and operational choices that may cause significant negative impact to a business. A high risk best practice is considered a foundational, must-do practice within a pillar. They may impact organizational operations, assets, and individuals. An example of an HRI from the security pillar is not securing your AWS account. 
+  **Medium risk:** Choices that may also impact your business negatively, but to a lesser extent than high risks. A medium risk best practice represents an enabling practice that can substantially improve a workload. An example of MRI on the security pillar is not auditing and rotating credentials periodically. 
+  **Low risk:** Low risk best practices represent optional or nice-to-have architectural choices, or they are practices that help you display progress towards other high or medium risk issues. We do not have a *low risk issue* item, as low risks are evaluated as progression, non-mandatory actions. 

 When architecting workloads, you make trade-offs between pillars based on your business context. These business decisions can drive your engineering priorities. You might optimize to improve sustainability impact and reduce cost at the expense of reliability in development environments, or, for mission-critical solutions, you might optimize reliability with increased costs and sustainability impact. In ecommerce solutions, performance can affect revenue and customer propensity to buy. Security and operational excellence are generally not traded-off against the other pillars. 