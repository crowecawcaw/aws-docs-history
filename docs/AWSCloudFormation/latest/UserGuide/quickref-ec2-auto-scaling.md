

# Configure Amazon EC2 Auto Scaling resources with CloudFormation
<a name="quickref-ec2-auto-scaling"></a>

The following examples show different snippets to include in templates for use with Amazon EC2 Auto Scaling.

**Topics**
+ [Create a single instance Auto Scaling group](#scenario-single-instance-as-group)
+ [Create an Auto Scaling group with an attached load balancer](#scenario-as-group)
+ [Create an Auto Scaling group with notifications](#scenario-as-notification)
+ [Create an Auto Scaling group that uses a `CreationPolicy` and an `UpdatePolicy`](#scenario-as-updatepolicy)
+ [Create a step scaling policy](#scenario-step-scaling-policy)
+ [Mixed instances group examples](#scenario-mixed-instances-group-template-examples)
+ [Launch configuration examples](#scenario-launch-config-template-examples)

## Create a single instance Auto Scaling group
<a name="scenario-single-instance-as-group"></a>

This example shows an [`AWS::AutoScaling::AutoScalingGroup`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html) resource with a single instance to help you get started. The `VPCZoneIdentifier` property of the Auto Scaling group specifies a list of existing subnets in three different Availability Zones. You must specify the applicable subnet IDs from your account before you create your stack. The `LaunchTemplate` property references an [`AWS::EC2::LaunchTemplate`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-launchtemplate.html) resource with the logical name `myLaunchTemplate` that is defined elsewhere in your template.

**Note**  
For examples of launch templates, see [Create launch templates with CloudFormation](quickref-ec2-launch-templates.md) in the Amazon EC2 snippets section and the [Examples](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-launchtemplate.html#aws-resource-ec2-launchtemplate--examples) section in the `AWS::EC2::LaunchTemplate` resource.

### JSON
<a name="quickref-autoscaling-example-1.json"></a>

```
 1. "myASG" : {
 2.    "Type" : "AWS::AutoScaling::AutoScalingGroup",
 3.    "Properties" : {
 4.       "VPCZoneIdentifier" : [ "{{subnetIdAz1}}", "{{subnetIdAz2}}", "{{subnetIdAz3}}" ],
 5.       "LaunchTemplate" : {
 6.         "LaunchTemplateId" : {
 7.           "Ref" : "{{myLaunchTemplate}}"
 8.         },
 9.         "Version" : {
10.           "Fn::GetAtt" : [
11.             "{{myLaunchTemplate}}",
12.             "LatestVersionNumber"
13.           ]
14.         }
15.       },
16.       "MaxSize" : "1",
17.       "MinSize" : "1"
18.    }
19. }
```

### YAML
<a name="quickref-autoscaling-example-1.yaml"></a>

```
 1. myASG:
 2.   Type: AWS::AutoScaling::AutoScalingGroup
 3.   Properties:
 4.     VPCZoneIdentifier:
 5.       - {{subnetIdAz1}}
 6.       - {{subnetIdAz2}}
 7.       - {{subnetIdAz3}}
 8.     LaunchTemplate:
 9.       LaunchTemplateId: !Ref {{myLaunchTemplate}}
10.       Version: !GetAtt {{myLaunchTemplate}}.LatestVersionNumber
11.     MaxSize: '1'
12.     MinSize: '1'
```

## Create an Auto Scaling group with an attached load balancer
<a name="scenario-as-group"></a>

This example shows an [`AWS::AutoScaling::AutoScalingGroup`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html) resource for load balancing over multiple servers. It specifies the logical names of AWS resources declared elsewhere in the same template.

1. The `VPCZoneIdentifier` property specifies the logical names of two [`AWS::EC2::Subnet`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-subnet.html) resources where the Auto Scaling group's EC2 instances will be created: `myPublicSubnet1` and `myPublicSubnet2`.

1. The `LaunchTemplate` property specifies an [`AWS::EC2::LaunchTemplate`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-launchtemplate.html) resource with the logical name `myLaunchTemplate`.

1. The `TargetGroupARNs` property lists the target groups for an Application Load Balancer or Network Load Balancer used to route traffic to the Auto Scaling group. In this example, one target group is specified, an [`AWS::ElasticLoadBalancingV2::TargetGroup`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.html) resource with the logical name `myTargetGroup`.

### JSON
<a name="quickref-autoscaling-example-2.json"></a>

```
 1. "myServerGroup" : {
 2.    "Type" : "AWS::AutoScaling::AutoScalingGroup",
 3.    "Properties" : {
 4.       "VPCZoneIdentifier" : [ { "Ref" : "{{myPublicSubnet1}}" }, { "Ref" : "{{myPublicSubnet2}}" } ],
 5.       "LaunchTemplate" : {
 6.         "LaunchTemplateId" : {
 7.           "Ref" : "{{myLaunchTemplate}}"
 8.         },
 9.         "Version" : {
10.           "Fn::GetAtt" : [
11.             "{{myLaunchTemplate}}",
12.             "LatestVersionNumber"
13.           ]
14.         }
15.       },
16.       "MaxSize" : "5",
17.       "MinSize" : "1",
18.       "TargetGroupARNs" : [ { "Ref" : "{{myTargetGroup}}" } ]
19.    }
20. }
```

### YAML
<a name="quickref-autoscaling-example-2.yaml"></a>

```
 1. myServerGroup:
 2.   Type: AWS::AutoScaling::AutoScalingGroup
 3.   Properties:
 4.     VPCZoneIdentifier:
 5.       - !Ref {{myPublicSubnet1}}
 6.       - !Ref {{myPublicSubnet2}}
 7.     LaunchTemplate:
 8.       LaunchTemplateId: !Ref {{myLaunchTemplate}}
 9.       Version: !GetAtt {{myLaunchTemplate}}.LatestVersionNumber
10.     MaxSize: '5'
11.     MinSize: '1'
12.     TargetGroupARNs:
13.       - !Ref {{myTargetGroup}}
```

### See also
<a name="scenario-as-group-see-also"></a>

For a detailed example that creates an Auto Scaling group with a target tracking scaling policy based on the `ALBRequestCountPerTarget` predefined metric for your Application Load Balancer, see the [Examples](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-scalingpolicy.html#aws-resource-autoscaling-scalingpolicy--examples) section in the `AWS::AutoScaling::ScalingPolicy` resource.

## Create an Auto Scaling group with notifications
<a name="scenario-as-notification"></a>

This example shows an [`AWS::AutoScaling::AutoScalingGroup`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html) resource that sends Amazon SNS notifications when the specified events take place. The `NotificationConfigurations` property specifies the SNS topic where CloudFormation sends a notification and the events that will cause CloudFormation to send notifications. When the events specified by `NotificationTypes` occur, CloudFormation will send a notification to the SNS topic specified by `TopicARN`. When you launch the stack, CloudFormation creates an [`AWS::SNS::Subscription`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sns-subscription.html) resource (`snsTopicForAutoScalingGroup`) that's declared within the same template.

The `VPCZoneIdentifier` property of the Auto Scaling group specifies a list of existing subnets in three different Availability Zones. You must specify the applicable subnet IDs from your account before you create your stack. The `LaunchTemplate` property references the logical name of an [`AWS::EC2::LaunchTemplate`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-launchtemplate.html) resource declared elsewhere in the same template.

### JSON
<a name="quickref-autoscaling-example-3.json"></a>

```
 1. "myASG" : {
 2.   "Type" : "AWS::AutoScaling::AutoScalingGroup",
 3.   "DependsOn": [
 4.     "snsTopicForAutoScalingGroup"
 5.   ],
 6.   "Properties" : {
 7.     "VPCZoneIdentifier" : [ "{{subnetIdAz1}}", "{{subnetIdAz2}}", "{{subnetIdAz3}}" ],
 8.     "LaunchTemplate" : {
 9.       "LaunchTemplateId" : {
10.         "Ref" : "{{logicalName}}"
11.       },
12.       "Version" : {
13.         "Fn::GetAtt" : [
14.           "{{logicalName}}",
15.           "LatestVersionNumber"
16.         ]
17.       }
18.     },
19.     "MaxSize" : "5",
20.     "MinSize" : "1",
21.     "NotificationConfigurations" : [
22.       {
23.         "TopicARN" : { "Ref" : "snsTopicForAutoScalingGroup" },
24.         "NotificationTypes" : [
25.           "autoscaling:EC2_INSTANCE_LAUNCH",
26.           "autoscaling:EC2_INSTANCE_LAUNCH_ERROR",
27.           "autoscaling:EC2_INSTANCE_TERMINATE",
28.           "autoscaling:EC2_INSTANCE_TERMINATE_ERROR",
29.           "autoscaling:TEST_NOTIFICATION"
30.         ]
31.       }
32.     ]
33.   }
34. }
```

### YAML
<a name="quickref-autoscaling-example-3.yaml"></a>

```
 1. myASG:
 2.   Type: AWS::AutoScaling::AutoScalingGroup
 3.   DependsOn:
 4.     - snsTopicForAutoScalingGroup
 5.   Properties:
 6.     VPCZoneIdentifier:
 7.       - {{subnetIdAz1}}
 8.       - {{subnetIdAz2}}
 9.       - {{subnetIdAz3}}
10.     LaunchTemplate:
11.       LaunchTemplateId: !Ref {{logicalName}}
12.       Version: !GetAtt {{logicalName}}.LatestVersionNumber
13.     MaxSize: '5'
14.     MinSize: '1'
15.     NotificationConfigurations:
16.       - TopicARN: !Ref snsTopicForAutoScalingGroup
17.         NotificationTypes:
18.           - autoscaling:EC2_INSTANCE_LAUNCH
19.           - autoscaling:EC2_INSTANCE_LAUNCH_ERROR
20.           - autoscaling:EC2_INSTANCE_TERMINATE
21.           - autoscaling:EC2_INSTANCE_TERMINATE_ERROR
22.           - autoscaling:TEST_NOTIFICATION
```

## Create an Auto Scaling group that uses a `CreationPolicy` and an `UpdatePolicy`
<a name="scenario-as-updatepolicy"></a>

The following example shows how to add `CreationPolicy` and `UpdatePolicy` attributes to an [`AWS::AutoScaling::AutoScalingGroup`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html) resource.

The sample creation policy prevents the Auto Scaling group from reaching `CREATE_COMPLETE` status until CloudFormation receives `Count` number of success signals when the group is ready. To signal that the Auto Scaling group is ready, a `cfn-signal` helper script added to the launch template's user data (not shown) is run on the instances. If the instances don't send a signal within the specified `Timeout`, CloudFormation assumes that the instances were not created, the resource creation fails, and CloudFormation rolls the stack back.

The sample update policy instructs CloudFormation to perform a rolling update using the `AutoScalingRollingUpdate` property. The rolling update makes changes to the Auto Scaling group in small batches (for this example, instance by instance) based on the `MaxBatchSize` and a pause time between batches of updates based on the `PauseTime`. The `MinInstancesInService` attribute specifies the minimum number of instances that must be in service within the Auto Scaling group while CloudFormation updates old instances.

The `WaitOnResourceSignals` attribute is set to `true`. CloudFormation must receive a signal from each new instance within the specified `PauseTime` before continuing the update. While the stack update is in progress, the following EC2 Auto Scaling processes are suspended: `HealthCheck`, `ReplaceUnhealthy`, `AZRebalance`, `AlarmNotification`, and `ScheduledActions`. Note: Don't suspend the `Launch`, `Terminate`, or `AddToLoadBalancer` (if the Auto Scaling group is being used with Elastic Load Balancing) process types because doing so can prevent the rolling update from functioning properly.

The `VPCZoneIdentifier` property of the Auto Scaling group specifies a list of existing subnets in three different Availability Zones. You must specify the applicable subnet IDs from your account before you create your stack. The `LaunchTemplate` property references the logical name of an [`AWS::EC2::LaunchTemplate`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-launchtemplate.html) resource declared elsewhere in the same template.

For more information about the `CreationPolicy` and `UpdatePolicy` attributes, see [Resource attribute reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-product-attribute-reference.html).

### JSON
<a name="quickref-autoscaling-example-4.json"></a>

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
        "MaxSize":"5",
        "MinSize":"3"
      }
    }
  }
}
```

### YAML
<a name="quickref-autoscaling-example-4.yaml"></a>

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
        - {{subnetIdAz1}}
        - {{subnetIdAz2}}
        - {{subnetIdAz3}}
      LaunchTemplate:
        LaunchTemplateId: !Ref {{logicalName}}
        Version: !GetAtt {{logicalName}}.LatestVersionNumber
      MaxSize: '5'
      MinSize: '3'
```

## Create a step scaling policy
<a name="scenario-step-scaling-policy"></a>

This example shows an [`AWS::AutoScaling::ScalingPolicy`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-scalingpolicy.html) resource that scales out the Auto Scaling group using a step scaling policy. The `AdjustmentType` property specifies `ChangeInCapacity`, which means that the `ScalingAdjustment` represents the number of instances to add (if `ScalingAdjustment` is positive) or delete (if it is negative). In this example, `ScalingAdjustment` is 1; therefore, the policy increments the number of EC2 instances in the group by 1 when the alarm threshold is breached.

The [`AWS::CloudWatch::Alarm`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-alarm.html) resource `CPUAlarmHigh` specifies the scaling policy `ASGScalingPolicyHigh` as the action to run when the alarm is in an ALARM state (`AlarmActions`). The `Dimensions` property references the logical name of an [`AWS::AutoScaling::AutoScalingGroup`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html) resource declared elsewhere in the same template.

### JSON
<a name="quickref-autoscaling-example-5.json"></a>

```
 1. {
 2.   "Resources":{
 3.     "ASGScalingPolicyHigh":{
 4.       "Type":"AWS::AutoScaling::ScalingPolicy",
 5.       "Properties":{
 6.         "AutoScalingGroupName":{ "Ref":"{{logicalName}}" },
 7.         "PolicyType":"StepScaling",
 8.         "AdjustmentType":"ChangeInCapacity",
 9.         "StepAdjustments":[
10.           {
11.             "MetricIntervalLowerBound":0,
12.             "ScalingAdjustment":1
13.           }
14.         ]
15.       }
16.     },
17.     "CPUAlarmHigh":{
18.       "Type":"AWS::CloudWatch::Alarm",
19.       "Properties":{
20.         "EvaluationPeriods":"2",
21.         "Statistic":"Average",
22.         "Threshold":"90",
23.         "AlarmDescription":"Scale out if CPU > 90% for 2 minutes",
24.         "Period":"60",
25.         "AlarmActions":[ { "Ref":"ASGScalingPolicyHigh" } ],
26.         "Namespace":"AWS/EC2",
27.         "Dimensions":[
28.           {
29.             "Name":"AutoScalingGroupName",
30.             "Value":{ "Ref":"{{logicalName}}" }
31.           }
32.         ],
33.         "ComparisonOperator":"GreaterThanThreshold",
34.         "MetricName":"CPUUtilization"
35.       }
36.     }
37.   }
38. }
```

### YAML
<a name="quickref-autoscaling-example-5.yaml"></a>

```
 1. ---
 2. Resources:
 3.   ASGScalingPolicyHigh:
 4.     Type: AWS::AutoScaling::ScalingPolicy
 5.     Properties:
 6.       AutoScalingGroupName: !Ref {{logicalName}}
 7.       PolicyType: StepScaling
 8.       AdjustmentType: ChangeInCapacity
 9.       StepAdjustments: 
10.         - MetricIntervalLowerBound: 0
11.           ScalingAdjustment: 1
12.   CPUAlarmHigh:
13.     Type: AWS::CloudWatch::Alarm
14.     Properties:
15.       EvaluationPeriods: 2
16.       Statistic: Average
17.       Threshold: 90
18.       AlarmDescription: 'Scale out if CPU > 90% for 2 minutes'
19.       Period: 60
20.       AlarmActions:
21.         - !Ref ASGScalingPolicyHigh
22.       Namespace: AWS/EC2
23.       Dimensions:
24.         - Name: AutoScalingGroupName
25.           Value:
26.             !Ref {{logicalName}}
27.       ComparisonOperator: GreaterThanThreshold
28.       MetricName: CPUUtilization
```

### See also
<a name="scenario-as-policy-see-also"></a>

For more example templates for scaling policies, see the [Examples](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-scalingpolicy.html#aws-resource-autoscaling-scalingpolicy--examples) section in the `AWS::AutoScaling::ScalingPolicy` resource.

## Mixed instances group examples
<a name="scenario-mixed-instances-group-template-examples"></a>

### Create an Auto Scaling group using attribute-based instance type selection
<a name="scenario-mixed-instances-group-instance-requirements"></a>

This example shows an [`AWS::AutoScaling::AutoScalingGroup`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html) resource that contains the information to launch a mixed instances group using attribute-based instance type selection. You specify the minimum and maximum values for the `VCpuCount` property and the minimum value for the `MemoryMiB` property. Any instance types used by the Auto Scaling group must match your required instance attributes. 

The `VPCZoneIdentifier` property of the Auto Scaling group specifies a list of existing subnets in three different Availability Zones. You must specify the applicable subnet IDs from your account before you create your stack. The `LaunchTemplate` property references the logical name of an [`AWS::EC2::LaunchTemplate`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-launchtemplate.html) resource declared elsewhere in the same template.

#### JSON
<a name="quickref-mixed-instances-group-example-2.json"></a>

```
 1. {
 2.   "Resources":{
 3.     "myASG":{
 4.       "Type":"AWS::AutoScaling::AutoScalingGroup",
 5.       "Properties":{
 6.         "VPCZoneIdentifier":[
 7.           "{{subnetIdAz1}}",
 8.           "{{subnetIdAz2}}",
 9.           "{{subnetIdAz3}}"
10.         ],
11.         "MixedInstancesPolicy":{
12.           "LaunchTemplate":{
13.             "LaunchTemplateSpecification":{
14.               "LaunchTemplateId":{
15.                 "Ref":"{{logicalName}}"
16.               },
17.               "Version":{
18.                 "Fn::GetAtt":[
19.                   "{{logicalName}}",
20.                   "LatestVersionNumber"
21.                 ]
22.               }
23.             },
24.             "Overrides":[
25.               {
26.                 "InstanceRequirements":{
27.                   "VCpuCount":{
28.                     "Min":{{2}},
29.                     "Max":{{4}}
30.                   },
31.                   "MemoryMiB":{
32.                     "Min":{{2048}}
33.                   }
34.                 }
35.               }
36.             ]
37.           }
38.         },
39.         "MaxSize":"5",
40.         "MinSize":"1"
41.       }
42.     }
43.   }
44. }
```

#### YAML
<a name="quickref-mixed-instances-group-example-1.yaml"></a>

```
 1. ---
 2. Resources:
 3.   myASG:
 4.     Type: AWS::AutoScaling::AutoScalingGroup
 5.     Properties:
 6.       VPCZoneIdentifier:
 7.         - {{subnetIdAz1}}
 8.         - {{subnetIdAz2}}
 9.         - {{subnetIdAz3}}
10.       MixedInstancesPolicy:
11.         LaunchTemplate:
12.           LaunchTemplateSpecification:
13.             LaunchTemplateId: !Ref {{logicalName}}
14.             Version: !GetAtt {{logicalName}}.LatestVersionNumber
15.           Overrides:
16.             - InstanceRequirements:
17.                 VCpuCount:
18.                   Min: {{2}}
19.                   Max: {{4}}
20.                 MemoryMiB:
21.                   Min: {{2048}}
22.       MaxSize: '5'
23.       MinSize: '1'
```

## Launch configuration examples
<a name="scenario-launch-config-template-examples"></a>

### Create a launch configuration
<a name="scenario-as-launch-config"></a>

This example shows an [`AWS::AutoScaling::LaunchConfiguration`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-launchconfiguration.html) resource for an Auto Scaling group where you specify values for the `ImageId`, `InstanceType`, and `SecurityGroups` properties. The `SecurityGroups` property specifies both the logical name of an [`AWS::EC2::SecurityGroup`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroup.html) resource that's specified elsewhere in the template, and an existing EC2 security group named `myExistingEC2SecurityGroup`.

#### JSON
<a name="quickref-launch-config-example-1.json"></a>

```
1. "mySimpleConfig" : {
2.    "Type" : "AWS::AutoScaling::LaunchConfiguration",
3.    "Properties" : {
4.       "ImageId" : "{{ami-02354e95b3example}}",
5.       "InstanceType" : "{{t3.micro}}",
6.       "SecurityGroups" : [ { "Ref" : "{{logicalName}}" }, "{{myExistingEC2SecurityGroup}}" ]
7.    }
8. }
```

#### YAML
<a name="quickref-launch-config-example-1.yaml"></a>

```
1. mySimpleConfig:
2.   Type: AWS::AutoScaling::LaunchConfiguration
3.   Properties:
4.     ImageId: {{ami-02354e95b3example}}
5.     InstanceType: {{t3.micro}}
6.     SecurityGroups:
7.       - !Ref {{logicalName}}
8.       - {{myExistingEC2SecurityGroup}}
```

### Create an Auto Scaling group that uses a launch configuration
<a name="scenario-single-instance-as-group-launch-configuration"></a>

This example shows an [`AWS::AutoScaling::AutoScalingGroup`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html) resource with a single instance. The `VPCZoneIdentifier` property of the Auto Scaling group specifies a list of existing subnets in three different Availability Zones. You must specify the applicable subnet IDs from your account before you create your stack. The `LaunchConfigurationName` property references an [`AWS::AutoScaling::LaunchConfiguration`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-launchconfiguration.html) resource with the logical name `mySimpleConfig` that is defined in your template.

#### JSON
<a name="quickref-launch-config-example-2.json"></a>

```
1. "myASG" : {
2.    "Type" : "AWS::AutoScaling::AutoScalingGroup",
3.    "Properties" : {
4.       "VPCZoneIdentifier" : [ "{{subnetIdAz1}}", "{{subnetIdAz2}}", "{{subnetIdAz3}}" ],
5.       "LaunchConfigurationName" : { "Ref" : "{{mySimpleConfig}}" },
6.       "MaxSize" : "1",
7.       "MinSize" : "1"
8.    }
9. }
```

#### YAML
<a name="quickref-launch-config-example-2.yaml"></a>

```
 1. myASG:
 2.   Type: AWS::AutoScaling::AutoScalingGroup
 3.   Properties:
 4.     VPCZoneIdentifier:
 5.       - {{subnetIdAz1}}
 6.       - {{subnetIdAz2}}
 7.       - {{subnetIdAz3}}
 8.     LaunchConfigurationName: !Ref {{mySimpleConfig}}
 9.     MaxSize: '1'
10.     MinSize: '1'
```