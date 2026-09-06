

# Configure Amazon EC2 instances with CloudFormation
<a name="quickref-ec2-instance-config"></a>

The following snippets demonstrate how to configure Amazon EC2 instances using CloudFormation.

**Topics**
+ [General Amazon EC2 configurations](#quickref-ec2-instance-config-general)
+ [Specify the block device mappings for an instance](#scenario-ec2-bdm)

## General Amazon EC2 configurations
<a name="quickref-ec2-instance-config-general"></a>

The following snippets demonstrate general configurations for Amazon EC2 instances using CloudFormation.

**Topics**
+ [Create an Amazon EC2 instance in a specified Availability Zone](#scenario-ec2-instance)
+ [Configure a tagged Amazon EC2 instance with an EBS volume and user data](#scenario-ec2-instance-with-vol-and-tags)
+ [Define DynamoDB table name in user data for Amazon EC2 instance launch](#scenario-ec2-with-sdb-domain)
+ [Create an Amazon EBS volume with `DeletionPolicy`](#scenario-ec2-volume)

### Create an Amazon EC2 instance in a specified Availability Zone
<a name="scenario-ec2-instance"></a>

The following snippet creates an Amazon EC2 instance in the specified Availability Zone using an [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html) resource. The code for an Availability Zone is its Region code followed by a letter identifier. You can launch an instance into a single Availability Zone. 

#### JSON
<a name="quickref-ec2-example-6.json"></a>

```
1. "Ec2Instance": {
2.     "Type": "AWS::EC2::Instance",
3.     "Properties": {
4.         "AvailabilityZone": "{{aa-example-1a}}",
5.         "ImageId": "{{ami-1234567890abcdef0}}"
6.     }
7. }
```

#### YAML
<a name="quickref-ec2-example-6.yaml"></a>

```
1. Ec2Instance:
2.   Type: AWS::EC2::Instance
3.   Properties:
4.     AvailabilityZone: {{aa-example-1a}}
5.     ImageId: {{ami-1234567890abcdef0}}
```

### Configure a tagged Amazon EC2 instance with an EBS volume and user data
<a name="scenario-ec2-instance-with-vol-and-tags"></a>

The following snippet creates an Amazon EC2 instance with a tag, an EBS volume, and user data. It uses an [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html) resource. In the same template, you must define an [AWS::EC2::SecurityGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroup.html) resource, an [AWS::SNS::Topic](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sns-topic.html) resource, and an [AWS::EC2::Volume](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-volume.html) resource. The `KeyName` must be defined in the `Parameters` section of the template.

Tags can help you to categorize AWS resources based on your preferences, such as by purpose, owner, or environment. User data allows for the provisioning of custom scripts or data to an instance during launch. This data facilitates task automation, software configuration, package installation, and other actions on an instance during initialization. 

For more information about tagging your resources, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) in the *Amazon EC2 User Guide*. 

For information about user data, see [Use instance metadata to manage your EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) in the *Amazon EC2 User Guide*.

#### JSON
<a name="quickref-ec2-example-7.json"></a>

```
 1. "Ec2Instance": {
 2.   "Type": "AWS::EC2::Instance",
 3.   "Properties": {
 4.     "KeyName": { "Ref": "KeyName" },
 5.     "SecurityGroups": [ { "Ref": "Ec2SecurityGroup" } ],
 6.     "UserData": {
 7.       "Fn::Base64": {
 8.         "Fn::Join": [ ":", [
 9.             "PORT=80",
10.             "TOPIC=",
11.             { "Ref": "MySNSTopic" }
12.           ]
13.         ]
14.       }
15.     },
16.     "InstanceType": "{{aa.size}}",
17.     "AvailabilityZone": "{{aa-example-1a}}",
18.     "ImageId": "{{ami-1234567890abcdef0}}",
19.     "Volumes": [
20.       {
21.         "VolumeId": { "Ref": "MyVolumeResource" },
22.         "Device": "/dev/sdk"
23.       }
24.     ],
25.     "Tags": [ { "Key": "Name", "Value": "MyTag" } ]
26.   }
27. }
```

#### YAML
<a name="quickref-ec2-example-7.yaml"></a>

```
 1. Ec2Instance:
 2.   Type: AWS::EC2::Instance
 3.   Properties:
 4.     KeyName: !Ref KeyName
 5.     SecurityGroups:
 6.       - !Ref Ec2SecurityGroup
 7.     UserData:
 8.       Fn::Base64:
 9.         Fn::Join:
10.           - ":"
11.           - - "PORT=80"
12.             - "TOPIC="
13.             - !Ref MySNSTopic
14.     InstanceType: {{aa.size}}
15.     AvailabilityZone: {{aa-example-1a}}
16.     ImageId: {{ami-1234567890abcdef0}}
17.     Volumes:
18.       - VolumeId: !Ref MyVolumeResource
19.         Device: "/dev/sdk"
20.     Tags:
21.       - Key: Name
22.         Value: MyTag
```

### Define DynamoDB table name in user data for Amazon EC2 instance launch
<a name="scenario-ec2-with-sdb-domain"></a>

The following snippet creates an Amazon EC2 instance and defines a DynamoDB table name in the user data to pass to the instance at launch. It uses an [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html) resource. You can define parameters or dynamic values in the user data to pass an EC2 instance at launch. 

For more information about user data, see [Use instance metadata to manage your EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) in the *Amazon EC2 User Guide*.

#### JSON
<a name="quickref-ec2-example-8.json"></a>

```
 1. "Ec2Instance": {
 2.     "Type": "AWS::EC2::Instance",
 3.     "Properties": {
 4.         "UserData": {
 5.             "Fn::Base64": {
 6.                 "Fn::Join": [
 7.                     "",
 8.                     [
 9.                         "TableName=",
10.                         {
11.                             "Ref": "DynamoDBTableName"
12.                         }
13.                     ]
14.                 ]
15.             }
16.         },
17.         "AvailabilityZone": "{{aa-example-1a}}",
18.         "ImageId": "{{ami-1234567890abcdef0}}"
19.     }
20. }
```

#### YAML
<a name="quickref-ec2-example-8.yaml"></a>

```
 1. Ec2Instance:
 2.   Type: AWS::EC2::Instance
 3.   Properties:
 4.     UserData:
 5.       Fn::Base64:
 6.         Fn::Join:
 7.           - ''
 8.           - - 'TableName='
 9.             - Ref: DynamoDBTableName
10.     AvailabilityZone: {{aa-example-1a}}
11.     ImageId: {{ami-1234567890abcdef0}}
```

### Create an Amazon EBS volume with `DeletionPolicy`
<a name="scenario-ec2-volume"></a>

The following snippets create an Amazon EBS volume using an Amazon EC2 [AWS::EC2::Volume](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-volume.html) resource. You can use the `Size` or `SnapshotID` properties to define the volume, but not both. A `DeletionPolicy` attribute is set to create a snapshot of the volume when the stack is deleted. 

For more information about the `DeletionPolicy` attribute, see [DeletionPolicy attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-deletionpolicy.html).

For more information about creating Amazon EBS volumes, see [Create an Amazon EBS volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-creating-volume.html).

#### JSON
<a name="quickref-ec2-example-13.json"></a>

This snippet creates an Amazon EBS volume with a specified **size**. The size is set to 10, but you can adjust it as needed. The [AWS::EC2::Volume](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-volume.html) resource allows you to specify either the size or a snapshot ID but not both.

```
 1. "MyEBSVolume": {
 2.     "Type": "AWS::EC2::Volume",
 3.     "Properties": {
 4.         "Size": "10",
 5.         "AvailabilityZone": {
 6.             "Ref": "AvailabilityZone"
 7.         }
 8.     },
 9.     "DeletionPolicy": "Snapshot"
10. }
```

This snippet creates an Amazon EBS volume using a provided **snapshot ID**. The [AWS::EC2::Volume](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-volume.html) resource allows you to specify either the size or a snapshot ID but not both.

```
 1. "MyEBSVolume": {
 2.     "Type": "AWS::EC2::Volume",
 3.     "Properties": {
 4.         "SnapshotId" : "snap-1234567890abcdef0",
 5.         "AvailabilityZone": {
 6.             "Ref": "AvailabilityZone"
 7.         }
 8.     },
 9.     "DeletionPolicy": "Snapshot"
10. }
```

#### YAML
<a name="quickref-ec2-example-13.yaml"></a>

This snippet creates an Amazon EBS volume with a specified **size**. The size is set to 10, but you can adjust it as needed. The [AWS::EC2::Volume](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-volume.html) resource allows you to specify either the size or a snapshot ID but not both.

```
1. MyEBSVolume:
2.   Type: AWS::EC2::Volume
3.   Properties:
4.     Size: 10
5.     AvailabilityZone:
6.       Ref: AvailabilityZone
7.   DeletionPolicy: Snapshot
```

This snippet creates an Amazon EBS volume using a provided **snapshot ID**. The [AWS::EC2::Volume](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-volume.html) resource allows you to specify either the size or a snapshot ID but not both.

```
1. MyEBSVolume:
2.   Type: AWS::EC2::Volume
3.   Properties:
4.     SnapshotId: snap-1234567890abcdef0
5.     AvailabilityZone:
6.       Ref: AvailabilityZone
7.   DeletionPolicy: Snapshot
```

## Specify the block device mappings for an instance
<a name="scenario-ec2-bdm"></a>

A block device mapping defines the block devices, which includes instance store volumes and EBS volumes, to attach to an instance. You can specify a block device mapping when creating an AMI so that the mapping is used by all instances launched from the AMI. Alternatively, you can specify a block device mapping when you launch an instance, so that the mapping overrides the one specified in the AMI from which the instance was launched.

You can use the following template snippets to specify the block device mappings for your EBS or instance store volumes using the `BlockDeviceMappings` property of an [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html) resource. 

For more information about block device mappings, see [Block device mappings for volumes on Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html) in the *Amazon EC2 User Guide*.

**Topics**
+ [Specify the block device mappings for two EBS volumes](#w2aac11c41c43c13b9c11)
+ [Specify the block device mapping for an instance store volume](#w2aac11c41c43c13b9c13)

### Specify the block device mappings for two EBS volumes
<a name="w2aac11c41c43c13b9c11"></a>

#### JSON
<a name="quickref-ec2-example-1.json"></a>

```
"Ec2Instance": {
    "Type": "AWS::EC2::Instance",
    "Properties": {
      "ImageId": "{{resolve:ssm:/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2}}",
      "KeyName": { "Ref": "KeyName" },
      "InstanceType": { "Ref": "InstanceType" },
      "SecurityGroups": [{ "Ref": "Ec2SecurityGroup" }],
      "BlockDeviceMappings": [
        {
          "DeviceName": "{{/dev/sda1}}",
          "Ebs": { "VolumeSize": "{{50}}" }
        },
        {
          "DeviceName": "{{/dev/sdm}}",
          "Ebs": { "VolumeSize": "{{100}}" }
        }
      ]
    }
  }
}
```

#### YAML
<a name="quickref-ec2-example-1.yaml"></a>

```
EC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: '{{resolve:ssm:/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2}}'
      KeyName: !Ref KeyName
      InstanceType: !Ref InstanceType
      SecurityGroups:
        - !Ref Ec2SecurityGroup
      BlockDeviceMappings:
        -
          DeviceName: {{/dev/sda1}}
          Ebs:
            VolumeSize: {{50}}
        -
          DeviceName: {{/dev/sdm}}
          Ebs:
            VolumeSize: {{100}}
```

### Specify the block device mapping for an instance store volume
<a name="w2aac11c41c43c13b9c13"></a>

#### JSON
<a name="quickref-ec2-example-2.json"></a>

```
"Ec2Instance" : {
  "Type" : "AWS::EC2::Instance", 
  "Properties" : {
    "ImageId" : "{{resolve:ssm:/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2}}",
    "KeyName" : { "Ref" : "KeyName" },
    "InstanceType": { "Ref": "InstanceType" },
    "SecurityGroups" : [{ "Ref" : "Ec2SecurityGroup" }],
    "BlockDeviceMappings" : [
      {
        "DeviceName"  : "{{/dev/sdc}}",
        "VirtualName" : "{{ephemeral0}}"
      }
    ]
  }
}
```

#### YAML
<a name="quickref-ec2-example-2.yaml"></a>

```
EC2Instance:
  Type: AWS::EC2::Instance
  Properties:
    ImageId: '{{resolve:ssm:/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2}}'
    KeyName: !Ref KeyName
    InstanceType: !Ref InstanceType
    SecurityGroups:
      - !Ref Ec2SecurityGroup
    BlockDeviceMappings:
      - DeviceName: {{/dev/sdc}}
        VirtualName: {{ephemeral0}}
```