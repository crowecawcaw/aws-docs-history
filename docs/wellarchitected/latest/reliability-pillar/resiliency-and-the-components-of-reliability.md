# Resiliency, and the

components of reliability

Reliability of a workload in the cloud depends on several factors, the primary of which
is _Resiliency_:

- **Resiliency** is the ability of a workload to recover from
  infrastructure or service disruptions, dynamically acquire computing resources to meet
  demand, and mitigate disruptions, such as misconfigurations or transient network issues.
  The other factors impacting workload reliability are:

- Operational Excellence, which includes automation of changes, use of playbooks to
  respond to failures, and Operational Readiness Reviews (ORRs) to confirm that
  applications are ready for production operations.
- Security, which includes preventing harm to data or infrastructure from malicious
  actors, which would impact availability. For example, encrypt backups to ensure that
  data is secure.
- Performance Efficiency, which includes designing for maximum request rates and
  minimizing latencies for your workload.
- Cost Optimization, which includes trade-offs such as whether to spend more on EC2
  instances to achieve static stability, or to rely on automatic scaling when more
  capacity is needed.
  Resiliency is the primary focus of this whitepaper.

The other four aspects are also important and they are covered by their respective
pillars of the [AWS
Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/ "https://aws.amazon.com/architecture/well-architected/"). Many of the best practices here also address those
aspects of reliability, but the focus is on resiliency.
