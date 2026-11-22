

# Availability and recovery objectives

 Availability and recovery objectives are the measures that turn reliability from an intention into a target you can design and test against. Availability quantifies how much of the time a workload performs its function. Recovery objectives set the limits on downtime and data loss you are willing to accept after a disruption. These are among the most misunderstood concepts in reliability, so this page defines them precisely and shows how to determine the levels your workload actually needs. 

## Availability
<a name="rel-availability-and-recovery-objectives-availability"></a>

 Availability, also called service availability, is both a metric that measures resilience and a target resilience objective. 
+  **Availability** is the percentage of time that a workload is available for use. 

 *Available for use* means the workload performs its agreed function successfully when required. The percentage is calculated over a period such as a month, a year, or a trailing three years. Under the strictest interpretation, availability is reduced any time the application is not operating normally, including both scheduled and unscheduled interruptions. 

![Formula defining availability as available-for-use time divided by total time.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/availability-formula.png)

*Availability calculated from available time and total time*

+  Availability is a percentage of uptime, such as 99.9 percent, over a period of time. 
+  Common shorthand refers only to the number of nines. "Five nines," for example, means 99.999 percent available. 
+  Some teams exclude scheduled downtime, such as planned maintenance, from total time. This is not advised, because your users still want to use the service during those times. 

 The following table shows common availability design goals, the maximum interruption per year that still meets each goal, and the kinds of applications typically seen at each tier. 


|  Availability  |  Maximum unavailability per year  |  Application categories  | 
| --- | --- | --- | 
|  99%  |  3 days 15 hours  |  Batch processing, data extraction, transfer, and load jobs  | 
|  99.9%  |  8 hours 45 minutes  |  Internal tools such as knowledge management and project tracking  | 
|  99.95%  |  4 hours 22 minutes  |  Online commerce, point of sale  | 
|  99.99%  |  52 minutes  |  Video delivery, broadcast workloads  | 
|  99.999%  |  5 minutes  |  ATM transactions, telecommunications workloads  | 

 **Measuring availability by requests.** For some services it is easier to count successful and failed requests than time available for use. In that case you can measure availability as the ratio of successful responses to valid requests. 

![Formula defining availability as the number of successful responses divided by the number of valid requests.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/availability-formula-requests.png)

*Availability calculated from successful responses and valid requests*


 This is often measured over one-minute or five-minute periods, and a monthly uptime percentage is calculated from the average of those periods. A period with no requests counts as 100 percent available. 

 **Calculating availability with hard dependencies.** Many systems have hard dependencies on other systems, where an interruption in a dependency directly interrupts the invoking system. This is different from a soft dependency, where the application compensates for a dependency failure. Where hard dependencies exist, the invoking system's availability is the product of the dependencies' availabilities. A system designed for 99.99 percent availability with hard dependencies on two independent systems, each designed for 99.99 percent, can theoretically achieve 99.97 percent: 

 99.99% × 99.99% × 99.99% = 99.97% 

 Understand your dependencies and their availability design goals as you calculate your own. 

 **Calculating availability with redundant components.** When a system uses independent, redundant components, such as redundant resources in different Availability Zones, the theoretical availability is 100 percent minus the product of the component failure rates. Two independent components, each with 99.9 percent availability, give an effective availability of 99.9999 percent: 

![Diagram of two dependencies with the same availability arranged in parallel, so the combined component stays available if either path works.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/image2.png)

*Availability of two redundant dependencies in parallel*


 99.9999% = 100% − (0.1% × 0.1%) 

 As a shortcut, if the availabilities all consist solely of the digit nine, sum the count of nines. Two redundant, independent components with three nines each give six nines. 

 **Calculating dependency availability.** Some dependencies publish their availability, including availability design goals for many AWS services. Where a dependency does not publish this, you can estimate it from the mean time between failure (MTBF) and the mean time to recover (MTTR): 

![Formula estimating availability as mean time between failures (MTBF) divided by the sum of MTBF and mean time to repair (MTTR).](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/avail-est-formula.png)

*Estimated availability from MTBF and MTTR*


 For example, an MTBF of 150 days and an MTTR of 1 hour give an availability estimate of 99.97 percent. For more detail, see [Availability and beyond: understanding and improving the resilience of distributed systems on AWS](https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/availability-and-beyond-improving-resilience.html). 

 **The cost of availability.** Designing for higher availability usually costs more, so identify your true availability needs before you design. High availability imposes stricter requirements for testing and validation under exhaustive failure scenarios, requires automated recovery from every kind of failure, and requires that capacity changes, deployments, rollbacks, and data migrations all meet the same standard. At very high availability, innovation slows because you must deploy more carefully. The choice of dependencies also narrows, because fewer services have had the deep investment that very high availability requires, so purpose-built services tend to replace multi-purpose ones. Apply the standard thoroughly and choose an availability target that fits the entire lifecycle of operating the system. 

## Recovery objectives
<a name="rel-availability-and-recovery-objectives-recovery-objectives"></a>

 Alongside availability objectives, your resilience strategy should include disaster recovery objectives, based on strategies to recover a workload after a disaster event. Disaster recovery focuses on one-time recovery in response to natural disasters, large-scale technical failures, or human threats such as attack or error. This differs from availability, which measures mean resilience over a period of time in response to component failures, load spikes, or software bugs. 
+  **Recovery time objective (RTO)** is the maximum acceptable delay between the interruption of service and its restoration. It sets the acceptable window during which service is unavailable. RTO is defined by the organization. 
+  **Recovery point objective (RPO)** is the maximum acceptable time since the last data recovery point. It sets the acceptable loss of data between the last recovery point and the interruption. RPO is defined by the organization. 

![Timeline with a disaster event in the center, the recovery point (RPO) and the data-loss window before it, and the recovery time (RTO) and the downtime window after it.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/business-continuity.png)

*The relationship of RPO (Recovery Point Objective), RTO (Recovery Time Objective), and the disaster event*


 RTO is similar to MTTR in that both measure the time between the start of an availability-affecting event and recovery. MTTR is a mean taken over several availability-affecting events over a period, while RTO is a target, the maximum value allowed, for a single availability-affecting event. 

## Understanding your availability needs
<a name="rel-availability-and-recovery-objectives-understanding-your-availability-needs"></a>

 It is common to first think of availability as a single target for the application as a whole. On closer inspection, different parts of an application often have different availability requirements. Some systems prioritize receiving and storing new data ahead of retrieving existing data. Others prioritize real-time operations over operations that change configuration. A service might need very high availability during certain hours and tolerate longer disruption outside them. Decomposing an application into its parts and evaluating the availability requirement of each lets you focus effort and expense where it matters, rather than engineering the whole system to the strictest requirement. 

 Critically evaluate the unique aspects of your applications and, where appropriate, differentiate the availability and disaster recovery design goals to reflect the needs of your business. 

 Within AWS, services are commonly divided into a data plane and a control plane. The data plane delivers real-time service, and the control plane configures the environment. Amazon EC2 instances running, Amazon RDS database reads and writes, and Amazon DynamoDB table read and write operations are data plane operations. Launching new EC2 instances or RDS databases, or changing table metadata in DynamoDB, are control plane operations. Data planes typically have higher availability design goals than control planes, so workloads with high availability requirements should avoid a run-time dependency on control plane operations. 

 Planning for availability is not done only before launch. It continues as you refine your design, gain operational experience, learn from real-world events, and endure failures of different types. Align the availability a workload needs to its business criticality: define a business criticality framework with RTO, RPO, and availability, then assess each workload against it. This approach requires that the people implementing a workload understand the framework and the impact their workload has on business needs. 