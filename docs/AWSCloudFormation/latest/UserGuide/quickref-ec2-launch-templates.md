# Create launch templates with

CloudFormation

This section provides an example for creating an Amazon EC2 launch template using
CloudFormation. Launch templates allow you to create templates for configuring and
provisioning Amazon EC2 instances within AWS. With launch templates, you can store launch
parameters so that you do not have to specify them every time you launch an instance.
For more examples, see the [Examples](../TemplateReference/aws-resource-ec2-launchtemplate.md#aws-resource-ec2-launchtemplate--examples "../TemplateReference/aws-resource-ec2-launchtemplate.md#aws-resource-ec2-launchtemplate--examples") section in the `AWS::EC2::LaunchTemplate`
resource.

For more information about launch templates, see [Store instance launch
parameters in Amazon EC2 launch templates](../../../AWSEC2/latest/UserGuide/ec2-launch-templates.md "../../../AWSEC2/latest/UserGuide/ec2-launch-templates.md") in the
_Amazon EC2 User Guide_.

For information about creating launch templates for use with Auto Scaling groups, see [Auto Scaling
launch templates](../../../autoscaling/ec2/userguide/launch-templates.md "../../../autoscaling/ec2/userguide/launch-templates.md") in the _Amazon EC2 Auto Scaling User Guide_.

###### Snippet categories

- [Create a launch template that
  specifies security groups, tags, user data, and an IAM role](#scenario-as-launch-template "#scenario-as-launch-template")

## Create a launch template that

specifies security groups, tags, user data, and an IAM role

This snippet shows an [AWS::EC2::LaunchTemplate](../TemplateReference/aws-resource-ec2-launchtemplate.md "../TemplateReference/aws-resource-ec2-launchtemplate.md") resource that contains the configuration
information to launch an instance. You specify values for the `ImageId`,
`InstanceType`, `SecurityGroups`, `UserData`,
and `TagSpecifications` properties. The `SecurityGroups`
property specifies an existing EC2 security group and a new security group. The
`Ref` function gets the ID of the [AWS::EC2::SecurityGroup](../TemplateReference/aws-resource-ec2-securitygroup.md "../TemplateReference/aws-resource-ec2-securitygroup.md") resource `myNewEC2SecurityGroup`
that's declared elsewhere in the stack template.

The launch template includes a section for custom user data. You can pass in
configuration tasks and scripts that run when an instance launches in this section.
In this example, the user data installs the AWS Systems Manager Agent and starts the
agent.

The launch template also includes an IAM role that allows applications running
on instances to perform actions on your behalf. This example shows an [AWS::IAM::Role](../TemplateReference/aws-resource-iam-role.md "../TemplateReference/aws-resource-iam-role.md") resource for the launch template, which uses the
`IamInstanceProfile` property to specify the IAM role. The
`Ref` function gets the name of the [AWS::IAM::InstanceProfile](../TemplateReference/aws-resource-iam-instanceprofile.md "../TemplateReference/aws-resource-iam-instanceprofile.md") resource `myInstanceProfile`. To
configure the permissions of the IAM role, you specify a value for the
`ManagedPolicyArns` property.

### JSON

```
{
  "Resources":{
    "myLaunchTemplate":{
      "Type":"AWS::EC2::LaunchTemplate",
      "Properties":{
        "LaunchTemplateName":{ "Fn::Sub": "${AWS::StackName}-launch-template" },
        "LaunchTemplateData":{
          "ImageId":"`ami-02354e95b3example`",
          "InstanceType":"`t3.micro`",
          "IamInstanceProfile":{
            "Name":{
              "Ref":"myInstanceProfile"
            }
          },
          "SecurityGroupIds":[
            {
              "Ref":"`myNewEC2SecurityGroup`"
            },
            "`sg-083cd3bfb8example`"
          ],
          "UserData":{
            "Fn::Base64":{
              "Fn::Join": [
                "", [
                  "`#!/bin/bash\n`",
                  "`cd /tmp\n`",
                  "`yum install -y https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_amd64/amazon-ssm-agent.rpm\n`",
                  "`systemctl enable amazon-ssm-agent\n`",
                  "`systemctl start amazon-ssm-agent\n`"
                ]
              ]
            }
          },
          "TagSpecifications":[
            {
              "ResourceType":"instance",
              "Tags":[
                {
                  "Key":"`environment`",
                  "Value":"`development`"
                }
              ]
            },
            {
              "ResourceType":"volume",
              "Tags":[
                {
                  "Key":"`environment`",
                  "Value":"`development`"
                }
              ]
            }
          ]
        }
      }
    },
    "myInstanceRole":{
      "Type":"AWS::IAM::Role",
      "Properties":{
        "RoleName":"InstanceRole",
        "AssumeRolePolicyDocument":{
          "Version": "2012-10-17",
          "Statement":[
            {
              "Effect":"Allow",
              "Principal":{
                "Service":[
                  "ec2.amazonaws.com"
                ]
              },
              "Action":[
                "sts:AssumeRole"
              ]
            }
          ]
        },
        "ManagedPolicyArns":[
          "arn:aws:iam::aws:policy/`myCustomerManagedPolicy`"
        ]
      }
    },
    "myInstanceProfile":{
      "Type":"AWS::IAM::InstanceProfile",
      "Properties":{
        "Path":"/",
        "Roles":[
          {
            "Ref":"myInstanceRole"
          }
        ]
      }
    }
  }
}
```

### YAML

```
---
Resources:
  myLaunchTemplate:
    Type: AWS::EC2::LaunchTemplate
    Properties:
      LaunchTemplateName: !Sub ${AWS::StackName}-launch-template
      LaunchTemplateData:
        ImageId: `ami-02354e95b3example`
        InstanceType: `t3.micro`
        IamInstanceProfile:
          Name: !Ref myInstanceProfile
        SecurityGroupIds:
        - !Ref `myNewEC2SecurityGroup`
        - `sg-083cd3bfb8example`
        UserData:
          Fn::Base64: !Sub |
            `#!/bin/bash
 cd /tmp
 yum install -y https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_amd64/amazon-ssm-agent.rpm
 systemctl enable amazon-ssm-agent
 systemctl start amazon-ssm-agent`
        TagSpecifications:
        - ResourceType: instance
          Tags:
          - Key: `environment`
            Value: `development`
        - ResourceType: volume
          Tags:
          - Key: `environment`
            Value: `development`
  myInstanceRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: InstanceRole
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
        - Effect: 'Allow'
          Principal:
            Service:
            - 'ec2.amazonaws.com'
          Action:
          - 'sts:AssumeRole'
      ManagedPolicyArns:
        - 'arn:aws:iam::aws:policy/`myCustomerManagedPolicy`'
  myInstanceProfile:
    Type: AWS::IAM::InstanceProfile
    Properties:
      Path: '/'
      Roles:
      - !Ref myInstanceRole
```
