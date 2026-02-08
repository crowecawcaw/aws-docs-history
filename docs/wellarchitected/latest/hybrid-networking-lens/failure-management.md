# Failure management

Effective failure management for hybrid networking requires implementing robust
strategies to maintain connectivity between on-premises infrastructure and AWS environments
during disruptions.

| HNREL04: How does your system withstand component failures? |
| ----------------------------------------------------------- |
|                                                             |

In a reasonably complex system, failures are expected. Learn how to detect and respond to
these failures automatically, ensuring that your network can withstand the failures without
impact to existing workload.

| HNREL05: How are you testing for resiliency of hybrid network<br>connectivity? |
| ------------------------------------------------------------------------------ |
|                                                                                |

Test dedicated connection failover scenarios to identify hidden bugs before they appear
in production. Regularly conducting these tests ensures your configurations are suitable for
failovers and verifies how the workload is affected during these failovers. These tests
validate your recovery procedures.

| HNREL06: How are you planning for disaster recovery? |
| ---------------------------------------------------- |
|                                                      |

Hybrid network disaster recovery planning integrates comprehensive strategies across
on-premises infrastructure and cloud environments. Implementing geographic redundancy by
distributing critical workloads across different geographic cloud and on-premises environments
to ensure business continuity during localized failures. Included automated failover
mechanisms that can detect issues and seamlessly redirect traffic to healthy infrastructure
components, whether they reside in data centers or cloud environments. Established consistent
backup protocols and recovery point objectives across our hybrid landscape, with regular
testing of restoration processes to validate our ability to maintain operations during various
disaster scenarios.

###### Best practices

- [HNREL04-BP01 Use physical location redundancy to host dedicated
  connections](hnrel04-bp01.md "hnrel04-bp01.md")
- [HNREL04-BP02 Use redundant hardware and telecommunication
  providers](hnrel04-bp02.md "hnrel04-bp02.md")
- [HNREL04-BP03 Use dynamic routing for automatic failover](hnrel04-bp03.md "hnrel04-bp03.md")
- [HNREL04-BP04 Provision sufficient network capacity](hnrel04-bp04.md "hnrel04-bp04.md")
- [HNREL05-BP01 Failover testing of dedicated connections](hnrel05-bp01.md "hnrel05-bp01.md")
- [HNREL06-BP01 Use multiple data centers for physical location
  redundancy](hnrel06-bp01.md "hnrel06-bp01.md")
- [HNREL06-BP02 Ensure service continuity with redundant hardware
  and diverse telecommunications providers](hnrel06-bp02.md "hnrel06-bp02.md")
