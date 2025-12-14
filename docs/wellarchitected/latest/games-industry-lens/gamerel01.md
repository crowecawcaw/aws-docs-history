# Workload architecture

| GAMEREL01: Is your game architecture taking advantage of<br>the cloud's resiliency? |
| ----------------------------------------------------------------------------------- |
|                                                                                     |

AWS infrastructure is built around Regions and Availability Zones.
AWS Regions provide multiple physically separated and isolated
Availability Zones, which are connected using low-latency,
high-throughput, and highly redundant networking. These constructs
can be used to architect workloads with reliability goals in
focus.

###### Best practices

- [GAMEREL01-BP01 Distribute game infrastructure across multiple
  Availability Zones and Regions to improve resiliency](gamerel01-bp01.md "gamerel01-bp01.md")
