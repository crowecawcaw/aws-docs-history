This is the new _CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# `Fn::ImportValue`

The intrinsic function `Fn::ImportValue` returns the value of an output exported
by another stack. You typically use this function to create cross-stack references. For more
information, see [Walkthrough: Refer to resource outputs in another CloudFormation stack](../UserGuide/walkthrough-crossstackref.md "../UserGuide/walkthrough-crossstackref.md") in the
_AWS CloudFormation User Guide_.

In the following example template snippets, Stack A exports VPC security group values and
Stack B imports them.

###### Note

The following restrictions apply to cross-stack references:

- For each AWS account, `Export` names must be unique within a Region.
- You can't create cross-stack references across Regions. You can use the intrinsic function
  `Fn::ImportValue` to import only values that have been exported within the same Region.
- For outputs, the value of the `Name` property of an `Export` can't use `Ref` or `GetAtt` functions that depend on a resource.

Similarly, the `ImportValue` function can't include `Ref` or `GetAtt` functions that depend on a resource.

- After another stack imports an output value, you can't delete the stack that is exporting the output value or modify the exported output value. All the imports
  must be removed before you can delete the exporting stack or modify the output value.

## JSON

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

Stack B Import

```
Resources:
  WebServerInstance:
    Type: 'AWS::EC2::Instance'
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

### JSON

```
{ "Fn::ImportValue" : `sharedValueToImport` }
```

### YAML

You can use the full function name:

```
Fn::ImportValue: `sharedValueToImport`
```

Alternatively, you can use the short form:

```
!ImportValue `sharedValueToImport`
```

###### Important

You can't use the short form of `!ImportValue` when it contains the
short form of `!Sub`.

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

sharedValueToImport

The stack output value that you want to import.

## Return value

The stack output value.

## Example

### JSON

```
{ "Fn::ImportValue" : {"Fn::Sub": "${NetworkStackNameParameter}-SubnetID" } }
```

### YAML

```
Fn::ImportValue:
  !Sub "${NetworkStackName}-SecurityGroupID"
```

## Supported functions

You can use the following functions in the `Fn::ImportValue` function. The
value of these functions can't depend on a resource.

- `Fn::Base64`
- `Fn::FindInMap`
- `Fn::If`
- `Fn::Join`
- `Fn::Select`
- `Fn::Sub`
- `Ref`
