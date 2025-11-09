# SAP on AWS architecture patterns for Microsoft SQL server

This document provides information about architecture patterns for deploying SAP workloads in AWS Cloud on Microsoft SQL servers. These patterns offer highly available and resilient implementation options while considering your recovery time and point objectives.

Work backwards from your business requirements to define an approach that meets the availability goals of your SAP systems and data. For each failure scenario, the resiliency requirements, acceptable data loss, and mean time to recover need to be proportionate to the criticality of the component and the supported business applications.

You can customize these patterns for your specific business criteria. You should consider the risk and impact of each failure type, and the cost of mitigation when choosing a pattern.

###### Topics

- [Patterns](#patterns "#patterns")
- [Comparison matrix](#comparison "#comparison")
- [Single Region architecture patterns for Microsoft SQL server](single-region.md "single-region.md")
- [Multi-Region patterns for Microsoft SQL server](multi-region.md "multi-region.md")

## Patterns

The architecture patterns are divided into two categories.

- [Single Region patterns](single-region.md "single-region.md")
- [Multi-Region patterns](multi-region.md "multi-region.md")

## Comparison matrix

The following table provides a comparison of all the architecture patterns discussed further.

|                     |                                 |                              |                            |
| ------------------- | ------------------------------- | ---------------------------- | -------------------------- | -------------- | ---------------- | ------------------------- | ------------ |
| **Patterns**        | **Business requirements**       | **Solution characteristics** | **Implementation details** |
| **Resilience type** | **Recovery point objective**    | **Recovery time objective**  | **Cost**                   | **Complexity** | **SQL AlwaysOn** | **Amazon S3 replication** |
| Pattern 1           | Single Region disaster recovery | Near zero\*                  | Low                        | Medium         | Medium           | 2-tier                    | N/A          |
| Pattern 2           | Medium                          | High                         | Very low                   | Very low       | N/A              | N/A                       |
| Pattern 3           | Multi-Region disaster recovery  | Medium                       | High                       | Medium         | Medium           | 2-tier                    | Cross Region |
| Pattern 4           | Near zero\*                     | Low                          | High                       | High           | 3-tier           | Cross Region              |
| Pattern 5           | Medium                          | High                         | Low                        | Low            | N/A              | Cross Region              |
| Pattern 6           | Low                             | Low                          | Medium                     | Medium         | N/A              | N/A                       |

_\*To achieve near zero recovery point objective, database replication must be setup in synchronous data commit mode within the same AWS Region._
