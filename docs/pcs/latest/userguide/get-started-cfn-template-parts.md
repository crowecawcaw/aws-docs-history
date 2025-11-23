# Parts of a CloudFormation template for AWS PCS

A CloudFormation template has 1 or more sections that each serve a specific purpose.
CloudFormation defines standard format, syntax, and language in a template. For more information,
see [Working
with CloudFormation templates](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md") in the _AWS CloudFormation User Guide_.

CloudFormation templates are highly customizable and therefore their formats can vary.
To understand the necessary parts of a CloudFormation template to create an AWS PCS cluster,
we recommend you examine the sample template we provide to create a sample cluster. This topic
briefly explains the sections of that sample template.

###### Important

The code samples in this topic are **not complete**.
The presence of ellipsis (`[...]`) indicates that there is additional code
that isn't displayed. To download the complete YAML-formatted CloudFormation template, see
[CloudFormation templates to create a sample AWS PCS cluster](get-started-cfn-sample-templates.md "get-started-cfn-sample-templates.md").

###### Contents

- [Header](get-started-cfn-template-parts.md#get-started-cfn-template-parts-header "get-started-cfn-template-parts.md#get-started-cfn-template-parts-header")
- [Metadata](get-started-cfn-template-parts.md#get-started-cfn-template-parts-metadata "get-started-cfn-template-parts.md#get-started-cfn-template-parts-metadata")
- [Parameters](get-started-cfn-template-parts.md#get-started-cfn-template-parts-parameters "get-started-cfn-template-parts.md#get-started-cfn-template-parts-parameters")
- [Mappings](get-started-cfn-template-parts.md#get-started-cfn-template-parts-mappings "get-started-cfn-template-parts.md#get-started-cfn-template-parts-mappings")
- [Resources](get-started-cfn-template-parts.md#get-started-cfn-template-parts-resources "get-started-cfn-template-parts.md#get-started-cfn-template-parts-resources")
- [Outputs](get-started-cfn-template-parts.md#get-started-cfn-template-parts-outputs "get-started-cfn-template-parts.md#get-started-cfn-template-parts-outputs")

## Header

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: AWS Parallel Computing Service "getting started" cluster
```

`AWSTemplateFormatVersion` identifies the template format version
that the template conforms to. For more information, see
[CloudFormation
template format version syntax](../../../AWSCloudFormation/latest/UserGuide/format-version-structure.md "../../../AWSCloudFormation/latest/UserGuide/format-version-structure.md") in the _AWS CloudFormation User Guide_.

`Transform` specifies a macro that CloudFormation uses
to process the template. For more information, see
[CloudFormation
template Transform section](../../../AWSCloudFormation/latest/UserGuide/transform-section-structure.md "../../../AWSCloudFormation/latest/UserGuide/transform-section-structure.md") in the _AWS CloudFormation User Guide_.
The `AWS::Serverless-2016-10-31` transform enables CloudFormation to process a template
written in the AWS Serverless Application Model (AWS SAM) syntax. For more information, see
[`AWS::Serverless`
transform](../../../AWSCloudFormation/latest/UserGuide/transform-aws-serverless.md "../../../AWSCloudFormation/latest/UserGuide/transform-aws-serverless.md") in the _AWS CloudFormation User Guide_.

## Metadata

```
### Stack metadata
Metadata:
  AWS::CloudFormation::Interface:
    ParameterGroups:
      - Label:
          default: PCS Cluster configuration
        Parameters:
          - SlurmVersion
          - ManagedAccounting
          - AccountingPolicyEnforcement
      - Label:
          default: PCS ComputeNodeGroups configuration
        Parameters:
          - NodeArchitecture
          - KeyName
          - ClientIpCidr
      - Label:
          default: HPC Recipes configuration
        Parameters:
          - HpcRecipesS3Bucket
          - HpcRecipesBranch
```

The `metadata` section of a CloudFormation template provides information about the
template itself. The sample template creates a complete high performance computing (HPC)
cluster that uses AWS PCS. The metadata section of the sample template declares parameters
that control how CloudFormation launches (provisions) the corresponding stack.
There are parameters that control architecture choice (`NodeArchitecture`),
Slurm version (`SlurmVersion`), and access controls
(`KeyName` and `ClientIpCidr`).

## Parameters

The `Parameters` section defines the custom parameters for the template.
CloudFormation uses these parameter definitions to construct and validate the form that you interact
with when you launch a stack from this template.

```
Parameters:

  NodeArchitecture:
    Type: String
    Default: x86
    AllowedValues:
      - x86
      - Graviton
    Description: Processor architecture for the login and compute node instances

  SlurmVersion:
    Type: String
    Default: 25.05
    Description: Version of Slurm to use
    AllowedValues:
         - 24.05
         - 24.11
         - 25.05

  ManagedAccounting:
    Type: String
    Default: 'disabled'
    AllowedValues:
      - 'enabled'
      - 'disabled'
    Description: Monitor cluster usage, manage access control, and enforce resource limits with Slurm accounting. Requires Slurm 24.11 or newer.

  AccountingPolicyEnforcement:
    Description: Specify which Slurm accounting policies to enforce
    Type: String
    Default: none
    AllowedValues:
      - none
      - 'associations,limits,safe'

  KeyName:
    Description: SSH keypair to log in to the head node
    Type: AWS::EC2::KeyPair::KeyName
    AllowedPattern: ".+"  # Required

  ClientIpCidr:
    Description: IP(s) allowed to access the login node over SSH. We recommend that you restrict it with your own IP/subnet (x.x.x.x/32 for your own ip or x.x.x.x/24 for range. Replace x.x.x.x with your own PUBLIC IP. You can get your public IP using tools such as https://ifconfig.co/)
    Default: 127.0.0.1/32
    Type: String
    AllowedPattern: (\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})/(\d{1,2})
    ConstraintDescription: Value must be a valid IP or network range of the form x.x.x.x/x.

  HpcRecipesS3Bucket:
    Type: String
    Default: aws-hpc-recipes
    Description: HPC Recipes for AWS S3 bucket
    AllowedValues:
         - aws-hpc-recipes
         - aws-hpc-recipes-dev
  HpcRecipesBranch:
    Type: String
    Default: main
    Description: HPC Recipes for AWS release branch
    AllowedPattern: '^(?!.*/\.git$)(?!.*/\.)(?!.*\\.\.)[a-zA-Z0-9-_\.]+$'
```

## Mappings

The `Mappings` section defines key-value pairs that specify
values based on certain conditions or dependencies.

```
Mappings:

  Architecture:
    AmiArchParameter:
      Graviton: arm64
      x86: x86_64
    LoginNodeInstances:
      Graviton: c7g.xlarge
      x86: c6i.xlarge
    ComputeNodeInstances:
      Graviton: c7g.xlarge
      x86: c6i.xlarge
```

## Resources

The `Resources` section declares the AWS resources
to provision and configure as part of the stack.

```
Resources:

  [...]

```

The template provisions the sample cluster infrastructure in layers.
It starts with `Networking` for VPC configuration.
Storage is provided by dual systems: `EfsStorage` for shared storage
and `FSxLStorage` for high-performance storage.
The core cluster is established through `PCSCluster`.

```

  Networking:
    Type: AWS::CloudFormation::Stack
    Properties:
      Parameters:
        ProvisionSubnetsC: "False"
      TemplateURL: !Sub 'https://${HpcRecipesS3Bucket}.s3.amazonaws.com/${HpcRecipesBranch}/recipes/net/hpc_large_scale/assets/main.yaml'

  EfsStorage:
    Type: AWS::CloudFormation::Stack
    Properties:
      Parameters:
        SubnetIds: !GetAtt [ Networking, Outputs.DefaultPrivateSubnet ]
        SubnetCount: 1
        VpcId: !GetAtt [ Networking, Outputs.VPC ]
      TemplateURL: !Sub 'https://${HpcRecipesS3Bucket}.s3.amazonaws.com/${HpcRecipesBranch}/recipes/storage/efs_simple/assets/main.yaml'

  FSxLStorage:
    Type: AWS::CloudFormation::Stack
    Properties:
      Parameters:
        PerUnitStorageThroughput: 125
        SubnetId: !GetAtt [ Networking, Outputs.DefaultPrivateSubnet ]
        VpcId: !GetAtt [ Networking, Outputs.VPC ]
      TemplateURL: !Sub 'https://${HpcRecipesS3Bucket}.s3.amazonaws.com/${HpcRecipesBranch}/recipes/storage/fsx_lustre/assets/persistent.yaml'

  [...]

  # Cluster
  PCSCluster:
    Type: AWS::PCS::Cluster
    Properties:
      Name: !Sub '${AWS::StackName}'
      Size: SMALL
      Scheduler:
        Type: SLURM
        Version: !Ref SlurmVersion
      Networking:
        SubnetIds:
          - !GetAtt [ Networking, Outputs.DefaultPrivateSubnet ]
        SecurityGroupIds:
          - !GetAtt [ PCSSecurityGroup, Outputs.ClusterSecurityGroupId ]

```

For compute resources, the template creates two node groups:
`PCSNodeGroupLogin` for a single login node and
`PCSNodeGroupCompute` for up to four compute nodes.
These node groups are supported by
`PCSInstanceProfile` for permissions and
`PCSLaunchTemplate` for instance configurations.

```

  # Compute Node groups
  PCSInstanceProfile:
    Type: AWS::CloudFormation::Stack
    Properties:
      Parameters:
        # We have to regionalize this in case CX use the template in more than one region. Otherwise,
        # the create action will fail since instance-role-${AWS::StackName} already exists!
        RoleName: !Sub '${AWS::StackName}-${AWS::Region}'
      TemplateURL: !Sub 'https://${HpcRecipesS3Bucket}.s3.amazonaws.com/${HpcRecipesBranch}/recipes/pcs/getting_started/assets/pcs-iip-minimal.yaml'

  PCSLaunchTemplate:
    Type: AWS::CloudFormation::Stack
    Properties:
      Parameters:
        VpcDefaultSecurityGroupId: !GetAtt [ Networking, Outputs.SecurityGroup ]
        ClusterSecurityGroupId: !GetAtt [ PCSSecurityGroup, Outputs.ClusterSecurityGroupId ]
        SshSecurityGroupId: !GetAtt [ PCSSecurityGroup, Outputs.InboundSshSecurityGroupId ]
        EfsFilesystemSecurityGroupId: !GetAtt [ EfsStorage, Outputs.SecurityGroupId ]
        FSxLustreFilesystemSecurityGroupId: !GetAtt [ FSxLStorage, Outputs.FSxLustreSecurityGroupId ]
        SshKeyName: !Ref KeyName
        EfsFilesystemId: !GetAtt [ EfsStorage, Outputs.EFSFilesystemId ]
        FSxLustreFilesystemId: !GetAtt [ FSxLStorage, Outputs.FSxLustreFilesystemId ]
        FSxLustreFilesystemMountName: !GetAtt [ FSxLStorage, Outputs.FSxLustreMountName ]
      TemplateURL: !Sub 'https://${HpcRecipesS3Bucket}.s3.amazonaws.com/${HpcRecipesBranch}/recipes/pcs/getting_started/assets/cfn-pcs-lt-efs-fsxl.yaml'

  # Compute Node groups - Login Nodes
  PCSNodeGroupLogin:
    Type: AWS::PCS::ComputeNodeGroup
    Properties:
      ClusterId: !GetAtt [PCSCluster, Id]
      Name: login
      ScalingConfiguration:
        MinInstanceCount: 1
        MaxInstanceCount: 1
      IamInstanceProfileArn: !GetAtt [ PCSInstanceProfile, Outputs.InstanceProfileArn ]
      CustomLaunchTemplate:
        TemplateId: !GetAtt [ PCSLaunchTemplate, Outputs.LoginLaunchTemplateId ]
        Version: 1
      SubnetIds:
        - !GetAtt [ Networking, Outputs.DefaultPublicSubnet ]
      AmiId: !GetAtt [PcsSampleAmi, AmiId]
      InstanceConfigs:
        - InstanceType: !FindInMap [ Architecture, LoginNodeInstances, !Ref NodeArchitecture ]

  # Compute Node groups - Compute Nodes
  PCSNodeGroupCompute:
    Type: AWS::PCS::ComputeNodeGroup
    Properties:
      ClusterId: !GetAtt [PCSCluster, Id]
      Name: compute-1
      ScalingConfiguration:
        MinInstanceCount: 0
        MaxInstanceCount: 4
      IamInstanceProfileArn: !GetAtt [ PCSInstanceProfile, Outputs.InstanceProfileArn ]
      CustomLaunchTemplate:
        TemplateId: !GetAtt [ PCSLaunchTemplate, Outputs.ComputeLaunchTemplateId ]
        Version: 1
      SubnetIds:
        - !GetAtt [ Networking, Outputs.DefaultPrivateSubnet ]
      AmiId: !GetAtt [PcsSampleAmi, AmiId]
      InstanceConfigs:
        - InstanceType: !FindInMap [ Architecture, ComputeNodeInstances, !Ref NodeArchitecture ]

```

Job scheduling is handled through `PCSQueueCompute`.

```

  PCSQueueCompute:
    Type: AWS::PCS::Queue
    Properties:
      ClusterId: !GetAtt [PCSCluster, Id]
      Name: demo
      ComputeNodeGroupConfigurations:
        - ComputeNodeGroupId: !GetAtt [PCSNodeGroupCompute, Id]

```

AMI selection happens automatically through the PcsAMILookupFn Lambda function and related
resources.

```

  PcsAMILookupRole:
    Type: AWS::IAM::Role
    [...]

  PcsAMILookupFn:
    Type: AWS::Lambda::Function
    Properties:
      Runtime: python3.12
      Handler: index.handler
      Role: !GetAtt PcsAMILookupRole.Arn
      Code:
        [...]
      Timeout: 30
      MemorySize: 128

  # Example of using the custom resource to look up an AMI
  PcsSampleAmi:
    Type: Custom::AMILookup
    Properties:
      ServiceToken: !GetAtt PcsAMILookupFn.Arn
      OperatingSystem: 'amzn2'
      Architecture: !FindInMap [ Architecture, AmiArchParameter, !Ref NodeArchitecture ]
      SlurmVersion: !Ref SlurmVersion
```

## Outputs

The template outputs cluster identification and management URLs through
`ClusterId`, `PcsConsoleUrl`, and `Ec2ConsoleUrl`.

```
Outputs:
  ClusterId:
    Description: The Id of the PCS cluster
    Value: !GetAtt [ PCSCluster, Id ]

  PcsConsoleUrl:
    Description: URL to access the cluster in the PCS console
    Value: !Sub
      - https://${ConsoleDomain}/pcs/home?region=${AWS::Region}#/clusters/${ClusterId}
      - { ConsoleDomain: !If [ GovCloud, 'console.amazonaws-us-gov.com', !If [ China, 'console.amazonaws.cn', !Sub '${AWS::Region}.console.aws.amazon.com']],
          ClusterId: !GetAtt [ PCSCluster, Id ]
        }
    Export:
      Name: !Sub ${AWS::StackName}-PcsConsoleUrl

  Ec2ConsoleUrl:
    Description: URL to access instance(s) in the login node group via Session Manager
    Value: !Sub
      - https://${ConsoleDomain}/ec2/home?region=${AWS::Region}#Instances:instanceState=running;tag:aws:pcs:compute-node-group-id=${NodeGroupLoginId}
      - { ConsoleDomain: !If [ GovCloud, 'console.amazonaws-us-gov.com', !If [ China, 'console.amazonaws.cn', !Sub '${AWS::Region}.console.aws.amazon.com']],
          NodeGroupLoginId: !GetAtt [ PCSNodeGroupLogin, Id ]
        }
    Export:
      Name: !Sub ${AWS::StackName}-Ec2ConsoleUrl
```
