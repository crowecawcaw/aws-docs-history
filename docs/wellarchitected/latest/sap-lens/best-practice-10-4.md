# Best Practice 10.4 – Validate the

design against a set of criteria based on your business requirements

Establish a set of criteria based on your business requirements, balancing the risk of
failure, impact on the business, and acceptable trade-offs. Use these criteria to validate
the design and make adjustments where necessary.

**Suggestion 10.4.1 – Assess the cost to your business of an
outage**

Failures, of either AWS services or SAP components, will impact your SAP system
differently depending on the resilience and recovery strategies. The type of failure will
determine the duration of the outage (RTO) and the potential data loss (RPO).

For each failure, assess the risk of an outage and the cost to your business. For
example, are there revenue generating processes that will be impacted and what is the
hourly cost associated with the system not being available?

**Suggestion 10.4.2 – Assess the cost of your architecture**

In SAP Landscapes, the largest elements of the AWS monthly bill typically are for
Amazon EC2 and storage-related services. Understand the cost implications so that you
select the best architecture to meet your reliability requirements. Key contributors
include:

- Deployment patterns that don’t maximize hardware utilization
- Redundant copies of data
- Operating system license costs
- Clustering software license costs
- Costs associated with maintenance, testing, and skilled resources
  Refer to [Cost Optimization]: [Cost optimization
  Best Practices](cost-optimization.md "cost-optimization.md") for further details.

**Suggestion 10.4.3 – Evaluate your design against other pillars in
the framework**

Reliability cannot be designed in isolation, but should be assessed against the rest
of the pillars of the AWS Well-Architected Framework. Example questions you might ask to
evaluate this include:

- Operational excellence — Do you have the experience and skills to manage the
  solution?
- Security — Is your data protected during replication, recovery, etc.
- Performance — Does replication or the backup activity impact user
  performance?
- Cost optimization — Does the cost of the solution align with the assumed
  risk?
- Sustainability — Does the solution align with your sustainability and environmental
  impact initiatives?
