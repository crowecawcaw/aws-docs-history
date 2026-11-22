

# Concepts

 This section describes key concepts referenced throughout the AWS Well-Architected Framework and pillar guides. These concepts go beyond simple definitions and include process and methodology guidance that supports well-architected workloads. 

 **Topics** 
+  [Five whys](#concept-five-whys) 
+  [Correction of error](#concept-correction-of-error) 
+  [Root cause analysis](#concept-root-cause-analysis) 
+  [Ishikawa diagram](#concept-ishikawa-diagram) 
+  [Canary deployment](#concept-canary-deployment) 
+  [Continuous integration and continuous deployment](#concept-cicd) 
+  [Game day](#concept-game-day) 
+  [Playbook](#concept-playbook) 
+  [Runbook](#concept-runbook) 
+  [Events, incidents, and problems](#concept-event-incident-problem) 
+  [Feedback loop](#concept-feedback-loop) 
+  [Resiliency and the components of reliability](#concept-resiliency-components) 
+  [Disaster Recovery (DR) objectives](#concept-dr-objectives) 
+  [Availability](#concept-availability) 
+  [Mechanical sympathy](#concept-mechanical-sympathy) 

## Five whys
<a name="concept-five-whys"></a>

 The *five whys* technique identifies the root cause of a problem by determining the relationship between different root causes. It can also identify the reasons for a positive outcome or goal. 

 You may need to ask more than five whys to find the causes, and you should consider whether a cause could have been prevented. If you identify human error as a root cause, it may indicate a lack of checks or fail-safe mechanisms. Always ask why the human error was possible. 

 Five whys provides a consistent approach to understanding causes and helps overcome assumptions. Apply it in a blame-free way, where the focus is on finding out *why* an issue occurred, rather than blaming *who* caused the issue. 

 **To run a five whys analysis** 

1.  Identify the problem. 

1.  Ask why the problem happened, and record the reason. 

1.  Decide if the reason is the root cause. Consider whether it could have been prevented, whether it could have been detected before it happened, and if it was human error, why it was possible. 

1.  Repeat the process using the reason as the new problem. Stop when you are confident that you have found the root causes. 

## Correction of error
<a name="concept-correction-of-error"></a>

 A *correction of error* (COE) is a process for improving quality by documenting and addressing issues. To perform this process, define a standardized way to document critical root causes, and review and address them. 

 **To write a correction of error** 

1.  Document what happened. 

1.  Document the impact on customers and your business. 

1.  Identify the root cause. 

1.  Gather supporting data, especially metrics and graphs. 

1.  Identify the critical pillar implications, especially security. 

1.  Document lessons learned. 

1.  Define corrective actions, action items, and related tickets. 

 Have your COE reviewed by your team and other teams. Review high-impact COEs during operational meetings. 

## Root cause analysis
<a name="concept-root-cause-analysis"></a>

 *Root cause analysis* (RCA) identifies what, how, and why an event or failure happened, resulting in corrective and preventive measures. Although the word *cause* is singular, experience shows that causes are usually plural. Look for multiple causes when carrying out an RCA. 

 Effective RCA requires a focus on solving the problem, rather than just understanding it. Be wary of cognitive biases that make you focus on recent occurrences, or look for data that confirms your assumptions. 

 **To perform a root cause analysis** 

1.  Define the problem. 

1.  Collect data. 

1.  Identify root causes using five whys and Ishikawa diagrams. 

1.  Implement countermeasures. 

1.  Evaluate and follow up. 

## Ishikawa diagram
<a name="concept-ishikawa-diagram"></a>

 An *Ishikawa diagram* (also called a fishbone or cause-and-effect diagram) captures the causal relationship between cause and effect, and groups causes into meaningful categories. Use Ishikawa diagrams alongside five whys and root cause analysis to visualize and organize the contributing factors to a problem. 

## Canary deployment
<a name="concept-canary-deployment"></a>

 A *canary deployment* is the incremental rollout of a new version of an application. The purpose is to reduce the risk of deploying a new version that impacts the workload by making it visible to users in a slow, controlled fashion. As you gain confidence in the deployment, you increase traffic to the new version until it fully replaces the current version. 

 **To perform a canary deployment** 

1.  Use a router or load balancer to send a small percentage of users to the new version. 

1.  Use a dimension on your KPIs to indicate which version is reporting metrics. 

1.  Measure the success of the deployment using the metrics, and determine whether to continue or roll back. 

1.  Increase the load on the new version until all users are on the new version or you have fully rolled back. 

## Continuous integration and continuous deployment
<a name="concept-cicd"></a>

 *Continuous integration* (CI) is the automation of building software and running tests against that software. CI detects broken builds and failed tests early by running automation on events such as code merges. A mature CI pipeline includes build automation, unit tests, integration tests, load and performance tests, and deployment to a pre-production environment for acceptance testing. 

 *Continuous deployment* (CD) is automated deployment to production that depends on results from testing and building. Every time a build succeeds and all tests pass, code is deployed automatically. Full continuous deployment includes deployment across isolation zones with appropriate waiting periods, monitoring of business KPIs during deployment, and automated rollback when KPIs decrease. 

## Game day
<a name="concept-game-day"></a>

 A *game day* simulates a failure or event to test systems, processes, and team responses. The purpose is to perform the actions the team would perform as if an exceptional event happened. Conduct game days regularly so that your team builds muscle memory on how to respond. Game days should cover operations, security, reliability, performance, and cost. 

 **To run a game day** 

1.  Define the scenario. Select the workload, the personnel who interact with it, and the simulated events to practice. Good sources for simulation events are previous failures, known process weaknesses, and seasonal spikes in demand. 

1.  Prepare the environment. Use infrastructure as code to replicate your production environment. Add safeguards such as permission requirements, criticality indicators, and runtime verifiers to prevent game day simulations from running against production. 

1.  Run the simulation. Run simulated events using runbooks with runtime verifiers. Do not announce individual events, as prompt detection is part of what you are testing. 

1.  Analyze results. Document where tooling, processes, and personnel do not meet expectations. Debrief upon completion and use a COE process to address issues found. 

## Playbook
<a name="concept-playbook"></a>

 A *playbook* documents the investigation process for responding to failure scenarios. Playbooks contain the predefined steps to identify an issue. The results from each step determine the next steps until the issue is identified or escalated. 

 Playbooks provide adequately skilled team members, who may be unfamiliar with the workload, the guidance necessary to gather information, identify potential sources of failure, isolate faults, and determine root cause. They preserve institutional knowledge and reduce the burden on key personnel. 

 A playbook should include: 
+  Requirements (permissions, tools, network access). 
+  Constraints (conflicts with other activities). 
+  Process steps and expected results, with follow-on steps based on outcomes. 
+  Escalation processes (who to escalate to, when to escalate, and third-party contacts). 

 Where appropriate, implement playbooks in code and set them up to initiate automatically. 

## Runbook
<a name="concept-runbook"></a>

 A *runbook* documents the procedures to achieve a specific outcome. Runbooks contain the minimum information necessary to successfully perform the procedure. Start with a valid manual process, then implement it in code and automate where appropriate to ensure consistency, speed responses, and reduce errors. 

 Runbooks provide adequately skilled team members, who may be unfamiliar with the workload, the instructions necessary to complete an activity. They preserve institutional knowledge and enable more team members to achieve the same outcomes. 

 A runbook should include: 
+  Requirements (permissions, tools, network access). 
+  Constraints (maintenance windows, impacted resources, conflicting activities). 
+  Procedure steps and expected outcomes. 
+  Escalation procedures. 

 When writing runbooks, consider the following: 
+  Runbooks should be reversible, either by reverting the change or by running a procedure that returns the environment to the previous state. 
+  Include a mechanism to verify that the runbook achieved its intended outcome. 
+  Implement appropriate controls to ensure runbooks can only be run by authorized personnel against explicitly defined targets. 
+  Test runbooks with the same engineering discipline used for application code. 

## Events, incidents, and problems
<a name="concept-event-incident-problem"></a>

 Operations management distinguishes between events, incidents, and problems. These terms describe escalating levels of operational concern. 


|  Term  |  Definition  | 
| --- | --- | 
|  Event  |  An observation of an action, occurrence, or change of state. Events can be planned or unplanned, and can originate internal or external to the workload. Events that require a response are called incidents.  | 
|  Incident  |  An event that requires intervention or response. Incidents can result from normal operation (for example, a component failure requiring replacement) or be self-inflicted (for example, deploying incompatible patches). Incidents that recur or cannot currently be resolved are called problems.  | 
|  Problem  |  An event that requires intervention and either recurs or cannot currently be resolved. The cause of a problem might not yet be understood, or it might be a known issue. Mitigations for known issues should be communicated to those affected to limit impact.  | 

## Feedback loop
<a name="concept-feedback-loop"></a>

 A *feedback loop* is a mechanism where the monitored results of a process or the output of a system are fed back into the control of that system so it can be adjusted to achieve desired outcomes. Feedback loops provide a way to measure and evaluate the achievement of outcomes against expected baselines, permitting appropriate action in response. 

## Resiliency and the components of reliability
<a name="concept-resiliency-components"></a>

 Reliability of a workload in the cloud depends on several factors, the primary of which is *Resiliency*: 
+  **Resiliency** is the ability of a workload to recover from infrastructure or service disruptions, dynamically acquire computing resources to meet demand, and mitigate disruptions, such as misconfigurations or transient network issues. 

 The other factors impacting workload reliability are: 
+  Operational excellence, which includes automation of changes, use of playbooks to respond to failures, and Operational Readiness Reviews (ORRs) to confirm that applications are ready for production operations. 
+  Security, which includes preventing harm to data or infrastructure from malicious actors, which would impact availability. For example, encrypt backups to ensure that data is secure. 
+  Performance efficiency, which includes designing for maximum request rates and minimizing latencies for your workload. 
+  Cost optimization, which includes trade-offs such as whether to spend more on EC2 instances to achieve static stability, or to rely on automatic scaling when more capacity is needed. 

 Resiliency is the primary focus of reliability. The other four aspects are also important and they are covered by their respective pillars of the Well-Architected Framework. Many of the best practices here also address those aspects of reliability, but the focus is on resiliency. 

## Disaster Recovery (DR) objectives
<a name="concept-dr-objectives"></a>

 In addition to availability objectives, your resiliency strategy should also include Disaster Recovery (DR) objectives based on strategies to recover your workload in case of a disaster event. Disaster Recovery focuses on one-time recovery objectives in response to natural disasters, large-scale technical failures, or human threats such as attack or error. This is different than availability which measures mean resiliency over a period of time in response to component failures, load spikes, or software bugs. 

 **Recovery Time Objective (RTO):** Defined by the organization. RTO is the maximum acceptable delay between the interruption of service and restoration of service. This determines what is considered an acceptable time window when service is unavailable. 

 **Recovery Point Objective (RPO):** Defined by the organization. RPO is the maximum acceptable amount of time since the last data recovery point. This determines what is considered an acceptable loss of data between the last recovery point and the interruption of service. 

![Timeline with a disaster event in the center, the recovery point (RPO) and the data-loss window before it, and the recovery time (RTO) and the downtime window after it.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/business-continuity.png)

*The relationship of RPO (Recovery Point Objective), RTO (Recovery Time Objective), and the disaster event*


 RTO is similar to MTTR (Mean Time to Recovery) in that both measure the time between the start of an outage and workload recovery. However MTTR is a mean value taken over several availability impacting events over a period of time, while RTO is a target, or maximum value allowed, for a *single* availability impacting event. 

## Availability
<a name="concept-availability"></a>

 *Availability* (also known as *service availability*) is both a commonly used metric to quantitatively measure resiliency, as well as a target resiliency objective. 
+  **Availability** is the percentage of time that a workload is available for use. 

 *Available for use* means that it performs its agreed function successfully when required. 

 This percentage is calculated over a period of time, such as a month, year, or trailing three years. Applying the strictest possible interpretation, availability is reduced anytime that the application isn't operating normally, including both scheduled and unscheduled interruptions. We define *availability* as follows: 

![Formula defining availability as available-for-use time divided by total time.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/availability-formula.png)

*Availability calculated from available time and total time*

+  Availability is a percentage uptime (such as 99.9%) over a period of time (commonly a month or year) 
+  Common short-hand refers only to the "number of nines"; for example, "five nines" translates to being 99.999% available 
+  Some customers choose to exclude scheduled service downtime (for example, planned maintenance) from the *Total Time* in the formula. However, this is not advised, as your users will likely want to use your service during these times. 

 Here is a table of common application availability design goals and the maximum length of time that interruptions can occur within a year while still meeting the goal. The table contains examples of the types of applications we commonly see at each availability tier. Throughout this document, we refer to these values. 


|  Availability  |  Maximum Unavailability (per year)  |  Application Categories  | 
| --- | --- | --- | 
|  99%  |  3 days 15 hours  |  Batch processing, data extraction, transfer, and load jobs  | 
|  99.9%  |  8 hours 45 minutes  |  Internal tools like knowledge management, project tracking  | 
|  99.95%  |  4 hours 22 minutes  |  Online commerce, point of sale  | 
|  99.99%  |  52 minutes  |  Video delivery, broadcast workloads  | 
|  99.999%  |  5 minutes  |  ATM transactions, telecommunications workloads  | 

 **Measuring availability based on requests.** For your service it may be easier to count successful and failed requests instead of "time available for use". In this case the following calculation can be used: 

![Formula defining availability as the number of successful responses divided by the number of valid requests.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/availability-formula-requests.png)

*Availability calculated from successful responses and valid requests*


 This is often measured for one-minute or five-minute periods. Then a monthly uptime percentage (time-base availability measurement) can be calculated from the average of these periods. If no requests are received in a given period it is counted at 100% available for that time. 

 **Calculating availability with hard dependencies.** Many systems have hard dependencies on other systems, where an interruption in a dependent system directly translates to an interruption of the invoking system. This is opposed to a soft dependency, where a failure of the dependent system is compensated for in the application. Where such hard dependencies occur, the invoking system's availability is the product of the dependent systems' availabilities. For example, if you have a system designed for 99.99% availability that has a hard dependency on two other independent systems that each are designed for 99.99% availability, the workload can theoretically achieve 99.97% availability: 

 Availinvok × Avail*dep1* × Avail*dep2* = Availworkload 

 99.99% × 99.99% × 99.99% = 99.97% 

 It's therefore important to understand your dependencies and their availability design goals as you calculate your own. 

 **Calculating availability with redundant components.** When a system involves the use of independent, redundant components (for example, redundant resources in different Availability Zones), the theoretical availability is computed as 100% minus the product of the component failure rates. For example, if a system makes use of two independent components, each with an availability of 99.9%, the effective availability of this dependency is 99.9999%: 

![Diagram of two dependencies with the same availability arranged in parallel, so the combined component stays available if either path works.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/rel-availability-redundant.png)

*Availability of two redundant dependencies in parallel*


 Availeffective = *Avail*MAX − ((100%−Availdependency)×(100%−Availdependency)) 

 99.9999% = 100% − (0.1%×0.1%) 

 *Shortcut calculation*: If the availabilities of all components in your calculation consist solely of the digit nine, then you can sum the count of the number of nines digits to get your answer. In the above example two redundant, independent components with three nines availability results in six nines. 

 **Calculating dependency availability.** Some dependencies provide guidance on their availability, including availability design goals for many AWS services. But in cases where this isn't available (for example, a component where the manufacturer does not publish availability information), one way to estimate is to determine the **Mean Time Between Failure (MTBF)** and **Mean Time to Recover (MTTR)**. An availability estimate can be established by: 

![Formula estimating availability as mean time between failures (MTBF) divided by the sum of MTBF and mean time to repair (MTTR).](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/avail-est-formula.png)

*Estimated availability from MTBF and MTTR*


 For example, if the MTBF is 150 days and the MTTR is 1 hour, the availability estimate is 99.97%. 

 For additional details, see [Availability and Beyond: Understanding and improving the resilience of distributed systems on AWS](https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/availability-and-beyond-improving-resilience.html), which can help you calculate your availability. 

 **Costs for availability.** Designing applications for higher levels of availability typically results in increased cost, so it's appropriate to identify the true availability needs before embarking on your application design. High levels of availability impose stricter requirements for testing and validation under exhaustive failure scenarios. They require automation for recovery from all manner of failures, and require that all aspects of system operations be similarly built and tested to the same standards. For example, the addition or removal of capacity, the deployment or rollback of updated software or configuration changes, or the migration of system data must be conducted to the desired availability goal. Compounding the costs for software development, at very high levels of availability, innovation suffers because of the need to move more slowly in deploying systems. The guidance, therefore, is to be thorough in applying the standards and considering the appropriate availability target for the entire lifecycle of operating the system. 

 Another way that costs escalate in systems that operate with higher availability design goals is in the selection of dependencies. At these higher goals, the set of software or services that can be chosen as dependencies diminishes based on which of these services have had the deep investments we previously described. As the availability design goal increases, it's typical to find fewer multi-purpose services (such as a relational database) and more purpose-built services. This is because the latter are easier to evaluate, test, and automate, and have a reduced potential for surprise interactions with included but unused functionality. 

## Mechanical sympathy
<a name="concept-mechanical-sympathy"></a>

 *Mechanical sympathy* is using a tool or system with an understanding of how it operates best. When you understand how a system is designed to be used, you can align with that design to gain optimal performance. For example, if a certain type of memory is more efficient when addresses are multiples of a factor, you can optimize performance by using data structure alignment. 