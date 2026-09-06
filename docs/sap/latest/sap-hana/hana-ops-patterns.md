

# Architecture patterns for SAP HANA on AWS
<a name="hana-ops-patterns"></a>

This section provides information on architecture patterns that can be used as guidelines for deploying SAP HANA systems on AWS. For more information on the architecture patterns for SAP NetWeaver-based applications on AWS, see [Architecture guidance for availability and reliability of SAP on AWS](https://docs.aws.amazon.com/sap/latest/general/architecture-guidance-of-sap-on-aws.html).

You can change the patterns to fit your changing business requirements with minimum to no downtime, depending on the complexity of your chosen architecture pattern.

**Topics**
+ [SAP HANA System Replication](#hana-ops-patterns-hsr)
+ [Secondary SAP HANA instance](#hana-ops-secondary-instance)
+ [Overview of patterns](#hana-ops-patterns-types)
+ [Single Region architecture patterns for SAP HANA](hana-ops-patterns-single.md)
+ [Multi-Region architecture patterns for SAP HANA](hana-ops-patterns-multi.md)

## SAP HANA System Replication
<a name="hana-ops-patterns-hsr"></a>

SAP HANA System Replication is a high availability solution provided by SAP for SAP HANA that can be used to reduce outage due to maintenance activities, faults, and disasters. It continuously replicates data on a secondary instance. The changes persist on the alternate instance in the event of a failure on the primary instance. For more information, see [Configuring SAP HANA System Replication](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/676844172c2442f0bf6c8b080db05ae7.html?version=2.0.01).

## Secondary SAP HANA instance
<a name="hana-ops-secondary-instance"></a>

In AWS Cloud, a secondary SAP HANA instance can exist in the same Region on a different Availability Zone or in a separate Region. For more information, see [Architecture guidelines and decisions](https://docs.aws.amazon.com/sap/latest/general/arch-guide-architecture-guidelines-and-decisions.html). The secondary instance can be deployed as a passive instance or an active (read-only) instance. When the secondary instance is deployed as a passive instance, you can reuse the Amazon EC2 instance capacity to accommodate a non-production SAP HANA workload.

## Overview of patterns
<a name="hana-ops-patterns-types"></a>

The architecture patterns for SAP HANA are divided into the following two categories:
+  [Single Region architecture patterns for SAP HANA](hana-ops-patterns-single.md) 
+  [Multi-Region architecture patterns for SAP HANA](hana-ops-patterns-multi.md) 

You must consider the risk and impact of each failure type, and the cost of mitigation when choosing a pattern. The following table provides a quick overview of the architecture patterns for SAP HANA systems on AWS.


<table>
<tbody>
  <tr><td rowspan="2"> <b>Patterns</b> </td><td colspan="3"> <b>Business requirements</b> </td><td colspan="3"> <b>Solution characteristics</b> </td><td colspan="2"> <b>Implementation details</b> </td></tr>
  <tr><td> <b>Resilience type</b> </td><td> <b>Recovery point objective1 </b> </td><td> <b>Recovery time objective2 </b> </td><td> <b>Cost</b> </td><td> <b>Complexity</b> </td><td> <b>Capacity re-use3 </b> </td><td> <b>SAP HANA System Replication4 </b> </td><td> <b>Amazon S3 replication5 </b> </td></tr>
  <tr><td> <a href="hana-ops-patterns-single.md#hana-ops-patterns-pattern1">Pattern 1</a> </td><td rowspan="4">Single Region disaster recovery</td><td>Near zero</td><td>Low</td><td>Medium</td><td>Medium</td><td>Optional</td><td>2-tier</td><td rowspan="4">Same Region</td></tr>
  <tr><td> <a href="hana-ops-patterns-single.md#hana-ops-patterns-pattern2">Pattern 2</a> </td><td>Near zero</td><td>Low</td><td>Medium</td><td>High</td><td>Yes</td><td>3-tier</td></tr>
  <tr><td> <a href="hana-ops-patterns-single.md#hana-ops-patterns-pattern3">Pattern 3</a> </td><td>Low</td><td>Medium</td><td>Low</td><td>Medium</td><td>Yes</td><td>2-tier</td></tr>
  <tr><td> <a href="hana-ops-patterns-single.md#hana-ops-patterns-pattern4">Pattern 4</a> </td><td>Medium</td><td>High</td><td>Very low</td><td>Very low</td><td>N/A</td><td>N/A</td></tr>
  <tr><td> <a href="hana-ops-patterns-multi.md#hana-ops-patterns-pattern5">Pattern 5</a> </td><td rowspan="4">Multi-Region disaster recovery</td><td>Near zero</td><td>Low</td><td>Medium</td><td>Medium</td><td>Optional</td><td>2-tier</td><td rowspan="4">Cross Region</td></tr>
  <tr><td> <a href="hana-ops-patterns-multi.md#hana-ops-patterns-pattern6">Pattern 6</a> </td><td>Near zero</td><td>Low</td><td>High</td><td>High</td><td>Optional</td><td>3-tier</td></tr>
  <tr><td> <a href="hana-ops-patterns-multi.md#hana-ops-patterns-pattern7">Pattern 7</a> </td><td>Near zero</td><td>Low</td><td>Very high</td><td>Very high</td><td>Optional</td><td>Multi-target</td></tr>
  <tr><td> <a href="hana-ops-patterns-multi.md#hana-ops-patterns-pattern8">Pattern 8</a> </td><td>Medium</td><td>High</td><td>Low</td><td>Low</td><td>N/A</td><td>N/A</td></tr>
</tbody>
</table>


 * 1To achieve near zero recovery point objective, SAP HANA System Replication must be setup in sync mode for the SAP HANA instances within the same Region.* 

 * 2To achieve the lowest recovery time objective, we recommend using a high availability setup with third-party cluster solutions in combination with SAP HANA System Replication.* 

 * 3A production sized Amazon EC2 instance can be deployed as an MCOS installation to accommodate a non-production SAP HANA instance.* 

 * 4SAP HANA System Replication and the number of SAP HANA instance copies as targets.* 

 * 5Same-Region replication copies objects across Amazon S3 buckets in the same Region.* 