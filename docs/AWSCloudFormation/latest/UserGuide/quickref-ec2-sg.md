# Manage security groups with CloudFormation

The following snippets demonstrate how to use CloudFormation to manage security groups and
 Amazon EC2 instances to control access to your AWS resources.

###### Snippet categories

* [Associate an Amazon EC2
 instance with a security group](#quickref-ec2-instances-associate-security-group "#quickref-ec2-instances-associate-security-group")
* [Create security groups with ingress
 rules](#quickref-ec2-instances-ingress "#quickref-ec2-instances-ingress")
* [Create an Elastic Load
 Balancer with a security group ingress rule](#scenario-ec2-security-group-elbingress "#scenario-ec2-security-group-elbingress")

## Associate an Amazon EC2
 instance with a security group


The following example snippets demonstrate how to associate an Amazon EC2 instance with
 a default Amazon VPC security group using CloudFormation.


###### Example snippets

* [Associate an Amazon EC2 instance
 with a default VPC security group](#using-cfn-getatt-default-values "#using-cfn-getatt-default-values")
* [Create an Amazon EC2 instance with an
 attached volume and security group](#scenario-ec2-volumeattachment "#scenario-ec2-volumeattachment")

### Associate an Amazon EC2 instance
 with a default VPC security group


The following snippet creates an Amazon VPC, a subnet within the VPC, and an Amazon EC2
 instance. The VPC is created using an [AWS::EC2::VPC](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpc.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpc.html") resource.
 The IP address range for the VPC is defined in the larger template and is
 referenced by the `MyVPCCIDRRange` parameter.


A subnet is created within the VPC using an [AWS::EC2:: Subnet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-subnet.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-subnet.html")
 resource. The subnet is associated with the VPC, which is referenced as
 `MyVPC`.


An EC2 instance is launched within the VPC and subnet using an [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html") resource. This resource specifies the Amazon
 Machine Image (AMI) to use to launch the instance, the subnet where the instance
 will run, and the security group to associate with the instance. The
 `Fn::FindInMap` function is used to retrieve values from the
 `AWSRegionToAMI` mapping defined in the template to determine the
 `ImageId` for the [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html")
 resource. 


The security group ID is obtained using the `Fn::GetAtt` function,
 which retrieves the default security group from the `MyVPC` resource. 


The instance is placed within the `MySubnet` resource defined in
 the snippet. 


When you create a VPC using CloudFormation, AWS automatically creates default
 resources within the VPC, including a default security group. However, when you
 define a VPC within a CloudFormation template, you may not have access to the IDs of
 these default resources when you create the template. To access and use the
 default resources specified in the template, you can use intrinsic functions
 such as `Fn::GetAtt`. This function allows you to work with the
 default resources that are automatically created by CloudFormation.



#### JSON



```
"MyVPC": {
    "Type": "AWS::EC2::VPC",
    "Properties": {
        "CidrBlock": {
            "Ref": "MyVPCCIDRRange"
        },
        "EnableDnsSupport": false,
        "EnableDnsHostnames": false,
        "InstanceTenancy": "default"
    }
},
"MySubnet": {
    "Type": "AWS::EC2::Subnet",
    "Properties": {
        "CidrBlock": {
            "Ref": "MyVPCCIDRRange"
        },
        "VpcId": {
            "Ref": "MyVPC"
        }
    }
},
"MyInstance": {
    "Type": "AWS::EC2::Instance",
    "Properties": {
        "ImageId": {
            "Fn::FindInMap": [
                "AWSRegionToAMI",
                {
                    "Ref": "AWS::Region"
                },
                "64"
            ]
        },
        "SecurityGroupIds": [
            {
                "Fn::GetAtt": [
                    "MyVPC",
                    "DefaultSecurityGroup"
                ]
            }
        ],
        "SubnetId": {
            "Ref": "MySubnet"
        }
    }
}
```



#### YAML



```
MyVPC:
  Type: AWS::EC2::VPC
  Properties:
    CidrBlock:
      Ref: MyVPCCIDRRange
    EnableDnsSupport: false
    EnableDnsHostnames: false
    InstanceTenancy: default
MySubnet:
  Type: AWS::EC2::Subnet
  Properties:
    CidrBlock:
      Ref: MyVPCCIDRRange
    VpcId:
      Ref: MyVPC
MyInstance:
  Type: AWS::EC2::Instance
  Properties:
    ImageId:
      Fn::FindInMap:
        - AWSRegionToAMI
        - Ref: AWS::Region
        - "64"
    SecurityGroupIds:
      - Fn::GetAtt:
          - MyVPC
          - DefaultSecurityGroup
    SubnetId:
      Ref: MySubnet
```


### Create an Amazon EC2 instance with an
 attached volume and security group


The following snippet creates an Amazon EC2 instance using an [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html") resource, which is launched from a designated
 AMI . The instance is associated with a security group that allows incoming SSH
 traffic on port 22 from a specified IP address, using an [AWS::EC2::SecurityGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroup.html") resource . It creates a 100 GB Amazon EBS volume
 using an [AWS::EC2::Volume](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-volume.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-volume.html")
 resource. The volume is created in the same availability zone as the instance,
 as specified by the `GetAtt` function, and is mounted to the instance
 at the `/dev/sdh` device.


For more information about creating Amazon EBS volumes, see [Create an Amazon EBS volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-creating-volume.html "https://docs.aws.amazon.com/ebs/latest/userguide/ebs-creating-volume.html").



#### JSON



```
"Ec2Instance": {
    "Type": "AWS::EC2::Instance",
    "Properties": {
        "SecurityGroups": [
            {
                "Ref": "InstanceSecurityGroup"
            }
        ],
        "ImageId": "`ami-1234567890abcdef0`"
    }
},
"InstanceSecurityGroup": {
    "Type": "AWS::EC2::SecurityGroup",
    "Properties": {
        "GroupDescription": "Enable SSH access via port 22",
        "SecurityGroupIngress": [
            {
                "IpProtocol": "tcp",
                "FromPort": "22",
                "ToPort": "22",
                "CidrIp": "`192.0.2.0/24`"
            }
        ]
    }
},
"NewVolume": {
    "Type": "AWS::EC2::Volume",
    "Properties": {
        "Size": "100",
        "AvailabilityZone": {
            "Fn::GetAtt": [
                "Ec2Instance",
                "AvailabilityZone"
            ]
        }
    }
},
"MountPoint": {
    "Type": "AWS::EC2::VolumeAttachment",
    "Properties": {
        "InstanceId": {
            "Ref": "Ec2Instance"
        },
        "VolumeId": {
            "Ref": "NewVolume"
        },
        "Device": "/dev/sdh"
    }
}
```



#### YAML



```
Ec2Instance:
  Type: AWS::EC2::Instance
  Properties:
    SecurityGroups:
      - !Ref InstanceSecurityGroup
    ImageId: `ami-1234567890abcdef0`
InstanceSecurityGroup:
  Type: AWS::EC2::SecurityGroup
  Properties:
    GroupDescription: Enable SSH access via port 22
    SecurityGroupIngress:
      - IpProtocol: tcp
        FromPort: 22
        ToPort: 22
        CidrIp: `192.0.2.0/24`
NewVolume:
  Type: AWS::EC2::Volume
  Properties:
    Size: 100
    AvailabilityZone: !GetAtt [Ec2Instance, AvailabilityZone]
MountPoint:
  Type: AWS::EC2::VolumeAttachment
  Properties:
    InstanceId: !Ref Ec2Instance
    VolumeId: !Ref NewVolume
    Device: /dev/sdh
```


## Create security groups with ingress
 rules


The following example snippets demonstrate how to configure security groups with
 specific ingress rules using CloudFormation.


###### Snippets

* [Create security group with
 ingress rules for SSH and HTTP access](#scenario-ec2-security-group-rule "#scenario-ec2-security-group-rule")
* [Create a security group
 with ingress rules for HTTP and SSH access from specified CIDR
 ranges](#scenario-ec2-security-group-two-ports "#scenario-ec2-security-group-two-ports")
* [Create cross-referencing
 security groups with ingress rules](#scenario-ec2-security-group-ingress "#scenario-ec2-security-group-ingress")

### Create security group with
 ingress rules for SSH and HTTP access


The following snippet describes two security group ingress rules using an
 [AWS::EC2::SecurityGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroup.html") resource. The first ingress rule allows SSH
 (port 22) access from an existing security group named
 `MyAdminSecurityGroup`, which is owned by the AWS account with
 the account number `1111-2222-3333`. The second ingress rule allows
 HTTP (port 80) access from a different security group named
 `MySecurityGroupCreatedInCFN`, which is created in the same
 template. The `Ref` function is used to reference the logical name of
 the security group created in the same template. 


In the first ingress rule, you must add a value for both the
 `SourceSecurityGroupName` and
 `SourceSecurityGroupOwnerId` properties. In the second ingress
 rule, `MySecurityGroupCreatedInCFNTemplate` references a different
 security group, which is created in the same template. Verify that the logical
 name `MySecurityGroupCreatedInCFNTemplate` matches the actual logical
 name of the security group resource that you specify in the larger template. 


For more information about security groups, see [Amazon EC2 security groups
 for your Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html") in the
 *Amazon EC2 User Guide*.



#### JSON



```
"SecurityGroup": {
    "Type": "AWS::EC2::SecurityGroup",
    "Properties": {
        "GroupDescription": "Allow connections from specified source security group",
        "SecurityGroupIngress": [
            {
                "IpProtocol": "tcp",
                "FromPort": "22",
                "ToPort": "22",
                "SourceSecurityGroupName": "MyAdminSecurityGroup",
                "SourceSecurityGroupOwnerId": "`1111-2222-3333`"
            },
            {
                "IpProtocol": "tcp",
                "FromPort": "80",
                "ToPort": "80",
                "SourceSecurityGroupName": {
                    "Ref": "MySecurityGroupCreatedInCFNTemplate"
                }
            }
        ]
    }
}
```



#### YAML



```
SecurityGroup:
  Type: 'AWS::EC2::SecurityGroup'
  Properties:
    GroupDescription: Allow connections from specified source security group
    SecurityGroupIngress:
      - IpProtocol: tcp
        FromPort: '22'
        ToPort: '22'
        SourceSecurityGroupName: MyAdminSecurityGroup
        SourceSecurityGroupOwnerId: '`1111-2222-3333`'
      - IpProtocol: tcp
        FromPort: '80'
        ToPort: '80'
        SourceSecurityGroupName:
          Ref: MySecurityGroupCreatedInCFNTemplate
```


### Create a security group
 with ingress rules for HTTP and SSH access from specified CIDR
 ranges


The following snippet creates a security group for an Amazon EC2 instance with two
 inbound rules. The inbound rules allow incoming TCP traffic on the specified
 ports from the designated CIDR ranges. An [AWS::EC2::SecurityGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroup.html") resource is used to specify the rules. You
 must specify a protocol for each rule. For TCP, you must specify a port or port
 range. If you do not specify either a source security group or a CIDR range, the
 stack will launch successfully, but the rule will not be applied to the security
 group. 


For more information about security groups, see [Amazon EC2 security groups
 for your Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html") in the
 *Amazon EC2 User Guide*.



#### JSON



```
"ServerSecurityGroup": {
  "Type": "AWS::EC2::SecurityGroup",
  "Properties": {
    "GroupDescription": "Allow connections from specified CIDR ranges",
    "SecurityGroupIngress": [
      {
        "IpProtocol": "tcp",
        "FromPort": "80",
        "ToPort": "80",
        "CidrIp": "`192.0.2.0/24`"
      },
      {
        "IpProtocol": "tcp",
        "FromPort": "22",
        "ToPort": "22",
        "CidrIp": "`192.0.2.0/24`"
      }
    ]
  }
}
```



#### YAML



```
ServerSecurityGroup:
  Type: AWS::EC2::SecurityGroup
  Properties:
    GroupDescription: Allow connections from specified CIDR ranges
    SecurityGroupIngress:
      - IpProtocol: tcp
        FromPort: 80
        ToPort: 80
        CidrIp: `192.0.2.0/24`
      - IpProtocol: tcp
        FromPort: 22
        ToPort: 22
        CidrIp: `192.0.2.0/24`
```


### Create cross-referencing
 security groups with ingress rules


The following snippet uses the [AWS::EC2::SecurityGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroup.html") resource to create two Amazon EC2 security
 groups, `SGroup1` and `SGroup2`. Ingress rules that allow
 communication between the two security groups are created by using the [AWS::EC2::SecurityGroupIngress](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroupingress.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroupingress.html") resource.
 `SGroup1Ingress` establishes an ingress rule for
 `SGroup1` that allows incoming TCP traffic on port 80 from the
 source security group, `SGroup2`. `SGroup2Ingress`
 establishes an ingress rule for `SGroup2` that allows incoming TCP
 traffic on port 80 from the source security group, `SGroup1`. 



#### JSON



```
"SGroup1": {
    "Type": "AWS::EC2::SecurityGroup",
    "Properties": {
        "GroupDescription": "EC2 instance access"
    }
},
"SGroup2": {
    "Type": "AWS::EC2::SecurityGroup",
    "Properties": {
        "GroupDescription": "EC2 instance access"
    }
},
"SGroup1Ingress": {
    "Type": "AWS::EC2::SecurityGroupIngress",
    "Properties": {
        "GroupName": {
            "Ref": "SGroup1"
        },
        "IpProtocol": "tcp",
        "ToPort": "80",
        "FromPort": "80",
        "SourceSecurityGroupName": {
            "Ref": "SGroup2"
        }
    }
},
"SGroup2Ingress": {
    "Type": "AWS::EC2::SecurityGroupIngress",
    "Properties": {
        "GroupName": {
            "Ref": "SGroup2"
        },
        "IpProtocol": "tcp",
        "ToPort": "80",
        "FromPort": "80",
        "SourceSecurityGroupName": {
            "Ref": "SGroup1"
        }
    }
}
```



#### YAML



```
SGroup1:
  Type: AWS::EC2::SecurityGroup
  Properties:
    GroupDescription: EC2 Instance access
SGroup2:
  Type: AWS::EC2::SecurityGroup
  Properties:
    GroupDescription: EC2 Instance access
SGroup1Ingress:
  Type: AWS::EC2::SecurityGroupIngress
  Properties:
    GroupName: !Ref SGroup1
    IpProtocol: tcp
    ToPort: 80
    FromPort: 80
    SourceSecurityGroupName: !Ref SGroup2
SGroup2Ingress:
  Type: AWS::EC2::SecurityGroupIngress
  Properties:
    GroupName: !Ref SGroup2
    IpProtocol: tcp
    ToPort: 80
    FromPort: 80
    SourceSecurityGroupName: !Ref SGroup1
```


## Create an Elastic Load
 Balancer with a security group ingress rule


The following template creates an [AWS::ElasticLoadBalancing::LoadBalancer](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancing-loadbalancer.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancing-loadbalancer.html") resource in the specified
 availability zone. The [AWS::ElasticLoadBalancing::LoadBalancer](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancing-loadbalancer.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancing-loadbalancer.html") resource is configured to
 listen on port 80 for HTTP traffic and direct requests to instances also on port 80.
 The Elastic Load Balancer is responsible for load balancing incoming HTTP traffic
 among the instances.


 Additionally, this template generates an [AWS::EC2::SecurityGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroup.html") resource associated with the load balancer.
 This security group is created with a single ingress rule, described as `ELB
 ingress group`, which allows incoming TCP traffic on port 80. The source
 for this ingress rule is defined using the `Fn::GetAtt` fucntion to
 retrieve attributes from the load balancer resource.
 `SourceSecurityGroupOwnerId` uses `Fn::GetAtt` to obtain
 the `OwnerAlias` of the source security group of the load balancer.
 `SourceSecurityGroupName` uses `Fn::Getatt` to obtain the
 `GroupName` of the source security group of the ELB. 


This setup ensures secure communication between the ELB and the instances. 


For more information about load balancing, see the [Elastic Load Balancing User Guide](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/ "https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/").



### JSON



```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "MyELB": {
            "Type": "AWS::ElasticLoadBalancing::LoadBalancer",
            "Properties": {
                "AvailabilityZones": [
                    "`aa-example-1a`"
                ],
                "Listeners": [
                    {
                        "LoadBalancerPort": "80",
                        "InstancePort": "80",
                        "Protocol": "HTTP"
                    }
                ]
            }
        },
        "MyELBIngressGroup": {
            "Type": "AWS::EC2::SecurityGroup",
            "Properties": {
                "GroupDescription": "ELB ingress group",
                "SecurityGroupIngress": [
                    {
                        "IpProtocol": "tcp",
                        "FromPort": 80,
                        "ToPort": 80,
                        "SourceSecurityGroupOwnerId": {
                            "Fn::GetAtt": [
                                "MyELB",
                                "SourceSecurityGroup.OwnerAlias"
                            ]
                        },
                        "SourceSecurityGroupName": {
                            "Fn::GetAtt": [
                                "MyELB",
                                "SourceSecurityGroup.GroupName"
                            ]
                        }
                    }
                ]
            }
        }
    }
}
```



### YAML



```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  MyELB:
    Type: 'AWS::ElasticLoadBalancing::LoadBalancer'
    Properties:
      AvailabilityZones:
        - `aa-example-1a`
      Listeners:
        - LoadBalancerPort: '80'
          InstancePort: '80'
          Protocol: HTTP
  MyELBIngressGroup:
    Type: 'AWS::EC2::SecurityGroup'
    Properties:
      GroupDescription: ELB ingress group
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: '80'
          ToPort: '80'
          SourceSecurityGroupOwnerId:
            Fn::GetAtt:
              - MyELB
              - SourceSecurityGroup.OwnerAlias
          SourceSecurityGroupName:
            Fn::GetAtt:
              - MyELB
              - SourceSecurityGroup.GroupName
```
