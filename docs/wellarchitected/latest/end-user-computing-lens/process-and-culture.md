# Process and culture

When architecting an AWS EUC solution, there are principles and practices that you can
adopt to help you better run an efficient, high-performing environment. This focus area offers
best practices to help adopt a culture that delivers and maintains a level of performance that
both meet and exceed the requirements of the business.

| EUCPERF07: How do you test performance of your EUC environment? |
| --------------------------------------------------------------- |
|                                                                 |

Validate your workload performance against real-life testing conditions based on your end
users' use cases, performance metrics, and constraints within their workloads.

| EUCPERF08: How do you monitor performance and availability in your EUC<br>environment? |
| -------------------------------------------------------------------------------------- |
|                                                                                        |

Unless you can accurately measure your resource performance against your key
performance indicators and functional requirements, you cannot be certain that the
workload will meet your objectives consistently. Establish a set of baseline requirements.
Once established, routinely measure performance to understand how your workload's
performance may vary against external demands.

| EUCPERF09: How do you evolve your workload to benefit from new feature<br>releases? |
| ----------------------------------------------------------------------------------- |
|                                                                                     |

New releases are inevitable, and updates can change the performance characteristics
of a system. Understand what changes are being made, and develop strategies for taking
advantage of performance increases and resource consumption due to those changes.

| EUCPERF10: How do you manage ongoing and on-demand sizing changes in your<br>EUC environment? |
| --------------------------------------------------------------------------------------------- |
|                                                                                               |

Consider the growth of performance needs over time. Also consider cyclical events
such as end-of-month or end-of-quarter reporting, annual updates, and holiday demands.

###### Best practices

- [EUCPERF07-BP01 Conduct realistic end-to-end testing aligned with organizational
  objectives](eucperf07-bp01.md "eucperf07-bp01.md")
- [EUCPERF08-BP01 Establish and monitor service metrics and KPIs](eucperf08-bp01.md "eucperf08-bp01.md")
- [EUCPERF08-BP02 Monitor Amazon WorkSpaces Applications CloudWatch metrics](eucperf08-bp02.md "eucperf08-bp02.md")
- [EUCPERF08-BP03 Monitor Amazon WorkSpaces Personal CloudWatch metrics](eucperf08-bp03.md "eucperf08-bp03.md")
- [EUCPERF08-BP04 Monitor
  operating system metrics](eucperf08-bp04.md "eucperf08-bp04.md")
- [EUCPERF09-BP01 Follow AWS EUC
  news sources](eucperf09-bp01.md "eucperf09-bp01.md")
- [EUCPERF10-BP01 Align the instance type and instance size of a fleet with the
  workload](eucperf10-bp01.md "eucperf10-bp01.md")
- [EUCPERF10-BP02 Enable self-service WorkSpaces Personal management capabilities,
  and allow users to request changes by an administrator](eucperf10-bp02.md "eucperf10-bp02.md")
- [EUCPERF10-BP03 Install only the application features required by end users](eucperf10-bp03.md "eucperf10-bp03.md")
- [EUCPERF10-BP04 Remove caches, temporary data, log files, and unneeded files such as
  tutorials and sample data before creating an image](eucperf10-bp04.md "eucperf10-bp04.md")
- [EUCPERF10-BP05 Tune application performance where possible to optimize compute resource
  usage](eucperf10-bp05.md "eucperf10-bp05.md")
