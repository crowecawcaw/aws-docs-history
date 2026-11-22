

# Detection

 Detection is the ability to see what is happening across a workload and to make sense of it when something goes wrong. It rests on two connected habits: capturing the events that record activity, and turning those events into signals a team can act on before a problem escalates. 

 Evidence comes first. Every layer of a workload produces security-relevant activity, from control-plane calls and network flows to application authentication and authorization events. Capturing that activity consistently, storing it where it stays trustworthy, and keeping it long enough to investigate is what makes detection and later incident response possible. Gaps in coverage become gaps in the investigation. 

 Raw events on their own do not tell a team when to act. Metrics measured against a known baseline, alarms that reach the right responders, and dashboards tuned to each workload convert stored data into early warning. This capability covers building that visibility and acting on it. It does not cover the incident response process itself, which later capabilities address. 


|  SEC04: How do you detect and investigate security events?  | 
| --- | 
|  [SEC04-BP01 Configure service and application logging](sec04-bp01.md)  | 
|  [SEC04-BP02 Prepare metrics, alarms, and dashboards](sec04-bp02.md)  | 

## Capability intent
<a name="sec04-intent"></a>
+  Security-relevant events are captured from every workload component across the infrastructure and application layers in a consistent, queryable format. 
+  Logs are centralized, retained under defined policies, and protected by access controls that keep the evidence reliable and tamper-resistant. 
+  Sensitive data such as credentials and personal information is masked or removed before it reaches log storage. 
+  Meaningful metrics are measured against established baselines, so abnormal behavior stands out from normal activity. 
+  Alarms route to the responders who can act, and dashboards present the signal each team needs to read quickly under pressure. 
+  Investigators can query and correlate events across sources fast enough to support active incident response. 

## Common issues to watch for
<a name="sec04-issues"></a>
+  Logging is enabled on some components and skipped on others, so investigations hit blind spots exactly where detail is needed. 
+  Logs sit in fragmented formats and locations, so correlating events across components is slow or impossible. 
+  Log stores lack access controls or share the accounts they monitor, so a workload under unauthorized control can read or erase its own audit trail. 
+  Sensitive values such as credentials or personal data land in logs unmasked, spreading that exposure to everyone who can read the store. 
+  Alarm thresholds are set without a baseline, so alerts either flood responders with noise or stay silent during a real event. 
+  Dashboards are built and then never acted on, so the metrics reveal problems that no one responds to. 