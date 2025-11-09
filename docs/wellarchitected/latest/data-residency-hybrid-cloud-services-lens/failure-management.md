# Failure management

| DRHCREL05: How do you manage and recover<br>from failure to maintain reliable data access and processing<br>across on-premises, edge, and cloud environments? |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                               |

Running workloads are subject to disruptions for a number of
reasons. Therefore, you must take steps to implement resiliency if
you need your workload to be reliable while also meeting your data
residency requirements.

| DRHCREL06: Is your application resilient<br>to on-premises maintenance activities? |
| ---------------------------------------------------------------------------------- |
|                                                                                    |

Under the
[shared
responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/"), AWS is responsible for the hardware
and software that run AWS services. This applies to AWS Outposts, just as it does to an AWS Region. AWS monitors the
performance, health, and metrics for your Outposts rack and
determines whether any maintenance is required. If AWS detects
an irreparable issue with hardware during the server
provisioning process or while hosting Amazon EC2 instances
running on your Outposts server, we will notify the Outpost
owner and the owner of the instances that the affected instances
are scheduled for retirement. For high availability, your
workloads must be resilient during maintenance activities while
also preserving data residency requirements.

###### Best practices

- [DRHCREL05-BP01 Provision spare compute capacity following an N+M model](drhcrel05-bp01.md "drhcrel05-bp01.md")
- [DRHCREL05-BP02 To mitigate the impact of Availability Zone or Region failures, deploy multiple Outposts anchored to different Availability Zones or Regions](drhcrel05-bp02.md "drhcrel05-bp02.md")
- [DRHCREL05-BP03 Maintain high availability during on-premises maintenance activities](drhcrel05-bp03.md "drhcrel05-bp03.md")
- [DRHCREL05-BP04 Design your environment to maintain availability and recover in case of failure in a critical sub-system like networking, server, rack, or within the application itself](drhcrel05-bp04.md "drhcrel05-bp04.md")
- [DRHCREL06-BP01 Use AWS Health to receive EC2 instance retirement notifications and scheduled events on Outposts that may require instance failover ahead of time](drhcrel06-bp01.md "drhcrel06-bp01.md")
