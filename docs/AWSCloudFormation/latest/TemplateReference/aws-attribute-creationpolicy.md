This is the new _CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# `CreationPolicy` attribute

Associate the `CreationPolicy` attribute with a resource to prevent its status
from reaching create complete until CloudFormation receives a specified number of success signals or the
timeout period is exceeded. To signal a resource, you can use the [cfn-signal](cfn-signal.md "cfn-signal.md") helper script or [SignalResource](../APIReference/API_SignalResource.md "../APIReference/API_SignalResource.md") API. CloudFormation publishes valid signals to the stack
events so that you track the number of signals sent.

The creation policy is invoked only when CloudFormation creates the associated resource.
Currently, the only CloudFormation resources that support creation policies are:

- [AWS::AppStream::Fleet](aws-resource-appstream-fleet.md "aws-resource-appstream-fleet.md")
- [AWS::AutoScaling::AutoScalingGroup](aws-resource-autoscaling-autoscalinggroup.md "aws-resource-autoscaling-autoscalinggroup.md")
- [AWS::EC2::Instance](aws-resource-ec2-instance.md "aws-resource-ec2-instance.md")
- [AWS::CloudFormation::WaitCondition](aws-resource-cloudformation-waitcondition.md "aws-resource-cloudformation-waitcondition.md")
  Use the `CreationPolicy` attribute when you want to wait on resource
  configuration actions before stack creation proceeds. For example, if you install and configure
  software applications on an EC2 instance, you might want those applications to be running before
  proceeding. In such cases, you can add a `CreationPolicy` attribute to the instance,
  and then send a success signal to the instance after the applications are installed and
  configured. For a detailed example, see [Deploying applications on Amazon EC2 with
  CloudFormation](../UserGuide/deploying.md "../UserGuide/deploying.md") in the _AWS CloudFormation User Guide_.

## WorkSpaces Applications creation

policy

Amazon AppStream configuration for a creation policy.

### Syntax

#### JSON

```
{
    "CreationPolicy": {
        "StartFleet": "`Boolean`"
    }
}
```

#### YAML

```
CreationPolicy:
  StartFleet: `Boolean`
```

`StartFleet`

Starts the specified fleet.

_Required_: No

## Amazon EC2 Auto Scaling creation properties

Amazon EC2 Auto Scaling configuration for a creation policy.

### Syntax

#### JSON

```
"CreationPolicy" : {
  "AutoScalingCreationPolicy" : {
    "MinSuccessfulInstancesPercent" : `Integer`
  },
  "ResourceSignal" : {
    "Count" : `Integer`,
    "Timeout" : `String`
  }
}
```

#### YAML

```
CreationPolicy:
  AutoScalingCreationPolicy:
    MinSuccessfulInstancesPercent: `Integer`
  ResourceSignal:
    Count: `Integer`
    Timeout: `String`
```

### Amazon EC2 Auto Scaling creation

properties

Amazon EC2 Auto Scaling configuration for a creation policy.

`AutoScalingCreationPolicy`

For a new Amazon EC2 Auto Scaling group, specifies the number of instances that must signal
success before setting the group's status to `CREATE_COMPLETE`.

`MinSuccessfulInstancesPercent`

Specifies the percentage of instances in an Amazon EC2 Auto Scaling that must signal
success before setting the group's status to `CREATE_COMPLETE`. You
can specify a value from `0` to `100`. CloudFormation rounds
to the nearest tenth of a percent. For example, if you create five instances
with a minimum successful percentage of `50`, three instances must
signal success. If an instance doesn't send a signal within the time specified
by the `Timeout` property, CloudFormation assumes that the instance
wasn't created.

_Default_: `100`

_Type_: Integer

_Required_: No

`ResourceSignal`

When CloudFormation creates the associated resource, configures the number of required
success signals and the length of time that CloudFormation waits for those signals.

`Count`

The number of success signals CloudFormation must receive before it sets the
resource status as `CREATE_COMPLETE`. If the resource receives a
failure signal or doesn't receive the specified number of signals before the
timeout period expires, the resource creation fails and CloudFormation rolls the
stack back.

_Default_: `1`

_Type_: Integer

_Required_: No

`Timeout`

The length of time that CloudFormation waits for the number of signals that was
specified in the `Count` property. The timeout period starts after
CloudFormation stabilizes the resource, and the timeout expires no sooner than the
time you specify but can occur shortly thereafter. The maximum time that you can
specify is 12 hours.

The value must be in [ISO8601 duration
format](https://en.wikipedia.org/wiki/ISO_8601#Durations "https://en.wikipedia.org/wiki/ISO_8601#Durations"), in the form:
`PT`#`H`#`M`#`S`,
where each `#` is the number of hours, minutes, and
seconds, respectively. For best results, specify a period of time that gives
your instances plenty of time to get up and running. A shorter timeout can cause
a rollback.

_Default_: `PT5M` (5 minutes)

_Type_: String

_Required_: No

## Examples

### Amazon EC2 Auto Scaling group

The following example shows how to add a creation policy to an Amazon EC2 Auto Scaling group. The
creation policy requires three success signals and times out after 15 minutes. Use the [cfn-signal](cfn-signal.md "cfn-signal.md") helper script to signal when an instance creation
process has completed successfully.

To have instances wait for an ELB health check before they signal success, add a
health-check verification by using the [cfn-init](cfn-init.md "cfn-init.md") helper script. For an example, see the
`verify_instance_health` command in the sample templates for Amazon EC2 Auto Scaling rolling
updates in our [GitHub repository](https://github.com/aws-cloudformation/aws-cloudformation-templates/tree/main/AutoScaling "https://github.com/aws-cloudformation/aws-cloudformation-templates/tree/main/AutoScaling").

#### JSON

```
"AutoScalingGroup": {
  "Type": "AWS::AutoScaling::AutoScalingGroup",
  "Properties": {
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
    "MinSize": "1",
    "MaxSize": "4"
  },
  "CreationPolicy": {
    "ResourceSignal": {
      "Count": "3",
      "Timeout": "PT15M"
    }
  }
}
```

#### YAML

```
AutoScalingGroup:
  Type: AWS::AutoScaling::AutoScalingGroup
  Properties:
    VPCZoneIdentifier:
      - `subnetIdAz1`
      - `subnetIdAz2`
      - `subnetIdAz3`
    LaunchTemplate:
      LaunchTemplateId: !Ref `logicalName`
      Version: !GetAtt `logicalName`.LatestVersionNumber
    MinSize: '1'
    MaxSize: '4'
  CreationPolicy:
    ResourceSignal:
      Count: '3'
      Timeout: PT15M
```

### WaitCondition

The following example shows how to add a creation policy to a wait condition for
CloudFormation resources beyond Amazon EC2.

To
signal the `WaitCondition` resource, use the [SignalResource](../APIReference/API_SignalResource.md "../APIReference/API_SignalResource.md") API. This
API is designed to work with `WaitCondition` resources that you configure using a
`CreationPolicy`.

#### JSON

```
"WaitCondition" : {
    "Type" : "AWS::CloudFormation::WaitCondition",
    "CreationPolicy" : {
        "ResourceSignal" : {
            "Timeout" : "PT15M",
            "Count" : "5"
        }
    }
}
```

#### YAML

```
WaitCondition:
  Type: AWS::CloudFormation::WaitCondition
  CreationPolicy:
    ResourceSignal:
      Timeout: PT15M
      Count: 5
```
