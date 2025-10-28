# Manually resize a running Amazon EMR cluster

You can add and remove instances from core and task instance groups and instance
fleets in a running cluster with the AWS Management Console, AWS CLI, or the Amazon EMR API. If a cluster
uses instance groups, you explicitly change the instance count. If your cluster uses
instance fleets, you can change the target units for On-Demand Instances and Spot
Instances. The instance fleet then adds and removes instances to meet the new target.
For more information, see [Instance fleet options](emr-instance-fleet.md#emr-instance-fleet-options "emr-instance-fleet.md#emr-instance-fleet-options"). Applications can use newly provisioned
Amazon EC2 instances to host nodes as soon as the instances are available. When instances are
removed, Amazon EMR shuts down tasks in a way that does not interrupt jobs and safeguards
against data loss. For more information, see [Terminate at task completion](emr-scaledown-behavior.md#emr-scaledown-terminate-task "emr-scaledown-behavior.md#emr-scaledown-terminate-task").

## Resize a cluster with the console

You can use the Amazon EMR console to resize a running cluster.

Console

###### To change the instance count for an existing cluster with the new

console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left navigation
   pane, choose **Clusters**, and select the
   cluster that you want to update. The cluster must be running;
   you can't resize a provisioning or terminated cluster.
3. On the **Instances** tab on the cluster
   details page, view the **Instance groups**
   panel.
4. To resize an existing instance group, select the radio button
   next to the core or task instance group that you want to resize
   and then choose **Resize instance group**.
   Specify the new number of instances for the instance group, then
   select **Resize**.

###### Note

If you choose to reduce the size of a running instance
group, Amazon EMR will intelligently select the instances to
remove from the group for minimal data loss. For more
granular control of your resize action, you can select the
**ID** for the instance group, choose
the instances you want to remove, and then use the
**Terminate** option. For more
information on intelligent scale-down behavior, see [Cluster scale-down options for Amazon EMR clusters](emr-scaledown-behavior.md "emr-scaledown-behavior.md"). 5. If you want to cancel the resizing action, you can select the
radio button for an instance group with the status
**Resizing** and then choose **Stop
resize** from the list actions. 6. To add one or more task instance groups to your cluster in
response to increasing workload, choose **Add task
instance group** from the list actions. Choose the
Amazon EC2 instance type, enter the number of instances for the task
group, then select **Add task instance group**
to return to the **Instance groups** panel for
your cluster.

When you make a change to the number of nodes, the **Status** of
the instance group updates. When the change you requested is complete, the
**Status** is **Running**.

## Resize a cluster with the AWS CLI

You can use the AWS CLI to resize a running cluster. You can increase or decrease
the number of task nodes, and you can increase the number of core nodes in a running
cluster. It is also possible to shut down an instance in the core instance group
with the AWS CLI or the API. This should be done with caution. Shutting down an
instance in the core instance group risks data loss, and the instance is not
automatically replaced.

In addition to resizing the core and task groups, you can also add one or more
task instance groups to a running cluster with the AWS CLI.

###### To resize a cluster by changing the

instance count with the AWS CLI

You can add instances to the core group or task group, and you can remove
instances from the task group with the AWS CLI `modify-instance-groups`
subcommand with the `InstanceCount` parameter. To add instances to
the core or task groups, increase the `InstanceCount`. To reduce the
number of instances in the task group, decrease the `InstanceCount`.
Changing the instance count of the task group to 0 removes all instances but not
the instance group.

- To increase the number of instances in the task instance group from 3 to
  4, type the following command and replace
  `ig-31JXXXXXXBTO` with the instance group
  ID.

```
aws emr modify-instance-groups --instance-groups InstanceGroupId=`ig-31JXXXXXXBTO`,InstanceCount=`4`
```

To retrieve the `InstanceGroupId`, use the
`describe-cluster` subcommand. The output is a JSON object
called `Cluster` that contains the ID of each instance group. To
use this command, you need the cluster ID (which you can retrieve with the
`aws emr list-clusters` command or the console). To retrieve
the instance group ID, type the following command and replace
`j-2AXXXXXXGAPLF` with the cluster ID.

```
aws emr describe-cluster --cluster-id `j-2AXXXXXXGAPLF`
```

With the AWS CLI, you can also terminate an instance in the core instance
group with the `--modify-instance-groups` subcommand.

###### Warning

Specifying `EC2InstanceIdsToTerminate` must be done with
caution. Instances are terminated immediately, regardless of the status
of applications running on them, and the instance is not automatically
replaced. This is true regardless of the cluster's **Scale down
behavior** configuration. Terminating an instance in this
way risks data loss and unpredictable cluster behavior.

To terminate a specific instance you need the instance group ID (returned
by the `aws emr describe-cluster --cluster-id` subcommand) and
the instance ID (returned by the `aws emr list-instances
 --cluster-id` subcommand), type the following command, replace
`ig-6RXXXXXX07SA` with the instance group ID
and replace `i-f9XXXXf2` with the instance
ID.

```
aws emr modify-instance-groups --instance-groups InstanceGroupId=`ig-6RXXXXXX07SA`,EC2InstanceIdsToTerminate=`i-f9XXXXf2`
```

For more information about using Amazon EMR commands in the AWS CLI, see [https://docs.aws.amazon.com/cli/latest/reference/emr](../../../cli/latest/reference/emr.md "../../../cli/latest/reference/emr.md").

###### To resize a cluster by adding task instance groups with the AWS CLI

With the AWS CLI, you can add from 1–48 task instance groups to a cluster
with the `--add-instance-groups` subcommand. Task instances groups
can only be added to a cluster containing a primary instance group and a
core instance group. When you use the AWS CLI, you can add up to five task
instance groups each time you use the `--add-instance-groups`
subcommand.

1. To add a single task instance group to a cluster, type the following
   command and replace `j-JXBXXXXXX37R` with the
   cluster ID.

```
aws emr add-instance-groups --cluster-id `j-JXBXXXXXX37R` --instance-groups InstanceCount=`6`,InstanceGroupType=`task`,InstanceType=`m5.xlarge`
```

2. To add multiple task instance groups to a cluster, type the following
   command and replace `j-JXBXXXXXX37R` with the
   cluster ID. You can add up to five task instance groups in a single
   command.

```
aws emr add-instance-groups --cluster-id `j-JXBXXXXXX37R` --instance-groups InstanceCount=`6`,InstanceGroupType=`task`,InstanceType=`m5.xlarge` InstanceCount=`10`,InstanceGroupType=`task`,InstanceType=`m5.xlarge`
```

For more information about using Amazon EMR commands in the AWS CLI, see [https://docs.aws.amazon.com/cli/latest/reference/emr](../../../cli/latest/reference/emr.md "../../../cli/latest/reference/emr.md").

## Interrupting a resize

Using Amazon EMR version 4.1.0 or later, you can issue a resize in the midst of an
existing resize operation. Additionally, you can stop a previously submitted resize
request or submit a new request to override a previous request without waiting for
it to finish. You can also stop an existing resize from the console or with the
`ModifyInstanceGroups` API call with the current count as the target
count of the cluster.

The following screenshot shows a task instance group that is resizing but can be
stopped by choosing **Stop**.

![Task instance group showing resizing status with options to resize or stop.](images/resize-stop.png)

###### To interrupt a resize with the AWS CLI

You can use the AWS CLI to stop a resize with the
`modify-instance-groups` subcommand. Assume that you have six
instances in your instance group and you want to increase this to 10. You later
decide that you would like to cancel this request:

- The initial request:

```
aws emr modify-instance-groups --instance-groups InstanceGroupId=ig-`myInstanceGroupId`,InstanceCount=10
```

The second request to stop the first request:

```
aws emr modify-instance-groups --instance-groups InstanceGroupId=ig-`myInstanceGroupId`,InstanceCount=6
```

###### Note

Because this process is asynchronous, you may see instance counts change with
respect to previous API requests before subsequent requests are honored. In the
case of shrinking, it is possible that if you have work running on the nodes,
the instance group may not shrink until nodes have completed their work.

## Suspended state

An instance group goes into a suspended state if it encounters too many errors
while trying to start the new cluster nodes. For example, if new nodes fail while
performing bootstrap actions, the instance group goes into a
_SUSPENDED_ state, rather than continuously provisioning new
nodes. After you resolve the underlying issue, reset the desired number of nodes on
the cluster's instance group, and then the instance group resumes allocating nodes.
Modifying an instance group instructs Amazon EMR to attempt to provision nodes again. No
running nodes are restarted or terminated.

In the AWS CLI, the `list-instances` subcommand returns all instances and
their states as does the `describe-cluster` subcommand. If Amazon EMR detects
a fault with an instance group, it changes the group's state to
`SUSPENDED`.

###### To reset a cluster in a SUSPENDED state with the AWS CLI

Type the `describe-cluster` subcommand with the
`--cluster-id` parameter to view the state of the instances in
your cluster.

- To view information on all instances and instance groups in a cluster,
  type the following command and replace
  `j-3KVXXXXXXY7UG` with the cluster ID.

```
aws emr describe-cluster --cluster-id `j-3KVXXXXXXY7UG`
```

The output displays information about your instance groups and the state
of the instances:

```
{
    "Cluster": {
        "Status": {
            "Timeline": {
                "ReadyDateTime": 1413187781.245,
                "CreationDateTime": 1413187405.356
            },
            "State": "WAITING",
            "StateChangeReason": {
                "Message": "Waiting after step completed"
            }
        },
        "Ec2InstanceAttributes": {
            "Ec2AvailabilityZone": "us-west-2b"
        },
        "Name": "Development Cluster",
        "Tags": [],
        "TerminationProtected": false,
        "RunningAmiVersion": "3.2.1",
        "NormalizedInstanceHours": 16,
        "InstanceGroups": [
            {
                "RequestedInstanceCount": 1,
                "Status": {
                    "Timeline": {
                        "ReadyDateTime": 1413187775.749,
                        "CreationDateTime": 1413187405.357
                    },
                    **"State": "RUNNING",**
                    "StateChangeReason": {
                        "Message": ""
                    }
                },
                **"Name": "MASTER",
 "InstanceGroupType": "MASTER",
 "InstanceType": "m5.xlarge",
 "Id": "ig-3ETXXXXXXFYV8",**
                "Market": "ON_DEMAND",
                "RunningInstanceCount": 1
            },
            {
                "RequestedInstanceCount": 1,
                "Status": {
                    "Timeline": {
                        "ReadyDateTime": 1413187781.301,
                        "CreationDateTime": 1413187405.357
                    },
                    **"State": "RUNNING",**
                    "StateChangeReason": {
                        "Message": ""
                    }
                },
                **"Name": "CORE",
 "InstanceGroupType": "CORE",
 "InstanceType": "m5.xlarge",
 "Id": "ig-3SUXXXXXXQ9ZM",**
                "Market": "ON_DEMAND",
                "RunningInstanceCount": 1
            }
...
}
```

To view information about a particular instance group, type the
`list-instances` subcommand with the
`--cluster-id` and `--instance-group-types`
parameters. You can view information for the primary, core, or task
groups.

```
aws emr list-instances --cluster-id `j-3KVXXXXXXY7UG` --instance-group-types `"CORE"`
```

Use the `modify-instance-groups` subcommand with the
`--instance-groups` parameter to reset a cluster in the
`SUSPENDED` state. The instance group id is returned by the
`describe-cluster` subcommand.

```
aws emr modify-instance-groups --instance-groups InstanceGroupId=`ig-3SUXXXXXXQ9ZM`,InstanceCount=`3`
```

## Considerations when reducing cluster

size

If you choose to reduce the size of a running cluster, consider the following
Amazon EMR behavior and best practices:

- To reduce impact on jobs that are in progress, Amazon EMR intelligently selects
  the instances to remove. For more information on cluster scale-down
  behavior, see [Terminate at task completion](emr-scaledown-behavior.md#emr-scaledown-terminate-task "emr-scaledown-behavior.md#emr-scaledown-terminate-task") in the Amazon EMR Management
  Guide.
- When you scale down the size of a cluster, Amazon EMR copies the data from the
  instances that it removes to the instances that remain. Ensure that there is
  sufficient storage capacity for this data in the instances that remain in
  the group.
- Amazon EMR attempts to decommission HDFS on instances in the group. Before you
  reduce the size of a cluster, we recommend that you minimize HDFS write
  I/O.
- For the most granular control when you reduce the size of a cluster, you
  can view the cluster in the console and navigate to the
  **Instances** tab. Select the **ID**
  for the instance group that you want to resize. Then use the
  **Terminate** option for the specific instances that
  you want to remove.
