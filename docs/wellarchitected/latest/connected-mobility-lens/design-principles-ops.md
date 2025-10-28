# Design principles

The following are design principles for operational excellence
in the cloud:

- Based on the workload and your business objectives, identify connected mobility key
  performance indicators (KPIs). The connected mobility KPIs should be linked to metrics
  from all layers: business, application, data, security, and infrastructure. Once
  identified, use the connected mobility KPIs to work backwards and identify operational
  KPIs.
- Implement end-to-end observability and a single pane view of the connected mobility
  workload status from vehicle to the cloud and full stack of the application: Proactively
  monitor end user experience in-vehicle.
- Develop a testing framework to simulate production-like conditions: Site
  Reliability Engineering (SRE) team are responsible for reliability of the application
  amidst frequent updates from development teams. The SRE team works closely with the
  development team to create new features and stabilize production systems. One of the
  challenges faced by the SRE team is to simulate the vehicle while trying to test or debug
  a connected mobility feature or a production issue. Develop a virtual vehicle in the cloud
  that has capability to simulate various real-world conditions including load and Mobile
  Network Operator (MNO) failures.
- Implement mechanisms to improve developer productivity enabling reduction in Time
  to Market (TTM), which is the time it takes to take connected mobility features from
  concept to launching it in the industry. Develop deployment templates and provide a
  developer portal to quickly spin up new development and lab environments.
- Implement a multi-stakeholder runbook to effectively respond to production events.
  Connected mobility is a complex system with multiple stakeholders from end users to Mobile
  Network Operators, cloud hyperscalers, downstream data consumers, and OEMs. To reduce the
  Mean Time to Restore (MTTR), a runbook should be developed for all critical events.
  Eventually, automate runbooks to streamline operational processes, reduce human error, and
  improve efficiency, leading to faster incident resolution and enhanced operational
  excellence.

## Definitions

**Observability:** Observability allows users to understand a
system's state from its external output and take (corrective) action. Observable systems
yield meaningful, actionable data to their operators, allowing them to achieve favorable
outcomes (faster incident response, increased developer productivity) and less toil and
downtime.

Best practices implementing observability include:

- **Monitor what matters:** Start with the connected
  mobility business key performance indicators (KPIs) and work backwards to the application
  and infrastructure metrics.
- **Collect telemetry from all layers:** Connected mobility
  has dependencies and interactions with vehicles, Mobile Network Operators, cloud
  providers, internet service providers, AWS Partners, and other components—both within
  and outside your control—that can impact your business outcomes. It is important that you
  have a holistic view of your entire workload.
- **Propagate context:** Collect logs, metrics, and traces,
  and propagate transaction IDs, which helps to perform correlation, analysis, anomaly
  detection, dashboarding, and alarms.

**Leading versus lagging indicators:** Leading indicators are
metrics that are used to measure future performance. For example, customer satisfaction and
connected mobility feature usage metrics can be used to predict renewal rates, as a happy and
engaged customer is more likely to renew the paid subscription. Similarly, quality metrics of
the feature releases can be a leading indicator to predict the failure rate of the
system.

Lagging indicators are metrics used to measure past performance for example connected
mobility subscription renewal rates, Mean Time Between Failures (MTBF), and remote command
latency. Lagging indicators provide valuable feedback on the effectiveness of past decisions
and help identify areas for improvement. Both leading and lagging indicators are important for
managing and measuring operational efficiency of connected mobility workloads.
