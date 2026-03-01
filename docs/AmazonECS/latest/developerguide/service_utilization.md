# Amazon ECS service utilization metrics

The service utilization metrics are available for CPU, memory, and, when there is an
EBS volume attached to your tasks, EBS filesystem utilization. The service level metrics
are supported for services with tasks hosted on both Amazon EC2 instances and
Fargate.

## Service level CPU and memory utilization

The CPU and memory utilization is measured as the percentage of CPU and memory
that is used by the Amazon ECS tasks that belong to a service on a cluster when compared
to the CPU and memory that is specified in the service's task definition.

When viewing these metrics in CloudWatch, you can choose different statistics:

- **Average**: The average utilization across all tasks in the service. This is calculated using the formula below.
- **Minimum**: The utilization of the task with the lowest resource usage in the service. This represents the percentage of CPU or memory used by the least resource-intensive task compared to what was specified in the task definition.
- **Maximum**: The utilization of the task with the highest resource usage in the service. This represents the percentage of CPU or memory used by the most resource-intensive task compared to what was specified in the task definition.

The following formulas show how the Average statistic is calculated:

```
                                  (Total CPU units used by tasks in service) x 100
Service CPU utilization =  --------------------------------------------------------------
                           (Total CPU units specified in the task definition) x (Number of tasks in the service)
```

```
                                     (Total MiB of memory used by tasks in service x 100)
Service memory utilization =  ------------------------------------------------------------------
                              (Total MiB of memory specified in the task definition)  x (Number of tasks in the service)
```

###### Note

The formulas above apply only to the Average statistic. The Minimum and Maximum statistics represent the individual task with the lowest and highest resource utilization, respectively, rather than an aggregate calculation across all tasks.

Amazon ECS collects metrics every 20 seconds. Each minute, the Amazon ECS container agent
calculates the number of CPU units and MiB of memory that are currently being used
for each running task owned by the service. This information is reported back to
Amazon ECS. The total amount of CPU and memory used for all tasks owned by the service
that are running on the cluster is calculated, and those numbers are reported to
CloudWatch as a percentage of the total resources that are specified for the service in
the service's task definition. The minimum and maximum values are the smallest and
largest of the 20 second metrics. The average is the aggregate of the 3
values.

If you specify a soft limit (`memoryReservation`), it's used to
calculate the amount of reserved memory. Otherwise, the hard limit
(`memory`) is used. For more information about hard and soft limits,
see [Task size](task_definition_parameters.md#task_size "task_definition_parameters.md#task_size").

For example, the task definition for a service specifies a total of 512 CPU units
and 1,024 MiB of memory (with the hard limit `memory` parameter) for all
of its containers. The service has a desired count of 1 running task, the service is
running on a cluster with 1 `c4.large` container instance (with 2,048 CPU
units and 3,768 MiB of total memory), and there are no other tasks running on the
cluster. Although the task specifies 512 CPU units, because it is the only running
task on a container instance with 2,048 CPU units, it can use up to four times the
specified amount (2,048 / 512). However, the specified memory of 1,024 MiB is a hard
limit and it can't be exceeded, so in this case, service memory utilization can't
exceed 100%.

If the previous example used the soft limit `memoryReservation` instead
of the hard limit `memory` parameter, the service's tasks could use more
than the specified 1,024 MiB of memory as needed. In this case, the service's memory
utilization could exceed 100%.

If your application has a sudden spike in memory utilization for a short amount of
time, you will not see the service memory utilization increasing because Amazon ECS
collects multiple data points every minute, and then aggregates them to one data
point that is sent to CloudWatch.

If this task is performing CPU-intensive work during a period and using all 2,048
of the available CPU units and 512 MiB of memory, the service reports 400% CPU
utilization and 50% memory utilization. If the task is idle and using 128 CPU units
and 128 MiB of memory, the service reports 25% CPU utilization and 12.5% memory
utilization.

###### Note

In this example, the CPU utilization will only go above 100% when the CPU
units are defined at the container level. If you define CPU units at the task
level, the utilization will not go above the defined task-level limit.

## Service level EBS filesystem utilization

The service level EBS filesystem utilization is measured as the total amount of
the EBS filesystem in use by the tasks that belong to the service, divided by the
total amount of EBS filesystem storage that is allocated for all tasks that belong
to the service.

## Service `RUNNING` task count

You can use CloudWatch metrics to view the number of tasks in your services that are in the
`RUNNING` state. For example, you can set a CloudWatch alarm for this metric to
alert you if the number of running tasks in your service falls below a specified
value.

### Service `RUNNING` task count in Amazon ECS CloudWatch Container Insights

A "Number of Running Tasks" (`RunningTaskCount`) metric is available
per cluster and per service when you use Amazon ECS CloudWatch Container Insights. You can use Container Insights for
all new clusters created by opting in to the `containerInsights` account
setting, on individual clusters by turning on the cluster settings during cluster
creation, or on existing clusters by using the UpdateClusterSettings API. Metrics
collected by CloudWatch Container Insights are charged as custom metrics. For more information about
CloudWatch pricing, see [CloudWatch
Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

To view this metric, see [Amazon ECS Container Insights Metrics](../../../AmazonCloudWatch/latest/monitoring/Container-Insights-view-metrics.md "../../../AmazonCloudWatch/latest/monitoring/Container-Insights-view-metrics.md") in the
_Amazon CloudWatch User Guide_.
