# Configure Amazon VPC resources with CloudFormation

This section provides examples for configuring Amazon VPC resources using CloudFormation. VPCs
 allow you to create a virtual network within AWS, and these snippets show how to
 configure aspects of VPCs to meet your networking requirements. 

###### Example snippets

* [Enable IPv6
 egress-only internet access in a VPC](#quickref-ec2-route-egressonlyinternetgateway "#quickref-ec2-route-egressonlyinternetgateway")
* [Elastic network interface (ENI) template
 snippets](#cfn-template-snippets-eni "#cfn-template-snippets-eni")

## Enable IPv6
 egress-only internet access in a VPC


An egress-only internet gateway allows instances within a VPC to access the
 internet and prevent resources on the internet from communicating with the
 instances. The following snippet enables IPv6 egress-only internet access from
 within a VPC. It creates a VPC with an IPv4 address range of `10.0.0/16`
 using an [AWS::EC2::VPC](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpc.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpc.html") resource. A route table is associated with this VPC
 resource using an [AWS::EC2::RouteTable](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-routetable.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-routetable.html")
 resource. The route table manages routes for instances within the VPC. An [AWS::EC2::EgressOnlyInternetGateway](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-egressonlyinternetgateway.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-egressonlyinternetgateway.html") is used to create an egress-only
 internet gateway to enable IPv6 communication for outbound traffic from instances
 within the VPC, while preventing inbound traffic. An [AWS::EC2::Route](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-route.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-route.html") resource is
 specified to create an IPv6 route in the route table that directs all outbound IPv6
 traffic (`::/0`) to the egress-only internet gateway. 


For more information about egress-only internet gateways, see [Enable outbound
 IPv6 traffic using an egress-only internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/egress-only-internet-gateway.html "https://docs.aws.amazon.com/vpc/latest/userguide/egress-only-internet-gateway.html") in the
 *Amazon VPC User Guide*.



### JSON



```
"DefaultIpv6Route": {
    "Type": "AWS::EC2::Route",
    "Properties": {
        "DestinationIpv6CidrBlock": "::/0",
        "EgressOnlyInternetGatewayId": {
            "Ref": "EgressOnlyInternetGateway"
        },
        "RouteTableId": {
            "Ref": "RouteTable"
        }
    }
},
"EgressOnlyInternetGateway": {
    "Type": "AWS::EC2::EgressOnlyInternetGateway",
    "Properties": {
        "VpcId": {
            "Ref": "VPC"
        }
    }
},
"RouteTable": {
    "Type": "AWS::EC2::RouteTable",
    "Properties": {
        "VpcId": {
            "Ref": "VPC"
        }
    }
},
"VPC": {
    "Type": "AWS::EC2::VPC",
    "Properties": {
        "CidrBlock": "10.0.0.0/16"
    }
}
```



### YAML



```
DefaultIpv6Route:
  Type: "AWS::EC2::Route"
  Properties:
    DestinationIpv6CidrBlock: "::/0"
    EgressOnlyInternetGatewayId:
      Ref: "EgressOnlyInternetGateway"
    RouteTableId:
      Ref: "RouteTable"
EgressOnlyInternetGateway:
  Type: "AWS::EC2::EgressOnlyInternetGateway"
  Properties:
    VpcId:
      Ref: "VPC"
RouteTable:
  Type: "AWS::EC2::RouteTable"
  Properties:
    VpcId:
      Ref: "VPC"
VPC:
  Type: "AWS::EC2::VPC"
  Properties:
    CidrBlock: "10.0.0.0/16"
```


## Elastic network interface (ENI) template
 snippets


### Create an Amazon EC2 instance with attached
 elastic network interfaces (ENIs)


The following example snippet creates an Amazon EC2 instance using an [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html") resource in the specified Amazon VPC and subnet. It attaches two
 network interfaces (ENIs) with the instance, associates Elastic IP addresses to the instances
 through the attached ENIs, and configures the security group for SSH and HTTP access. User
 data is supplied to the instance as part of the launch configuration when the instance is
 created. The user data includes a script encoded in `base64` format to ensure it is
 passed to the instance. When the instance is launched, the script runs automatically as part
 of the bootstrapping process. It installs `ec2-net-utils`, configures the network
 interfaces, and starts the HTTP service. 


To determine the appropriate Amazon Machine Image (AMI) based on the selected Region, the
 snippet uses a `Fn::FindInMap` function that looks up values in a
 `RegionMap` mapping. This mapping must be defined in the larger template. The
 two network interfaces are created using [AWS::EC2::NetworkInterface](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-networkinterface.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-networkinterface.html") resources. Elastic IP addresses are specified using
 [AWS::EC2::EIP](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-eip.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-eip.html")
 resources allocated to the `vpc` domain. These elastic IP addresses are associated
 with the network interfaces using [AWS::EC2::EIPAssociation](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-eipassociation.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-eipassociation.html") resources. 


The `Outputs` section defines values or resources that you want to access after
 the stack is created. In this snippet, the defined output is `InstancePublicIp`,
 which represents the public IP address of the EC2 instance created by the stack. You can
 retrieve this output in the **Output** tab on the AWS CloudFormation console, or using the
 [describe-stacks](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-stacks.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-stacks.html") command. 


For more information about elastic network interfaces, see [Elastic network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html").



#### JSON



```
"Resources": {
    "ControlPortAddress": {
        "Type": "AWS::EC2::EIP",
        "Properties": {
            "Domain": "vpc"
        }
    },
    "AssociateControlPort": {
        "Type": "AWS::EC2::EIPAssociation",
        "Properties": {
            "AllocationId": {
                "Fn::GetAtt": [
                    "ControlPortAddress",
                    "AllocationId"
                ]
            },
            "NetworkInterfaceId": {
                "Ref": "controlXface"
            }
        }
    },
    "WebPortAddress": {
        "Type": "AWS::EC2::EIP",
        "Properties": {
            "Domain": "vpc"
        }
    },
    "AssociateWebPort": {
        "Type": "AWS::EC2::EIPAssociation",
        "Properties": {
            "AllocationId": {
                "Fn::GetAtt": [
                    "WebPortAddress",
                    "AllocationId"
                ]
            },
            "NetworkInterfaceId": {
                "Ref": "webXface"
            }
        }
    },
    "SSHSecurityGroup": {
        "Type": "AWS::EC2::SecurityGroup",
        "Properties": {
            "VpcId": {
                "Ref": "VpcId"
            },
            "GroupDescription": "Enable SSH access via port 22",
            "SecurityGroupIngress": [
                {
                    "CidrIp": "0.0.0.0/0",
                    "FromPort": 22,
                    "IpProtocol": "tcp",
                    "ToPort": 22
                }
            ]
        }
    },
    "WebSecurityGroup": {
        "Type": "AWS::EC2::SecurityGroup",
        "Properties": {
            "VpcId": {
                "Ref": "VpcId"
            },
            "GroupDescription": "Enable HTTP access via user-defined port",
            "SecurityGroupIngress": [
                {
                    "CidrIp": "0.0.0.0/0",
                    "FromPort": 80,
                    "IpProtocol": "tcp",
                    "ToPort": 80
                }
            ]
        }
    },
    "controlXface": {
        "Type": "AWS::EC2::NetworkInterface",
        "Properties": {
            "SubnetId": {
                "Ref": "SubnetId"
            },
            "Description": "Interface for controlling traffic such as SSH",
            "GroupSet": [
                {
                    "Fn::GetAtt": [
                        "SSHSecurityGroup",
                        "GroupId"
                    ]
                }
            ],
            "SourceDestCheck": true,
            "Tags": [
                {
                    "Key": "Network",
                    "Value": "Control"
                }
            ]
        }
    },
    "webXface": {
        "Type": "AWS::EC2::NetworkInterface",
        "Properties": {
            "SubnetId": {
                "Ref": "SubnetId"
            },
            "Description": "Interface for web traffic",
            "GroupSet": [
                {
                    "Fn::GetAtt": [
                        "WebSecurityGroup",
                        "GroupId"
                    ]
                }
            ],
            "SourceDestCheck": true,
            "Tags": [
                {
                    "Key": "Network",
                    "Value": "Web"
                }
            ]
        }
    },
    "Ec2Instance": {
        "Type": "AWS::EC2::Instance",
        "Properties": {
            "ImageId": {
                "Fn::FindInMap": [
                    "RegionMap",
                    {
                        "Ref": "AWS::Region"
                    },
                    "AMI"
                ]
            },
            "KeyName": {
                "Ref": "KeyName"
            },
            "NetworkInterfaces": [
                {
                    "NetworkInterfaceId": {
                        "Ref": "controlXface"
                    },
                    "DeviceIndex": "0"
                },
                {
                    "NetworkInterfaceId": {
                        "Ref": "webXface"
                    },
                    "DeviceIndex": "1"
                }
            ],
            "Tags": [
                {
                    "Key": "Role",
                    "Value": "Test Instance"
                }
            ],
            "UserData": {
                "Fn::Base64": {
                    "Fn::Sub": "#!/bin/bash -xe\nyum install ec2-net-utils -y\nec2ifup eth1\nservice httpd start\n"
                }
            }
        }
    }
},
"Outputs": {
    "InstancePublicIp": {
        "Description": "Public IP Address of the EC2 Instance",
        "Value": {
            "Fn::GetAtt": [
                "Ec2Instance",
                "PublicIp"
            ]
        }
    }
}
```



#### YAML



```
Resources:
  ControlPortAddress:
    Type: 'AWS::EC2::EIP'
    Properties:
      Domain: vpc
  AssociateControlPort:
    Type: 'AWS::EC2::EIPAssociation'
    Properties:
      AllocationId:
        Fn::GetAtt:
          - ControlPortAddress
          - AllocationId
      NetworkInterfaceId:
        Ref: controlXface
  WebPortAddress:
    Type: 'AWS::EC2::EIP'
    Properties:
      Domain: vpc
  AssociateWebPort:
    Type: 'AWS::EC2::EIPAssociation'
    Properties:
      AllocationId:
        Fn::GetAtt:
          - WebPortAddress
          - AllocationId
      NetworkInterfaceId:
        Ref: webXface
  SSHSecurityGroup:
    Type: 'AWS::EC2::SecurityGroup'
    Properties:
      VpcId:
        Ref: VpcId
      GroupDescription: Enable SSH access via port 22
      SecurityGroupIngress:
        - CidrIp: 0.0.0.0/0
          FromPort: 22
          IpProtocol: tcp
          ToPort: 22
  WebSecurityGroup:
    Type: 'AWS::EC2::SecurityGroup'
    Properties:
      VpcId:
        Ref: VpcId
      GroupDescription: Enable HTTP access via user-defined port
      SecurityGroupIngress:
        - CidrIp: 0.0.0.0/0
          FromPort: 80
          IpProtocol: tcp
          ToPort: 80
  controlXface:
    Type: 'AWS::EC2::NetworkInterface'
    Properties:
      SubnetId:
        Ref: SubnetId
      Description: Interface for controlling traffic such as SSH
      GroupSet:
        - Fn::GetAtt:
            - SSHSecurityGroup
            - GroupId
      SourceDestCheck: true
      Tags:
        - Key: Network
          Value: Control
  webXface:
    Type: 'AWS::EC2::NetworkInterface'
    Properties:
      SubnetId:
        Ref: SubnetId
      Description: Interface for web traffic
      GroupSet:
        - Fn::GetAtt:
            - WebSecurityGroup
            - GroupId
      SourceDestCheck: true
      Tags:
        - Key: Network
          Value: Web
  Ec2Instance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId:
        Fn::FindInMap:
          - RegionMap
          - Ref: AWS::Region
          - AMI
      KeyName:
        Ref: KeyName
      NetworkInterfaces:
        - NetworkInterfaceId:
            Ref: controlXface
          DeviceIndex: "0"
        - NetworkInterfaceId:
            Ref: webXface
          DeviceIndex: "1"
      Tags:
        - Key: Role
          Value: Test Instance
      UserData:
        Fn::Base64: !Sub |
          #!/bin/bash -xe
          yum install ec2-net-utils -y
          ec2ifup eth1
          service httpd start
Outputs:
  InstancePublicIp:
    Description: Public IP Address of the EC2 Instance
    Value:
      Fn::GetAtt:
        - Ec2Instance
        - PublicIp
```
