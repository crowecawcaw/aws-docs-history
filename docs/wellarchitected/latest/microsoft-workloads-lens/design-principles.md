# Design principles

The Well-Architected Framework identifies a set of general design principles to facilitate
good design in the cloud. In addition, the following design principles should also be considered
for designing and operating Microsoft workloads:

- **Assess your Microsoft environment holistically:** Before
  designing or migrating, assess your current Microsoft workloads with tools like AWS
  Optimization and Licensing Assessment (OLA), Migration Evaluator, and Application Discovery
  Service. This foundational step helps define the business case, understand resource
  utilization, licensing, and technical dependencies.
- **Define clear business and technical goals:** Clarify the
  expected outcomes of moving or running Microsoft workloads on AWS. Whether you're aiming
  to reduce licensing costs, improve availability, increase agility, or enhance security,
  these goals should shape your architecture choices, migration strategy, and operational
  model.
- **Use AWS services and managed offerings:** Reduce
  operational burden and complexity by using managed services tailored for Microsoft
  workloads—such as Amazon RDS for SQL Server, Amazon FSx for Windows File Server, AWS Managed Microsoft AD, and EC2 Image Builder. This
  improves performance, reliability, and maintainability.
- **Optimize licensing and cost models:** Right-size instances
  and storage, automate start and stop schedules, and consider BYOL strategies when
  applicable. Evaluate SQL Server edition needs and instance consolidation opportunities. Use
  services like AWS Compute Optimizer and Trusted Advisor to continuously refine your resource usage.
- **Prioritize security aligned with workload criticality:**
  Apply Microsoft and AWS-aligned security controls. Enforce the principle of least
  privilege, encrypt data at rest, in transit, and in use (for example, using Always
  Encrypted), and align with your organizational identity strategy. Use centralized logging
  and SIEM integrations to detect and respond to anomalies.
- **Design for availability and resilience:** Define
  business-driven availability targets and choose architecture patterns that meet those
  needs—such as multi-AZ deployments, SQL Server Always On, or Amazon FSx Multi-AZ. Regularly
  test for failover and disaster recovery capabilities.
- **Enable operational excellence through automation and
  observability:** Automate infrastructure and patch management with AWS Systems Manager,
  and use infrastructure as code with AWS CloudFormation or Terraform. Implement robust observability
  using Amazon CloudWatch, Performance Counters, Application Insights, and AWS X-Ray for deep
  visibility into system health.
- **Embrace modernization incrementally:** Where feasible,
  modernize traditional workloads using containers (with ECS, EKS) or serverless solutions
  (like .NET on AWS Lambda). This unlocks agility, scalability, and cost optimization, while
  maintaining alignment with existing Microsoft technologies.
- **Govern through consistency and compliance:** Use
  AWS Control Tower, AWS Organizations, and tagging strategies to enforce adherence, manage accounts, and
  apply consistent policies across environments. Integrate security baselines and operational
  controls from day one.
- **Plan for lifecycle, sustainability, and continuous
  improvement:** Continuously monitor workload performance and cost. Reassess
  choices as AWS services evolve, license agreements change, or application usage shifts.
  Define update strategies for OS, SQL Server, and application components for sustainability.
