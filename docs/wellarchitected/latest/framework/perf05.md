

# Monitor, test, and improve workload performance

 Meeting a workload's performance requirements once is not the same as meeting them over time. Traffic grows, dependencies change, and the infrastructure underneath the workload evolves. This capability covers the performance lifecycle from build through operation and optimization: instrumenting the paths that matter, testing the complete workload under representative conditions, investigating selected incidents, automating guarded remediation, keeping components current, and reviewing metrics and alarms. 

 The work is continuous and controlled. Instrumentation reveals the components that shape customer experience, testing exposes limits before users reach them, and automation or agents accelerate evidence gathering, triage, and routine low-risk actions. Workload owners retain responsibility for high-impact remediation, update adoption, and changes to monitoring. 


|  PERF05: How do you monitor, test, and improve workload performance over time?  | 
| --- | 
|  [PERF05-BP01 Use monitoring solutions to understand the areas where performance is most critical](perf05-bp01.md)  | 
|  [PERF05-BP02 Evaluate your workload performance](perf05-bp02.md)  | 
|  [PERF05-BP03 Use automation to proactively remediate performance-related issues](perf05-bp03.md)  | 
|  [PERF05-BP04 Keep your workload and services up-to-date](perf05-bp04.md)  | 
|  [PERF05-BP05 Review metrics at regular intervals](perf05-bp05.md)  | 

## Capability intent
<a name="perf05-intent"></a>
+  Instrumentation covers performance-relevant paths, and correlated metrics, logs, and traces identify the components that drive customer-facing latency and cost. 
+  The complete workload is tested against defined KPIs under representative normal, peak, and beyond-peak conditions, with results compared against previous baselines. 
+  Selected alerts and incident tickets start agent-assisted investigation, while deterministic automation remediates well-understood, low-risk conditions within approval, rollback, and verification controls. 
+  Workload inventory, provider announcements, and account-specific lifecycle events follow documented triage and ownership paths; candidate updates are adopted only after evidence and performance testing support the decision. 
+  Metrics, alarms, dashboards, SLOs, baselines, and thresholds are reviewed on a cadence and after significant incidents or workload changes. Agents and MCP tools prepare evidence, and workload owners validate findings and decide what changes. 
+  Performance work is prioritized by measured impact on business KPIs instead of intuition. 

## Common issues to watch for
<a name="perf05-issues"></a>
+  Teams rely on default resource counters and do not instrument performance-relevant paths, so they cannot attribute a slow customer request to the responsible component. 
+  Performance tests exercise isolated components, stop at expected peak, or use environments that do not reproduce the production factors affecting results, so scaling limits and time-dependent degradation remain hidden. 
+  Teams route every alert directly to a person or every alert to an agent without incident classification, severity, actionability, deduplication, maintenance, or skip criteria. 
+  Teams accept agent-generated root-cause hypotheses or mitigation plans without evidence, or automate remediation without least-privilege access, approval, rollback, and independent verification. 
+  Teams treat architecture choices as fixed, ignore provider and account-specific lifecycle events, or let an agent adopt updates without owner validation and performance testing. 
+  Teams set metrics and thresholds once, or schedule automated reports without a team review ritual, so stale alarms, missing coverage, and unowned recommendations accumulate. 