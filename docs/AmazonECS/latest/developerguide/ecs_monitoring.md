# Monitoring Amazon ECS

Monitoring is an important part of maintaining the reliability, availability, and
performance of Amazon ECS and your AWS solutions. You should collect monitoring data from all
of the parts of your AWS solution so that you can more easily debug a multi-point failure
if one occurs. Before you start monitoring Amazon ECS, create a monitoring plan that includes
answers to the following questions:

- What are your monitoring goals?
- What resources will you monitor?
- How often will you monitor these resources?
- What monitoring tools will you use?
- Who will perform the monitoring tasks?
- Who should be notified when something goes wrong?
  The metrics made available depend on the compute option of the tasks and services in your
  clusters. If you are using Fargate for your services, then CPU
  and memory utilization metrics are provided to assist in the monitoring of your services.
  For EC2, you own and need to monitor the EC2 instances that make your
  underlying infrastructure. Additional CPU and memory reservation and utilization metrics are
  made available at the cluster, service, and task.

The next step is to establish a baseline for normal Amazon ECS performance in your environment,
by measuring performance at various times and under different load conditions. As you
monitor Amazon ECS, store historical monitoring data so that you can compare it with current
performance data, identify normal performance patterns and performance anomalies, and devise
methods to address issues.

To establish a baseline you should, at a minimum, monitor the following
items:

- The CPU and memory reservation and utilization metrics for your Amazon ECS
  clusters
- The CPU and memory utilization metrics for your Amazon ECS services

For more information, see [Viewing Amazon ECS metrics](viewing_cloudwatch_metrics.md "viewing_cloudwatch_metrics.md").
