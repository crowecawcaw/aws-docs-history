# Replicating your data using NetApp SnapMirror

You can use NetApp SnapMirror to schedule periodic replication of your FSx for ONTAP file system
to or from a second file system. This capability is available for both in-Region and cross-Region
deployments.

NetApp SnapMirror replicates data at high speeds, so you get high data availability and fast data replication
across ONTAP systems, whether you're replicating between two Amazon FSx file systems in AWS, or from on-premises to AWS.
Replication can be scheduled as frequently as every 5 minutes, although intervals should be carefully chosen based
on RPOs (Recovery Point Objectives), RTOs (Recovery Time Objectives), and performance considerations.

When you replicate data to NetApp storage systems and continually update the secondary data,
your data is kept current and remains available whenever you need it. No external replication servers
are required. For more information about using NetApp SnapMirror to replicate your data,
see [Learn about NetApp Replication](https://docs.netapp.com/us-en/data-services-replication/concept-replication.html "https://docs.netapp.com/us-en/data-services-replication/concept-replication.html")
in the _NetApp Console documentation_.

You can create a data protection (DP) destination volume for NetApp SnapMirror
using the Amazon FSx console, the AWS CLI, and the Amazon FSx API, in addition to the NetApp ONTAP CLI and REST API.
For information about creating a destination volume using the Amazon FSx console and AWS CLI,
see [Creating volumes](creating-volumes.md "creating-volumes.md").

You can use NetApp Console or the ONTAP CLI to schedule replication for your file system.

###### Note

There are two types of SnapMirror replication: Volume-level SnapMirror and SVM Disaster Recovery (SVMDR).
Only volume-level SnapMirror replication is supported by FSx for ONTAP. Synchronous SnapMirror, including StrictSync, is not supported.

## Using NetApp Console to schedule replication

You can use NetApp Console to set up replication with SnapMirror on your FSx for ONTAP file system. For more information, see
[Set up data replication in NetApp Replication](https://docs.netapp.com/us-en/cloud-manager-replication/task-replicating-data.html "https://docs.netapp.com/us-en/cloud-manager-replication/task-replicating-data.html") in the
_NetApp Console documentation_.

## Using the ONTAP CLI to schedule replication

You can use the ONTAP CLI to configure scheduled volume replication. For information, see
[Managing SnapMirror volume replication](https://docs.netapp.com/us-en/ontap/data-protection/snapmirror-replication-workflow-concept.html "https://docs.netapp.com/us-en/ontap/data-protection/snapmirror-replication-workflow-concept.html") in the _NetApp ONTAP Documentation Center_.
