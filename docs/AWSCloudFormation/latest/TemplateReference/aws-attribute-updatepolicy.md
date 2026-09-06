

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# `UpdatePolicy` attribute
<a name="aws-attribute-updatepolicy"></a>

Use the `UpdatePolicy` attribute to specify how CloudFormation handles updates to certain resources during stack update operations. 

**Topics**
+ [Overview](#aws-resource-update-policies)
+ [WorkSpaces Applications update policy](#aws-attribute-update-policy-app-stream-fleet)
+ [AutoScalingReplacingUpdate policy](#cfn-attributes-updatepolicy-replacingupdate)
+ [AutoScalingRollingUpdate policy](#cfn-attributes-updatepolicy-rollingupdate)
+ [AutoScalingInstanceRefresh policy](#cfn-attributes-updatepolicy-instancerefresh)
+ [AutoScalingScheduledAction policy](#cfn-attributes-updatepolicy-scheduledactions)
+ [UseOnlineResharding policy](#cfn-attributes-updatepolicy-useonlineresharding)
+ [EnableVersionUpgrade policy](#cfn-attributes-updatepolicy-upgradeopensearchdomain)
+ [CodeDeployLambdaAliasUpdate policy](#cfn-attributes-updatepolicy-codedeploylambdaaliasupdate)
+ [Examples](#aws-attribute-updatepolicy-examples)

## Overview
<a name="aws-resource-update-policies"></a>

By using the `UpdatePolicy` attribute, you can control how the following resources are updated, as described here:
+ **[AWS::AppStream::Fleet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appstream-fleet.html)** – CloudFormation can stop and start a fleet, which causes the fleet's instances to be replaced. By doing so, all instances will have the latest changes applied immediately after a stack update.
+ **[AWS::AutoScaling::AutoScalingGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html)** – With Auto Scaling groups, you can use one or more update policies to control how CloudFormation handles certain updates. These policies include:
  + **`AutoScalingReplacingUpdate` and `AutoScalingRollingUpdate` policies** – CloudFormation can either replace the Auto Scaling group and its instances with an `AutoScalingReplacingUpdate` policy, or replace only the instances with an `AutoScalingRollingUpdate` policy. These replacement operations occur when you make one or more of the following changes:
    + Change the Auto Scaling group's [AWS::AutoScaling::LaunchConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-launchconfiguration.html).
    + Change the Auto Scaling group's `VPCZoneIdentifier` property.
    + Change the Auto Scaling group's `LaunchTemplate` property.
    + Change the Auto Scaling group's `PlacementGroup` property.
    + Update an Auto Scaling group that contains instances that don't match the current `LaunchConfiguration`.

    If both the `AutoScalingReplacingUpdate` and `AutoScalingRollingUpdate` policies are specified, setting the `WillReplace` property to `true` gives `AutoScalingReplacingUpdate` precedence.
  + **`AutoScalingInstanceRefresh` policy** – CloudFormation runs an Auto Scaling instance refresh when you change certain properties of the Auto Scaling group. Compared to `AutoScalingRollingUpdate`, this policy supports instance maintenance policies (including launch-before-terminate), termination policies, scale-in protection, root volume replacement, and additional Amazon EC2 Auto Scaling features. You can't specify both `AutoScalingInstanceRefresh` and `AutoScalingRollingUpdate` on the same Auto Scaling group. For more information, see the [AutoScalingInstanceRefresh policy](#cfn-attributes-updatepolicy-instancerefresh).
  + **`AutoScalingScheduledAction` policy** – This policy applies when you update a stack that includes an Auto Scaling group with scheduled actions that scale the group at specific times. CloudFormation can't modify the minimum size, maximum size, or desired capacity of the group unless they have been explicitly changed in the stack template. This policy helps to prevent any unexpected updates that could interfere with the scheduled scaling activities.
+ **[AWS::ElastiCache::ReplicationGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticache-replicationgroup.html)** – CloudFormation can modify a replication group's shards by adding or removing shards, rather than replacing the entire resource. 
+ **[AWS::OpenSearchService::Domain](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opensearchservice-domain.html)** and **[AWS::Elasticsearch::Domain](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticsearch-domain.html)** (legacy) – CloudFormation can upgrade an OpenSearch Service domain to a new version of OpenSearch or Elasticsearch without replacing the entire resource. 
+ **[AWS::Lambda::Alias](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-alias.html)** – CloudFormation can perform a CodeDeploy deployment when the version changes on the alias. 

The sections that follow describe the syntax and properties for the `UpdatePolicy` attribute supported by each resource type.

## WorkSpaces Applications update policy
<a name="aws-attribute-update-policy-app-stream-fleet"></a>

To stop an WorkSpaces Applications fleet before an update and restart it after an update, use the WorkSpaces Applications update policy. 

### Syntax
<a name="aws-attribute-update-policy-app-stream-fleet-syntax"></a>

#### JSON
<a name="aws-attribute-update-policy-app-stream-fleet-syntax-json"></a>

```
{
    "UpdatePolicy": {
        "StopBeforeUpdate": {
            "Type": "{{Boolean}}"
        },
        "StartAfterUpdate": {
            "Type": "{{Boolean}}"
        }
    }
}
```

#### YAML
<a name="aws-attribute-update-policy-app-stream-fleet-syntax-yaml"></a>

```
UpdatePolicy:
  StopBeforeUpdate:
    Type: {{Boolean}}
  StartAfterUpdate:
    Type: {{Boolean}}
```

`StopBeforeUpdate`  <a name="cfn-attributes-updatepolicy-replacingupdate-StopBeforeUpdate"></a>
Stops the specified fleet before the update.  
*Required*: No

`StartAfterUpdate`  <a name="cfn-attributes-updatepolicy-replacingupdate-StartAfterUpdate"></a>
Starts the specified fleet after the update.  
*Required*: No

## AutoScalingReplacingUpdate policy
<a name="cfn-attributes-updatepolicy-replacingupdate"></a>

To replace the Auto Scaling group and the instances it contains, use the `AutoScalingReplacingUpdate` policy.

Before attempting an update, ensure that you have sufficient Amazon EC2 capacity for both your old and new Auto Scaling groups.

### Syntax
<a name="cfn-attributes-updatepolicy-replacingupdate-syntax"></a>

#### JSON
<a name="aws-attribute-updatepolicy-replacingupdate-syntax.json"></a>

```
"UpdatePolicy" : {
  "AutoScalingReplacingUpdate" : {
    "WillReplace" : {{Boolean}}
  }
}
```

#### YAML
<a name="aws-attribute-updatepolicy-replacingupdate-syntax.yaml"></a>

```
UpdatePolicy:
  AutoScalingReplacingUpdate:
    WillReplace: {{Boolean}}
```

### Properties
<a name="cfn-attributes-updatepolicy-replacingupdate-properties"></a>

`WillReplace`  <a name="cfn-attributes-updatepolicy-replacingupdate-willreplace"></a>
Specifies whether an Auto Scaling group and the instances it contains are replaced during an update. During replacement, CloudFormation retains the old group until it finishes creating the new one. If the update fails, CloudFormation can roll back to the old Auto Scaling group and delete the new Auto Scaling group.  
While CloudFormation creates the new group, it doesn't detach or attach any instances. After successfully creating the new Auto Scaling group, CloudFormation deletes the old Auto Scaling group during the cleanup process.  
When you set the `WillReplace` parameter, remember to specify a matching [`CreationPolicy` attribute](aws-attribute-creationpolicy.md). If the minimum number of instances (specified by the `MinSuccessfulInstancesPercent` property) don't signal success within the `Timeout` period (specified in the `CreationPolicy` attribute), the replacement update fails and CloudFormation rolls back to the old Auto Scaling group.  
*Type*: Boolean  
*Required*: No

## AutoScalingRollingUpdate policy
<a name="cfn-attributes-updatepolicy-rollingupdate"></a>

To perform a rolling update of the instances in an Auto Scaling group rather than wait for scaling activities to gradually replace older instances with newer instances, use the `AutoScalingRollingUpdate` policy. This policy provides you the flexibility to specify whether CloudFormation replaces instances that are in an Auto Scaling group in batches or all at once without replacing the entire resource. 

Things to consider when using an `AutoScalingRollingUpdate` policy:

**Warning**  
Rolling updates don't honor the instance maintenance policy configured on your Auto Scaling group. During a rolling update, healthy capacity can drop below the `MinHealthyPercentage` set on the group, and CloudFormation doesn't launch new instances before terminating existing ones, regardless of `MaxHealthyPercentage`. To preserve your instance maintenance policy during stack updates, use the [AutoScalingInstanceRefresh policy](#cfn-attributes-updatepolicy-instancerefresh) instead.
+ When CloudFormation rolls back an update, it uses the `UpdatePolicy` configuration specified in the template before the current stack update. For example, you change the `MaxBatchSize` from 1 to 10 in the `UpdatePolicy`, perform a stack update, and that update fails. CloudFormation will use 1 as the maximum batch size when it rolls back, not 10. To avoid this scenario, make changes to the `UpdatePolicy` in a separate update before any updates to the Auto Scaling group that are likely to initiate rolling updates.
+ CloudFormation recommends specifying the `SuspendProcesses` property to temporarily suspend Amazon EC2 Auto Scaling processes that might interfere with the rolling update and cause it to fail. For more information, see [How can I update my Auto Scaling group when I update my CloudFormation stack?](https://repost.aws/knowledge-center/auto-scaling-group-rolling-updates)

  Alternatively, the `AutoScalingInstanceRefresh` policy supports all Auto Scaling group processes during stack updates, so you don't need to suspend them. If you need processes such as health checks and AZ rebalance to remain active, use `AutoScalingInstanceRefresh` instead. For more information, see the [AutoScalingInstanceRefresh policy](#cfn-attributes-updatepolicy-instancerefresh).
+ CloudFormation supports using Amazon EC2 Auto Scaling lifecycle hooks when launching or terminating instances. This gives you time to perform custom actions on an instance before it moves to the next state. To make sure that new instances reach the `InService` state, complete the lifecycle hook with a `CONTINUE` result when the custom action finishes. By default, if no response is received and the lifecycle hook times out, the instance launch will be considered unsuccessful and abandoned. If no instances reach the `InService` state, the rolling update will eventually fail.
+ Other Amazon EC2 Auto Scaling features such as termination policies and scale-in protection aren't available for use with CloudFormation rolling updates. If you need any of these features, use `AutoScalingInstanceRefresh` instead. For more information, see [AutoScalingInstanceRefresh policy](#cfn-attributes-updatepolicy-instancerefresh).
+ If you use an `AutoScalingRollingUpdate` policy and remove the placement group setting, the placement group will be removed from the Auto Scaling group and the CloudFormation template. Also this triggers a rolling update, so new instances won't be launched into a placement group.

### Syntax
<a name="cfn-attributes-updatepolicy-rollingupdate-syntax"></a>

#### JSON
<a name="aws-attribute-updatepolicy-rollingupdate-syntax.json"></a>

```
"UpdatePolicy" : {
  "AutoScalingRollingUpdate" : {
    "MaxBatchSize" : {{Integer}},
    "MinActiveInstancesPercent" : {{Integer}},
    "MinInstancesInService" : {{Integer}},
    "MinSuccessfulInstancesPercent" : {{Integer}},
    "PauseTime" : {{String}},
    "SuspendProcesses" : [ {{List of processes}} ],
    "WaitOnResourceSignals" : {{Boolean}}
  }
}
```

#### YAML
<a name="aws-attribute-updatepolicy-rollingupdate-syntax.yaml"></a>

```
UpdatePolicy:
  AutoScalingRollingUpdate:
    MaxBatchSize: {{Integer}}
    MinActiveInstancesPercent: {{Integer}}
    MinInstancesInService: {{Integer}}
    MinSuccessfulInstancesPercent: {{Integer}}
    PauseTime: {{String}}
    SuspendProcesses:
      - {{List of processes}}
    WaitOnResourceSignals: {{Boolean}}
```

### Properties
<a name="aws-attribute-updatepolicy-rollingupdate-properties"></a>

`MaxBatchSize`  <a name="cfn-attributes-updatepolicy-rollingupdate-maxbatchsize"></a>
Specifies the maximum number of instances that can be replaced simultaneously.  
*Default*: `1`  
*Maximum*: `100`  
*Type*: Integer  
*Required*: No

`MinActiveInstancesPercent`  <a name="cfn-attributes-updatepolicy-rollingupdate-minactiveinstancespercent"></a>
Specifies the percentage of instances in an Auto Scaling group that must be in the `InService` state relative to that group's desired capacity during a rolling update for an update to succeed. You can specify a value from 0 to 100. CloudFormation rounds to the nearest tenth of a percent. For example, if you update five instances with a minimum `InService` percentage of 50, at least three instances must be in the `InService` state. If an instance doesn't transition to the `InService` state within a fixed time of 1 hour, CloudFormation assumes that the instance wasn't updated.  
Setting `MinActiveInstancesPercent` in your `UpdatePolicy` will also affect instances launched when the `DesiredCapacity` property of the `AWS::AutoScaling::AutoScalingGroup` resource is set higher than the current desired capacity of that Auto Scaling group.  
*Default*: `100`  
*Type*: Integer  
*Required*: No

`MinInstancesInService`  <a name="cfn-attributes-updatepolicy-rollingupdate-mininstancesinservice"></a>
Specifies the minimum number of instances that must be in service within the Auto Scaling group while CloudFormation updates old instances. This value must be less than the [MaxSize](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-maxsize) of the Auto Scaling group.  
We recommend that you set the value of the `MinInstancesInService` property to at least the [MinSize](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-minsize) of the Auto Scaling group. This avoids potential availability issues during a rolling update due to 0 instances serving customer traffic. 
*Default*: `0`  
*Type*: Integer  
*Required*: No

`MinSuccessfulInstancesPercent`  <a name="cfn-attributes-updatepolicy-rollingupdate-minsuccessfulinstancespercent"></a>
Specifies the percentage of instances in an Auto Scaling rolling update that must signal success for an update to succeed. You can specify a value from 0 to 100. CloudFormation rounds to the nearest tenth of a percent. For example, if you update five instances with a minimum successful percentage of `50`, three instances must signal success. If an instance doesn't send a signal within the time specified in the `PauseTime` property, CloudFormation assumes that the instance wasn't updated.  
We recommend that you set the value of the `MinSuccessfulInstancesPercent` property to a value greater than 0. When the `MinSuccessfulInstancesPercent` property is set to 0, CloudFormation waits for 0% of the capacity instances to be in an `InService` state. `MinSuccessfulInstancesPercent` returns immediately and before considering the Auto Scaling group status as `UPDATE_COMPLETE` to move on to the subsequent resources defined in the stack template. If other Auto Scaling groups are defined in your CloudFormation template, they will update simultaneously. When all Auto Scaling groups are deployed at once with 0% of the capacity instances in an `InService` state, then you will experience availability issues, due to 0 instances serving customer traffic.  
*Default*: `100`  
*Type*: Integer  
*Required*: No

`PauseTime`  <a name="cfn-attributes-updatepolicy-rollingupdate-pausetime"></a>
The amount of time that CloudFormation pauses after making a change to a batch of instances to give those instances time to start software applications.   
Specify `PauseTime` in the [ISO8601 duration format](https://en.wikipedia.org/wiki/ISO_8601#Durations) (in the format `PT{{#}}H{{#}}M{{#}}S`, where each {{\#}} is the number of hours, minutes, and seconds, respectively). The maximum `PauseTime` is one hour (`PT1H`).  
When `WaitOnResourceSignals` is set to `true`, `PauseTime` acts as a timeout value. It determines the maximum time that CloudFormation waits to receive the required number of valid signals from the instances being replaced during a rolling update and from new instances being added by increasing the [DesiredCapacity](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html#cfn-autoscaling-autoscalinggroup-desiredcapacity) property of the `AWS::AutoScaling::AutoScalingGroup` resource. If the `PauseTime` is exceeded before CloudFormation receives the expected signals, the update fails. For best results, specify a time period that provides sufficient time for your applications to start up. If the update needs to be rolled back, a short `PauseTime` can cause the rollback to fail.
*Default*: `PT5M` (5 minutes) when the `WaitOnResourceSignals` property is set to `true`. Otherwise, no default value is set.   
*Type*: String  
*Required*: No

`SuspendProcesses`  <a name="cfn-attributes-updatepolicy-rollingupdate-suspendprocesses"></a>
Specifies the Auto Scaling processes to suspend during a stack update. Suspending processes prevents Auto Scaling from interfering with a stack update. For example, you can suspend alarming so that Amazon EC2 Auto Scaling doesn't initiate scaling policies associated with an alarm. For valid values, see [Types of processes](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html#process-types) in the *Amazon EC2 Auto Scaling User Guide*.  
*Default*: Not specified  
*Type*: List of Auto Scaling processes  
*Required*: No

`WaitOnResourceSignals`  <a name="cfn-attributes-updatepolicy-rollingupdate-waitonresourcesignals"></a>
Specifies whether CloudFormation waits for success signals from new instances before continuing the update. CloudFormation waits for the specified `PauseTime` duration for success signals.  
To signal the Auto Scaling group, use the [cfn-signal](cfn-signal.md) helper script. For Auto Scaling groups associated with Elastic Load Balancing, consider adding a health check to ensure that instances are healthy before signaling success by using the [cfn-init](cfn-init.md) helper script. For an example, see the `verify_instance_health` command in the sample templates for Amazon EC2 Auto Scaling rolling updates in our [GitHub repository](https://github.com/aws-cloudformation/aws-cloudformation-templates/tree/main/AutoScaling).  
*Default*: `false`  
*Type*: Boolean  
*Required*: Conditional. If you specify the `MinSuccessfulInstancesPercent` property, the `WaitOnResourceSignals` property must be set to `true`.

## AutoScalingInstanceRefresh policy
<a name="cfn-attributes-updatepolicy-instancerefresh"></a>

To update the instances in an Auto Scaling group by performing an Auto Scaling instance refresh, use the `AutoScalingInstanceRefresh` policy. For the full list of instance refresh capabilities, see [Use an instance refresh to update instances in an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html) in the *Amazon EC2 Auto Scaling User Guide*.

CloudFormation performs an instance refresh only when you update one of the following properties of an `AWS::AutoScaling::AutoScalingGroup` resource:
+ `LaunchTemplate`
+ `MixedInstancesPolicy`
+ `VPCZoneIdentifier`
+ `AvailabilityZones`
+ `AvailabilityZoneIds`
+ `PlacementGroup`

When you use the `AutoScalingInstanceRefresh` policy, consider the following:
+ You can't specify both `AutoScalingInstanceRefresh` and `AutoScalingRollingUpdate` policies on the same Auto Scaling group. If you do, the stack update fails.
+ CloudFormation stack rollback is the rollback mechanism for `AutoScalingInstanceRefresh`. If an instance refresh fails, CloudFormation rolls back the stack and starts a new instance refresh to restore the group to its previous configuration. You can't use the Auto Scaling `RollbackInstanceRefresh` API operation on an instance refresh that CloudFormation has already started. To revert a refresh, use the `CancelInstanceRefresh` API or roll back the stack update.
+ An Auto Scaling group can run only one instance refresh at a time. If a user-initiated instance refresh is in progress when you start a stack update with the `AutoScalingInstanceRefresh` policy, the stack update may fail.
+ When you set the instance refresh `Strategy` to `ReplaceRootVolume`, only changes to `ImageId` within the launch template or mixed instances policy are allowed. Other property changes may cause the stack update to fail. For more information, see [Replace root volumes during instance refresh](https://docs.aws.amazon.com/autoscaling/ec2/userguide/replace-root-volume.html) in the *Amazon EC2 Auto Scaling User Guide*.
+ Each direction of the stack update (forward and rollback) is bounded by the CloudFormation resource timeout of 36 hours.
+ Long-running instance refreshes might exceed the lifetime of the temporary credentials CloudFormation uses to call Auto Scaling. To avoid this, configure a service role on the stack. For more information, see [CloudFormation service role](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-servicerole.html).

**Note**  
Instance refresh doesn't support the [cfn-signal](cfn-signal.md) helper script. For information about how to verify instance readiness during an instance refresh, see [Verify instance readiness during an instance refresh](#cfn-attributes-updatepolicy-instancerefresh-readiness).

### Syntax
<a name="cfn-attributes-updatepolicy-instancerefresh-syntax"></a>

#### JSON
<a name="cfn-attributes-updatepolicy-instancerefresh-syntax.json"></a>

```
"UpdatePolicy" : {
  "AutoScalingInstanceRefresh" : {
    "Strategy" : {{String}},
    "Preferences" : {
      "AlarmSpecification" : {
        "Alarms" : [ {{List of alarm names}} ]
      },
      "BakeTime" : {{Integer}},
      "CheckpointDelay" : {{Integer}},
      "CheckpointPercentages" : [ {{List of integers}} ],
      "InstanceWarmup" : {{Integer}},
      "MaxHealthyPercentage" : {{Integer}},
      "MinHealthyPercentage" : {{Integer}},
      "ScaleInProtectedInstances" : {{String}},
      "SkipMatching" : {{Boolean}},
      "StandbyInstances" : {{String}}
    }
  }
}
```

#### YAML
<a name="cfn-attributes-updatepolicy-instancerefresh-syntax.yaml"></a>

```
UpdatePolicy:
  AutoScalingInstanceRefresh:
    Strategy: {{String}}
    Preferences:
      AlarmSpecification:
        Alarms:
          - {{List of alarm names}}
      BakeTime: {{Integer}}
      CheckpointDelay: {{Integer}}
      CheckpointPercentages:
        - {{List of integers}}
      InstanceWarmup: {{Integer}}
      MaxHealthyPercentage: {{Integer}}
      MinHealthyPercentage: {{Integer}}
      ScaleInProtectedInstances: {{String}}
      SkipMatching: {{Boolean}}
      StandbyInstances: {{String}}
```

### Properties
<a name="cfn-attributes-updatepolicy-instancerefresh-properties"></a>

`Strategy`  <a name="cfn-attributes-updatepolicy-instancerefresh-strategy"></a>
The strategy to use for the instance refresh. Valid values are `Rolling` and `ReplaceRootVolume`. For information about the `ReplaceRootVolume` strategy, see [Replace root volumes during instance refresh](https://docs.aws.amazon.com/autoscaling/ec2/userguide/replace-root-volume.html) in the *Amazon EC2 Auto Scaling User Guide*.  
*Type*: String  
*Required*: Yes

`Preferences`  <a name="cfn-attributes-updatepolicy-instancerefresh-properties-preferences"></a>
Sets the preferences for the instance refresh. Includes the instance warmup time, the minimum and maximum healthy percentages, and the behaviors that Amazon EC2 Auto Scaling uses if instances are in `Standby` state or protected from scale in. You can also enable additional features:  
+ Checkpoints
+ CloudWatch alarms
+ Skip matching
+ Bake time
*Type*: [Preferences](#cfn-attributes-updatepolicy-instancerefresh-preferences)  
*Required*: No

### Preferences
<a name="cfn-attributes-updatepolicy-instancerefresh-preferences"></a>

`AlarmSpecification`  <a name="cfn-attributes-updatepolicy-instancerefresh-preferences-alarmspecification"></a>
The CloudWatch alarm specification. You can use CloudWatch alarms to identify any issues during the instance refresh and roll back the stack if an alarm threshold is met. For more information, see [Start an instance refresh with auto rollback](https://docs.aws.amazon.com/autoscaling/ec2/userguide/instance-refresh-rollback.html#instance-refresh-using-auto-rollback) in the *Amazon EC2 Auto Scaling User Guide*.  
*Type*: [AlarmSpecification](#cfn-attributes-updatepolicy-instancerefresh-alarmspecification)  
*Required*: No

`BakeTime`  <a name="cfn-attributes-updatepolicy-instancerefresh-preferences-baketime"></a>
The amount of time, in seconds, to wait at the end of an instance refresh before the instance refresh is considered complete.  
*Default*: `0`  
*Minimum*: `0`  
*Maximum*: `172800`  
*Type*: Integer  
*Required*: No

`CheckpointDelay`  <a name="cfn-attributes-updatepolicy-instancerefresh-preferences-checkpointdelay"></a>
The amount of time, in seconds, to wait after a checkpoint before continuing. If you specify a value for `CheckpointPercentages` but not for `CheckpointDelay`, the `CheckpointDelay` defaults to `3600` (1 hour).  
*Minimum*: `0`  
*Maximum*: `172800`  
*Type*: Integer  
*Required*: No

`CheckpointPercentages`  <a name="cfn-attributes-updatepolicy-instancerefresh-preferences-checkpointpercentages"></a>
Threshold values for each checkpoint in ascending order. Each number must be unique. To replace all instances in the Auto Scaling group, the last number in the array must be `100`. For usage examples, see [Add checkpoints to an instance refresh](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-adding-checkpoints-instance-refresh.html) in the *Amazon EC2 Auto Scaling User Guide*.  
*Type*: List of integers  
*Required*: No

`InstanceWarmup`  <a name="cfn-attributes-updatepolicy-instancerefresh-preferences-instancewarmup"></a>
A time period, in seconds, during which an instance refresh waits before moving on to replacing the next instance after a new instance enters the `InService` state.  
If you don't specify `InstanceWarmup`, Auto Scaling uses the value for the `DefaultInstanceWarmup` property instead. We recommend that you set a value for `DefaultInstanceWarmup` in all use cases.  
If you don't specify a value for either property, Auto Scaling uses the value of the `HealthCheckGracePeriod` property.  
*Type*: Integer  
*Required*: No

`MaxHealthyPercentage`  <a name="cfn-attributes-updatepolicy-instancerefresh-preferences-maxhealthypercentage"></a>
Specifies the maximum percentage of the group that can be in service and healthy, or pending, to support your workload when replacing instances. The value is expressed as a percentage of the desired capacity of the Auto Scaling group. If you specify `MaxHealthyPercentage`, you must also specify `MinHealthyPercentage`, and the difference between them cannot be greater than 100. A larger range increases the number of instances that can be replaced at the same time.  
*Default*: The value set in the Auto Scaling group's instance maintenance policy, if defined. Otherwise, `110` when `Strategy` is `Rolling`, or `100` when `Strategy` is `ReplaceRootVolume`.  
*Minimum*: `100`  
*Maximum*: `200`  
*Type*: Integer  
*Required*: No

`MinHealthyPercentage`  <a name="cfn-attributes-updatepolicy-instancerefresh-preferences-minhealthypercentage"></a>
Specifies the minimum percentage of the group to keep in service, healthy, and ready to use to support your workload to allow the operation to continue. The value is expressed as a percentage of the desired capacity of the Auto Scaling group.  
*Default*: The value set in the Auto Scaling group's instance maintenance policy, if defined. Otherwise, `100` when `Strategy` is `Rolling`, or `90` when `Strategy` is `ReplaceRootVolume`.  
*Minimum*: `0`  
*Maximum*: `100`  
*Type*: Integer  
*Required*: No

`ScaleInProtectedInstances`  <a name="cfn-attributes-updatepolicy-instancerefresh-preferences-scaleinprotectedinstances"></a>
Choose the behavior that you want Amazon EC2 Auto Scaling to use if instances protected from scale in are found. The following lists the valid values:  
+ *Refresh*: Amazon EC2 Auto Scaling replaces instances that are protected from scale in.
+ *Ignore*: Amazon EC2 Auto Scaling ignores instances that are protected from scale in and continues to replace instances that are not protected.
+ *Wait*: Amazon EC2 Auto Scaling waits one hour for you to remove scale-in protection. Otherwise, the instance refresh fails.
*Default*: `Wait`  
*Type*: String  
*Required*: No

`SkipMatching`  <a name="cfn-attributes-updatepolicy-instancerefresh-preferences-skipmatching"></a>
Indicates whether skip matching is enabled. If enabled (`true`), Auto Scaling skips replacing instances that already match the configuration specified in your stack template. For more information, see [Use an instance refresh with skip matching](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh-skip-matching.html) in the *Amazon EC2 Auto Scaling User Guide*.  
*Default*: `true`  
*Type*: Boolean  
*Required*: No

`StandbyInstances`  <a name="cfn-attributes-updatepolicy-instancerefresh-preferences-standbyinstances"></a>
Choose the behavior that you want Amazon EC2 Auto Scaling to use if instances in `Standby` state are found. The following lists the valid values:  
+ *Terminate*: Amazon EC2 Auto Scaling terminates instances that are in `Standby`.
+ *Ignore*: Amazon EC2 Auto Scaling ignores instances that are in `Standby` and continues to replace instances that are in the `InService` state.
+ *Wait*: Amazon EC2 Auto Scaling waits one hour for you to return the instances to service. Otherwise, the instance refresh fails.
*Default*: `Wait`  
*Type*: String  
*Required*: No

### AlarmSpecification
<a name="cfn-attributes-updatepolicy-instancerefresh-alarmspecification"></a>

`Alarms`  <a name="cfn-attributes-updatepolicy-instancerefresh-alarmspecification-alarms"></a>
The names of one or more CloudWatch alarms to monitor for the instance refresh. You can specify up to 10 alarms.  
*Type*: List of strings  
*Required*: No

### Verify instance readiness during an instance refresh
<a name="cfn-attributes-updatepolicy-instancerefresh-readiness"></a>

By default, instance refresh automatically proceeds to the next set of instances when newly launched instances pass the health checks configured on your Auto Scaling group. These include the Amazon EC2 health checks and, if configured, the Elastic Load Balancing health checks. For more information, see [Health checks for instances in an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-health-checks.html) in the *Amazon EC2 Auto Scaling User Guide*.

If your instances require application bootstrapping before moving to `InService`, add an `autoscaling:EC2_INSTANCE_LAUNCHING` lifecycle hook to the Auto Scaling group. The instance refresh waits for the lifecycle hook to complete before it proceeds to the next set of instances. Complete the hook by calling the `CompleteLifecycleAction` API. You can make this call from the instance itself using a launch template user data script, or from an external service. For more information, see [Amazon EC2 Auto Scaling lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html) and [Complete a lifecycle action in an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/completing-lifecycle-hooks.html) in the *Amazon EC2 Auto Scaling User Guide*.

## AutoScalingScheduledAction policy
<a name="cfn-attributes-updatepolicy-scheduledactions"></a>

To specify how CloudFormation handles updates for the `MinSize`, `MaxSize`, and `DesiredCapacity` properties when the `AWS::AutoScaling::AutoScalingGroup` resource has an associated scheduled action, use the `AutoScalingScheduledAction` policy.

With scheduled actions, the group size properties of an Auto Scaling group can change at any time. When you update a stack with an Auto Scaling group and scheduled action, CloudFormation always sets the group size property values of your Auto Scaling group to the values that are defined in the `AWS::AutoScaling::AutoScalingGroup` resource of your template, even if a scheduled action is in effect.

If you don't want CloudFormation to change any of the group size property values when you have a scheduled action in effect, use the `AutoScalingScheduledAction` update policy and set `IgnoreUnmodifiedGroupSizeProperties` to `true` to prevent CloudFormation from changing the `MinSize`, `MaxSize`, or `DesiredCapacity` properties unless you have modified these values in your template.



### Syntax
<a name="cfn-attributes-updatepolicy-scheduledactions-syntax"></a>

#### JSON
<a name="aws-attribute-updatepolicy-scheduledactions-syntax.json"></a>

```
"UpdatePolicy" : {
  "AutoScalingScheduledAction" : {
    "IgnoreUnmodifiedGroupSizeProperties" : {{Boolean}}
  }
}
```

#### YAML
<a name="aws-attribute-updatepolicy-scheduledactions-syntax.yaml"></a>

```
UpdatePolicy:
  AutoScalingScheduledAction:
    IgnoreUnmodifiedGroupSizeProperties: {{Boolean}}
```

### Properties
<a name="cfn-attributes-updatepolicy-scheduledactions-properties"></a>

`IgnoreUnmodifiedGroupSizeProperties`  <a name="cfn-attributes-updatepolicy-scheduledactions-ignoreunmodifiedgroupsizeproperties"></a>
If `true`, CloudFormation ignores differences in group size properties between your current Auto Scaling group and the Auto Scaling group described in the `AWS::AutoScaling::AutoScalingGroup` resource of your template during a stack update. If you modify any of the group size property values in your template, CloudFormation uses the modified values and updates your Auto Scaling group.  
This property is ignored during a stack rollback.
*Default*: `false`  
*Type*: Boolean  
*Required*: No

## UseOnlineResharding policy
<a name="cfn-attributes-updatepolicy-useonlineresharding"></a>

To modify a replication group's shards by adding or removing shards, rather than replacing the entire [AWS::ElastiCache::ReplicationGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticache-replicationgroup.html) resource, use the `UseOnlineResharding` update policy.

If `UseOnlineResharding` is set to `true`, you can update the `NumNodeGroups` and `NodeGroupConfiguration` properties of the `AWS::ElastiCache::ReplicationGroup` resource, and CloudFormation will update those properties without interruption. When `UseOnlineResharding` is set to `false`, or not specified, updating the `NumNodeGroups` and `NodeGroupConfiguration` properties results in CloudFormation replacing the entire `AWS::ElastiCache::ReplicationGroup` resource.

The `UseOnlineResharding` update policy has no properties.

Things to consider when setting the `UseOnlineResharding` update policy to `true`:
+ We strongly recommend you perform updates to the `NumNodeGroups` and `NodeGroupConfiguration` properties as the only updates in a given stack update operation.

  Updating the node group configuration of a replication group is a resource-intensive operation. If a stack update fails, CloudFormation doesn't roll back changes to the node group configuration of a replication group. However, CloudFormation will roll back any other properties that were changed as part of the failed update operation.
+ Any node group updates require identifying all node groups.

  If you specify the `NodeGroupConfiguration` property, you must also specify the NodeGroupId for each node group configuration in order for CloudFormation to update the number of nodes without interruption.

  When creating a replication group, if you don't specify an ID for each node group, ElastiCache automatically generates an ID for each node group. To update the replication group without interruption, use the ElastiCache console ([https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/)) or [DescribeReplicationGroups](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeReplicationGroups.html) to retrieve the IDs for all node groups in the replication group. Then specify the ID for each node group in your stack template before attempting to add or remove shards.
**Note**  
As a best practice, when you create a replication group in a stack template, include an ID for each node group you specify.

  In addition, updating the number of nodes without interruption requires that you have accurately specified the `PrimaryAvailabilityZone`, `ReplicaAvailabilityZones`, and `ReplicaCount` properties for each `NodeGroupConfiguration` as well. Again, you can use the ElastiCache console ([https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/)) or [DescribeReplicationGroups](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeReplicationGroups.html) to retrieve the actual values for each node group and compare them to the values in your stack template. You can update the property values of the node groups as a separate stack update, or as part of the same stack update that changes the number of node groups.

  When you use an `UseOnlineResharding` update policy to update the number of node groups without interruption, ElastiCache evenly distributes the keyspaces between the specified number of slots. This can't be updated later. Therefore, after updating the number of node groups in this way, you should remove the value specified for the `Slots` property of each `NodeGroupConfiguration` from the stack template, as it no longer reflects the actual values in each node group.
+ Actual node group removal results may vary.

  When you specify a `NumNodeGroups` value that's less than the current number of node groups, CloudFormation instructs ElastiCache to remove as many node groups as necessary to reach the specified number of nodes. However, ElastiCache may not always be able to remove the desired number of node groups. In the event ElastiCache can't remove the desired number of node groups, CloudFormation generates a stack event alerting you to this. In cases where ElastiCache can't remove *any* node groups, the CloudFormation resource update fails.

For more information on modifying replication groups, see [ModifyReplicationGroupShardConfiguration](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyReplicationGroupShardConfiguration.html) in the *Amazon ElastiCache API Reference*.

### Syntax
<a name="cfn-attributes-updatepolicy-useonlineresharding-syntax"></a>

#### JSON
<a name="cfn-attributes-updatepolicy-useonlineresharding-syntax.json"></a>

```
"UpdatePolicy" : {
  "UseOnlineResharding" : {{Boolean}}
}
```

#### YAML
<a name="cfn-attributes-updatepolicy-useonlineresharding-syntax.yaml"></a>

```
UpdatePolicy:
  UseOnlineResharding: {{Boolean}}
```

## EnableVersionUpgrade policy
<a name="cfn-attributes-updatepolicy-upgradeopensearchdomain"></a>

To upgrade an OpenSearch Service domain to a new version of OpenSearch or Elasticsearch rather than replacing the entire [AWS::OpenSearchService::Domain](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opensearchservice-domain.html) or [AWS::Elasticsearch::Domain](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticsearch-domain.html) resource, use the `EnableVersionUpgrade` update policy.

If `EnableVersionUpgrade` is set to `true`, you can update the `EngineVersion` property of the `AWS::OpenSearchService::Domain` resource (or the `ElasticsearchVersion` property of the legacy `AWS::Elasticsearch::Domain` resource), and CloudFormation will update that property without interruption. When `EnableVersionUpgrade` is set to `false`, or not specified, updating the `EngineVersion` or `ElasticsearchVersion` property results in CloudFormation replacing the entire `AWS::OpenSearchService::Domain`/`AWS::Elasticsearch::Domain` resource.

The `EnableVersionUpgrade` update policy has no properties.

For more information, see [Upgrading OpenSearch Service domains](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/version-migration.html) in the Amazon OpenSearch Service Developer Guide.

### Syntax
<a name="cfn-attributes-updatepolicy-upgradeopensearchdomain-syntax"></a>

#### JSON
<a name="cfn-attributes-updatepolicy-upgradeopensearchdomain-syntax.json"></a>

```
"UpdatePolicy" : {
  "EnableVersionUpgrade" : {{Boolean}}
}
```

#### YAML
<a name="cfn-attributes-updatepolicy-upgradeopensearchdomain-syntax.yaml"></a>

```
UpdatePolicy:
  EnableVersionUpgrade: {{Boolean}}
```

## CodeDeployLambdaAliasUpdate policy
<a name="cfn-attributes-updatepolicy-codedeploylambdaaliasupdate"></a>

To perform an CodeDeploy deployment when the version changes on an `AWS::Lambda::Alias` resource, use the `CodeDeployLambdaAliasUpdate` update policy.

### Syntax
<a name="cfn-attributes-updatepolicy-codedeploylambdaaliasupdate-syntax"></a>

#### JSON
<a name="aws-attribute-updatepolicy-codedeploylambdaaliasupdate-syntax.json"></a>

```
"UpdatePolicy" : {
  "CodeDeployLambdaAliasUpdate" : {
    "AfterAllowTrafficHook" : {{String}},
    "ApplicationName" : {{String}},
    "BeforeAllowTrafficHook" : {{String}},
    "DeploymentGroupName" : {{String}}
  }
}
```

#### YAML
<a name="aws-attribute-updatepolicy-codedeploylambdaaliasupdate-syntax.yaml"></a>

```
UpdatePolicy:
  CodeDeployLambdaAliasUpdate:
    AfterAllowTrafficHook: {{String}}
    ApplicationName: {{String}}
    BeforeAllowTrafficHook: {{String}}
    DeploymentGroupName: {{String}}
```

### Properties
<a name="aws-attribute-updatepolicy-codedeploylambdaaliasupdate-properties"></a>

`AfterAllowTrafficHook`  <a name="cfn-attributes-updatepolicy-codedeploylambdaaliasupdate-afterallowtraffichook"></a>
The name of the Lambda function to run after traffic routing completes.  
*Required*: No  
*Type: *String

`ApplicationName`  <a name="cfn-attributes-updatepolicy-codedeploylambdaaliasupdate-applicationname"></a>
The name of the CodeDeploy application.  
*Required: *Yes  
*Type: *String

`BeforeAllowTrafficHook`  <a name="cfn-attributes-updatepolicy-codedeploylambdaaliasupdate-beforeallowtraffichook"></a>
The name of the Lambda function to run before traffic routing starts.  
*Required*: No  
*Type: *String

`DeploymentGroupName`  <a name="cfn-attributes-updatepolicy-codedeploylambdaaliasupdate-deploymentgroupname"></a>
The name of the CodeDeploy deployment group. This is where the traffic-shifting policy is set.  
*Required*: Yes  
*Type: *String

For an example that specifies the `UpdatePolicy` attribute for an `AWS::Lambda::Alias` resource, see [Lambda alias update policy](#aws-resource-lambda-alias-example).

## Examples
<a name="aws-attribute-updatepolicy-examples"></a>

The following examples show how to add an update policy to an Auto Scaling group and how to maintain availability when updating metadata.

### Add an `UpdatePolicy` to an Auto Scaling group
<a name="aws-attribute-updatepolicy-example-1"></a>

The following example shows how to add an update policy. During an update, the Auto Scaling group updates instances in batches of two and keeps a minimum of one instance in service. Because the `WaitOnResourceSignals` flag is set, the Auto Scaling group waits for new instances that are added to the group. The new instances must signal the Auto Scaling group before it updates the next batch of instances.

#### JSON
<a name="attribute-updatepolicy-example-1.json"></a>

```
"ASG" : {
  "Type":"AWS::AutoScaling::AutoScalingGroup",
  "Properties":{
    "VPCZoneIdentifier":[ "{{subnetIdAz1}}", "{{subnetIdAz2}}", "{{subnetIdAz3}}" ],
    "LaunchTemplate":{
      "LaunchTemplateId":{
        "Ref":"{{logicalName}}"
      },
      "Version":{
        "Fn::GetAtt":[
          "{{logicalName}}",
          "LatestVersionNumber"
        ]
      }
    },
    "MaxSize":"4",
    "MinSize":"1"
  },
  "UpdatePolicy":{
    "AutoScalingScheduledAction":{
      "IgnoreUnmodifiedGroupSizeProperties":"true"
    },
    "AutoScalingRollingUpdate":{
      "MinInstancesInService":"1",
      "MaxBatchSize":"2",
      "WaitOnResourceSignals":"true",
      "PauseTime":"PT10M",
      "SuspendProcesses":[
        "HealthCheck",
        "ReplaceUnhealthy",
        "AZRebalance",
        "AlarmNotification",
        "ScheduledActions",
        "InstanceRefresh"
      ]
    }
  }
}
```

#### YAML
<a name="attribute-updatepolicy-example-1.yaml"></a>

```
ASG:
  Type: AWS::AutoScaling::AutoScalingGroup
  Properties:
    VPCZoneIdentifier:
      - {{subnetIdAz1}}
      - {{subnetIdAz2}}
      - {{subnetIdAz3}}
    LaunchTemplate:
      LaunchTemplateId: !Ref {{logicalName}}
      Version: !GetAtt {{logicalName}}.LatestVersionNumber
    MaxSize: '4'
    MinSize: '1'
  UpdatePolicy:
    AutoScalingScheduledAction:
      IgnoreUnmodifiedGroupSizeProperties: 'true'
    AutoScalingRollingUpdate:
      MinInstancesInService: '1'
      MaxBatchSize: '2'
      WaitOnResourceSignals: 'true'
      PauseTime: PT10M
      SuspendProcesses:
        - HealthCheck
        - ReplaceUnhealthy
        - AZRebalance
        - AlarmNotification
        - ScheduledActions
        - InstanceRefresh
```

### AutoScalingReplacingUpdate policy
<a name="attribute-updatepolicy-AutoScalingReplacingUpdate"></a>

The following example declares a policy that forces an associated Auto Scaling group to be replaced during an update. For the update to succeed, a percentage of instances (specified by the `MinSuccessfulPercentParameter` parameter) must signal success within the `Timeout` period.

#### JSON
<a name="attribute-updatepolicy-example-2.json"></a>

```
"UpdatePolicy" : {
  "AutoScalingReplacingUpdate" : {
    "WillReplace" : true
  }
},
"CreationPolicy" : {
  "ResourceSignal" : {
    "Count" : { "Ref" : "ResourceSignalsOnCreate"},
    "Timeout" : "PT10M"
  },
  "AutoScalingCreationPolicy" : {
    "MinSuccessfulInstancesPercent" : { "Ref" : "MinSuccessfulPercentParameter" }
  }
}
```

#### YAML
<a name="attribute-updatepolicy-example-2.yaml"></a>

```
UpdatePolicy:
  AutoScalingReplacingUpdate:
    WillReplace: true
CreationPolicy:
  ResourceSignal:
    Count: !Ref 'ResourceSignalsOnCreate'
    Timeout: PT10M
  AutoScalingCreationPolicy:
    MinSuccessfulInstancesPercent: !Ref 'MinSuccessfulPercentParameter'
```

### AutoScalingInstanceRefresh policy
<a name="attribute-updatepolicy-AutoScalingInstanceRefresh"></a>

The following examples show two common configurations of the `AutoScalingInstanceRefresh` policy. The first example uses launch-before-terminate to maintain capacity during the refresh. The second example uses a CloudWatch alarm to roll back the stack if the deployment causes problems.

#### Launch-before-terminate refresh
<a name="attribute-updatepolicy-AutoScalingInstanceRefresh-lbt"></a>

The following example declares an `AutoScalingInstanceRefresh` policy that uses launch-before-terminate. Setting `MinHealthyPercentage` to `100` ensures new instances launch before existing ones terminate, and `MaxHealthyPercentage` of `200` lets the group temporarily double in size. The policy also skips instances that already match the configuration.

##### JSON
<a name="attribute-updatepolicy-AutoScalingInstanceRefresh-lbt.json"></a>

```
"ASG" : {
  "Type" : "AWS::AutoScaling::AutoScalingGroup",
  "Properties" : {
    "VPCZoneIdentifier" : [ "{{subnetIdAz1}}", "{{subnetIdAz2}}", "{{subnetIdAz3}}" ],
    "LaunchTemplate" : {
      "LaunchTemplateId" : { "Ref" : "{{logicalName}}" },
      "Version" : { "Fn::GetAtt" : [ "{{logicalName}}", "LatestVersionNumber" ] }
    },
    "MaxSize" : "4",
    "MinSize" : "1"
  },
  "UpdatePolicy" : {
    "AutoScalingInstanceRefresh" : {
      "Strategy" : "Rolling",
      "Preferences" : {
        "MinHealthyPercentage" : 100,
        "MaxHealthyPercentage" : 200,
        "SkipMatching" : true
      }
    }
  }
}
```

##### YAML
<a name="attribute-updatepolicy-AutoScalingInstanceRefresh-lbt.yaml"></a>

```
ASG:
  Type: AWS::AutoScaling::AutoScalingGroup
  Properties:
    VPCZoneIdentifier:
      - {{subnetIdAz1}}
      - {{subnetIdAz2}}
      - {{subnetIdAz3}}
    LaunchTemplate:
      LaunchTemplateId: !Ref {{logicalName}}
      Version: !GetAtt {{logicalName}}.LatestVersionNumber
    MaxSize: '4'
    MinSize: '1'
  UpdatePolicy:
    AutoScalingInstanceRefresh:
      Strategy: Rolling
      Preferences:
        MinHealthyPercentage: 100
        MaxHealthyPercentage: 200
        SkipMatching: true
```

#### Refresh with alarm-based rollback
<a name="attribute-updatepolicy-AutoScalingInstanceRefresh-alarm"></a>

The following example declares an `AutoScalingInstanceRefresh` policy with checkpoints, alarm-based rollback, and a bake time. Auto Scaling pauses for 5 minutes at each checkpoint, and waits 10 minutes after completion before declaring success.

##### JSON
<a name="attribute-updatepolicy-AutoScalingInstanceRefresh-alarm.json"></a>

```
"ASG" : {
  "Type" : "AWS::AutoScaling::AutoScalingGroup",
  "Properties" : {
    "VPCZoneIdentifier" : [ "{{subnetIdAz1}}", "{{subnetIdAz2}}", "{{subnetIdAz3}}" ],
    "LaunchTemplate" : {
      "LaunchTemplateId" : { "Ref" : "{{logicalName}}" },
      "Version" : { "Fn::GetAtt" : [ "{{logicalName}}", "LatestVersionNumber" ] }
    },
    "MaxSize" : "4",
    "MinSize" : "1"
  },
  "UpdatePolicy" : {
    "AutoScalingInstanceRefresh" : {
      "Strategy" : "Rolling",
      "Preferences" : {
        "CheckpointPercentages" : [ 33, 66, 100 ],
        "CheckpointDelay" : 300,
        "BakeTime" : 600,
        "AlarmSpecification" : {
          "Alarms" : [ "{{my-cloud-watch-alarm}}" ]
        }
      }
    }
  }
}
```

##### YAML
<a name="attribute-updatepolicy-AutoScalingInstanceRefresh-alarm.yaml"></a>

```
ASG:
  Type: AWS::AutoScaling::AutoScalingGroup
  Properties:
    VPCZoneIdentifier:
      - {{subnetIdAz1}}
      - {{subnetIdAz2}}
      - {{subnetIdAz3}}
    LaunchTemplate:
      LaunchTemplateId: !Ref {{logicalName}}
      Version: !GetAtt {{logicalName}}.LatestVersionNumber
    MaxSize: '4'
    MinSize: '1'
  UpdatePolicy:
    AutoScalingInstanceRefresh:
      Strategy: Rolling
      Preferences:
        CheckpointPercentages:
          - 33
          - 66
          - 100
        CheckpointDelay: 300
        BakeTime: 600
        AlarmSpecification:
          Alarms:
            - {{my-cloud-watch-alarm}}
```

### Maintain availability when updating the metadata for the cfn-init helper script
<a name="aws-attribute-updatepolicy-cfn-init-metadata"></a>

When you install software applications on your instances, you might use the [`AWS::CloudFormation::Init`](aws-resource-init.md) metadata key and the [cfn-init](cfn-init.md) helper script to bootstrap the instances in your Auto Scaling group. CloudFormation installs the packages, runs the commands, and performs other bootstrapping actions described in the metadata.

When you update only the metadata (for example, when updating a package to another version), you can use the [cfn-hup](cfn-hup.md) helper daemon to detect and apply the updates. However, the `cfn-hup` daemon runs independently on each instance. If the daemon happens to runs at the same time on all instances, your application or service might be unavailable during the update. To guarantee availability, you can force a rolling update so that CloudFormation updates your instances one batch at a time.

**Important**  
Forcing a rolling update requires CloudFormation to create a new instance and then delete the old one. Any information stored on the old instance is lost.

To force a rolling update, change the logical ID of the launch configuration resource, and then update the stack and any references pointing to the original logic ID (such as the associated Auto Scaling group). CloudFormation triggers a rolling update on the Auto Scaling group, replacing all instances.

### Original template
<a name="aws-attribute-updatepolicy-cfn-init-metadata-original"></a>

```
"LaunchConfig": {
  "Type" : "AWS::AutoScaling::LaunchConfiguration",
  "Metadata" : {
    "Comment" : "Install a simple PHP application",
    "AWS::CloudFormation::Init" : {
    ...
    }
  }
}
```

### Updated logical ID
<a name="aws-attribute-updatepolicy-cfn-init-metadata-updated"></a>

```
"LaunchConfigUpdateRubygemsPkg": {
  "Type" : "AWS::AutoScaling::LaunchConfiguration",
  "Metadata" : {
    "Comment" : "Install a simple PHP application",
    "AWS::CloudFormation::Init" : {
    ...
    }
  }
}
```

### Lambda alias update policy
<a name="aws-resource-lambda-alias-example"></a>

The following example specifies the `UpdatePolicy` attribute for an `AWS::Lambda::Alias` resource. All the details for the deployment are defined by the application and deployment group that are passed into the policy.

#### JSON
<a name="aws-attribute-updatepolicy-codedeploylambda.json"></a>

```
"Alias": {
  "Type": "AWS::Lambda::Alias",
  "Properties": {
    "FunctionName": {
      "Ref": "LambdaFunction"
    },
    "FunctionVersion": {
      "Fn::GetAtt": [
        "FunctionVersionTwo",
        "Version"
      ]
    },
    "Name": "MyAlias"
  },
  "UpdatePolicy": {
    "CodeDeployLambdaAliasUpdate": {
      "ApplicationName": {
        "Ref": "CodeDeployApplication"
      },
      "DeploymentGroupName": {
        "Ref": "CodeDeployDeploymentGroup"
      },
      "BeforeAllowTrafficHook": {
        "Ref": "PreHookLambdaFunction"
      },
      "AfterAllowTrafficHook": {
        "Ref": "PreHookLambdaFunction"
      }
    }
  }
}
```

#### YAML
<a name="aws-attribute-updatepolicy-codedeploylambda-example.yaml"></a>

```
Alias:
  Type: AWS::Lambda::Alias
  Properties:
    FunctionName: !Ref LambdaFunction
    FunctionVersion: !GetAtt FunctionVersionTwo.Version
    Name: MyAlias
  UpdatePolicy:
    CodeDeployLambdaAliasUpdate:
      ApplicationName: !Ref CodeDeployApplication
      DeploymentGroupName: !Ref CodeDeployDeploymentGroup
      BeforeAllowTrafficHook: !Ref PreHookLambdaFunction
      AfterAllowTrafficHook: !Ref PreHookLambdaFunction
```