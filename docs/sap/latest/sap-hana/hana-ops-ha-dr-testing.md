# Testing SAP HANA high availability deployments

This section covers failure scenarios for backup, testing guidance and considerations for high availability and disaster recovery solutions, and disaster recovery mock exercise.

###### Topics

- [Failure scenarios for backup and recommendations](#hana-ops-ha-dr-scenarios "#hana-ops-ha-dr-scenarios")
- [Testing guidance and considerations](#hana-ops-ha-dr-testing-guidance "#hana-ops-ha-dr-testing-guidance")

## Failure scenarios for backup and recommendations

The following table provides an overview of different failures scenarios for the SAP HANA system, the risk of occurrence, potential data loss, and maximum outage. It is important to determine which failure scenario will require a recovery from backup. Note that the granularity of the scenarios, classification, and impact will vary depending on your requirements and architecture.

|                                       |                                                                                                        |                                    |                                              |                                                                                     |              |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------- | -------------------------------------------- | ----------------------------------------------------------------------------------- | ------------ |
| **Data protection/disaster recovery** | **Failure scenarios**                                                                                  | **Comparative risk of occurrence** | **Potential data loss**                      | **Maximum outage**                                                                  | **Impact**   |
| **No high availability**              | Resource exhausted or compromised (high CPU utilization/file system full/out of memory/storage issues) | Medium                             | ~o (uncommitted transactions)                | Avoidable                                                                           | Region       |
| **High availability**                 | Single point of failure (database)                                                                     | Medium                             | ~o (uncommitted transactions)                | Time to detect failure and failover (automated)                                     | Region       |
| **High availability**                 | Availability Zone/network failure                                                                      | Low                                | ~o (uncommitted transactions)                | Time to detect failure and failover (automated)                                     | Region       |
| **High availability**                 | Core service failure                                                                                   | Low                                | o                                            | Dependent on failure                                                                | Region       |
| **Disaster recovery**                 | Corruption/accidental deletion/malicious activities/faulty code deployment                             | Low                                | Last consistent restore point before failure | Time to detect failure and failover (manual)                                        | Cross-Region |
| **Disaster recovery**                 | Region failure                                                                                         | Very low                           | Replication delay                            | Time to detect failure and make a decision to invoke disaster recovery and takeover | Cross-Region |

For SAP HANA systems without high availability implementation, the core critical components of failure for an instance at the infrastructure level are compute, memory, and storage. For compute or memory related failure scenarios, it could be a processor, memory failure or resource exhaustion, such as high CPU utilization, out of memory etc. We recommend the following approaches for recovery of SAP HANA system, in case of CPU or memory issue.

- Use Amazon EC2 automatic recovery or host recovery to bring the SAP HANA system up on new host. For more information, see [Amazon EC2 recovery options](hana-ops-ha-dr.md#ec2-recovery-hana-hadr "hana-ops-ha-dr.md#ec2-recovery-hana-hadr").
- Create a full backup of your Amazon EC2 instance using Amazon Machine Image along with a snapshot of individual Amazon EBS volumes. Use this as golden image to launch a new instance in case of any failure.
- Implement a monitoring solution, such as Amazon CloudWatch to prevent failure scenarios involving CPU or memory resource exhaustion.

You can resize or upgrade your Amazon EC2 instance to support a greater number of CPU cores or instance memory size. For more information, see [Change the instance type](../../../AWSEC2/latest/UserGuide/ec2-instance-resize.md "../../../AWSEC2/latest/UserGuide/ec2-instance-resize.md").

For SAP HANA system, Amazon EBS volumes can be the primary storage for operating `root`, `data` or `log` volumes. There can be different failure scenarios, such as Amazon EBS volume failure, disk corruption, accidental deletion of data, malicious attack, faulty code deployment etc. We recommend the following options to safeguard your data.

- Use SAP HANA backup and restore to back up your SAP HANA database to Amazon S3 using AWS Backint Agent for SAP HANA.
- Take regular Amazon Machine Images/Amazon EBS snapshots of your servers on a regular basis.

Amazon S3 single-Region replication should be configured to protect against data loss in the same Region. For disaster recovery, we recommend using Amazon S3 cross-Region replication to save backups/snapshots in the secondary Region, in the event of a failure in the primary Region. You can restore the SAP HANA system in the secondary Region from the last set of backups/snapshots. Here the recovery point objective depends on the last consistent restore point before the failure.

## Testing guidance and considerations

Pacemaker cluster can help you perform planned downtime tasks, such as patching SAP HANA database, by automating failover and failback of cluster members. Various unplanned or fault situations can arise during SAP HANA database operations. These can include but are not limited to the following.

- Hardware failures, such as memory module failures on bare-metal instances
- Software failures, such as process crashes due to out-of-memory issues
- Network outage

Most of these failure scenarios can be simulated using SAP HANA database and Linux operating system commands. The scenarios for AWS infrastructure can also be simulated on AWS Management Console or by using AWS APIs. For more information, see [AWS APIs](../../../general/latest/gr/aws-apis.md "../../../general/latest/gr/aws-apis.md").

High availability cluster solutions constantly monitor the configured resources, to detect and react as per pre-defined thresholds, dependencies, and target state. SAP HANA pacemaker cluster configuration can vary, depending on factors such as, size of the database, application availability, and others. The following are some of the considerations for testing SAP HANA high availability deployments based on pacemaker cluster.

- SAP HANA high availability installation based on a pacemaker cluster must undergo planned and unplanned outage scenarios to verify stability.
- You can perform initial cluster tests without loading business data into SAP HANA database. The first iteration of testing verifies if the cluster behaves as intended during various fault scenarios. In this iteration, you can also perform initial cycle of test cases and find out about any product or configuration issues.
- The second iteration of testing can be performed with production size data loaded into the SAP HANA database. The main objective is to tune the cluster monitors for effective timeouts.

Large SAP HANA databases take more time to start and stop. If they are hosted on AWS bare-metal instances, the time taken to reboot can be longer. As these factors can impact the cluster behavior, the cluster timeout values have to be tuned accordingly.

- An SAP Application can have many single point of failures, and SAP HANA database is one of them. The availability of an SAP application is dependent on all single point of failures being resilient to failure situations. Include single point of failures in overall testing. For example, validate an AWS Availability Zone failure where both SAP Application/NetWeaver stack component (ASCS) and SAP HANA database are deployed in the same Availability Zone. The cluster solution must be able to failover pre-configured resources and the SAP application must be restored on the target Availability Zone.
- Test cases that comprise of planned and unplanned downtimes should be tested as a minimum validation. You can also include scenarios where single point of failures was observed in the past. For instance, a year-end consolidation jobs testing the instance memory limits, leading to database crashes.

For SAP HANA high availability deployment with pacemaker cluster on **SLES** on AWS test cases, see [Testing the cluster](sap-hana-pacemaker-sles-testing.md "sap-hana-pacemaker-sles-testing.md").

For SAP HANA high availability deployment with pacemaker cluster on **RHEL** on AWS test cases, see [Testing the cluster](sap-hana-pacemaker-rhel-testing.md "sap-hana-pacemaker-rhel-testing.md").

- Pacemaker cluster solution require virtual IP address configuration for client connections. With virtual IP addresses, the actual hardware where the SAP workloads run remain transparent to client applications. There is a seamless failover of connections in the event of a failure. You must verify that all the intended SAP or third-party interfaces are able to connect to the target SAP application post failover.

You can start by preparing a client connections or interfaces list that includes all critical connections to the target SAP system. Identify the modifications required in your connection configuration to point to a virtual IP address or load balancing mechanism. During testing, each connection must be validated for connectivity, time taken to detect new connection, and loss of locks set by the application, before the cluster performs a failover. For more information, see [Client redirect options](hana-ops-ha-dr-hsr.md#hsr-client-redirect "hana-ops-ha-dr-hsr.md#hsr-client-redirect").

- If you have high availability and disaster recovery on your SAP HANA workloads, you must take additional steps to perform cluster validations. A pacemaker cluster only has visibility into its cluster members(primary and secondary). The cluster software does not control disaster recovery operations (tier-3/tertiary).

When a failover is triggered in a multi-tier SAP HANA system replication setup and the secondary database takes over the role of primary, the replication continues on the tertiary system. However, once the fault with the original primary system is rectified and the system is made available again, manual intervention are be required to complete the reverse replication requirements from the new primary SAP HANA database to the original primary. These manual steps are needed for SAP HANA databases that do not support (lower than SAP HANA 2.0) multi-target replication. For more information, see [SAP HANA multi-target replication](hana-ops-ha-dr-hsr.md#hsr-multi-target "hana-ops-ha-dr-hsr.md#hsr-multi-target").

After performing failback to the original primary, some manual steps have to be performed to re-enable the replication on the tertiary site. It is very important to validate the flow of these steps and the time taken for services to startup during each testing scenario before releasing the systems for productive usage.
