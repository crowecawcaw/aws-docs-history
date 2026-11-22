

# Observe from multiple perspectives

 Implement observability in your workload so that you can understand its state and make data-driven decisions based on business requirements. 

 Observability goes beyond simple monitoring, providing a comprehensive understanding of a system's internal workings based on its external outputs. Rooted in metrics, logs, and traces, observability offers insights into system behavior and dynamics. With effective observability, teams can discern patterns, anomalies, and trends, helping them proactively address potential issues and maintain optimal system health. 

 Begin by defining your key performance indicators (KPIs) before you develop telemetry. For more information on KPIs, see [OPS02-BP01 Develop key performance indicators](ops02-bp01.md). A KPI measures a business outcome, which is what the workload achieves on behalf of its users. The Amazon retail site exists so that customers can order products, so its most important KPI is orders per minute. Deriving KPIs from business outcomes in this way informs which telemetry you collect and keeps monitoring aligned with what matters to the business. KPIs then stay part of the process: the telemetry you develop through these practices is what measures them, and regular analysis against them refines both the indicators and the telemetry as the workload evolves. 

 Expressing each KPI as a service level objective (SLO) gives it a target and an error budget, turning the measurement into something you can alarm on and be accountable for. Technical metrics belong in your KPIs and SLOs as well, and the RED method (Rate, Errors, Duration) is the natural starting set because each signal relates strongly to a business outcome: rate measures overall volume, while errors and duration shape the experience your users receive. A checkout that is slow or failing is an order that may never complete. 

 Observability empowers businesses to be proactive rather than reactive. Teams can understand the cause-and-effect relationships within their systems, predicting and helping prevent issues rather than reacting to them. As workloads evolve, revisit and refine the observability strategy, verifying that it remains relevant and effective. 


|  OPS01: How do you observe your workload from multiple perspectives?  | 
| --- | 
|  [OPS01-BP01 Develop application telemetry](ops01-bp01.md)  | 
|  [OPS01-BP02 Develop user experience telemetry](ops01-bp02.md)  | 
|  [OPS01-BP03 Develop dependency telemetry](ops01-bp03.md)  | 
|  [OPS01-BP04 Develop distributed tracing](ops01-bp04.md)  | 

## Capability intent
<a name="ops01-intent"></a>
+  Every layer of the workload emits metrics, logs, and traces in a consistent, open format, tied to the business KPIs the telemetry exists to measure. 
+  The experience real users receive is measured directly, and critical journeys are tested continuously with synthetic canaries. 
+  The internal and external dependencies a workload relies on are discovered, classified by criticality, and monitored against measurable health objectives. 
+  Requests can be followed across every service in their path, so the exact service and operation where latency or errors originate is known. 
+  Telemetry coverage stays complete as services change, so anomalies surface before customers report them. 

## Common issues to watch for
<a name="ops01-issues"></a>
+  Monitoring is limited to infrastructure metrics, so the workload's actual behavior and the customer's experience stay invisible. 
+  Telemetry is collected in inconsistent formats across teams, which makes signals impossible to correlate when a problem spans services. 
+  The experience real users receive is inferred from server-side averages rather than measured directly, hiding problems at the edge. 
+  Dependencies are unmonitored, so a failing downstream service is attributed to the wrong component and cascades go unnoticed. 
+  Instrumentation is added once and left behind as services change, so trace coverage decays and new code paths are invisible. 