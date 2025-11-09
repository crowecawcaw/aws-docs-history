# Design for single- and Multi-Region deployments

| ADVREL03: How have you designed<br>application to achieve reliability in single<br>• and multi<br>• Region<br>deployments? |
| -------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                            |

There are multiple strategies for achieving reliability in
single and multi-Region deployments. Implement full Regional
deployment using auto scaling and container orchestration.
Select AWS Regions based on legal and disaster recovery
requirements. Configure your databases with appropriate
reliability and recovery strategies. Manage service capacity
through proper resource reservation and load testing.

Focus on building resilient architectures that balance
performance, compliance, and cost considerations.

###### Best practices

- [ADVREL03-BP01 Use a full Regional deployment for compute resources through Auto Scaling groups and compute container orchestrators](advrel03-bp01.md "advrel03-bp01.md")
- [ADVREL03-BP02 Choose AWS Regions that meet your legal and disaster recovery requirements](advrel03-bp02.md "advrel03-bp02.md")
- [ADVREL03-BP03 Configure databases to span across multiple Availability Zones](advrel03-bp03.md "advrel03-bp03.md")
- [ADVREL03-BP04 Reserve appropriate capacity of services in the supported Regions](advrel03-bp04.md "advrel03-bp04.md")
