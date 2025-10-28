This is the new _AWS CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# `Fn::Sub`

The intrinsic function `Fn::Sub` substitutes variables in an input string with
values that you specify. In your templates, you can use this function to construct commands or
outputs that include values that aren't available until you create or update a stack.

## Declaration

The following sections show the function's syntax.

### JSON

```
{ "Fn::Sub" : [ `String`, { `Var1Name`: `Var1Value`, `Var2Name`: `Var2Value` } ] }
```

If you're substituting only template parameters, resource logical IDs, or resource
attributes in the `String` parameter, don't
specify a variable map.

```
{ "Fn::Sub" : `String` }
```

### YAML

Syntax for the full function name:

```
Fn::Sub:
  - `String`
  - `Var1Name`: `Var1Value`
    `Var2Name`: `Var2Value`
```

Syntax for the short form:

```
!Sub
  - `String`
  - `Var1Name`: `Var1Value`
    `Var2Name`: `Var2Value`
```

If you're substituting only template parameters, resource logical IDs, or resource
attributes in the `String` parameter, don't
specify a variable map.

Syntax for the full function name:

```
Fn::Sub: `String`
```

Syntax for the short form:

```
!Sub `String`
```

## Parameters

`String`

A string with variables that CloudFormation substitutes with their associated
values at runtime. Write variables as
`${`MyVarName`}`. Variables can be template
parameter names, resource logical IDs, resource attributes, or a variable in a
key-value map. If you specify only template parameter names, resource logical IDs,
and resource attributes, don't specify a key-value map.

If you specify template parameter names or resource logical IDs, such as
`${InstanceTypeParameter}`, CloudFormation returns the same values as if
you used the `Ref` intrinsic function. If you specify resource
attributes, such as `${MyInstance.PublicIp}`, CloudFormation returns the
same values as if you used the `Fn::GetAtt` intrinsic function.

To write a dollar sign and curly braces (`${}`) literally, add an
exclamation point (`!`) after the open curly brace, such as
`${!`Literal`}`. CloudFormation resolves
this text as `${`Literal`}`.

If you're using a launch template, add a backslash `\` before the dollar sign,
such as `\${!Literal}`, otherwise the literal will resolve as an empty
string.

`VarName`

The name of a variable that you included in the `String`
parameter.

`VarValue`

The value that CloudFormation substitutes for the associated variable name at
runtime.

## Return value

CloudFormation returns the original string, substituting the values for all the
variables.

## Examples

The following examples demonstrate how to use the `Fn::Sub` function.

### Use `Fn::Sub` without a key-value map

In this simple example, the `InstanceSecurityGroup` resource's description
is dynamically created with the `AWS::StackName` pseudo parameter. For
instance, if the stack name is "VPC-EC2-ALB-Stack", the resulting
description is "SSH security group for VPC-EC2-ALB-Stack".

#### JSON

```
"InstanceSecurityGroup" : {
    "Type" : "AWS::EC2::SecurityGroup",
    "Properties" : {
        "GroupDescription" : {"Fn::Sub": "SSH security group for ${AWS::StackName}"}
}}
```

#### YAML

```
InstanceSecurityGroup:
  Type: AWS::EC2::SecurityGroup
  Properties:
    GroupDescription: !Sub "SSH security group for ${AWS::StackName}"
```

### Use `Fn::Sub` with a key-value map

In this example, the `WWWBucket` resource's name is dynamically created
with a key-value map. The `Fn::Sub` function substitutes
`${Domain}` in the input string `www.${Domain}` with the value
from a `Ref` function that references the `RootDomainName`
parameter that's defined within the same stack template. For instance, if the root
domain name is "mydomain.com", the resulting name for this resource is
"www.mydomain.com".

#### JSON

```
"WWWBucket":{
  "Type":"AWS::S3::Bucket",
  "Properties":{
    "BucketName":{
      "Fn::Sub":[
        "www.${Domain}",
        {
          "Domain":{
            "Ref":"RootDomainName"
          }
        }
      ]
    }
  }
}
```

#### YAML

```
  WWWBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Sub
        - 'www.${Domain}'
        - Domain: !Ref RootDomainName
```

### Use multiple variables to construct ARNs

The following example uses `Fn::Sub` with the `AWS::Region` and
`AWS::AccountId` pseudo parameters and the `vpc` resource
logical ID to create an Amazon Resource Name (ARN) for a VPC.

#### JSON

```
{ "Fn::Sub": "arn:aws:ec2:${AWS::Region}:${AWS::AccountId}:vpc/${vpc}" }
```

#### YAML

```
!Sub 'arn:aws:ec2:${AWS::Region}:${AWS::AccountId}:vpc/${vpc}'
```

### Pass parameter values in user data scripts

The following example uses `Fn::Sub` to substitute the
`AWS::StackName` and `AWS::Region` pseudo parameters for the
actual stack name and Region at runtime.

#### JSON

For readability, the JSON example uses the `Fn::Join` function to
separate each command, instead of specifying the entire user data script in a single
string value.

```
"UserData": { "Fn::Base64": { "Fn::Join": ["\n", [
  "#!/bin/bash -xe",
  "yum update -y aws-cfn-bootstrap",
  { "Fn::Sub": "/opt/aws/bin/cfn-init -v --stack ${AWS::StackName} --resource LaunchConfig --configsets wordpress_install --region ${AWS::Region}" },
  { "Fn::Sub": "/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource WebServerGroup --region ${AWS::Region}" }]]
}}
```

#### YAML

The YAML example uses a literal block to specify the user data script.

```
UserData:
  Fn::Base64:
    !Sub |
      #!/bin/bash -xe
      yum update -y aws-cfn-bootstrap
      /opt/aws/bin/cfn-init -v --stack ${AWS::StackName} --resource LaunchConfig --configsets wordpress_install --region ${AWS::Region}
      /opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource WebServerGroup --region ${AWS::Region}
```

### Specify conditional values using mappings

In this example, the `myLogGroup` resource's name is dynamically created
by substituting the `log_group_name` variable with the resulting value from
the `Fn::FindInMap` function.

#### JSON

```
{
  "Mappings": {
    "LogGroupMapping": {
      "Test": {
        "Name": "test_log_group"
      },
      "Prod": {
        "Name": "prod_log_group"
      }
    }
  },
  "Resources": {
    "myLogGroup": {
      "Type": "AWS::Logs::LogGroup",
      "Properties": {
        "LogGroupName": {
          "Fn::Sub": [
            "cloud_watch_${log_group_name}",
            {
              "log_group_name": {
                "Fn::FindInMap": [
                  "LogGroupMapping",
                  "Test",
                  "Name"
                ]
              }
            }
          ]
        }
      }
    }
  }
}
```

#### YAML

```
Mappings:
  LogGroupMapping:
    Test:
      Name: test_log_group
    Prod:
      Name: prod_log_group
Resources:
  myLogGroup:
    Type: 'AWS::Logs::LogGroup'
    Properties:
      LogGroupName: !Sub
        - 'cloud_watch_${log_group_name}'
        - log_group_name: !FindInMap
            - LogGroupMapping
            - Test
            - Name
```

## Supported

functions

For the `String` parameter, you can't use any functions. You must specify a
string value.

For the `VarName` and `VarValue` parameters, you can use the
following functions:

- [Fn::Base64](intrinsic-function-reference-base64.md "intrinsic-function-reference-base64.md")
- [Fn::FindInMap](intrinsic-function-reference-findinmap.md "intrinsic-function-reference-findinmap.md")
- [Fn::GetAtt](intrinsic-function-reference-getatt.md "intrinsic-function-reference-getatt.md")
- [Fn::GetAZs](intrinsic-function-reference-getavailabilityzones.md "intrinsic-function-reference-getavailabilityzones.md")
- [Fn::If](intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-if "intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-if")
- [Fn::ImportValue](intrinsic-function-reference-importvalue.md "intrinsic-function-reference-importvalue.md")
- [Fn::Join](intrinsic-function-reference-join.md "intrinsic-function-reference-join.md")
- [Fn::Select](intrinsic-function-reference-select.md "intrinsic-function-reference-select.md")
- [Fn::Sub](intrinsic-function-reference-sub.md "intrinsic-function-reference-sub.md")
- [Ref](intrinsic-function-reference-ref.md "intrinsic-function-reference-ref.md")
