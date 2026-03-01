# Amazon ECS cluster utilization metrics

The cluster utilization metrics are available for CPU, memory, and, when there is an
EBS volume attached to your tasks, EBS filesystem utilization. These metrics are only
available for clusters with tasks or services hosted on Amazon EC2 instances. They're not
supported on clusters with tasks hosted on AWS Fargate.

## Amazon ECS cluster level CPU and memory utilization metrics

The CPU and memory utilization is measured as the percentage of CPU and memory
that is used by all tasks on a cluster when compared to the aggregate CPU and memory
that was registered for each active Amazon EC2 instances registered to the cluster. Only
Amazon EC2 instances in `ACTIVE` or `DRAINING` status will affect
cluster utilization metrics.

```
                                  (Total CPU units used by tasks in cluster) x 100
Cluster CPU utilization =  --------------------------------------------------------------
                           (Total CPU units registered by container instances in cluster)
```

```
                                     (Total MiB of memory used by tasks in cluster x 100)
Cluster memory utilization =  ------------------------------------------------------------------
                              (Total MiB of memory registered by container instances in cluster)
```

Each minute, the Amazon ECS container agent on each Amazon EC2 instance calculates the
number of CPU units and MiB of memory that is currently being used for each task
that is running on that Amazon EC2 instance, and this information is reported back to
Amazon ECS. The total amount of CPU and memory used for all tasks running on the cluster
is calculated, and those numbers are reported to CloudWatch as a percentage of the total
registered resources for the cluster.

For example, a cluster has two active Amazon EC2 instances registered, a
`c4.4xlarge` instance and a `c4.large` instance. The
`c4.4xlarge` instance registers into the cluster with
`16,384` CPU units and `30,158` MiB of memory. The
`c4.large` instance registers with `2,048` CPU units and
`3,768` MiB of memory. The aggregate resources of this cluster are
`18,432` CPU units and `33,926` MiB of memory.

If ten tasks are running on this cluster and each task consumes `1,024`
CPU units and `2,048` MiB of memory, a total of `10,240` CPU
units and `20,480` MiB of memory are used on the cluster. This is
reported to CloudWatch as 55% CPU utilization and 60% memory utilization for the
cluster.

## Amazon ECS cluster-level Amazon EBS filesystem utilization

The cluster level EBS filesystem utilization metric is measured as the total
amount of the EBS filesystem in use by the tasks running on the cluster, divided by
the total amount of EBS filesystem storage that was allocated for all of the tasks
in the cluster.

```
                                       (Total GB of EBS filesystem used by tasks in cluster x 100)
Cluster EBS filesystem utilization =  ---------------------------------------------------------------
                                       (Total GB of EBS filesystem allocated to tasks in cluster)
```
