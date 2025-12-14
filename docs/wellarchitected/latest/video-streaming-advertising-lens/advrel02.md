# Latency sensitive advertising

| ADVREL02: How do your latency sensitive advertising workloads react to including throttling and rate-limiting scenarios? |
| ------------------------------------------------------------------------------------------------------------------------ |
|                                                                                                                          |

Consider strategies for managing latency-sensitive advertising
workloads through throttling and rate-limiting implementations.
Avoid traditional retry mechanisms for fast-failing services,
implement effective caching strategies, and proportionally scale
across all system components to maintain consistent performance.

###### Best practices

- [ADVREL02-BP01 To allow fast and graceful failure of latency-sensitive services, avoid exponential backing off and retry](advrel02-bp01.md "advrel02-bp01.md")
- [ADVREL02-BP02 Implement a caching strategy](advrel02-bp02.md "advrel02-bp02.md")
- [ADVREL02-BP03 Prevent scale mismatch of both internal services and external partners](advrel02-bp03.md "advrel02-bp03.md")
