This is the new _CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# `DependsOn` attribute

With the `DependsOn` attribute you can specify that the creation of a specific
resource follows another. When you add a `DependsOn` attribute to a resource,
that resource is created only after the creation of the resource specified in the
`DependsOn` attribute.

###### Important

Dependent stacks also have implicit dependencies in the form of target properties
`!Ref`, `!GetAtt`, and `!Sub`. For example, if the
properties of resource A use a `!Ref` to resource B, the following rules
apply:

- Resource B is created before resource A.
- Resource A is deleted before resource B.
- Resource B is updated before resource A.
  You can use the `DependsOn` attribute with any resource. Here are some typical
  uses:

- Determine when a wait condition goes into effect. For more information, see [Creating wait
  conditions in a template](../UserGuide/using-cfn-waitcondition.md "../UserGuide/using-cfn-waitcondition.md") in the
  _AWS CloudFormation User Guide_.
- Declare dependencies for resources that must be created or deleted in a specific
  order. For example, you must explicitly declare dependencies on gateway attachments
  for some resources in a VPC. For more information, see [When a DependsOn attribute is
  required](#gatewayattachment "#gatewayattachment").
- Override default parallelism when creating, updating, or deleting resources. CloudFormation
  creates, updates, and deletes resources in parallel to the extent possible. It
  automatically determines which resources in a template can be parallelized and which
  have dependencies that require other operations to finish first. You can use
  `DependsOn` to explicitly specify dependencies, which overrides the
  default parallelism and directs CloudFormation to operate on those resources in a
  specified order.

###### Note

During a stack update, resources that depend on updated resources are updated
automatically. CloudFormation makes no changes to the automatically updated resources, but,
if a stack policy is associated with these resources, your account must have the
permissions to update them.

## Syntax

The `DependsOn` attribute can take a single string or list of
strings.

```
"DependsOn" : [ `String, ...` ]
```

## Example

The following template contains an [AWS::EC2::Instance](aws-resource-ec2-instance.md "aws-resource-ec2-instance.md") resource
with a `DependsOn` attribute that specifies `myDB`, an [AWS::RDS::DBInstance](aws-resource-rds-dbinstance.md "aws-resource-rds-dbinstance.md"). When CloudFormation creates this stack, it first creates
`myDB`, then creates `Ec2Instance`.

### JSON

```
{
    "Resources" : {
        "Ec2Instance" : {
            "Type" : "AWS::EC2::Instance",
            "Properties" : {
                "ImageId": "{{resolve:ssm:/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64}}",
                "InstanceType": "t2.micro"
            },
            "DependsOn" : "myDB"
        },
        "myDB" : {
            "Type" : "AWS::RDS::DBInstance",
            "Properties" : {
               "AllocatedStorage" : "5",
               "DBInstanceClass" : "db.t2.small",
               "Engine" : "MySQL",
               "EngineVersion" : "5.5",
               "MasterUsername" : "{{resolve:secretsmanager:`MySecret`:SecretString:`username`}}",
               "MasterUserPassword" : "{{resolve:secretsmanager:`MySecret`:SecretString:`password`}}"
            }
        }
    }
}
```

### YAML

```
Resources:
  Ec2Instance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: '{{resolve:ssm:/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64}}'
      InstanceType: t2.micro
    DependsOn: myDB
  myDB:
    Type: AWS::RDS::DBInstance
    Properties:
      AllocatedStorage: '5'
      DBInstanceClass: db.t2.small
      Engine: MySQL
      EngineVersion: '5.5'
      MasterUsername: '{{resolve:secretsmanager:`MySecret`:SecretString:`username`}}'
      MasterUserPassword: '{{resolve:secretsmanager:`MySecret`:SecretString:`password`}}'
```

## When a `DependsOn` attribute is

required

VPC-gateway attachment

Some resources in a VPC require a gateway (either an Internet or VPN gateway). If your
CloudFormation template defines a VPC, a gateway, and a gateway attachment, any resources
that require the gateway are dependent on the gateway attachment. For example, an Amazon EC2
instance with a public IP address is dependent on the VPC-gateway attachment if the
`VPC` and `InternetGateway` resources are also declared in the
same template.

Currently, the following resources depend on a VPC-gateway attachment when they have
an associated public IP address and are in a VPC.

- Amazon EC2 Auto Scaling groups
- Amazon EC2 instances
- ELB load balancers
- Elastic IP addresses
- Amazon RDS database instances
- Amazon VPC routes that include the Internet gateway

A VPN gateway route propagation depends on a VPC-gateway attachment when you have a
VPN gateway.

The following snippet shows a sample gateway attachment and an Amazon EC2 instance that
depends on a gateway attachment:

### JSON

```
"GatewayToInternet" : {
  "Type" : "AWS::EC2::VPCGatewayAttachment",
  "Properties" : {
    "VpcId" : {
      "Ref" : "VPC"
    },
    "InternetGatewayId" : {
      "Ref" : "InternetGateway"
    }
  }
},

"EC2Host" : {
  "Type" : "AWS::EC2::Instance",
  "DependsOn" : "GatewayToInternet",
  "Properties" : {
    "InstanceType" : "t2.micro",
    "ImageId": "{{resolve:ssm:/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64}}",
    "KeyName"  : {
      "Ref" : "KeyName"
    },
    "NetworkInterfaces" : [
      {
        "GroupSet" : [
          {
            "Ref" : "EC2SecurityGroup"
          }
        ],
        "AssociatePublicIpAddress" : "true",
        "DeviceIndex" : "0",
        "DeleteOnTermination" : "true",
        "SubnetId" : {
          "Ref" : "PublicSubnet"
        }
      }
    ]
  }
}
```

### YAML

```
GatewayToInternet:
  Type: AWS::EC2::VPCGatewayAttachment
  Properties:
    VpcId:
      Ref: VPC
    InternetGatewayId:
      Ref: InternetGateway
EC2Host:
  Type: AWS::EC2::Instance
  DependsOn: GatewayToInternet
  Properties:
    InstanceType: t2.micro
    ImageId: '{{resolve:ssm:/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64}}'
    KeyName:
      Ref: KeyName
    NetworkInterfaces:
    - GroupSet:
      - Ref: EC2SecurityGroup
      AssociatePublicIpAddress: 'true'
      DeviceIndex: '0'
      DeleteOnTermination: 'true'
      SubnetId:
        Ref: PublicSubnet
```

### Amazon ECS service and Amazon EC2 Auto Scaling group

When you use Amazon EC2 Auto Scaling or Amazon Elastic Compute Cloud (Amazon EC2) to create container instances for an Amazon ECS
cluster, the Amazon ECS service resource must have a dependency on the Amazon EC2 Auto Scaling group or
Amazon EC2 instances, as shown in the following snippet. That way the container instances
are available and associated with the Amazon ECS cluster before CloudFormation creates the
Amazon ECS service.

#### JSON

```
"service": {
  "Type": "AWS::ECS::Service",
  "DependsOn": [
    "ECSAutoScalingGroup"
  ],
  "Properties" : {
    "Cluster": {
      "Ref": "ECSCluster"
    },
    "DesiredCount": "1",
    "LoadBalancers": [
      {
        "ContainerName": "simple-app",
        "ContainerPort": "80",
        "LoadBalancerName" : {
          "Ref" : "EcsElasticLoadBalancer"
        }
      }
    ],
    "Role" : {
      "Ref":"ECSServiceRole"
    },
    "TaskDefinition" : {
      "Ref":"taskdefinition"
    }
  }
}
```

#### YAML

```
service:
  Type: AWS::ECS::Service
  DependsOn:
  - ECSAutoScalingGroup
  Properties:
    Cluster:
      Ref: ECSCluster
    DesiredCount: 1
    LoadBalancers:
    - ContainerName: simple-app
      ContainerPort: 80
      LoadBalancerName:
        Ref: EcsElasticLoadBalancer
    Role:
      Ref: ECSServiceRole
    TaskDefinition:
      Ref: taskdefinition
```

### IAM role policy

Resources that make additional calls to AWS require a service role, which
permits a service to make calls to AWS on your behalf. For example, the
`AWS::CodeDeploy::DeploymentGroup` resource requires a service role
so that CodeDeploy has permissions to deploy applications to your instances. When you
have a single template that defines a service role, the role's policy (by using the
`AWS::IAM::Policy` or `AWS::IAM::ManagedPolicy` resource),
and a resource that uses the role, add a dependency so that the resource depends on
the role's policy. This dependency ensures that the policy is available throughout
the resource's lifecycle.

For example, imagine that you have a template with a deployment group resource, a
service role, and the role's policy. When you create a stack, CloudFormation won't
create the deployment group until it creates the role's policy. Without the
dependency, CloudFormation can create the deployment group resource before it creates
the role's policy. If that happens, the deployment group will fail to create because
of insufficient permissions.

If the role has an embedded policy, don't specify a dependency. CloudFormation creates
the role and its policy at the same time.
