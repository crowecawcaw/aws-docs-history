# Using Elastic Disaster Recovery for recovery and failback

In the event of a disaster, AWS Elastic Disaster Recovery facilitates the recovery of your workloads by
launching recovery instances in AWS. Once the disaster has been mitigated, you can also
use AWS Elastic Disaster Recovery to perform failback to the original source infrastructure.

## Key terminology

The following terms are used throughout the AWS Elastic Disaster Recovery documentation. Understanding
the distinction between these terms is important for using the service
effectively.

Recovery
The process of launching recovery instances on AWS using
AWS Elastic Disaster Recovery. This is the action you perform within the Elastic Disaster Recovery Console or API
(using `start-recovery` or **Initiate
recovery job** in the Console). Recovery creates new Amazon EC2
instances from your replicated data.

Recovery drill
A non-disruptive test that launches drill instances to validate
your disaster recovery readiness. Drills use the same process as recovery
but do not affect your source servers or ongoing replication.

Failover
The act of redirecting production traffic from your primary
(source) environment to your recovery instances on AWS. Failover is
performed outside of AWS Elastic Disaster Recovery, typically using a DNS routing service such
as [Amazon
Route 53](../../../Route53/latest/DeveloperGuide/Welcome.md "../../../Route53/latest/DeveloperGuide/Welcome.md") or your organization's traffic management
solution.

Failback
The process of returning your workloads from the recovery
environment on AWS back to your original source infrastructure after the
disaster has been resolved. AWS Elastic Disaster Recovery assists with failback by replicating
data from recovery instances back to your source servers.

In summary: AWS Elastic Disaster Recovery handles **recovery** (launching
instances) and **failback** (returning to source). The
**failover** step (redirecting traffic) is performed by
you, outside of AWS Elastic Disaster Recovery.

## Recovery and Failback overview

AWS Elastic Disaster Recovery provides scalable resilience to your existing infrastructure, coupled with low Recovery Point Objectives (RPO)
and Recovery Time Objectives (RTO). Learn more about how AWS Elastic Disaster Recovery (DRS) can meet your team's
[RPO](CloudEndure-Concepts.md#What-is-RPO "CloudEndure-Concepts.md#What-is-RPO") and [RTO](CloudEndure-Concepts.md#What-is-RTO "CloudEndure-Concepts.md#What-is-RTO").

### Understanding recovery

Recovery allows you to orchestrate launch of your workload within AWS EC2 Instances. After initial sync is completed,
you are able to customize the configuration of the recovery environment in preparation of a business continuity event.

AWS Elastic Disaster Recovery allows you to launch Drill and Recovery instances for
your source servers in AWS once they are in **Continuous Data Protection**. While
Drill Instances and Recovery Instances are launched similarly, they serve different purposes.
During normal operations, we recommend periodically testing your ability to recover using DRS by using Drill Instances.

To recover a group of interdependent source servers in a defined order, with wait
times between groups, use a recovery plan. For more information, see [Orchestrating recovery with recovery
plans](recovery-plans.md "recovery-plans.md").

### Understanding failback

Failback allows you to restore your Recovery Instances back to your source infrastructure. Depending on the source infrastructure,
performing a failback uses differing mechanisms.

| Source Infrastructure  | Failback Mechanism                                                                | More Information                                                                                  |
| ---------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| On-Premise             | Use the Failback Client ISO or the DRS Failback Automation.                       | [On-Premise Failback](failback-performing.md "failback-performing.md")                            |
| AWS<br>• Same Account  | Start Reverse Replication on the Protected Recovery Instance.                     | [Same Account Failback](failback-failover-region-region.md "failback-failover-region-region.md")  |
| AWS<br>• Cross Account | Start Reverse Replication on the Protected Recovery Instance in Failover Account. | [Cross Account Failback](failback-failover-cross-account.md "failback-failover-cross-account.md") |
| Other Cloud            | Configuration varies per provider.                                                | [Other Cloud Failback](failback-performing-main.md "failback-performing-main.md")                 |
