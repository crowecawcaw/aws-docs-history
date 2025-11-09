# Expenditure and usage awareness

To effectively manage costs and drive efficiency, it's essential to
understand your organization's expenses, identify cost drivers, and
attribute resource costs to specific workloads, teams, or product
owners. This understanding informs your decisions about resource
allocation and encourages efficient usage behavior.

| AOSCOST02: How do you choose appropriate<br>storage tiering? |
| ------------------------------------------------------------ |
|                                                              |

Implement a tiered data storage strategy for long-term data
retention or infrequently accessed read-only data. This approach
optimizes cost in OpenSearch domains by offloading less frequently
used data to cost-effective storage options.

###### Best practices

- [AOSCOST02-BP01 Use the latest Amazon EBS gp3 volumes with your
  OpenSearch Service nodes](aoscost02-bp01.md "aoscost02-bp01.md")
- [AOSCOST02-BP02 Use instances optimized for heavy indexing use
  cases](aoscost02-bp02.md "aoscost02-bp02.md")
- [AOSCOST02-BP03 Use the warm storage tier to optimize storage
  for a significant amount of read-only data](aoscost02-bp03.md "aoscost02-bp03.md")
- [AOSCOST02-BP04 Use the cold tier storage option to store and
  retrieve infrequently accessed or historical data](aoscost02-bp04.md "aoscost02-bp04.md")
