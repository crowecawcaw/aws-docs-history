This is the new _AWS CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# `UpdatePolicy` attribute

Use the `UpdatePolicy` attribute to specify how AWS CloudFormation handles updates to certain
resources during stack update operations.

###### Topics

- [Overview](#aws-resource-update-policies "#aws-resource-update-policies")
- [AppStream 2.0 update policy](#aws-attribute-update-policy-app-stream-fleet "#aws-attribute-update-policy-app-stream-fleet")
- [AutoScalingReplacingUpdate
  policy](#cfn-attributes-updatepolicy-replacingupdate "#cfn-attributes-updatepolicy-replacingupdate")
- [AutoScalingRollingUpdate
  policy](#cfn-attributes-updatepolicy-rollingupdate "#cfn-attributes-updatepolicy-rollingupdate")
- [AutoScalingScheduledAction
  policy](#cfn-attributes-updatepolicy-scheduledactions "#cfn-attributes-updatepolicy-scheduledactions")
- [UseOnlineResharding
  policy](#cfn-attributes-updatepolicy-useonlineresharding "#cfn-attributes-updatepolicy-useonlineresharding")
- [EnableVersionUpgrade
  policy](#cfn-attributes-updatepolicy-upgradeopensearchdomain "#cfn-attributes-updatepolicy-upgradeopensearchdomain")
- [CodeDeployLambdaAliasUpdate policy](#cfn-attributes-updatepolicy-codedeploylambdaaliasupdate "#cfn-attributes-updatepolicy-codedeploylambdaaliasupdate")
- [Examples](#aws-attribute-updatepolicy-examples "#aws-attribute-updatepolicy-examples")

## Overview

By using the `UpdatePolicy` attribute, you can control how the following
resources are updated, as described here:

- [AWS::AppStream::Fleet](aws-resource-appstream-fleet.md "aws-resource-appstream-fleet.md") – CloudFormation can stop and start a fleet,
  which causes the fleet's instances to be replaced. By doing so, all instances will have
  the latest changes applied immediately after a stack update.
- [AWS::AutoScaling::AutoScalingGroup](aws-resource-autoscaling-autoscalinggroup.md "aws-resource-autoscaling-autoscalinggroup.md") – With
  Auto Scaling groups, you can use one or more update policies to control how CloudFormation handles
  certain updates. These policies include:
  - `AutoScalingReplacingUpdate` and
    `AutoScalingRollingUpdate` policies – CloudFormation can
    either replace the Auto Scaling group and its instances with an
    `AutoScalingReplacingUpdate` policy, or replace only the instances with
    an `AutoScalingRollingUpdate` policy. These replacement operations occur
    when you make one or more of the following changes:

        - Change the Auto Scaling group's [AWS::AutoScaling::LaunchConfiguration](aws-resource-autoscaling-launchconfiguration.md "aws-resource-autoscaling-launchconfiguration.md").
        - Change the Auto Scaling group's `VPCZoneIdentifier` property.
        - Change the Auto Scaling group's `LaunchTemplate` property.
        - Change the Auto Scaling group's `PlacementGroup` property.
        - Update an Auto Scaling group that contains instances that don't match the current
         `LaunchConfiguration`.

    If both the `AutoScalingReplacingUpdate` and
    `AutoScalingRollingUpdate` policies are specified, setting the
    `WillReplace` property to `true` gives
    `AutoScalingReplacingUpdate` precedence.

  - `AutoScalingScheduledAction` policy
    – This policy applies when you update a stack that includes an Auto Scaling group with
    scheduled actions that scale the group at specific times. CloudFormation can't modify the
    minimum size, maximum size, or desired capacity of the group unless they have been
    explicitly changed in the stack template. This policy helps to prevent any unexpected
    updates that could interfere with the scheduled scaling activities.

- [AWS::ElastiCache::ReplicationGroup](aws-resource-elasticache-replicationgroup.md "aws-resource-elasticache-replicationgroup.md") –
  CloudFormation can modify a replication group's shards by adding or removing shards, rather
  than replacing the entire resource.
- [AWS::OpenSearchService::Domain](aws-resource-opensearchservice-domain.md "aws-resource-opensearchservice-domain.md") and [AWS::Elasticsearch::Domain](aws-resource-elasticsearch-domain.md "aws-resource-elasticsearch-domain.md") (legacy) –
  CloudFormation can upgrade an OpenSearch Service domain to a new version of OpenSearch or Elasticsearch
  without replacing the entire resource.
- [AWS::Lambda::Alias](aws-resource-lambda-alias.md "aws-resource-lambda-alias.md") – CloudFormation can perform a
  CodeDeploy deployment when the version changes on the alias.

The sections that follow describe the syntax and properties for the
`UpdatePolicy` attribute supported by each resource type.

## AppStream 2.0 update policy

To stop an AppStream 2.0 fleet before an update and restart it after an update, use the AppStream 2.0
update policy.

### Syntax

#### JSON

```
{
    "UpdatePolicy": {
        "StopBeforeUpdate": {
            "Type": "`Boolean`"
        },
        "StartAfterUpdate": {
            "Type": "`Boolean`"
        }
    }
}
```

#### YAML

```
UpdatePolicy:
  StopBeforeUpdate:
    Type: `Boolean`
  StartAfterUpdate:
    Type: `Boolean`
```

`StopBeforeUpdate`

Stops the specified fleet before the update.

_Required_: No

`StartAfterUpdate`

Starts the specified fleet after the update.

_Required_: No

## AutoScalingReplacingUpdate

policy

To replace the Auto Scaling group and the instances it contains, use the
`AutoScalingReplacingUpdate` policy.

Before attempting an update, ensure that you have sufficient Amazon EC2 capacity for both your
old and new Auto Scaling groups.

### Syntax

#### JSON

```
"UpdatePolicy" : {
  "AutoScalingReplacingUpdate" : {
    "WillReplace" : `Boolean`
  }
}
```

#### YAML

```
UpdatePolicy:
  AutoScalingReplacingUpdate:
    WillReplace: `Boolean`
```

### Properties

`WillReplace`

Specifies whether an Auto Scaling group and the instances it contains are replaced during
an update. During replacement, CloudFormation retains the old group until it finishes
creating the new one. If the update fails, CloudFormation can roll back to the old Auto Scaling
group and delete the new Auto Scaling group.

While CloudFormation creates the new group, it doesn't detach or attach any instances.
After successfully creating the new Auto Scaling group, CloudFormation deletes the old Auto Scaling group
during the cleanup process.

When you set the `WillReplace` parameter, remember to specify a
matching [CreationPolicy attribute](aws-attribute-creationpolicy.md "aws-attribute-creationpolicy.md"). If the minimum number of instances
(specified by the `MinSuccessfulInstancesPercent` property) don't signal
success within the `Timeout` period (specified in the
`CreationPolicy` attribute), the replacement update fails and CloudFormation
rolls back to the old Auto Scaling group.

_Type_: Boolean

_Required_: No

## AutoScalingRollingUpdate

policy

To perform a rolling update of the instances in an Auto Scaling group rather than wait for scaling
activities to gradually replace older instances with newer instances, use the
`AutoScalingRollingUpdate` policy. This policy provides you the flexibility to
specify whether CloudFormation replaces instances that are in an Auto Scaling group in batches or all at
once without replacing the entire resource.

Things to consider when using an `AutoScalingRollingUpdate` policy:

- When CloudFormation rolls back an update, it uses the `UpdatePolicy`
  configuration specified in the template before the current stack update. For example, you
  change the `MaxBatchSize` from 1 to 10 in the `UpdatePolicy`,
  perform a stack update, and that update fails. CloudFormation will use 1 as the maximum batch
  size when it rolls back, not 10. To avoid this scenario, make changes to the
  `UpdatePolicy` in a separate update before any updates to the Auto Scaling group that
  are likely to initiate rolling updates.
- CloudFormation recommends specifying the `SuspendProcesses` property to
  temporarily suspend Amazon EC2 Auto Scaling processes that might interfere with the rolling update and
  cause it to fail. For more information, see [How can I update
  my Auto Scaling group when I update my CloudFormation stack?](https://repost.aws/knowledge-center/auto-scaling-group-rolling-updates "https://repost.aws/knowledge-center/auto-scaling-group-rolling-updates")
- CloudFormation supports using Amazon EC2 Auto Scaling lifecycle hooks when launching or terminating
  instances. This gives you time to perform custom actions on an instance before it moves to
  the next state. To make sure that new instances reach the `InService` state,
  complete the lifecycle hook with a `CONTINUE` result when the custom action
  finishes. By default, if no response is received and the lifecycle hook times out, the
  instance launch will be considered unsuccessful and abandoned. If no instances reach the
  `InService` state, the rolling update will eventually fail.
- Amazon EC2 Auto Scaling features such as instance maintenance policies, termination policies, and
  scale-in protection are not available for use with CloudFormation rolling updates. Plan your
  rolling updates accordingly.
- If you use an `AutoScalingRollingUpdate` policy and remove the placement
  group setting, the placement group will be removed from the Auto Scaling group and the CloudFormation
  template. Also this triggers a rolling update, so new instances won't be launched into a
  placement group.

### Syntax

#### JSON

```
"UpdatePolicy" : {
  "AutoScalingRollingUpdate" : {
    "MaxBatchSize" : `Integer`,
    "MinActiveInstancesPercent" : `Integer`,
    "MinInstancesInService" : `Integer`,
    "MinSuccessfulInstancesPercent" : `Integer`,
    "PauseTime" : `String`,
    "SuspendProcesses" : [ `List of processes` ],
    "WaitOnResourceSignals" : `Boolean`
  }
}
```

#### YAML

```
UpdatePolicy:
  AutoScalingRollingUpdate:
    MaxBatchSize: `Integer`
    MinActiveInstancesPercent: `Integer`
    MinInstancesInService: `Integer`
    MinSuccessfulInstancesPercent: `Integer`
    PauseTime: `String`
    SuspendProcesses:
      - `List of processes`
    WaitOnResourceSignals: `Boolean`
```

### Properties

`MaxBatchSize`

Specifies the maximum number of instances that can be replaced
simultaneously.

_Default_: `1`

_Maximum_: `100`

_Type_: Integer

_Required_: No

`MinActiveInstancesPercent`

Specifies the percentage of instances in an Auto Scaling group that must be in the
`InService` state relative to that group's desired capacity during a
rolling update for an update to succeed. You can specify a value from 0 to 100.
CloudFormation rounds to the nearest tenth of a percent. For example, if you update five
instances with a minimum `InService` percentage of 50, at least three
instances must be in the `InService` state. If an instance doesn't
transition to the `InService` state within a fixed time of 1 hour,
CloudFormation assumes that the instance wasn't updated.

Setting `MinActiveInstancesPercent` in your `UpdatePolicy`
will also affect instances launched when the `DesiredCapacity` property of
the `AWS::AutoScaling::AutoScalingGroup` resource is set higher than the
current desired capacity of that Auto Scaling group.

_Default_: `100`

_Type_: Integer

_Required_: No

`MinInstancesInService`

Specifies the minimum number of instances that must be in service within the Auto Scaling
group while CloudFormation updates old instances. This value must be less than the [MaxSize](aws-resource-autoscaling-autoscalinggroup.md#cfn-autoscaling-autoscalinggroup-maxsize "aws-resource-autoscaling-autoscalinggroup.md#cfn-autoscaling-autoscalinggroup-maxsize") of the Auto Scaling group.

###### Warning

We recommend that you set the value of the `MinInstancesInService`
property to at least the [MinSize](aws-resource-autoscaling-autoscalinggroup.md#cfn-autoscaling-autoscalinggroup-minsize "aws-resource-autoscaling-autoscalinggroup.md#cfn-autoscaling-autoscalinggroup-minsize") of the Auto Scaling group. This avoids potential
availability issues during a rolling update due to 0 instances serving customer
traffic.

_Default_: `0`

_Type_: Integer

_Required_: No

`MinSuccessfulInstancesPercent`

Specifies the percentage of instances in an Auto Scaling rolling update that must signal
success for an update to succeed. You can specify a value from 0 to 100. CloudFormation
rounds to the nearest tenth of a percent. For example, if you update five instances
with a minimum successful percentage of `50`, three instances must signal
success. If an instance doesn't send a signal within the time specified in the
`PauseTime` property, CloudFormation assumes that the instance wasn't
updated.

We recommend that you set the value of the
`MinSuccessfulInstancesPercent` property to a value greater than 0. When
the `MinSuccessfulInstancesPercent` property is set to 0, CloudFormation waits
for 0% of the capacity instances to be in an `InService` state.
`MinSuccessfulInstancesPercent` returns immediately and before
considering the Auto Scaling group status as `UPDATE_COMPLETE` to move on to the
subsequent resources defined in the stack template. If other Auto Scaling groups are defined
in your CloudFormation template, they will update simultaneously. When all Auto Scaling groups are
deployed at once with 0% of the capacity instances in an `InService` state,
then you will experience availability issues, due to 0 instances serving customer
traffic.

_Default_: `100`

_Type_: Integer

_Required_: No

`PauseTime`

The amount of time that CloudFormation pauses after making a change to a batch of
instances to give those instances time to start software applications.

Specify `PauseTime` in the [ISO8601 duration
format](https://en.wikipedia.org/wiki/ISO_8601#Durations "https://en.wikipedia.org/wiki/ISO_8601#Durations") (in the format
`PT`#`H`#`M`#`S`,
where each `#` is the number of hours, minutes, and seconds,
respectively). The maximum `PauseTime` is one hour
(`PT1H`).

###### Warning

When `WaitOnResourceSignals` is set to `true`,
`PauseTime` acts as a timeout value. It determines the maximum time
that CloudFormation waits to receive the required number of valid signals from the
instances being replaced during a rolling update and from new instances being added
by increasing the [DesiredCapacity](aws-resource-autoscaling-autoscalinggroup.md#cfn-autoscaling-autoscalinggroup-desiredcapacity "aws-resource-autoscaling-autoscalinggroup.md#cfn-autoscaling-autoscalinggroup-desiredcapacity") property of the
`AWS::AutoScaling::AutoScalingGroup` resource. If the
`PauseTime` is exceeded before CloudFormation receives the expected
signals, the update fails. For best results, specify a time period that provides
sufficient time for your applications to start up. If the update needs to be rolled
back, a short `PauseTime` can cause the rollback to fail.

_Default_: `PT5M` (5 minutes) when the
`WaitOnResourceSignals` property is set to `true`. Otherwise,
no default value is set.

_Type_: String

_Required_: No

`SuspendProcesses`

Specifies the Auto Scaling processes to suspend during a stack update. Suspending
processes prevents Auto Scaling from interfering with a stack update. For example, you can
suspend alarming so that Amazon EC2 Auto Scaling doesn't initiate scaling policies associated with an
alarm. For valid values, see [Types
of processes](../../../autoscaling/ec2/userguide/as-suspend-resume-processes.md#process-types "../../../autoscaling/ec2/userguide/as-suspend-resume-processes.md#process-types") in the _Amazon EC2 Auto Scaling User Guide_.

_Default_: Not specified

_Type_: List of Auto Scaling processes

_Required_: No

`WaitOnResourceSignals`

Specifies whether CloudFormation waits for success signals from new instances before
continuing the update. CloudFormation waits for the specified `PauseTime`
duration for success signals.

To signal the Auto Scaling group, use the [cfn-signal](cfn-signal.md "cfn-signal.md") helper script. For Auto Scaling groups associated with Elastic Load Balancing,
consider adding a health check to ensure that instances are healthy before signaling
success by using the [cfn-init](cfn-init.md "cfn-init.md") helper
script. For an example, see the `verify_instance_health` command in the
sample templates for Amazon EC2 Auto Scaling rolling updates in our [GitHub repository](https://github.com/aws-cloudformation/aws-cloudformation-templates/tree/main/AutoScaling "https://github.com/aws-cloudformation/aws-cloudformation-templates/tree/main/AutoScaling").

_Default_: `false`

_Type_: Boolean

_Required_: Conditional. If you specify the
`MinSuccessfulInstancesPercent` property, the
`WaitOnResourceSignals` property must be set to `true`.

## AutoScalingScheduledAction

policy

To specify how CloudFormation handles updates for the `MinSize`,
`MaxSize`, and `DesiredCapacity` properties when the
`AWS::AutoScaling::AutoScalingGroup` resource has an associated scheduled action,
use the `AutoScalingScheduledAction` policy.

With scheduled actions, the group size properties of an Auto Scaling group can change at any time.
When you update a stack with an Auto Scaling group and scheduled action, CloudFormation always sets the
group size property values of your Auto Scaling group to the values that are defined in the
`AWS::AutoScaling::AutoScalingGroup` resource of your template, even if a
scheduled action is in effect.

If you don't want CloudFormation to change any of the group size property values when you have
a scheduled action in effect, use the `AutoScalingScheduledAction` update policy
and set `IgnoreUnmodifiedGroupSizeProperties` to `true` to prevent
CloudFormation from changing the `MinSize`, `MaxSize`, or
`DesiredCapacity` properties unless you have modified these values in your
template.

### Syntax

#### JSON

```
"UpdatePolicy" : {
  "AutoScalingScheduledAction" : {
    "IgnoreUnmodifiedGroupSizeProperties" : `Boolean`
  }
}
```

#### YAML

```
UpdatePolicy:
  AutoScalingScheduledAction:
    IgnoreUnmodifiedGroupSizeProperties: `Boolean`
```

### Properties

`IgnoreUnmodifiedGroupSizeProperties`

If `true`, CloudFormation ignores differences in group size properties
between your current Auto Scaling group and the Auto Scaling group described in the
`AWS::AutoScaling::AutoScalingGroup` resource of your template during a
stack update. If you modify any of the group size property values in your template,
CloudFormation uses the modified values and updates your Auto Scaling group.

###### Note

This property is ignored during a stack rollback.

_Default_: `false`

_Type_: Boolean

_Required_: No

## UseOnlineResharding

policy

To modify a replication group's shards by adding or removing shards, rather than replacing
the entire [AWS::ElastiCache::ReplicationGroup](aws-resource-elasticache-replicationgroup.md "aws-resource-elasticache-replicationgroup.md") resource, use the
`UseOnlineResharding` update policy.

If `UseOnlineResharding` is set to `true`, you can update the
`NumNodeGroups` and `NodeGroupConfiguration` properties of the
`AWS::ElastiCache::ReplicationGroup` resource, and CloudFormation will update those
properties without interruption. When `UseOnlineResharding` is set to
`false`, or not specified, updating the `NumNodeGroups` and
`NodeGroupConfiguration` properties results in CloudFormation replacing the entire
`AWS::ElastiCache::ReplicationGroup` resource.

The `UseOnlineResharding` update policy has no properties.

Things to consider when setting the `UseOnlineResharding` update policy to
`true`:

- We strongly recommend you perform updates to the `NumNodeGroups` and
  `NodeGroupConfiguration` properties as the only updates in a given stack
  update operation.

Updating the node group configuration of a replication group is a resource-intensive
operation. If a stack update fails, CloudFormation doesn't roll back changes to the node group
configuration of a replication group. However, CloudFormation will roll back any other
properties that were changed as part of the failed update operation.

- Any node group updates require identifying all node groups.

If you specify the `NodeGroupConfiguration` property, you must also specify
the NodeGroupId for each node group configuration in order for CloudFormation to update the
number of nodes without interruption.

When creating a replication group, if you don't specify an ID for each node group,
ElastiCache automatically generates an ID for each node group. To update the replication group
without interruption, use the ElastiCache console ([https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/")) or [DescribeReplicationGroups](../../../AmazonElastiCache/latest/APIReference/API_DescribeReplicationGroups.md "../../../AmazonElastiCache/latest/APIReference/API_DescribeReplicationGroups.md")
to retrieve the IDs for all node groups in the replication group. Then specify the ID for
each node group in your stack template before attempting to add or remove shards.

###### Note

As a best practice, when you create a replication group in a stack template, include
an ID for each node group you specify.

In addition, updating the number of nodes without interruption requires that you have
accurately specified the `PrimaryAvailabilityZone`,
`ReplicaAvailabilityZones`, and `ReplicaCount` properties for each
`NodeGroupConfiguration` as well. Again, you can use the ElastiCache console
([https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/")) or [DescribeReplicationGroups](../../../AmazonElastiCache/latest/APIReference/API_DescribeReplicationGroups.md "../../../AmazonElastiCache/latest/APIReference/API_DescribeReplicationGroups.md")
to retrieve the actual values for each node group and compare them to the values in your
stack template. You can update the property values of the node groups as a separate stack
update, or as part of the same stack update that changes the number of node groups.

When you use an `UseOnlineResharding` update policy to update the number of
node groups without interruption, ElastiCache evenly distributes the keyspaces between the
specified number of slots. This can't be updated later. Therefore, after updating the
number of node groups in this way, you should remove the value specified for the
`Slots` property of each `NodeGroupConfiguration` from the stack
template, as it no longer reflects the actual values in each node group.

- Actual node group removal results may vary.

When you specify a `NumNodeGroups` value that's less than the current
number of node groups, CloudFormation instructs ElastiCache to remove as many node groups as
necessary to reach the specified number of nodes. However, ElastiCache may not always be able to
remove the desired number of node groups. In the event ElastiCache can't remove the desired
number of node groups, CloudFormation generates a stack event alerting you to this. In cases
where ElastiCache can't remove _any_ node groups, the CloudFormation resource
update fails.

For more information on modifying replication groups, see [ModifyReplicationGroupShardConfiguration](../../../AmazonElastiCache/latest/APIReference/API_ModifyReplicationGroupShardConfiguration.md "../../../AmazonElastiCache/latest/APIReference/API_ModifyReplicationGroupShardConfiguration.md") in the
_Amazon ElastiCache API Reference_.

### Syntax

#### JSON

```
"UpdatePolicy" : {
  "UseOnlineResharding" : `Boolean`
}
```

#### YAML

```
UpdatePolicy:
  UseOnlineResharding: `Boolean`
```

## EnableVersionUpgrade

policy

To upgrade an OpenSearch Service domain to a new version of OpenSearch or Elasticsearch rather than
replacing the entire [AWS::OpenSearchService::Domain](aws-resource-opensearchservice-domain.md "aws-resource-opensearchservice-domain.md") or [AWS::Elasticsearch::Domain](aws-resource-elasticsearch-domain.md "aws-resource-elasticsearch-domain.md")
resource, use the `EnableVersionUpgrade` update policy.

If `EnableVersionUpgrade` is set to `true`, you can update the
`EngineVersion` property of the `AWS::OpenSearchService::Domain`
resource (or the `ElasticsearchVersion` property of the legacy
`AWS::Elasticsearch::Domain` resource), and CloudFormation will update that property
without interruption. When `EnableVersionUpgrade` is set to `false`, or
not specified, updating the `EngineVersion` or `ElasticsearchVersion`
property results in CloudFormation replacing the entire
`AWS::OpenSearchService::Domain`/`AWS::Elasticsearch::Domain`
resource.

The `EnableVersionUpgrade` update policy has no properties.

For more information, see [Upgrading OpenSearch Service
domains](../../../opensearch-service/latest/developerguide/version-migration.md "../../../opensearch-service/latest/developerguide/version-migration.md") in the Amazon OpenSearch Service Developer Guide.

### Syntax

#### JSON

```
"UpdatePolicy" : {
  "EnableVersionUpgrade" : `Boolean`
}
```

#### YAML

```
UpdatePolicy:
  EnableVersionUpgrade: `Boolean`
```

## CodeDeployLambdaAliasUpdate policy

To perform an CodeDeploy deployment when the version changes on an
`AWS::Lambda::Alias` resource, use the `CodeDeployLambdaAliasUpdate`
update policy.

### Syntax

#### JSON

```
"UpdatePolicy" : {
  "CodeDeployLambdaAliasUpdate" : {
    "AfterAllowTrafficHook" : `String`,
    "ApplicationName" : `String`,
    "BeforeAllowTrafficHook" : `String`,
    "DeploymentGroupName" : `String`
  }
}
```

#### YAML

```
UpdatePolicy:
  CodeDeployLambdaAliasUpdate:
    AfterAllowTrafficHook: `String`
    ApplicationName: `String`
    BeforeAllowTrafficHook: `String`
    DeploymentGroupName: `String`
```

### Properties

`AfterAllowTrafficHook`

The name of the Lambda function to run after traffic routing completes.

_Required_: No

_Type:_ String

`ApplicationName`

The name of the CodeDeploy application.

_Required:_ Yes

_Type:_ String

`BeforeAllowTrafficHook`

The name of the Lambda function to run before traffic routing starts.

_Required_: No

_Type:_ String

`DeploymentGroupName`

The name of the CodeDeploy deployment group. This is where the traffic-shifting policy
is set.

_Required_: Yes

_Type:_ String

For an example that specifies the `UpdatePolicy` attribute for an
`AWS::Lambda::Alias` resource, see [Lambda alias update policy](#aws-resource-lambda-alias-example "#aws-resource-lambda-alias-example").

## Examples

The following examples show how to add an update policy to an Auto Scaling group and how to
maintain availability when updating metadata.

### Add an `UpdatePolicy` to

an Auto Scaling group

The following example shows how to add an update policy. During an update, the Auto Scaling
group updates instances in batches of two and keeps a minimum of one instance in service.
Because the `WaitOnResourceSignals` flag is set, the Auto Scaling group waits for new
instances that are added to the group. The new instances must signal the Auto Scaling group before
it updates the next batch of instances.

#### JSON

```
"ASG" : {
  "Type":"AWS::AutoScaling::AutoScalingGroup",
  "Properties":{
    "VPCZoneIdentifier":[ "`subnetIdAz1`", "`subnetIdAz2`", "`subnetIdAz3`" ],
    "LaunchTemplate":{
      "LaunchTemplateId":{
        "Ref":"`logicalName`"
      },
      "Version":{
        "Fn::GetAtt":[
          "`logicalName`",
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

```
ASG:
  Type: 'AWS::AutoScaling::AutoScalingGroup'
  Properties:
    VPCZoneIdentifier:
      - `subnetIdAz1`
      - `subnetIdAz2`
      - `subnetIdAz3`
    LaunchTemplate:
      LaunchTemplateId: !Ref `logicalName`
      Version: !GetAtt `logicalName`.LatestVersionNumber
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

The following example declares a policy that forces an associated Auto Scaling group to be
replaced during an update. For the update to succeed, a percentage of instances (specified
by the `MinSuccessfulPercentParameter` parameter) must signal success within the
`Timeout` period.

#### JSON

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

### Maintain availability when

updating the metadata for the cfn-init helper script

When you install software applications on your instances, you might use the [AWS::CloudFormation::Init](aws-resource-init.md "aws-resource-init.md") metadata key and the [cfn-init](cfn-init.md "cfn-init.md") helper script to bootstrap the instances in
your Auto Scaling group. CloudFormation installs the packages, runs the commands, and performs other
bootstrapping actions described in the metadata.

When you update only the metadata (for example, when updating a package to another
version), you can use the [cfn-hup](cfn-hup.md "cfn-hup.md") helper daemon to
detect and apply the updates. However, the `cfn-hup` daemon runs independently on
each instance. If the daemon happens to runs at the same time on all instances, your
application or service might be unavailable during the update. To guarantee availability,
you can force a rolling update so that CloudFormation updates your instances one batch at a
time.

###### Important

Forcing a rolling update requires CloudFormation to create a new instance and then delete
the old one. Any information stored on the old instance is lost.

To force a rolling update, change the logical ID of the launch configuration resource,
and then update the stack and any references pointing to the original logic ID (such as the
associated Auto Scaling group). CloudFormation triggers a rolling update on the Auto Scaling group, replacing
all instances.

### Original

template

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

### Updated logical

ID

```
"**LaunchConfigUpdateRubygemsPkg**": {
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

The following example specifies the `UpdatePolicy` attribute for an
`AWS::Lambda::Alias` resource. All the details for the deployment are defined
by the application and deployment group that are passed into the policy.

#### JSON

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

```
Alias:
  Type: 'AWS::Lambda::Alias'
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
