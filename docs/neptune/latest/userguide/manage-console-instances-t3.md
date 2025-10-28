# Neptune T3 Burstable Instance Class

In addition to fixed-performance instance classes such as `R5` and `R6`,
Amazon Neptune gives you the option of using a burstable-performance `T3` instance.
While you’re developing your graph application, you want your database to be fast
and responsive, but you don't need to use it all the time. Neptune's `db.t3.medium`
instance class is just what you should use in that situation, at significantly lower cost than
the least expensive fixed-performance instance class.

A burstable instance runs at a baseline level of CPU performance until a workload needs more,
and then bursts well above the baseline for as long as a workload requires. Its hourly price
covers the bursts, provided that the average CPU utilization doesn't exceed the baseline over
a 24-hour period. For most development and test situations, that translates to good performance
at a low cost.

If you start with a `T3` instance class, you can easily switch later to a
fixed-performance instance class when you’re ready to go into production, using the AWS Management Console,
AWS CLI, or one of the AWS SDKs.

## T3 Bursting Is Governed by CPU Credits

A CPU credit represents the full utilization of one virtual CPU core (vCPU) for one minute.
That can also translate into 50% utilization of a vCPU for two minutes, or 25% utilization of two
vCPUs for two minutes, and so on.

A `T3` instance accrues CPU credits when it's idle and uses them up when it's
active, both measured at millisecond resolution. The `db.t3.medium` instance class
has two vCPUs, each of which earns 12 CPU credits per hour when idle. This means that 20%
utilization of each vCPU results in a zero CPU credit balance. The 12 CPU credits earned are
spent by 20% utilization of the vCPU (since 20% of 60 minutes is also 12). This 20% utilization
is thus the _baseline_ utilization rate that produces neither a positive
nor negative CPU-credit balance.

Idle time (CPU utilization below 20% of the total available) causes CPU credits to
be stored in a credit balance bucket, up to the limit for a `db.t3.medium`
instance class of 576 (the maximum number of CPU credits that could be accrued in 24
hours, namely 2 x 12 x 24). Over that limit, CPU credits are simply discarded.

When necessary, CPU utilization can burst to as high as 100% for as long as needed
by a workload, even after the CPU credit balance falls below zero. If the instance
sustains a negative balance continuously for 24 hours, it incurs an additional charge of
$0.05 for every -60 CPU credits accrued over that period. For most development
and test workloads, however, bursting is usually covered by idle time before or after
the burst.

###### Note

Neptune's `T3` instance class is configured like the Amazon EC2
[unlimited
mode](../../../AWSEC2/latest/UserGuide/burstable-performance-instances-unlimited-mode.md "../../../AWSEC2/latest/UserGuide/burstable-performance-instances-unlimited-mode.md").

## Using the AWS Management Console to Create a T3 Burstable Instance

In the AWS Management Console, you can create a primary DB cluster instance or a
read-replica instance that uses the `db.t3.medium` instance class, or
you can modify an existing instance to use the `db.t3.medium` instance
class.

For example, to create a new DB cluster primary instance in the Neptune console:

- Choose
  **Create Database**.
- Choose a **DB engine version** equal to or later
  than `1.0.2.2`.
- Under **Purpose**, choose **Development
  and Testing**.
- As the **DB instance class**, accept the default:
  `db.t3.medium — 2 vCPU, 4 GiB RAM`.

## Using the AWS CLI to Create a T3 Burstable Instance

You can also use the AWS CLI to do the same thing:

```
aws neptune create-db-cluster \
    --db-cluster-identifier `(name for a new DB cluster)` \
    --engine neptune \
    --engine-version "1.0.2.2"

aws neptune create-db-instance \
    --db-cluster-identifier `(name of the new DB cluster)` \
    --db-instance-identifier `(name for the primary writer instance in the cluster)` \
    --engine neptune \
    --db-instance-class db.t3.medium
```
