# Best Practice 13.4 – Choose location

to minimize latency

Deploy your SAP instances in Regions and Availability Zones that minimize latency for
key business processes impacting end users, critical interfaces, and intra-system
traffic.

**Suggestion 13.4.1 – Select Region and cloud connectivity to optimize
performance**

Choose a Region based on proximity to your SAP end users and corporate data center.
Select and size any cloud connectivity options (such as Direct Connect and VPN) to accommodate
your data transfer requirements.

Use SAP performance tools to understand the breakdown of user response time (such as
network, GUI, application, and database) and evaluate the impact of any changes to the
network round trip time as a result of increased latency. We recommend you focus on high
frequency, low latency interfaces between systems in different locations.

If increased latency impacts certain end user groups, consider the use of end user
compute services and accelerators.

- AWS Documentation: [AWS
  Direct Connect](https://aws.amazon.com/directconnect/ "https://aws.amazon.com/directconnect/")
- AWS Documentation: [What is AWS Global Accelerator? - AWS Global Accelerator](../../../global-accelerator/latest/dg/what-is-global-accelerator.md "../../../global-accelerator/latest/dg/what-is-global-accelerator.md")
- SAP on AWS Blog: [Deploying SAP GUI on Amazon AppStream 2.0](https://aws.amazon.com/blogs/desktop-and-application-streaming/deploying-sap-gui-on-amazon-appstream-2-0/ "https://aws.amazon.com/blogs/desktop-and-application-streaming/deploying-sap-gui-on-amazon-appstream-2-0/")

**Suggestion 13.4.2 – Be aware of SAP guidelines for intra-system
latency**

SAP provides guidance for acceptable network latency for two traffic patterns: between
SAP application servers and the database, and between SAP HANA database servers (primary and
secondary) for the purposes of data replication. AWS regional networks generally meet or
exceed these requirements.

**Network Latency between SAP application servers and database
(Pattern 1)**

The following SAP guidance for database to application server connectivity is based on
systems running in a single data center, which does not reﬂect the resiliency beneﬁts of a
Multi-AZ deployment. An Availability Zone is one or more discrete data centers with
redundant power, networking, and connectivity in an AWS Region separated by a meaningful
distance (at least 10km).

Resilient SAP architectures in AWS typically involve deploying infrastructure across
multiple AZs, including SAP application server and database instances.

If you have SAP transactions or batch jobs with time-critical performance requirements and
that make a signiﬁcant number of database calls, we recommend that you run these jobs on SAP
application servers located in the same AZ as the database. This can be achieved by using
SAP Logon Groups (transaction SMLG) for end users and a batch server group (transaction
SM61) for background processing jobs. This helps ensure that the latency sensitive parts of
the SAP workload run on application servers with the lowest latency to the database. Use
tools such as NIPING to measure latency.

- SAP Note: [1100926 -
  FAQ: Network performance](https://launchpad.support.sap.com/#/notes/1100926 "https://launchpad.support.sap.com/#/notes/1100926") [Requires SAP Portal Access]
- SAP Note: [2543171 -
  Latency issue between application server and database](https://launchpad.support.sap.com/#/notes/2543171 "https://launchpad.support.sap.com/#/notes/2543171") [Requires SAP Portal
  Access]
  **Network Latency between SAP HANA primary and secondary servers
  (Pattern 2)**

The network latency between the primary and secondary instances will be a factor in the
redo log shipping wait time. For synchronous replication, SAP recommends that this wait time
should be in the low single millisecond range. This requirement can be achieved across AWS
Availability Zones. Use tools such as NIPING to measure latency.

- SAP Documentation: [SAP HANA system replication network requirements](https://www.sap.com/documents/2016/06/18079a1c-767c-0010-82c7-eda71af511fa.html "https://www.sap.com/documents/2016/06/18079a1c-767c-0010-82c7-eda71af511fa.html")

**Suggestion 13.4.3 – Use placement groups for SAP HANA scale
out**

To meet the SAP certification for internode communication in an SAP HANA scale-out
deployment, it is necessary to use a cluster placement group.

- AWS Documentation: [Placement groups - Amazon Elastic Compute Cloud](../../../AWSEC2/latest/UserGuide/placement-groups.md#placement-groups-cluster "../../../AWSEC2/latest/UserGuide/placement-groups.md#placement-groups-cluster")
