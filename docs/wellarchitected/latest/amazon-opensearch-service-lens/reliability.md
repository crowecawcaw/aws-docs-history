# Reliability

The reliability pillar focuses on verifying that your Amazon OpenSearch Service workload performs correctly and consistently when needed.
This includes operating and testing the workload throughout its
entire lifecycle. This paper provides best practices for building
and maintaining reliable OpenSearch Service workloads.

###### Focus areas

- [Design principles](#design-principles-rel "#design-principles-rel")
- [Foundations](foundations.md "foundations.md")
- [Workload architecture](workload-architecture.md "workload-architecture.md")
- [Key AWS services](key-aws-services-rel.md "key-aws-services-rel.md")
- [Resources](resources-rel.md "resources-rel.md")

## Design principles

- **Implement monitoring and
  notifications:** Set up monitoring and notifications
  for OpenSearch domain failures to ensure timely detection and
  response to potential issues.
- **Provide continuous
  availability:** Implement multi-AZ with standby
  deployment, Index State Management (ISM) policy, index
  replication, cross-cluster replication, and regular quota
  monitoring to ensure OpenSearch Service domain availability.
- **Implement a disaster recovery
  strategy:** Develop a Disaster Recovery (DR) strategy
  for OpenSearch Service, including regular updates to the
  latest version, and monitoring of software updates.
- **Stay informed about
  updates:** Stay informed about OpenSearch Service
  update notifications, keep domains updated to the latest
  version, and monitor software updates for reliability and
  security.
