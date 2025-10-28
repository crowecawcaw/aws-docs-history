# Amazon EMR cluster error: HDFS insufficient space error

An Hadoop Distributed File System (HDFS) insufficient space error can occur if you attempt to remove a core node, but Amazon EMR can't
safely complete the operation because of insuficicent space left in the HDFS. Before Amazon EMR removes
a core node, all HDFS data on the node must be transferred to other core nodes to ensure data redundancy.
However, if there isn't enough space on the other core nodes for replication, Amazon EMR can't gracefully
decommission the node.

## Possible causes

See the following for a list of possible causes of HDFS insufficient space error:

- If you manually scale down a core instance group or instance fleet when there isn't enough
  HDFS space on the remaining nodes for data replication prior to the scale down.
- Managed scaling or autoscaling scales down a core instance group or instance fleet
  when there isn't enough HDFS space for data replication.
- Amazon EMR attempts to replace an unhealthy core node but is unable to safely replace the node
  due to insufficient HDFS space.

## Solutions and best practices

See the following for solutions and best practices:

- Scale up the number of core nodes in your Amazon EMR cluster. If you use
  managed scaling or autoscaling, increase the minimum capacity of your core nodes.
- Use larger EBS volumes for your core nodes when you create your EMR cluster.
- Delete unneeded HDFS data in your EMR cluster. We recommend that you set up
  CloudWatch alarms to monitor the `HDFSUtilization` metric in your cluster
  to know if your EMR cluster is low on space.
