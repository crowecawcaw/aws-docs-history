

# Design principles
<a name="operational-excellence-design-principles"></a>

In addition to the lens-level design principles, the operational excellence best practices in this lens are represented by at least one of the following principles:
+ **Define purpose, autonomy, and success criteria before deployment:** Role descriptions, scope boundaries, and measurable outcomes are prerequisites for shipping. They drive guardrails, monitoring thresholds, and escalation triggers downstream.
+ **Promote agents through a lifecycle with explicit gates:** SME-driven validation, CI/CD designed for non-deterministic systems, and staged rollouts prevent prompt, tool, or model changes from regressing production silently.
+ **Detect drift and remediate automatically where safe:** Configuration drift, behavioral anomalies, and tool failures get detected, contained, and recovered without human intervention for routine cases. Humans are reserved for exceptions.
+ **Operate by KPIs that map to business outcomes:** Resolution rate, escalation rate, customer satisfaction, and task completion sit alongside infrastructure metrics with equal weight in dashboards and reviews.
+ **Manage agents as a portfolio:** Registries, catalogs, ownership records, and decommissioning processes treat agents as a population that needs governance, not as one-off projects.
+ **Codify and recycle operational knowledge:** Runbooks, decision artifacts, change records, and incident learnings become structured inputs to future agent improvement and human operator training, not tribal knowledge.