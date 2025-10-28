# Reliability

The reliability pillar includes the ability of a workload to perform
its intended function correctly and consistently when it's expected
to. This includes the ability to operate and test the workload
through its total lifecycle. This paper provides in-depth, best
practice guidance for implementing reliable workloads on AWS. The
reliability pillar provides an overview of design principles, best
practices, and questions.

## Definitions

This whitepaper covers reliability in the cloud, describing best
practices in the following areas:

- Foundations
- Workload architecture
- Change management
- Failure management

To achieve reliability, you must start with the foundations: an
environment where service quotas and network topology accommodate
the workload. The workload architecture of the distributed system
must be designed to prevent and mitigate failures. The workload
must handle changes in demand or requirements, and it must be
designed to detect failure and automatically heal itself.

## Design principles

While meeting data residency requirements in AWS Regions, Local
Zones, and Outposts, there are a number of principles that can
help you increase reliability. Keep these in mind as we discuss
best practices:

- **Automatically recover from failure
  while maintaining data residency requirements:** By
  monitoring a workload for key performance indicators (KPIs),
  you can run automation when a threshold is breached. These
  KPIs should be a measure of business value, not of the
  technical aspects of the operation of the service. This allows
  for automatic notification and tracking of failures, as well
  as automated recovery processes that work around or repair the
  failure. The failure recovery must be designed to comply with
  your data residency requirements. With prediction and testing,
  it is possible to anticipate and remediate most of the
  failures before they occur.
- **Plan capacity requirements:**
  In an AWS Region, you can monitor demand and workload
  utilization and automate the addition or removal of resources
  to maintain the optimal level that satisfies demand without
  over- or under-provisioning. There are still limits, but some
  quotas can be controlled and others can be managed (for more
  detail, see
  [Manage
  service quotas and constraints](../reliability-pillar/manage-service-quotas-and-constraints.md "../reliability-pillar/manage-service-quotas-and-constraints.md")). With Outposts,
  capacity is finite and should be planned ahead of time using
  prediction and testing to forecast capacity correctly ahead of
  time.
