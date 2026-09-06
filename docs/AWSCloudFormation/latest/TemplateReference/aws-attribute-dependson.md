

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# `DependsOn` attribute
<a name="aws-attribute-dependson"></a>

With the `DependsOn` attribute you can specify that the creation of a specific resource follows another. When you add a `DependsOn` attribute to a resource, that resource is created only after the creation of the resource specified in the `DependsOn` attribute.

**Important**  
Dependent stacks also have implicit dependencies in the form of target properties `!Ref`, `!GetAtt`, and `!Sub`. For example, if the properties of resource A use a `!Ref` to resource B, the following rules apply:  
Resource B is created before resource A.
Resource A is deleted before resource B.
Resource B is updated before resource A.

You can use the `DependsOn` attribute with any resource. Here are some typical uses:
+ Determine when a wait condition goes into effect. For more information, see [Creating wait conditions in a template](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-waitcondition.html) in the *AWS CloudFormation User Guide*.
+ Declare dependencies for resources that must be created or deleted in a specific order. For example, you must explicitly declare dependencies on gateway attachments for some resources in a VPC. For more information, see [When a `DependsOn` attribute is required](#gatewayattachment).
+ Override default parallelism when creating, updating, or deleting resources. CloudFormation creates, updates, and deletes resources in parallel to the extent possible. It automatically determines which resources in a template can be parallelized and which have dependencies that require other operations to finish first. You can use `DependsOn` to explicitly specify dependencies, which overrides the default parallelism and directs CloudFormation to operate on those resources in a specified order.

**Note**  
During a stack update, resources that depend on updated resources are updated automatically. CloudFormation makes no changes to the automatically updated resources, but, if a stack policy is associated with these resources, your account must have the permissions to update them.

## Syntax
<a name="aws-attribute-dependson-syntax"></a>

The `DependsOn` attribute can take a single string or list of strings.

```
"DependsOn" : [ {{String, ...}} ]
```

## Example
<a name="aws-attribute-dependson-example"></a>

The following template contains an [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html) resource with a `DependsOn` attribute that specifies `myDB`, an [AWS::RDS::DBInstance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html). When CloudFormation creates this stack, it first creates `myDB`, then creates `Ec2Instance`.

### JSON
<a name="aws-attribute-dependson-example-1.json"></a>

```
 1. {
 2.     "Resources" : {
 3.         "Ec2Instance" : {
 4.             "Type" : "AWS::EC2::Instance",
 5.             "Properties" : {
 6.                 "ImageId": "{{resolve:ssm:/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64}}",
 7.                 "InstanceType": "t2.micro"
 8.             },
 9.             "DependsOn" : "myDB"
10.         },
11.         "myDB" : {
12.             "Type" : "AWS::RDS::DBInstance",
13.             "Properties" : {
14.                "AllocatedStorage" : "5",
15.                "DBInstanceClass" : "db.t2.small",
16.                "Engine" : "MySQL",
17.                "EngineVersion" : "5.5",
18.                "MasterUsername" : "{{resolve:secretsmanager:{{MySecret}}:SecretString:{{username}}}}",
19.                "MasterUserPassword" : "{{resolve:secretsmanager:{{MySecret}}:SecretString:{{password}}}}"
20.             }
21.         }
22.     }
23. }
```

### YAML
<a name="aws-attribute-dependson-example-1.yaml"></a>

```
 1. Resources:
 2.   Ec2Instance:
 3.     Type: AWS::EC2::Instance
 4.     Properties:
 5.       ImageId: '{{resolve:ssm:/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64}}'
 6.       InstanceType: t2.micro
 7.     DependsOn: myDB
 8.   myDB:
 9.     Type: AWS::RDS::DBInstance
10.     Properties:
11.       AllocatedStorage: '5'
12.       DBInstanceClass: db.t2.small
13.       Engine: MySQL
14.       EngineVersion: '5.5'
15.       MasterUsername: '{{resolve:secretsmanager:{{MySecret}}:SecretString:{{username}}}}'
16.       MasterUserPassword: '{{resolve:secretsmanager:{{MySecret}}:SecretString:{{password}}}}'
```

## When a `DependsOn` attribute is required
<a name="gatewayattachment"></a>

VPC-gateway attachment

Some resources in a VPC require a gateway (either an Internet or VPN gateway). If your CloudFormation template defines a VPC, a gateway, and a gateway attachment, any resources that require the gateway are dependent on the gateway attachment. For example, an Amazon EC2 instance with a public IP address is dependent on the VPC-gateway attachment if the `VPC` and `InternetGateway` resources are also declared in the same template.

Currently, the following resources depend on a VPC-gateway attachment when they have an associated public IP address and are in a VPC.
+ Auto Scaling groups
+ Amazon EC2 instances
+ Elastic Load Balancing load balancers
+ Elastic IP addresses
+ Amazon RDS database instances
+ Amazon VPC routes that include the Internet gateway

A VPN gateway route propagation depends on a VPC-gateway attachment when you have a VPN gateway.

The following snippet shows a sample gateway attachment and an Amazon EC2 instance that depends on a gateway attachment:

### JSON
<a name="aws-attribute-dependson-example-2.json"></a>

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
<a name="aws-attribute-dependson-example-2.yaml"></a>

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

### Amazon ECS service and Auto Scaling group
<a name="w2aac19c19c17c19"></a>

When you use Auto Scaling or Amazon Elastic Compute Cloud (Amazon EC2) to create container instances for an Amazon ECS cluster, the Amazon ECS service resource must have a dependency on the Auto Scaling group or Amazon EC2 instances, as shown in the following snippet. That way the container instances are available and associated with the Amazon ECS cluster before CloudFormation creates the Amazon ECS service.

#### JSON
<a name="aws-attribute-dependson-example-3.json"></a>

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
<a name="aws-attribute-dependson-example-3.yaml"></a>

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
<a name="w2aac19c19c17c21"></a>

Resources that make additional calls to AWS require a service role, which permits a service to make calls to AWS on your behalf. For example, the `AWS::CodeDeploy::DeploymentGroup` resource requires a service role so that CodeDeploy has permissions to deploy applications to your instances. When you have a single template that defines a service role, the role's policy (by using the `AWS::IAM::Policy` or `AWS::IAM::ManagedPolicy` resource), and a resource that uses the role, add a dependency so that the resource depends on the role's policy. This dependency ensures that the policy is available throughout the resource's lifecycle.

For example, imagine that you have a template with a deployment group resource, a service role, and the role's policy. When you create a stack, CloudFormation won't create the deployment group until it creates the role's policy. Without the dependency, CloudFormation can create the deployment group resource before it creates the role's policy. If that happens, the deployment group will fail to create because of insufficient permissions.

If the role has an embedded policy, don't specify a dependency. CloudFormation creates the role and its policy at the same time.