# Foundations

| EUCREL01: How do you increase resilience and minimize<br>impact of failure in your EUC environment? |
| --------------------------------------------------------------------------------------------------- |
|                                                                                                     |

An Amazon WorkSpaces environment can achieve increased resilience
using the native deployment pattern within the managed services
that dictates that a minimum of two Availability Zones (AZs) are
used. Where increased resilience is required at the regional
rather than zonal level, multi-region Amazon WorkSpaces
environments can be deployed in separate regions.

For Amazon WorkSpaces Applications, increased resilience can be achieved by
deploying fleets across a minimum of two AZs and using three AZs
where possible. Where increased resilience is required at the
regional rather than zonal level, multi-region Amazon AppStream
2.0 environments can be deployed in separate regions. This is
achieved by copying images between regions and establishing
separate fleets in multiple regions.

###### Best practices

- [EUCREL01-BP01 Add redundancy and remove single points of failure in your environment](eucrel01-bp01.md "eucrel01-bp01.md")
