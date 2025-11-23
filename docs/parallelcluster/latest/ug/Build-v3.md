# `Build` section

**(Required)** Specifies the configuration in which the image will be built.

```
Build:
  Imds:
    ImdsSupport: `string`
  InstanceType: `string`
  SubnetId: `string`
  ParentImage: `string`
  Iam:
    InstanceRole: `string`
    InstanceProfile: `string`
    CleanupLambdaRole: `string`
    AdditionalIamPolicies:
      - Policy: `string`
    PermissionsBoundary: `string`
  Components:
    - Type: `string`
      Value: `string`
  Tags:
    - Key: `string`
      Value: `string`
  SecurityGroupIds:
    - `string`
  UpdateOsPackages:
    Enabled: `boolean`
  Installation:
    NvidiaSoftware:
      Enabled: `boolean`
    LustreClient:
      Enabled: `boolean`
```

## `Build` properties

`InstanceType`
(**Required**, `String`)

Specifies the instance type for the instance used to build the image.

`SubnetId`
(**Optional**, `String`)

Specifies the ID of an existing subnet in which to provision the instance to
build the image. The provided subnet requires internet access. Note that you might
need to [Modify the IP addressing attributes of your subnet](../../../vpc/latest/userguide/subnet-public-ip.md "../../../vpc/latest/userguide/subnet-public-ip.md") if the build fails.

###### Warning

`pcluster build-image` uses the default VPC. If the default VPC
has been deleted, perhaps by using AWS Control Tower or AWS Landing Zone, then
the subnet ID must be specified.

When you specify the SubnetId, it is recommended to specify the SecurityGroupIds property
as well. If you leave SecurityGroupIds out, AWS ParallelCluster will use default security
groups or rely on the default behavior within the specified subnet. When you use both, you
gain these advantages:

- Granular control: When you explicitly define both you ensure the instances launched
  during the image build process are placed in the correct subnet and have the precise
  network access you need for your build components and any required services (like access
  to S3 for build scripts).
- Security best practices: When you define appropriate security groups this helps restrict
  network access to only necessary ports and services, which enhances the security of your
  build environment.
- Avoiding potential issues: If you rely solely on defaults this might result in security
  groups that are too open or too restrictive, which can lead to problems during the build
  process.

`ParentImage`
(**Required**, `String`)

Specifies the base image. The parent image can be either a non AWS ParallelCluster
AMI or an official AWS ParallelCluster AMI for the same version. You can't use a
AWS ParallelCluster official or custom AMI from a different version of AWS ParallelCluster.
The format must either be the ARN of a image
`arn:`Partition`:imagebuilder:`Region`:`Account`:image/`ImageName`/`ImageVersion`` or an AMI ID`ami-12345678`.

`SecurityGroupIds`
(**Optional**, `[String]`)

Specifies the list of security group IDs for the image.

### `Imds`

#### `Imds` properties

**(Optional)** Specifies the Amazon EC2 ImageBuilder build and test instance metadata service (IMDS) settings.

```
Imds:
  ImdsSupport: `string`
```

`ImdsSupport` (**Optional**, `String`)

Specifies which IMDS versions are supported in the Amazon EC2 ImageBuilder build and test instances. Supported values
are `v2.0` and `v1.0`. The default value is `v2.0`.

If `ImdsSupport` is set to `v1.0`, both IMDSv1 and IMDSv2 are supported.

If `ImdsSupport` is set to `v2.0`, only IMDSv2 is supported.

For more information, see [Use IMDSv2](../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md "../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md")
in the _Amazon EC2 User Guide for Linux instances_.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

###### Note

Starting with AWS ParallelCluster version 3.7.0, the `ImdsSupport` default value is `v2.0`. We recommend that you set
`ImdsSupport` to `v2.0` and replace IMDSv1 with IMDSv2 in your custom actions calls.

Support for [Imds](#Build-v3-Imds "#Build-v3-Imds") / [ImdsSupport](#yaml-build-image-Build-Imds-ImdsSupport "#yaml-build-image-Build-Imds-ImdsSupport")
is added with AWS ParallelCluster version 3.3.0.

### `Iam`

#### `Iam` properties

(**Optional**) Specifies the IAM resources for the image build.

```
Iam:
  InstanceRole: `string`
  InstanceProfile: `string`
  CleanupLambdaRole: `string`
  AdditionalIamPolicies:
    - Policy: `string`
  PermissionsBoundary: `string`
```

`InstanceProfile` (**Optional**, `String`)

Specifies an instance profile to override the default instance profile for the EC2 Image Builder instance.
`InstanceProfile` and `InstanceRole` and `AdditionalIamPolicies` cannot be
specified together. The format is
`arn:`Partition`:iam::`Account`:instance-profile/`InstanceProfileName``.

`InstanceRole` (**Optional**, `String`)

Specifies an instance role to override the default instance role for the EC2 Image Builder instance.
`InstanceProfile` and `InstanceRole` and `AdditionalIamPolicies` cannot be
specified together. The format is
`arn:`Partition`:iam::`Account`:role/`RoleName``.

`CleanupLambdaRole` (**Optional**, `String`)

The ARN of the IAM role to use for the AWS Lambda function that backs the CloudFormation custom resource that removes
build artifacts on build completion. Lambda needs to be configured as the principal allowed to assume the role.
The format is `arn:`Partition`:iam::`Account`:role/`RoleName``.

`AdditionalIamPolicies` (**Optional**)

Specifies additional IAM policies to attach to the EC2 Image Builder instance used to produce the custom
AMI.

```
AdditionalIamPolicies:
  - Policy: `string`
```

`Policy` (**Optional**, `[String]`)

List of IAM policies. The format is
`arn:`Partition`:iam::`Account`:policy/`PolicyName``.

`PermissionsBoundary` (**Optional**,
`String`)

The ARN of the IAM policy to use as permissions boundary for all roles created by AWS ParallelCluster. For
more information on IAM permissions boundaries please refer to [Permissions boundaries for IAM entities](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md") in
the _IAM User Guide_. The format is
`arn:`Partition`:iam::`Account`:policy/`PolicyName``.

### `Components`

#### `Components` properties

(**Optional**) Specifies Amazon EC2 ImageBuilder components to use during the AMI build
process in addition to the ones provided by default by AWS ParallelCluster. Such components can be used to customize
the AMI build process. For more information, see [AWS ParallelCluster AMI customization](custom-ami-v3.md "custom-ami-v3.md").

```
Components:
  - Type: `string`
    Value: `string`
```

`Type` (**Optional**, `String`)

Specifies the type of the type-value pair for the component. Type can be `arn` or
`script`.

`Value` (**Optional**, `String`)

Specifies the value of the type-value pair for the component. When type is `arn`, this is the
ARN of a EC2 Image Builder component. When type is `script`, this is the https or s3 link that points to the
script to use when you create the EC2 Image Builder component.

### `Tags`

#### `Tags` properties

(**Optional**) Specifies the list of tags to be set in the resources used to
build the AMI.

```
Tags:
  - Key: `string`
    Value: `string`
```

`Key` (**Optional**,
`String`)

Defines the name of the tag.

`Value` (**Optional**, `String`)

Defines the value of the tag.

### `UpdateOsPackages`

#### `UpdateOsPackages` properties

(**Optional**) Specifies whether the operating system is updated before
installing AWS ParallelCluster software stack.

```
UpdateOsPackages:
  Enabled: `boolean`
```

`Enabled` (**Optional**, `Boolean`)

If `true`, the OS is updated and rebooted before installing the AWS ParallelCluster software. The
default is `false`.

###### Note

When `UpdateOsPackages` is enabled, all available OS packages are updated, including the kernel. As a customer, it is your
responsibility to verify that the update is compatible with the AMI dependencies that aren't included in the update.

For example, suppose you want to build an AMI for AWS ParallelCluster version X.0 that's shipped with kernel version Y.0 and some component version Z.0.
Suppose the available update includes updated kernel version Y.1 without updates to component Z.0. Before you enable
`UpdateOsPackages`, it's your responsibility to verify that component Z.0 supports kernel Y.1.

### `Installation`

#### `Installation` properties

**(Optional)** Specifies additional software to be installed on the image.

```
Installation:
  NvidiaSoftware:
    Enabled: `boolean`
  LustreClient:
    Enabled: `boolean`
```

`NvidiaSoftware` properties
(**Optional**)

Specifies the Nvidia Software to be installed.

```
NvidiaSoftware:
    Enabled: `boolean`
```

`Enabled`
(**Optional**, `boolean`)

If `true`, the Nvidia GPU driver and CUDA will be installed. The default is `false`.

`LustreClient` properties
(**Optional**)

Specifies that the Amazon FSx Lustre client will be installed.

```
LustreClient:
    Enabled: `boolean`
```

`Enabled`
(**Optional**, `boolean`)

If `true`, the Lustre client will be installed. The default is `true`.
