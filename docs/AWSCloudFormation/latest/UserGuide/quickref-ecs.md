# Amazon Elastic Container Service sample templates

Amazon Elastic Container Service (Amazon ECS) is a container management service that makes it easy to run, stop, and
manage Docker containers on a cluster of Amazon Elastic Compute Cloud (Amazon EC2) instances.

## Create a cluster with the AL2023 Amazon ECS-Optimized-AMI

Define a cluster that uses a capacity provider that launches AL2023 instances on
Amazon EC2.

###### Important

For the latest AMI IDs, see [Amazon ECS-optimized AMI](../../../AmazonECS/latest/developerguide/ecs-optimized_AMI.md "../../../AmazonECS/latest/developerguide/ecs-optimized_AMI.md") in the _Amazon Elastic Container Service Developer Guide_.

### JSON

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "EC2 ECS cluster that starts out empty, with no EC2 instances yet. An ECS capacity provider automatically launches more EC2 instances as required on the fly when you request ECS to launch services or standalone tasks.",
  "Parameters": {
      "InstanceType": {
          "Type": "String",
          "Description": "EC2 instance type",
          "Default": "t2.medium",
          "AllowedValues": [
              "t1.micro",
              "t2.2xlarge",
              "t2.large",
              "t2.medium",
              "t2.micro",
              "t2.nano",
              "t2.small",
              "t2.xlarge",
              "t3.2xlarge",
              "t3.large",
              "t3.medium",
              "t3.micro",
              "t3.nano",
              "t3.small",
              "t3.xlarge"
          ]
      },
      "DesiredCapacity": {
          "Type": "Number",
          "Default": "0",
          "Description": "Number of EC2 instances to launch in your ECS cluster."
      },
      "MaxSize": {
          "Type": "Number",
          "Default": "100",
          "Description": "Maximum number of EC2 instances that can be launched in your ECS cluster."
      },
      "ECSAMI": {
          "Description": "The Amazon Machine Image ID used for the cluster",
          "Type": "AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>",
          "Default": "/aws/service/ecs/optimized-ami/amazon-linux-2023/recommended/image_id"
      },
      "VpcId": {
          "Type": "AWS::EC2::VPC::Id",
          "Description": "VPC ID where the ECS cluster is launched",
          "Default": "vpc-1234567890abcdef0"
      },
      "SubnetIds": {
          "Type": "List<AWS::EC2::Subnet::Id>",
          "Description": "List of subnet IDs where the EC2 instances will be launched",
          "Default": "subnet-021345abcdef67890"
      }
  },
  "Resources": {
      "ECSCluster": {
          "Type": "AWS::ECS::Cluster",
          "Properties": {
              "ClusterSettings": [
                  {
                      "Name": "containerInsights",
                      "Value": "enabled"
                  }
              ]
          }
      },
      "ECSAutoScalingGroup": {
          "Type": "AWS::AutoScaling::AutoScalingGroup",
          "DependsOn": [
              "ECSCluster",
              "EC2Role"
          ],
          "Properties": {
              "VPCZoneIdentifier": {
                  "Ref": "SubnetIds"
              },
              "LaunchTemplate": {
                  "LaunchTemplateId": {
                      "Ref": "ContainerInstances"
                  },
                  "Version": {
                      "Fn::GetAtt": [
                          "ContainerInstances",
                          "LatestVersionNumber"
                      ]
                  }
              },
              "MinSize": 0,
              "MaxSize": {
                  "Ref": "MaxSize"
              },
              "DesiredCapacity": {
                  "Ref": "DesiredCapacity"
              },
              "NewInstancesProtectedFromScaleIn": true
          },
          "UpdatePolicy": {
              "AutoScalingReplacingUpdate": {
                  "WillReplace": "true"
              }
          }
      },
      "ContainerInstances": {
          "Type": "AWS::EC2::LaunchTemplate",
          "Properties": {
              "LaunchTemplateName": "asg-launch-template",
              "LaunchTemplateData": {
                  "ImageId": {
                      "Ref": "ECSAMI"
                  },
                  "InstanceType": {
                      "Ref": "InstanceType"
                  },
                  "IamInstanceProfile": {
                      "Name": {
                          "Ref": "EC2InstanceProfile"
                      }
                  },
                  "SecurityGroupIds": [
                      {
                          "Ref": "ContainerHostSecurityGroup"
                      }
                  ],
                  "UserData": {
                      "Fn::Base64": {
                          "Fn::Sub": "#!/bin/bash -xe\n echo ECS_CLUSTER=${ECSCluster} >> /etc/ecs/ecs.config\n yum install -y aws-cfn-bootstrap\n /opt/aws/bin/cfn-init -v --stack ${AWS::StackId} --resource ContainerInstances --configsets full_install --region ${AWS::Region} &\n"
                      }
                  },
                  "MetadataOptions": {
                      "HttpEndpoint": "enabled",
                      "HttpTokens": "required"
                  }
              }
          }
      },
      "EC2InstanceProfile": {
          "Type": "AWS::IAM::InstanceProfile",
          "Properties": {
              "Path": "/",
              "Roles": [
                  {
                      "Ref": "EC2Role"
                  }
              ]
          }
      },
      "CapacityProvider": {
          "Type": "AWS::ECS::CapacityProvider",
          "Properties": {
              "AutoScalingGroupProvider": {
                  "AutoScalingGroupArn": {
                      "Ref": "ECSAutoScalingGroup"
                  },
                  "ManagedScaling": {
                      "InstanceWarmupPeriod": 60,
                      "MinimumScalingStepSize": 1,
                      "MaximumScalingStepSize": 100,
                      "Status": "ENABLED",
                      "TargetCapacity": 100
                  },
                  "ManagedTerminationProtection": "ENABLED"
              }
          }
      },
      "CapacityProviderAssociation": {
          "Type": "AWS::ECS::ClusterCapacityProviderAssociations",
          "Properties": {
              "CapacityProviders": [
                  {
                      "Ref": "CapacityProvider"
                  }
              ],
              "Cluster": {
                  "Ref": "ECSCluster"
              },
              "DefaultCapacityProviderStrategy": [
                  {
                      "Base": 0,
                      "CapacityProvider": {
                          "Ref": "CapacityProvider"
                      },
                      "Weight": 1
                  }
              ]
          }
      },
      "ContainerHostSecurityGroup": {
          "Type": "AWS::EC2::SecurityGroup",
          "Properties": {
              "GroupDescription": "Access to the EC2 hosts that run containers",
              "VpcId": {
                  "Ref": "VpcId"
              }
          }
      },
      "EC2Role": {
          "Type": "AWS::IAM::Role",
          "Properties": {
              "AssumeRolePolicyDocument": {
                  "Statement": [
                      {
                          "Effect": "Allow",
                          "Principal": {
                              "Service": [
                                  "ec2.amazonaws.com"
                              ]
                          },
                          "Action": [
                              "sts:AssumeRole"
                          ]
                      }
                  ]
              },
              "Path": "/",
              "ManagedPolicyArns": [
                  "arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role",
                  "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
              ]
          }
      },
      "ECSTaskExecutionRole": {
          "Type": "AWS::IAM::Role",
          "Properties": {
              "AssumeRolePolicyDocument": {
                  "Statement": [
                      {
                          "Effect": "Allow",
                          "Principal": {
                              "Service": [
                                  "ecs-tasks.amazonaws.com"
                              ]
                          },
                          "Action": [
                              "sts:AssumeRole"
                          ],
                          "Condition": {
                              "ArnLike": {
                                  "aws:SourceArn": {
                                      "Fn::Sub": "arn:${AWS::Partition}:ecs:${AWS::Region}:${AWS::AccountId}:*"
                                  }
                              },
                              "StringEquals": {
                                  "aws:SourceAccount": {
                                        "Fn::Sub": "${AWS::AccountId}"
                                    }
                              }
                          }
                      }
                  ]
              },
              "Path": "/",
              "ManagedPolicyArns": [
                  "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
              ]
          }
      }
  },
  "Outputs": {
      "ClusterName": {
          "Description": "The ECS cluster into which to launch resources",
          "Value": "ECSCluster"
      },
      "ECSTaskExecutionRole": {
          "Description": "The role used to start up a task",
          "Value": "ECSTaskExecutionRole"
      },
      "CapacityProvider": {
          "Description": "The cluster capacity provider that the service should use to request capacity when it wants to start up a task",
          "Value": "CapacityProvider"
      }
  }
}

```

### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Description: EC2 ECS cluster that starts out empty, with no EC2 instances yet.
  An ECS capacity provider automatically launches more EC2 instances as required
  on the fly when you request ECS to launch services or standalone tasks.
Parameters:
  InstanceType:
    Type: String
    Description: EC2 instance type
    Default: "t2.medium"
    AllowedValues:
      - t1.micro
      - t2.2xlarge
      - t2.large
      - t2.medium
      - t2.micro
      - t2.nano
      - t2.small
      - t2.xlarge
      - t3.2xlarge
      - t3.large
      - t3.medium
      - t3.micro
      - t3.nano
      - t3.small
      - t3.xlarge
  DesiredCapacity:
    Type: Number
    Default: "0"
    Description: Number of EC2 instances to launch in your ECS cluster.
  MaxSize:
    Type: Number
    Default: "100"
    Description: Maximum number of EC2 instances that can be launched in your ECS cluster.
  ECSAMI:
    Description: The Amazon Machine Image ID used for the cluster
    Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
    Default: /aws/service/ecs/optimized-ami/amazon-linux-2023/recommended/image_id
  VpcId:
    Type: AWS::EC2::VPC::Id
    Description: VPC ID where the ECS cluster is launched
    Default: vpc-1234567890abcdef0
  SubnetIds:
    Type: List<AWS::EC2::Subnet::Id>
    Description: List of subnet IDs where the EC2 instances will be launched
    Default: "subnet-021345abcdef67890"
Resources:
# This is authorizes ECS to manage resources on your
  # account on your behalf. This role is likely already created on your account
  # ECSRole:
  #  Type: AWS::IAM::ServiceLinkedRole
  #  Properties:
  #    AWSServiceName: 'ecs.amazonaws.com'

   # ECS Resources
  ECSCluster:
    Type: AWS::ECS::Cluster
    Properties:
      ClusterSettings:
        - Name: containerInsights
          Value: enabled

  # Autoscaling group. This launches the actual EC2 instances that will register
  # themselves as members of the cluster, and run the docker containers.
  ECSAutoScalingGroup:
    Type: AWS::AutoScaling::AutoScalingGroup
    DependsOn:
      # This is to ensure that the ASG gets deleted first before these
    # resources, when it comes to stack teardown.
      - ECSCluster
      - EC2Role
    Properties:
      VPCZoneIdentifier:
        Ref: SubnetIds
      LaunchTemplate:
        LaunchTemplateId: !Ref ContainerInstances
        Version: !GetAtt ContainerInstances.LatestVersionNumber
      MinSize: 0
      MaxSize:
        Ref: MaxSize
      DesiredCapacity:
        Ref: DesiredCapacity
      NewInstancesProtectedFromScaleIn: true
    UpdatePolicy:
      AutoScalingReplacingUpdate:
        WillReplace: "true"
  # The config for each instance that is added to the cluster
  ContainerInstances:
    Type: AWS::EC2::LaunchTemplate
    Properties:
      LaunchTemplateName: "asg-launch-template"
      LaunchTemplateData:
        ImageId:
          Ref: ECSAMI
        InstanceType:
          Ref: InstanceType
        IamInstanceProfile:
          Name: !Ref EC2InstanceProfile
        SecurityGroupIds:
          - !Ref ContainerHostSecurityGroup
        # This injected configuration file is how the EC2 instance
      # knows which ECS cluster on your AWS account it should be joining
        UserData:
          Fn::Base64: !Sub |
           #!/bin/bash -xe
            echo ECS_CLUSTER=${ECSCluster} >> /etc/ecs/ecs.config
            yum install -y aws-cfn-bootstrap
            /opt/aws/bin/cfn-init -v --stack ${AWS::StackId} --resource ContainerInstances --configsets full_install --region ${AWS::Region} &
         # Disable IMDSv1, and require IMDSv2
        MetadataOptions:
          HttpEndpoint: enabled
          HttpTokens: required
  EC2InstanceProfile:
    Type: AWS::IAM::InstanceProfile
    Properties:
      Path: /
      Roles:
      - !Ref EC2Role
  # Create an ECS capacity provider to attach the ASG to the ECS cluster
  # so that it autoscales as we launch more containers
  CapacityProvider:
    Type: AWS::ECS::CapacityProvider
    Properties:
      AutoScalingGroupProvider:
        AutoScalingGroupArn: !Ref ECSAutoScalingGroup
        ManagedScaling:
          InstanceWarmupPeriod: 60
          MinimumScalingStepSize: 1
          MaximumScalingStepSize: 100
          Status: ENABLED
          # Percentage of cluster reservation to try to maintain
          TargetCapacity: 100
        ManagedTerminationProtection: ENABLED
   # Create a cluster capacity provider assocation so that the cluster
  # will use the capacity provider
  CapacityProviderAssociation:
    Type: AWS::ECS::ClusterCapacityProviderAssociations
    Properties:
      CapacityProviders:
        - !Ref CapacityProvider
      Cluster: !Ref ECSCluster
      DefaultCapacityProviderStrategy:
        - Base: 0
          CapacityProvider: !Ref CapacityProvider
          Weight: 1
  # A security group for the EC2 hosts that will run the containers.
  # This can be used to limit incoming traffic to or outgoing traffic
  # from the container's host EC2 instance.
  ContainerHostSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Access to the EC2 hosts that run containers
      VpcId:
        Ref: VpcId
  # Role for the EC2 hosts. This allows the ECS agent on the EC2 hosts
  # to communciate with the ECS control plane, as well as download the docker
  # images from ECR to run on your host.
  EC2Role:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - ec2.amazonaws.com
            Action:
              - sts:AssumeRole
      Path: /
      ManagedPolicyArns:
      # See reference: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonEC2ContainerServiceforEC2Role
        - arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role
      # This managed policy allows us to connect to the instance using SSM
        - arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore
  # This is a role which is used within Fargate to allow the Fargate agent
  # to download images, and upload logs.
  ECSTaskExecutionRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - ecs-tasks.amazonaws.com
            Action:
              - sts:AssumeRole
            Condition:
              ArnLike:
                aws:SourceArn: !Sub arn:${AWS::Partition}:ecs:${AWS::Region}:${AWS::AccountId}:*
              StringEquals:
                aws:SourceAccount: !Sub ${AWS::AccountId}
      Path: /
      # This role enables all features of ECS. See reference:
    # https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonECSTaskExecutionRolePolicy
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy
Outputs:
  ClusterName:
    Description: The ECS cluster into which to launch resources
    Value: ECSCluster
  ECSTaskExecutionRole:
    Description: The role used to start up a task
    Value: ECSTaskExecutionRole
  CapacityProvider:
    Description: The cluster capacity provider that the service should use to
      request capacity when it wants to start up a task
    Value: CapacityProvider
```

## Deploy a service

The following template defines a service that uses the capacity provider to request AL2023 capacity to run on. Containers will be launched onto the AL2023 instances as they come online:

### JSON

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "An example service that deploys in AWS VPC networking mode on EC2 capacity. Service uses a capacity provider to request EC2 instances to run on. Service runs with networking in private subnets, but still accessible to the internet via a load balancer hosted in public subnets.",
  "Parameters": {
      "VpcId": {
          "Type": "String",
          "Description": "The VPC that the service is running inside of"
      },
      "PublicSubnetIds": {
          "Type": "List<AWS::EC2::Subnet::Id>",
          "Description": "List of public subnet ID's to put the load balancer in"
      },
      "PrivateSubnetIds": {
          "Type": "List<AWS::EC2::Subnet::Id>",
          "Description": "List of private subnet ID's that the AWS VPC tasks are in"
      },
      "ClusterName": {
          "Type": "String",
          "Description": "The name of the ECS cluster into which to launch capacity."
      },
      "ECSTaskExecutionRole": {
          "Type": "String",
          "Description": "The role used to start up an ECS task"
      },
      "CapacityProvider": {
          "Type": "String",
          "Description": "The cluster capacity provider that the service should use to request capacity when it wants to start up a task"
      },
      "ServiceName": {
          "Type": "String",
          "Default": "web",
          "Description": "A name for the service"
      },
      "ImageUrl": {
          "Type": "String",
          "Default": "public.ecr.aws/docker/library/nginx:latest",
          "Description": "The url of a docker image that contains the application process that will handle the traffic for this service"
      },
      "ContainerCpu": {
          "Type": "Number",
          "Default": 256,
          "Description": "How much CPU to give the container. 1024 is 1 CPU"
      },
      "ContainerMemory": {
          "Type": "Number",
          "Default": 512,
          "Description": "How much memory in megabytes to give the container"
      },
      "ContainerPort": {
          "Type": "Number",
          "Default": 80,
          "Description": "What port that the application expects traffic on"
      },
      "DesiredCount": {
          "Type": "Number",
          "Default": 2,
          "Description": "How many copies of the service task to run"
      }
  },
  "Resources": {
      "TaskDefinition": {
          "Type": "AWS::ECS::TaskDefinition",
          "Properties": {
              "Family": {
                  "Ref": "ServiceName"
              },
              "Cpu": {
                  "Ref": "ContainerCpu"
              },
              "Memory": {
                  "Ref": "ContainerMemory"
              },
              "NetworkMode": "awsvpc",
              "RequiresCompatibilities": [
                  "EC2"
              ],
              "ExecutionRoleArn": {
                  "Ref": "ECSTaskExecutionRole"
              },
              "ContainerDefinitions": [
                  {
                      "Name": {
                          "Ref": "ServiceName"
                      },
                      "Cpu": {
                          "Ref": "ContainerCpu"
                      },
                      "Memory": {
                          "Ref": "ContainerMemory"
                      },
                      "Image": {
                          "Ref": "ImageUrl"
                      },
                      "PortMappings": [
                          {
                              "ContainerPort": {
                                  "Ref": "ContainerPort"
                              },
                              "HostPort": {
                                  "Ref": "ContainerPort"
                              }
                          }
                      ],
                      "LogConfiguration": {
                          "LogDriver": "awslogs",
                          "Options": {
                              "mode": "non-blocking",
                              "max-buffer-size": "25m",
                              "awslogs-group": {
                                  "Ref": "LogGroup"
                              },
                              "awslogs-region": {
                                  "Ref": "AWS::Region"
                              },
                              "awslogs-stream-prefix": {
                                  "Ref": "ServiceName"
                              }
                          }
                      }
                  }
              ]
          }
      },
      "Service": {
          "Type": "AWS::ECS::Service",
          "DependsOn": "PublicLoadBalancerListener",
          "Properties": {
              "ServiceName": {
                  "Ref": "ServiceName"
              },
              "Cluster": {
                  "Ref": "ClusterName"
              },
              "PlacementStrategies": [
                  {
                      "Field": "attribute:ecs.availability-zone",
                      "Type": "spread"
                  },
                  {
                      "Field": "cpu",
                      "Type": "binpack"
                  }
              ],
              "CapacityProviderStrategy": [
                  {
                      "Base": 0,
                      "CapacityProvider": {
                          "Ref": "CapacityProvider"
                      },
                      "Weight": 1
                  }
              ],
              "NetworkConfiguration": {
                  "AwsvpcConfiguration": {
                      "SecurityGroups": [
                          {
                              "Ref": "ServiceSecurityGroup"
                          }
                      ],
                      "Subnets": {
                          "Ref": "PrivateSubnetIds"
                      }
                  }
              },
              "DeploymentConfiguration": {
                  "MaximumPercent": 200,
                  "MinimumHealthyPercent": 75
              },
              "DesiredCount": {
                  "Ref": "DesiredCount"
              },
              "TaskDefinition": {
                  "Ref": "TaskDefinition"
              },
              "LoadBalancers": [
                  {
                      "ContainerName": {
                          "Ref": "ServiceName"
                      },
                      "ContainerPort": {
                          "Ref": "ContainerPort"
                      },
                      "TargetGroupArn": {
                          "Ref": "ServiceTargetGroup"
                      }
                  }
              ]
          }
      },
      "ServiceSecurityGroup": {
          "Type": "AWS::EC2::SecurityGroup",
          "Properties": {
              "GroupDescription": "Security group for service",
              "VpcId": {
                  "Ref": "VpcId"
              }
          }
      },
      "ServiceTargetGroup": {
          "Type": "AWS::ElasticLoadBalancingV2::TargetGroup",
          "Properties": {
              "HealthCheckIntervalSeconds": 6,
              "HealthCheckPath": "/",
              "HealthCheckProtocol": "HTTP",
              "HealthCheckTimeoutSeconds": 5,
              "HealthyThresholdCount": 2,
              "TargetType": "ip",
              "Port": {
                  "Ref": "ContainerPort"
              },
              "Protocol": "HTTP",
              "UnhealthyThresholdCount": 10,
              "VpcId": {
                  "Ref": "VpcId"
              },
              "TargetGroupAttributes": [
                  {
                      "Key": "deregistration_delay.timeout_seconds",
                      "Value": 0
                  }
              ]
          }
      },
      "PublicLoadBalancerSG": {
          "Type": "AWS::EC2::SecurityGroup",
          "Properties": {
              "GroupDescription": "Access to the public facing load balancer",
              "VpcId": {
                  "Ref": "VpcId"
              },
              "SecurityGroupIngress": [
                  {
                      "CidrIp": "0.0.0.0/0",
                      "IpProtocol": -1
                  }
              ]
          }
      },
      "PublicLoadBalancer": {
          "Type": "AWS::ElasticLoadBalancingV2::LoadBalancer",
          "Properties": {
              "Scheme": "internet-facing",
              "LoadBalancerAttributes": [
                  {
                      "Key": "idle_timeout.timeout_seconds",
                      "Value": "30"
                  }
              ],
              "Subnets": {
                  "Ref": "PublicSubnetIds"
              },
              "SecurityGroups": [
                  {
                      "Ref": "PublicLoadBalancerSG"
                  }
              ]
          }
      },
      "PublicLoadBalancerListener": {
          "Type": "AWS::ElasticLoadBalancingV2::Listener",
          "Properties": {
              "DefaultActions": [
                  {
                      "Type": "forward",
                      "ForwardConfig": {
                          "TargetGroups": [
                              {
                                  "TargetGroupArn": {
                                      "Ref": "ServiceTargetGroup"
                                  },
                                  "Weight": 100
                              }
                          ]
                      }
                  }
              ],
              "LoadBalancerArn": {
                  "Ref": "PublicLoadBalancer"
              },
              "Port": 80,
              "Protocol": "HTTP"
          }
      },
      "ServiceIngressfromLoadBalancer": {
          "Type": "AWS::EC2::SecurityGroupIngress",
          "Properties": {
              "Description": "Ingress from the public ALB",
              "GroupId": {
                  "Ref": "ServiceSecurityGroup"
              },
              "IpProtocol": -1,
              "SourceSecurityGroupId": {
                  "Ref": "PublicLoadBalancerSG"
              }
          }
      },
      "LogGroup": {
          "Type": "AWS::Logs::LogGroup"
      }
  }
}
```

### YAML

```
AWSTemplateFormatVersion: '2010-09-09'
Description: >-
  An example service that deploys in AWS VPC networking mode on EC2 capacity.
  Service uses a capacity provider to request EC2 instances to run on. Service
  runs with networking in private subnets, but still accessible to the internet
  via a load balancer hosted in public subnets.
Parameters:
  VpcId:
    Type: String
    Description: The VPC that the service is running inside of
  PublicSubnetIds:
    Type: 'List<AWS::EC2::Subnet::Id>'
    Description: List of public subnet ID's to put the load balancer in
  PrivateSubnetIds:
    Type: 'List<AWS::EC2::Subnet::Id>'
    Description: List of private subnet ID's that the AWS VPC tasks are in
  ClusterName:
    Type: String
    Description: The name of the ECS cluster into which to launch capacity.
  ECSTaskExecutionRole:
    Type: String
    Description: The role used to start up an ECS task
  CapacityProvider:
    Type: String
    Description: >-
      The cluster capacity provider that the service should use to request
      capacity when it wants to start up a task
  ServiceName:
    Type: String
    Default: web
    Description: A name for the service
  ImageUrl:
    Type: String
    Default: 'public.ecr.aws/docker/library/nginx:latest'
    Description: >-
      The url of a docker image that contains the application process that will
      handle the traffic for this service
  ContainerCpu:
    Type: Number
    Default: 256
    Description: How much CPU to give the container. 1024 is 1 CPU
  ContainerMemory:
    Type: Number
    Default: 512
    Description: How much memory in megabytes to give the container
  ContainerPort:
    Type: Number
    Default: 80
    Description: What port that the application expects traffic on
  DesiredCount:
    Type: Number
    Default: 2
    Description: How many copies of the service task to run
Resources:
  TaskDefinition:
    Type: 'AWS::ECS::TaskDefinition'
    Properties:
      Family: !Ref ServiceName
      Cpu: !Ref ContainerCpu
      Memory: !Ref ContainerMemory
      NetworkMode: awsvpc
      RequiresCompatibilities:
        - EC2
      ExecutionRoleArn: !Ref ECSTaskExecutionRole
      ContainerDefinitions:
        - Name: !Ref ServiceName
          Cpu: !Ref ContainerCpu
          Memory: !Ref ContainerMemory
          Image: !Ref ImageUrl
          PortMappings:
            - ContainerPort: !Ref ContainerPort
              HostPort: !Ref ContainerPort
          LogConfiguration:
            LogDriver: awslogs
            Options:
              mode: non-blocking
              max-buffer-size: 25m
              awslogs-group: !Ref LogGroup
              awslogs-region: !Ref AWS::Region
              awslogs-stream-prefix: !Ref ServiceName
  Service:
    Type: AWS::ECS::Service
    DependsOn: PublicLoadBalancerListener
    Properties:
      ServiceName: !Ref ServiceName
      Cluster: !Ref ClusterName
      PlacementStrategies:
        - Field: 'attribute:ecs.availability-zone'
          Type: spread
        - Field: cpu
          Type: binpack
      CapacityProviderStrategy:
        - Base: 0
          CapacityProvider: !Ref CapacityProvider
          Weight: 1
      NetworkConfiguration:
        AwsvpcConfiguration:
          SecurityGroups:
            - !Ref ServiceSecurityGroup
          Subnets: !Ref PrivateSubnetIds
      DeploymentConfiguration:
        MaximumPercent: 200
        MinimumHealthyPercent: 75
      DesiredCount: !Ref DesiredCount
      TaskDefinition: !Ref TaskDefinition
      LoadBalancers:
        - ContainerName: !Ref ServiceName
          ContainerPort: !Ref ContainerPort
          TargetGroupArn: !Ref ServiceTargetGroup
  ServiceSecurityGroup:
    Type: 'AWS::EC2::SecurityGroup'
    Properties:
      GroupDescription: Security group for service
      VpcId: !Ref VpcId
  ServiceTargetGroup:
    Type: 'AWS::ElasticLoadBalancingV2::TargetGroup'
    Properties:
      HealthCheckIntervalSeconds: 6
      HealthCheckPath: /
      HealthCheckProtocol: HTTP
      HealthCheckTimeoutSeconds: 5
      HealthyThresholdCount: 2
      TargetType: ip
      Port: !Ref ContainerPort
      Protocol: HTTP
      UnhealthyThresholdCount: 10
      VpcId: !Ref VpcId
      TargetGroupAttributes:
        - Key: deregistration_delay.timeout_seconds
          Value: 0
  PublicLoadBalancerSG:
    Type: 'AWS::EC2::SecurityGroup'
    Properties:
      GroupDescription: Access to the public facing load balancer
      VpcId: !Ref VpcId
      SecurityGroupIngress:
        - CidrIp: 0.0.0.0/0
          IpProtocol: -1
  PublicLoadBalancer:
    Type: 'AWS::ElasticLoadBalancingV2::LoadBalancer'
    Properties:
      Scheme: internet-facing
      LoadBalancerAttributes:
        - Key: idle_timeout.timeout_seconds
          Value: '30'
      Subnets: !Ref PublicSubnetIds
      SecurityGroups:
        - !Ref PublicLoadBalancerSG
  PublicLoadBalancerListener:
    Type: 'AWS::ElasticLoadBalancingV2::Listener'
    Properties:
      DefaultActions:
        - Type: forward
          ForwardConfig:
            TargetGroups:
              - TargetGroupArn: !Ref ServiceTargetGroup
                Weight: 100
      LoadBalancerArn: !Ref PublicLoadBalancer
      Port: 80
      Protocol: HTTP
  ServiceIngressfromLoadBalancer:
    Type: 'AWS::EC2::SecurityGroupIngress'
    Properties:
      Description: Ingress from the public ALB
      GroupId: !Ref ServiceSecurityGroup
      IpProtocol: -1
      SourceSecurityGroupId: !Ref PublicLoadBalancerSG
  LogGroup:
    Type: 'AWS::Logs::LogGroup'

```
