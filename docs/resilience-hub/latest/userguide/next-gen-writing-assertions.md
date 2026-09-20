

# Writing effective assertions
<a name="next-gen-writing-assertions"></a>

The most useful assertions tell the assessment something it cannot learn from your resources. Focus on the following areas:
+ **Traffic and scale** – Typical and peak request rates, how spiky traffic is, and whether spikes are predictable.
+ **Environment purpose** – Whether the service is production, staging, or development, and how strictly it should be assessed.
+ **Components not visible to resource discovery** – Software you run on Amazon EC2 instances or Amazon EKS nodes, third-party services, on-premises systems, or dependencies in other accounts that are not part of the service's input sources.
+ **Tenancy and isolation** – Whether the service is multi-tenant, how tenants are isolated, and whether Availability Zone isolation matters for your use case.
+ **Disaster recovery intent** – The Multi-AZ or multi-Region strategy you intend to operate (for example, active-active or warm standby) and how data is replicated.
+ **Operational practices** – Deployment strategy, backup tooling, runbooks, on-call coverage, or other practices that mitigate risk but leave no trace in resource configuration.
+ **Business constraints** – Requirements such as "data loss is unacceptable" or planned changes such as an upcoming migration.

Avoid the following when writing assertions:
+ **Restating resource configuration** – The assessment already knows that your database is Multi-AZ or that your Auto Scaling group has a minimum size of 2. Restating configuration adds noise without adding context.
+ **Writing vague or hedged statements** – "Traffic might be high sometimes" gives the assessment nothing to calibrate against. State the fact directly.
+ **Combining multiple facts** – Keep each assertion to a single topic so that you can edit or delete it independently.
+ **Asserting capabilities you do not have** – If you assert a capability, the assessment suppresses failure mode findings that contradict it, so only assert mitigations that actually exist.
+ **Including sensitive data** – Do not include credentials, secrets, or personal data in assertion text.

The following table shows examples of effective and less effective assertions.


| Effective | Less effective | Why | 
| --- | --- | --- | 
| "Steady-state traffic is about 500 requests per second, with predictable spikes to 5,000 requests per second during weekday business hours." | "Traffic can be high." | Specific numbers let the assessment evaluate capacity and scaling configuration. A vague statement gives it nothing to calibrate against. | 
| "This is a production service. Any downtime affects paying customers." | "The service is important." | Stating the environment and the impact of downtime tells the assessment how strictly to evaluate the service. | 
| "The Network Load Balancer routes all traffic to an NGINX ingress controller that runs as pods on the Amazon EKS managed node group." | "The load balancer sends traffic to the Amazon EKS cluster." | The ingress controller is software the assessment cannot see. The load balancer to cluster connection is already visible in the topology. | 
| "Database backups are managed by a third-party backup tool with a 15-minute recovery point objective." | "Backups are handled." | Naming the mechanism and its recovery point objective lets the assessment evaluate it against your policy. "Handled" is too vague to act on. | 
| "The service operates as active-passive across two Regions with a warm standby in us-west-2. Data is replicated asynchronously." | "The RDS instance has Multi-AZ enabled." | Disaster recovery intent is not visible in resource configuration. The Multi-AZ setting already is. | 