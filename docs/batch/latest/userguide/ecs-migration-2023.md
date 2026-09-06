

# How to migrate from ECS AL2 to ECS AL2023
<a name="ecs-migration-2023"></a>

AL2023 is a Linux-based operating system designed to provide a secure, stable, and high-performance environment for your cloud applications. For more information about the differences between AL2 and AL2023 see [Compare Amazon Linux 2023 and Amazon Linux 2](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html) in the *Amazon Linux 2023 User Guide*.

**Important**  
Effective June 30, 2026, AWS Batch will block creation of new Amazon ECS compute environments using Batch-provided Amazon Linux 2 AMIs. We strongly recommend migrating your existing AWS Batch Amazon ECS compute environments to Amazon Linux 2023 prior to this date. For more information, see [Amazon ECS Amazon Linux 2 AMI deprecation](ecs-al2-ami-deprecation.md).

On January 12, 2026, AWS Batch changed the default AMI for new Amazon ECS compute environments from Amazon Linux 2 to Amazon Linux 2023 because AWS is [ending support for Amazon Linux 2](https://aws.amazon.com/amazon-linux-2/faqs/). The default AMI is used when you don't specify a value for the [imageType.Ec2Configuration](https://docs.aws.amazon.com/batch/latest/APIReference/API_Ec2Configuration.html) field when creating a new compute environment. We recommend migrating AWS Batch Amazon ECS compute environments to Amazon Linux 2023 to maintain optimal performance and security.

You can track the migration status of your affected Amazon ECS compute environments using AWS Health planned lifecycle events. For more information, see [AWS Health Planned lifecycle events](batch-planned-lifecycle-events.md).

Depending on how your compute environment is configured you can use one of the following upgrade paths from AL2 to AL2023.

**Upgrade using Ec2Configuration.ImageType**
+ If you are not using a launch template or launch template overrides then change [Ec2Configuration.ImageType](https://docs.aws.amazon.com/batch/latest/APIReference/API_Ec2Configuration.html#Batch-Type-Ec2Configuration-imageType) to `ECS_AL2023` (or `ECS_AL2023_NVIDIA` when using GPU instances) and then run [UpdateComputeEnvironment](https://docs.aws.amazon.com/batch/latest/APIReference/API_UpdateComputeEnvironment.html). 
+ If you specify an [Ec2Configuration.ImageIdOverride](https://docs.aws.amazon.com/batch/latest/APIReference/API_Ec2Configuration.html#Batch-Type-Ec2Configuration-imageIdOverride) then [Ec2Configuration.ImageType](https://docs.aws.amazon.com/batch/latest/APIReference/API_Ec2Configuration.html#Batch-Type-Ec2Configuration-imageType) must match the AMI type specified in [Ec2Configuration.ImageIdOverride](https://docs.aws.amazon.com/batch/latest/APIReference/API_Ec2Configuration.html#Batch-Type-Ec2Configuration-imageIdOverride). 

  If you mismatch `ImageIdOverride` and `ImageType` then the compute environment may not function properly. 

**Upgrade using launch templates**
+ If you use a launch template that specifies an AMI based on `ECS_AL2023`, ensure your launch template is compatible with Amazon Linux 2023. For information about changes in Amazon Linux 2023 for Amazon ECS-optimized AMI, see [Migrating from an Amazon Linux 2 to an Amazon Linux 2023 Amazon ECS-optimized AMI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/al2-to-al2023-ami-transition.html) in the *Amazon ECS User Guide*.
+ For AL2023 AMIs, verify that any custom user data or initialization scripts are compatible with the AL2023 environment and package management system.

**Upgrade using CloudFormation**
+ If you use CloudFormation to manage your compute environments, update your template to change the `ImageType` property in the `Ec2Configuration` from `ECS_AL2` to `ECS_AL2023` (or `ECS_AL2023_NVIDIA` when using GPU instances):

  ```
  ComputeEnvironment:
    Type: AWS::Batch::ComputeEnvironment
    Properties:
      ComputeResources:
        Ec2Configuration:
          - ImageType: ECS_AL2023
  ```

  Then update your CloudFormation stack to apply the changes.
+ If your CloudFormation template specifies a custom AMI using `ImageIdOverride`, ensure the AMI ID corresponds to an AL2023-based AMI and matches the `ImageType` setting.

## Migration considerations
<a name="ecs-migration-considerations"></a>

When migrating from Amazon Linux 2 to Amazon Linux 2023, consider the following:
+ **Package management** – Amazon Linux 2023 uses `dnf` instead of `yum` for package management.
+ **System services** – Some system services and their configurations may differ between AL2 and AL2023.
+ **Container runtime** – Both AL2 and AL2023 support Docker, but AL2023 may have different default configurations.
+ **Security** – AL2023 includes enhanced security features and may require updates to security-related configurations.
+ **Instance Metadata Service Version 2 (IMDSv2)** – IMDSv2 is a session-oriented service that requires token-based authentication to access EC2 instance metadata, providing enhanced security. For more information about IMDS, see [How Instance Metadata Service Version 2 works](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html#instance-metadata-v2-how-it-works) in the *Amazon EC2 User Guide*.

For a comprehensive list of changes and migration considerations, see [Migrating from an Amazon Linux 2 to an Amazon Linux 2023 Amazon ECS-optimized AMI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/al2-to-al2023-ami-transition.html) in the *Amazon ECS User Guide*.