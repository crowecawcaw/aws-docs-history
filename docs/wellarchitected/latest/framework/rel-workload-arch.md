# Workload architecture

A reliable workload starts with upfront design decisions for both
software and infrastructure. Your architecture choices will
impact your workload behavior across all of the Well-Architected
pillars. For reliability, there are specific patterns you must
follow.

With AWS, workload developers have their choice of languages and
technologies to use. AWS SDKs take the complexity out of coding by
providing language-specific APIs for AWS services. These SDKs,
plus the choice of languages, permits developers to implement the
reliability best practices listed here. Developers can also read
about and learn from how Amazon builds and operates software in
[The
Amazon Builders' Library](https://aws.amazon.com/builders-library/?ref=wellarchitected-wp "https://aws.amazon.com/builders-library/?ref=wellarchitected-wp").

The following questions focus on these considerations for
reliability.

| REL 3:  How do you design your workload service architecture?                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Build highly scalable and reliable workloads using a service-oriented architecture (SOA) or a microservices architecture. Service-oriented architecture (SOA) is the practice of making software components reusable via service interfaces. Microservices architecture goes further to make components smaller and simpler.                                                                                                                                                                                                                |
| REL 4:  How do you design interactions in a distributed system to prevent failures?                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Distributed systems rely on communications networks to interconnect components, such as servers or services. Your workload must operate reliably despite data loss or latency in these networks. Components of the distributed system must operate in a way that does not negatively impact other components or the workload. These best practices prevent failures and improve mean time between failures (MTBF).                                                                                                                          |
| REL 5:  How do you design interactions in a distributed system to mitigate or withstand failures?                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Distributed systems rely on communications networks to interconnect components (such as servers or services). Your workload must operate reliably despite data loss or latency over these networks. Components of the distributed system must operate in a way that does not negatively impact other components or the workload. These best practices permit workloads to withstand stresses or failures, more quickly recover from them, and mitigate the impact of such impairments. The result is improved mean time to recovery (MTTR). |
