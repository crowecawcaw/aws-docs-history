# Workload architecture

| AOSREL02: How do you provide high<br>availability for your OpenSearch Service domain? |
| ------------------------------------------------------------------------------------- |
|                                                                                       |

To protect your OpenSearch Service domain during a service
disruption, you can deploy nodes across two or three Availability
Zones within the same Region. This configuration, known as Multi-AZ,
leverages isolated locations called Availability Zones within each
AWS Region. You can also choose to deploy OpenSearch with Multi-AZ
with Standby deployment to protect against infrastructure failures.
Enabling Multi-AZ with Standby deployment increases the availability
of your domain to 99.99%.

| AOSREL03: How do you monitor quotas and<br>limits in your OpenSearch Service domain? |
| ------------------------------------------------------------------------------------ |
|                                                                                      |

Cloud providers have built-in usage constraints that prevent
excessive resource utilization. Understanding and monitoring these
quotas is essential to prevent scaling issues and ensure
uninterrupted service operations.

| AOSREL04: How do you recover your OpenSearch Service<br>domains from outages? |
| ----------------------------------------------------------------------------- |
|                                                                               |

Disaster recovery involves plans and processes to resume operations
and restore data in the aftermath of a disruptive event or
catastrophe. Having a disaster recovery plan is important to recover
from any disruptions to the OpenSearch domain.

| AOSREL05: How do you use reliable instances<br>for your production search workloads? |
| ------------------------------------------------------------------------------------ |
|                                                                                      |

Business-critical workloads demand enough resources in production
environments to handle reliability, stability, and high performance.
In contrast, dev environments can function on minimal resources
without impacting critical operations.

###### Best practices

- [AOSREL02-BP01 Create Multi-AZ with Standby OpenSearch Service domains](aosrel02-bp01.md "aosrel02-bp01.md")
- [AOSREL03-BP01 Regularly review your OpenSearch Service
  quotas](aosrel03-bp01.md "aosrel03-bp01.md")
- [AOSREL04-BP01 Implement a disaster recovery (DR) strategy for
  your OpenSearch Service for business continuity](aosrel04-bp01.md "aosrel04-bp01.md")
- [AOSREL04-BP02 Implement an Index State Management (ISM) policy
  to generate snapshots for your crucial indices](aosrel04-bp02.md "aosrel04-bp02.md")
- [AOSREL04-BP03 Enable index replication for your critical
  indices](aosrel04-bp03.md "aosrel04-bp03.md")
- [AOSREL04-BP04 Employ cross-cluster replication to achieve
  higher availability](aosrel04-bp04.md "aosrel04-bp04.md")
- [AOSREL05-BP01 Implement appropriate compute sizing for
  production workloads](aosrel05-bp01.md "aosrel05-bp01.md")
