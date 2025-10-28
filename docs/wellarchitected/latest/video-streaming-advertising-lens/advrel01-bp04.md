# ADVREL01-BP04 Implement chaos engineering practices

Accept that "everything fails, all the time," (Dr. Werner Vogels,
Amazon CTO), and safely disrupt things on your terms to discover
faults and fragility so that you can later improve services.

## Implementation guidance

Advertising systems have components that are sensitive to
disconnects, latency, and bandwidth changes. Use tools like
[AWS Fault
Injection Service (FIS)](https://aws.amazon.com/fis/ "https://aws.amazon.com/fis/") or open-source tools like
[Chaos
Monkey](https://netflix.github.io/chaosmonkey/ "https://netflix.github.io/chaosmonkey/") to inject failures into your workload which
simulate network disruptions or resource unavailability. Based
on the results, update responses to failure scenarios, how you
monitor, and what you alert on, then adapt runbooks and
playbooks before practicing failure response with relevant
teams.

## Key AWS services

- [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/ "https://aws.amazon.com/resilience-hub/")

## Resources

**Related documentation:**

- [AWS chaos engineering blogs](https://aws.amazon.com/blogs/architecture/tag/chaos-engineering/ "https://aws.amazon.com/blogs/architecture/tag/chaos-engineering/")
- [Continuous
  integration and continuous delivery](../../../prescriptive-guidance/latest/aws-caf-platform-perspective/ci-cd.md "../../../prescriptive-guidance/latest/aws-caf-platform-perspective/ci-cd.md")
- [Leverage
  AWS Resilience Lifecycle Framework to assess and improve the resilience of application using AWS Resilience Hub](https://aws.amazon.com/blogs/mt/leverage-aws-resilience-lifecycle-framework-to-assess-and-improve-the-resilience-of-application-using-aws-resilience-hub/index.html "https://aws.amazon.com/blogs/mt/leverage-aws-resilience-lifecycle-framework-to-assess-and-improve-the-resilience-of-application-using-aws-resilience-hub/index.html")
- [[QA.NT.6]
  Experiment with failure using resilience testing to build recovery preparedness](../devops-guidance/qa.nt.md "../devops-guidance/qa.nt.md")

**Related
videos:**

- [AWS re:Invent 2020 - Developer Keynote with Dr. Werner Vogels](https://www.youtube.com/watch?v=jt-gV1YwmnI "https://www.youtube.com/watch?v=jt-gV1YwmnI")
