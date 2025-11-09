# Networking and content delivery

The optimal networking solution for a workload varies based on latency, throughput
requirements, jitter, and bandwidth. Physical constraints, such as the location of users and
data sources, will affect the performance of the solution.

| EUCPERF06: How do you configure network connectivity in your EUC environment for<br>best performance? |
| ----------------------------------------------------------------------------------------------------- |
|                                                                                                       |

In an EUC architecture, there are two key networking configurations to consider:

- Connections from end users to their most proximal AWS EUC service connection point
- Connections from the EUC instances to any backend infrastructure and other services

###### Best practices

- [EUCPERF06-BP01 Minimize latency between end users and EUC services](eucperf06-bp01.md "eucperf06-bp01.md")
- [EUCPERF06-BP02 Minimize latency between EUC instances and dependent services](eucperf06-bp02.md "eucperf06-bp02.md")
- [EUCPERF06-BP03 Make sure that EUC network configurations don't interfere with service
  management connections](eucperf06-bp03.md "eucperf06-bp03.md")
