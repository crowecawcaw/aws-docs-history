# Performance efficiency

The performance efficiency pillar focuses on the efficient use of resources
to meet requirements, and to maintain and improve that efficiency as
demands change and technologies evolve.

Key topics include selecting the right infrastructure based on
workload requirements, monitoring performance, and making informed
decisions to maintain efficiency.

Performance optimization should be a continuous, data-driven process
of confirming business requirements, monitoring and measuring
workload performance, identifying under-performing components and
adjusting the infrastructure to meet evolving requirements. By
reviewing your choices on a cyclical basis, you can take advantage of the continually evolving AWS Cloud.

## Design principles

In addition to the design principles in the AWS Well-Architected Framework whitepaper, the following design principles can help you achieve performance efficiency for your financial services workloads.

**Consider both internal and external requirements**

Regulators expect financial services institutions to define operational performance objectives for workloads, and implement policies that achieve those objectives. Regulators may also impose their own Key Performance Indicator (KPI) requirements on systemically-important workloads, such as Open Banking interfaces, or trading transaction reporting and expect institutions to monitor and report on their compliance with these requirements, with penalties for breaches.
The objectives must define both qualitative and quantitative measures of operational performance and thereby explicitly state the performance standards that the workload intends to meet.

**Architect for performance-driven workloads**

Some financial services workloads, for example high-frequency trading systems and risk
calculation engines, are particularly performance sensitive, with factors such as speed of
completion and latency of response directly impacting the profitability of the system. Systems
with considerations like these need to prioritize performance over other factors such as
cost-efficiency or reliability, considering the trade-offs required to achieve their
performance goals while also preserving non-functional requirements such as transactional
consistency and recoverability. See the [Trade-offs](perf-trade-offs.md "perf-trade-offs.md") section of this
pillar for more detail.

**Use managed services**
Leverage AWS cloud services to allow teams to use a wide range of technologies, to experiment with options and achieve their performance goals, while maintaining overall control. You can reduce the time it takes to configure, and invest in operations and on-going management, reducing operational overhead and using the right tool for the job.

## Definitions

Focus on the following areas to achieve performance efficiency in
the cloud:

- [Selection](../framework/a-selection.md "../framework/a-selection.md")
- [Review](../framework/a-review.md "../framework/a-review.md")
- [Monitoring](../framework/a-monitoring.md "../framework/a-monitoring.md")
- [Trade-offs](../framework/a-tradeoffs.md "../framework/a-tradeoffs.md")

Gather data on all aspects of the architecture for a data-driven approach to building a high-performance architecture, from the high-level design to the selection and configuration of infrastructure services and components from compute to storage and networking.

Reviewing these architectural choices on a regular basis helps you take advantage of continually evolving AWS cloud capabilities and match your workload requirements with available services and features.

Monitoring the performance of your workload continuously makes you aware of deviances from expected performance, and able to take timely action. It is also important to plan for the future performance of the system by performing load tests of projected future loads, and running game days of exceptional circumstances in order to understand the behavior and limits of the system. Performance can degrade unexpectedly as workloads grow.

However, be aware of some constraints AWS places on testing of this type, as running load tests on Amazon Web Services can initiate security mechanisms. For more information, see the Amazon Elastic Compute Cloud [testing policy](https://aws.amazon.com/ec2/testing/ "https://aws.amazon.com/ec2/testing/"). In particular, [Penetration testing](https://aws.amazon.com/security/penetration-testing/ "https://aws.amazon.com/security/penetration-testing/") can be run only on permitted AWS services and [Distributed Denial of Service](https://aws.amazon.com/security/ddos-simulation-testing/ "https://aws.amazon.com/security/ddos-simulation-testing/") (DDoS) testing must be performed by a pre-approved AWS Partner.

Finally, make trade-offs in your architecture to improve performance, such as using compression to reduce the size of data stored and transiting your network, caching frequently used data in dedicated services or relaxing consistency requirements, prioritizing your most important requirements.
