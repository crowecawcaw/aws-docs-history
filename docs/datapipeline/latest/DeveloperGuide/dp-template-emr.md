AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Run job on an Amazon EMR cluster

The **Run Job on an Elastic MapReduce Cluster** template
launches an Amazon EMR cluster based on the parameters provided and starts running
steps based on the specified schedule. Once the job completes, the EMR cluster
is terminated. Optional bootstrap actions can be specified to install additional
software or to change application configuration on the cluster.

The template uses the following pipeline objects:

- [EmrActivity](dp-object-emractivity.md "dp-object-emractivity.md")
- [EmrCluster](dp-object-emrcluster.md "dp-object-emrcluster.md")
