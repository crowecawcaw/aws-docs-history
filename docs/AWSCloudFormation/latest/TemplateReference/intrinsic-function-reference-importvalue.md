

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# `Fn::ImportValue`
<a name="intrinsic-function-reference-importvalue"></a>

The intrinsic function `Fn::ImportValue` returns the value of an output exported by another stack. You typically use this function to create cross-stack references. For more information, see [Walkthrough: Refer to resource outputs in another CloudFormation stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/walkthrough-crossstackref.html) in the *AWS CloudFormation User Guide*.

**Tip**  
To reference stack outputs across AWS accounts or Regions without requiring explicit exports, use [`Fn::GetStackOutput`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getstackoutput.html). `Fn::GetStackOutput` creates a weak reference that is resolved at stack create or update time and does not require the referenced stack to declare an `Export`.

In the following example template snippets, Stack A exports VPC security group values and Stack B imports them.

**Note**  
The following restrictions apply to cross-stack references:  
For each AWS account, `Export` names must be unique within a Region.
When using `Export` and `Fn::ImportValue`, cross-stack references are limited to the same account and Region. To reference stack outputs across accounts or Regions, use `Fn::GetStackOutput`.
For outputs, the value of the `Name` property of an `Export` can't use `Ref` or `GetAtt` functions that depend on a resource.  
Similarly, the `ImportValue` function can't include `Ref` or `GetAtt` functions that depend on a resource.
After another stack imports an output value, you can't delete the stack that is exporting the output value or modify the exported output value. All the imports must be removed before you can delete the exporting stack or modify the output value.

## JSON
<a name="intrinsic-function-reference-importvalue-export.json"></a>

Stack A Export

```
"Outputs" : {
  "PublicSubnet" : {
    "Description" : "The subnet ID to use for public web servers",
    "Value" :  { "Ref" : "PublicSubnet" },
    "Export" : { "Name" : {"Fn::Sub": "${AWS::StackName}-SubnetID" }}
  },
  "WebServerSecurityGroup" : {
    "Description" : "The security group ID to use for public web servers",
    "Value" :  { "Fn::GetAtt" : ["WebServerSecurityGroup", "GroupId"] },
    "Export" : { "Name" : {"Fn::Sub": "${AWS::StackName}-SecurityGroupID" }}
  }
}
```

## YAML
<a name="intrinsic-function-reference-importvalue-export.yaml"></a>

Stack A Export

```
Outputs:
  PublicSubnet:
    Description: The subnet ID to use for public web servers
    Value:
      Ref: PublicSubnet
    Export:
      Name:
        'Fn::Sub': '${AWS::StackName}-SubnetID'
  WebServerSecurityGroup:
    Description: The security group ID to use for public web servers
    Value:
      'Fn::GetAtt':
        - WebServerSecurityGroup
        - GroupId
    Export:
      Name:
        'Fn::Sub': '${AWS::StackName}-SecurityGroupID'
```

## JSON
<a name="intrinsic-function-reference-importvalue-import.json"></a>

Stack B Import

```
"Resources" : {
  "WebServerInstance" : {
    "Type" : "AWS::EC2::Instance",
    "Properties" : {
      "InstanceType" : "t2.micro",
      "ImageId" : "ami-a1b23456",
      "NetworkInterfaces" : [{
        "GroupSet" : [{"Fn::ImportValue" : {"Fn::Sub" : "${NetworkStackNameParameter}-SecurityGroupID"}}],
        "AssociatePublicIpAddress" : "true",
        "DeviceIndex" : "0",
        "DeleteOnTermination" : "true",
        "SubnetId" : {"Fn::ImportValue" : {"Fn::Sub" : "${NetworkStackNameParameter}-SubnetID"}}
      }]
    }
  }
}
```

## YAML
<a name="intrinsic-function-reference-importvalue-import.yaml"></a>

Stack B Import

```
Resources:
  WebServerInstance:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: t2.micro
      ImageId: ami-a1b23456
      NetworkInterfaces:
        - GroupSet:
            - Fn::ImportValue: 
              'Fn::Sub': '${NetworkStackNameParameter}-SecurityGroupID'
          AssociatePublicIpAddress: 'true'
          DeviceIndex: '0'
          DeleteOnTermination: 'true'
          SubnetId: Fn::ImportValue: 
            'Fn::Sub': '${NetworkStackNameParameter}-SubnetID'
```

## Declaration
<a name="w2aac24c48c13"></a>

### JSON
<a name="intrinsic-function-reference-importvalue-syntax.json"></a>

```
{ "Fn::ImportValue" : {{sharedValueToImport}} }
```

### YAML
<a name="intrinsic-function-reference-importvalue-syntax.yaml"></a>

You can use the full function name:

```
Fn::ImportValue: {{sharedValueToImport}}
```

Alternatively, you can use the short form:

```
!ImportValue {{sharedValueToImport}}
```

**Important**  
You can't use the short form of `!ImportValue` when it contains the short form of `!Sub`.   

```
# do not use
!ImportValue
  !Sub '${NetworkStack}-SubnetID'
```
Instead, you must use the full function name, for example:  

```
Fn::ImportValue:
  !Sub "${NetworkStack}-SubnetID"
```

## Parameters
<a name="w2aac24c48c15"></a>

sharedValueToImport  
The stack output value that you want to import.

## Return value
<a name="w2aac24c48c17"></a>

The stack output value.

## Example
<a name="w2aac24c48c19"></a>

### JSON
<a name="intrinsic-function-reference-importvalue-example.json"></a>

```
{ "Fn::ImportValue" : {"Fn::Sub": "${NetworkStackNameParameter}-SubnetID" } }
```

### YAML
<a name="intrinsic-function-reference-importvalue-example.yaml"></a>

```
Fn::ImportValue:
  !Sub "${NetworkStackName}-SecurityGroupID"
```

## Supported functions
<a name="w2aac24c48c21"></a>

You can use the following functions in the `Fn::ImportValue` function. The value of these functions can't depend on a resource.
+ `Fn::Base64`
+ `Fn::FindInMap`
+ `Fn::If`
+ `Fn::Join`
+ `Fn::Select`
+ `Fn::Sub`
+ `Ref`