

# Establish workload supportability for production

 Evaluate the operational readiness of your workload, processes, procedures, and personnel to understand the operational risks related to your workload. Manage the flow of change into your environments. 

 You should use a consistent process (including manual or automated checklists) to know when you are ready to go live with your workload or a change. This also helps you find any areas that you need to make plans to address. Create runbooks that document your routine activities and playbooks that guide your processes for issue resolution. Use a mechanism to manage changes that supports the delivery of business value and helps mitigate risks associated with change. 


|  OPS05: How do you establish workload supportability for production?  | 
| --- | 
|  [OPS05-BP01 Develop and test runbooks to perform procedures](ops05-bp01.md)  | 
|  [OPS05-BP02 Develop and test playbooks to respond to incidents](ops05-bp02.md)  | 
|  [OPS05-BP03 Create support plans for production workloads](ops05-bp03.md)  | 
|  [OPS05-BP04 Assess operational readiness](ops05-bp04.md)  | 

## Capability intent
<a name="ops05-intent"></a>
+  Routine and high-stakes procedures are captured as version-controlled runbooks that state the desired outcome, required tools and permissions, error handling, and escalation path. 
+  Investigation is guided by tested playbooks that lead from symptoms to a likely cause and link to the runbook that resolves it. 
+  Every software and service dependency has a support plan matched to the response time the workload's service levels require. 
+  Operational readiness is assessed against a checklist built from best practices and past incidents, before launch and periodically across the lifecycle. 
+  Findings are triaged into accepted mitigations or backlog items, and lessons from incidents feed back into the readiness checklist. 

## Common issues to watch for
<a name="ops05-issues"></a>
+  Procedures exist only in individual memory, so support quality depends on who happens to be on call. 
+  Runbooks and playbooks are written once and never tested, so they fail or mislead during a real incident. 
+  Dependency support plans do not match the response times the workload promises, leaving teams waiting during a dependency failure. 
+  Workloads go live without a readiness review, so known gaps are discovered in production. 
+  Readiness checklists are static, so the same class of incident recurs because its lesson was never fed back. 