# 9 – Choose the best-performing storage solution

**How do you select the best-performing
storage options for your workload?**

An analytics workload’s optimal storage solution is influenced by several factors such as:

- Compute engine (Amazon EMR, Amazon Redshift, Amazon RDS, and
  so on)
- Access patterns (random or sequential)
- Required throughput
- Access frequency (online, offline, archival)
- CRUD (create, read, update, delete) operation requirements
- Data durability requirements
- Archival requirements

Choose the best-performing storage solution for your analytics
workload’s own characteristics.

| **ID**      | **Priority**       | **Best practice**                                                                                      |
| ----------- | ------------------ | ------------------------------------------------------------------------------------------------------ |
| ☐<br>BP 9.1 | Highly recommended | Identify critical performance criteria for your storage<br>workload.                                   |
| ☐<br>BP 9.2 | Highly recommended | Identify and evaluate the available storage options for<br>your compute solution.                      |
| ☐<br>BP 9.3 | Recommended        | Choose the optimal storage based on access patterns,<br>data growth, and the performance requirements. |

For more details, refer to the following information:

- Amazon Elastic Compute Cloud User Guide for Linux Instances:
  [Amazon EBS volume types](../../../AWSEC2/latest/UserGuide/ebs-volume-types.md "../../../AWSEC2/latest/UserGuide/ebs-volume-types.md")
- Amazon Redshift Database Developer Guide:
  [Amazon Redshift best practices for loading data PDF](../../../redshift/latest/dg/c_loading-data-best-practices.md "../../../redshift/latest/dg/c_loading-data-best-practices.md")
- Amazon EMR Management Guide:
  [Instance
  storage](../../../emr/latest/ManagementGuide/emr-plan-storage.md "../../../emr/latest/ManagementGuide/emr-plan-storage.md")
- Amazon Simple Storage Service User Guide:
  [Best
  practices design patterns: Optimizing Amazon S3](../../../AmazonS3/latest/userguide/optimizing-performance.md "../../../AmazonS3/latest/userguide/optimizing-performance.md")
  [performance](../../../AmazonS3/latest/userguide/optimizing-performance.md "../../../AmazonS3/latest/userguide/optimizing-performance.md")
