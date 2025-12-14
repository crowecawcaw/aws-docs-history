# GAMEOPS03-BP02 Conduct performance engineering before every

release (or at least for major releases)

Performance engineering is the process of monitoring multiple key
operational metrics of an app to discover optimization
opportunities that can further improve the application's
performance. This is an iterative process that starts with
testing, followed by optimizing code, its dependencies, associated
processes, its host operating system, and the underlying
infrastructure.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

To conduct a deeper analysis of the app's performance, integrate
an application performance monitoring (APM) or debugging tool in
the app code that can isolate issues and reduce troubleshooting
time by tracking its behavior for anomalies across the flows of
the app. APM tools are also able to identify slow performing
methods and external operations.

[AWS X-Ray](https://aws.amazon.com/xray/ "https://aws.amazon.com/xray/") assists developers with their performance engineering
activities, like identifying performance bottlenecks and analyzing
and debugging production errors. You can use X-Ray to understand
how your application and its underlying services are performing
and identify and troubleshoot the root cause of performance issues
and errors. Through numerous rounds of load tests, in which the
application and its infrastructure is gradually loaded with
synthetic player traffic, various system bottlenecks, app errors,
exceptions, OS problems, and other issues are identified that may
have not been found during other QA tests.

For critical events like game launches, content releases,
promotions, and major in-game events, use
[AWS Countdown](https://aws.amazon.com/premiumsupport/aws-countdown-sports/ "https://aws.amazon.com/premiumsupport/aws-countdown-sports/"), which provides implementation guidance based on
playbooks built by games experts to verify operational readiness,
mitigate potential risks, and plan for capacity needs. AWS Countdown also has a
[premium
support](https://aws.amazon.com/premiumsupport/aws-countdown/ "https://aws.amazon.com/premiumsupport/aws-countdown/") option that offers enhanced support and options
like engineers to optimize your infrastructure.

### Implementation steps

- Performance engineering involves evaluating and monitoring
  key operational metrics to verify that your application's
  code, processes, operating system, and infrastructure are
  functioning as expected. Pre-production review also assists
  to define baseline performance at different levels of
  simulated usage.
- Discover and track key metrics like utilization, services,
  I/O, processes and such by using system tools such as sar,
  top, vmstat, sysstat, netstat, and Performance Monitor.
- Track your application's performance and behavior using APM
  tools like AWS X-Ray to isolate issues, identify
  bottlenecks, and debug production errors.
- For critical events like game launches, subscribe to AWS
  Countdown (IEM) for architectural and operational guidance,
  on-demand operational support, and to identify risks and
  plan mitigations.
