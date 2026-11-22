

# Create an effective event response

 You should anticipate operational events, both planned (for example, sales promotions, deployments, and failure tests) and unplanned (for example, surges in utilization and component failures). Use your existing runbooks and playbooks to deliver consistent results when you respond to alerts. Specify ownership of defined alerts to a role or team that is accountable for the response and escalations. Understand the business impact of your system components, and use this to target efforts when needed. These practices support evidence collection, which becomes crucial when performing post-incident analysis (also known as root cause analysis (RCA)) after events, and then to help prevent recurrence of failures or to document workarounds. 

 AWS helps simplify your event response by providing tools that support all aspects of your workload and operations as code. These tools help you script responses to operations events and start their initiation in response to monitoring data. 

 With AWS, you can improve recovery time by replacing failed components with known good versions, rather than trying to repair them. You can then carry out a separate analysis on the failed resources. 


|  OPS06: How do you create an effective event response?  | 
| --- | 
|  [OPS06-BP01 Create actionable alerts](ops06-bp01.md)  | 
|  [OPS06-BP02 Automate responses to events](ops06-bp02.md)  | 
|  [OPS06-BP03 Define escalation paths](ops06-bp03.md)  | 

## Capability intent
<a name="ops06-intent"></a>
+  Every alert maps to a documented and ideally automated response, with a clear owner and escalation path. 
+  Alert noise is controlled by grouping related signals and tuning thresholds against historical data, so operators trust the alarms they receive. 
+  Frequent, well-understood events with a safe remediation are handled automatically, freeing operators for problems that need human judgment. 
+  Escalation paths are pre-agreed: who acts at each tier, the permissions they need, and which high-impact actions are pre-approved. 
+  Response paths are rehearsed through drills and refined after incidents, so they hold up under real conditions. 

## Common issues to watch for
<a name="ops06-issues"></a>
+  Alerts fire without a defined response or owner, so a signal arrives but nobody knows what to do with it. 
+  Alarm noise trains operators to ignore alerts, so the one that matters is missed. 
+  Frequent, well-understood events are handled manually every time, consuming operator attention that novel problems need. 
+  Escalation depends on informal knowledge of who to call, so the right person is reached late during an incident. 
+  Escalation paths and automated responses are never rehearsed, so they fail the first time they are actually used. 