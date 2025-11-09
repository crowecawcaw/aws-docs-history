# Using Elastic Disaster Recovery for recovery and failback

In the event of a disaster, AWS Elastic Disaster Recovery can facilitate with the process of Failover from
either an on-premise environment, Amazon EC2, or a third-party cloud provider. Once the disaster
has been mitigated, you can also use AWS Elastic Disaster Recovery to perform failback to the original source
infrastructure.

## Recovery and Failback overview

AWS Elastic Disaster Recovery provides scalable resilience to your existing infrastructure, coupled with low Recovery Point Objectives (RPO)
and Recovery Time Objectives (RTO). Learn more about how AWS Elastic Disaster Recovery (DRS) can meet your team's
[RPO](CloudEndure-Concepts.md#What-is-RPO "CloudEndure-Concepts.md#What-is-RPO") and [RTO](CloudEndure-Concepts.md#What-is-RTO "CloudEndure-Concepts.md#What-is-RTO").

### Understanding recovery

Recovery allows you to orchestrate launch of your workload within AWS EC2 Instances. After initial sync is completed,
you are able to customize the configuration of recovery environment in preparation of a business continuity event.

AWS Elastic Disaster Recovery allows you to launch Drill and Recovery instances for
your source servers in AWS once they are in **Continuous Data Protection**. While
Drill Instances and Recovery Instances are launched similarly, they serve different purposes.
During normal operations, we recommend periodically testing your ability to recover using DRS by using Drill Instances.

### Understanding failback

Failback allows you to restore your Recovery Instances back to your source infrastructure. Depending on the source infrasture,
performing a failback uses differing mechanisms

| Source Infrastructure  | Failback Mechanism                                                                | More Information                                                                                  |
| ---------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| On-Premise             | Use the Failback Client ISO or the DRS Failback Automation.                       | [On-Premise Failback](failback-performing.md "failback-performing.md")                            |
| AWS<br>• Same Account  | Start Reverse Replication on the Protected Recovery Instance.                     | [Same Account Failback](failback-failover-region-region.md "failback-failover-region-region.md")  |
| AWS<br>• Cross Account | Start Reverse Replication on the Protected Recovery Instance in Failover Account. | [Cross Account Failback](failback-failover-cross-account.md "failback-failover-cross-account.md") |
| Other Cloud            | Configuration varies per provider.                                                | [Other Cloud Failback](failback-performing-main.md "failback-performing-main.md")                 |
