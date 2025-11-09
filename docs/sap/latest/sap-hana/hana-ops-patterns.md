# Architecture patterns for SAP HANA on AWS

This section provides information on architecture patterns that can be used as guidelines for deploying SAP HANA systems on AWS. For more information on the architecture patterns for SAP NetWeaver-based applications on AWS, see [Architecture guidance for availability and reliability of SAP on AWS](../general/architecture-guidance-of-sap-on-aws.md "../general/architecture-guidance-of-sap-on-aws.md").

You can change the patterns to fit your changing business requirements with minimum to no downtime, depending on the complexity of your chosen architecture pattern.

###### Topics

- [SAP HANA System Replication](#hana-ops-patterns-hsr "#hana-ops-patterns-hsr")
- [Secondary SAP HANA instance](#hana-ops-secondary-instance "#hana-ops-secondary-instance")
- [Overview of patterns](#hana-ops-patterns-types "#hana-ops-patterns-types")
- [Single Region architecture patterns for SAP HANA](hana-ops-patterns-single.md "hana-ops-patterns-single.md")
- [Multi-Region architecture patterns for SAP HANA](hana-ops-patterns-multi.md "hana-ops-patterns-multi.md")

## SAP HANA System Replication

SAP HANA System Replication is a high availability solution provided by SAP for SAP HANA that can be used to reduce outage due to maintenance activities, faults, and disasters. It continuously replicates data on a secondary instance. The changes persist on the alternate instance in the event of a failure on the primary instance. For more information, see [Configuring SAP HANA System Replication](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/676844172c2442f0bf6c8b080db05ae7.html?version=2.0.01 "https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/676844172c2442f0bf6c8b080db05ae7.html?version=2.0.01").

## Secondary SAP HANA instance

In AWS Cloud, a secondary SAP HANA instance can exist in the same Region on a different Availability Zone or in a separate Region. For more information, see [Architecture guidelines and decisions](../general/arch-guide-architecture-guidelines-and-decisions.md "../general/arch-guide-architecture-guidelines-and-decisions.md"). The secondary instance can be deployed as a passive instance or an active (read-only) instance. When the secondary instance is deployed as a passive instance, you can reuse the Amazon EC2 instance capacity to accommodate a non-production SAP HANA workload.

## Overview of patterns

The architecture patterns for SAP HANA are divided into the following two categories:

- [Single Region architecture patterns for SAP HANA](hana-ops-patterns-single.md "hana-ops-patterns-single.md")
- [Multi-Region architecture patterns for SAP HANA](hana-ops-patterns-multi.md "hana-ops-patterns-multi.md")

You must consider the risk and impact of each failure type, and the cost of mitigation when choosing a pattern. The following table provides a quick overview of the architecture patterns for SAP HANA systems on AWS.

|                                                                                                                              |                                 |                              |                            |
| ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ---------------------------- | -------------------------- | -------------- | -------------------- | -------------------------------- | -------------------------- | ------------ |
| **Patterns**                                                                                                                 | **Business requirements**       | **Solution characteristics** | **Implementation details** |
| **Resilience type**                                                                                                          | **Recovery point objective1**   | **Recovery time objective2** | **Cost**                   | **Complexity** | **Capacity re-use3** | **SAP HANA System Replication4** | **Amazon S3 replication5** |
| [Pattern 1](hana-ops-patterns-single.md#hana-ops-patterns-pattern1 "hana-ops-patterns-single.md#hana-ops-patterns-pattern1") | Single Region disaster recovery | Near zero                    | Low                        | Medium         | Medium               | Optional                         | 2-tier                     | Same Region  |
| [Pattern 2](hana-ops-patterns-single.md#hana-ops-patterns-pattern2 "hana-ops-patterns-single.md#hana-ops-patterns-pattern2") | Near zero                       | Low                          | Medium                     | High           | Yes                  | 3-tier                           |
| [Pattern 3](hana-ops-patterns-single.md#hana-ops-patterns-pattern3 "hana-ops-patterns-single.md#hana-ops-patterns-pattern3") | Low                             | Medium                       | Low                        | Medium         | Yes                  | 2-tier                           |
| [Pattern 4](hana-ops-patterns-single.md#hana-ops-patterns-pattern4 "hana-ops-patterns-single.md#hana-ops-patterns-pattern4") | Medium                          | High                         | Very low                   | Very low       | N/A                  | N/A                              |
| [Pattern 5](hana-ops-patterns-multi.md#hana-ops-patterns-pattern5 "hana-ops-patterns-multi.md#hana-ops-patterns-pattern5")   | Multi-Region disaster recovery  | Near zero                    | Low                        | Medium         | Medium               | Optional                         | 2-tier                     | Cross Region |
| [Pattern 6](hana-ops-patterns-multi.md#hana-ops-patterns-pattern6 "hana-ops-patterns-multi.md#hana-ops-patterns-pattern6")   | Near zero                       | Low                          | High                       | High           | Optional             | 3-tier                           |
| [Pattern 7](hana-ops-patterns-multi.md#hana-ops-patterns-pattern7 "hana-ops-patterns-multi.md#hana-ops-patterns-pattern7")   | Near zero                       | Low                          | Very high                  | Very high      | Optional             | Multi-target                     |
| [Pattern 8](hana-ops-patterns-multi.md#hana-ops-patterns-pattern8 "hana-ops-patterns-multi.md#hana-ops-patterns-pattern8")   | Medium                          | High                         | Low                        | Low            | N/A                  | N/A                              |

_1To achieve near zero recovery point objective, SAP HANA System Replication must be setup in sync mode for the SAP HANA instances within the same Region._

_2To achieve the lowest recovery time objective, we recommend using a high availability setup with third-party cluster solutions in combination with SAP HANA System Replication._

_3A production sized Amazon EC2 instance can be deployed as an MCOS installation to accommodate a non-production SAP HANA instance._

_4SAP HANA System Replication and the number of SAP HANA instance copies as targets._

_5Same-Region replication copies objects across Amazon S3 buckets in the same Region._
