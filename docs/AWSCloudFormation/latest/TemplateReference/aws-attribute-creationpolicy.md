

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# `CreationPolicy` attribute
<a name="aws-attribute-creationpolicy"></a>

Associate the `CreationPolicy` attribute with a resource to prevent its status from reaching create complete until CloudFormation receives a specified number of success signals or the timeout period is exceeded. To signal a resource, you can use the [cfn-signal](cfn-signal.md) helper script or [SignalResource](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_SignalResource.html) API. CloudFormation publishes valid signals to the stack events so that you track the number of signals sent.

The creation policy is invoked only when CloudFormation creates the associated resource. Currently, the only CloudFormation resources that support creation policies are:
+ [AWS::AppStream::Fleet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appstream-fleet.html)
+ [AWS::AutoScaling::AutoScalingGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html)
+ [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html)
+ [AWS::CloudFormation::WaitCondition](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-waitcondition.html)

Use the `CreationPolicy` attribute when you want to wait on resource configuration actions before stack creation proceeds. For example, if you install and configure software applications on an EC2 instance, you might want those applications to be running before proceeding. In such cases, you can add a `CreationPolicy` attribute to the instance, and then send a success signal to the instance after the applications are installed and configured. For a detailed example, see [Deploying applications on Amazon EC2 with CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/deploying.applications.html) in the *AWS CloudFormation User Guide*.

## WorkSpaces Applications creation policy
<a name="aws-attribute-creation-policy-app-stream-fleet"></a>

Amazon AppStream configuration for a creation policy.

### Syntax
<a name="aws-attribute-creation-policy-app-stream-fleet-syntax"></a>

#### JSON
<a name="aws-attribute-creation-policy-app-stream-fleet-syntax-json"></a>

```
{
    "CreationPolicy": {
        "StartFleet": "{{Boolean}}"
    }
}
```

#### YAML
<a name="aws-attribute-creation-policy-app-stream-fleet-syntax-yaml"></a>

```
CreationPolicy:
  StartFleet: {{Boolean}}
```

`StartFleet`  <a name="cfn-attributes-updatepolicy-replacingupdate-StartFleet"></a>
Starts the specified fleet.  
*Required*: No

## Amazon EC2 Auto Scaling creation properties
<a name="w2aac19b7c13"></a>

Amazon EC2 Auto Scaling configuration for a creation policy.

### Syntax
<a name="aws-attribute-creation-policy-app-auto-scaling-syntax"></a>

#### JSON
<a name="aws-attribute-creation-policy-app-auto-scaling-syntax.json"></a>

```
"CreationPolicy" : {
  "AutoScalingCreationPolicy" : {
    "MinSuccessfulInstancesPercent" : {{Integer}}
  },
  "ResourceSignal" : {    
    "Count" : {{Integer}},
    "Timeout" : {{String}}
  }
}
```

#### YAML
<a name="aws-attribute-creation-policy-app-auto-scaling-syntax.yaml"></a>

```
CreationPolicy:
  AutoScalingCreationPolicy:
    MinSuccessfulInstancesPercent: {{Integer}}
  ResourceSignal:    
    Count: {{Integer}}
    Timeout: {{String}}
```

### Amazon EC2 Auto Scaling creation properties
<a name="cfn-attributes-creationpolicy-properties"></a>

Amazon EC2 Auto Scaling configuration for a creation policy.

`AutoScalingCreationPolicy`  <a name="cfn-attributes-creationpolicy-autoscalingcreationpolicy"></a>
For a new Amazon EC2 Auto Scaling group, specifies the number of instances that must signal success before setting the group's status to `CREATE_COMPLETE`.    
`MinSuccessfulInstancesPercent`  <a name="cfn-attributes-creationpolicy-autoscalingcreationpolicy-minsuccessfulinstancespercent"></a>
Specifies the percentage of instances in an Amazon EC2 Auto Scaling that must signal success before setting the group's status to `CREATE_COMPLETE`. You can specify a value from `0` to `100`. CloudFormation rounds to the nearest tenth of a percent. For example, if you create five instances with a minimum successful percentage of `50`, three instances must signal success. If an instance doesn't send a signal within the time specified by the `Timeout` property, CloudFormation assumes that the instance wasn't created.  
*Default*: `100`  
*Type*: Integer  
*Required*: No

`ResourceSignal`  <a name="cfn-attributes-creationpolicy-resourcesignal"></a>
When CloudFormation creates the associated resource, configures the number of required success signals and the length of time that CloudFormation waits for those signals.    
`Count`  <a name="cfn-attributes-creationpolicy-resourcesignal-count"></a>
The number of success signals CloudFormation must receive before it sets the resource status as `CREATE_COMPLETE`. If the resource receives a failure signal or doesn't receive the specified number of signals before the timeout period expires, the resource creation fails and CloudFormation rolls the stack back.  
*Default*: `1`  
*Type*: Integer  
*Required*: No  
`Timeout`  <a name="cfn-attributes-creationpolicy-resourcesignal-timeout"></a>
The length of time that CloudFormation waits for the number of signals that was specified in the `Count` property. The timeout period starts after CloudFormation stabilizes the resource, and the timeout expires no sooner than the time you specify but can occur shortly thereafter. The maximum time that you can specify is 12 hours.  
The value must be in [ISO8601 duration format](https://en.wikipedia.org/wiki/ISO_8601#Durations), in the form: `PT{{#}}H{{#}}M{{#}}S`, where each {{\#}} is the number of hours, minutes, and seconds, respectively. For best results, specify a period of time that gives your instances plenty of time to get up and running. A shorter timeout can cause a rollback.  
*Default*: `PT5M` (5 minutes)  
*Type*: String  
*Required*: No

## Examples
<a name="aws-attribute-creation-policy-examples"></a>

### Auto Scaling group
<a name="aws-attribute-creation-policy-as-group"></a>

The following example shows how to add a creation policy to an Amazon EC2 Auto Scaling group. The creation policy requires three success signals and times out after 15 minutes. Use the [cfn-signal](cfn-signal.md) helper script to signal when an instance creation process has completed successfully.

To have instances wait for an Elastic Load Balancing health check before they signal success, add a health-check verification by using the [cfn-init](cfn-init.md) helper script. For an example, see the `verify_instance_health` command in the sample templates for Amazon EC2 Auto Scaling rolling updates in our [GitHub repository](https://github.com/aws-cloudformation/aws-cloudformation-templates/tree/main/AutoScaling).

#### JSON
<a name="aws-attribute-creationpolicy-example-1.json"></a>

```
"AutoScalingGroup": {
  "Type": "AWS::AutoScaling::AutoScalingGroup",
  "Properties": {
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
<a name="aws-attribute-creationpolicy-example-1.yaml"></a>

```
AutoScalingGroup:
  Type: AWS::AutoScaling::AutoScalingGroup
  Properties:
    VPCZoneIdentifier:
      - {{subnetIdAz1}}
      - {{subnetIdAz2}}
      - {{subnetIdAz3}}
    LaunchTemplate:
      LaunchTemplateId: !Ref {{logicalName}}
      Version: !GetAtt {{logicalName}}.LatestVersionNumber
    MinSize: '1'
    MaxSize: '4'
  CreationPolicy:
    ResourceSignal:
      Count: '3'
      Timeout: PT15M
```

### WaitCondition
<a name="w2aac19b7c15b5"></a>

The following example shows how to add a creation policy to a wait condition for CloudFormation resources beyond Amazon EC2.

To signal the `WaitCondition` resource, use the [SignalResource](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_SignalResource.html) API. This API is designed to work with `WaitCondition` resources that you configure using a `CreationPolicy`.

#### JSON
<a name="aws-attribute-creationpolicy-example-2.json"></a>

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
<a name="aws-attribute-creationpolicy-example-2.yaml"></a>

```
WaitCondition:
  Type: AWS::CloudFormation::WaitCondition
  CreationPolicy:
    ResourceSignal:
      Timeout: PT15M
      Count: 5
```