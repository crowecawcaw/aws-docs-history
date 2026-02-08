# Manage demand and supply

resources

Effectively managing demand and supply resources in hybrid networking environments
requires a strategic approach that balances on-premises infrastructure with cloud resources.
Organizations should implement scaling mechanisms that dynamically adjust network resources
based on real-time traffic patterns and application demands.

| HNCOST05: How do you match the supply of resources for your hybrid<br>networking with demand? |
| --------------------------------------------------------------------------------------------- |
|                                                                                               |

Effective hybrid networking requires alignment between resource supply and fluctuating
demand. Since scaling hybrid connectivity components like dedicated connections often involves
significant lead times, forward planning becomes crucial. Organizations should implement a
proactive approach that combines early provisioning for anticipated future needs with regular
performance testing to identify bottlenecks. This balanced strategy ensures seamless
connectivity across on-premises and cloud environments while maintaining cost-effectiveness,
preventing both expensive over-provisioning and performance-limiting under-allocation.

| HNCOST06: How do you prioritize traffic across your hybrid networking<br>connections? |
| ------------------------------------------------------------------------------------- |
|                                                                                       |

Prioritizing traffic ensures mission-critical applications such as VoIP and real-time
data to receive guaranteed bandwidth, while non-critical traffic such as backups uses
remaining capacity. This prevents congestion and aligns costs with business priorities.

###### Best practices

- [HNCOST05-BP01 Forecast demand and baseline requirements before
  scaling dedicated connections](hncost05-bp01.md "hncost05-bp01.md")
- [HNCOST06-BP01 Implement QoS policies for traffic
  prioritization](hncost06-bp01.md "hncost06-bp01.md")
- [HNCOST06-BP02 Separate traffic classes for dedicated connections](hncost06-bp02.md "hncost06-bp02.md")
