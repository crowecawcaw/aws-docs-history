# Design principles

In addition to the overall Well-Architected Framework design
principles, there are three design principles for reliability for
IoT:

- **Simulate device behavior at production
  scale**: Create a production-scale test environment
  that closely mirrors your production deployment. Leverage a
  multi-step simulation plan that allows you to test your
  applications with a more significant load before your go-live
  date. During development, ramp up your simulation tests over a
  period of time starting with 10% of overall traffic for a
  single test and incrementing over time (that is, 25%, 50%,
  then 100% of day one device traffic). During simulation tests,
  monitor performance and review logs to make sure that the
  entire solution behaves as expected.
- **Buffer message delivery from the IoT
  rules engine with streams or queues**:
  Leverage-managed services enable high throughput telemetry. By
  injecting a queuing layer behind high throughput topics, IoT
  applications can manage failures, aggregate messaging, and
  scale other downstream services.
- **Design for resiliency**: It
  is essential to plan for resiliency on the device itself.
  Depending on your use case, resiliency may entail robust retry
  logic for intermittent connectivity, ability to roll back
  firmware updates, ability to fail over to a different
  networking protocol or communicate locally for critical
  message delivery, running redundant sensors or edge gateways
  to be resilient to hardware failures, and the ability to
  perform a factory reset.
