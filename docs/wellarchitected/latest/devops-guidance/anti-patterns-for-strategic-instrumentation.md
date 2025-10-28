# Anti-patterns for strategic instrumentation

- **Excessive data
  collection**: Over-instrumentation leads to
  unnecessary data collection, escalating costs, and storage
  requirements. Prioritize collecting relevant data that
  provides valuable insights into the customer experience
  while interacting with systems and your organization's
  desired business outcomes. For use cases needing verbose
  datasets, implement aggressive data retention policies.
  This approach balances the need for detailed, short-term
  data for efficient troubleshooting without excessive
  costs.
- **Lack of
  standardization:** Inconsistency in Service Level
  Agreements (SLAs), Service Level Objectives (SLOs), and
  Key Performance Indicators (KPIs), and metric formats
  impedes understanding and interpretation of metrics.
  DevOps principles emphasize communication, collaboration,
  and visibility, which inconsistent standards undermine.
  Establish standardized guidelines for defining and
  formatting these metrics, and use a centralized
  observability platform for tracking and enforcing these
  standards, promoting continuous improvement.
- **Monitoring in
  isolation:** Observing individual components in
  isolation decreases visibility into system interactions
  and dependencies, hindering root cause identification,
  adds delay to detection time, and can generate inaccurate
  alerts. Adopt a holistic observability approach through a
  centralized platform, taking into account the entire
  system and its interdependencies.
- **Reactive monitoring:**
  Reactive monitoring, triggered by incidents or issues, can
  increase downtime and incur additional cost over time.
  Embrace a proactive, continuous monitoring stance that
  tracks system performance and user behaviors. Implement
  thresholds, alerts, predictive analytics, and constant
  data collection across all system components to detect and
  address issues before affecting the end user.
- **Misaligned
  SLOs:**Service Level Objectives (SLOs) defined
  solely by business teams without the input from technical
  teams can result in unachievable targets, leading to
  frequent breaches of Service Level Agreements and missed
  KPIs. Defining SLOs should be a collaborative process
  involving both business and technical teams to align
  technical realities with business objectives and customer
  expectations.
