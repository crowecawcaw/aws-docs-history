# REL07-BP03 Obtain resources upon detection that more resources

are needed for a workload

One of the most valuable features of cloud computing is the ability
to provision resources dynamically.

In traditional on-premises compute environments, you must identify
and provision enough capacity in advance to serve peak demand. This
is a problem because it is expensive and because it poses risks to
availability if you underestimate the workload's peak capacity
needs.

In the cloud, you don't have to do this. Instead, you can provision
compute, database, and other resource capacity as needed to meet
current and forecasted demand. Automated solutions such as Amazon EC2 Auto Scaling and Application Auto Scaling can bring resources
online for you based on metrics you specify. This can make the
scaling process easier and predictable, and it can make your
workload significantly more reliable by ensuring you have enough
resources available at all times.

**Desired outcome**: You configure
automatic scaling of compute and other resources to meet demand. You
provide sufficient headroom in your scaling policies to allow bursts
of traffic to be served while additional resources are brought
online.

**Common anti-patterns:**

- You provision a fixed number of scalable resources.
- You choose a scaling metric that does not correlate to actual
  demand.
- You fail to provide enough headroom in your scaling plans to
  accommodate demand bursts.
- Your scaling policies add capacity too late, which leads to
  capacity exhaustion and degraded service while additional
  resources are brought online.
- You fail to correctly configure minimum and maximum resource
  counts, which leads to scaling failures.

**Benefits of establishing this best
practice:** Having enough resources to meet current demand
is critical to provide high availability of your workload and adhere
to your defined service-level objectives (SLOs). Automatic scaling
allows you to provide the right amount of compute, database, and
other resources your workload needs in order to serve current and
forecasted demand. You don't need to determine peak capacity needs
and statically allocate resources to serve it. Instead, as demand
grows, you can allocate more resources to accommodate it, and after
demand falls, you can deactivate resources to reduce cost.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

First, determine whether the workload component is suitable for
automatic scaling. These components are called
_horizontally scalable_ because they provide
the same resources and behave identically. Examples of
horizontally-scalable components include EC2 instances that are
configured alike,
[Amazon Elastic Container Service (ECS)](https://aws.amazon.com/ecs/ "https://aws.amazon.com/ecs/") tasks, and pods running on
[Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/ "https://aws.amazon.com/eks/"). These compute resources are
typically located behind a load balancer and are referred to as
_replicas_.

Other replicated resources may include database read replicas,
[Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") tables, and
[Amazon ElastiCache](https://aws.amazon.com/elasticache/ "https://aws.amazon.com/elasticache/") (Redis OSS) clusters. For a complete list of
supported resources, see
[AWS services that you can use with Application Auto Scaling](../../../autoscaling/application/userguide/integrated-services-list.md "../../../autoscaling/application/userguide/integrated-services-list.md").

For container-based architectures, you may need to scale two
different ways. First, you may need to scale the containers that
provide horizontally-scalable services. Second, you may need to
scale the compute resources to make space for new containers.
Different automatic scaling mechanisms exist for each layer. To
scale ECS tasks, you can use
[Application
Auto Scaling](../../../AmazonECS/latest/developerguide/service-auto-scaling.md "../../../AmazonECS/latest/developerguide/service-auto-scaling.md"). To scale Kubernetes pods, you can use
[Horizontal
Pod Autoscaler (HPA)](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/ "https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/") or
[Kubernetes Event-driven
Autoscaling (KEDA)](https://keda.sh/ "https://keda.sh/"). To scale the compute resources, you can
use
[Capacity
Providers](../../../AmazonECS/latest/developerguide/asg-capacity-providers.md "../../../AmazonECS/latest/developerguide/asg-capacity-providers.md") for ECS, or for Kubernetes, you can use
[Karpenter](https://karpenter.sh "https://karpenter.sh") or
[Cluster
Autoscaler](https://kubernetes.io/docs/concepts/cluster-administration/cluster-autoscaling/ "https://kubernetes.io/docs/concepts/cluster-administration/cluster-autoscaling/").

Next, select how you will perform automatic scaling. There are
three major options: metric-based scaling, scheduled scaling, and
predictive scaling.

**Metric-based scaling**

Metric-based scaling provisions resources based on the value of
one or more _scaling metrics_. A scaling metric
is one that corresponds to your workload's demand. A good way to
determine appropriate scaling metrics is to perform load testing
in a non-production environment. During your load tests, keep the
number of scalable resources fixed, and slowly increase demand
(for example, throughput, concurrency, or simulated users). Then
look for metrics that increase (or decrease) as demand grows, and
conversely decrease (or increase) as demand falls. Typical scaling
metrics include CPU utilization, work queue depth (such as an
[Amazon SQS](https://aws.amazon.com/sqs/ "https://aws.amazon.com/sqs/")
queue), number of active users, and network throughput.

###### Note

AWS has observed that
with most applications, memory utilization increases as the
application warms up and then reaches a steady value. When demand
decreases, memory utilization typically remains elevated rather
than decreasing in parallel. Because memory utilization does not
correspond to demand in both directions–that is, growing and
falling with demand–consider carefully before you select this
metric for automatic scaling.

Metric-based scaling is a _latent operation_.
It can take several minutes for utilization metrics to propagate
to auto scaling mechanisms, and these mechanisms typically wait
for a clear signal of increased demand before reacting. Then, as
the auto scaler creates new resources, it can take additional time
for them to come to full service. Because of this, it is important
to not set your scaling metric targets too close to full
utilization (for example, 90% CPU utilization). Doing so risks
exhausting existing resource capacity before additional capacity
can come online. Typical resource utilization targets can range
between 50-70% for optimum availability, depending on demand
patterns and time required to provision additional resources.

**Scheduled scaling**

Scheduled scaling provisions or removes resources based on the
calendar or time of day. It is frequently used for workloads that
have predictable demand, such as peak utilization during weekday
business hours or sales events. Both
[Amazon EC2 Auto Scaling](../../../autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.md "../../../autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.md") and
[Application
Auto Scaling](../../../autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.md "../../../autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.md") support scheduled scaling. KEDA's
[cron
scaler](https://keda.sh/docs/latest/scalers/cron/ "https://keda.sh/docs/latest/scalers/cron/") supports scheduled scaling of Kubernetes pods.

**Predictive scaling**

Predictive scaling uses machine learning to automatically scale
resources based on anticipated demand. Predictive scaling analyzes
the historical value of a utilization metric you provide and
continuously predicts its future value. The predicted value is
then used to scale the resource up or down.
[Amazon EC2 Auto Scaling](../../../autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.md "../../../autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.md") can perform predictive scaling.

### Implementation steps

1. Determine whether the workload component is suitable for
   automatic scaling.
2. Determine what kind of scaling mechanism is most appropriate
   for the workload: metric-based scaling, scheduled scaling,
   or predictive scaling.
3. Select the appropriate automatic scaling mechanism for the
   component. For Amazon EC2 instances, use Amazon EC2 Auto Scaling. For other AWS services, use Application Auto
   Scaling. For Kubernetes pods (such as those running in an
   Amazon EKS cluster), consider Horizontal Pod Autoscaler
   (HPA) or Kubernetes Event-driven Autoscaling (KEDA). For
   Kubernetes or EKS nodes, consider Karpenter and Cluster Auto
   Scaler (CAS).
4. For metric or scheduled scaling, conduct load testing to
   determine the appropriate scaling metrics and target values
   for your workload. For scheduled scaling, determine the
   number of resources needed at the dates and times you
   select. Determine the maximum number of resources needed to
   serve expected peak traffic.
5. Configure the auto scaler based on the information collected
   above. Consult the auto scaling service's documentation for
   details. Verify that the maximum and minimum scaling limits
   are configured correctly.
6. Verify the scaling configuration is working as expected.
   Perform load testing in a non-production environment and
   observe how the system reacts, and adjust as needed. When
   enabling auto scaling in production, configure appropriate
   alarms to notify you of any unexpected behavior.

## Resources

**Related documents:**

- [What
  Is Amazon EC2 Auto Scaling?](../../../autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.md "../../../autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.md")
- [AWS Prescriptive Guidance: Load testing applications](../../../prescriptive-guidance/latest/load-testing.md "../../../prescriptive-guidance/latest/load-testing.md")
- [AWS Marketplace: products that can be used with auto
  scaling](https://aws.amazon.com/marketplace/search/results?searchTerms=Auto+Scaling "https://aws.amazon.com/marketplace/search/results?searchTerms=Auto+Scaling")
- [Managing
  Throughput Capacity Automatically with DynamoDB Auto
  Scaling](../../../amazondynamodb/latest/developerguide/AutoScaling.md "../../../amazondynamodb/latest/developerguide/AutoScaling.md")
- [Predictive
  Scaling for EC2, Powered by Machine Learning](https://aws.amazon.com/blogs/aws/new-predictive-scaling-for-ec2-powered-by-machine-learning/ "https://aws.amazon.com/blogs/aws/new-predictive-scaling-for-ec2-powered-by-machine-learning/")
- [Scheduled
  Scaling for Amazon EC2 Auto Scaling](../../../autoscaling/ec2/userguide/schedule_time.md "../../../autoscaling/ec2/userguide/schedule_time.md")
- [Telling
  Stories About Little's Law](https://brooker.co.za/blog/2018/06/20/littles-law.html "https://brooker.co.za/blog/2018/06/20/littles-law.html")
