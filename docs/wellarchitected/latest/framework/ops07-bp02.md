

# OPS07-BP02 Identify and drive improvements

 With clear drivers for improvement, you evaluate opportunities against business outcomes and data, rank them by their effect, and automate work where the return justifies the effort. 

 **Desired outcome:** 
+  You collect operational data across your environment and correlate events and activities to business outcomes. 
+  You evaluate improvement opportunities against defined drivers rather than reacting to the most recent event. 
+  You compare metrics across environments and systems to find where improvement is needed, including partial failures that affect only some customers, requests, or locations. 
+  You maintain a history of deployments and their outcomes to measure the effect of changes. 
+  You measure the results of new features against the experience they were meant to deliver, judged from the customer's side rather than from internal health metrics alone. 

 **Common anti-patterns:** 
+  Teams collect telemetry across the environment but never correlate events and activities, so the data drives no decisions. 
+  Organizations gather detailed data at significant monitoring and logging cost yet never turn it into improvement actions. 
+  Improvement priorities ignore business outcomes and reflect individual preference or recency bias. 
+  Teams ship new features without measuring whether they achieved the intended result. 
+  Improvement work starts only after an incident, so preventable issues accumulate between events. 
+  Dashboards report the system as healthy while some customers experience failure, so a real degradation never becomes an improvement candidate. 

 **Benefits of establishing this best practice:** 
+  You prioritize improvements that deliver the greatest benefit for the business. 
+  You reduce the influence of emotion and recency by applying consistent criteria. 
+  You respond to business drivers such as compliance deadlines and customer needs, not only technical faults. 
+  You confirm whether a change actually improved anything by measuring its effect. 
+  You direct effort toward the systems and processes where data shows the most opportunity. 
+  You surface degradations that affect real customers but stay hidden from aggregate metrics, so the experience people actually get is what drives your backlog. 
+  You keep a continuously refreshed supply of improvement candidates drawn from operational evidence, rather than waiting for the next incident to generate them. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A driver for improvement is a documented reason to change a system, and only a supported desired outcome justifies the change. Most of these drivers fall into one of three categories: 

1.  Desired capabilities are new features or service options for something you cannot do today. 

1.  Unacceptable issues are bugs, vulnerabilities, and inefficiencies to remove, including rightsizing and optimization opportunities. 

1.  Compliance requirements are changes needed to meet regulation or policy, or to stay under support from a third party. 

 Apply consistent criteria to every candidate. Rank opportunities by their effect on cost, risk, customer experience, or revenue so priority does not depend on recency or individual preference. 

 Connect events and activities to business outcomes. Link each activity to its outcome, such as which deployment changed which metric and whether the metric moved the intended business result. Use these correlations to compare environments and systems and locate opportunities. Uncorrelated telemetry wastes monitoring and logging spend. 

 Aggregate metrics can hide a subset of users still affected. A change that improves a server-side average while the customer experience stays slow has not delivered the improvement. Judge each improvement by the customer experience, and treat the customer-side signal as authoritative when it disagrees with an internal one. 

 Some failures resist detection. A *gray failure* is one with differential observability: your health checks report the system as fine while customers observe it as broken. Finding them takes metrics dimensioned the way failures actually occur — per Availability Zone, per instance, per API, per client. An impairment confined to one dimension looks like an outlier. A related pattern is a failure that persists after its trigger is gone. A retry storm, or a cache that has lost its effectiveness, generates enough extra work to sustain the overload on its own. Recovery needs deliberate intervention such as [shedding load](https://builder.aws.com/content/3Eun1EEyX6p2e3VYNyRLSJzLuMV/using-load-shedding-to-avoid-overload). Both patterns belong on your improvement backlog as instrumentation gaps. 

 Build a reusable analysis capability to turn data into decisions. Query stored logs and operational data, transform it, and present it in dashboards that make trends visible to the people who prioritize work. A history of deployments and their outcomes gives you the before-and-after evidence to judge whether a change helped. 

 Drivers also come from outside your own telemetry. New service capabilities, security bulletins, and compliance program updates all signal changes to evaluate, and account-level advisory findings surface cost and resilience opportunities. Watch these sources on a cadence to keep your improvement backlog current. 

 [AWS DevOps Agent](https://aws.amazon.com/devops-agent/) reviews your incident history on a schedule and produces [proactive prevention recommendations](https://docs.aws.amazon.com/devopsagent/latest/userguide/production-operations-proactive-incident-prevention.html) grouped into observability, infrastructure, governance, and code optimization. It targets changes that prevent classes of incidents. Its observability recommendations focus on time to detection, which matters most for partial failures, and often name instrumentation you did not previously have. Each recommendation records the incidents that motivated it and its expected impact. For code or configuration changes, it can produce a specification detailed enough to hand to a coding agent. Recommendations you keep form a tracked backlog; discarding one with an explanation teaches the agent which improvements your team considers out of scope. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define your drivers for improvement:** Classify each opportunity as a desired capability, an unacceptable issue, or a compliance requirement - record the desired outcome that justifies it. Reject changes that do not map to a supported outcome. 

1.  **Establish feedback loops and correlate data to outcomes:** Collect operational data across your environment and connect events and activities to business results. A feedback loop is only as good as the telemetry feeding it, so build on the instrumentation established in [OPS01-BP01 Develop application telemetry](ops01-bp01.md) and [OPS01-BP02 Develop user experience telemetry](ops01-bp02.md), the latter of which supplies the customer-side signal you need to judge whether an improvement landed. Export operational logs to durable storage so you can analyze them over time, for example with [Export log data to Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/S3Export.html). 

1.  **Instrument for partial failures, not just large scale incidents:** Dimension your metrics along the boundaries where impairments actually occur, such as Availability Zone, instance, API operation, and client, so a problem confined to one dimension surfaces rather than being absorbed into an average. Add a customer-side view of the experience alongside your server-side health metrics. Outlier detection over log data, for example with [CloudWatch Contributor Insights](https://aws.amazon.com/blogs/mt/detecting-gray-failures-with-outlier-detection-in-amazon-cloudwatch-contributor-insights/), will point to the hosts or zones behaving differently from the rest. Record each detection gap you find as an improvement candidate in its own right. 

1.  **Build an analysis and reporting capability:** Query and transform your operational data with services such as [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) and [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html), then present trends in [AWS Quick Sight](https://docs.aws.amazon.com/quick/latest/userguide/what-is.html) dashboards, the business intelligence capability within [AWS Quick](https://aws.amazon.com/quick/). Use the [Cloud Intelligence Dashboards](https://catalog.workshops.aws/awscid/en-US) for prebuilt cost and usage views. 

1.  **Generate improvement candidates from operational evidence:** Have [AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/production-operations-proactive-incident-prevention.html) evaluate your incident history on a schedule and propose changes that would help prevent classes of incidents, categorized across observability, infrastructure, governance, and code optimization. Keep the ones worth pursuing so they form a tracked backlog, and discard the rest with an explanation so future evaluations improve. Use to inform prioritization. 

1.  **Monitor external sources of drivers:** Track new capabilities through [What's New with AWS](https://aws.amazon.com/new/), review [AWS Security Bulletins](https://aws.amazon.com/security/security-bulletins/) for vulnerabilities, and check [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) for cost and resilience findings. Fold compliance changes from [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/) into your backlog. 

1.  **Prioritize using consistent criteria:** Rank opportunities by their effect on business outcomes such as cost, risk, customer experience, and revenue. Apply the same criteria to every candidate so that priority does not depend on recency or individual preference. 

1.  **Measure results and automate where it pays off:** After you implement an improvement, compare the outcome against the deployment history to confirm the change helped, and check the customer-side signal rather than only the internal metric. Automate recurring improvement work where the frequency and cost of manual effort justify the investment. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [OPS07-BP01 Perform post-incident analysis](ops07-bp01.md) 
+  [OPS01-BP01 Develop application telemetry](ops01-bp01.md) 
+  [OPS01-BP02 Develop user experience telemetry](ops01-bp02.md) 
+  [OPS02-BP01 Develop key performance indicators](ops02-bp01.md) 
+  [OPS02-BP03 Regularly analyze workload metrics](ops02-bp03.md) 
+  [OPS06-BP02 Automate responses to events](ops06-bp02.md) 

 **Related documents:** 
+  [Export log data to Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/S3Export.html) 
+  [FSIREL06: Can your workload owners detect, locate, and recover from gray failures?](https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsirel06.html) 
+  [AWS DevOps Agent: Proactive incident prevention](https://docs.aws.amazon.com/devopsagent/latest/userguide/production-operations-proactive-incident-prevention.html) 
+  [AWS DevOps Agent: Production operations](https://docs.aws.amazon.com/devopsagent/latest/userguide/working-with-devops-agent-production-operations-index.html) 
+  [Using load shedding to avoid overload](https://builder.aws.com/content/3Eun1EEyX6p2e3VYNyRLSJzLuMV/using-load-shedding-to-avoid-overload) 
+  [AWS Security Bulletins](https://aws.amazon.com/security/security-bulletins/) 
+  [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) 
+  [AWS Compliance](https://aws.amazon.com/compliance/) 
+  [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/) 
+  [AWS Compliance latest news](https://aws.amazon.com/new/?nc1=f_cc&whats-new-content-all.sort-by=item.additionalFields.postDateTime&whats-new-content-all.sort-order=desc&awsf.whats-new-categories=marketing-marchitecture%23security-identity-and-compliance) 

 **Related videos:** 
+  [AWS Summit London 2024 - Building observability to increase resiliency (ARC302)](https://www.youtube.com/watch?v=rJ13gpd_X3M) 
+  [Observability for better resiliency: JustEat Takeaway.com's journey to operational excellence](https://www.youtube.com/watch?v=06oVJ9fdULM) 
+  [AWS re:Invent 2023 - Improve operational efficiency and resilience with Support (SUP310)](https://www.youtube.com/watch?v=jaehZYBNG0Y) 

 **Related examples:** 
+  [Detecting gray failures with outlier detection in Amazon CloudWatch Contributor Insights](https://aws.amazon.com/blogs/mt/detecting-gray-failures-with-outlier-detection-in-amazon-cloudwatch-contributor-insights/) 

 **Related services:** 
+  [Amazon Athena](https://aws.amazon.com/athena/) 
+  [AWS DevOps Agent](https://aws.amazon.com/devops-agent/) 
+  [AWS Glue](https://aws.amazon.com/glue/) 
+  [AWS Quick](https://aws.amazon.com/quick/) 
+  [AWS Quick Sight](https://aws.amazon.com/quick/quicksight/) 