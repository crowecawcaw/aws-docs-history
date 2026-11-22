

# Using Amazon Neptune Serverless

You can create a new Neptune DB cluster as a serverless one, or in some cases you can convert an existing DB cluster to use serverless. You can also convert DB instances in a serverless DB cluster to and from serverless instances. You can only use Neptune Serverless in one of the AWS Regions where it's supported, with a few other limitations (see [Amazon Neptune Serverless constraints](neptune-serverless.md#neptune-serverless-limitations)).

You can also use the [Neptune CloudFormation stack](get-started-cfn-create.md) to create a Neptune Serverless DB cluster.

## Creating a new DB cluster that uses Serverless
<a name="neptune-serverless-create"></a>

To create a Neptune DB cluster that uses serverless, you can do so [using the AWS Management Console](manage-console-launch-console.md) the same way you do to create a provisioned cluster. The difference is that under **DB instance size**, you need to set the **DB instance class** to **serverless**. When you do that, you then need to [set the serverless capacity range](neptune-serverless-capacity-scaling.md) for the cluster.

You can also create a serverless DB cluster using the AWS CLI with commands like this (on Windows, replace '\\' with '^'):

```
aws neptune create-db-cluster \
  --region {{(an AWS Region region that supports serverless)}} \
  --db-cluster-identifier {{(ID for the new serverless DB cluster)}} \
  --engine neptune \
  --engine-version {{(optional: 1.2.0.1 or above)}} \
  --serverless-v2-scaling-configuration "MinCapacity={{1.0}}, MaxCapacity={{128.0}}"
```

You could also specify the `serverless-v2-scaling-configuration` parameter like this:

```
  --serverless-v2-scaling-configuration '{"MinCapacity":{{1.0}}, "MaxCapacity":{{128.0}}}'
```

You can then run the `describe-db-clusters` command for the `ServerlessV2ScalingConfiguration` attribute, which should return the capacity range settings you specified:

```json
"ServerlessV2ScalingConfiguration": {
    "MinCapacity": {{(the specified minimum number of NCUs)}},
    "MaxCapacity": {{(the specified maximum number of NCUs)}}
}
```

## Converting an existing DB cluster or instance to Serverless
<a name="neptune-conversion-to-serverless"></a>

If you have a Neptune DB cluster that is using engine version 1.2.0.1 or above, you can convert it to be serverless. This process does incur some downtime.

The first step is to add a capacity range to the existing cluster. You can do so using the AWS Management Console, or by using a AWS CLI command like this (on Windows, replace '\\' with '^'):

```
aws neptune modify-db-cluster \
  --db-cluster-identifier {{(your DB cluster ID)}} \
  --serverless-v2-scaling-configuration \
      MinCapacity={{(minimum number of NCUs, such as  2.0)}}, \
      MaxCapacity={{(maximum number of NCUs, such as 24.0)}}
```

The next step is to create a new serverless DB instance to replace the existing primary instance (the writer) in the cluster. Again, you can do this and all the subsequent steps using either the AWS Management Console or the AWS CLI. In either case, specify the DB instance class as serverless. The AWS CLI command would look like this (on Windows, replace '\\' with '^'):

```
aws neptune create-db-instance \
  --db-instance-identifier {{(an instance ID for the new writer instance)}} \
  --db-cluster-identifier {{(ID of the DB cluster)}} \
  --db-instance-class db.serverless \
  --engine neptune
```

When the new writer instance has become available, perform a failover to make it the writer instance for the cluster:

```
aws neptune failover-db-cluster \
  --db-cluster-identifier {{(ID of the DB cluster)}} \
  --target-db-instance-identifier {{(instance ID of the new serverless instance)}}
```

Next, delete the old writer instance:

```
aws neptune delete-db-instance \
  --db-instance-identifier {{(instance ID of the old writer instance)}} \
  --skip-final-snapshot
```

Finally, do the same thing to create a new serverless instance to take the place of each existing provisioned reader instance that you would like to turn into a serverless instance, and delete the existing provisioned instances (no failover is needed for reader instances).

## Modifying the capacity range of an existing serverless DB cluster
<a name="neptune-modify-capacity-range"></a>

You can change the capacity range of a Neptune Serverless DB cluster using the AWS CLI like this (on Windows, replace '\\' with '^'):

```
aws neptune modify-db-cluster \
  --region {{(an AWS region that supports serverless)}} \
  --db-cluster-identifier {{(ID of the serverless DB cluster)}} \
  --apply-immediately \
  --serverless-v2-scaling-configuration MinCapacity={{4.0}}, MaxCapacity={{32}}
```

Changing the capacity range causes changes to the default values of some configuration parameters. Neptune can apply some of those new defaults immediately, but some of the dynamic parameter changes take effect only after a reboot. A status of `pending-reboot` indicates that you need a reboot to apply some parameter changes.

## Checking the platform version of a Neptune Serverless DB cluster
<a name="neptune-serverless-platform-version"></a>

Every Neptune Serverless DB cluster runs on a specific *serverless platform version*. The platform version indicates the underlying infrastructure that provides scaling for your DB instances. It is independent from the Neptune database's engine version, and it determines the capacity range that your cluster can use. When you create a new serverless DB cluster, Neptune uses the default platform version.

The capacity range that you can configure for a cluster depends on both the engine version and the platform version. For information about setting the range, see [Capacity scaling in a Neptune Serverless DB cluster](neptune-serverless-capacity-scaling.md).

### Checking the platform version of an existing DB cluster
<a name="neptune-serverless-platform-version-cluster"></a>

The platform version that a DB cluster is using is reported in the `ServerlessV2PlatformVersion` attribute of the DB cluster. You can retrieve it with the `describe-db-clusters` command of the AWS CLI (on Windows, replace '\\' with '^'):

```
aws neptune describe-db-clusters \
  --db-cluster-identifier {{(ID of the serverless DB cluster)}} \
  --query 'DBClusters[*].{ServerlessV2PlatformVersion: ServerlessV2PlatformVersion, ServerlessV2ScalingConfiguration: ServerlessV2ScalingConfiguration}'
```

The output looks like this:

```json
[
    {
        "ServerlessV2PlatformVersion": "1",
        "ServerlessV2ScalingConfiguration": {
            "MinCapacity": 1.0,
            "MaxCapacity": 16.0
        }
    }
]
```

### Listing the available platform versions and the default version
<a name="neptune-serverless-platform-version-list"></a>

Use the `describe-serverless-v2-platform-versions` command to see the details of the available platform versions, or to find the default version that a new cluster receives. To restrict the results to Neptune, specify `--engine neptune`:

```
aws neptune describe-serverless-v2-platform-versions \
  --engine neptune
```

The output looks like this:

```json
{
    "ServerlessV2PlatformVersions": [
        {
            "ServerlessV2PlatformVersion": "4",
            "ServerlessV2PlatformVersionDescription": "Version 4 offering scaling up to 128 NCUs",
            "Engine": "neptune",
            "ServerlessV2FeaturesSupport": {
                "MinCapacity": 1.0,
                "MaxCapacity": 128.0
            },
            "Status": "enabled",
            "IsDefault": true
        },
        {
            "ServerlessV2PlatformVersion": "1",
            "ServerlessV2PlatformVersionDescription": "Version 1 offering scaling up to 128 NCUs",
            "Engine": "neptune",
            "ServerlessV2FeaturesSupport": {
                "MinCapacity": 1.0,
                "MaxCapacity": 128.0
            },
            "Status": "enabled",
            "IsDefault": false
        }
    ]
}
```

Each entry in the list has the following fields:
+ `ServerlessV2PlatformVersion`   –   The platform version number.
+ `ServerlessV2PlatformVersionDescription`   –   A short description of the platform version.
+ `Engine`   –   The database engine that the platform version applies to.
+ `ServerlessV2FeaturesSupport`   –   The `MinCapacity` and `MaxCapacity` values, in NCUs, that the platform version supports.
+ `Status`   –   Either `enabled` or `disabled`.
+ `IsDefault`   –   `true` for the platform version that Neptune assigns to a newly created cluster.

You can narrow or widen the results with these optional parameters:
+ `--serverless-v2-platform-version`   –   Return details only for the specified platform version.
+ `--default-only`   –   Return only the default platform version for each engine.
+ `--include-all`   –   Also return platform versions that are no longer in use.
+ `--max-records` and `--marker`   –   Page through the results. `--max-records` accepts values from 1 to 200, and the default is 20. If more results are available, the response includes a `Marker` value that you pass to `--marker` in the next call.

For example, to find the default platform version for Neptune:

```
aws neptune describe-serverless-v2-platform-versions \
  --engine neptune \
  --default-only
```

**Note**  
The `--filters` parameter is not currently supported.

### Checking for pending platform version upgrades
<a name="neptune-serverless-platform-version-pending"></a>

When a newer platform version is available for a cluster, Neptune makes the upgrade available as a pending maintenance action named `serverless-platform-version-update`. A cluster only has this pending action if it is not already on the latest platform version and it contains at least one `db.serverless` instance.

To check whether a DB cluster has a pending platform version upgrade, use the `describe-pending-maintenance-actions` command and specify the Amazon Resource Name (ARN) of the cluster in the `--resource-identifier` parameter (on Windows, replace '\\' with '^'):

```
aws neptune describe-pending-maintenance-actions \
  --resource-identifier arn:aws:rds:{{us-west-2}}:{{123456789012}}:cluster:{{my-serverless-cluster}}
```

If an upgrade is pending, the output looks like this:

```json
{
    "PendingMaintenanceActions": [
        {
            "ResourceIdentifier": "arn:aws:rds:us-west-2:123456789012:cluster:my-serverless-cluster",
            "PendingMaintenanceActionDetails": [
                {
                    "Action": "serverless-platform-version-update",
                    "Description": "Upgrade to platform version 4"
                }
            ]
        }
    ]
}
```

If the cluster has no pending platform version upgrade, the `PendingMaintenanceActions` list is empty.

### Upgrading the platform version of a DB cluster
<a name="neptune-serverless-platform-version-upgrade"></a>

After you find a pending platform version upgrade, use the `apply-pending-maintenance-action` command to schedule it. Specify the following parameters:
+ `--resource-identifier`   –   The ARN of your Neptune Serverless DB cluster.
+ `--apply-action`   –   Specify `serverless-platform-version-update`.
+ `--opt-in-type`   –   Choose when to apply the upgrade:
  + `immediate`   –   Apply the upgrade now.
  + `next-maintenance`   –   Apply the upgrade during the next maintenance window of the cluster.

For example, to start the upgrade immediately (on Windows, replace '\\' with '^'):

```
aws neptune apply-pending-maintenance-action \
  --resource-identifier arn:aws:rds:{{us-west-2}}:{{123456789012}}:cluster:{{my-serverless-cluster}} \
  --apply-action serverless-platform-version-update \
  --opt-in-type immediate
```

The output confirms the opt-in:

```json
{
    "ResourcePendingMaintenanceActions": {
        "PendingMaintenanceActionDetails": [
            {
                "Action": "serverless-platform-version-update",
                "OptInStatus": "immediate",
                "CurrentApplyDate": "2026-10-28T04:37:14Z",
                "Description": "Upgrade to platform version 4"
            }
        ]
    }
}
```

**Important**  
A platform version upgrade replaces the host that each `db.serverless` instance in the cluster runs on, and the database is unavailable while the host is replaced. In testing, the upgrade of a single-instance cluster took about 10 minutes in total, and the instance was unavailable for about 6 minutes of that time. Plan the upgrade for a time when your application can tolerate the interruption, and make sure your application reconnects after the instance restarts. Your cluster's capacity range (`ServerlessV2ScalingConfiguration`) doesn't change during the upgrade.

While the upgrade is running, the DB cluster and its serverless instances have a status of `upgrading`, and the `ServerlessV2PlatformVersion` of the cluster keeps its old value. You can follow the progress by checking the cluster status:

```
aws neptune describe-db-clusters \
  --db-cluster-identifier {{(ID of the serverless DB cluster)}} \
  --query 'DBClusters[0].{Status:Status,PV:ServerlessV2PlatformVersion}'
```

You can also view the progress as Neptune events for the cluster:

```
aws neptune describe-events \
  --source-type db-cluster \
  --source-identifier {{(ID of the serverless DB cluster)}} \
  --duration 60 \
  --query 'Events[].[Date,Message]' \
  --output text
```

The cluster events include the following messages:
+ `DB cluster serverless platform update starting.`
+ `DB cluster serverless platform update completed. Database cluster is online.`

When the upgrade is complete, the cluster status returns to `available`, the `ServerlessV2PlatformVersion` attribute shows the new platform version, and `describe-pending-maintenance-actions` no longer returns the `serverless-platform-version-update` action for the cluster.

## Changing a Serverless DB instance to provisioned
<a name="neptune-conversion-to-provisioned"></a>

All you need to do to convert a Neptune Serverless instance to a provisioned one is to change its instance class to one of the provisioned instance classes. See [Modifying a Neptune DB Instance (and Applying Immediately)](manage-console-instances-modify.md).

## Configuring Gremlin clients for Serverless
<a name="neptune-serverless-client-config"></a>

When using Gremlin WebSocket clients with Neptune Serverless, you need to configure the client's heartbeat interval appropriately to maintain stable connections during scaling events. For detailed configuration instructions for Java, Go, JavaScript/Node.js, and Python clients, see [Heartbeat Configuration for Neptune Serverless](best-practices-gremlin-heartbeat-serverless.md).

## Monitoring serverless capacity with Amazon CloudWatch
<a name="neptune-serverless-monitoring"></a>

You can use CloudWatch to monitor the capacity and utilization of the Neptune serverless instances in your DB cluster. There are two CloudWatch metrics that let you track current serverless capacity both at the cluster level and at the instance level:
+ **`ServerlessDatabaseCapacity`**   –   As an instance-level metric, `ServerlessDatabaseCapacity` reports the current instance capacity, in NCUs. As a cluster-level metric, it reports the average of all the `ServerlessDatabaseCapacity` values of all the DB instances in the cluster.
+ **`NCUUtilization`**   –   This metric reports the percentage of possible capacity being used. It is calculated as the current `ServerlessDatabaseCapacity` (either at the instance level or at the cluster level) divided by the maximum capacity setting for the DB cluster.

  If this metric approaches 100% at a cluster level, meaning that the cluster has scaled as high as it can, consider increasing the maximum capacity setting.

  If it approaches 100% for a reader instance while the writer instance is not near maximum capacity, consider adding more reader instances to distribute the read workload.

Note that the `CPUUtilization` and `FreeableMemory` metrics have slightly different meanings for serverless instances than for provisioned instances. In a serverless context, `CPUUtilization` is a percentage that's calculated as the amount of CPU currently being used divided by the amount of CPU that would be available at maximum capacity. Similarly, `FreeableMemory` reports the amount of freeable memory that would be available if an instance was at maximum capacity.

The following example shows how to use the AWS CLI on Linux to retrieve the minimum, maximum, and average capacity values for a given DB instance, measured every 10 minutes over one hour. The Linux `date` command specifies the start and end times relative to the current date and time. The `sort_by` function in the `--query` parameter sorts the results chronologically based on the `Timestamp` field:

```
aws cloudwatch get-metric-statistics \
  --metric-name "ServerlessDatabaseCapacity" \
  --start-time "$(date -d '1 hour ago')" \
  --end-time "$(date -d 'now')" \
  --period 600 \
  --namespace "AWS/Neptune"
  --statistics Minimum Maximum Average \
  --dimensions Name=DBInstanceIdentifier,Value={{(instance ID)}} \
  --query 'sort_by(Datapoints[*].{min:Minimum,max:Maximum,avg:Average,ts:Timestamp},&ts)' \
  --output table
```