# Availability Zone

flexibility for an Amazon EMR cluster

Each AWS Region has multiple, isolated locations known as Availability Zones. When
you launch an instance, you can optionally specify an Availability Zone (AZ) in the
AWS Region that you use. [Availability Zone
flexibility](#emr-flexibility-az "#emr-flexibility-az") is the distribution of instances across multiple AZs. If
one instance fails, you can design your application so that an instance in
another AZ can handle requests. For more information on Availability Zones, see the
[Region and zones](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-availability-zones "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-availability-zones") documentation in the _Amazon EC2 User
Guide_.

[Instance flexibility](#emr-flexibility-types "#emr-flexibility-types") is the use
of multiple instance types to satisfy capacity requirements. When you express
flexibility with instances, you can use aggregate capacity across instance
sizes, families, and generations. Greater flexibility improves the chance to
find and allocate your required amount of compute capacity when compared with a
cluster that uses a single instance type.

Instance and Availability Zone flexibility reduces [insufficient capacity errors
(ICE)](emr-events-response-insuff-capacity.md "emr-events-response-insuff-capacity.md") and Spot interruptions when compared to a cluster with a single
instance type or AZ. Use the best practices covered here to determine which
instances to diversify after you know the initial instance family and size. This
approach maximizes availability to Amazon EC2 capacity pools with minimal performance
and cost variance.

## Being flexible about Availability Zones

We recommend that you configure all Availability Zones for use in your virtual
private cloud (VPC) and that you select them for your EMR cluster.
Clusters must exist in only one Availability Zone, but with Amazon EMR instance fleets,
you can select multiple subnets for different Availability Zones. When Amazon EMR
launches the cluster, it looks across those subnets to find the instances
and purchasing options that you specify. When you provision an EMR cluster
for multiple subnets, your cluster can access a deeper Amazon EC2 capacity pool
when compared to clusters in a single subnet.

If you must prioritize a certain number of Availability Zones for use in your
virtual private cloud (VPC) for your EMR cluster, you can leverage the
Spot placement score capability with Amazon EC2. With Spot placement scoring, you
specify the compute requirements for your Spot Instances, then EC2 returns
the top ten AWS Regions or Availability Zones scored on a scale from 1 to 10. A
score of 10 indicates that your Spot request is highly likely to succeed; a
score of 1 indicates that your Spot request is not likely to succeed. For
more information on how to use Spot placement scoring, see [Spot placement
score](../../../AWSEC2/latest/UserGuide/spot-placement-score.md "../../../AWSEC2/latest/UserGuide/spot-placement-score.md") in the _Amazon EC2 User Guide_.

## Being flexible about instance types

Instance flexibility is the use of multiple instance types to satisfy
capacity requirements. Instance flexibility benefits both Amazon EC2 Spot and
On-Demand Instance usage. With Spot Instances, instance flexibility lets
Amazon EC2 launch instances from deeper capacity pools using real-time capacity
data. It also predicts which instances are most available. This offers fewer
interruptions and can reduce the overall cost of a workload. With On-Demand
Instances, instance flexibility reduces insufficient capacity errors (ICE)
when total capacity provisions across a greater number of instance
pools.

For **Instance Group** clusters, you can specify up to 50
EC2 instance types. For **Instance Fleets** with allocation
strategy, you can specify up to 30 EC2 instance types for each primary,
core, and task node group. A broader range of instances improves the
benefits of instance flexibility.

### Expressing instance

flexibility

Consider the following best practices to express instance flexibility
for your application.

###### Topics

- [Determine instance
  family and size](#emr-flexibility-express-size "#emr-flexibility-express-size")
- [Include additional
  instances](#emr-flexibility-express-include "#emr-flexibility-express-include")

#### Determine instance

family and size

Amazon EMR supports several instance types for different use cases.
These instance types are listed in the [Supported instance types with Amazon EMR](emr-supported-instance-types.md "emr-supported-instance-types.md") documentation.
Each instance type belongs to an instance family that describes what
application the type is optimized for.

For new workloads, you should benchmark with instance types in the
general purpose family, such as `m5` or `c5`.
Then, monitor the OS and YARN metrics from Ganglia and
Amazon CloudWatch to determine system bottlenecks at peak
load. Bottlenecks include CPU, memory, storage, and I/O operations.
After you identify the bottlenecks, choose compute optimized, memory
optimized, storage optimized, or another appropriate instance family
for your instance types. For more details, see the [Determine right infrastructure for your Spark workloads](https://github.com/aws/aws-emr-best-practices/blob/main/website/docs/bestpractices/Applications/Spark/best_practices.md#bp-512-----determine-right-infrastructure-for-your-spark-workloads "https://github.com/aws/aws-emr-best-practices/blob/main/website/docs/bestpractices/Applications/Spark/best_practices.md#bp-512-----determine-right-infrastructure-for-your-spark-workloads")
page in the Amazon EMR best practices guide on GitHub.

Next, identify the smallest YARN container or Spark executor that
your application requires. This is the smallest instance size that
fits the container and the minimum instance size for the cluster.
Use this metric to determine instances that you can further
diversify with. A smaller instance will allow for more instance
flexibility.

For maximum instance flexibility, you should leverage as many
instances as possible. We recommend that you diversify with
instances that have similar hardware specifications. This maximizes
access to EC2 capacity pools with minimal cost and performance
variance. Diversify across sizes. To do so, prioritize AWS
Graviton and previous generations first. As a general rule, try to
be flexible across at least 15 instance types for each workload. We
recommend that you start with general purpose, compute optimized, or
memory optimized instances. These instance types will provide the
greatest flexibility.

#### Include additional

instances

For maximum diversity, include additional instance types.
Prioritize instance size, Graviton, and generation flexibility
first. This allows access to additional EC2 capacity pools with
similar cost and performance profiles. If you need further
flexibility due to ICE or spot interruptions, consider variant and
family flexibility. Each approach has tradeoffs that depend on your
use case and requirements.

- Size flexibility –
  First, diversify with instances of different sizes within
  the same family. Instances within the same family provide
  the same cost and performance, but can launch a different
  number of containers on each host. For example, if the
  minimum executor size that you need is 2vCPU and 8Gb memory,
  the minimum instance size is `m5.xlarge`. For
  size flexibility, include `m5.xlarge`,
  `m5.2xlarge`, `m5.4xlarge`,
  `m5.8xlarge`, `m5.12xlarge`,
  `m5.16xlarge`, and
  `m5.24xlarge`.
- Graviton flexibility
  – In addition to size, you can diversify with
  Graviton instances. Graviton instances are powered by AWS Graviton2
  processors that deliver the best price performance for cloud
  workloads in Amazon EC2. For example, with the minimum instance
  size of `m5.xlarge`, you can include
  `m6g.xlarge`, `m6g.2xlarge`,
  `m6g.4xlarge`, `m6g.8xlarge`, and
  `m6g.16xlarge` for Graviton
  flexibility.
- Generation flexibility
  – Similar to Graviton and size flexibility, instances
  in previous generation families share the same hardware
  specifications. This results in a similar cost and
  performance profile with an increase in the total accessible
  Amazon EC2 pool. For generation flexibility, include
  `m4.xlarge`, `m4.2xlarge`,
  `m4.10xlarge`, and
  `m4.16xlarge`.
- Family and variant
  flexibility
  - Capacity –
    To optimize for capacity, we recommend instance
    flexibility across instance families. Common
    instances from different instance families have
    deeper instance pools that can assist with meeting
    capacity requirements. However, instances from
    different families will have different vCPU to
    memory ratios. This results in under-utilization if
    the expected application container is sized for a
    different instance. For example, with
    `m5.xlarge`, include compute-optimized
    instances such as `c5` or
    memory-optimized instances such as `r5`
    for instance family flexibility.
  - Cost – To
    optimize for cost, we recommend instance flexibility
    across variants. These instances have the same
    memory and vCPU ratio as the initial instance. The
    tradeoff with variant flexibility is that these
    instances have smaller capacity pools which might
    result in limited additional capacity or higher Spot
    interruptions. With `m5.xlarge` for
    example, include AMD-based instances
    (`m5a`), SSD-based instances
    (`m5d`) or network-optimized instances
    (`m5n`) for instance variant
    flexibility.
