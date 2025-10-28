# Using Amazon Neptune Serverless

You can create a new Neptune DB cluster as a serverless one, or in some cases
you can convert an existing DB cluster to use serverless. You can also convert DB
instances in a serverless DB cluster to and from serverless instances. You can only use
Neptune Serverless in one of the AWS Regions where it's supported, with
a few other limitations (see [Amazon Neptune Serverless constraints](neptune-serverless.md#neptune-serverless-limitations "neptune-serverless.md#neptune-serverless-limitations")).

You can also use the [Neptune AWS CloudFormation
stack](get-started-cfn-create.md "get-started-cfn-create.md") to create a Neptune Serverless DB cluster.

## Creating a new DB cluster that uses Serverless

To create a Neptune DB cluster that uses serverless, you can do so
[using the AWS Management Console](manage-console-launch-console.md "manage-console-launch-console.md") the same
way you do to create a provisioned cluster. The difference is that under **DB
instance size**, you need to set the **DB instance class**
to **serverless**. When you do that, you then need to [set the serverless capacity range](neptune-serverless-capacity-scaling.md "neptune-serverless-capacity-scaling.md")
for the cluster.

You can also create a serverless DB cluster using the AWS CLI with commands
like this (on Windows, replace '\' with '^'):

```
aws neptune create-db-cluster \
  --region `(an AWS Region region that supports serverless)` \
  --db-cluster-identifier `(ID for the new serverless DB cluster)` \
  --engine neptune \
  --engine-version `(optional: 1.2.0.1 or above)` \
  --serverless-v2-scaling-configuration "MinCapacity=`1.0`, MaxCapacity=`128.0`"
```

You could also specify the `serverless-v2-scaling-configuration`
parameter like this:

```
  --serverless-v2-scaling-configuration '{"MinCapacity":`1.0`, "MaxCapacity":`128.0`}'
```

You can then run the `describe-db-clusters` command for the
`ServerlessV2ScalingConfiguration` attribute, which should return the
capacity range settings you specified:

```
"ServerlessV2ScalingConfiguration": {
    "MinCapacity": `(the specified minimum number of NCUs)`,
    "MaxCapacity": `(the specified maximum number of NCUs)`
}
```

## Converting an existing DB cluster or instance to Serverless

If you have a Neptune DB cluster that is using engine version 1.2.0.1 or above,
you can convert it to be serverless. This process does incur some downtime.

The first step is to add a capacity range to the existing cluster. You can do
so using the AWS Management Console, or by using a AWS CLI command like this (on Windows, replace '\'
with '^'):

```
aws neptune modify-db-cluster \
  --db-cluster-identifier `(your DB cluster ID)` \
  --serverless-v2-scaling-configuration \
      MinCapacity=`(minimum number of NCUs, such as 2.0)`, \
      MaxCapacity=`(maximum number of NCUs, such as 24.0)`
```

The next step is to create a new serverless DB instance to replace the existing
primary instance (the writer) in the cluster. Again, you can do this and all
the subsequent steps using either the AWS Management Console or the AWS CLI. In either case,
specify the DB instance class as serverless. The AWS CLI command would look like
this (on Windows, replace '\' with '^'):

```
aws neptune create-db-instance \
  --db-instance-identifier `(an instance ID for the new writer instance)` \
  --db-cluster-identifier `(ID of the DB cluster)` \
  --db-instance-class db.serverless
  --engine neptune
```

When the new writer instance has become available, perform a failover to make it
the writer instance for the cluster:

```
aws neptune failover-db-cluster \
  --db-cluster-identifier `(ID of the DB cluster)` \
  --target-db-instance-identifier `(instance ID of the new serverless instance)`
```

Next, delete the old writer instance:

```
aws neptune delete-db-instance \
  --db-instance-identifier `(instance ID of the old writer instance)` \
  --skip-final-snapshot
```

Finally, do the same thing to create a new serverless instance to take the
place of each existing provisioned reader instance that you would like to
turn into a serverless instance, and delete the existing provisioned instances
(no failover is needed for reader instances).

## Modifying the capacity range of an

existing serverless DB cluster

You can change the capacity range of a Neptune Serverless DB cluster using the
AWS CLI like this (on Windows, replace '\' with '^'):

```
aws neptune modify-db-cluster \
  --region `(an AWS region that supports serverless)` \
  --db-cluster-identifier `(ID of the serverless DB cluster)` \
  --apply-immediately \
  --serverless-v2-scaling-configuration MinCapacity=`4.0`, MaxCapacity=`32`
```

Changing the capacity range causes changes to the default values of some
configuration parameters. Neptune can apply some of those new defaults immediately,
but some of the dynamic parameter changes take effect only after a reboot. A
status of `pending-reboot` indicates that you need a reboot to apply
some parameter changes.

## Changing a Serverless DB instance to provisioned

All you need to do to convert a Neptune Serverless instance to a provisioned one
is to change its instance class to one of the provisioned instance classes. See [Modifying a Neptune DB Instance (and
Applying Immediately)](manage-console-instances-modify.md "manage-console-instances-modify.md").

## Monitoring serverless capacity with Amazon CloudWatch

You can use CloudWatch to to monitor the capacity and utilization of the Neptune
serverless instances in your DB cluster. There are two CloudWatch metrics that let you track
current serverless capacity both at the cluster level and at the instance level:

- **`ServerlessDatabaseCapacity`**   –  
  As an instance-level metric, `ServerlessDatabaseCapacity` reports the
  current instance capacity, in NCUs. As a cluster-level metric, it reports the average
  of all the `ServerlessDatabaseCapacity` values of all the DB instances in
  the cluster.
- **`NCUUtilization`**   –  
  This metric reports the percentage of possible capacity being used. It is calculated
  as the current `ServerlessDatabaseCapacity` (either at the instance level
  or at the cluster level) divided by the maximum capacity setting for the DB cluster.

If this metric approaches 100% at a cluster level, meaning that the cluster has
scaled as high as it can, consider increasing the maximum capacity setting.

If it approaches 100% for a reader instance while the writer instance is not
near maximum capacity, consider adding more reader instances to distribute the read
workload.

Note that the `CPUUtilization` and `FreeableMemory` metrics
have slightly different meanings for serverless instances than for provisioned
instances. In a serverless context, `CPUUtilization` is a percentage
that's calculated as the amount of CPU currently being used divided by the amount
of CPU that would be available at maximum capacity. Similarly, `FreeableMemory`
reports the amount of freeable memory that would be available if an instance was at
maximum capacity.

The following example shows how to use the AWS CLI on Linux to retrieve the minimum,
maximum, and average capacity values for a given DB instance, measured every 10 minutes
over one hour. The Linux `date` command specifies the start and end times relative
to the current date and time. The `sort_by` function in the `--query`
parameter sorts the results chronologically based on the `Timestamp` field:

```
aws cloudwatch get-metric-statistics \
  --metric-name "ServerlessDatabaseCapacity" \
  --start-time "$(date -d '1 hour ago')" \
  --end-time "$(date -d 'now')" \
  --period 600 \
  --namespace "AWS/Neptune"
  --statistics Minimum Maximum Average \
  --dimensions Name=DBInstanceIdentifier,Value=`(instance ID)` \
  --query 'sort_by(Datapoints[*].{min:Minimum,max:Maximum,avg:Average,ts:Timestamp},&ts)' \
  --output table
```
