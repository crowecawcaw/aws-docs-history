# Architecture selection

There are multiple technology and design choices to consider when setting up hybrid
networking connectivity on AWS. Each option has its own performance characteristics and
considerations. Understand your performance requirements to make the right choice.

| HNPERF01: How would you select technology for best performing hybrid<br>networking architecture? |
| ------------------------------------------------------------------------------------------------ |
|                                                                                                  |

Carefully evaluate the application requirements, including bandwidth demands, latency
sensitivity, and jitter tolerance. This evaluation should also encompass the geographical
distribution of resources and users, scalability needs for future growth, security and
compliance requirements, and the cost-effectiveness of different solutions like IPSec VPN or
dedicated connectivity. By considering these elements, organizations can make informed
decisions that align with specific needs and ensure a robust, efficient hybrid network
infrastructure.

| HNPERF02: What choice of technology are available for best performing<br>hybrid networking architecture? |
| -------------------------------------------------------------------------------------------------------- |
|                                                                                                          |

When selecting technology for high-performance hybrid networking architectures,
organizations carefully evaluate their connectivity options based on specific workload
requirements. Dedicated network connections offer consistent latency and higher bandwidth
capabilities compared to virtual private networks operating over the internet. For
mission-critical workloads requiring predictable performance, redundant dedicated connections
are often the optimal choice, despite higher costs. Organizations should consider factors such
as geographic distribution, bandwidth requirements, latency sensitivity, and budget
constraints when selecting connectivity solutions. The chosen technology should balance
performance needs with operational costs while ensuring reliability and scalability across
multiple Regions.

###### Best practices

- [HNPERF01-BP01 Determine and define your performance
  requirements using bandwidth, latency and jitter values.](hnperf01-bp01..md "hnperf01-bp01..md")
- [HNPERF01-BP02 Identify what applications and types of data will
  be transmitted over the network](hnperf01-bp02.md "hnperf01-bp02.md")
- [HNPERF02-BP01 Use tradeoffs to improve network
  performance](hnperf02-bp01.md "hnperf02-bp01.md")
- [HNPERF02-BP02 Choose the right physical PoP location for
  dedicated connectivity](hnperf02-bp02.md "hnperf02-bp02.md")
- [HNPERF02-BP03 Choose the right termination endpoint in the
  cloud](hnperf02-bp03.md "hnperf02-bp03.md")
- [HNPERF02-BP04 Select the most appropriate region for your
  workloads](hnperf02-bp04.md "hnperf02-bp04.md")
- [HNPERF02-BP05 Plan for bandwidth scaling](hnperf02-bp05.md "hnperf02-bp05.md")
