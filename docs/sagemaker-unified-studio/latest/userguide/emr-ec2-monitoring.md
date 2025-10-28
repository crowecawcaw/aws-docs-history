# Monitoring Amazon EMR on EC2 clusters in Amazon SageMaker Unified Studio

You can monitor the performance of your Amazon EMR on EC2 clusters to ensure optimal resource
use and efficient job execution. Information on metrics is automatically collected and sent to
Amazon CloudWatch during operation of an Amazon EMR cluster.

You can see [CloudWatch metrics](../../../emr/latest/ManagementGuide/UsingEMR_ViewingMetrics.md "../../../emr/latest/ManagementGuide/UsingEMR_ViewingMetrics.md") for a specific cluster by selecting the cluster you're
interested in from the list of clusters under the Cluster tab. Selecting a cluster will bring
you to the Detail view for that cluster. After you've selected a cluster, select the
**Monitoring** tab.

You will be able to see a grid view of the CloudWatch Metrics for the cluster you selected.

You can see information presented through different views by using the **Dashboard View** drop-down menu: Cluster
Overview, Primary Node Group, Core Node Group, Task Node Group. You can also adjust the time range.
