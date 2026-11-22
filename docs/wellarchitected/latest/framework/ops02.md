

# Derive essential insights

 Keep your workload healthy by observing it, not by assuming it. Use relevant metrics, logs, and traces to build a comprehensive view of workload performance, and start with key performance indicators (KPIs): define them before you develop telemetry, derive them from the business outcomes the workload exists to achieve, and analyze what you collect against them. That alignment keeps teams making decisions on measurements that genuinely matter, for the system and for the business. 

 Observability is selective by design. The goal is not to collect everything: it is to concentrate on the signals that explain workload behavior and business impact, and to drop the data that explains nothing. Deriving essential insights from focused telemetry keeps both understanding and cost under control. 

 Collected data has to be interpreted before it becomes insight. Establish a baseline for each key signal, set alert thresholds against it, and monitor for deviations. A shift in a key metric, especially when correlated with other signals, points at the specific area where a problem is forming. 

 With these insights, you can address challenges early, before they affect the workload or the business outcomes it serves. 

 [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) provides the metrics, logs, dashboards, and alarms these practices build on. [Amazon CloudWatch Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html), when enabled, adds a service-level view of each service's RED metrics (rate, errors, and duration) and the service level objectives (SLOs) that track them, and [Application Observability (APM)](https://aws.amazon.com/cloudwatch/features/application-observability-apm/) is the trace backend for following individual requests. Together these services turn collected telemetry into the insights that inform data-driven decisions. 


|  OPS02: How do you derive essential insights from your telemetry?  | 
| --- | 
|  [OPS02-BP01 Develop key performance indicators](ops02-bp01.md)  | 
|  [OPS02-BP02 Create actionable insights with dashboards](ops02-bp02.md)  | 
|  [OPS02-BP03 Regularly analyze workload metrics](ops02-bp03.md)  | 
|  [OPS02-BP04 Regularly analyze workload logs](ops02-bp04.md)  | 
|  [OPS02-BP05 Regularly analyze workload traces](ops02-bp05.md)  | 
|  [OPS02-BP06 Augment observability with AI assistants](ops02-bp06.md)  | 

## Capability intent
<a name="ops02-intent"></a>
+  Key performance indicators are defined from business outcomes, paired with owners, targets, and thresholds, and expressed as service level objectives where they apply. 
+  Dashboards present business KPIs alongside the technical signals beneath them, scoped to a defined audience and maintained as code. 
+  Metrics, logs, and traces are analyzed on a regular cadence against a steady-state baseline, not only when something breaks. 
+  Analysis prioritizes business impact and correlates signals across sources to locate where a problem is forming. 
+  Every review ends with owned actions, so insight leads to change rather than accumulating unread. 

## Common issues to watch for
<a name="ops02-issues"></a>
+  Telemetry is collected but never turned into insight, so storage grows while decisions are still made on hunches. 
+  KPIs are technical measures with no line to a business outcome, so a green dashboard can coexist with unhappy customers. 
+  Dashboards try to show everything, burying the few signals that matter under metrics nobody acts on. 
+  Analysis happens only during incidents, so slow degradations that never trip an alarm go unnoticed. 
+  Reviews end without owned actions, so the same problems are rediscovered at the next review. 