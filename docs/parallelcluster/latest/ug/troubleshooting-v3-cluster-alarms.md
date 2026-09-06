

# Cluster alarms
<a name="troubleshooting-v3-cluster-alarms"></a>

Cluster health monitoring is essential for ensuring optimal performance. AWS ParallelCluster enables you to monitor multiple CloudWatch based alarms for the cluster's head node. 

This section provides detail for each type of Head node cluster alarms including its naming conventions, specific conditions that trigger alarms, and suggested troubleshooting steps.

The naming convention for cluster alarms is `CLUSTER_NAME-COMPONENT-METRIC`, e.g. `mycluster-HeadNode-Cpu`.
+ `CLUSTER_NAME-HeadNode`: signals the overall status of the head node. It is red if at least one of the alarms below is.
+ `CLUSTER_NAME-HeadNode-Health`: red if there is at least one Amazon EC2 Health Check failure. In case of alarm, we suggest having a look at [Troubleshoot instances with failed status checks](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstances.html).
+ `CLUSTER_NAME-HeadNode-Cpu`: red if CPU utilization is greater than 90%. In case of alarm, check the processes that are consuming the CPU the most with `ps -aux --sort=-%cpu | head -n 10`.
+ `CLUSTER_NAME-HeadNode-Mem`: red if memory utilization is greater than 90%. In case of alarm, check the processes that are consuming the memory the most with `ps -aux --sort=-%mem | head -n 10`.
+ `CLUSTER_NAME-HeadNode-Disk`: red if the occupied disk space is greater than 90% on path /. In case of alarm, check the folders consuming the majority of the space with `du -h --max-depth=2 / 2> /dev/null | sort -hr`.