# CloudFormation template Mappings
 syntax

The optional `Mappings` section helps you create key-value pairs that can be used
 to specify values based on certain conditions or dependencies. 

One common use case for the `Mappings` section is to set values based on the
 AWS Region where the stack is deployed. This can be achieved by using the
 `AWS::Region` pseudo parameter. The `AWS::Region` pseudo parameter is a
 value that CloudFormation resolves to the region where the stack is created. Pseudo parameters are
 resolved by CloudFormation when you create the stack. 

To retrieve values in a map, you can use the `Fn::FindInMap` intrinsic function
 within the `Resources` section of your template. 


## Syntax


The `Mappings` section uses the following syntax:



### JSON



```
"Mappings" : {
  "`MappingLogicalName`" : {
    "`Key1`" : {
      "`Name`" : "`Value1`"
    },
    "`Key2`" : {
      "`Name`" : "`Value2`"
    },
    "`Key3`" : {
      "`Name`" : "`Value3`"
    }
  }
}
```



### YAML



```
Mappings: 
  `MappingLogicalName`: 
    `Key1`: 
      `Name`: `Value1`
    `Key2`: 
      `Name`: `Value2`
    `Key3`: 
      `Name`: `Value3`
```



* `MappingLogicalName` is the logical name for the mapping.
* Within the mapping, each map is a key followed by another mapping.
* The key must be a map of name-value pairs and unique within the mapping.
* The name-value pair is a label, and the value to map. By naming the values, you can
 map more than one set of values to a key.
* The keys in mappings must be literal strings.
* The values can be of type `String` or
 `List`.

###### Note

You can't include parameters, pseudo parameters, or intrinsic functions in the
 `Mappings` section. 
 

If the values in a mapping aren't currently used by your stack, you cannot update the
 mapping alone. You must include changes that add, modify, or delete resources.


## Examples


###### Topics

* [Basic mapping](#mappings-section-structure-basic-example "#mappings-section-structure-basic-example")
* [Mapping with multiple
 values](#mappings-section-structure-multiple-values-example "#mappings-section-structure-multiple-values-example")
* [Return a value from a
 mapping](#mappings-section-structure-return-value-example "#mappings-section-structure-return-value-example")
* [Input parameter and
 Fn::FindInMap](#mappings-section-structure-input-parameter-example "#mappings-section-structure-input-parameter-example")

### Basic mapping


The following example shows a `Mappings` section with a map
 `RegionMap`, which contains five keys that map to name-value pairs containing
 single string values. The keys are region names. Each name-value pair is an instance type
 from the T family that's available in the region represented by the key. The name-value
 pairs have a name (`InstanceType` in the example) and a value. 



#### JSON



```
"Mappings" : {
  "RegionMap" : {
    "us-east-1"      : {"InstanceType": "t2.micro"},
    "us-west-1"      : {"InstanceType": "t2.micro"},
    "eu-west-1"      : {"InstanceType": "t2.micro"},
    "eu-north-1"     : {"InstanceType": "t3.micro"},
    "me-south-1"     : {"InstanceType": "t3.micro"}
  }
}
```



#### YAML



```
Mappings:
  RegionMap:
    us-east-1:
      InstanceType: t2.micro
    us-west-1:
      InstanceType: t2.micro
    eu-west-1:
      InstanceType: t2.micro
    eu-north-1:
      InstanceType: t3.micro
    me-south-1:
      InstanceType: t3.micro
```


### Mapping with multiple
 values


The following example has region keys that are mapped to two sets of values: one named
 `MyAMI1` and the other `MyAMI2`.


###### Note

The AMI IDs shown in these examples are placeholders for demonstration purposes. Whenever possible, consider using dynamic references to AWS Systems Manager 
 parameters as an alternative to the `Mappings` section. To avoid
 updating all your templates with a new ID each time the AMI that you want to use changes,
 use a AWS Systems Manager parameter to retrieve the latest AMI ID when the stack is created or updated. The latest versions of
 commonly used AMIs are also available as public parameters in Systems Manager. For more information, 
 see [Get values stored in other services using dynamic references](dynamic-references.md "dynamic-references.md"). 



#### JSON



```
    "AMIIDMap" : {
      "us-east-1"        : {"MyAMI1" : "ami-12345678901234567", "MyAMI2" : "ami-23456789012345678"},
      "us-west-1"        : {"MyAMI1" : "ami-34567890123456789", "MyAMI2" : "ami-45678901234567890"},
      "eu-west-1"        : {"MyAMI1" : "ami-56789012345678901", "MyAMI2" : "ami-67890123456789012"},
      "ap-southeast-1"   : {"MyAMI1" : "ami-78901234567890123", "MyAMI2" : "ami-89012345678901234"},
      "ap-northeast-1"   : {"MyAMI1" : "ami-90123456789012345", "MyAMI2" : "ami-01234567890123456"}
    }
```



#### YAML



```
AMIIDMap: 
    us-east-1:
      MyAMI1: ami-12345678901234567
      MyAMI2: ami-23456789012345678
    us-west-1:
      MyAMI1: ami-34567890123456789
      MyAMI2: ami-45678901234567890
    eu-west-1:
      MyAMI1: ami-56789012345678901
      MyAMI2: ami-67890123456789012
    ap-southeast-1:
      MyAMI1: ami-78901234567890123
      MyAMI2: ami-89012345678901234
    ap-northeast-1:
      MyAMI1: ami-90123456789012345
      MyAMI2: ami-01234567890123456
```


### Return a value from a
 mapping


You can use the `Fn::FindInMap` function to return a named value based on a
 specified key. The following example template contains an Amazon EC2 resource whose
 `ImageId` property is assigned by the `FindInMap` function. The
 `FindInMap` function specifies key as the region where the stack is created
 (using the `AWS::Region` pseudo parameter) and `MyAMI1` as the name of
 the value to map to. For more information about pseudo parameters, see [Get AWS values using pseudo parameters](pseudo-parameter-reference.md "pseudo-parameter-reference.md").



#### JSON



```
{
  "AWSTemplateFormatVersion" : "2010-09-09",
  "Mappings" : {
    "AMIIDMap" : {
      "us-east-1"        : {"MyAMI1" : "ami-12345678901234567", "MyAMI2" : "ami-23456789012345678"},
      "us-west-1"        : {"MyAMI1" : "ami-34567890123456789", "MyAMI2" : "ami-45678901234567890"},
      "eu-west-1"        : {"MyAMI1" : "ami-56789012345678901", "MyAMI2" : "ami-67890123456789012"},
      "ap-northeast-1"   : {"MyAMI1" : "ami-90123456789012345", "MyAMI2" : "ami-01234567890123456"},
      "ap-southeast-1"   : {"MyAMI1" : "ami-78901234567890123", "MyAMI2" : "ami-89012345678901234"}
    }
  },
  "Resources" : {
    "myEC2Instance" : {
      "Type" : "AWS::EC2::Instance",
      "Properties" : {
        "ImageId" : { "Fn::FindInMap" : [ "AMIIDMap", { "Ref" : "AWS::Region" }, "MyAMI1" ]},
        "InstanceType" : "t2.micro"
      }
    }
  }
}
```



#### YAML



```
AWSTemplateFormatVersion: 2010-09-09
Mappings: 
  AMIIDMap: 
    us-east-1:
      MyAMI1: ami-12345678901234567
      MyAMI2: ami-23456789012345678
    us-west-1:
      MyAMI1: ami-34567890123456789
      MyAMI2: ami-45678901234567890
    eu-west-1:
      MyAMI1: ami-56789012345678901
      MyAMI2: ami-67890123456789012
    ap-northeast-1:
      MyAMI1: ami-90123456789012345
      MyAMI2: ami-01234567890123456
    ap-southeast-1:
      MyAMI1: ami-78901234567890123
      MyAMI2: ami-89012345678901234
Resources: 
  myEC2Instance: 
    Type: AWS::EC2::Instance
    Properties: 
      ImageId: !FindInMap [AMIIDMap, !Ref "AWS::Region", MyAMI1]
      InstanceType: t2.micro
```


### Input parameter and
 `Fn::FindInMap`


You can use an input parameter with the `Fn::FindInMap` function to refer to
 a specific value in a map. For example, suppose you have a list of regions and environment
 types that map to a specific security group ID. You can select the security group ID that
 your stack uses by using an input parameter (`EnvironmentType`). To determine the
 region, use the `AWS::Region` pseudo parameter, which gets the AWS Region in
 which you create the stack. 


This example also declares a Systems Manager parameter type that provides a Systems Manager parameter alias
 (`/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2`) as the
 default value for the `ImageId` property of the EC2 instance. This is a value
 that CloudFormation resolves as the AMI ID value for the latest Amazon Linux 2 AMI in the region
 where the stack is created.



#### JSON



```
{
  "AWSTemplateFormatVersion" : "2010-09-09",
  "Parameters" : {
    "LatestAmiId" : {
      "Description" : "The latest Amazon Linux 2 AMI from the Parameter Store",
      "Type" : "AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>",
      "Default" : "/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2"
    },
    "EnvironmentType" : {
      "Description" : "The environment type (Dev or Prod)",
      "Type" : "String",
      "Default" : "Dev",
      "AllowedValues" : [
        "Dev",
        "Prod"
      ]
    }
  },
  "Mappings" : {
    "SecurityGroupMap" : {
      "us-east-1" : {
        "Dev" : "sg-12345678",
        "Prod" : "sg-abcdef01"
      },
      "us-west-2" : {
        "Dev" : "sg-ghijkl23",
        "Prod" : "sg-45678abc"
      }
    }
  },
  "Resources" : {
    "Ec2Instance" : {
      "Type" : "AWS::EC2::Instance",
      "Properties" : {
        "ImageId" : {
          "Ref" : "LatestAmiId"
        },
        "InstanceType" : "t2.micro",
        "SecurityGroupIds" : [{ "Fn::FindInMap" : [ "SecurityGroupMap", { "Ref" : "AWS::Region" }, { "Ref" : "EnvironmentType" } ]}]
      }
    }
  }
}
```



#### YAML



```
AWSTemplateFormatVersion: 2010-09-09
Parameters:
  LatestAmiId:
    Description: The latest Amazon Linux 2 AMI from the Parameter Store
    Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
  EnvironmentType: 
    Description: The environment type (Dev or Prod)
    Type: String
    Default: Dev
    AllowedValues: 
      - Dev
      - Prod
Mappings: 
  SecurityGroupMap: 
    us-east-1: 
      Dev: sg-12345678
      Prod: sg-abcdef01
    us-west-2: 
      Dev: sg-ghijkl23
      Prod: sg-45678abc
Resources:
  Ec2Instance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: !Ref LatestAmiId
      InstanceType: t2.micro
      SecurityGroupIds:
        - !FindInMap [SecurityGroupMap, !Ref "AWS::Region", !Ref EnvironmentType]
```


## Related resources


These related topics can be helpful as you develop templates that use the
 `Fn::FindInMap` function.



* [Fn::FindInMap](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-findinmap.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-findinmap.html")
* [Fn::FindInMap enhancements](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-findinmap-enhancements.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-findinmap-enhancements.html")
* [Fn::Sub](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-sub.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-sub.html")
