

# Cluster configuration changes after Replicator creation
<a name="msk-replicator-post-creation-config"></a>
+ We recommend that you do not turn tiered storage on or off after the MSK Replicator has been created. If your target cluster is not tiered, MSK will not copy the tiered storage configurations, regardless of whether your source cluster is tiered. If you turn on tiered storage on the target cluster after Replicator is created, the Replicator needs to be recreated. If you want to copy data from a non-tiered to a tiered cluster, you should not copy topic configurations.
+ Do not change the following cluster configuration settings after MSK Replicator creation, as they are validated during creation:
  + Change MSK cluster to t3 instance type.
  + Change service execution role permissions.
  + Disable MSK multi-VPC private connectivity.
  + Change the attached cluster resource-based policy.
  + Change cluster security group rules.
+ For Identical topic name replication configurations, do not make changes to the headers that MSK Replicator creates (`__mskmr`) to avoid the risk of cyclic replication.