

# Manage security groups with CloudFormation
<a name="quickref-ec2-sg"></a>

The following snippets demonstrate how to use CloudFormation to manage security groups and Amazon EC2 instances to control access to your AWS resources.

**Topics**
+ [Associate an Amazon EC2 instance with a security group](#quickref-ec2-instances-associate-security-group)
+ [Create security groups with ingress rules](#quickref-ec2-instances-ingress)
+ [Create an Elastic Load Balancer with a security group ingress rule](#scenario-ec2-security-group-elbingress)

## Associate an Amazon EC2 instance with a security group
<a name="quickref-ec2-instances-associate-security-group"></a>

The following example snippets demonstrate how to associate an Amazon EC2 instance with a default Amazon VPC security group using CloudFormation.

**Topics**
+ [Associate an Amazon EC2 instance with a default VPC security group](#using-cfn-getatt-default-values)
+ [Create an Amazon EC2 instance with an attached volume and security group](#scenario-ec2-volumeattachment)

### Associate an Amazon EC2 instance with a default VPC security group
<a name="using-cfn-getatt-default-values"></a>

The following snippet creates an Amazon VPC, a subnet within the VPC, and an Amazon EC2 instance. The VPC is created using an [AWS::EC2::VPC](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpc.html) resource. The IP address range for the VPC is defined in the larger template and is referenced by the `MyVPCCIDRRange` parameter.

A subnet is created within the VPC using an [AWS::EC2:: Subnet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-subnet.html) resource. The subnet is associated with the VPC, which is referenced as `MyVPC`.

An EC2 instance is launched within the VPC and subnet using an [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html) resource. This resource specifies the Amazon Machine Image (AMI) to use to launch the instance, the subnet where the instance will run, and the security group to associate with the instance. The `ImageId` uses a Systems Manager parameter to dynamically retrieve the latest Amazon Linux 2 AMI. 

The security group ID is obtained using the `Fn::GetAtt` function, which retrieves the default security group from the `MyVPC` resource. 

The instance is placed within the `MySubnet` resource defined in the snippet. 

When you create a VPC using CloudFormation, AWS automatically creates default resources within the VPC, including a default security group. However, when you define a VPC within a CloudFormation template, you may not have access to the IDs of these default resources when you create the template. To access and use the default resources specified in the template, you can use intrinsic functions such as `Fn::GetAtt`. This function allows you to work with the default resources that are automatically created by CloudFormation.

#### JSON
<a name="quickref-ec2-example-15.json"></a>

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
        "ImageId": "{{resolve:ssm:/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2}}",
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
<a name="quickref-ec2-example-15.yaml"></a>

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
    ImageId: '{{resolve:ssm:/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2}}'
    SecurityGroupIds:
      - Fn::GetAtt:
          - MyVPC
          - DefaultSecurityGroup
    SubnetId:
      Ref: MySubnet
```

### Create an Amazon EC2 instance with an attached volume and security group
<a name="scenario-ec2-volumeattachment"></a>

The following snippet creates an Amazon EC2 instance using an [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html) resource, which is launched from a designated AMI . The instance is associated with a security group that allows incoming SSH traffic on port 22 from a specified IP address, using an [AWS::EC2::SecurityGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroup.html) resource . It creates a 100 GB Amazon EBS volume using an [AWS::EC2::Volume](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-volume.html) resource. The volume is created in the same availability zone as the instance, as specified by the `GetAtt` function, and is mounted to the instance at the `/dev/sdh` device.

For more information about creating Amazon EBS volumes, see [Create an Amazon EBS volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-creating-volume.html).

#### JSON
<a name="quickref-ec2-example-14.json"></a>

```
 1. "Ec2Instance": {
 2.     "Type": "AWS::EC2::Instance",
 3.     "Properties": {
 4.         "SecurityGroups": [
 5.             {
 6.                 "Ref": "InstanceSecurityGroup"
 7.             }
 8.         ],
 9.         "ImageId": "{{ami-1234567890abcdef0}}"
10.     }
11. },
12. "InstanceSecurityGroup": {
13.     "Type": "AWS::EC2::SecurityGroup",
14.     "Properties": {
15.         "GroupDescription": "Enable SSH access via port 22",
16.         "SecurityGroupIngress": [
17.             {
18.                 "IpProtocol": "tcp",
19.                 "FromPort": "22",
20.                 "ToPort": "22",
21.                 "CidrIp": "{{192.0.2.0/24}}"
22.             }
23.         ]
24.     }
25. },
26. "NewVolume": {
27.     "Type": "AWS::EC2::Volume",
28.     "Properties": {
29.         "Size": "100",
30.         "AvailabilityZone": {
31.             "Fn::GetAtt": [
32.                 "Ec2Instance",
33.                 "AvailabilityZone"
34.             ]
35.         }
36.     }
37. },
38. "MountPoint": {
39.     "Type": "AWS::EC2::VolumeAttachment",
40.     "Properties": {
41.         "InstanceId": {
42.             "Ref": "Ec2Instance"
43.         },
44.         "VolumeId": {
45.             "Ref": "NewVolume"
46.         },
47.         "Device": "/dev/sdh"
48.     }
49. }
```

#### YAML
<a name="quickref-ec2-example-14.yaml"></a>

```
 1. Ec2Instance:
 2.   Type: AWS::EC2::Instance
 3.   Properties:
 4.     SecurityGroups:
 5.       - !Ref InstanceSecurityGroup
 6.     ImageId: {{ami-1234567890abcdef0}}
 7. InstanceSecurityGroup:
 8.   Type: AWS::EC2::SecurityGroup
 9.   Properties:
10.     GroupDescription: Enable SSH access via port 22
11.     SecurityGroupIngress:
12.       - IpProtocol: tcp
13.         FromPort: 22
14.         ToPort: 22
15.         CidrIp: {{192.0.2.0/24}}
16. NewVolume:
17.   Type: AWS::EC2::Volume
18.   Properties:
19.     Size: 100
20.     AvailabilityZone: !GetAtt [Ec2Instance, AvailabilityZone]
21. MountPoint:
22.   Type: AWS::EC2::VolumeAttachment
23.   Properties:
24.     InstanceId: !Ref Ec2Instance
25.     VolumeId: !Ref NewVolume
26.     Device: /dev/sdh
```

## Create security groups with ingress rules
<a name="quickref-ec2-instances-ingress"></a>

The following example snippets demonstrate how to configure security groups with specific ingress rules using CloudFormation.

**Topics**
+ [Create security group with ingress rules for SSH and HTTP access](#scenario-ec2-security-group-rule)
+ [Create a security group with ingress rules for HTTP and SSH access from specified CIDR ranges](#scenario-ec2-security-group-two-ports)
+ [Create cross-referencing security groups with ingress rules](#scenario-ec2-security-group-ingress)

### Create security group with ingress rules for SSH and HTTP access
<a name="scenario-ec2-security-group-rule"></a>

The following snippet describes two security group ingress rules using an [AWS::EC2::SecurityGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroup.html) resource. The first ingress rule allows SSH (port 22) access from an existing security group named `MyAdminSecurityGroup`, which is owned by the AWS account with the account number `1111-2222-3333`. The second ingress rule allows HTTP (port 80) access from a different security group named `MySecurityGroupCreatedInCFN`, which is created in the same template. The `Ref` function is used to reference the logical name of the security group created in the same template. 

In the first ingress rule, you must add a value for both the `SourceSecurityGroupName` and `SourceSecurityGroupOwnerId` properties. In the second ingress rule, `MySecurityGroupCreatedInCFNTemplate` references a different security group, which is created in the same template. Verify that the logical name `MySecurityGroupCreatedInCFNTemplate` matches the actual logical name of the security group resource that you specify in the larger template. 

For more information about security groups, see [Amazon EC2 security groups for your Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html) in the *Amazon EC2 User Guide*.

#### JSON
<a name="quickref-ec2-example-10.json"></a>

```
 1. "SecurityGroup": {
 2.     "Type": "AWS::EC2::SecurityGroup",
 3.     "Properties": {
 4.         "GroupDescription": "Allow connections from specified source security group",
 5.         "SecurityGroupIngress": [
 6.             {
 7.                 "IpProtocol": "tcp",
 8.                 "FromPort": "22",
 9.                 "ToPort": "22",
10.                 "SourceSecurityGroupName": "MyAdminSecurityGroup",
11.                 "SourceSecurityGroupOwnerId": "{{1111-2222-3333}}"
12.             },
13.             {
14.                 "IpProtocol": "tcp",
15.                 "FromPort": "80",
16.                 "ToPort": "80",
17.                 "SourceSecurityGroupName": {
18.                     "Ref": "MySecurityGroupCreatedInCFNTemplate"
19.                 }
20.             }
21.         ]
22.     }
23. }
```

#### YAML
<a name="quickref-ec2-example-10.yaml"></a>

```
 1. SecurityGroup:
 2.   Type: AWS::EC2::SecurityGroup
 3.   Properties:
 4.     GroupDescription: Allow connections from specified source security group
 5.     SecurityGroupIngress:
 6.       - IpProtocol: tcp
 7.         FromPort: '22'
 8.         ToPort: '22'
 9.         SourceSecurityGroupName: MyAdminSecurityGroup
10.         SourceSecurityGroupOwnerId: '{{1111-2222-3333}}'
11.       - IpProtocol: tcp
12.         FromPort: '80'
13.         ToPort: '80'
14.         SourceSecurityGroupName:
15.           Ref: MySecurityGroupCreatedInCFNTemplate
```

### Create a security group with ingress rules for HTTP and SSH access from specified CIDR ranges
<a name="scenario-ec2-security-group-two-ports"></a>

The following snippet creates a security group for an Amazon EC2 instance with two inbound rules. The inbound rules allow incoming TCP traffic on the specified ports from the designated CIDR ranges. An [AWS::EC2::SecurityGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroup.html) resource is used to specify the rules. You must specify a protocol for each rule. For TCP, you must specify a port or port range. If you do not specify either a source security group or a CIDR range, the stack will launch successfully, but the rule will not be applied to the security group. 

For more information about security groups, see [Amazon EC2 security groups for your Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html) in the *Amazon EC2 User Guide*.

#### JSON
<a name="quickref-ec2-example-9.json"></a>

```
 1. "ServerSecurityGroup": {
 2.   "Type": "AWS::EC2::SecurityGroup",
 3.   "Properties": {
 4.     "GroupDescription": "Allow connections from specified CIDR ranges",
 5.     "SecurityGroupIngress": [
 6.       {
 7.         "IpProtocol": "tcp",
 8.         "FromPort": "80",
 9.         "ToPort": "80",
10.         "CidrIp": "{{192.0.2.0/24}}"
11.       },
12.       {
13.         "IpProtocol": "tcp",
14.         "FromPort": "22",
15.         "ToPort": "22",
16.         "CidrIp": "{{192.0.2.0/24}}"
17.       }
18.     ]
19.   }
20. }
```

#### YAML
<a name="quickref-ec2-example-9.yaml"></a>

```
 1. ServerSecurityGroup:
 2.   Type: AWS::EC2::SecurityGroup
 3.   Properties:
 4.     GroupDescription: Allow connections from specified CIDR ranges
 5.     SecurityGroupIngress:
 6.       - IpProtocol: tcp
 7.         FromPort: 80
 8.         ToPort: 80
 9.         CidrIp: {{192.0.2.0/24}}
10.       - IpProtocol: tcp
11.         FromPort: 22
12.         ToPort: 22
13.         CidrIp: {{192.0.2.0/24}}
```

### Create cross-referencing security groups with ingress rules
<a name="scenario-ec2-security-group-ingress"></a>

The following snippet uses the [AWS::EC2::SecurityGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroup.html) resource to create two Amazon EC2 security groups, `SGroup1` and `SGroup2`. Ingress rules that allow communication between the two security groups are created by using the [AWS::EC2::SecurityGroupIngress](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroupingress.html) resource. `SGroup1Ingress` establishes an ingress rule for `SGroup1` that allows incoming TCP traffic on port 80 from the source security group, `SGroup2`. `SGroup2Ingress` establishes an ingress rule for `SGroup2` that allows incoming TCP traffic on port 80 from the source security group, `SGroup1`. 

#### JSON
<a name="quickref-ec2-example-12.json"></a>

```
 1. "SGroup1": {
 2.     "Type": "AWS::EC2::SecurityGroup",
 3.     "Properties": {
 4.         "GroupDescription": "EC2 instance access"
 5.     }
 6. },
 7. "SGroup2": {
 8.     "Type": "AWS::EC2::SecurityGroup",
 9.     "Properties": {
10.         "GroupDescription": "EC2 instance access"
11.     }
12. },
13. "SGroup1Ingress": {
14.     "Type": "AWS::EC2::SecurityGroupIngress",
15.     "Properties": {
16.         "GroupName": {
17.             "Ref": "SGroup1"
18.         },
19.         "IpProtocol": "tcp",
20.         "ToPort": "80",
21.         "FromPort": "80",
22.         "SourceSecurityGroupName": {
23.             "Ref": "SGroup2"
24.         }
25.     }
26. },
27. "SGroup2Ingress": {
28.     "Type": "AWS::EC2::SecurityGroupIngress",
29.     "Properties": {
30.         "GroupName": {
31.             "Ref": "SGroup2"
32.         },
33.         "IpProtocol": "tcp",
34.         "ToPort": "80",
35.         "FromPort": "80",
36.         "SourceSecurityGroupName": {
37.             "Ref": "SGroup1"
38.         }
39.     }
40. }
```

#### YAML
<a name="quickref-ec2-example-12.yaml"></a>

```
 1. SGroup1:
 2.   Type: AWS::EC2::SecurityGroup
 3.   Properties:
 4.     GroupDescription: EC2 Instance access
 5. SGroup2:
 6.   Type: AWS::EC2::SecurityGroup
 7.   Properties:
 8.     GroupDescription: EC2 Instance access
 9. SGroup1Ingress:
10.   Type: AWS::EC2::SecurityGroupIngress
11.   Properties:
12.     GroupName: !Ref SGroup1
13.     IpProtocol: tcp
14.     ToPort: 80
15.     FromPort: 80
16.     SourceSecurityGroupName: !Ref SGroup2
17. SGroup2Ingress:
18.   Type: AWS::EC2::SecurityGroupIngress
19.   Properties:
20.     GroupName: !Ref SGroup2
21.     IpProtocol: tcp
22.     ToPort: 80
23.     FromPort: 80
24.     SourceSecurityGroupName: !Ref SGroup1
```

## Create an Elastic Load Balancer with a security group ingress rule
<a name="scenario-ec2-security-group-elbingress"></a>

The following template creates an [AWS::ElasticLoadBalancing::LoadBalancer](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancing-loadbalancer.html) resource in the specified availability zone. The [AWS::ElasticLoadBalancing::LoadBalancer](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancing-loadbalancer.html) resource is configured to listen on port 80 for HTTP traffic and direct requests to instances also on port 80. The Elastic Load Balancer is responsible for load balancing incoming HTTP traffic among the instances.

 Additionally, this template generates an [AWS::EC2::SecurityGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroup.html) resource associated with the load balancer. This security group is created with a single ingress rule, described as `ELB ingress group`, which allows incoming TCP traffic on port 80. The source for this ingress rule is defined using the `Fn::GetAtt` fucntion to retrieve attributes from the load balancer resource. `SourceSecurityGroupOwnerId` uses `Fn::GetAtt` to obtain the `OwnerAlias` of the source security group of the load balancer. `SourceSecurityGroupName` uses `Fn::Getatt` to obtain the `GroupName` of the source security group of the ELB. 

This setup ensures secure communication between the ELB and the instances. 

For more information about load balancing, see the [Elastic Load Balancing User Guide](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/).

### JSON
<a name="quickref-ec2-example-11.json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "MyELB": {
            "Type": "AWS::ElasticLoadBalancing::LoadBalancer",
            "Properties": {
                "AvailabilityZones": [
                    "{{aa-example-1a}}"
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
<a name="quickref-ec2-example-11.yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  MyELB:
    Type: AWS::ElasticLoadBalancing::LoadBalancer
    Properties:
      AvailabilityZones:
        - {{aa-example-1a}}
      Listeners:
        - LoadBalancerPort: '80'
          InstancePort: '80'
          Protocol: HTTP
  MyELBIngressGroup:
    Type: AWS::EC2::SecurityGroup
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