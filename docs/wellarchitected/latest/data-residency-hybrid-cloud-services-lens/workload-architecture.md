# Workload architecture

| DRHCREL03: What strategies should you<br>implement to provide reliable data access and processing across<br>on-premises, edge, and cloud environments? |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|                                                                                                                                                        |

If a resource failure occurs, healthy resources should continue to
serve requests. When you have effective failover strategies, your
systems in place can fail over to healthy resources in unimpaired
locations. The failover must be implemented in accordance with
your data residency requirements across on-premises, edge, and
cloud environments.

###### Best practices

- [DRHCREL03-BP01 Use AWS Outposts or Local Zones for scenarios where data must reside within a country or jurisdiction without a local AWS Region](drhcrel03-bp01.md "drhcrel03-bp01.md")
- [DRHCREL03-BP02 Implement failover
  mechanisms to maintain highly-available data access and
  processing across on-premises, edge, and cloud
  environments](drhcrel03-bp02.md "drhcrel03-bp02.md")
