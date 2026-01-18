This is the new _CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# Examples of

`Fn::ForEach` in the `Resources` section

These examples demonstrate using the `Fn::ForEach` intrinsic function in the
`Resources` section. For more information about this section, see [Resources](../UserGuide/resources-section-structure.md "../UserGuide/resources-section-structure.md") in
the _AWS CloudFormation User Guide_.

###### Topics

- [Replicate an Amazon SNS resource](#intrinsic-function-reference-foreach-example-replicate-resource "#intrinsic-function-reference-foreach-example-replicate-resource")
- [Replicate an Amazon DynamoDB resource](#intrinsic-function-reference-foreach-example-replicate-ddb-resource "#intrinsic-function-reference-foreach-example-replicate-ddb-resource")
- [Replicate multiple resources](#intrinsic-function-reference-foreach-example-replicate-multiple-resources "#intrinsic-function-reference-foreach-example-replicate-multiple-resources")
- [Replicate multiple resources using a nested Fn::ForEach loops](#intrinsic-function-reference-foreach-example-nested-loop-resources "#intrinsic-function-reference-foreach-example-nested-loop-resources")
- [Reference replicated properties for an Amazon EC2 resource](#intrinsic-function-reference-foreach-example-reference-replicated-resource "#intrinsic-function-reference-foreach-example-reference-replicated-resource")
- [Replicate properties for an Amazon EC2 resource](#intrinsic-function-reference-foreach-example-replicate-resource-properties "#intrinsic-function-reference-foreach-example-replicate-resource-properties")
- [Passing
  non-alphanumeric characters within the Collection for
  Fn::ForEach](#intrinsic-function-reference-foreach-example-non-alphanumeric "#intrinsic-function-reference-foreach-example-non-alphanumeric")

## Replicate an Amazon SNS resource

This example snippet returns a list of four Amazon SNS topics, with the logical ID
corresponding to the items in the collection (`Success`, `Failure`,
`Timeout`, `Unknown`), with a matching `TopicName` and
`FifoTopic` set to `true`.

###### Note

For templates that need to work with both FIFO and standard topics, you can use the
`DisplayName` property instead of `TopicName`. This allows
CloudFormation to automatically generate topic names with the appropriate `.fifo`
suffix when `FifoTopic` is `true`. Simply replace
`TopicName` with `DisplayName: !Ref TopicName` in the
`Properties` section.

### JSON

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Transform": "AWS::LanguageExtensions",
    "Resources": {
        "Fn::ForEach::Topics": [
            "TopicName",
            ["Success", "Failure", "Timeout", "Unknown"],
            {
                "SnsTopic${TopicName}": {
                    "Type": "AWS::SNS::Topic",
                    "Properties": {
                        "TopicName": {"Fn::Sub": "${TopicName}.fifo"},
                        "FifoTopic": true
                    }
                }
            }
        ]
    }
}
```

### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Transform: AWS::LanguageExtensions
Resources:
  'Fn::ForEach::Topics':
    - TopicName
    - [Success, Failure, Timeout, Unknown]
    - 'SnsTopic${TopicName}':
        Type: AWS::SNS::Topic
        Properties:
          TopicName: !Sub '${TopicName}.fifo'
          FifoTopic: true
```

The transformed template will be equivalent to the following template:

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  SnsTopicSuccess:
    Type: AWS::SNS::Topic
    Properties:
      TopicName: Success.fifo
      FifoTopic: true
  SnsTopicFailure:
    Type: AWS::SNS::Topic
    Properties:
      TopicName: Failure.fifo
      FifoTopic: true
  SnsTopicTimeout:
    Type: AWS::SNS::Topic
    Properties:
      TopicName: Timeout.fifo
      FifoTopic: true
  SnsTopicUnknown:
    Type: AWS::SNS::Topic
    Properties:
      TopicName: Unknown.fifo
      FifoTopic: true

```

## Replicate an Amazon DynamoDB resource

This example snippet creates four [AWS::DynamoDB::Table](aws-resource-dynamodb-table.md "aws-resource-dynamodb-table.md") resources
with names such as `Points`, `Score`, etc.

### JSON

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Transform": "AWS::LanguageExtensions",
    "Resources": {
        "Fn::ForEach::Tables": [
            "TableName",
            ["Points", "Score", "Name", "Leaderboard"],
            {
                "DynamoDB${TableName}": {
                    "Type": "AWS::DynamoDB::Table",
                    "Properties": {
                        "TableName": {
                            "Ref": "TableName"
                        },
                        "AttributeDefinitions": [
                            {
                                "AttributeName": "id",
                                "AttributeType": "S"
                            }
                        ],
                        "KeySchema": [
                            {
                                "AttributeName": "id",
                                "KeyType": "HASH"
                            }
                        ],
                        "ProvisionedThroughput": {
                            "ReadCapacityUnits": "5",
                            "WriteCapacityUnits": "5"
                        }
                    }
                }
            }
        ]
    }
}
```

### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Transform: AWS::LanguageExtensions
Resources:
  'Fn::ForEach::Tables':
    - TableName
    - [Points, Score, Name, Leaderboard]
    - 'DynamoDB${TableName}':
        Type: AWS::DynamoDB::Table
        Properties:
          TableName: !Ref TableName
          AttributeDefinitions:
            - AttributeName: id
              AttributeType: S
          KeySchema:
            - AttributeName: id
              KeyType: HASH
          ProvisionedThroughput:
            ReadCapacityUnits: '5'
            WriteCapacityUnits: '5'
```

The transformed template will be equivalent to the following template:

```
AWSTemplateFormatVersion: 2010-09-09
Transform: AWS::LanguageExtensions
Resources:
  DynamoDBPoints:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: Points
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: S
      KeySchema:
        - AttributeName: id
          KeyType: HASH
      ProvisionedThroughput:
        ReadCapacityUnits: '5'
        WriteCapacityUnits: '5'
  DynamoDBScore:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: Score
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: S
      KeySchema:
        - AttributeName: id
          KeyType: HASH
      ProvisionedThroughput:
        ReadCapacityUnits: '5'
        WriteCapacityUnits: '5'
  DynamoDBName:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: Name
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: S
      KeySchema:
        - AttributeName: id
          KeyType: HASH
      ProvisionedThroughput:
        ReadCapacityUnits: '5'
        WriteCapacityUnits: '5'
  DynamoDBLeaderboard:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: Leaderboard
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: S
      KeySchema:
        - AttributeName: id
          KeyType: HASH
      ProvisionedThroughput:
        ReadCapacityUnits: '5'
        WriteCapacityUnits: '5'
```

## Replicate multiple resources

This example creates multiple instances of [AWS::EC2::NatGateway](aws-resource-ec2-natgateway.md "aws-resource-ec2-natgateway.md") and
[AWS::EC2::EIP](aws-resource-ec2-eip.md "aws-resource-ec2-eip.md") using a naming convention of `"{ResourceType}${Identifier}"`. You
can declare multiple resource types under one `Fn::ForEach` loop to take
advantage of a single identifier.

Unique values for each element in the collection are defined within the `Mappings`
section, where the [Fn::FindInMap](intrinsic-function-reference-findinmap.md "intrinsic-function-reference-findinmap.md") intrinsic function is used to
reference the corresponding value. If `Fn::FindInMap` is unable to find the
corresponding identifier, the `Condition` property will not be set resolving
to `!Ref AWS:::NoValue`.

### JSON

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Transform": "AWS::LanguageExtensions",
  "Conditions": {
    "TwoNatGateways": {"Fn::Equals": [{"Ref": "AWS::Region"}, "us-east-1"]},
    "ThreeNatGateways": {"Fn::Equals": [{"Ref": "AWS::Region"}, "us-west-2"]}
  },
  "Mappings": {
    "NatGateway": {
      "Condition": {
        "B": "TwoNatGateways",
        "C": "ThreeNatGateways"
      }
    }
  },
  "Resources": {
    "VPC": {
      "Type": "AWS::EC2::VPC",
      "Properties": {"CidrBlock": "10.0.0.0/16"}
    },
    "PublicSubnetA": {
      "Type": "AWS::EC2::Subnet",
      "Properties": {
        "VpcId": {"Ref": "VPC"},
        "CidrBlock": "10.0.1.0/24",
        "AvailabilityZone": {"Fn::Select": [0, {"Fn::GetAZs": ""}]}
      }
    },
    "PublicSubnetB": {
      "Type": "AWS::EC2::Subnet",
      "Properties": {
        "VpcId": {"Ref": "VPC"},
        "CidrBlock": "10.0.2.0/24",
        "AvailabilityZone": {"Fn::Select": [1, {"Fn::GetAZs": ""}]}
      }
    },
    "PublicSubnetC": {
      "Type": "AWS::EC2::Subnet",
      "Properties": {
        "VpcId": {"Ref": "VPC"},
        "CidrBlock": "10.0.3.0/24",
        "AvailabilityZone": {"Fn::Select": [2, {"Fn::GetAZs": ""}]}
      }
    },
    "Fn::ForEach::NatGatewayAndEIP": [
      "Identifier",
      [ "A", "B", "C" ],
      {
        "NatGateway${Identifier}": {
          "Type": "AWS::EC2::NatGateway",
          "Properties": {
            "AllocationId": {"Fn::GetAtt": [{"Fn::Sub": "NatGatewayAttachment${Identifier}"}, "AllocationId"]},
            "SubnetId": {"Ref": {"Fn::Sub": "PublicSubnet${Identifier}"}}
          },
          "Condition": {"Fn::FindInMap": ["NatGateway", "Condition", {"Ref": "Identifier"}, {"DefaultValue": {"Ref": "AWS::NoValue"}}]}
        },
        "NatGatewayAttachment${Identifier}": {
          "Type": "AWS::EC2::EIP",
          "Properties": {
            "Domain": "vpc"
          },
          "Condition": {"Fn::FindInMap": ["NatGateway", "Condition", {"Ref": "Identifier"}, {"DefaultValue": {"Ref": "AWS::NoValue"}}]}
        }
      }
    ]
  }
}
```

### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Transform: AWS::LanguageExtensions
Conditions:
  TwoNatGateways: !Equals [!Ref "AWS::Region", "us-east-1"]
  ThreeNatGateways: !Equals [!Ref "AWS::Region", "us-west-2"]
Mappings:
  NatGateway:
    Condition:
      B: TwoNatGateways
      C: ThreeNatGateways
Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
  PublicSubnetA:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: 10.0.1.0/24
      AvailabilityZone: !Select [0, !GetAZs ""]
  PublicSubnetB:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: 10.0.2.0/24
      AvailabilityZone: !Select [1, !GetAZs ""]
  PublicSubnetC:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: 10.0.3.0/24
      AvailabilityZone: !Select [2, !GetAZs ""]
  Fn::ForEach::NatGatewayAndEIP:
    - Identifier
    - - A
      - B
      - C
    - NatGateway${Identifier}:
        Type: AWS::EC2::NatGateway
        Properties:
          AllocationId: !GetAtt
            - !Sub NatGatewayAttachment${Identifier}
            - AllocationId
          SubnetId: !Ref
            Fn::Sub: PublicSubnet${Identifier}
        Condition: !FindInMap
          - NatGateway
          - Condition
          - !Ref Identifier
          - DefaultValue: !Ref AWS::NoValue
      NatGatewayAttachment${Identifier}:
        Type: AWS::EC2::EIP
        Properties:
          Domain: vpc
        Condition: !FindInMap
          - NatGateway
          - Condition
          - !Ref Identifier
          - DefaultValue: !Ref AWS::NoValue
```

The transformed template will be equivalent to the following template:

```
AWSTemplateFormatVersion: 2010-09-09
Transform: AWS::LanguageExtensions
Conditions:
  TwoNatGateways: !Equals [!Ref "AWS::Region", "us-east-1"]
  ThreeNatGateways: !Equals [!Ref "AWS::Region", "us-west-2"]
Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
  PublicSubnetA:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: 10.0.1.0/24
      AvailabilityZone: !Select [0, !GetAZs ""]
  PublicSubnetB:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: 10.0.2.0/24
      AvailabilityZone: !Select [1, !GetAZs ""]
  PublicSubnetC:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: 10.0.3.0/24
      AvailabilityZone: !Select [2, !GetAZs ""]
  NatGatewayA:
    Type: AWS::EC2::NatGateway
    Properties:
      AllocationId: !GetAtt
        - NatGatewayAttachmentA
        - AllocationId
      SubnetId: !Ref PublicSubnetA
  NatGatewayB:
    Type: AWS::EC2::NatGateway
    Properties:
      AllocationId: !GetAtt
        - NatGatewayAttachmentB
        - AllocationId
      SubnetId: !Ref PublicSubnetB
    Condition: TwoNatGateways
  NatGatewayC:
    Type: AWS::EC2::NatGateway
    Properties:
      AllocationId: !GetAtt
        - NatGatewayAttachmentC
        - AllocationId
      SubnetId: !Ref PublicSubnetC
    Condition: ThreeNatGateways
  NatGatewayAttachmentA:
    Type: AWS::EC2::EIP
    Properties:
      Domain: vpc
  NatGatewayAttachmentB:
    Type: AWS::EC2::EIP
    Properties:
      Domain: vpc
    Condition: TwoNatGateways
  NatGatewayAttachmentC:
    Type: AWS::EC2::EIP
    Properties:
      Domain: vpc
    Condition: ThreeNatGateways
```

## Replicate multiple resources using a nested `Fn::ForEach` loops

This example uses nested `Fn::ForEach` loops to map three resources (
[AWS::EC2::NetworkAcl](aws-resource-ec2-natgateway.md "aws-resource-ec2-natgateway.md"), [AWS::EC2::Subnet](aws-resource-ec2-subnet.md "aws-resource-ec2-subnet.md"), and [AWS::EC2::SubnetNetworkAclAssociation](aws-resource-ec2-subnetnetworkaclassociation.md "aws-resource-ec2-subnetnetworkaclassociation.md")) with each other.

### JSON

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Transform": "AWS::LanguageExtensions",
  "Resources": {
    "VPC": {
      "Type": "AWS::EC2::VPC",
      "Properties": {
        "CidrBlock": "10.0.0.0/16",
        "EnableDnsSupport": "true",
        "EnableDnsHostnames": "true"
      }
    },
    "Fn::ForEach::SubnetResources": [
      "Prefix",
      [
        "Transit",
        "Public"
      ],
      {
        "Nacl${Prefix}Subnet": {
          "Type": "AWS::EC2::NetworkAcl",
          "Properties": {
            "VpcId": {
              "Ref": "VPC"
            }
          }
        },
        "Fn::ForEach::LoopInner": [
          "Suffix",
          [
            "A",
            "B",
            "C"
          ],
          {
            "${Prefix}Subnet${Suffix}": {
              "Type": "AWS::EC2::Subnet",
              "Properties": {
                "VpcId": {
                  "Ref": "VPC"
                }
              }
            },
            "Nacl${Prefix}Subnet${Suffix}Association": {
              "Type": "AWS::EC2::SubnetNetworkAclAssociation",
              "Properties": {
                "SubnetId": {
                  "Ref": {
                    "Fn::Sub": "${Prefix}Subnet${Suffix}"
                  }
                },
                "NetworkAclId": {
                  "Ref": {
                    "Fn::Sub": "Nacl${Prefix}Subnet"
                  }
                }
              }
            }
          }
        ]
      }
    ]
  }
}
```

### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Transform: AWS::LanguageExtensions
Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: 'true'
      EnableDnsHostnames: 'true'
  'Fn::ForEach::SubnetResources':
  - Prefix
  - [Transit, Public]
  - 'Nacl${Prefix}Subnet':
      Type: AWS::EC2::NetworkAcl
      Properties:
        VpcId: !Ref 'VPC'
    'Fn::ForEach::LoopInner':
    - Suffix
    - [A, B, C]
    - '${Prefix}Subnet${Suffix}':
        Type: AWS::EC2::Subnet
        Properties:
          VpcId: !Ref 'VPC'
      'Nacl${Prefix}Subnet${Suffix}Association':
        Type: AWS::EC2::SubnetNetworkAclAssociation
        Properties:
          SubnetId: !Ref
            'Fn::Sub': '${Prefix}Subnet${Suffix}'
          NetworkAclId: !Ref
            'Fn::Sub': 'Nacl${Prefix}Subnet'
```

The transformed template will be equivalent to the following template:

```
AWSTemplateFormatVersion: 2010-09-09
Transform: AWS::LanguageExtensions
Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: 'true'
      EnableDnsHostnames: 'true'
  NaclTransitSubnet:
    Type: AWS::EC2::NetworkAcl
    Properties:
      VpcId: !Ref VPC
  TransitSubnetA:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
  NaclTransitSubnetAAssociation:
    Type: AWS::EC2::SubnetNetworkAclAssociation
    Properties:
      SubnetId: !Ref TransitSubnetA
      NetworkAclId: !Ref NaclTransitSubnet
  TransitSubnetB:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
  NaclTransitSubnetBAssociation:
    Type: AWS::EC2::SubnetNetworkAclAssociation
    Properties:
      SubnetId: !Ref TransitSubnetB
      NetworkAclId: !Ref NaclTransitSubnet
  TransitSubnetC:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
  NaclTransitSubnetCAssociation:
    Type: AWS::EC2::SubnetNetworkAclAssociation
    Properties:
      SubnetId: !Ref TransitSubnetC
      NetworkAclId: !Ref NaclTransitSubnet
  NaclPublicSubnet:
    Type: AWS::EC2::NetworkAcl
    Properties:
      VpcId: !Ref VPC
  PublicSubnetA:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
  NaclPublicSubnetAAssociation:
    Type: AWS::EC2::SubnetNetworkAclAssociation
    Properties:
      SubnetId: !Ref PublicSubnetA
      NetworkAclId: !Ref NaclPublicSubnet
  PublicSubnetB:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
  NaclPublicSubnetBAssociation:
    Type: AWS::EC2::SubnetNetworkAclAssociation
    Properties:
      SubnetId: !Ref PublicSubnetB
      NetworkAclId: !Ref NaclPublicSubnet
  PublicSubnetC:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
  NaclPublicSubnetCAssociation:
    Type: AWS::EC2::SubnetNetworkAclAssociation
    Properties:
      SubnetId: !Ref PublicSubnetC
      NetworkAclId: !Ref NaclPublicSubnet
```

## Reference replicated properties for an Amazon EC2 resource

This example uses the `Fn::ForEach` intrinsic function to reference
replicated [AWS::EC2::Instance](aws-resource-ec2-instance.md "aws-resource-ec2-instance.md") resources.

### JSON

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Transform": "AWS::LanguageExtensions",
  "Mappings": {
    "Instances": {
      "InstanceType": {
        "B": "m5.4xlarge",
        "C": "c5.2xlarge"
      },
      "ImageId": {"A": "`ami-id1`"}
    }
  },
  "Resources": {
    "Fn::ForEach::Instances": [
      "Identifier",
      [
        "A",
        "B",
        "C"
      ],
      {
        "Instance${Identifier}": {
          "Type": "AWS::EC2::Instance",
          "Properties": {
            "InstanceType": {"Fn::FindInMap": ["Instances", "InstanceType", {"Ref": "Identifier"}, {"DefaultValue": "m5.xlarge"}]},
            "ImageId": {"Fn::FindInMap": ["Instances", "ImageId", {"Ref": "Identifier"}, {"DefaultValue": "`ami-id-default`"}]}
          }
        }
      }
    ]
  },
  "Outputs": {
    "SecondInstanceId": {
      "Description": "Instance Id for InstanceB",
      "Value": {"Ref": "InstanceB"}
    },
    "SecondPrivateIp": {
      "Description": "Private IP for InstanceB",
      "Value": {
        "Fn::GetAtt": [
          "InstanceB",
          "PrivateIp"
        ]
      }
    }
  }
}
```

### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Transform: AWS::LanguageExtensions
Mappings:
  Instances:
    InstanceType:
      B: m5.4xlarge
      C: c5.2xlarge
    ImageId:
      A: `ami-id1`
Resources:
  'Fn::ForEach::Instances':
  - Identifier
  - [A, B, C]
  - 'Instance${Identifier}':
      Type: AWS::EC2::Instance
      Properties:
        InstanceType: !FindInMap [Instances, InstanceType, !Ref 'Identifier', {DefaultValue: m5.xlarge}]
        ImageId: !FindInMap [Instances, ImageId, !Ref 'Identifier', {DefaultValue: `ami-id-default`}]
Outputs:
  SecondInstanceId:
    Description: Instance Id for InstanceB
    Value: !Ref 'InstanceB'
  SecondPrivateIp:
    Description: Private IP for InstanceB
    Value: !GetAtt [InstanceB, PrivateIp]
```

The transformed template will be equivalent to the following template:

```
AWSTemplateFormatVersion: 2010-09-09
Transform: AWS::LanguageExtensions
Resources:
  InstanceA:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: m5.xlarge
      ImageId: `ami-id1`
  InstanceB:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: m5.4xlarge
      ImageId: `ami-id-default`
  InstanceC:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: c5.2xlarge
      ImageId: `ami-id-default`
Outputs:
  SecondInstanceId:
    Description: Instance Id for InstanceB
    Value: !Ref InstanceB
  SecondPrivateIp:
    Description: Private IP for InstanceB
    Value: !GetAtt [InstanceB, PrivateIp]
```

## Replicate properties for an Amazon EC2 resource

This example uses the `Fn::ForEach` intrinsic function to repeat some
properties like `ImageId`, `InstanceType`, and
`AvailabilityZone` to an [AWS::EC2::Instance](aws-resource-ec2-instance.md "aws-resource-ec2-instance.md")
resource.

### JSON

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Transform": "AWS::LanguageExtensions",
  "Mappings": {
    "InstanceA": {
      "Properties": {
        "ImageId": "`ami-id1`",
        "InstanceType": "m5.xlarge"
      }
    },
    "InstanceB": {
      "Properties": {
        "ImageId": "`ami-id2`"
      }
    },
    "InstanceC": {
      "Properties": {
        "ImageId": "`ami-id3`",
        "InstanceType": "m5.2xlarge",
        "AvailabilityZone": "us-east-1a"
      }
    }
  },
  "Resources": {
    "Fn::ForEach::Instances": [
      "InstanceLogicalId",
      [ "InstanceA", "InstanceB", "InstanceC" ],
      {
        "${InstanceLogicalId}": {
          "Type": "AWS::EC2::Instance",
          "Properties": {
            "DisableApiTermination": true,
            "UserData": {
              "Fn::Base64": {
                "Fn::Join": [
                  "",
                  [
                    "#!/bin/bash\n",
                    "yum update -y\n",
                    "yum install -y httpd.x86_64\n",
                    "systemctl start httpd.service\n",
                    "systemctl enable httpd.service\n",
                    "echo \"Hello World from $(hostname -f)\" > /var/www/html/index.html\n"
                  ]
                ]
              }
            },
            "Fn::ForEach::Properties": [
              "PropertyName",
              [ "ImageId", "InstanceType", "AvailabilityZone" ],
              {
                "${PropertyName}": {
                  "Fn::FindInMap": [
                    { "Ref": "InstanceLogicalId" },
                    "Properties",
                    { "Ref": "PropertyName"},
                    {
                      "DefaultValue": { "Ref": "AWS::NoValue" }
                    }
                  ]
                }
              }
            ]
          }
        }
      }
    ]
  }
}
```

### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Transform: AWS::LanguageExtensions
Mappings:
  InstanceA:
    Properties:
      ImageId: `ami-id1`
      InstanceType: m5.xlarge
  InstanceB:
    Properties:
      ImageId: `ami-id2`
  InstanceC:
    Properties:
      ImageId: `ami-id3`
      InstanceType: m5.2xlarge
      AvailabilityZone: us-east-1a
Resources:
  'Fn::ForEach::Instances':
  - InstanceLogicalId
  - [InstanceA, InstanceB, InstanceC]
  - '${InstanceLogicalId}':
      Type: AWS::EC2::Instance
      Properties:
        DisableApiTermination: true
        UserData:
          Fn::Base64: !Sub |
            #!/bin/bash
            yum update -y
            yum install -y httpd.x86_64
            systemctl start httpd.service
            systemctl enable httpd.service
            echo "Hello World from $(hostname -f)" > /var/www/html/index.html
        'Fn::ForEach::Properties':
          - PropertyName
          - [ImageId, InstanceType, AvailabilityZone]
          - '${PropertyName}':
             'Fn::FindInMap':
               - Ref: 'InstanceLogicalId'
               - Properties
               - Ref: 'PropertyName'
               - {DefaultValue: !Ref 'AWS::NoValue'}
```

The transformed template will be equivalent to the following template:

```
AWSTemplateFormatVersion: 2010-09-09
Transform: AWS::LanguageExtensions
Resources:
  InstanceA:
    Type: AWS::EC2::Instance
    Properties:
      DisableApiTermination: true
      UserData:
        Fn::Base64:
          !Sub |
            #!/bin/bash
            yum update -y
            yum install -y httpd.x86_64
            systemctl start httpd.service
            systemctl enable httpd.service
            echo "Hello World from $(hostname -f)" > /var/www/html/index.html
      ImageId: `ami-id1`
      InstanceType: m5.xlarge
  InstanceB:
    Type: AWS::EC2::Instance
    Properties:
      DisableApiTermination: true
      UserData:
        Fn::Base64:
          !Sub |
            #!/bin/bash
            yum update -y
            yum install -y httpd.x86_64
            systemctl start httpd.service
            systemctl enable httpd.service
            echo "Hello World from $(hostname -f)" > /var/www/html/index.html
      ImageId: `ami-id2`
  InstanceC:
    Type: AWS::EC2::Instance
    Properties:
      DisableApiTermination: true
      UserData:
        Fn::Base64:
          !Sub |
            #!/bin/bash
            yum update -y
            yum install -y httpd.x86_64
            systemctl start httpd.service
            systemctl enable httpd.service
            echo "Hello World from $(hostname -f)" > /var/www/html/index.html
      ImageId: `ami-id3`
      InstanceType: m5.2xlarge
      AvailabilityZone: us-east-1a
```

## Passing

non-alphanumeric characters within the `Collection` for
`Fn::ForEach`

This example uses the `&{}` syntax, which allows the non-alphanumeric
characters (`.` and `/`) in the IP addresses to be passed within the
`Collection`.

### JSON

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Transform": "AWS::LanguageExtensions",
    "Parameters": {
        "IpAddresses": {
            "Type": "CommaDelimitedList",
            "Default": "10.0.2.0/24,10.0.3.0/24,10.0.4.0/24"
        }
    },
    "Resources": {
        "VPC": {
            "Type": "AWS::EC2::VPC",
            "Properties": {
                "CidrBlock": "10.0.0.0/16",
                "EnableDnsSupport": "true",
                "EnableDnsHostnames": "true"
            }
        },
        "Fn::ForEach::Subnets": [
            "CIDR",
            {
                "Ref": "IpAddresses"
            },
            {
                "Subnet&{CIDR}": {
                    "Type": "AWS::EC2::Subnet",
                    "Properties": {
                        "VpcId": {
                            "Ref": "VPC"
                        },
                        "CidrBlock": {
                            "Ref": "CIDR"
                        }
                    }
                }
            }
        ]
    }
}
```

### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Transform: AWS::LanguageExtensions
Parameters:
  IpAddresses:
    Type: CommaDelimitedList
    Default: '10.0.2.0/24,10.0.3.0/24,10.0.4.0/24'
Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: 'true'
      EnableDnsHostnames: 'true'
  'Fn::ForEach::Subnets':
    - CIDR
    - !Ref IpAddresses
    - 'Subnet&{CIDR}':
        Type: AWS::EC2::Subnet
        Properties:
          VpcId: !Ref VPC
          CidrBlock: !Ref CIDR
```

The transformed template will be equivalent to the following template:

```
AWSTemplateFormatVersion: 2010-09-09
Transform: AWS::LanguageExtensions
Parameters:
  IpAddresses:
    Type: CommaDelimitedList
    Default: '10.0.2.0/24,10.0.3.0/24,10.0.4.0/24'
Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: 'true'
      EnableDnsHostnames: 'true'
  Subnet1002024:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: 10.0.2.0/24
  Subnet1003024:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: 10.0.3.0/24
  Subnet1004024:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: 10.0.4.0/24
```
