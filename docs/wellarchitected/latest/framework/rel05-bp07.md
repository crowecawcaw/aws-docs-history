

# REL05-BP07 Implement emergency levers

 An emergency lever is a rapid, pre-tested process that reduces availability impact during an incident. It disables, throttles, or changes the behavior of a component or dependency, so you can shed a non-critical failure or absorb an unexpected demand spike. Your workload keeps performing its business-critical functions while the lever is active. 

 **Desired outcome:** 
+  Your critical components stay available when non-critical dependencies fail or demand spikes unexpectedly. 
+  Your workload degrades gracefully and continues its business-critical functions while a lever is active. 
+  Your levers have clear, deterministic criteria for activation and deactivation. 
+  Your responders have established, tested processes to invoke rather than improvising under pressure. 

 **Common anti-patterns:** 
+  Failure of a non-critical dependency takes down the core workload. 
+  Critical component behavior is not tested or verified during non-critical component impairment. 
+  No clear, deterministic criteria define when to activate or deactivate a lever. 
+  Levers are designed but never exercised, so responders cannot trust them during a real incident. 

 **Benefits of establishing this best practice:** 
+  Availability of critical components improves, because responders have ready processes for demand spikes and non-critical failures. 
+  Incident response is faster and more predictable, because the mechanism is defined and tested in advance. 
+  Non-critical failures stay contained rather than cascading into the core workload. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 During an incident, designing a mitigation on the spot is slow and risky. A prepared and well-known emergency lever can remove that risk by providing a way to turn off a non-critical feature, throttle a dependency, or switch a component into a reduced mode. Predefined criteria specify when to pull and release the lever. Test the mechanism before you need it, so you can trust it during an incident. 

 Levers depend on a clear split between critical and non-critical functionality, which is a joint business and technical decision. Map each technical component to the business function it serves, then rank each as critical or non-critical. The ranking varies by organization and workload. A lever protects the critical set by sacrificing something in the non-critical set. Without this map, you cannot tell which failures a lever should respond to or what it is safe to disable. 

 A lever uses established reliability patterns, applied under defined conditions. Load shedding drops low-priority work to protect capacity. Throttling caps intake to keep a dependency within its limits. Graceful degradation turns a hard dependency into a soft one so the component keeps its core function. A lever packages one of these into a known-good process with an activation trigger, so during an incident the decision is only whether to pull the lever. 

 Activating a lever must not introduce bimodal behavior, where the system behaves differently enough in degraded mode that the degraded path is itself untested and fragile. Static stability guards against this. The right trigger metric depends on what the lever protects. Common choices are latency or the count of failed requests to a dependency. Monitor and alarm on those metrics so activation can be prompt and, where appropriate, automated. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Rank components as critical or non-critical:** Map each technical component to its business function and rank it critical or non-critical. Treat this as a joint technical and business decision. For an example of critical and non-critical functionality at scale, see [How Amazon.com search uses chaos engineering](https://builder.aws.com/content/2dvVG1dk8rSnrDHekhjk09CjXVP). 

1.  **Design critical components to withstand non-critical failure:** During dependency analysis, consider all potential failure modes, and verify that your lever mechanisms still deliver critical functionality to downstream components when a non-critical dependency fails. 

1.  **Test critical behavior during lever activation:** Exercise your critical components while a lever is active to confirm they continue functioning. Avoid bimodal behavior by applying [REL11-BP05 Use static stability to prevent bimodal behavior](rel11-bp05.md) so the degraded path is as well understood as the primary path. 

1.  **Define and monitor activation triggers:** Choose the metrics that signal when a lever is needed, such as dependency latency or failed-request counts, and set monitoring and alarms on them. The right metrics depend on the workload and what the lever protects. 

1.  **Define the lever procedure:** Document the manual or automated steps that make up the lever, with deterministic activation and deactivation criteria. Build the procedure from established mechanisms such as [load shedding](https://builder.aws.com/content/3Eun1EEyX6p2e3VYNyRLSJzLuMV/using-load-shedding-to-avoid-overload) , [REL05-BP02 Throttle requests](rel05-bp02.md), or [REL05-BP01 Implement graceful degradation to transform applicable hard dependencies into soft dependencies](rel05-bp01.md). 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL05-BP01 Implement graceful degradation to transform applicable hard dependencies into soft dependencies](rel05-bp01.md) 
+  [REL05-BP02 Throttle requests](rel05-bp02.md) 
+  [REL05-BP04 Fail fast and limit queues](rel05-bp04.md) 
+  [REL11-BP05 Use static stability to prevent bimodal behavior](rel11-bp05.md) 

 **Related documents:** 
+  [The Amazon Builders' Library: Using load shedding to avoid overload](https://builder.aws.com/content/3Eun1EEyX6p2e3VYNyRLSJzLuMV/using-load-shedding-to-avoid-overload) 
+  [The Amazon Builders' Library: Automating safe, hands-off deployments](https://builder.aws.com/content/3ErTKQOTKc5NIw031UePBPxTQ6I/automating-safe-hands-off-deployments) 
+  [How Amazon.com search uses chaos engineering](https://builder.aws.com/content/2dvVG1dk8rSnrDHekhjk09CjXVP) 

 **Related videos:** 
+  [AWS re:Invent 2024 - How Netflix handles sudden load spikes in the cloud (NFX301)](https://www.youtube.com/watch?v=TkFyZyxFRBM) 