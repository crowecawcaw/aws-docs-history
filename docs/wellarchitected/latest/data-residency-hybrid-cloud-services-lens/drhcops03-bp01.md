# DRHCOPS03-BP01 Understand your organization's RTO and RPO requirements, and build out your disaster recovery solution

Understand your organization's RTO and RPO requirements and build
a tailored disaster recovery solution to minimize disruptions,
data loss, and financial impacts. When using AWS Outposts or Local
Zones, consider data replication, network redundancy, failover
automation, and capacity planning to meet desired RTO and RPO
targets across on-premises and AWS environments.

**Desired outcome:** Establish
clear recovery time and recovery point objectives that align with
the business's tolerance for downtime and data loss related to
your data residency requirements.

**Benefits of establishing this best
practice:** Implementing a disaster recovery solution
tailored to the defined RTO and RPO targets helps your
organization minimize disruptions, data loss, and financial
impacts in the event of a disaster or major outage.

When using AWS Outposts or Local Zones for hybrid workloads,
consider data replication strategies between Outposts and AWS Regions, network connectivity redundancy, failover automation, and
capacity planning to meet desired RTO and RPO targets across
on-premises and AWS environments.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Recovery Time Objective (RTO) defines the maximum acceptable
duration of downtime or service interruption before the recovery
of applications and data must be completed. A shorter RTO
implies a need for faster recovery mechanisms and failover
strategies.

AWS Outposts and AWS Local Zones can be used to extend the AWS
cloud to edge locations, enabling low-latency data processing
and potentially faster recovery times. By deploying critical
workloads on Outposts or Local Zones, organizations can achieve
a shorter RTO by using local redundancy and failover
capabilities.

Recovery Point Objective (RPO) defines the maximum acceptable
amount of data loss or the age of the most recent recoverable
data point in the event of a failure or disaster. A shorter RPO
implies a need for more frequent data backups and replication
mechanisms.

By using local storage and compute resources, Outposts and Local
Zones can facilitate frequent data backups and replication,
helping organizations achieve a shorter RPO. Additionally, these
services can be integrated with AWS services like Amazon Elastic Block Store (Amazon EBS) snapshots, for efficient data
protection and recovery mechanisms.

The choice of using AWS Outposts or AWS Local Zones for hybrid
edge workloads can be influenced by your organization's RTO and
RPO requirements, which are key metrics for ensuring data
availability and business continuity in the event of failures or
disasters. To understand failure scenarios and resiliency
options, see
[Reliability](../data-residency-hybrid-cloud-lens/reliability.md "../data-residency-hybrid-cloud-lens/reliability.md").

Depending on your organizational complexity, you might have
multiple use cases based on the policies of different countries.
Evaluate the specific requirements, laws and regulations, data
volumes, and recovery strategies to determine the most
appropriate solution for each use case.
