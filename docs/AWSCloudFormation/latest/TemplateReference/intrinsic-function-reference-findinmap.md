

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# `Fn::FindInMap`
<a name="intrinsic-function-reference-findinmap"></a>

The intrinsic function `Fn::FindInMap` returns the value corresponding to keys in a two-level map that's declared in the `Mappings` section.

## Declaration
<a name="w2aac24c25b5"></a>

### JSON
<a name="intrinsic-function-reference-findinmap-syntax.json"></a>

```
{ "Fn::FindInMap" : [ "{{MapName}}", "{{TopLevelKey}}", "{{SecondLevelKey}}"] }
```

If you want to specify a fallback value for when a key isn't found in the mapping, include a `DefaultValue`:

```
{ "Fn::FindInMap" : [ "{{MapName}}", "{{TopLevelKey}}", "{{SecondLevelKey}}", {"DefaultValue": "{{DefaultValue}}"}] }
```

### YAML
<a name="intrinsic-function-reference-findinmap-syntax.yaml"></a>

Syntax for the full function name:

```
Fn::FindInMap: [ {{MapName}}, {{TopLevelKey}}, {{SecondLevelKey}} ]
```

Syntax for the short form:

```
!FindInMap [ {{MapName}}, {{TopLevelKey}}, {{SecondLevelKey}} ]
```

If you want to specify a fallback value for when a key isn't found in the mapping, include a `DefaultValue`:

Syntax for the full function name:

```
Fn::FindInMap:
  - {{MapName}}
  - {{TopLevelKey}}
  - {{SecondLevelKey}}
  - DefaultValue: {{DefaultValue}}
```

Syntax for the short form:

```
!FindInMap
  - {{MapName}}
  - {{TopLevelKey}}
  - {{SecondLevelKey}}
  - DefaultValue: {{DefaultValue}}
```

**Note**  
You can't nest two instances of two functions in short form.

## Parameters
<a name="w2aac24c25b7"></a>

MapName  <a name="MapName"></a>
The logical name of a mapping declared in the Mappings section that contains the keys and values.

TopLevelKey  <a name="TopLevelKey"></a>
The top-level key name. Its value is a list of key-value pairs.

SecondLevelKey  <a name="SecondLevelKey"></a>
The second-level key name, which is set to one of the keys from the list assigned to `TopLevelKey`.

DefaultValue  <a name="DefaultValue"></a>
The value that `Fn::FindInMap` returns if either the `TopLevelKey` or `SecondLevelKey` is not found in the specified mapping. This parameter is optional. If omitted, `Fn::FindInMap` raises an error when a key is not found.  
The fourth parameter must be a map with the key `DefaultValue`. For example: `{"DefaultValue": "us-east-1"}`.

## Return value
<a name="w2aac24c25b9"></a>

The value that's assigned to `SecondLevelKey`. If the `TopLevelKey` or `SecondLevelKey` is not found and a `DefaultValue` is specified, the `DefaultValue` is returned instead.

## Examples
<a name="intrinsic-function-reference-findinmap-examples"></a>

The following examples demonstrate how to use the `Fn::FindInMap` function.

**Topics**
+ [Use Fn::FindInMap with region-specific values](#intrinsic-function-reference-findinmap-region-example)
+ [Use Fn::FindInMap for environment-specific configurations](#intrinsic-function-reference-findinmap-environment-example)
+ [Use Fn::FindInMap with a default value](#intrinsic-function-reference-findinmap-default-value-example)

### Use Fn::FindInMap with region-specific values
<a name="intrinsic-function-reference-findinmap-region-example"></a>

The following example shows how to use `Fn::FindInMap` in a template that includes two mappings: `AWSInstanceType2Arch` and `AWSRegionArch2AMI`. It also includes an `InstanceType` parameter that allows you to choose between `t3.micro` and `t4g.nano`. The default is `t3.micro`, but this can be overridden during stack creation. 

`Fn::FindInMap` first determines the architecture (`HVM64` or `ARM64`) based on the selected instance type, and then looks up the correct AMI ID for that architecture in the current AWS Region. 

**Note**  
The AMI IDs shown in these examples are placeholders for demonstration purposes. Whenever possible, consider using dynamic references to AWS Systems Manager parameters as an alternative to the `Mappings` section. To avoid updating all your templates with a new ID each time the AMI that you want to use changes, use a AWS Systems Manager parameter to retrieve the latest AMI ID when the stack is created or updated. The latest versions of commonly used AMIs are also available as public parameters in Systems Manager. For more information, see [Get values stored in other services using dynamic references](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html). 

#### JSON
<a name="intrinsic-function-reference-findinmap-region-example.json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Parameters": {
    "InstanceType": {
      "Description": "The EC2 instance type",
      "Type": "String",
      "AllowedValues": [
        "t3.micro",
        "t4g.nano"
      ],
      "Default": "t3.micro"
    }
  },
  "Mappings": {
    "AWSInstanceType2Arch": {
      "t3.micro": {
        "Arch": "HVM64"
      },
      "t4g.nano": {
        "Arch": "ARM64"
      }
    },
    "AWSRegionArch2AMI": {
      "us-east-1" : { 
        "HVM64" : "{{ami-12345678901234567}}", "ARM64" : "{{ami-23456789012345678}}" 
      },
      "us-west-1" : { 
        "HVM64" : "{{ami-34567890123456789}}", "ARM64" : "{{ami-45678901234567890}}"
      },
      "eu-west-1" : { 
        "HVM64" : "{{ami-56789012345678901}}", "ARM64" : "{{ami-67890123456789012}}" 
      },
      "ap-southeast-1" : { 
        "HVM64" : "{{ami-78901234567890123}}", "ARM64" : "{{ami-89012345678901234}}" 
      },
      "ap-northeast-1" : { 
        "HVM64" : "{{ami-90123456789012345}}", "ARM64" : "{{ami-01234567890123456}}" 
      }
    }
  },
  "Resources" : {
    "MyEC2Instance" : {
      "Type" : "AWS::EC2::Instance",
      "Properties" : {
        "InstanceType" : { "Ref": "InstanceType" },
        "ImageId" : {
          "Fn::FindInMap" : [ "AWSRegionArch2AMI", { "Ref": "AWS::Region" }, { "Fn::FindInMap": [ "AWSInstanceType2Arch", { "Ref": "InstanceType" }, "Arch" ]}]
        }
      }
    }
  }
}
```

#### YAML
<a name="intrinsic-function-reference-findinmap-region-example.yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Parameters:
  InstanceType:
    Description: The EC2 instance type
    Type: String
    AllowedValues:
      - t3.micro
      - t4g.nano
    Default: t3.micro
Mappings: 
  AWSInstanceType2Arch:
    t3.micro:
      Arch: HVM64
    t4g.nano:
      Arch: ARM64
  AWSRegionArch2AMI:
    us-east-1: 
      HVM64: {{ami-12345678901234567}}
      ARM64: {{ami-23456789012345678}}
    us-west-1: 
      HVM64: {{ami-34567890123456789}}
      ARM64: {{ami-45678901234567890}}
    eu-west-1: 
      HVM64: {{ami-56789012345678901}}
      ARM64: {{ami-67890123456789012}}
    ap-southeast-1: 
      HVM64: {{ami-78901234567890123}}
      ARM64: {{ami-89012345678901234}}
    ap-northeast-1: 
      HVM64: {{ami-90123456789012345}}
      ARM64: {{ami-01234567890123456}}
Resources: 
  myEC2Instance: 
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: !Ref InstanceType
      ImageId:
        Fn::FindInMap:
        - AWSRegionArch2AMI
        - Ref: AWS::Region
        - Fn::FindInMap:
          - AWSInstanceType2Arch
          - Ref: InstanceType
          - Arch
```

### Use Fn::FindInMap for environment-specific configurations
<a name="intrinsic-function-reference-findinmap-environment-example"></a>

The following example shows how to use `Fn::FindInMap` for a template with a `Mappings` section that contains a single map, `SecurityGroups`. It also contains an `EnvironmentType` parameter that allows you to specify whether the environment is `Dev` or `Prod`. It defaults to `Dev` but can be overridden during stack creation.

`Fn::FindInMap` returns the appropriate `SecurityGroupIds` based on the `EnvironmentType` parameter. `Fn::Split` then splits the comma-separated string of security group IDs into a list, which is the expected format for [SecurityGroupIds](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html#cfn-ec2-instance-securitygroupids).

If you deploy this stack with `EnvironmentType` set to `Dev`, the `SecurityGroupIds` for `EC2Instance` will be `sg-12345678`. If you set `EnvironmentType` to `Prod`, it will use `sg-abcdef01` and `sg-ghijkl23`.

#### JSON
<a name="intrinsic-function-reference-findinmap-environment-example.json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Parameters":{
    "EnvironmentType":{
      "Description":"The environment type (Dev or Prod)",
      "Type":"String",
      "Default":"Dev",
      "AllowedValues":[
        "Dev",
        "Prod"
      ]
    }
  },
  "Mappings":{
    "SecurityGroups":{
      "Dev":{
        "SecurityGroupIds":"{{sg-12345678}}"
      },
      "Prod":{
        "SecurityGroupIds":"{{sg-abcdef01}},{{sg-ghijkl23}}"
      }
    }
  },
  "Resources":{
    "Ec2Instance":{
      "Type":"AWS::EC2::Instance",
      "Properties":{
        "ImageId": "{{resolve:ssm:/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64}}",
        "InstanceType": "t2.micro",
        "SecurityGroupIds":{
          "Fn::Split":[
            ",",
            {
              "Fn::FindInMap":[
                "SecurityGroups",
                {
                  "Ref":"EnvironmentType"
                },
                "SecurityGroupIds"
              ]
            }
          ]
        }
      }
    }
  }
}
```

#### YAML
<a name="intrinsic-function-reference-findinmap-environment-example.yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Parameters:
  EnvironmentType:
    Description: The environment type (Dev or Prod)
    Type: String
    Default: Dev
    AllowedValues:
      - Dev
      - Prod
Mappings:
  SecurityGroups:
    Dev:
      SecurityGroupIds: {{sg-12345678}}
    Prod:
      SecurityGroupIds: {{sg-abcdef01}},{{sg-ghijkl23}}
Resources:
  Ec2Instance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: '{{resolve:ssm:/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64}}'
      InstanceType: t2.micro
      SecurityGroupIds:
        Fn::Split:
          - ","
          - Fn::FindInMap: [ SecurityGroups, !Ref EnvironmentType, SecurityGroupIds ]
```

### Use Fn::FindInMap with a default value
<a name="intrinsic-function-reference-findinmap-default-value-example"></a>

The following example uses a `DefaultValue` to provide a fallback when a key is not found in the mapping. If the current AWS Region is not defined in the `RegionMap` mapping, `Fn::FindInMap` returns `t3.micro` instead of raising an error.

#### JSON
<a name="intrinsic-function-reference-findinmap-default-value-example.json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Mappings": {
    "RegionMap": {
      "us-east-1": {
        "InstanceType": "t3.large"
      },
      "eu-west-1": {
        "InstanceType": "t3.medium"
      }
    }
  },
  "Resources": {
    "MyInstance": {
      "Type": "AWS::EC2::Instance",
      "Properties": {
        "ImageId": "{{resolve:ssm:/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64}}",
        "InstanceType": {
          "Fn::FindInMap": [
            "RegionMap",
            { "Ref": "AWS::Region" },
            "InstanceType",
            { "DefaultValue": "t3.micro" }
          ]
        }
      }
    }
  }
}
```

#### YAML
<a name="intrinsic-function-reference-findinmap-default-value-example.yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Mappings:
  RegionMap:
    us-east-1:
      InstanceType: t3.large
    eu-west-1:
      InstanceType: t3.medium
Resources:
  MyInstance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: '{{resolve:ssm:/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64}}'
      InstanceType: !FindInMap
        - RegionMap
        - !Ref AWS::Region
        - InstanceType
        - DefaultValue: t3.micro
```

## Supported functions
<a name="w2aac24c25c13"></a>

You can use the following functions in a `Fn::FindInMap` function:
+ `Fn::FindInMap`
+ `Ref`

## Related resources
<a name="w2aac24c25c15"></a>

To use intrinsic functions beyond `Fn::FindInMap` and `Ref` in the parameters of a `Fn::FindInMap` function, you must declare the `AWS::LanguageExtensions` transform within your template. For more information, see [`Fn::FindInMap enhancements`](intrinsic-function-reference-findinmap-enhancements.md).

These related topics can be helpful as you develop templates that use the `Fn::FindInMap` function.
+ [`Fn::Sub`](intrinsic-function-reference-sub.md)
+ [CloudFormation template Mappings syntax](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/mappings-section-structure.html) in the *AWS CloudFormation User Guide*