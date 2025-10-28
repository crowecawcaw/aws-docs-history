# How to migrate from ECS AL2 to ECS AL2023

AL2023 is a Linux-based operating system designed to provide a
secure, stable, and high-performance environment for your cloud applications. For more
information about the differences between AL2 and AL2023 see [Compare Amazon Linux 2023 and Amazon Linux
2](../../../linux/al2023/ug/compare-with-al2.md "../../../linux/al2023/ug/compare-with-al2.md") in the _Amazon Linux 2023 User Guide_.

Starting in January 2026, AWS Batch will change the default AMI for new Amazon ECS compute
environments from Amazon Linux 2 to Amazon Linux 2023 because AWS will be [ending support for Amazon Linux 2](https://aws.amazon.com/amazon-linux-2/faqs/ "https://aws.amazon.com/amazon-linux-2/faqs/").
The default AMI is used when you don't specify a value for the [imageType.Ec2Configuration](../APIReference/API_Ec2Configuration.md "../APIReference/API_Ec2Configuration.md")
field when creating a new compute environment. We recommend migrating AWS Batch Amazon ECS compute
environments to Amazon Linux 2023 to maintain optimal performance and security.

Depending on how your compute environment is configured you can use one of the following
upgrade paths from AL2 to AL2023.

###### Upgrade using Ec2Configuration.ImageType

- If you are not using a launch template or launch template overrides then change [Ec2Configuration.ImageType](../APIReference/API_Ec2Configuration.md#Batch-Type-Ec2Configuration-imageType "../APIReference/API_Ec2Configuration.md#Batch-Type-Ec2Configuration-imageType") to `ECS_AL2023` (or
  `ECS_AL2023_NVIDIA` when using GPU instances) and
  then run [UpdateComputeEnvironment](../APIReference/API_UpdateComputeEnvironment.md "../APIReference/API_UpdateComputeEnvironment.md").
- If you specify an [Ec2Configuration.ImageIdOverride](../APIReference/API_Ec2Configuration.md#Batch-Type-Ec2Configuration-imageIdOverride "../APIReference/API_Ec2Configuration.md#Batch-Type-Ec2Configuration-imageIdOverride") then [Ec2Configuration.ImageType](../APIReference/API_Ec2Configuration.md#Batch-Type-Ec2Configuration-imageType "../APIReference/API_Ec2Configuration.md#Batch-Type-Ec2Configuration-imageType") must match the AMI type specified
  in [Ec2Configuration.ImageIdOverride](../APIReference/API_Ec2Configuration.md#Batch-Type-Ec2Configuration-imageIdOverride "../APIReference/API_Ec2Configuration.md#Batch-Type-Ec2Configuration-imageIdOverride").

If you mismatch `ImageIdOverride` and `ImageType` then the compute
environment may not function properly.

###### Upgrade using launch templates

- If you use a launch template that specifies an AMI based on `ECS_AL2023`,
  ensure your launch template is compatible with Amazon Linux 2023. For information about changes
  in Amazon Linux 2023 for Amazon ECS-optimized AMI, see [Migrating from an Amazon
  Linux 2 to an Amazon Linux 2023 Amazon ECS-optimized AMI](../../../AmazonECS/latest/developerguide/al2-to-al2023-ami-transition.md "../../../AmazonECS/latest/developerguide/al2-to-al2023-ami-transition.md") in the _Amazon ECS
  User Guide_.
- For AL2023 AMIs, verify that any custom user data or initialization scripts are
  compatible with the AL2023 environment and package management system.

###### Upgrade using AWS CloudFormation

- If you use AWS CloudFormation to manage your compute environments, update your template to change the `ImageType` property in the `Ec2Configuration` from `ECS_AL2` to `ECS_AL2023` (or `ECS_AL2023_NVIDIA` when using GPU instances):

```
ComputeEnvironment:
  Type: AWS::Batch::ComputeEnvironment
  Properties:
    ComputeResources:
      Ec2Configuration:
        - ImageType: ECS_AL2023
```

Then update your AWS CloudFormation stack to apply the changes.

- If your AWS CloudFormation template specifies a custom AMI using `ImageIdOverride`, ensure the AMI ID corresponds to an AL2023-based AMI and matches the `ImageType` setting.

## Migration considerations

When migrating from Amazon Linux 2 to Amazon Linux 2023, consider the following:

- **Package management** – Amazon Linux 2023 uses
  `dnf` instead of `yum` for package management.
- **System services** – Some system services and their
  configurations may differ between AL2 and AL2023.
- **Container runtime** – Both AL2 and AL2023 support
  Docker, but AL2023 may have different default configurations.
- **Security** – AL2023 includes enhanced security features
  and may require updates to security-related configurations.
- **Instance Metadata Service Version 2 (IMDSv2)** – IMDSv2
  is a session-oriented service that requires token-based authentication to access EC2
  instance metadata, providing enhanced security. For more information about IMDS see and
  [How Instance Metadata Service Version 2 works](../../../configuring-instance-metadata-service.md#instance-metadata-v2-how-it-works "../../../configuring-instance-metadata-service.md#instance-metadata-v2-how-it-works") in the
  _Amazon EC2 User Guide_.

For a comprehensive list of changes and migration considerations, see [Migrating from an Amazon
Linux 2 to an Amazon Linux 2023 Amazon ECS-optimized AMI](../../../AmazonECS/latest/developerguide/al2-to-al2023-ami-transition.md "../../../AmazonECS/latest/developerguide/al2-to-al2023-ami-transition.md") in the _Amazon ECS
User Guide_.
