# Retrieving Amazon ECS-optimized Linux AMI

metadata

You can programmatically retrieve the Amazon ECS-optimized AMI metadata. The metadata
includes the AMI name, Amazon ECS container agent version, and Amazon ECS runtime version which
includes the Docker version.

When you create a cluster using the console, Amazon ECS creates a launch template for
your instances with the latest AMI associated with the selected operating system.

When you use AWS CloudFormation to create a cluster, the SSM parameter is part of the Amazon EC2
launch template for the Auto Scaling group instances. You can configure the template to use a
dynamic Systems Manager parameter to determine what Amazon ECS Optimized AMI to deploy. This
parameter ensures that each time you deploy the stack it will check to see if there
is available update that needs to be applied to the EC2 instances. For an example of
how to use the Systems Manager parameter, see [Create an Amazon ECS cluster with the Amazon ECS-optimized Amazon Linux 2023 AMI](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.md#aws-resource-ecs-cluster--examples--Create_an_cluster_with_the_Amazon_Linux_2023_ECS-Optimized-AMI "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.md#aws-resource-ecs-cluster--examples--Create_an_cluster_with_the_Amazon_Linux_2023_ECS-Optimized-AMI") in the _AWS CloudFormation User Guide_.

The AMI ID, image name, operating system, container agent version, source image
name, and runtime version for each variant of the Amazon ECS-optimized AMIs can be
programmatically retrieved by querying the Systems Manager Parameter Store API. For more
information about the Systems Manager Parameter Store API, see [GetParameters](../../../systems-manager/latest/APIReference/API_GetParameters.md "../../../systems-manager/latest/APIReference/API_GetParameters.md") and [GetParametersByPath](../../../systems-manager/latest/APIReference/API_GetParametersByPath.md "../../../systems-manager/latest/APIReference/API_GetParametersByPath.md").

###### Note

Your administrative user must have the following IAM permissions to retrieve the
Amazon ECS-optimized AMI metadata. These permissions have been added to the
`AmazonECS_FullAccess` IAM policy.

- ssm:GetParameters
- ssm:GetParameter
- ssm:GetParametersByPath

## Systems Manager Parameter Store parameter

format

The following is the format of the parameter name for each Amazon ECS-optimized AMI
variant.

**Linux Amazon ECS-optimized AMIs**

- Amazon Linux 2023 AMI metadata:

```
/aws/service/ecs/optimized-ami/amazon-linux-2023/`<version>`
```

- Amazon Linux 2023 (arm64) AMI metadata:

```
/aws/service/ecs/optimized-ami/amazon-linux-2023/arm64/`<version>`
```

- Amazon Linux 2023 (Neuron) AMI metadata:

```
/aws/service/ecs/optimized-ami/amazon-linux-2023/neuron/`<version>`
```

- Amazon Linux 2023 (GPU) AMI metadata:

```
/aws/service/ecs/optimized-ami/amazon-linux-2023/gpu/`<version>`
```

Amazon Linux 2 AMI metadata:

```
/aws/service/ecs/optimized-ami/amazon-linux-2/`<version>`
```

- Amazon Linux 2 kernel 5.10 AMI metadata:

```
/aws/service/ecs/optimized-ami/amazon-linux-2/kernel-5.10/`<version>`
```

- Amazon Linux 2 (arm64) AMI metadata:

```
/aws/service/ecs/optimized-ami/amazon-linux-2/arm64/`<version>`
```

- Amazon Linux 2 kernel 5.10 (arm64) AMI metadata:

```
/aws/service/ecs/optimized-ami/amazon-linux-2/kernel-5.10/arm64/`<version>`
```

- Amazon ECS GPU-optimized kernel 5.10 AMI metadata:

```
/aws/service/ecs/optimized-ami/amazon-linux-2/kernel-5.10/gpu/`<version>`
```

- Amazon Linux 2 (GPU) AMI metadata:

```
/aws/service/ecs/optimized-ami/amazon-linux-2/gpu/`<version>`
```

- Amazon ECS optimized Amazon Linux 2 (Neuron) kernel 5.10 AMI metadata:

```
/aws/service/ecs/optimized-ami/amazon-linux-2/kernel-5.10/inf/`<version>`
```

- Amazon Linux 2 (Neuron) AMI metadata:

```
/aws/service/ecs/optimized-ami/amazon-linux-2/inf/`<version>`
```

The following parameter name format retrieves the image ID of the latest
recommended Amazon ECS-optimized Amazon Linux 2 AMI by using the sub-parameter `image_id`.

```
/aws/service/ecs/optimized-ami/amazon-linux-2/`recommended/image_id`
```

The following parameter name format retrieves the metadata of a specific
Amazon ECS-optimized AMI version by specifying the AMI name.

- Amazon ECS-optimized Amazon Linux 2 AMI metadata:

```
/aws/service/ecs/optimized-ami/amazon-linux-2/`amzn2-ami-ecs-hvm-2.0.20181112-x86_64-ebs`
```

###### Note

All versions of the Amazon ECS-optimized Amazon Linux 2 AMI are available for retrieval. Only Amazon ECS-optimized
AMI versions `amzn-ami-2017.09.l-amazon-ecs-optimized` (Linux) and
later can be retrieved.

## Examples

The following examples show ways in which you can retrieve the metadata for each
Amazon ECS-optimized AMI variant.

### Retrieving the metadata

of the latest recommended Amazon ECS-optimized AMI

You can retrieve the latest recommended Amazon ECS-optimized AMI using the AWS CLI with
the following AWS CLI commands.

**Linux Amazon ECS-optimized AMIs**

- **For the Amazon ECS-optimized Amazon Linux 2023 AMIs:**

```
`aws ssm get-parameters --names /aws/service/ecs/optimized-ami/amazon-linux-2023/recommended --region `us-east-1``
```

- **For the Amazon ECS-optimized Amazon Linux 2023 (arm64) AMIs:**

```
`aws ssm get-parameters --names /aws/service/ecs/optimized-ami/amazon-linux-2023/arm64/recommended --region `us-east-1``
```

- **For the Amazon ECS-optimized Amazon Linux 2023 (Neuron) AMIs:**

```
`aws ssm get-parameters --names /aws/service/ecs/optimized-ami/amazon-linux-2023/neuron/recommended --region `us-east-1``
```

- **For the Amazon ECS-optimized Amazon Linux 2023 GPU AMIs:**

```
`aws ssm get-parameters --names /aws/service/ecs/optimized-ami/amazon-linux-2023/gpu/recommended --region `us-east-1``
```

- **For the Amazon ECS-optimized Amazon Linux 2 kernel 5.10 AMIs:**

```
`aws ssm get-parameters --names /aws/service/ecs/optimized-ami/amazon-linux-2/kernel-5.10/recommended --region `us-east-1``
```

- **For the Amazon ECS-optimized Amazon Linux 2 AMIs:**

```
`aws ssm get-parameters --names /aws/service/ecs/optimized-ami/amazon-linux-2/recommended --region `us-east-1``
```

- **For the Amazon ECS-optimized Amazon Linux 2 kernel 5.10 (arm64) AMIs:**

```
`aws ssm get-parameters --names /aws/service/ecs/optimized-ami/amazon-linux-2/kernel-5.10/arm64/recommended --region `us-east-1``
```

- **For the Amazon ECS-optimized Amazon Linux 2 (arm64) AMIs:**

```
`aws ssm get-parameters --names /aws/service/ecs/optimized-ami/amazon-linux-2/arm64/recommended --region `us-east-1``
```

- **For the Amazon ECS GPU-optimized kernel 5.10 AMIs:**

```
`aws ssm get-parameters --names /aws/service/ecs/optimized-ami/amazon-linux-2/kernel-5.10/gpu/recommended --region `us-east-1``
```

- **For the Amazon ECS GPU-optimized AMIs:**

```
`aws ssm get-parameters --names /aws/service/ecs/optimized-ami/amazon-linux-2/gpu/recommended --region `us-east-1``
```

- **For the Amazon ECS optimized Amazon Linux 2 (Neuron) kernel 5.10 AMIs:**

```
`aws ssm get-parameters --names /aws/service/ecs/optimized-ami/amazon-linux-2/kernel-5.10/inf/recommended --region `us-east-1``
```

- **For the Amazon ECS optimized Amazon Linux 2 (Neuron) AMIs:**

```
`aws ssm get-parameters --names /aws/service/ecs/optimized-ami/amazon-linux-2/inf/recommended --region `us-east-1``
```

### Retrieving the image ID

of the latest recommended Amazon ECS-optimized Amazon Linux 2023 AMI

You can retrieve the image ID of the latest recommended Amazon ECS-optimized Amazon Linux 2023 AMI ID by
using the sub-parameter `image_id`.

```
`aws ssm get-parameters --names /aws/service/ecs/optimized-ami/amazon-linux-2023/`recommended/image_id` --region `us-east-1``
```

To retrieve the `image_id` value only, you can query the specific
parameter value; for example:

```
`aws ssm get-parameters --names /aws/service/ecs/optimized-ami/amazon-linux-2023/recommended/`image_id` --region us-east-1 --query "`Parameters[0].Value`"`
```

### Retrieving the metadata

of a specific Amazon ECS-optimized Amazon Linux 2 AMI version

Retrieve the metadata of a specific Amazon ECS-optimized Amazon Linux AMI version using the AWS CLI with the
following AWS CLI command. Replace the AMI name with the name of the Amazon ECS-optimized Amazon Linux AMI to
retrieve.

```
`aws ssm get-parameters --names /aws/service/ecs/optimized-ami/amazon-linux-2/`amzn2-ami-ecs-hvm-2.0.20200928-x86_64-ebs` --region `us-east-1``
```

### Retrieving the

Amazon ECS-optimized Amazon Linux 2 kernel 5.10 AMI metadata using the Systems Manager GetParametersByPath API

Retrieve the Amazon ECS-optimized Amazon Linux 2 AMI metadata with the Systems Manager GetParametersByPath API using
the AWS CLI with the following command.

```
`aws ssm get-parameters-by-path --path /aws/service/ecs/optimized-ami/amazon-linux-2/kernel-5.10/ --region `us-east-1``
```

### Retrieving the image ID

of the latest recommended Amazon ECS-optimized Amazon Linux 2 kernel 5.10 AMI

You can retrieve the image ID of the latest recommended Amazon ECS-optimized Amazon Linux 2 kernel 5.10 AMI ID by
using the sub-parameter `image_id`.

```
`aws ssm get-parameters --names /aws/service/ecs/optimized-ami/amazon-linux-2/kernel-5.10/`recommended/image_id` --region `us-east-1``
```

To retrieve the `image_id` value only, you can query the specific
parameter value; for example:

```
`aws ssm get-parameters --names /aws/service/ecs/optimized-ami/amazon-linux-2/recommended/`image_id` --region us-east-1 --query "`Parameters[0].Value`"`
```

### Using the latest

recommended Amazon ECS-optimized AMI in an AWS CloudFormation template

You can reference the latest recommended Amazon ECS-optimized AMI in an AWS CloudFormation
template by referencing the Systems Manager parameter store name.

**Linux example**

```
Parameters:kernel-5.10
  LatestECSOptimizedAMI:
    Description: AMI ID
    Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
    Default: `/aws/service/ecs/optimized-ami/amazon-linux-2/kernel-5.10/recommended/image_id`
```
