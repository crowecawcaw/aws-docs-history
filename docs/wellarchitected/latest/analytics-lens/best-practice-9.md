# Best practice 9.2 – Identify and evaluate the available storage options for your compute solution

Many AWS data analytics services allow you to use more than
one type of storage. For example, Amazon Redshift allows
access to data stored in the compute nodes in addition to
data stored in Amazon S3. When performing research on each
data analytics service, evaluate relevant storage options
to determine the most performance efficient solution that
meets business requirements.

## Suggestion 9.2.1 – Review the available storage options for the analytics services being considered

There are often multiple storage options available for each service, each offering different characteristics and potentially performance benefits. It is important to review these available options and determine which may best fit your requirements.

For example, Amazon EMR provides local storage via HDFS
file system and Amazon S3 as an external storage via EMRFS.
For more information, refer to the AWS documentation for
your compute solution:

- Amazon EMR Management Guide:
  [Work
  with storage and file systems](../../../emr/latest/ManagementGuide/emr-plan-file-systems.md "../../../emr/latest/ManagementGuide/emr-plan-file-systems.md")
- Amazon Redshift Cluster Management Guide:
  [Overview
  of Amazon Redshift clusters](../../../redshift/latest/mgmt/working-with-clusters.md#working-with-clusters-overview "../../../redshift/latest/mgmt/working-with-clusters.md#working-with-clusters-overview")
- Amazon OpenSearch Service Developer Guide:
  [Managing](../../../opensearch-service/latest/developerguide/managing-indices.md "../../../opensearch-service/latest/developerguide/managing-indices.md")
  [indices
  in Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/managing-indices.md "../../../opensearch-service/latest/developerguide/managing-indices.md")
- Amazon Aurora User Guide:
  [Overview
  of Aurora storage](../../../AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.md#Aurora.Overview.Storage "../../../AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.md#Aurora.Overview.Storage")

## Suggestion 9.2.2 – Evaluate the performance of the selected storage option

To ensure that the overall analytics system design meets
your non-functional requirements, evaluate the performance
by running simulated real-world tests in a test
environment.
