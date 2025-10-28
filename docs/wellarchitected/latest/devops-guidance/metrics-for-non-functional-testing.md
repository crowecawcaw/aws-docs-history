# Metrics for non-functional testing

- **Availability**: The
  percentage of time a system is operational and accessible
  to users. High availability helps to maintain user trust
  and ensure business continuity. A decrease in this metric
  can signify issues with infrastructure reliability or
  application stability. Enhance availability by
  implementing redundant architecture, employing failover
  strategies, and ensuring continuous monitoring. Calculate
  the availability percentage by dividing the total time the
  system was operational by the overall time period being
  examined, and then multiply the result by 100.
- **Latency**: The time it
  takes for a system to process a given task. This metric
  specifically considers the time taken from when a request
  is made to when a response is received. This metric offers
  insight into the responsiveness of an application,
  affecting user experience and system efficiency. Improve
  this metric by optimizing application code, streamline
  database operations, utilize efficient algorithms, and
  scaling infrastructure.
  Using [percentiles](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Percentiles "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Percentiles")
  and
  [trimmed
  mean](../../../AmazonCloudWatch/latest/monitoring/Statistics-definitions.md#Percentile-versus-Trimmed-Mean "../../../AmazonCloudWatch/latest/monitoring/Statistics-definitions.md#Percentile-versus-Trimmed-Mean") are good statistics for this measurement.
- **Cyclomatic
  complexity**: [Cyclomatic
  complexity](https://en.wikipedia.org/wiki/Cyclomatic_complexity "https://en.wikipedia.org/wiki/Cyclomatic_complexity") counts the distinct paths through a code
  segment. It reflects the complexity in the code's
  decision-making structure. Higher values can indicate code
  that can be harder to maintain, understand, or test,
  increasing the likelihood of errors. Improve this metric
  by simplifying code where possible by performing regular
  code reviews and refactoring sessions. In these sessions,
  break down complex code into smaller, more manageable
  functions and reduce nested conditions and loops. The
  complexity is calculated using the difference between the
  number of transitions between sections of code (edges) and
  the number of sequential command groups (nodes), adjusted
  by twice the number of connected components. We recommend
  adopting tools to measure complexity automatically.
- **Peak load threshold**: Represents the maximum number of
  simultaneous users or requests a system can handle before performance degrades.
  Understanding this threshold aids in capacity planning and ensures the system can cope
  with usage spikes. Increase the peak load threshold by conducting load tests with
  increasing numbers of users, identifying and resolving bottlenecks. Track this metric by
  stress testing the system and observing the point of performance degradation.
- **Test case run
  time**: The duration taken to run a test case
  or a suite of test cases. Increasing duration may
  highlight bottlenecks in the test process or performance
  issues emerging in the software under test. Improve this
  metric by optimizing test scripts and the order they run
  in, enhancing testing infrastructure, and running tests in
  parallel. Measure the timestamp difference between the
  start and end of test case execution.
- **Infrastructure utilization**: Percentage utilization of
  infrastructure resources such as CPU, memory, storage, and bandwidth. Infrastructure
  utilization helps in understanding if there are over-provisioned resources leading to
  cost overhead or under provisioned resources that could affect performance. Calculate
  this metric for each type of resource (such as CPU, RAM, or storage) to get a
  comprehensive understanding of infrastructure utilization.
- **Time to restore service**: The time taken to restore a
  service to its operational state after an incident or failure. Faster time to restore
  can indicate a more resilient system and optimized incident response processes. An ideal
  time to restore service must be capable of meeting recovery time objectives (RTO). RTO
  is the duration the system must be restored after a failure to avoid unacceptable
  interruptions to business continuity. RTO takes into account the criticality of each
  system, while balancing cost, risk, and operational needs. Measure the time duration
  from the moment the service disruption is reported to when the service is fully
  restored.
- **Application performance index ([Apdex](https://en.wikipedia.org/wiki/Apdex "https://en.wikipedia.org/wiki/Apdex"))**: Measures user
  satisfaction with application responsiveness using a scale from 0 to 1. A higher Apdex
  score indicates better application performance, likely resulting in improved user
  experience, while a lower score means that users might become frustrated.

To determine the Apdex score, start by defining a target response time that
represents an acceptable user experience for your application. Then, categorize every
transaction in one of three ways:

    + **Satisfied**, if its response time is up to and
     including the target time.
    + **Tolerating**, if its response time is more than
     the target time but no more than four times the target time.
    + **Frustrated**, for any response time beyond four
     times the target time.

Calculate the Apdex score by adding the number of _Satisfied_
transactions with half the _Tolerating_ transactions. Then, divide
this sum by the total number of transactions. Continuously monitor and adjust your
target time based on evolving user expectations and leverage the score to identify and
rectify areas that contribute to user dissatisfaction.
