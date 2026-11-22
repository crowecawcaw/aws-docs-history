

# Configuring instance health checks

You configure health monitoring and deep health checks on each compute node group, when you create it or later. Each has its own repair action, and you can turn on either one or both.

Before you start, check the [Prerequisites](cng-instance-health-checks.md#cng-instance-health-checks-requirements).

**Important**  
Changing instance health checks on an existing compute node group replaces all its instances after their running jobs finish.

**Contents**
+ [Instance health check settings](#cng-instance-health-checks-configure-settings)
+ [Turning on instance health checks when you create a compute node group](#cng-instance-health-checks-configure-create)
+ [Changing or turning off instance health checks](#cng-instance-health-checks-configure-update)
+ [Viewing instance health check settings](#cng-instance-health-checks-configure-view)

## Instance health check settings
<a name="cng-instance-health-checks-configure-settings"></a>

In the API and the AWS CLI, the settings are in the `instanceHealthChecks` member of the compute node group. In the console, they are in the **Instance health checks** section of the create and edit pages.

```json
{
  "healthMonitoring": {
    "mode": "STANDARD",
    "repairAction": "AUTO"
  },
  "deepHealthChecks": {
    "onStart": {
      "profile": "MEDIUM",
      "repairAction": "AUTO"
    }
  }
}
```


**Instance health check settings**  

| **Setting** | **Console label** | **Values** | 
| --- | --- | --- | 
| `healthMonitoring.mode` | **Enable health monitoring** | `STANDARD` monitors the compute nodes for faults while they run. `NONE` turns health monitoring off. Required when you specify `healthMonitoring`. When the value is `NONE`, omit `repairAction`. | 
| `healthMonitoring.repairAction` | **Repair action** | What AWS PCS does when health monitoring finds a fault: `AUTO` (default), `REPLACE`, `ISOLATE`, or `NONE`. | 
| `deepHealthChecks.onStart.profile` | **Enable deep health checks when instances start** and **Test profile** | The set of diagnostic tests that runs each time an instance starts: `QUICK`, `MEDIUM`, or `LONG`. Longer profiles test more and add more time to each start. `NONE` turns deep health checks off. Required when you specify `onStart`. When the value is `NONE`, omit `repairAction`. | 
| `deepHealthChecks.onStart.repairAction` | **Repair action** | What AWS PCS does when a deep health check finds a fault: `AUTO` (default), `REPLACE`, `ISOLATE`, or `NONE`. | 

For what each repair action does, see [Repair actions](cng-instance-health-checks.md#cng-instance-health-checks-repair-actions). For the DCGM level that each profile runs, see [Profiles](cng-instance-health-checks-deep.md#cng-instance-health-checks-deep-profiles).

## Turning on instance health checks when you create a compute node group
<a name="cng-instance-health-checks-configure-create"></a>

------
#### [ AWS Management Console ]

**To turn on instance health checks when you create a compute node group (console)**

1. Start creating the compute node group. For more information, see [Creating a compute node group in AWS PCS](working-with_cng_create.md).

1. In the **Instance health checks** section, do one or both of the following:

   1. To turn on health monitoring, turn on **Enable health monitoring**. For **Repair action**, choose the action that AWS PCS takes when health monitoring finds a fault.

   1. To turn on deep health checks, turn on **Enable deep health checks when instances start**. For **Test profile**, choose **Quick**, **Medium**, or **Long**. For **Repair action**, choose the action that AWS PCS takes when an instance fails the tests.

      Deep health checks need instance types with NVIDIA GPUs. If the compute node group's instance types don't have NVIDIA GPUs, the console doesn't let you turn on deep health checks, and AWS PCS rejects the request.

1. Finish configuring the other settings for the compute node group, and then choose **Create compute node group**.

------
#### [ AWS CLI ]

Add the `--instance-health-checks` option to the `create-compute-node-group` command. The following command turns on health monitoring and deep health checks with the `MEDIUM` profile. Both use the default repair action, `AUTO`.

```
aws pcs create-compute-node-group --region {{region}} \
    --cluster-identifier {{my-cluster}} \
    --compute-node-group-name {{my-node-group}} \
    --launch-template-mode MANAGED \
    --ami-id {{ami-ExampleID1}} \
    --subnet-ids {{subnet-ExampleID1}} \
    --security-group-ids {{sg-ExampleID1}} \
    --iam-instance-profile-arn {{arn:InstanceProfile}} \
    --scaling-configuration minInstanceCount={{min-instances}},maxInstanceCount={{max-instances}} \
    --instance-configs instanceType={{p5.48xlarge}} \
    --instance-health-checks '{
        "healthMonitoring": {"mode": "STANDARD"},
        "deepHealthChecks": {"onStart": {"profile": "MEDIUM"}}
    }'
```

Replace {{region}} with the ID of the AWS Region where your cluster is. To use only one type of check, omit the other block. To choose a different repair action, add `repairAction` to the block. For example, `"healthMonitoring": {"mode": "STANDARD", "repairAction": "ISOLATE"}`.

------

## Changing or turning off instance health checks
<a name="cng-instance-health-checks-configure-update"></a>

------
#### [ AWS Management Console ]

**To change or turn off instance health checks (console)**

1. Open the edit page for the compute node group. For more information, see [Updating a compute node group in AWS PCS](working-with_cng_update.md).

1. In the **Instance health checks** section, change the settings. To turn off a type of check, turn off **Enable health monitoring** or **Enable deep health checks when instances start**.

1. Choose **Update compute node group**.

------
#### [ AWS CLI ]

Use the `--instance-health-checks` option with the `update-compute-node-group` command. To keep the current settings, omit `--instance-health-checks`. The value that you send replaces all of the compute node group's instance health check settings. Start from the output of `get-compute-node-group`.

To turn off a type of check, set its `mode` or `profile` to `NONE`.

**Example – Turning off all instance health checks**  

```
aws pcs update-compute-node-group --region {{region}} \
    --cluster-identifier {{my-cluster}} \
    --compute-node-group-identifier {{my-node-group}} \
    --instance-health-checks '{
        "healthMonitoring": {"mode": "NONE"},
        "deepHealthChecks": {"onStart": {"profile": "NONE"}}
    }'
```

Replace {{region}} with the ID of the AWS Region where your cluster is. Updates can take several minutes. To check the status of the update, run the `get-compute-node-group` command. For more information, see [Viewing instance health check settings](#cng-instance-health-checks-configure-view).

------

## Viewing instance health check settings
<a name="cng-instance-health-checks-configure-view"></a>

------
#### [ AWS Management Console ]

**To view instance health check settings (console)**

1. Open the [AWS PCS console](https://console.aws.amazon.com/pcs/home#/clusters), and then choose your cluster.

1. Choose **Compute node groups**, and then choose the compute node group.

1. In the **Instance health checks** section, **Status** shows **Enabled** or **Disabled** for each type of check. For a check that's turned on, the section also shows its **Repair action** and, for deep health checks, its **Test profile**.

------
#### [ AWS CLI ]

```
aws pcs get-compute-node-group --region {{region}} \
    --cluster-identifier {{my-cluster}} \
    --compute-node-group-identifier {{my-node-group}} \
    --query 'computeNodeGroup.instanceHealthChecks'
```

The output shows the settings as you specified them.

------