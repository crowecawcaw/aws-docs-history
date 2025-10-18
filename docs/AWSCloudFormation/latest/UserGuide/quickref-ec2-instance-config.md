# Configure Amazon EC2 instances with
 CloudFormation

The following snippets demonstrate how to configure Amazon EC2 instances using
 CloudFormation.

###### Snippet categories

* [General Amazon EC2
 configurations](#quickref-ec2-instance-config-general "#quickref-ec2-instance-config-general")
* [Specify the block device mappings for an
 instance](#scenario-ec2-bdm "#scenario-ec2-bdm")

## General Amazon EC2
 configurations


The following snippets demonstrate general configurations for Amazon EC2 instances
 using CloudFormation.


###### Example snippets

* [Create an Amazon EC2 instance in a specified
 Availability Zone](#scenario-ec2-instance "#scenario-ec2-instance")
* [Configure a tagged
 Amazon EC2 instance with an EBS volume and user data](#scenario-ec2-instance-with-vol-and-tags "#scenario-ec2-instance-with-vol-and-tags")
* [Define DynamoDB table name in
 user data for Amazon EC2 instance launch](#scenario-ec2-with-sdb-domain "#scenario-ec2-with-sdb-domain")
* [Create an Amazon EBS volume with
 DeletionPolicy](#scenario-ec2-volume "#scenario-ec2-volume")

### Create an Amazon EC2 instance in a specified
 Availability Zone


The following snippet creates an Amazon EC2 instance in the specified Availability
 Zone using an [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html")
 resource. The code for an Availability Zone is its Region code followed by a
 letter identifier. You can launch an instance into a single Availability Zone. 



#### JSON



```
"Ec2Instance": {
    "Type": "AWS::EC2::Instance",
    "Properties": {
        "AvailabilityZone": "`aa-example-1a`",
        "ImageId": "`ami-1234567890abcdef0`"
    }
}
```



#### YAML



```
Ec2Instance:
  Type: AWS::EC2::Instance
  Properties:
    AvailabilityZone: `aa-example-1a`
    ImageId: `ami-1234567890abcdef0`
```


### Configure a tagged
 Amazon EC2 instance with an EBS volume and user data


The following snippet creates an Amazon EC2 instance with a tag, an EBS volume, and
 user data. It uses an [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html")
 resource. In the same template, you must define an [AWS::EC2::SecurityGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroup.html") resource, an [AWS::SNS::Topic](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sns-topic.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sns-topic.html")
 resource, and an [AWS::EC2::Volume](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-volume.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-volume.html")
 resource. The `KeyName` must be defined in the
 `Parameters` section of the template.


Tags can help you to categorize AWS resources based on your preferences,
 such as by purpose, owner, or environment. User data allows for the provisioning
 of custom scripts or data to an instance during launch. This data facilitates
 task automation, software configuration, package installation, and other actions
 on an instance during initialization. 


For more information about tagging your resources, see [Tag your
 Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html") in the *Amazon EC2 User Guide*. 


For information about user data, see [Use instance
 metadata to manage your EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html") in the
 *Amazon EC2 User Guide*.



#### JSON



```
"Ec2Instance": {
  "Type": "AWS::EC2::Instance",
  "Properties": {
    "KeyName": { "Ref": "KeyName" },
    "SecurityGroups": [ { "Ref": "Ec2SecurityGroup" } ],
    "UserData": {
      "Fn::Base64": {
        "Fn::Join": [ ":", [
            "PORT=80",
            "TOPIC=",
            { "Ref": "MySNSTopic" }
          ]
        ]
      }
    },
    "InstanceType": "`aa.size`",
    "AvailabilityZone": "`aa-example-1a`",
    "ImageId": "`ami-1234567890abcdef0`",
    "Volumes": [
      {
        "VolumeId": { "Ref": "MyVolumeResource" },
        "Device": "/dev/sdk"
      }
    ],
    "Tags": [ { "Key": "Name", "Value": "MyTag" } ]
  }
}
```



#### YAML



```
Ec2Instance:
  Type: AWS::EC2::Instance
  Properties:
    KeyName: !Ref KeyName
    SecurityGroups:
      - !Ref Ec2SecurityGroup
    UserData:
      Fn::Base64:
        Fn::Join:
          - ":"
          - - "PORT=80"
            - "TOPIC="
            - !Ref MySNSTopic
    InstanceType: `aa.size`
    AvailabilityZone: `aa-example-1a`
    ImageId: `ami-1234567890abcdef0`
    Volumes:
      - VolumeId: !Ref MyVolumeResource
        Device: "/dev/sdk"
    Tags:
      - Key: Name
        Value: MyTag
```


### Define DynamoDB table name in
 user data for Amazon EC2 instance launch


The following snippet creates an Amazon EC2 instance and defines a DynamoDB table name
 in the user data to pass to the instance at launch. It uses an [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html") resource. You can define parameters or dynamic
 values in the user data to pass an EC2 instance at launch. 


For more information about user data, see [Use instance
 metadata to manage your EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html") in the
 *Amazon EC2 User Guide*.



#### JSON



```
"Ec2Instance": {
    "Type": "AWS::EC2::Instance",
    "Properties": {
        "UserData": {
            "Fn::Base64": {
                "Fn::Join": [
                    "",
                    [
                        "TableName=",
                        {
                            "Ref": "DynamoDBTableName"
                        }
                    ]
                ]
            }
        },
        "AvailabilityZone": "`aa-example-1a`",
        "ImageId": "`ami-1234567890abcdef0`"
    }
}
```



#### YAML



```
Ec2Instance:
  Type: AWS::EC2::Instance
  Properties:
    UserData:
      Fn::Base64:
        Fn::Join:
          - ''
          - - 'TableName='
            - Ref: DynamoDBTableName
    AvailabilityZone: `aa-example-1a`
    ImageId: `ami-1234567890abcdef0`
```


### Create an Amazon EBS volume with
 `DeletionPolicy`


The following snippets create an Amazon EBS volume using an Amazon EC2 [AWS::EC2::Volume](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-volume.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-volume.html") resource. You can use the `Size` or
 `SnapshotID` properties to define the volume, but not both. A
 `DeletionPolicy` attribute is set to create a snapshot of the
 volume when the stack is deleted. 


For more information about the `DeletionPolicy` attribute, see
 [DeletionPolicy attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-deletionpolicy.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-deletionpolicy.html").


For more information about creating Amazon EBS volumes, see [Create an Amazon EBS volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-creating-volume.html "https://docs.aws.amazon.com/ebs/latest/userguide/ebs-creating-volume.html").



#### JSON


This snippet creates an Amazon EBS volume with a specified **size**. The size is set to 10, but you can adjust
 it as needed. The [AWS::EC2::Volume](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-volume.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-volume.html")
 resource allows you to specify either the size or a snapshot ID but not
 both.



```
"MyEBSVolume": {
    "Type": "AWS::EC2::Volume",
    "Properties": {
        "Size": "`10`",
        "AvailabilityZone": {
            "Ref": "AvailabilityZone"
        }
    },
    "DeletionPolicy": "Snapshot"
}
```


This snippet creates an Amazon EBS volume using a provided **snapshot ID**. The [AWS::EC2::Volume](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-volume.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-volume.html")
 resource allows you to specify either the size or a snapshot ID but not
 both.



```
"MyEBSVolume": {
    "Type": "AWS::EC2::Volume",
    "Properties": {
        "SnapshotId" : "`snap-1234567890abcdef0`",
        "AvailabilityZone": {
            "Ref": "AvailabilityZone"
        }
    },
    "DeletionPolicy": "Snapshot"
}
```


#### YAML


This snippet creates an Amazon EBS volume with a specified **size**. The size is set to 10, but you can adjust
 it as needed. The [AWS::EC2::Volume](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-volume.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-volume.html")
 resource allows you to specify either the size or a snapshot ID but not
 both.



```
MyEBSVolume:
  Type: AWS::EC2::Volume
  Properties:
    Size: `10`
    AvailabilityZone:
      Ref: AvailabilityZone
  DeletionPolicy: Snapshot
```

This snippet creates an Amazon EBS volume using a provided **snapshot ID**. The [AWS::EC2::Volume](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-volume.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-volume.html")
 resource allows you to specify either the size or a snapshot ID but not
 both.



```
MyEBSVolume:
  Type: AWS::EC2::Volume
  Properties:
    SnapshotId: `snap-1234567890abcdef0`
    AvailabilityZone:
      Ref: AvailabilityZone
  DeletionPolicy: Snapshot
```


## Specify the block device mappings for an
 instance


A block device mapping defines the block devices, which includes instance store
 volumes and EBS volumes, to attach to an instance. You can specify a block device
 mapping when creating an AMI so that the mapping is used by all instances launched
 from the AMI. Alternatively, you can specify a block device mapping when you launch
 an instance, so that the mapping overrides the one specified in the AMI from which
 the instance was launched.


You can use the following template snippets to specify the block device mappings
 for your EBS or instance store volumes using the `BlockDeviceMappings`
 property of an [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html")
 resource. 


For more information about block device mappings, see [Block device
 mappings for volumes on Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html") in the
 *Amazon EC2 User Guide*.


###### Scenarios

* [Specify the block device mappings for two EBS volumes](#w71aac11c39c43c13b9c11 "#w71aac11c39c43c13b9c11")
* [Specify the block device mapping for an instance store volume](#w71aac11c39c43c13b9c13 "#w71aac11c39c43c13b9c13")

### Specify the block device mappings for two EBS volumes



#### JSON



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
          "DeviceName": "`/dev/sda1`",
          "Ebs": { "VolumeSize": "`50`" }
        },
        {
          "DeviceName": "`/dev/sdm`",
          "Ebs": { "VolumeSize": "`100`" }
        }
      ]
    }
  }
}
```



#### YAML



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
          DeviceName: `/dev/sda1`
          Ebs:
            VolumeSize: `50`
        -
          DeviceName: `/dev/sdm`
          Ebs:
            VolumeSize: `100`
```


### Specify the block device mapping for an instance store volume



#### JSON



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
        "DeviceName"  : "`/dev/sdc`",
        "VirtualName" : "`ephemeral0`"
      }
    ]
  }
}
```



#### YAML



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
      - DeviceName: `/dev/sdc`
        VirtualName: `ephemeral0`
```
