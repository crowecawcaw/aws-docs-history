# Configure Amazon EC2 Auto Scaling resources with CloudFormation

The following examples show different snippets to include in templates for use with
Amazon EC2 Auto Scaling.

###### Snippet categories

- [Create a single instance Amazon EC2 Auto Scaling
  group](#scenario-single-instance-as-group "#scenario-single-instance-as-group")
- [Create an Amazon EC2 Auto Scaling group with an attached load
  balancer](#scenario-as-group "#scenario-as-group")
- [Create an Amazon EC2 Auto Scaling group with notifications](#scenario-as-notification "#scenario-as-notification")
- [Create an Amazon EC2 Auto Scaling group that uses a
  CreationPolicy and an UpdatePolicy](#scenario-as-updatepolicy "#scenario-as-updatepolicy")
- [Create a step scaling policy](#scenario-step-scaling-policy "#scenario-step-scaling-policy")
- [Mixed instances group
  examples](#scenario-mixed-instances-group-template-examples "#scenario-mixed-instances-group-template-examples")
- [Launch configuration
  examples](#scenario-launch-config-template-examples "#scenario-launch-config-template-examples")

## Create a single instance Amazon EC2 Auto Scaling

group

This example shows an [`AWS::AutoScaling::AutoScalingGroup`](../TemplateReference/aws-resource-autoscaling-autoscalinggroup.md "../TemplateReference/aws-resource-autoscaling-autoscalinggroup.md") resource with a single instance
to help you get started. The `VPCZoneIdentifier` property of the Amazon EC2 Auto Scaling group
specifies a list of existing subnets in three different Availability Zones. You must specify
the applicable subnet IDs from your account before you create your stack. The
`LaunchTemplate` property references an [`AWS::EC2::LaunchTemplate`](../TemplateReference/aws-resource-ec2-launchtemplate.md "../TemplateReference/aws-resource-ec2-launchtemplate.md") resource with the logical name
`myLaunchTemplate` that is defined elsewhere in your template.

###### Note

For examples of launch templates, see [Create launch templates with
CloudFormation](quickref-ec2-launch-templates.md "quickref-ec2-launch-templates.md") in the Amazon EC2 snippets section and the
[Examples](../TemplateReference/aws-resource-ec2-launchtemplate.md#aws-resource-ec2-launchtemplate--examples "../TemplateReference/aws-resource-ec2-launchtemplate.md#aws-resource-ec2-launchtemplate--examples") section in the `AWS::EC2::LaunchTemplate` resource.

### JSON

```

"myASG" : {
   "Type" : "AWS::AutoScaling::AutoScalingGroup",
   "Properties" : {
      "VPCZoneIdentifier" : [ "`subnetIdAz1`", "`subnetIdAz2`", "`subnetIdAz3`" ],
      "LaunchTemplate" : {
        "LaunchTemplateId" : {
          "Ref" : "`myLaunchTemplate`"
        },
        "Version" : {
          "Fn::GetAtt" : [
            "`myLaunchTemplate`",
            "LatestVersionNumber"
          ]
        }
      },
      "MaxSize" : "1",
      "MinSize" : "1"
   }
}
```

### YAML

```
myASG:
  Type: AWS::AutoScaling::AutoScalingGroup
  Properties:
    VPCZoneIdentifier:
      - `subnetIdAz1`
      - `subnetIdAz2`
      - `subnetIdAz3`
    LaunchTemplate:
      LaunchTemplateId: !Ref `myLaunchTemplate`
      Version: !GetAtt `myLaunchTemplate`.LatestVersionNumber
    MaxSize: '1'
    MinSize: '1'
```

## Create an Amazon EC2 Auto Scaling group with an attached load

balancer

This example shows an [`AWS::AutoScaling::AutoScalingGroup`](../TemplateReference/aws-resource-autoscaling-autoscalinggroup.md "../TemplateReference/aws-resource-autoscaling-autoscalinggroup.md") resource for load balancing
over multiple servers. It specifies the logical names of AWS resources declared elsewhere
in the same template.

1. The `VPCZoneIdentifier` property specifies the logical names of two
   [`AWS::EC2::Subnet`](../TemplateReference/aws-resource-ec2-subnet.md "../TemplateReference/aws-resource-ec2-subnet.md") resources where the Amazon EC2 Auto Scaling group's EC2
   instances will be created: `myPublicSubnet1` and
   `myPublicSubnet2`.
2. The `LaunchTemplate` property specifies an [`AWS::EC2::LaunchTemplate`](../TemplateReference/aws-resource-ec2-launchtemplate.md "../TemplateReference/aws-resource-ec2-launchtemplate.md") resource with the logical name
   `myLaunchTemplate`.
3. The `TargetGroupARNs` property lists the target groups for an Application Load Balancer or
   Network Load Balancer used to route traffic to the Amazon EC2 Auto Scaling group. In this example, one target group is
   specified, an [`AWS::ElasticLoadBalancingV2::TargetGroup`](../TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md "../TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md") resource with the
   logical name `myTargetGroup`.

### JSON

```

"myServerGroup" : {
   "Type" : "AWS::AutoScaling::AutoScalingGroup",
   "Properties" : {
      "VPCZoneIdentifier" : [ { "Ref" : "`myPublicSubnet1`" }, { "Ref" : "`myPublicSubnet2`" } ],
      "LaunchTemplate" : {
        "LaunchTemplateId" : {
          "Ref" : "`myLaunchTemplate`"
        },
        "Version" : {
          "Fn::GetAtt" : [
            "`myLaunchTemplate`",
            "LatestVersionNumber"
          ]
        }
      },
      "MaxSize" : "5",
      "MinSize" : "1",
      "TargetGroupARNs" : [ { "Ref" : "`myTargetGroup`" } ]
   }
}
```

### YAML

```
myServerGroup:
  Type: AWS::AutoScaling::AutoScalingGroup
  Properties:
    VPCZoneIdentifier:
      - !Ref `myPublicSubnet1`
      - !Ref `myPublicSubnet2`
    LaunchTemplate:
      LaunchTemplateId: !Ref `myLaunchTemplate`
      Version: !GetAtt `myLaunchTemplate`.LatestVersionNumber
    MaxSize: '5'
    MinSize: '1'
    TargetGroupARNs:
      - !Ref `myTargetGroup`
```

### See also

For a detailed example that creates an Amazon EC2 Auto Scaling group with a target tracking scaling
policy based on the `ALBRequestCountPerTarget` predefined metric for your
Application Load Balancer, see the [Examples](../TemplateReference/aws-resource-autoscaling-scalingpolicy.md#aws-resource-autoscaling-scalingpolicy--examples "../TemplateReference/aws-resource-autoscaling-scalingpolicy.md#aws-resource-autoscaling-scalingpolicy--examples") section in the `AWS::AutoScaling::ScalingPolicy`
resource.

## Create an Amazon EC2 Auto Scaling group with notifications

This example shows an [`AWS::AutoScaling::AutoScalingGroup`](../TemplateReference/aws-resource-autoscaling-autoscalinggroup.md "../TemplateReference/aws-resource-autoscaling-autoscalinggroup.md") resource that sends Amazon SNS
notifications when the specified events take place. The
`NotificationConfigurations` property specifies the SNS topic where CloudFormation sends
a notification and the events that will cause CloudFormation to send notifications. When the events
specified by `NotificationTypes` occur, CloudFormation will send a notification to the SNS
topic specified by `TopicARN`. When you launch the stack, CloudFormation creates an [`AWS::SNS::Subscription`](../TemplateReference/aws-resource-sns-subscription.md "../TemplateReference/aws-resource-sns-subscription.md") resource
(`snsTopicForAutoScalingGroup`) that's declared within the same
template.

The `VPCZoneIdentifier` property of the Amazon EC2 Auto Scaling group specifies a list of
existing subnets in three different Availability Zones. You must specify the applicable
subnet IDs from your account before you create your stack. The `LaunchTemplate`
property references the logical name of an [`AWS::EC2::LaunchTemplate`](../TemplateReference/aws-resource-ec2-launchtemplate.md "../TemplateReference/aws-resource-ec2-launchtemplate.md") resource declared elsewhere in the same
template.

### JSON

```
"myASG" : {
  "Type" : "AWS::AutoScaling::AutoScalingGroup",
  "DependsOn": [
    "snsTopicForAutoScalingGroup"
  ],
  "Properties" : {
    "VPCZoneIdentifier" : [ "`subnetIdAz1`", "`subnetIdAz2`", "`subnetIdAz3`" ],
    "LaunchTemplate" : {
      "LaunchTemplateId" : {
        "Ref" : "`logicalName`"
      },
      "Version" : {
        "Fn::GetAtt" : [
          "`logicalName`",
          "LatestVersionNumber"
        ]
      }
    },
    "MaxSize" : "5",
    "MinSize" : "1",
    "NotificationConfigurations" : [
      {
        "TopicARN" : { "Ref" : "snsTopicForAutoScalingGroup" },
        "NotificationTypes" : [
          "autoscaling:EC2_INSTANCE_LAUNCH",
          "autoscaling:EC2_INSTANCE_LAUNCH_ERROR",
          "autoscaling:EC2_INSTANCE_TERMINATE",
          "autoscaling:EC2_INSTANCE_TERMINATE_ERROR",
          "autoscaling:TEST_NOTIFICATION"
        ]
      }
    ]
  }
}
```

### YAML

```
myASG:
  Type: AWS::AutoScaling::AutoScalingGroup
  DependsOn:
    - snsTopicForAutoScalingGroup
  Properties:
    VPCZoneIdentifier:
      - `subnetIdAz1`
      - `subnetIdAz2`
      - `subnetIdAz3`
    LaunchTemplate:
      LaunchTemplateId: !Ref `logicalName`
      Version: !GetAtt `logicalName`.LatestVersionNumber
    MaxSize: '5'
    MinSize: '1'
    NotificationConfigurations:
      - TopicARN: !Ref snsTopicForAutoScalingGroup
        NotificationTypes:
          - autoscaling:EC2_INSTANCE_LAUNCH
          - autoscaling:EC2_INSTANCE_LAUNCH_ERROR
          - autoscaling:EC2_INSTANCE_TERMINATE
          - autoscaling:EC2_INSTANCE_TERMINATE_ERROR
          - autoscaling:TEST_NOTIFICATION
```

## Create an Amazon EC2 Auto Scaling group that uses a

`CreationPolicy` and an `UpdatePolicy`

The following example shows how to add `CreationPolicy` and
`UpdatePolicy` attributes to an [`AWS::AutoScaling::AutoScalingGroup`](../TemplateReference/aws-resource-autoscaling-autoscalinggroup.md "../TemplateReference/aws-resource-autoscaling-autoscalinggroup.md") resource.

The sample creation policy prevents the Amazon EC2 Auto Scaling group from reaching
`CREATE_COMPLETE` status until CloudFormation receives `Count` number of
success signals when the group is ready. To signal that the Amazon EC2 Auto Scaling group is ready, a
`cfn-signal` helper script added to the launch template's user data (not shown)
is run on the instances. If the instances don't send a signal within the specified
`Timeout`, CloudFormation assumes that the instances were not created, the resource
creation fails, and CloudFormation rolls the stack back.

The sample update policy instructs CloudFormation to perform a rolling update using the
`AutoScalingRollingUpdate` property. The rolling update makes changes to the
Amazon EC2 Auto Scaling group in small batches (for this example, instance by instance) based on the
`MaxBatchSize` and a pause time between batches of updates based on the
`PauseTime`. The `MinInstancesInService` attribute specifies the
minimum number of instances that must be in service within the Amazon EC2 Auto Scaling group while CloudFormation
updates old instances.

The `WaitOnResourceSignals` attribute is set to `true`. CloudFormation
must receive a signal from each new instance within the specified `PauseTime`
before continuing the update. While the stack update is in progress, the following EC2 Auto
Scaling processes are suspended: `HealthCheck`, `ReplaceUnhealthy`,
`AZRebalance`, `AlarmNotification`, and
`ScheduledActions`. Note: Don't suspend the `Launch`,
`Terminate`, or `AddToLoadBalancer` (if the Amazon EC2 Auto Scaling group is being used
with ELB) process types because doing so can prevent the rolling update from functioning
properly.

The `VPCZoneIdentifier` property of the Amazon EC2 Auto Scaling group specifies a list of
existing subnets in three different Availability Zones. You must specify the applicable
subnet IDs from your account before you create your stack. The `LaunchTemplate`
property references the logical name of an [`AWS::EC2::LaunchTemplate`](../TemplateReference/aws-resource-ec2-launchtemplate.md "../TemplateReference/aws-resource-ec2-launchtemplate.md") resource declared elsewhere in the same
template.

For more information about the `CreationPolicy` and `UpdatePolicy`
attributes, see [Resource attribute reference](../TemplateReference/aws-product-attribute-reference.md "../TemplateReference/aws-product-attribute-reference.md").

### JSON

```
{
  "Resources":{
    "myASG":{
      "CreationPolicy":{
        "ResourceSignal":{
          "Count":"3",
          "Timeout":"PT15M"
        }
      },
      "UpdatePolicy":{
        "AutoScalingRollingUpdate":{
          "MinInstancesInService":"3",
          "MaxBatchSize":"1",
          "PauseTime":"PT12M5S",
          "WaitOnResourceSignals":"true",
          "SuspendProcesses":[
            "HealthCheck",
            "ReplaceUnhealthy",
            "AZRebalance",
            "AlarmNotification",
            "ScheduledActions",
            "InstanceRefresh"
          ]
        }
      },
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
        "MaxSize":"5",
        "MinSize":"3"
      }
    }
  }
}
```

### YAML

```
---
Resources:
  myASG:
    CreationPolicy:
      ResourceSignal:
        Count: '3'
        Timeout: PT15M
    UpdatePolicy:
      AutoScalingRollingUpdate:
        MinInstancesInService: '3'
        MaxBatchSize: '1'
        PauseTime: PT12M5S
        WaitOnResourceSignals: true
        SuspendProcesses:
          - HealthCheck
          - ReplaceUnhealthy
          - AZRebalance
          - AlarmNotification
          - ScheduledActions
          - InstanceRefresh
    Type: AWS::AutoScaling::AutoScalingGroup
    Properties:
      VPCZoneIdentifier:
        - `subnetIdAz1`
        - `subnetIdAz2`
        - `subnetIdAz3`
      LaunchTemplate:
        LaunchTemplateId: !Ref `logicalName`
        Version: !GetAtt `logicalName`.LatestVersionNumber
      MaxSize: '5'
      MinSize: '3'
```

## Create a step scaling policy

This example shows an [`AWS::AutoScaling::ScalingPolicy`](../TemplateReference/aws-resource-autoscaling-scalingpolicy.md "../TemplateReference/aws-resource-autoscaling-scalingpolicy.md") resource that scales out the Amazon EC2 Auto Scaling
group using a step scaling policy. The `AdjustmentType` property specifies
`ChangeInCapacity`, which means that the `ScalingAdjustment`
represents the number of instances to add (if `ScalingAdjustment` is positive) or
delete (if it is negative). In this example, `ScalingAdjustment` is 1; therefore,
the policy increments the number of EC2 instances in the group by 1 when the alarm threshold
is breached.

The [`AWS::CloudWatch::Alarm`](../TemplateReference/aws-resource-cloudwatch-alarm.md "../TemplateReference/aws-resource-cloudwatch-alarm.md") resource `CPUAlarmHigh`
specifies the scaling policy `ASGScalingPolicyHigh` as the action to run when the
alarm is in an ALARM state (`AlarmActions`). The `Dimensions` property
references the logical name of an [`AWS::AutoScaling::AutoScalingGroup`](../TemplateReference/aws-resource-autoscaling-autoscalinggroup.md "../TemplateReference/aws-resource-autoscaling-autoscalinggroup.md") resource declared elsewhere in
the same template.

### JSON

```

{
  "Resources":{
    "ASGScalingPolicyHigh":{
      "Type":"AWS::AutoScaling::ScalingPolicy",
      "Properties":{
        "AutoScalingGroupName":{ "Ref":"`logicalName`" },
        "PolicyType":"StepScaling",
        "AdjustmentType":"ChangeInCapacity",
        "StepAdjustments":[
          {
            "MetricIntervalLowerBound":0,
            "ScalingAdjustment":1
          }
        ]
      }
    },
    "CPUAlarmHigh":{
      "Type":"AWS::CloudWatch::Alarm",
      "Properties":{
        "EvaluationPeriods":"2",
        "Statistic":"Average",
        "Threshold":"90",
        "AlarmDescription":"Scale out if CPU > 90% for 2 minutes",
        "Period":"60",
        "AlarmActions":[ { "Ref":"ASGScalingPolicyHigh" } ],
        "Namespace":"AWS/EC2",
        "Dimensions":[
          {
            "Name":"AutoScalingGroupName",
            "Value":{ "Ref":"`logicalName`" }
          }
        ],
        "ComparisonOperator":"GreaterThanThreshold",
        "MetricName":"CPUUtilization"
      }
    }
  }
}
```

### YAML

```
---
Resources:
  ASGScalingPolicyHigh:
    Type: AWS::AutoScaling::ScalingPolicy
    Properties:
      AutoScalingGroupName: !Ref `logicalName`
      PolicyType: StepScaling
      AdjustmentType: ChangeInCapacity
      StepAdjustments:
        - MetricIntervalLowerBound: 0
          ScalingAdjustment: 1
  CPUAlarmHigh:
    Type: AWS::CloudWatch::Alarm
    Properties:
      EvaluationPeriods: 2
      Statistic: Average
      Threshold: 90
      AlarmDescription: 'Scale out if CPU > 90% for 2 minutes'
      Period: 60
      AlarmActions:
        - !Ref ASGScalingPolicyHigh
      Namespace: AWS/EC2
      Dimensions:
        - Name: AutoScalingGroupName
          Value:
            !Ref `logicalName`
      ComparisonOperator: GreaterThanThreshold
      MetricName: CPUUtilization
```

### See also

For more example templates for scaling policies, see the [Examples](../TemplateReference/aws-resource-autoscaling-scalingpolicy.md#aws-resource-autoscaling-scalingpolicy--examples "../TemplateReference/aws-resource-autoscaling-scalingpolicy.md#aws-resource-autoscaling-scalingpolicy--examples") section in the `AWS::AutoScaling::ScalingPolicy`
resource.

## Mixed instances group

examples

### Create an Amazon EC2 Auto Scaling

group using attribute-based instance type selection

This example shows an [`AWS::AutoScaling::AutoScalingGroup`](../TemplateReference/aws-resource-autoscaling-autoscalinggroup.md "../TemplateReference/aws-resource-autoscaling-autoscalinggroup.md") resource that contains the
information to launch a mixed instances group using attribute-based instance type
selection. You specify the minimum and maximum values for the `VCpuCount`
property and the minimum value for the `MemoryMiB` property. Any instance types
used by the Amazon EC2 Auto Scaling group must match your required instance attributes.

The `VPCZoneIdentifier` property of the Amazon EC2 Auto Scaling group specifies a list of
existing subnets in three different Availability Zones. You must specify the applicable
subnet IDs from your account before you create your stack. The `LaunchTemplate`
property references the logical name of an [`AWS::EC2::LaunchTemplate`](../TemplateReference/aws-resource-ec2-launchtemplate.md "../TemplateReference/aws-resource-ec2-launchtemplate.md") resource declared elsewhere in the same
template.

#### JSON

```
{
  "Resources":{
    "myASG":{
      "Type":"AWS::AutoScaling::AutoScalingGroup",
      "Properties":{
        "VPCZoneIdentifier":[
          "`subnetIdAz1`",
          "`subnetIdAz2`",
          "`subnetIdAz3`"
        ],
        "MixedInstancesPolicy":{
          "LaunchTemplate":{
            "LaunchTemplateSpecification":{
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
            "Overrides":[
              {
                "InstanceRequirements":{
                  "VCpuCount":{
                    "Min":`2`,
                    "Max":`4`
                  },
                  "MemoryMiB":{
                    "Min":`2048`
                  }
                }
              }
            ]
          }
        },
        "MaxSize":"5",
        "MinSize":"1"
      }
    }
  }
}
```

#### YAML

```
---
Resources:
  myASG:
    Type: AWS::AutoScaling::AutoScalingGroup
    Properties:
      VPCZoneIdentifier:
        - `subnetIdAz1`
        - `subnetIdAz2`
        - `subnetIdAz3`
      MixedInstancesPolicy:
        LaunchTemplate:
          LaunchTemplateSpecification:
            LaunchTemplateId: !Ref `logicalName`
            Version: !GetAtt `logicalName`.LatestVersionNumber
          Overrides:
            - InstanceRequirements:
                VCpuCount:
                  Min: `2`
                  Max: `4`
                MemoryMiB:
                  Min: `2048`
      MaxSize: '5'
      MinSize: '1'
```

## Launch configuration

examples

### Create a launch configuration

This example shows an [`AWS::AutoScaling::LaunchConfiguration`](../TemplateReference/aws-resource-autoscaling-launchconfiguration.md "../TemplateReference/aws-resource-autoscaling-launchconfiguration.md") resource for an Amazon EC2 Auto Scaling group
where you specify values for the `ImageId`, `InstanceType`, and
`SecurityGroups` properties. The `SecurityGroups` property
specifies both the logical name of an [`AWS::EC2::SecurityGroup`](../TemplateReference/aws-resource-ec2-securitygroup.md "../TemplateReference/aws-resource-ec2-securitygroup.md") resource that's specified elsewhere in
the template, and an existing EC2 security group named
`myExistingEC2SecurityGroup`.

#### JSON

```

"mySimpleConfig" : {
   "Type" : "AWS::AutoScaling::LaunchConfiguration",
   "Properties" : {
      "ImageId" : "`ami-02354e95b3example`",
      "InstanceType" : "`t3.micro`",
      "SecurityGroups" : [ { "Ref" : "`logicalName`" }, "`myExistingEC2SecurityGroup`" ]
   }
}
```

#### YAML

```
mySimpleConfig:
  Type: AWS::AutoScaling::LaunchConfiguration
  Properties:
    ImageId: `ami-02354e95b3example`
    InstanceType: `t3.micro`
    SecurityGroups:
      - !Ref `logicalName`
      - `myExistingEC2SecurityGroup`
```

### Create an Amazon EC2 Auto Scaling

group that uses a launch configuration

This example shows an [`AWS::AutoScaling::AutoScalingGroup`](../TemplateReference/aws-resource-autoscaling-autoscalinggroup.md "../TemplateReference/aws-resource-autoscaling-autoscalinggroup.md") resource with a single
instance. The `VPCZoneIdentifier` property of the Amazon EC2 Auto Scaling group specifies a list
of existing subnets in three different Availability Zones. You must specify the applicable
subnet IDs from your account before you create your stack. The
`LaunchConfigurationName` property references an [`AWS::AutoScaling::LaunchConfiguration`](../TemplateReference/aws-resource-autoscaling-launchconfiguration.md "../TemplateReference/aws-resource-autoscaling-launchconfiguration.md") resource with the logical
name `mySimpleConfig` that is defined in your template.

#### JSON

```

"myASG" : {
   "Type" : "AWS::AutoScaling::AutoScalingGroup",
   "Properties" : {
      "VPCZoneIdentifier" : [ "`subnetIdAz1`", "`subnetIdAz2`", "`subnetIdAz3`" ],
      "LaunchConfigurationName" : { "Ref" : "`mySimpleConfig`" },
      "MaxSize" : "1",
      "MinSize" : "1"
   }
}
```

#### YAML

```
myASG:
  Type: AWS::AutoScaling::AutoScalingGroup
  Properties:
    VPCZoneIdentifier:
      - `subnetIdAz1`
      - `subnetIdAz2`
      - `subnetIdAz3`
    LaunchConfigurationName: !Ref `mySimpleConfig`
    MaxSize: '1'
    MinSize: '1'
```
