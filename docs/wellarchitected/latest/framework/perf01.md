

# Validate workload performance requirements

 Performance efficiency starts with knowing what the business actually needs from a workload. Validating performance requirements gives technical teams and business stakeholders a common language and a shared set of goals, so performance carries appropriate weight in decisions at every level. When requirements are vague or assumed, teams optimize the wrong things and spend effort where it returns little value. 

 This capability covers how an organization identifies, validates, and manages performance requirements: tracing them to business objectives, weighing performance against the other non-functional requirements, expressing adherence through measurable KPIs, and defining the degradation alerts and tolerances that signal when performance falls short. 


|  PERF01: How do you validate and manage your workload's performance requirements?  | 
| --- | 
|  [PERF01-BP01 Validate requirements align to business needs](perf01-bp01.md)  | 
|  [PERF01-BP02 Evaluate the trade-offs between performance and other non-functional requirements](perf01-bp02.md)  | 
|  [PERF01-BP03 Derive and establish KPIs that validate adherence to your performance requirements](perf01-bp03.md)  | 
|  [PERF01-BP04 Establish criteria for performance degradation alerts and tolerances](perf01-bp04.md)  | 

## Capability intent
<a name="perf01-intent"></a>
+  Performance requirements are specific, measurable, and traced to business objectives, and every stakeholder shares the same definition of what "fast enough" means. 
+  Performance is treated as a first-class requirement, weighed against cost, reliability, security, and sustainability, with the reasoning behind each trade-off recorded and open to revisiting. 
+  Business-oriented KPIs, built on percentile-based operational metrics, show objectively whether the workload meets its requirements. 
+  Degradation criteria and tolerance thresholds turn those KPIs into a trusted early-warning system that reaches the right people before users are affected. 
+  Requirements, KPIs, and thresholds have named owners, are reviewed on a cadence, and are updated as business needs and traffic change. 

## Common issues to watch for
<a name="perf01-issues"></a>
+  Performance goals are stated qualitatively without a metric, a target, and a condition, so teams cannot test against them and "fast enough" means something different to everyone. 
+  The same performance targets are applied to every component, so effort and spend go to components that do not need them while the ones that do are under-served. 
+  Performance is optimized in isolation, so a gain in latency quietly costs cost, reliability, or security because the trade-off was never weighed or recorded. 
+  KPIs rely on averages that hide the tail, so a healthy-looking mean masks the slow experience a meaningful fraction of users actually receive. 
+  Alerting is too sensitive or fires on conditions no one can act on, so responders learn to ignore alerts and a real incident slips through the noise. 
+  Requirements and KPIs are set once and never revisited, so they drift out of alignment as traffic grows and business priorities change. 